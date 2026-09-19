import Foundation
import Combine

/// Every `interval` the loop grabs the newest camera frame, encodes it, and hands
/// it to the transport. It never queues frames: if a send is still in flight the
/// tick is counted as dropped so the phone always sends the freshest image.
@MainActor
final class LocalizationQueryLoop: ObservableObject {
    struct Stats: Equatable {
        var ticks = 0
        var sent = 0
        var skipped = 0
        var failed = 0
        var droppedNoFrame = 0
        var droppedBusy = 0
        var lastOutcome: LocalizationOutcome?
        var lastLatencyMs: Int?
        var lastPayloadBytes = 0
    }

    @Published private(set) var stats = Stats()
    @Published private(set) var isRunning = false

    private(set) var interval: TimeInterval
    private var frameProvider: () -> FrameSnapshot?
    private var transport: LocalizationTransport
    private var encoder: FrameEncoder
    private var timerTask: Task<Void, Never>?
    private var inFlight = false
    private var sequence = 0

    init(interval: TimeInterval,
         encoder: FrameEncoder,
         transport: LocalizationTransport,
         frameProvider: @escaping () -> FrameSnapshot?) {
        self.interval = interval
        self.encoder = encoder
        self.transport = transport
        self.frameProvider = frameProvider
    }

    /// Rebuilds the loop from settings without losing counters.
    func reconfigure(settings: CameraSettings) {
        interval = settings.captureInterval
        encoder = FrameEncoder(maxDimension: settings.maxImageDimension, quality: settings.jpegQuality)
        transport = Self.makeTransport(settings: settings)
        if isRunning {
            stop()
            start()
        }
    }

    static func makeTransport(settings: CameraSettings) -> LocalizationTransport {
        if settings.hasNianticCredentials, let url = settings.endpointURL {
            return NianticRESTTransport(endpoint: url, token: settings.nianticToken)
        }
        return LoggingTransport()
    }

    func start() {
        guard !isRunning else { return }
        isRunning = true
        let period = Duration.seconds(interval)
        timerTask = Task { [weak self] in
            let clock = ContinuousClock()
            var next = clock.now + period
            while !Task.isCancelled {
                try? await clock.sleep(until: next)
                if Task.isCancelled { break }
                next += period
                // Fire and forget so a slow send never delays the next tick.
                Task { await self?.tick() }
            }
        }
    }

    func stop() {
        timerTask?.cancel()
        timerTask = nil
        isRunning = false
    }

    func resetStats() { stats = Stats() }

    /// One capture-and-send cycle. Exposed so tests can drive it deterministically.
    func tick() async {
        stats.ticks += 1
        guard !inFlight else {
            stats.droppedBusy += 1
            return
        }
        guard let frame = frameProvider() else {
            stats.droppedNoFrame += 1
            return
        }
        inFlight = true
        defer { inFlight = false }
        let encoder = self.encoder
        let encoded = await Task.detached(priority: .userInitiated) { encoder.encode(frame.capturedImage) }.value
        guard let encoded else {
            stats.failed += 1
            stats.lastOutcome = .failed("encode")
            return
        }
        sequence += 1
        let query = LocalizationQuery(
            sequence: sequence,
            capturedAt: frame.timestamp,
            jpeg: encoded.data,
            imageWidth: encoded.width,
            imageHeight: encoded.height,
            cameraTransform: frame.cameraTransform,
            intrinsics: frame.intrinsics
        )
        stats.lastPayloadBytes = encoded.data.count
        let outcome = await transport.send(query)
        stats.lastOutcome = outcome
        switch outcome {
        case .sent(_, let ms):
            stats.sent += 1
            stats.lastLatencyMs = ms
        case .skipped:
            stats.skipped += 1
        case .failed:
            stats.failed += 1
        }
    }
}
