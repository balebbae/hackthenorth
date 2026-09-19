import XCTest
import CoreVideo
@testable import NavigationAssistant

final class ObstacleDetectorTests: XCTestCase {
    /// Builds a Float32 depth map in sensor (landscape) orientation.
    private func depthMap(width: Int = 256, height: Int = 192, fill: (Int, Int) -> Float) -> CVPixelBuffer {
        var buffer: CVPixelBuffer?
        CVPixelBufferCreate(kCFAllocatorDefault, width, height, kCVPixelFormatType_DepthFloat32, nil, &buffer)
        let map = buffer!
        CVPixelBufferLockBaseAddress(map, [])
        let stride = CVPixelBufferGetBytesPerRow(map) / MemoryLayout<Float32>.stride
        let base = CVPixelBufferGetBaseAddress(map)!.assumingMemoryBound(to: Float32.self)
        for y in 0..<height { for x in 0..<width { base[y * stride + x] = fill(x, y) } }
        CVPixelBufferUnlockBaseAddress(map, [])
        return map
    }

    func testOpenSceneHasNoObstacles() {
        var detector = ObstacleDetector()
        let zones = detector.analyze(depthMap: depthMap { _, _ in 6.0 })
        XCTAssertNil(zones.left); XCTAssertNil(zones.center); XCTAssertNil(zones.right)
    }

    func testWallAheadFillsAllZones() {
        var detector = ObstacleDetector()
        let zones = detector.analyze(depthMap: depthMap { _, _ in 1.0 })
        XCTAssertEqual(zones.left ?? 0, 1.0, accuracy: 0.01)
        XCTAssertEqual(zones.center ?? 0, 1.0, accuracy: 0.01)
        XCTAssertEqual(zones.right ?? 0, 1.0, accuracy: 0.01)
    }

    func testObstacleOnDisplayLeftPushesGapRight() {
        var detector = ObstacleDetector()
        // Portrait mount: display-left corresponds to high raw x.
        let map = depthMap { x, _ in x > 180 ? 0.6 : 3.5 }
        var zones = ObstacleZones.empty
        for _ in 0..<5 { zones = detector.analyze(depthMap: map) }
        XCTAssertNotNil(zones.left)
        XCTAssertLessThan(zones.left!, 0.7)
        XCTAssertGreaterThan(zones.gapDirection, 0.2)
    }
}
