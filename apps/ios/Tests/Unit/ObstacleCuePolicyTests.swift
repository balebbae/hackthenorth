import XCTest
@testable import NavigationAssistant

final class ObstacleCuePolicyTests: XCTestCase {
    let policy = ObstacleCuePolicy()

    func testClearSceneProducesNothing() {
        XCTAssertEqual(policy.decide(.empty), .clear)
    }

    func testCenterObstacleStopsAndBuzzesBackPlusObstacleSide() {
        let zones = ObstacleZones(left: nil, center: 0.5, right: nil, gapDirection: 0.8)
        let d = policy.decide(zones)
        XCTAssertEqual(d.cue?.priority, .obstacle)
        XCTAssertTrue(d.cue!.text.contains("right"))
        XCTAssertEqual(d.haptics, HapticCommand(left: true, right: false, back: true, distance: 0.5))
    }

    func testLeftObstacleBuzzesLeftPhone() {
        let d = policy.decide(ObstacleZones(left: 0.4, center: nil, right: nil))
        XCTAssertEqual(d.haptics, HapticCommand(left: true, distance: 0.4))
        XCTAssertTrue(d.haptics.shouldBuzz(.left))
        XCTAssertFalse(d.haptics.shouldBuzz(.right))
        XCTAssertEqual(d.cue?.text, "Obstacle on your left. Move right.")
    }

    func testRightObstacleBuzzesRightPhone() {
        let d = policy.decide(ObstacleZones(left: nil, center: nil, right: 0.4))
        XCTAssertEqual(d.haptics, HapticCommand(right: true, distance: 0.4))
    }

    func testFarObstaclesAreIgnored() {
        let d = policy.decide(ObstacleZones(left: 2.0, center: 3.0, right: 2.5))
        XCTAssertEqual(d, .clear)
    }

    func testObstacleOutranksRoute() {
        XCTAssertTrue(SpokenCue.Priority.route < .obstacle)
    }
}
