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

    let arSession = ARSessionController()
    let speech = SpeechCoordinator()
    let queryLoop: LocalizationQueryLoop

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

        // SwiftUI only observes this object, so republish the children's changes.
        for child in [arSession.objectWillChange.eraseToAnyPublisher(),
                      queryLoop.objectWillChange.eraseToAnyPublisher(),
                      speech.objectWillChange.eraseToAnyPublisher()] {
            child.sink { [weak self] _ in self?.objectWillChange.send() }.store(in: &forwarding)
        }
    }

    func start(settings: CameraSettings) {
        arSession.start(settings: settings)
        queryLoop.reconfigure(settings: settings)
        queryLoop.start()
        isActive = true
        UIApplication.shared.isIdleTimerDisabled = true
    }

    func stop() {
        queryLoop.stop()
        arSession.stop()
        speech.stop()
        isActive = false
        UIApplication.shared.isIdleTimerDisabled = false
    }

    func applySettings(_ settings: CameraSettings) {
        queryLoop.reconfigure(settings: settings)
        if isActive, arSession.state == .running {
            arSession.stop()
            arSession.start(settings: settings)
        }
    }

    private func handle(_ frame: FrameSnapshot) {
        guard frame.timestamp - lastDetection >= detectionInterval, let depth = frame.depthMap else { return }
        lastDetection = frame.timestamp
        zones = detector.analyze(depthMap: depth)
        let decision = policy.decide(zones)
        lastDecision = decision
        if let cue = decision.cue { speech.speak(cue) }
    }
}
