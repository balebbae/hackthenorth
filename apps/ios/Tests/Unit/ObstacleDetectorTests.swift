import XCTest
import CoreVideo
@testable import NavigationAssistant

final class ObstacleDetectorTests: XCTestCase {
    /// Builds a Float32 depth map in sensor (landscape) orientation: width is the
    /// long axis, which is vertical on a portrait phone; height is horizontal.
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
        XCTAssertFalse(zones.touching)
    }

    func testWallAheadFillsAllZones() {
        var detector = ObstacleDetector()
        let zones = detector.analyze(depthMap: depthMap { _, _ in 1.0 })
        XCTAssertEqual(zones.left ?? 0, 1.0, accuracy: 0.01)
        XCTAssertEqual(zones.center ?? 0, 1.0, accuracy: 0.01)
        XCTAssertEqual(zones.right ?? 0, 1.0, accuracy: 0.01)
    }

    func testObstacleOnWearersLeftIsLeftZoneAndGapPointsRight() {
        var detector = ObstacleDetector()
        // Wearer's left is high raw y (bottom rows of the landscape sensor image).
        let map = depthMap { _, y in y > 140 ? 0.6 : 6.0 }
        var zones = ObstacleZones.empty
        for _ in 0..<5 { zones = detector.analyze(depthMap: map) }
        XCTAssertEqual(zones.left ?? 0, 0.6, accuracy: 0.01)
        XCTAssertNil(zones.center)
        XCTAssertNil(zones.right)
        XCTAssertGreaterThan(zones.gapDirection, 0.2)
    }

    func testObstacleOnWearersRightIsRightZoneAndGapPointsLeft() {
        var detector = ObstacleDetector()
        let map = depthMap { _, y in y < 50 ? 0.6 : 6.0 }
        var zones = ObstacleZones.empty
        for _ in 0..<5 { zones = detector.analyze(depthMap: map) }
        XCTAssertEqual(zones.right ?? 0, 0.6, accuracy: 0.01)
        XCTAssertNil(zones.left)
        XCTAssertLessThan(zones.gapDirection, -0.2)
    }

    func testObstacleAboveOrBelowTheBandIsIgnored() {
        var detector = ObstacleDetector()
        // Only the top of the view (low raw x) has something close.
        let zones = detector.analyze(depthMap: depthMap { x, _ in x < 60 ? 0.5 : 4.0 })
        XCTAssertEqual(zones.closest ?? 0, 4.0, accuracy: 0.01)
    }

    func testSubMinimumReadingsCountAsTouchingRange() {
        var detector = ObstacleDetector()
        let zones = detector.analyze(depthMap: depthMap { _, _ in 0.12 })
        XCTAssertEqual(zones.center ?? 0, 0.2, accuracy: 0.001)
    }

    func testPressedAgainstSurfaceIsTouching() {
        var detector = ObstacleDetector()
        // Mostly unmeasurable pixels with a scattering of sub-minimum ones.
        let zones = detector.analyze(depthMap: depthMap { _, y in y % 40 == 0 ? 0.1 : .nan })
        XCTAssertTrue(zones.touching)
        XCTAssertEqual(zones.closest ?? 0, 0.2, accuracy: 0.001)
    }

    func testAllInvalidWithoutCloseReadingsIsNotTouching() {
        var detector = ObstacleDetector()
        let zones = detector.analyze(depthMap: depthMap { _, _ in .nan })
        XCTAssertFalse(zones.touching)
        XCTAssertNil(zones.closest)
    }
}
