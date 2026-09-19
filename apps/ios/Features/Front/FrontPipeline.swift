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
    let notes = WorldNotesStore()
    @Published private(set) var usingNSDK = false
    /// Notes projected into the camera preview; empty unless the anchor is tracked.
    @Published private(set) var notePins: [NotePin] = []
    /// Size of the preview the overlay draws into, reported by `NoteOverlay`.
    var overlaySize: CGSize = .zero
    private var lastReportedFix: LocalizationFix?
    private var lastCameraTransform = matrix_identity_float4x4
    private var lastNoteUpdate: TimeInterval = 0
    /// Ranking and projecting notes is cheap but pointless at frame rate.
    private let noteInterval: TimeInterval = 1.0 / 10
    private var settings: CameraSettings?
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

        // SwiftUI only observes this object, so republish the children's changes.
        for child in [arSession.objectWillChange.eraseToAnyPublisher(),
                      queryLoop.objectWillChange.eraseToAnyPublisher(),
                      speech.objectWillChange.eraseToAnyPublisher(),
                      link.objectWillChange.eraseToAnyPublisher(),
                      localizer.objectWillChange.eraseToAnyPublisher(),
                      notes.objectWillChange.eraseToAnyPublisher(),
                      reporter.objectWillChange.eraseToAnyPublisher()] {
            child.sink { [weak self] _ in self?.objectWillChange.send() }.store(in: &forwarding)
        }
    }

    func start(settings: CameraSettings, deviceId: String = "") {
        detector.maxRange = Float(settings.obstacleRangeMeters)
        self.settings = settings
        arSession.start(settings: settings)
        reporter.configure(settings: settings, deviceId: deviceId, role: .front)
        loadNotes()
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
        notePins = []   // the list stays readable with the camera stopped; the overlay cannot
        isActive = false
        UIApplication.shared.isIdleTimerDisabled = false
    }

    func applySettings(_ settings: CameraSettings) {
        let worldChanged = settings.worldId != self.settings?.worldId
        self.settings = settings
        detector.maxRange = Float(settings.obstacleRangeMeters)
        queryLoop.reconfigure(settings: settings)
        if worldChanged { loadNotes() }
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
        // Ahead of the depth guard: notes must keep updating on phones without
        // LiDAR, and between the detector's slower ticks.
        updateNotes(frame: frame)
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

    /* ------------------------------------------------------------- notes */

    /// True while the VPS anchor is tracked against the map, which is the only
    /// state where a note's distance or on-screen position means anything. A
    /// `limited` anchor is a coarse GPS estimate (see the NSDK docs on anchor
    /// tracking states), so it deliberately does not count.
    var notesLocalized: Bool { localizer.latestFix?.state == .localized }

    /// Pull the world's notes from the backend. Safe to call repeatedly; the
    /// store cancels any fetch still in flight.
    func loadNotes() {
        guard let settings, let base = settings.backendBaseURL, !settings.backendAPIKey.isEmpty else {
            notes.reset()
            return
        }
        let client = WanderBackendClient(baseURL: base, apiKey: settings.backendAPIKey)
        notes.load(client: client, worldId: reporter.worldId ?? settings.worldId)
    }

    private func updateNotes(frame: FrameSnapshot) {
        guard !notes.isEmpty else {
            if !notePins.isEmpty { notePins = [] }
            return
        }
        guard frame.timestamp - lastNoteUpdate >= noteInterval else { return }
        lastNoteUpdate = frame.timestamp

        guard notesLocalized, let fix = localizer.latestFix else {
            notes.update(pose: nil)
            if !notePins.isEmpty { notePins = [] }
            return
        }
        // Where the phone is now, not where it was at the last fix.
        let pose = SitePose.deviceInAnchorFrame(anchor: fix.anchorTransform, device: frame.cameraTransform)
        for due in notes.update(pose: pose) {
            speech.speak(SpokenCue(text: due.spokenCue, priority: .route))
        }
        notePins = projectNotes(anchor: fix.anchorTransform)
    }

    /// Project each note into the camera preview. Site-frame positions go back
    /// into ARKit space through the anchor, then through ARKit's own projection
    /// so the labels line up with the aspect-filled preview.
    private func projectNotes(anchor: simd_float4x4) -> [NotePin] {
        guard overlaySize.width > 1, overlaySize.height > 1,
              let camera = arSession.session.currentFrame?.camera else { return [] }
        let view = camera.viewMatrix(for: .portrait)
        var pins: [NotePin] = []
        for bearing in notes.bearings {
            let p = bearing.note.point
            let world = anchor * SIMD4<Float>(p.x, p.y, p.z, 1)
            let inCamera = view * world
            // ARKit projects points behind the camera too; drop those and anything
            // practically on the lens.
            guard inCamera.z < -0.25 else { continue }
            let point = camera.projectPoint(SIMD3<Float>(world.x, world.y, world.z),
                                            orientation: .portrait, viewportSize: overlaySize)
            guard point.x.isFinite, point.y.isFinite else { continue }
            pins.append(NotePin(id: bearing.note.id, title: bearing.note.title,
                                distance: bearing.distance, point: point))
        }
        return pins
    }
}
