import Foundation
import simd

/// A device pose in the Niantic site frame, ready for the backend.
struct SitePose: Equatable, Sendable {
    var position: SIMD3<Float>
    /// Unit quaternion as x, y, z, w.
    var rotation: simd_quatf

    /// Device pose relative to a tracked anchor: both transforms are in ARKit
    /// world space, so the device in anchor space is anchor⁻¹ · device.
    static func deviceInAnchorFrame(anchor: simd_float4x4, device: simd_float4x4) -> SitePose {
        let relative = anchor.inverse * device
        let position = SIMD3<Float>(relative.columns.3.x, relative.columns.3.y, relative.columns.3.z)
        let rotation = simd_quatf(relative).normalized
        return SitePose(position: position, rotation: rotation)
    }

    var positionArray: [Float] { [position.x, position.y, position.z] }
    var rotationArray: [Float] { [rotation.vector.x, rotation.vector.y, rotation.vector.z, rotation.vector.w] }
}

/// Backend's view of localization quality.
enum BackendTrackingState: String, Codable, Sendable {
    case localized, limited, lost
}

/// What the backend answered to a localization fix.
struct LocalizeResponse: Decodable, Equatable, Sendable {
    struct NearestNode: Decodable, Equatable, Sendable {
        let id: String
        let name: String?
        let distanceMetres: Double
    }
    let sessionId: String
    let worldId: String
    let nearestNode: NearestNode?
    let offGraphMetres: Double?
}

struct WorldSummary: Decodable, Sendable {
    let id: String
    let name: String
    let nianticSiteId: String?
}

/// Talks to the Wander worlds API on Modal. Every request carries the team key.
struct WanderBackendClient: Sendable {
    let baseURL: URL
    let apiKey: String
    var session: URLSession = .shared

    nonisolated(unsafe) private static let iso: ISO8601DateFormatter = {
        let f = ISO8601DateFormatter()
        f.formatOptions = [.withInternetDateTime, .withFractionalSeconds]
        return f
    }()

    static func timestamp(_ date: Date) -> String { iso.string(from: date) }

    func request(_ method: String, _ path: String, body: [String: Any]? = nil) -> URLRequest {
        request(method, path, data: body.flatMap { try? JSONSerialization.data(withJSONObject: $0) })
    }

    func request(_ method: String, _ path: String, data: Data?) -> URLRequest {
        var request = URLRequest(url: baseURL.appendingPathComponent(path))
        request.httpMethod = method
        request.timeoutInterval = 8
        request.setValue(apiKey, forHTTPHeaderField: "X-API-Key")
        request.setValue("application/json", forHTTPHeaderField: "Accept")
        if let data {
            request.setValue("application/json", forHTTPHeaderField: "Content-Type")
            request.httpBody = data
        }
        return request
    }

    /// Body for `POST /worlds/{id}/localize`, matching `localizationUpdate` in the contract.
    static func localizationBody(deviceId: String, role: DeviceRole, siteId: String, pose: SitePose,
                                 confidence: Float, state: BackendTrackingState, timestamp: Date,
                                 sessionId: String?) -> [String: Any] {
        var body: [String: Any] = [
            "deviceId": deviceId,
            "role": role == .front ? "chest" : role.rawValue,
            "nianticSiteId": siteId,
            "pose": ["position": pose.positionArray, "rotation": pose.rotationArray],
            "confidence": max(0, min(1, confidence)),
            "trackingState": state.rawValue,
            "timestamp": Self.timestamp(timestamp)
        ]
        if let sessionId { body["sessionId"] = sessionId }
        return body
    }

    func localize(worldId: String, body: Data) async throws -> LocalizeResponse {
        let (data, response) = try await session.data(for: request("POST", "worlds/\(worldId)/localize", data: body))
        try Self.check(response, data)
        return try JSONDecoder().decode(LocalizeResponse.self, from: data)
    }

    /// `POST /sessions/{id}/pose` for high-rate ARKit poses between VPS fixes.
    func pose(sessionId: String, pose: SitePose, state: BackendTrackingState, timestamp: Date) async throws {
        let body: [String: Any] = [
            "pose": ["position": pose.positionArray, "rotation": pose.rotationArray],
            "trackingState": state.rawValue,
            "timestamp": Self.timestamp(timestamp)
        ]
        let (data, response) = try await session.data(for: request("POST", "sessions/\(sessionId)/pose", body: body))
        try Self.check(response, data)
    }

    func worlds() async throws -> [WorldSummary] {
        let (data, response) = try await session.data(for: request("GET", "worlds"))
        try Self.check(response, data)
        if let list = try? JSONDecoder().decode([WorldSummary].self, from: data) { return list }
        struct Wrapped: Decodable { let worlds: [WorldSummary] }
        return try JSONDecoder().decode(Wrapped.self, from: data).worlds
    }

    struct HTTPError: Error, LocalizedError {
        let status: Int
        let body: String
        var errorDescription: String? { "HTTP \(status): \(body.prefix(160))" }
    }

    private static func check(_ response: URLResponse, _ data: Data) throws {
        let status = (response as? HTTPURLResponse)?.statusCode ?? -1
        guard (200..<300).contains(status) else {
            throw HTTPError(status: status, body: String(decoding: data, as: UTF8.self))
        }
    }
}
