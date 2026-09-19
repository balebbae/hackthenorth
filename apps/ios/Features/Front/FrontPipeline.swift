import Foundation
import Combine
import ARKit

/// Wires the front phone together: one AR session feeds the obstacle detector and
/// the Niantic query loop; the cue policy drives speech and (later) side-phone haptics.
@MainActor
final class FrontPipeline: ObservableObject {
    @Published private(set) var zones: ObstacleZones = .empty
    @Published private(set) var lastDecision: ObstacleCuePolicy.Decision = .clear
    @Published private(set) var isActive = false
    @Published private(set) var usingPlaceholderFrames = false
    @Published private(set) var sideClearances: [DeviceRole: SideClearance] = [:]

    let arSession = ARSessionController()
    let speech = SpeechCoordinator()
    let queryLoop: LocalizationQueryLoop
    let link = PeerLink(role: .front)
    let haptics = HapticController()
    let localizer = NianticLocalizer()
    let reporter = LocalizationReporter()
    @Published private(set) var usingNSDK = false
    private var lastReportedFix: LocalizationFix?
    private var lastCameraTransform = matrix_identity_float4x4
    private var lastSentHaptics: HapticCommand?
    private var lastHapticSend: TimeInterval = 0
    private var statusTask: Task<Void, Never>?

    private var detector = ObstacleDetector()
    private let policy = ObstacleCuePolicy()
    private var lastDetection: TimeInterval = 0
    private let detectionInterval: TimeInterval = 1.0 / 15
    private var placeholderFrame: FrameSnapshot?
    private var forwarding = Set<AnyCancellable>()

    init(settings: CameraSettings) {
        let session = arSession
        var placeholder: FrameSnapshot?
        if !ARSessionController.isSupported, let buffer = FrameEncoder.makePlaceholderPixelBuffer() {
            placeholder = FrameSnapshot(
                timestamp: 0,
                cameraTransform: matrix_identity_float4x4,
                intrinsics: matrix_identity_float3x3,
                capturedImage: buffer,
                depthMap: nil,
                imageResolution: CGSize(width: 640, height: 480)
            )
        }
        placeholderFrame = placeholder
        queryLoop = LocalizationQueryLoop(
            interval: settings.captureInterval,
            encoder: FrameEncoder(maxDimension: settings.maxImageDimension, quality: settings.jpegQuality),
            transport: LocalizationQueryLoop.makeTransport(settings: settings),
            frameProvider: { [placeholder] in
                if let live = session.latestSnapshot { return live }
                guard var frame = placeholder else { return nil }
                frame = FrameSnapshot(
                    timestamp: Date().timeIntervalSince1970,
                    cameraTransform: frame.cameraTransform,
                    intrinsics: frame.intrinsics,
                    capturedImage: frame.capturedImage,
                    depthMap: nil,
                    imageResolution: frame.imageResolution
                )
                return frame
            }
        )
        usingPlaceholderFrames = placeholder != nil
        arSession.addFrameHandler { [weak self] frame in self?.handle(frame) }

        link.onMessage = { [weak self] message, _ in
            guard case .clearance(let reading) = message else { return }
            self?.sideClearances[reading.role] = reading
        }

        // Every VPS image query the SDK finishes goes to the backend with the pose
        // it produced, plus where the phone is right now for the live marker.
        localizer.onQueries = { [weak self] queries in
            guard let self else { return }
            let current = self.localizer.latestFix.map {
                SitePose.deviceInAnchorFrame(anchor: $0.anchorTransform, device: self.lastCameraTransform)
            }
            self.reporter.report(queries: queries, currentPose: current)
        }

        // Route guidance is whatever the backend told us to say; obstacle cues still win.
        reporter.onSpeak = { [weak self] phrase in
            self?.speech.speak(SpokenCue(text: phrase, priority: .route))
        }

        // SwiftUI only observes this object, so republish the children's changes.
        for child in [arSession.objectWillChange.eraseToAnyPublisher(),
                      queryLoop.objectWillChange.eraseToAnyPublisher(),
                      speech.objectWillChange.eraseToAnyPublisher(),
                      link.objectWillChange.eraseToAnyPublisher(),
                      localizer.objectWillChange.eraseToAnyPublisher(),
                      reporter.objectWillChange.eraseToAnyPublisher()] {
            child.sink { [weak self] _ in self?.objectWillChange.send() }.store(in: &forwarding)
        }
    }

    func start(settings: CameraSettings, deviceId: String = "") {
        detector.maxRange = Float(settings.obstacleRangeMeters)
        arSession.start(settings: settings)
        reporter.configure(settings: settings, deviceId: deviceId, role: .front)
        usingNSDK = settings.canLocalizeWithNSDK && NianticLocalizer.isAvailable && arSession.state == .running
        if usingNSDK {
            // The SDK submits frames itself at the configured rate; the REST loop stays off.
            localizer.start(token: settings.nianticToken, siteId: settings.nianticSiteId,
                            anchorPayload: nil, arSession: arSession.session)
        } else {
            queryLoop.reconfigure(settings: settings)
            queryLoop.start()
        }
        link.start()
        isActive = true
        UIApplication.shared.isIdleTimerDisabled = true
        statusTask?.cancel()
        statusTask = Task { [weak self] in
            while !Task.isCancelled {
                try? await Task.sleep(for: .seconds(1))
                guard let self else { break }
                let z = self.zones
                let fmt: (Float?) -> String = { $0.map { String(format: "%.2f", $0) } ?? "-" }
                let sides = self.sideClearances.map { "\($0.key.rawValue)=\(fmt($0.value.nearest))" }.joined(separator: ",")
                let q = self.localizer.queryStats
                print("[front] ar=\(self.arSession.state) frames=\(self.arSession.frameCount) L=\(fmt(z.left)) C=\(fmt(z.center)) R=\(fmt(z.right)) gap=\(String(format: "%.2f", z.gapDirection)) link=\(self.link.connectedRoles.map(\.rawValue)) sides=[\(sides)] haptics=\(self.lastDecision.haptics) query=\(self.queryLoop.stats.ticks) vps=\(self.localizer.phase.label) queries=\(q.issued)/\(q.succeeded)ok/\(q.failed)fail/\(q.rejected)rej uploaded=\(self.reporter.queriesSent)")
            }
        }
    }

    func stop() {
        statusTask?.cancel()
        haptics.stopPulsing()
        link.send(.haptic(.none))
        queryLoop.stop()
        localizer.stop()
        reporter.reset()
        usingNSDK = false
        arSession.stop()
        link.stop()
        speech.stop()
        isActive = false
        UIApplication.shared.isIdleTimerDisabled = false
    }

    func applySettings(_ settings: CameraSettings) {
        detector.maxRange = Float(settings.obstacleRangeMeters)
        queryLoop.reconfigure(settings: settings)
        if isActive, arSession.state == .running {
            arSession.stop()
            arSession.start(settings: settings)
        }
    }

    private func handle(_ frame: FrameSnapshot) {
        lastCameraTransform = frame.cameraTransform
        if usingNSDK {
            localizer.update(frame: frame)
            if let fix = localizer.latestFix {
                if fix != lastReportedFix {
                    lastReportedFix = fix
                    reporter.report(fix: fix)
                } else if fix.state != .lost {
                    reporter.report(cameraTransform: frame.cameraTransform, using: fix)
                }
            }
        }
        guard frame.timestamp - lastDetection >= detectionInterval, let depth = frame.depthMap else { return }
        lastDetection = frame.timestamp
        zones = detector.analyze(depthMap: depth)
        let decision = policy.decide(zones, sides: sideClearances)
        lastDecision = decision
        if let cue = decision.cue { speech.speak(cue) }
        haptics.setProximity(decision.haptics.front ? decision.haptics.distance : nil)

        // Push buzz commands when they change, with a half-second keepalive so a
        // dropped packet cannot leave a side phone pulsing forever.
        let now = Date().timeIntervalSince1970
        if decision.haptics != lastSentHaptics || now - lastHapticSend > 0.5 {
            link.send(.haptic(decision.haptics))
            lastSentHaptics = decision.haptics
            lastHapticSend = now
        }
    }
}
