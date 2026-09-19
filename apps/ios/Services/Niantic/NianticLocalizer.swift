import Foundation
import ARKit
import Combine
import UIKit
#if canImport(NSDK)
import NSDK
#endif

/// One VPS fix: the device pose in the Site's anchor frame plus quality.
struct LocalizationFix: Equatable, Sendable {
    var pose: SitePose
    var state: BackendTrackingState
    var confidence: Float
    var timestamp: Date
    /// Anchor transform in ARKit space, kept so ARKit poses between fixes can be
    /// converted into the site frame.
    var anchorTransform: simd_float4x4
}

/// Wraps the Niantic Spatial SDK: one NSDK session fed by our ARKit session,
/// a VPS2 session tracking the Site's anchor, and the resulting device pose in
/// the site frame. The SDK submits camera frames itself at the configured rate.
@MainActor
final class NianticLocalizer: NSObject, ObservableObject {
    enum Phase: Equatable {
        case idle
        case unavailable(String)
        case starting
        case fetchingAnchor
        case coarse
        case tracking(BackendTrackingState)
        case failed(String)

        var label: String {
            switch self {
            case .idle: "Idle"
            case .unavailable(let why): "Unavailable: \(why)"
            case .starting: "Starting SDK"
            case .fetchingAnchor: "Fetching site anchor"
            case .coarse: "Searching for site"
            case .tracking(let s): s == .localized ? "Localized" : (s == .limited ? "Limited" : "Lost")
            case .failed(let why): "Failed: \(why)"
            }
        }
    }

    @Published private(set) var phase: Phase = .idle
    @Published private(set) var isAuthorized = false
    @Published private(set) var latestFix: LocalizationFix?
    @Published private(set) var anchorUpdates = 0
    @Published private(set) var framesSubmitted = 0
    @Published private(set) var siteId = ""
    private var lastCameraTransform = matrix_identity_float4x4

    /// Frames per second requested from the VPS service before the first fix.
    /// 5 matches the 200 ms cadence the team asked for.
    var initialRequestsPerSecond: Float = 5
    var continuousRequestsPerSecond: Float = 1

    #if canImport(NSDK)
    private var nsdk: NSDKSession?
    private var dataSource: DefaultSessionDataSource?
    private var vps: NSDKVps2Session?
    private var cancellables = Set<AnyCancellable>()
    #endif

    static var isAvailable: Bool {
        #if canImport(NSDK)
        return true
        #else
        return false
        #endif
    }

    func start(token: String, siteId: String, anchorPayload: String?, arSession: ARSession) {
        self.siteId = siteId
        #if canImport(NSDK)
        stop()
        phase = .starting
        let session = NSDKSession(accessToken: token, useLidar: true)
        nsdk = session
        let source = DefaultSessionDataSource(session: arSession, orientationReporter: self)
        dataSource = source
        session.dataSource = source
        isAuthorized = session.isAuthorized

        let vps = session.acquireVps2Session()
        self.vps = vps
        do {
            try vps.configure(with: NSDKVps2Session.Configuration(
                universalLocalizationEnabled: false,
                vpsMapLocalizationEnabled: true,
                initialVpsRequestsPerSecond: initialRequestsPerSecond,
                continuousVpsRequestsPerSecond: continuousRequestsPerSecond,
                anchorDistanceGateMeters: -1
            ))
        } catch {
            phase = .failed("configure: \(error.localizedDescription)")
            return
        }
        vps.anchorUpdated
            .sink { [weak self] _, update in self?.handle(update) }
            .store(in: &cancellables)
        vps.start()
        phase = .coarse

        Task { [weak self] in
            guard let self else { return }
            let payload: String
            if let anchorPayload, !anchorPayload.isEmpty {
                payload = anchorPayload
            } else {
                self.phase = .fetchingAnchor
                do {
                    payload = try await self.fetchAnchorPayload(session: session, siteId: siteId)
                } catch {
                    self.phase = .failed("site assets: \(error.localizedDescription)")
                    return
                }
            }
            do {
                _ = try vps.trackAnchor(payload: payload)
                self.phase = .coarse
            } catch {
                self.phase = .failed("trackAnchor: \(error.localizedDescription)")
            }
        }
        #else
        phase = .unavailable("NSDK package not linked")
        #endif
    }

    /// Call once per ARKit frame so the SDK ingests it.
    func update(cameraTransform: simd_float4x4) {
        #if canImport(NSDK)
        guard let nsdk else { return }
        lastCameraTransform = cameraTransform
        nsdk.update()
        framesSubmitted += 1
        if isAuthorized != nsdk.isAuthorized { isAuthorized = nsdk.isAuthorized }
        #endif
    }

    func stop() {
        #if canImport(NSDK)
        cancellables.removeAll()
        vps?.stop()
        nsdk?.destroyAll()
        vps = nil
        dataSource = nil
        nsdk = nil
        #endif
        phase = .idle
        latestFix = nil
    }

    #if canImport(NSDK)
    private func fetchAnchorPayload(session: NSDKSession, siteId: String) async throws -> String {
        nonisolated(unsafe) let sites = session.acquireSitesSession()
        let result = try await sites.requestAssetsForSite(siteId: siteId)
        let assets: [AssetInfo] = result.assets
        guard let vpsAsset = assets.first(where: { $0.assetType == .vpsInfo && $0.deployment == .production })
                ?? assets.first(where: { $0.assetType == .vpsInfo }) else {
            throw NSError(domain: "NianticLocalizer", code: 1,
                          userInfo: [NSLocalizedDescriptionKey: "Site has no production VPS asset"])
        }
        guard let payload = vpsAsset.vpsData?.anchorPayload, !payload.isEmpty else {
            throw NSError(domain: "NianticLocalizer", code: 2,
                          userInfo: [NSLocalizedDescriptionKey: "VPS asset has no anchor payload"])
        }
        return payload
    }

    private func handle(_ update: VpsAnchorUpdate) {
        anchorUpdates += 1
        let state: BackendTrackingState
        switch update.trackingState {
        case .tracked: state = .localized
        case .limited: state = .limited
        case .notTracked: state = .lost
        }
        phase = .tracking(state)
        guard let data = update.trackingData else {
            if state == .lost, var fix = latestFix {
                fix.state = .lost
                fix.timestamp = Date()
                latestFix = fix
            }
            return
        }
        let pose = SitePose.deviceInAnchorFrame(anchor: data.targetAnchorTransform, device: lastCameraTransform)
        latestFix = LocalizationFix(
            pose: pose, state: state, confidence: data.confidence,
            timestamp: Date(timeIntervalSince1970: TimeInterval(data.timestampMs) / 1000),
            anchorTransform: data.targetAnchorTransform
        )
    }
    #endif
}

#if canImport(NSDK)
extension NianticLocalizer: UIOrientationReporter {
    nonisolated var currentOrientation: NSDKScreenOrientation { .portrait }
}
#endif
