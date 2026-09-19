import XCTest
import simd
@testable import NavigationAssistant

final class BackendAndPoseTests: XCTestCase {
    func testDeviceInAnchorFrameRemovesAnchorOffset() {
        // Anchor sits at (2, 0, 3) rotated 90° about Y; the device is 1 m in front of it along the anchor's -Z.
        let rotation = simd_quatf(angle: .pi / 2, axis: SIMD3<Float>(0, 1, 0))
        var anchor = simd_float4x4(rotation)
        anchor.columns.3 = SIMD4<Float>(2, 0, 3, 1)
        let localDevice = SIMD4<Float>(0, 0, -1, 1)
        var device = anchor
        device.columns.3 = anchor * localDevice
        let pose = SitePose.deviceInAnchorFrame(anchor: anchor, device: device)
        XCTAssertEqual(pose.position.x, 0, accuracy: 1e-4)
        XCTAssertEqual(pose.position.y, 0, accuracy: 1e-4)
        XCTAssertEqual(pose.position.z, -1, accuracy: 1e-4)
        XCTAssertEqual(abs(pose.rotation.real), 1, accuracy: 1e-4) // no relative rotation
    }

    func testLocalizationBodyMatchesContract() throws {
        let pose = SitePose(position: SIMD3<Float>(1, 2, 3), rotation: simd_quatf(ix: 0, iy: 0, iz: 0, r: 1))
        let body = WanderBackendClient.localizationBody(
            deviceId: "dev-1", role: .front, siteId: "site-9", pose: pose, confidence: 1.4,
            state: .localized, timestamp: Date(timeIntervalSince1970: 1_800_000_000), sessionId: nil)
        XCTAssertEqual(body["deviceId"] as? String, "dev-1")
        XCTAssertEqual(body["role"] as? String, "chest")
        XCTAssertEqual(body["nianticSiteId"] as? String, "site-9")
        XCTAssertEqual(body["confidence"] as? Float, 1.0)
        XCTAssertEqual(body["trackingState"] as? String, "localized")
        XCTAssertNil(body["sessionId"])
        let ts = try XCTUnwrap(body["timestamp"] as? String)
        XCTAssertTrue(ts.hasPrefix("2027-01-15T"), ts)
        let p = try XCTUnwrap(body["pose"] as? [String: [Float]])
        XCTAssertEqual(p["position"], [1, 2, 3])
        XCTAssertEqual(p["rotation"], [0, 0, 0, 1])
        XCTAssertNoThrow(try JSONSerialization.data(withJSONObject: body))
    }

    func testRequestCarriesAPIKey() {
        let client = WanderBackendClient(baseURL: URL(string: "https://example.modal.run")!, apiKey: "k")
        let request = client.request("POST", "worlds/w/localize", body: ["a": 1])
        XCTAssertEqual(request.url?.absoluteString, "https://example.modal.run/worlds/w/localize")
        XCTAssertEqual(request.value(forHTTPHeaderField: "X-API-Key"), "k")
        XCTAssertEqual(request.httpMethod, "POST")
        XCTAssertNotNil(request.httpBody)
    }

    func testSettingsSeedOnlyFillsEmptyFields() {
        var s = CameraSettings.default
        s.backendURL = "https://keep.me"
        s.seed(from: ["BackendURL": "https://ignored", "NianticSiteId": "abc", "BackendAPIKey": "key"])
        XCTAssertEqual(s.backendURL, "https://keep.me")
        XCTAssertEqual(s.nianticSiteId, "abc")
        XCTAssertTrue(s.hasBackend)
        XCTAssertFalse(s.canLocalizeWithNSDK)
        s.nianticToken = "t"
        XCTAssertTrue(s.canLocalizeWithNSDK)
    }
}
