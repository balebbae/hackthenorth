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
    @Published private(set) var usingNSDK = false
    private var lastReportedFix: LocalizationFix?
    private var lastCameraTransform = matrix_identity_float4x4
    private var lastSentHaptics: HapticCommand?
    private var lastHapticSend: TimeInterval = 0
    private var statusTask: Task<Void, Never>?
    private var relocalizeTask: Task<Void, Never>?
    private var activeSettings: CameraSettings?
    private var activeDeviceId = ""

    private var detector = ObstacleDetector()
    private var estimator = StructureObstacleEstimator()
    private var mapSensor = MapObstacleSensor()
    private var staticMap: StaticMap?
    private var mapWorldId: String?
    private var mapTask: Task<Void, Never>?
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
        estimator.maxRange = Float(settings.obstacleRangeMeters)
        mapSensor.maxRange = Float(settings.obstacleRangeMeters)
        arSession.start(settings: settings)
        activeSettings = settings
        activeDeviceId = deviceId
        startLocalization(settings: settings, deviceId: deviceId)
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
        arSession.stop()
        // The peer link stays up across Stop/Start so the side phones do not have to re-pair.
        speech.stop()
        isActive = false
        UIApplication.shared.isIdleTimerDisabled = false
    }

    func applySettings(_ settings: CameraSettings) {
        detector.maxRange = Float(settings.obstacleRangeMeters)
        estimator.maxRange = Float(settings.obstacleRangeMeters)
        mapSensor.maxRange = Float(settings.obstacleRangeMeters)
        queryLoop.reconfigure(settings: settings)
        let previous = activeSettings
        activeSettings = settings
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

    private func stopLocalization() {
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
        if let map = staticMap, let fix = localizer.latestFix, fix.state != .lost {
            reading = mapSensor.read(map: map, deviceTransform: fix.anchorTransform.inverse * frame.cameraTransform)
        }
        if reading != mapReading { mapReading = reading }
        if let reading { sensed = .merged(sensed, reading.zones) }
        // Side and back mounts are driven purely by the map around the localised pose.
        let sides = SideClearanceMerge.merge(live: [:], map: reading, now: now)
        zones = sensed
        let decision = policy.decide(zones, sides: sides, now: now)
        lastDecision = decision
        if let cue = decision.cue { speech.speak(cue) }
        haptics.setProximity(decision.haptics.front ? decision.haptics.distance : nil)

        // Push buzz commands when they change, with a half-second keepalive so a
        // dropped packet cannot leave a side phone pulsing forever.
        if decision.haptics != lastSentHaptics || now - lastHapticSend > 0.5 {
            link.send(.haptic(decision.haptics))
            lastSentHaptics = decision.haptics
            lastHapticSend = now
        }
    }
}
