import XCTest
@testable import NavigationAssistant

final class VoiceCallControllerTests: XCTestCase {
    func testPCM16RoundTripAndClamping() {
        let samples: [Float] = [0, 0.5, -0.5, 1.0, -1.0, 1.7, -3.0]
        let data = VoiceCallController.pcm16Data(from: samples)
        XCTAssertEqual(data.count, samples.count * 2, "two little-endian bytes per sample")
        let back = VoiceCallController.floats(fromPCM16: data)
        XCTAssertEqual(back[0], 0, accuracy: 0.0001)
        XCTAssertEqual(back[1], 0.5, accuracy: 0.001)
        XCTAssertEqual(back[2], -0.5, accuracy: 0.001)
        XCTAssertEqual(back[3], 1.0, accuracy: 0.001)
        XCTAssertEqual(back[5], 1.0, accuracy: 0.001, "over-range input is clamped")
        XCTAssertEqual(back[6], -1.0, accuracy: 0.001)
        // Little-endian check: 0.5 * 32767 = 16383 = 0x3FFF -> bytes FF 3F
        XCTAssertEqual([UInt8](data[2..<4]), [0xFF, 0x3F])
    }

    func testChunkSizeIsAbout100Milliseconds() {
        XCTAssertEqual(Double(VoiceCallController.samplesPerChunk) / VoiceCallController.sampleRate, 0.1, accuracy: 0.001)
        XCTAssertLessThan(VoiceCallController.samplesPerChunk * 2 * 4 / 3, 65536, "encoded chunk stays under the 64 KiB cap")
    }

    func testSampleQueueHandsOutWholeChunksOnly() {
        let queue = SampleQueue()
        queue.append([Float](repeating: 0.1, count: 150))
        XCTAssertNil(queue.take(200))
        queue.append([Float](repeating: 0.2, count: 100))
        let chunk = queue.take(200)
        XCTAssertEqual(chunk?.count, 200)
        XCTAssertEqual(chunk?.first, 0.1)
        XCTAssertEqual(chunk?.last, 0.2)
        XCTAssertNil(queue.take(200), "50 samples remain")
    }
}
