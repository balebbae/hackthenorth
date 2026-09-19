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
    /// True when the sensor is so close to a surface it can barely measure it.
    var touching = false
    var closest: Float? { [left, center, right].compactMap { $0 }.min() }

    static let empty = ObstacleZones()
}

/// Samples a LiDAR depth map on a coarse grid, splits it into left, center, and
/// right zones, filters floor pixels, and finds the clearest column.
///
/// The gap-profiling approach follows the Shepherd smart-cane detector
/// (github.com/tonywangs/shepherd). Orientation is handled for a portrait mount:
/// ARKit delivers depth in landscape sensor orientation, so the sensor's long axis
/// (raw x) runs top to bottom on the screen and the short axis (raw y) runs right
/// to left. Left and right zones therefore come from raw y, and the height band
/// and floor filter work along raw x.
struct ObstacleDetector {
    /// Below this LiDAR cannot measure; such pixels are treated as touching.
    var minRange: Float = 0.2
    var maxRange: Float = 5.0
    /// Band of the view to examine, as a fraction of the screen's vertical axis
    /// (0 is the top of the view, 1 the bottom).
    var heightBand: ClosedRange<Float> = 0.35...0.65
    var sampleStep = 8
    var gapColumns = 16
    /// When most samples are unmeasurable and some are sub-minimum, the sensor is
    /// pressed against something.
    var touchingInvalidFraction: Float = 0.6
    var touchingCloseFraction: Float = 0.05
    private var gapHistory: [Float] = []
    private let gapHistorySize = 5

    mutating func analyze(depthMap: CVPixelBuffer) -> ObstacleZones {
        CVPixelBufferLockBaseAddress(depthMap, .readOnly)
        defer { CVPixelBufferUnlockBaseAddress(depthMap, .readOnly) }
        guard let base = CVPixelBufferGetBaseAddress(depthMap) else { return .empty }

        let width = CVPixelBufferGetWidth(depthMap)    // long axis: screen vertical
        let height = CVPixelBufferGetHeight(depthMap)  // short axis: screen horizontal
        let rowStride = CVPixelBufferGetBytesPerRow(depthMap) / MemoryLayout<Float32>.stride
        let buffer = base.assumingMemoryBound(to: Float32.self)

        var leftMin = Float.infinity
        var centerMin = Float.infinity
        var rightMin = Float.infinity
        var columnSum = [Float](repeating: 0, count: gapColumns)
        var columnCount = [Int](repeating: 0, count: gapColumns)
        var total = 0, invalid = 0, tooClose = 0

        let xStart = Int(Float(width) * heightBand.lowerBound)
        let xEnd = Int(Float(width) * heightBand.upperBound)

        for x in stride(from: xStart, to: xEnd, by: sampleStep) {
            for y in stride(from: 0, to: height, by: sampleStep) {
                total += 1
                let raw = buffer[y * rowStride + x]
                if raw.isNaN || raw.isInfinite || raw <= 0 {
                    invalid += 1
                    continue
                }
                // Raw top (y = 0) is the wearer's right after the portrait rotation.
                let displayX = 1 - Float(y) / Float(height)
                let column = min(gapColumns - 1, max(0, Int(displayX * Float(gapColumns))))

                if raw > maxRange {
                    // Beyond range is open space: full clearance for the gap profile,
                    // but not an obstacle for the zones.
                    columnSum[column] += maxRange
                    columnCount[column] += 1
                    continue
                }
                var depth = raw
                if depth < minRange {
                    tooClose += 1
                    depth = minRange
                } else if isLikelyFloor(buffer, x: x, y: y, width: width, rowStride: rowStride) {
                    continue
                }
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

        let touching = total > 0
            && Float(invalid) / Float(total) >= touchingInvalidFraction
            && Float(tooClose) / Float(total) >= touchingCloseFraction
        if touching {
            leftMin = min(leftMin, minRange)
            centerMin = min(centerMin, minRange)
            rightMin = min(rightMin, minRange)
        }

        var averages = (0..<gapColumns).map { columnCount[$0] > 0 ? columnSum[$0] / Float(columnCount[$0]) : 0 }
        averages = (0..<gapColumns).map { i in
            let l = averages[max(0, i - 1)], c = averages[i], r = averages[min(gapColumns - 1, i + 1)]
            return 0.25 * l + 0.5 * c + 0.25 * r
        }
        // Direction of clearance is the centroid of every column within 10% of the
        // deepest one, so a wide open region pulls the direction toward its middle.
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
            gapDirection: gap,
            touching: touching
        )
    }

    /// Floor slopes away smoothly as the sample moves down the screen, which is
    /// increasing raw x in the portrait mount.
    private func isLikelyFloor(_ buffer: UnsafePointer<Float32>, x: Int, y: Int, width: Int, rowStride: Int) -> Bool {
        guard x + 8 < width else { return false }
        let current = buffer[y * rowStride + x]
        let below = buffer[y * rowStride + x + 8]
        let diff = below - current
        if diff > 0.5 && current > 1.0 { return true }
        if abs(diff) < 0.1 && Float(x) / Float(width) > 0.6 { return true }
        return false
    }
}
