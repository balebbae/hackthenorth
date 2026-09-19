import Foundation
import simd

/// Posts VPS fixes, in-between ARKit poses and the SDK's image queries to the
/// Wander backend, at most a few times a second, and remembers the session the
/// backend hands back.
@MainActor
final class LocalizationReporter: ObservableObject {
    @Published private(set) var sessionId: String?
    @Published private(set) var worldId: String?
    @Published private(set) var lastResponse: LocalizeResponse?
    @Published private(set) var lastError: String?
    @Published private(set) var fixesSent = 0
    @Published private(set) var posesSent = 0
    /// Image queries mirrored to `POST /worlds/{id}/localize/query`.
    @Published private(set) var queriesSent = 0
    @Published private(set) var queriesFailed = 0
    @Published private(set) var queriesSkipped = 0
    @Published private(set) var lastQueryResponse: LocalizationQueryResponse?
    /// The JPEG of the newest uploaded query, for the on-device thumbnail.
    @Published private(set) var lastQueryJPEG: Data?
    @Published private(set) var lastQueryError: String?

    private var client: WanderBackendClient?
    private var siteId = ""
    private var deviceId = ""
    private var role: DeviceRole = .front
    private var lastFixSend: TimeInterval = 0
    private var lastPoseSend: TimeInterval = 0
    private var inFlight = false
    var minInterval: TimeInterval = 0.2

    private var uploadQueryImages = true
    private var uploadFailedQueries = true
    private var encoder = FrameEncoder(maxDimension: 640, quality: 0.6)
    private var queryInFlight = false
    private var lastQuerySend: TimeInterval = 0
    /// Newest query that arrived while an upload was running; sent next so the last one is never lost.
    private var queuedQuery: (query: VPSImageQuery, currentPose: SitePose?)?
    var minQueryInterval: TimeInterval = 0.15

    func configure(settings: CameraSettings, deviceId: String, role: DeviceRole) {
        self.deviceId = deviceId
        self.role = role
        siteId = settings.nianticSiteId
        worldId = settings.worldId.isEmpty ? nil : settings.worldId
        uploadQueryImages = settings.uploadQueryImages
        uploadFailedQueries = settings.uploadFailedQueries
        encoder = FrameEncoder(maxDimension: settings.maxImageDimension, quality: settings.jpegQuality)
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

    /// Image queries the SDK finished since the last frame. Only the newest
    /// eligible one is uploaded per call; if an upload is already running it is
    /// queued and sent right after, so the dashboard always ends on the latest.
    func report(queries: [VPSImageQuery], currentPose: SitePose?) {
        guard uploadQueryImages, client != nil, worldId != nil else { return }
        let eligible = queries.filter { $0.succeeded || uploadFailedQueries }
        guard let newest = eligible.last else { return }
        queriesSkipped += max(0, eligible.count - 1)
        if queryInFlight {
            if queuedQuery != nil { queriesSkipped += 1 }
            queuedQuery = (newest, currentPose)
            return
        }
        send(query: newest, currentPose: currentPose)
    }

    private func send(query: VPSImageQuery, currentPose: SitePose?) {
        guard let client, let worldId else { return }
        guard query.pixelBuffer != nil else {
            // The frame fell out of the ring before the SDK reported the request; nothing to show.
            queriesSkipped += 1
            lastQueryError = "query frame not retained (\(query.frameMatch.rawValue))"
            return
        }
        let now = Date().timeIntervalSince1970
        let wait = max(0, minQueryInterval - (now - lastQuerySend))
        lastQuerySend = now + wait
        queryInFlight = true
        let encoder = self.encoder
        let sessionId = self.sessionId
        let deviceId = self.deviceId, role = self.role, siteId = self.siteId
        Task {
            defer {
                queryInFlight = false
                if let next = queuedQuery {
                    queuedQuery = nil
                    send(query: next.query, currentPose: next.currentPose)
                }
            }
            if wait > 0 { try? await Task.sleep(for: .seconds(wait)) }
            // `query` is @unchecked Sendable so the pixel buffer can cross to the encoder thread.
            let encoded = await Task.detached(priority: .utility) { query.pixelBuffer.flatMap { encoder.encode($0) } }.value
            guard let encoded else {
                queriesFailed += 1
                lastQueryError = "could not encode query frame"
                return
            }
            let dictionary = WanderBackendClient.queryBody(
                deviceId: deviceId, role: role, siteId: siteId, sessionId: sessionId,
                query: query, jpeg: encoded.data, imageWidth: encoded.width, imageHeight: encoded.height,
                currentPose: currentPose)
            guard let body = try? JSONSerialization.data(withJSONObject: dictionary) else {
                queriesFailed += 1
                lastQueryError = "could not serialise query"
                return
            }
            do {
                lastQueryResponse = try await client.uploadQuery(worldId: worldId, body: body)
                lastQueryJPEG = encoded.data
                lastQueryError = nil
                queriesSent += 1
            } catch {
                queriesFailed += 1
                lastQueryError = error.localizedDescription
            }
        }
    }

    func reset() {
        sessionId = nil
        lastResponse = nil
        lastError = nil
        lastQueryResponse = nil
        lastQueryJPEG = nil
        lastQueryError = nil
        queuedQuery = nil
    }
}
