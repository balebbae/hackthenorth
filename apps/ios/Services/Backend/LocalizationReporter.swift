import Foundation
import simd

/// Posts VPS fixes and in-between ARKit poses to the Wander backend, at most a
/// few times a second, and remembers the session the backend hands back.
@MainActor
final class LocalizationReporter: ObservableObject {
    @Published private(set) var sessionId: String?
    @Published private(set) var worldId: String?
    @Published private(set) var lastResponse: LocalizeResponse?
    @Published private(set) var lastError: String?
    @Published private(set) var fixesSent = 0
    @Published private(set) var posesSent = 0

    private var client: WanderBackendClient?
    private var siteId = ""
    private var deviceId = ""
    private var role: DeviceRole = .front
    private var lastFixSend: TimeInterval = 0
    private var lastPoseSend: TimeInterval = 0
    private var inFlight = false
    var minInterval: TimeInterval = 0.2

    func configure(settings: CameraSettings, deviceId: String, role: DeviceRole) {
        self.deviceId = deviceId
        self.role = role
        siteId = settings.nianticSiteId
        worldId = settings.worldId.isEmpty ? nil : settings.worldId
        if let base = settings.backendBaseURL, !settings.backendAPIKey.isEmpty {
            client = WanderBackendClient(baseURL: base, apiKey: settings.backendAPIKey)
            if worldId == nil { Task { await resolveWorld() } }
        } else {
            client = nil
        }
    }

    var isConfigured: Bool { client != nil }

    /// Look the world up by Niantic site ID when none was configured.
    private func resolveWorld() async {
        guard let client else { return }
        do {
            let worlds = try await client.worlds()
            if let match = worlds.first(where: { $0.nianticSiteId == siteId && !siteId.isEmpty }) {
                worldId = match.id
            } else if worlds.count == 1 {
                worldId = worlds[0].id
            } else {
                lastError = "no world matches site \(siteId)"
            }
        } catch {
            lastError = error.localizedDescription
        }
    }

    /// A VPS fix from the SDK. Sent through /localize.
    func report(fix: LocalizationFix) {
        guard let client, let worldId else { return }
        let now = Date().timeIntervalSince1970
        guard now - lastFixSend >= minInterval, !inFlight else { return }
        lastFixSend = now
        inFlight = true
        let dictionary = WanderBackendClient.localizationBody(
            deviceId: deviceId, role: role, siteId: siteId, pose: fix.pose,
            confidence: fix.confidence, state: fix.state, timestamp: fix.timestamp, sessionId: sessionId)
        guard let body = try? JSONSerialization.data(withJSONObject: dictionary) else { return }
        Task {
            defer { inFlight = false }
            do {
                let response = try await client.localize(worldId: worldId, body: body)
                sessionId = response.sessionId
                lastResponse = response
                lastError = nil
                fixesSent += 1
            } catch {
                lastError = error.localizedDescription
            }
        }
    }

    /// An ARKit pose between fixes, converted with the last known anchor transform.
    func report(cameraTransform: simd_float4x4, using fix: LocalizationFix) {
        guard let client, let sessionId else { return }
        let now = Date().timeIntervalSince1970
        guard now - lastPoseSend >= minInterval, !inFlight else { return }
        lastPoseSend = now
        let pose = SitePose.deviceInAnchorFrame(anchor: fix.anchorTransform, device: cameraTransform)
        inFlight = true
        Task {
            defer { inFlight = false }
            do {
                try await client.pose(sessionId: sessionId, pose: pose, state: fix.state, timestamp: Date())
                posesSent += 1
            } catch {
                lastError = error.localizedDescription
            }
        }
    }

    func reset() {
        sessionId = nil
        lastResponse = nil
        lastError = nil
    }
}
