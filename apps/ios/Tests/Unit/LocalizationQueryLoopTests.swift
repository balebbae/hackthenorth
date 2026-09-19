import XCTest
import simd
@testable import NavigationAssistant

/// Records queries and optionally delays to simulate a slow network.
actor RecordingTransport: LocalizationTransport {
    private(set) var queries: [LocalizationQuery] = []
    let delay: Duration
    let outcome: LocalizationOutcome

    init(delay: Duration = .zero, outcome: LocalizationOutcome = .sent(statusCode: 200, latencyMs: 1)) {
        self.delay = delay
        self.outcome = outcome
    }

    func send(_ query: LocalizationQuery) async -> LocalizationOutcome {
        queries.append(query)
        if delay > .zero { try? await Task.sleep(for: delay) }
        return outcome
    }

    func count() -> Int { queries.count }
    func last() -> LocalizationQuery? { queries.last }
}

@MainActor
final class LocalizationQueryLoopTests: XCTestCase {
    private func makeFrame() -> FrameSnapshot {
        FrameSnapshot(
            timestamp: 12.5,
            cameraTransform: matrix_identity_float4x4,
            intrinsics: matrix_identity_float3x3,
            capturedImage: FrameEncoder.makePlaceholderPixelBuffer(width: 1280, height: 960)!,
            depthMap: nil,
            imageResolution: CGSize(width: 1280, height: 960)
        )
    }

    func testTickEncodesAndSendsFreshestFrame() async {
        let transport = RecordingTransport()
        let loop = LocalizationQueryLoop(
            interval: 0.2,
            encoder: FrameEncoder(maxDimension: 640, quality: 0.6),
            transport: transport,
            frameProvider: { [frame = makeFrame()] in frame }
        )
        await loop.tick()
        await loop.tick()
        let count = await transport.count()
        XCTAssertEqual(count, 2)
        let last = await transport.last()
        XCTAssertEqual(last?.sequence, 2)
        XCTAssertEqual(last?.capturedAt, 12.5)
        XCTAssertEqual(max(last!.imageWidth, last!.imageHeight), 640)
        XCTAssertGreaterThan(last!.jpeg.count, 100)
        XCTAssertEqual(loop.stats.sent, 2)
        XCTAssertEqual(loop.stats.lastLatencyMs, 1)
    }

    func testTickWithoutFrameIsDropped() async {
        let transport = RecordingTransport()
        let loop = LocalizationQueryLoop(interval: 0.2, encoder: FrameEncoder(maxDimension: 640, quality: 0.6),
                                         transport: transport, frameProvider: { nil })
        await loop.tick()
        XCTAssertEqual(loop.stats.droppedNoFrame, 1)
        let count = await transport.count()
        XCTAssertEqual(count, 0)
    }

    func testSkippedOutcomeIsCounted() async {
        let loop = LocalizationQueryLoop(interval: 0.2, encoder: FrameEncoder(maxDimension: 320, quality: 0.5),
                                         transport: LoggingTransport(), frameProvider: { [f = makeFrame()] in f })
        await loop.tick()
        XCTAssertEqual(loop.stats.skipped, 1)
        XCTAssertEqual(loop.stats.lastOutcome, .skipped)
    }

    func testRunningLoopSendsAtRoughlyFiveHertz() async throws {
        let transport = RecordingTransport()
        let frame = makeFrame()
        _ = FrameEncoder(maxDimension: 320, quality: 0.5).encode(frame.capturedImage) // warm CoreImage
        let loop = LocalizationQueryLoop(interval: 0.2, encoder: FrameEncoder(maxDimension: 320, quality: 0.5),
                                         transport: transport, frameProvider: { frame })
        loop.start()
        XCTAssertTrue(loop.isRunning)
        try await Task.sleep(for: .seconds(1.1))
        loop.stop()
        try await Task.sleep(for: .milliseconds(100)) // let the last tick finish
        XCTAssertFalse(loop.isRunning)
        let count = await transport.count()
        XCTAssertGreaterThanOrEqual(count, 4, "expected about 5 sends in 1.1 s, got \(count)")
        XCTAssertLessThanOrEqual(count, 6, "expected about 5 sends in 1.1 s, got \(count)")
    }

    func testSlowTransportDropsTicksInsteadOfQueueing() async throws {
        let transport = RecordingTransport(delay: .seconds(1))
        let loop = LocalizationQueryLoop(interval: 0.2, encoder: FrameEncoder(maxDimension: 320, quality: 0.5),
                                         transport: transport, frameProvider: { [f = makeFrame()] in f })
        loop.start()
        try await Task.sleep(for: .seconds(0.9))
        loop.stop()
        try await Task.sleep(for: .milliseconds(50))
        let count = await transport.count()
        XCTAssertEqual(count, 1)
        XCTAssertGreaterThanOrEqual(loop.stats.droppedBusy, 2)
    }

    func testReconfigureSwapsIntervalAndTransport() {
        let loop = LocalizationQueryLoop(interval: 0.2, encoder: FrameEncoder(maxDimension: 320, quality: 0.5),
                                         transport: LoggingTransport(), frameProvider: { nil })
        var s = CameraSettings.default
        s.captureIntervalMs = 500
        loop.reconfigure(settings: s)
        XCTAssertEqual(loop.interval, 0.5, accuracy: 0.0001)
    }
}
