import XCTest
import simd
@testable import NavigationAssistant

final class NianticRESTTransportTests: XCTestCase {
    func testRequestCarriesTokenAndPayload() throws {
        let transport = NianticRESTTransport(endpoint: URL(string: "https://api.nianticspatial.com/web/v1/localize")!, token: "dev-token")
        let query = LocalizationQuery(
            sequence: 7, capturedAt: 1.25, jpeg: Data([0xFF, 0xD8, 0xFF]),
            imageWidth: 640, imageHeight: 480,
            cameraTransform: matrix_identity_float4x4, intrinsics: matrix_identity_float3x3
        )
        let request = transport.makeRequest(for: query)
        XCTAssertEqual(request.httpMethod, "POST")
        XCTAssertEqual(request.url?.absoluteString, "https://api.nianticspatial.com/web/v1/localize")
        XCTAssertEqual(request.value(forHTTPHeaderField: "Authorization"), "Bearer dev-token")
        XCTAssertEqual(request.value(forHTTPHeaderField: "Content-Type"), "application/json")

        let body = try XCTUnwrap(request.httpBody)
        let json = try XCTUnwrap(JSONSerialization.jsonObject(with: body) as? [String: Any])
        XCTAssertEqual(json["sequence"] as? Int, 7)
        XCTAssertEqual(json["imageBase64"] as? String, Data([0xFF, 0xD8, 0xFF]).base64EncodedString())
        XCTAssertEqual((json["cameraTransform"] as? [Double])?.count, 16)
        XCTAssertEqual((json["intrinsics"] as? [Double])?.count, 9)
    }

    func testFailedRequestReportsFailure() async {
        let transport = NianticRESTTransport(endpoint: URL(string: "https://127.0.0.1:9/nope")!, token: "t")
        let query = LocalizationQuery(sequence: 1, capturedAt: 0, jpeg: Data(), imageWidth: 1, imageHeight: 1,
                                      cameraTransform: matrix_identity_float4x4, intrinsics: matrix_identity_float3x3)
        let outcome = await transport.send(query)
        if case .failed = outcome { } else { XCTFail("expected failure, got \(outcome)") }
    }
}
