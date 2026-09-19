import Foundation
import simd

/// One camera snapshot ready to be sent to Niantic Spatial.
struct LocalizationQuery: Sendable {
    let sequence: Int
    let capturedAt: TimeInterval
    let jpeg: Data
    let imageWidth: Int
    let imageHeight: Int
    let cameraTransform: simd_float4x4
    let intrinsics: simd_float3x3
}

/// What came back from one query. `skipped` means no credentials were configured.
enum LocalizationOutcome: Equatable, Sendable {
    case sent(statusCode: Int, latencyMs: Int)
    case skipped
    case failed(String)

    var label: String {
        switch self {
        case .sent(let code, let ms): "HTTP \(code) in \(ms) ms"
        case .skipped: "skipped (no token)"
        case .failed(let reason): "failed: \(reason)"
        }
    }
}

protocol LocalizationTransport: Sendable {
    func send(_ query: LocalizationQuery) async -> LocalizationOutcome
}

/// Used when no developer token is configured. Counts the query and does nothing.
struct LoggingTransport: LocalizationTransport {
    func send(_ query: LocalizationQuery) async -> LocalizationOutcome {
        #if DEBUG
        print("[Localization] would send frame #\(query.sequence) \(query.imageWidth)x\(query.imageHeight) \(query.jpeg.count) bytes")
        #endif
        return .skipped
    }
}

/// Posts each snapshot to the Niantic Spatial REST endpoint with a developer token.
///
/// The request shape is a best guess until person 2 confirms the localization
/// endpoint; the JSON body carries the JPEG as base64 plus camera pose and intrinsics
/// so the payload can be adapted without touching the capture loop.
struct NianticRESTTransport: LocalizationTransport {
    let endpoint: URL
    let token: String
    let session: URLSession

    init(endpoint: URL, token: String, session: URLSession = .shared) {
        self.endpoint = endpoint
        self.token = token
        self.session = session
    }

    func makeRequest(for query: LocalizationQuery) -> URLRequest {
        var request = URLRequest(url: endpoint)
        request.httpMethod = "POST"
        request.timeoutInterval = 5
        request.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = try? JSONEncoder().encode(Body(query: query))
        return request
    }

    func send(_ query: LocalizationQuery) async -> LocalizationOutcome {
        let request = makeRequest(for: query)
        let started = Date()
        do {
            let (_, response) = try await session.data(for: request)
            let code = (response as? HTTPURLResponse)?.statusCode ?? -1
            let ms = Int(Date().timeIntervalSince(started) * 1000)
            return .sent(statusCode: code, latencyMs: ms)
        } catch {
            return .failed(error.localizedDescription)
        }
    }

    struct Body: Encodable {
        let sequence: Int
        let capturedAt: TimeInterval
        let imageBase64: String
        let imageWidth: Int
        let imageHeight: Int
        /// Column-major 4x4 camera-to-world transform from ARKit.
        let cameraTransform: [Float]
        /// Column-major 3x3 intrinsics for the full-resolution image.
        let intrinsics: [Float]

        init(query: LocalizationQuery) {
            sequence = query.sequence
            capturedAt = query.capturedAt
            imageBase64 = query.jpeg.base64EncodedString()
            imageWidth = query.imageWidth
            imageHeight = query.imageHeight
            cameraTransform = Body.flatten(query.cameraTransform)
            intrinsics = Body.flatten(query.intrinsics)
        }

        static func flatten(_ m: simd_float4x4) -> [Float] {
            (0..<4).flatMap { c in (0..<4).map { r in m[c][r] } }
        }

        static func flatten(_ m: simd_float3x3) -> [Float] {
            (0..<3).flatMap { c in (0..<3).map { r in m[c][r] } }
        }
    }
}
