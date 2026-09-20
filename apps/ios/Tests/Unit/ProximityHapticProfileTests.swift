import XCTest
@testable import NavigationAssistant

final class ProximityHapticProfileTests: XCTestCase {
    let profile = ProximityHapticProfile()

    func testNothingBeyondFarDistance() {
        XCTAssertNil(profile.pulse(for: 1.6))
        XCTAssertNil(profile.pulse(for: nil))
        XCTAssertNotNil(profile.pulse(for: 1.5))
    }

    func testCloserIsFasterStrongerSharper() {
        let far = profile.pulse(for: 1.4)!
        let mid = profile.pulse(for: 0.8)!
        let near = profile.pulse(for: 0.35)!
        XCTAssertGreaterThan(far.interval, mid.interval)
        XCTAssertGreaterThan(mid.interval, near.interval)
        XCTAssertLessThan(far.intensity, mid.intensity)
        XCTAssertLessThan(mid.intensity, near.intensity)
        XCTAssertLessThan(far.sharpness, mid.sharpness)
        XCTAssertLessThan(mid.sharpness, near.sharpness)
    }

    func testEndpointsClamp() {
        let touching = profile.pulse(for: 0.0)!
        XCTAssertEqual(touching.interval, profile.nearInterval, accuracy: 0.0001)
        XCTAssertEqual(touching.intensity, profile.nearIntensity, accuracy: 0.0001)
        XCTAssertEqual(touching.sharpness, profile.nearSharpness, accuracy: 0.0001)
        let edge = profile.pulse(for: profile.farDistance)!
        XCTAssertEqual(edge.interval, profile.farInterval, accuracy: 0.0001)
        XCTAssertEqual(edge.intensity, profile.farIntensity, accuracy: 0.0001)
    }

    func testSpeedUpIsGradual() {
        // Halfway in distance is halfway in interval: a steady ramp, not a late jump.
        let half = profile.pulse(for: 0.9)!
        let midpoint = (profile.farInterval + profile.nearInterval) / 2
        XCTAssertEqual(half.interval, midpoint, accuracy: 0.01)
    }

    func testProfileSpanningARangeStartsAtItsEdge() {
        let short = ProximityHapticProfile.spanning(0.4)
        XCTAssertNil(short.pulse(for: 0.45))
        XCTAssertEqual(short.pulse(for: 0.4)!.interval, short.farInterval, accuracy: 0.0001)
        XCTAssertEqual(short.pulse(for: 0.1)!.interval, short.nearInterval, accuracy: 0.0001)
        XCTAssertGreaterThan(short.pulse(for: 0.3)!.interval, short.pulse(for: 0.2)!.interval)
    }
}
