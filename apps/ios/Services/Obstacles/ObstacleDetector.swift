import Foundation
import CoreVideo
import simd

/// Nearest obstacle per horizontal zone plus the direction of greatest clearance.
struct ObstacleZones: Equatable, Sendable {
    var left: Float?
    var center: Float?
    var right: Float?
    /// -1 means the clearest path is to the left, +1 to the right.
    var gapDirection: Float = 0
    var closest: Float? { [left, center, right].compactMap { $0 }.min() }

    static let empty = ObstacleZones()
}

/// Samples a LiDAR depth map on a coarse grid, splits it into left, center, and
/// right zones, filters floor pixels, and finds the clearest column.
///
/// The approach follows the Shepherd smart-cane detector
/// (github.com/tonywangs/shepherd): three zones, 16-column gap profiling, a
/// [0.25, 0.5, 0.25] smoothing kernel, and a running average on the gap direction.
/// The depth map arrives in landscape sensor orientation; the phone is mounted in
/// portrait, so raw x runs top-to-bottom on screen and raw y runs right-to-left.
struct ObstacleDetector {
    var minRange: Float = 0.2
    var maxRange: Float = 4.0
    /// Band of the frame to examine, as a fraction of the sensor's vertical axis.
    var verticalBand: ClosedRange<Float> = 0.35...0.65
    var sampleStep = 8
    var gapColumns = 16
    private var gapHistory: [Float] = []
    private let gapHistorySize = 5

    mutating func analyze(depthMap: CVPixelBuffer) -> ObstacleZones {
        CVPixelBufferLockBaseAddress(depthMap, .readOnly)
        defer { CVPixelBufferUnlockBaseAddress(depthMap, .readOnly) }
        guard let base = CVPixelBufferGetBaseAddress(depthMap) else { return .empty }

        let width = CVPixelBufferGetWidth(depthMap)
        let height = CVPixelBufferGetHeight(depthMap)
        let rowStride = CVPixelBufferGetBytesPerRow(depthMap) / MemoryLayout<Float32>.stride
        let buffer = base.assumingMemoryBound(to: Float32.self)

        var leftMin = Float.infinity
        var centerMin = Float.infinity
        var rightMin = Float.infinity
        var columnSum = [Float](repeating: 0, count: gapColumns)
        var columnCount = [Int](repeating: 0, count: gapColumns)

        let yStart = Int(Float(height) * verticalBand.lowerBound)
        let yEnd = Int(Float(height) * verticalBand.upperBound)

        for y in stride(from: yStart, to: yEnd, by: sampleStep) {
            for x in stride(from: 0, to: width, by: sampleStep) {
                let depth = buffer[y * rowStride + x]
                if depth.isNaN || depth.isInfinite || depth < minRange || depth > maxRange { continue }
                if isLikelyFloor(buffer, x: x, y: y, height: height, rowStride: rowStride) { continue }

                // Portrait mount: raw x increasing means display-right decreasing.
                let displayX = 1 - Float(x) / Float(width)
                let column = min(gapColumns - 1, max(0, Int(displayX * Float(gapColumns))))
                columnSum[column] += depth
                columnCount[column] += 1

                if displayX < 0.33 {
                    leftMin = min(leftMin, depth)
                } else if displayX < 0.67 {
                    centerMin = min(centerMin, depth)
                } else {
                    rightMin = min(rightMin, depth)
                }
            }
        }

        var averages = (0..<gapColumns).map { columnCount[$0] > 0 ? columnSum[$0] / Float(columnCount[$0]) : 0 }
        averages = (0..<gapColumns).map { i in
            let l = averages[max(0, i - 1)], c = averages[i], r = averages[min(gapColumns - 1, i + 1)]
            return 0.25 * l + 0.5 * c + 0.25 * r
        }
        // Direction of clearance is the centroid of every column within 10% of the
        // deepest one, so a wide open region pulls the direction toward its middle
        // and ties do not collapse to the leftmost column.
        let bestDepth = averages.max() ?? 0
        var rawGap: Float = 0
        if bestDepth > 0 {
            let threshold = bestDepth * 0.9
            var indexSum: Float = 0
            var clearCount: Float = 0
            for (i, value) in averages.enumerated() where value >= threshold {
                indexSum += Float(i)
                clearCount += 1
            }
            let centroid = clearCount > 0 ? indexSum / clearCount : Float(gapColumns - 1) / 2
            rawGap = (centroid / Float(gapColumns - 1) - 0.5) * 2
        }
        gapHistory.append(rawGap)
        if gapHistory.count > gapHistorySize { gapHistory.removeFirst() }
        let gap = gapHistory.reduce(0, +) / Float(gapHistory.count)

        return ObstacleZones(
            left: leftMin.isFinite ? leftMin : nil,
            center: centerMin.isFinite ? centerMin : nil,
            right: rightMin.isFinite ? rightMin : nil,
            gapDirection: gap
        )
    }

    /// Floor slopes away smoothly as the sample moves down the frame.
    private func isLikelyFloor(_ buffer: UnsafePointer<Float32>, x: Int, y: Int, height: Int, rowStride: Int) -> Bool {
        guard y + 8 < height else { return false }
        let current = buffer[y * rowStride + x]
        let below = buffer[(y + 8) * rowStride + x]
        let diff = below - current
        if diff > 0.5 && current > 1.0 { return true }
        if abs(diff) < 0.1 && Float(y) / Float(height) > 0.6 { return true }
        return false
    }
}
