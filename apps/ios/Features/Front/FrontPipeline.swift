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
    /// What the static map (splat occupancy + annotated hazards) says is around the localised pose.
    @Published private(set) var mapReading: MapObstacleSensor.Reading?
    @Published private(set) var mapStatus = "not loaded"

    let arSession = ARSessionController()
    let speech = SpeechCoordinator()
    let queryLoop: LocalizationQueryLoop
    let link = PeerLink(role: .front)
    let haptics = HapticController()
    let localizer = NianticLocalizer()
    let reporter = LocalizationReporter()
    let voice = VoiceCallController()
    @Published private(set) var voiceError: String?
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
    private var relocalizeTask: Task<Void, Never>?
    private var activeSettings: CameraSettings?
    private var activeDeviceId = ""

    private var detector = ObstacleDetector()
    private var estimator = StructureObstacleEstimator()
    private var mapSensor = MapObstacleSensor()
    /// Map buzzes need a VPS fix at least this confident. VPS answers come in bursts
    /// with "lost" gaps between them, and ARKit keeps tracking relative to the last
    /// anchor, so the last good fix is held for `mapMaxFixAge` across those gaps.
    var mapMinConfidence: Float = 0.3
    var mapMaxFixAge: TimeInterval = 10
    private var lastGoodFix: (fix: LocalizationFix, at: Date)?
    private var staticMap: StaticMap?
    private var mapWorldId: String?
    private var mapTask: Task<Void, Never>?
    /// Polls the backend for externally triggered buzzes and relays them.
    private var pulseTask: Task<Void, Never>?
    private var lastPulseId = 0
    @Published private(set) var pulsesRelayed = 0
    var pulsePollInterval: TimeInterval = 0.4
    private var policy = ObstacleCuePolicy()
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
        // Browse for the shoulder/back phones as soon as the front screen exists,
        // not only after Start, so the phones pair while the wearer is still setting up.
        link.start()

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
                      voice.objectWillChange.eraseToAnyPublisher(),
                      notes.objectWillChange.eraseToAnyPublisher(),
                      reporter.objectWillChange.eraseToAnyPublisher()] {
            child.sink { [weak self] _ in self?.objectWillChange.send() }.store(in: &forwarding)
        }
    }

    func start(settings: CameraSettings, deviceId: String = "") {
        detector.maxRange = Float(settings.obstacleRangeMeters)
        estimator.maxRange = Float(settings.obstacleRangeMeters)
        mapSensor.maxRange = Float(settings.obstacleRangeMeters)
        policy.sideWarnDistance = Float(settings.sideBuzzRangeMeters)
        policy.backWarnDistance = 0.3
        speech.isEnabled = settings.voiceCuesEnabled
        self.settings = settings
        arSession.start(settings: settings)
        activeSettings = settings
        activeDeviceId = deviceId
        startLocalization(settings: settings, deviceId: deviceId)
        loadNotes()
        link.start()  // no-op when already browsing
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
        relocalizeTask?.cancel()
        haptics.stopPulsing()
        link.send(.haptic(.none))
        stopLocalization()
        voice.end()
        arSession.stop()
        // The peer link stays up across Stop/Start so the side phones do not have to re-pair.
        speech.stop()
        notePins = []   // the list stays readable with the camera stopped; the overlay cannot
        isActive = false
        UIApplication.shared.isIdleTimerDisabled = false
    }

    func applySettings(_ settings: CameraSettings) {
        let worldChanged = settings.worldId != self.settings?.worldId
        self.settings = settings
        detector.maxRange = Float(settings.obstacleRangeMeters)
        estimator.maxRange = Float(settings.obstacleRangeMeters)
        mapSensor.maxRange = Float(settings.obstacleRangeMeters)
        policy.sideWarnDistance = Float(settings.sideBuzzRangeMeters)
        policy.backWarnDistance = 0.3
        speech.isEnabled = settings.voiceCuesEnabled
        queryLoop.reconfigure(settings: settings)
        let previous = activeSettings
        activeSettings = settings
        if worldChanged { loadNotes() }
        guard isActive else { return }
        if arSession.state == .running {
            arSession.stop()
            arSession.start(settings: settings)
        }
        // Credentials or backend fields changed while running (e.g. the token was
        // pasted into Settings): restart the localization path so the SDK picks
        // them up. Debounced because the form publishes every keystroke.
        guard previous.map({ Self.localizationInputsChanged($0, settings) }) ?? true else { return }
        relocalizeTask?.cancel()
        relocalizeTask = Task { [weak self] in
            try? await Task.sleep(for: .milliseconds(800))
            guard !Task.isCancelled, let self, self.isActive else { return }
            self.stopLocalization()
            self.startLocalization(settings: settings, deviceId: self.activeDeviceId)
        }
    }

    /// Starts either the Niantic SDK or the REST fallback, plus the backend reporter.
    private func startLocalization(settings: CameraSettings, deviceId: String) {
        reporter.configure(settings: settings, deviceId: deviceId, role: .front)
        loadStaticMap(settings: settings)
        pollPulses(settings: settings)
        speech.requestMicrophone()
        usingNSDK = settings.canLocalizeWithNSDK && NianticLocalizer.isAvailable && arSession.state == .running
        if usingNSDK {
            // The SDK submits frames itself at the configured rate; the REST loop stays off.
            localizer.start(token: settings.nianticToken, siteId: settings.nianticSiteId,
                            anchorPayload: nil, arSession: arSession.session)
        } else {
            queryLoop.reconfigure(settings: settings)
            queryLoop.start()
        }
    }

    /// Fetch the world's occupancy grid and hazards once the world id is known.
    private func loadStaticMap(settings: CameraSettings) {
        mapTask?.cancel()
        guard let base = settings.backendBaseURL, !settings.backendAPIKey.isEmpty else {
            mapStatus = "no backend"
            return
        }
        let client = WanderBackendClient(baseURL: base, apiKey: settings.backendAPIKey)
        mapTask = Task { [weak self] in
            // The reporter resolves a blank world id by site; wait for it.
            var worldId = self?.reporter.worldId
            var waited = 0
            while worldId == nil, waited < 30, !Task.isCancelled {
                try? await Task.sleep(for: .milliseconds(500))
                waited += 1
                worldId = self?.reporter.worldId
            }
            guard let self, let worldId, !Task.isCancelled else { return }
            if worldId == self.mapWorldId, self.staticMap != nil { return }
            self.mapStatus = "loading \(worldId)"
            do {
                let payload = try await client.occupancy(worldId: worldId)
                let hazards = (try? await client.hazards(worldId: worldId)) ?? []
                guard let map = StaticMap(payload: payload, hazards: hazards) else {
                    self.mapStatus = "bad occupancy payload"
                    return
                }
                self.staticMap = map
                self.mapWorldId = worldId
                self.mapStatus = "\(map.cellCount) cells · \(hazards.count) hazards"
            } catch {
                self.mapStatus = "map: \(error.localizedDescription)"
            }
        }
    }

    /// Every `pulsePollInterval`, fetch buzzes queued through the backend's public
    /// /haptics endpoints: buzz this phone for `front`, relay the rest over the link.
    private func pollPulses(settings: CameraSettings) {
        pulseTask?.cancel()
        guard let base = settings.backendBaseURL, !settings.backendAPIKey.isEmpty else { return }
        let client = WanderBackendClient(baseURL: base, apiKey: settings.backendAPIKey)
        pulseTask = Task { [weak self] in
            while !Task.isCancelled {
                if let self, let feed = try? await client.pendingPulses(since: self.lastPulseId) {
                    // A backend restart would hand out smaller ids; follow it instead of ignoring them.
                    if feed.last < self.lastPulseId { self.lastPulseId = feed.last }
                    for pulse in feed.pulses {
                        self.lastPulseId = max(self.lastPulseId, pulse.id)
                        guard let role = pulse.role == "chest" ? .front : DeviceRole(rawValue: pulse.role) else { continue }
                        self.relay(PulseCommand(id: pulse.id, role: role, ms: pulse.ms))
                    }
                    if feed.last > self.lastPulseId { self.lastPulseId = feed.last }
                }
                try? await Task.sleep(for: .seconds(self?.pulsePollInterval ?? 0.4))
            }
        }
    }

    /// Start a live voice call on the current navigation session (creating one if needed).
    func startVoiceCall(settings: CameraSettings, deviceId: String) {
        guard let base = settings.backendBaseURL, !settings.backendAPIKey.isEmpty else {
            voiceError = "backend not configured"; return
        }
        guard !settings.voiceAccessToken.isEmpty else { voiceError = "voice token missing in Settings"; return }
        voiceError = nil
        let client = WanderBackendClient(baseURL: base, apiKey: settings.backendAPIKey)
        Task { [weak self] in
            guard let self else { return }
            var sessionId = self.reporter.sessionId
            if sessionId == nil {
                guard let worldId = self.reporter.worldId ?? (settings.worldId.isEmpty ? nil : settings.worldId) else {
                    self.voiceError = "no world yet"; return
                }
                do { sessionId = try await client.createSession(worldId: worldId, deviceId: deviceId) }
                catch { self.voiceError = "session: \(error.localizedDescription)"; return }
            }
            self.voice.start(baseURL: base, apiKey: settings.backendAPIKey, sessionId: sessionId!, token: settings.voiceAccessToken)
        }
    }

    func endVoiceCall() { voice.end() }

    func relay(_ pulse: PulseCommand) {
        pulsesRelayed += 1
        print("[pulse] #\(pulse.id) \(pulse.role.rawValue) \(pulse.ms) ms; linked=\(link.connectedRoles.map(\.rawValue))")
        if pulse.role == .front {
            haptics.buzz(duration: Double(pulse.ms) / 1000, intensity: 1, sharpness: 0.4)
        } else {
            link.send(.pulse(pulse), to: [pulse.role])
        }
    }

    private func stopLocalization() {
        pulseTask?.cancel()
        mapTask?.cancel()
        queryLoop.stop()
        localizer.stop()
        reporter.reset()
        usingNSDK = false
    }

    private static func localizationInputsChanged(_ a: CameraSettings, _ b: CameraSettings) -> Bool {
        a.nianticToken != b.nianticToken || a.nianticSiteId != b.nianticSiteId
            || a.nianticEndpoint != b.nianticEndpoint || a.backendURL != b.backendURL
            || a.backendAPIKey != b.backendAPIKey || a.worldId != b.worldId
            || a.uploadQueryImages != b.uploadQueryImages || a.uploadFailedQueries != b.uploadFailedQueries
            || a.maxImageDimension != b.maxImageDimension || a.jpegQuality != b.jpegQuality
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
        // Ahead of the detection guard: notes must keep updating between the detector's slower ticks.
        updateNotes(frame: frame)
        guard frame.timestamp - lastDetection >= detectionInterval else { return }
        lastDetection = frame.timestamp
        var sensed: ObstacleZones
        if let depth = frame.depthMap {
            sensed = detector.analyze(depthMap: depth)
        } else {
            // No LiDAR: feature points and walls from ARKit world tracking.
            sensed = estimator.analyze(points: frame.featurePoints, identifiers: frame.featurePointIDs, planes: frame.verticalPlanes,
                                       cameraTransform: frame.cameraTransform, timestamp: frame.timestamp)
        }

        // Static map: once localised, the scanned splat and annotated hazards say
        // what surrounds the wearer, including the sides and back no sensor covers.
        let now = Date().timeIntervalSince1970
        var reading: MapObstacleSensor.Reading?
        if let fix = localizer.latestFix, fix.state == .localized, fix.confidence >= mapMinConfidence,
           lastGoodFix?.fix != fix {
            lastGoodFix = (fix, Date())
        }
        if let map = staticMap, let good = lastGoodFix, Date().timeIntervalSince(good.at) <= mapMaxFixAge {
            reading = mapSensor.read(map: map, deviceTransform: good.fix.anchorTransform.inverse * frame.cameraTransform)
        }
        if reading != mapReading { mapReading = reading }
        // The front's own buzz trusts only what its LiDAR sees; the map is for the sides and back.
        // Side and back mounts are driven purely by the map around the localised pose.
        let sides = SideClearanceMerge.merge(live: [:], map: reading, now: now)
        zones = sensed
        let decision = policy.decide(zones, sides: sides, now: now)
        lastDecision = decision
        haptics.setProximity(decision.haptics.front ? decision.haptics.distance : nil)

        // Push buzz commands when they change, with a half-second keepalive so a
        // dropped packet cannot leave a side phone pulsing forever.
        var command = decision.haptics
        command.sideRange = policy.sideWarnDistance
        command.backRange = policy.backWarnDistance
        if command != lastSentHaptics || now - lastHapticSend > 0.5 {
            link.send(.haptic(command))
            lastSentHaptics = command
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
