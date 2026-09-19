import Foundation
import Combine
import UIKit

/// Side and back phones: stay linked to the front phone, buzz on command, and on
/// the left and right mounts also run LiDAR and stream clearance to the front.
@MainActor
final class SidePipeline: ObservableObject {
    @Published private(set) var zones: ObstacleZones = .empty
    @Published private(set) var lastCommand: HapticCommand = .none
    @Published private(set) var reportsSent = 0
    private var wantsSensing = false

    /// True only while ARKit is actually delivering frames.
    var isSensing: Bool { arSession.state == .running && arSession.frameCount > 0 }

    let role: DeviceRole
    let link: PeerLink
    let haptics = HapticController()
    let arSession = ARSessionController()

    private var detector = ObstacleDetector()
    private var lastDetection: TimeInterval = 0
    private let detectionInterval: TimeInterval = 1.0 / 10
    private var lastReport: TimeInterval = 0
    private let reportInterval: TimeInterval = 0.2
    private var forwarding = Set<AnyCancellable>()
    private var statusTask: Task<Void, Never>?

    var canSense: Bool { (role == .left || role == .right) && ARSessionController.isSupported }

    init(role: DeviceRole) {
        self.role = role
        link = PeerLink(role: role)
        link.onMessage = { [weak self] message, _ in self?.handle(message) }
        arSession.addFrameHandler { [weak self] frame in self?.handle(frame) }
        for child in [link.objectWillChange.eraseToAnyPublisher(),
                      haptics.objectWillChange.eraseToAnyPublisher(),
                      arSession.objectWillChange.eraseToAnyPublisher()] {
            child.sink { [weak self] _ in self?.objectWillChange.send() }.store(in: &forwarding)
        }
    }

    func start(settings: CameraSettings) {
        link.start()
        detector.maxRange = Float(settings.obstacleRangeMeters)
        wantsSensing = canSense && settings.sidePhonesSenseObstacles
        if wantsSensing { arSession.start(settings: settings) }
        UIApplication.shared.isIdleTimerDisabled = true
        statusTask?.cancel()
        statusTask = Task { [weak self] in
            while !Task.isCancelled {
                try? await Task.sleep(for: .seconds(1))
                guard let self else { break }
                let z = self.zones
                let fmt: (Float?) -> String = { $0.map { String(format: "%.2f", $0) } ?? "-" }
                print("[side \(self.role.rawValue)] ar=\(self.arSession.state) frames=\(self.arSession.frameCount) depth=\(self.arSession.depthAvailable) L=\(fmt(z.left)) C=\(fmt(z.center)) R=\(fmt(z.right)) touching=\(z.touching) link=\(self.link.connectedRoles.map(\.rawValue)) sent=\(self.link.messagesSent) recv=\(self.link.messagesReceived) cmd=\(self.lastCommand.shouldBuzz(self.role) ? "buzz" : "quiet") err=\(self.link.lastError ?? "-")")
            }
        }
    }

    func stop() {
        link.stop()
        arSession.stop()
        haptics.stopPulsing()
        wantsSensing = false
        statusTask?.cancel()
        UIApplication.shared.isIdleTimerDisabled = false
    }

    func applySettings(_ settings: CameraSettings) {
        detector.maxRange = Float(settings.obstacleRangeMeters)
        let shouldSense = canSense && settings.sidePhonesSenseObstacles
        if shouldSense, !wantsSensing {
            wantsSensing = true
            arSession.start(settings: settings)
        } else if !shouldSense, wantsSensing {
            wantsSensing = false
            arSession.stop()
            zones = .empty
        }
    }

    private func handle(_ message: PeerMessage) {
        guard case .haptic(let command) = message else { return }
        lastCommand = command
        haptics.setProximity(command.shouldBuzz(role) ? (command.distance ?? 0.5) : nil)
    }

    private func handle(_ frame: FrameSnapshot) {
        guard frame.timestamp - lastDetection >= detectionInterval, let depth = frame.depthMap else { return }
        lastDetection = frame.timestamp
        zones = detector.analyze(depthMap: depth)
        guard frame.timestamp - lastReport >= reportInterval else { return }
        lastReport = frame.timestamp
        let reading = SideClearance(role: role, nearest: zones.closest, timestamp: Date().timeIntervalSince1970)
        link.send(.clearance(reading), to: [.front], reliable: false)
        reportsSent += 1
    }
}
