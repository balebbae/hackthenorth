import Foundation
import AVFoundation
import Combine

/// A live voice call with the Wander backend's `/ws/sessions/{id}/voice` bridge.
///
/// Protocol (shared/contracts/voice.md): open the socket with the API key, send
/// `{"type":"auth","token":…}`, wait for `voice_ready`, then stream
/// `{"type":"audio","audio":<base64 PCM16LE mono 24 kHz>}` in ~100 ms chunks and
/// play returned `audio` chunks in order. The microphone runs through
/// AVAudioEngine with voice processing (echo cancellation) so the loudspeaker
/// reply does not feed back into the request.
@MainActor
final class VoiceCallController: NSObject, ObservableObject {
    enum State: Equatable {
        case idle, connecting, ready, ended(String)
        var label: String {
            switch self {
            case .idle: "Off"
            case .connecting: "Connecting"
            case .ready: "In call"
            case .ended(let why): "Ended: \(why)"
            }
        }
    }

    struct Line: Identifiable, Equatable {
        let id = UUID()
        let speaker: String
        var text: String
    }

    @Published private(set) var state: State = .idle
    @Published private(set) var transcript: [Line] = []
    @Published private(set) var lastAssistantResponse: String?
    @Published private(set) var chunksSent = 0
    @Published private(set) var chunksPlayed = 0

    nonisolated static let sampleRate: Double = 24_000
    /// ~100 ms of audio per message.
    nonisolated static let samplesPerChunk = 2_400

    private var socket: URLSessionWebSocketTask?
    private let engine = AVAudioEngine()
    private let player = AVAudioPlayerNode()
    private var converter: AVAudioConverter?
    private let outputFormat = AVAudioFormat(commonFormat: .pcmFormatFloat32, sampleRate: sampleRate, channels: 1, interleaved: false)!
    private var sendTask: Task<Void, Never>?
    private let pending = SampleQueue()
    private var isReady = false

    var isActive: Bool { state == .connecting || state == .ready }

    // MARK: - call lifecycle

    func start(baseURL: URL, apiKey: String, sessionId: String, token: String) {
        guard !isActive else { return }
        transcript.removeAll()
        lastAssistantResponse = nil
        chunksSent = 0
        chunksPlayed = 0
        isReady = false
        state = .connecting

        var components = URLComponents(url: baseURL, resolvingAgainstBaseURL: false)!
        components.scheme = components.scheme == "http" ? "ws" : "wss"
        components.path = (components.path as NSString).appendingPathComponent("ws/sessions/\(sessionId)/voice")
        var request = URLRequest(url: components.url!)
        request.setValue(apiKey, forHTTPHeaderField: "X-API-Key")
        let task = URLSession.shared.webSocketTask(with: request)
        socket = task
        task.resume()
        send(["type": "auth", "token": token])
        receiveLoop()
    }

    func end() {
        guard socket != nil else { return }
        send(["type": "close"])
        finish("hung up")
    }

    private func finish(_ reason: String) {
        sendTask?.cancel()
        sendTask = nil
        stopAudio()
        socket?.cancel(with: .normalClosure, reason: nil)
        socket = nil
        isReady = false
        if state != .idle { state = .ended(reason) }
    }

    // MARK: - socket

    private func send(_ object: [String: Any]) {
        guard let socket, let data = try? JSONSerialization.data(withJSONObject: object),
              let text = String(data: data, encoding: .utf8) else { return }
        socket.send(.string(text)) { [weak self] error in
            guard let error else { return }
            Task { @MainActor in self?.finish("send failed: \(error.localizedDescription)") }
        }
    }

    private func receiveLoop() {
        socket?.receive { [weak self] result in
            Task { @MainActor in
                guard let self else { return }
                switch result {
                case .failure(let error):
                    self.finish(error.localizedDescription)
                case .success(let message):
                    if case .string(let text) = message, let data = text.data(using: .utf8),
                       let event = try? JSONSerialization.jsonObject(with: data) as? [String: Any] {
                        self.handle(event)
                    }
                    if self.socket != nil { self.receiveLoop() }
                }
            }
        }
    }

    private func handle(_ event: [String: Any]) {
        switch event["type"] as? String {
        case "voice_ready":
            isReady = true
            state = .ready
            startAudio()
        case "audio":
            if let base64 = event["audio"] as? String, let data = Data(base64Encoded: base64) { play(pcm16: data) }
        case "transcript":
            let speaker = (event["speaker"] as? String) ?? "assistant"
            let delta = (event["delta"] as? String) ?? ""
            if let last = transcript.indices.last, transcript[last].speaker == speaker {
                transcript[last].text += delta
            } else {
                transcript.append(Line(speaker: speaker, text: delta))
                if transcript.count > 12 { transcript.removeFirst(transcript.count - 12) }
            }
        case "assistant_response":
            lastAssistantResponse = event["text"] as? String
        case "error":
            finish((event["message"] as? String) ?? "error")
        default:
            break
        }
    }

    // MARK: - audio

    private func startAudio() {
        let session = AVAudioSession.sharedInstance()
        try? session.setCategory(.playAndRecord, mode: .voiceChat, options: [.defaultToSpeaker, .allowBluetoothHFP, .duckOthers])
        try? session.setActive(true)

        let input = engine.inputNode
        try? input.setVoiceProcessingEnabled(true)  // echo cancellation against our own speaker
        let hardware = input.outputFormat(forBus: 0)
        let target = AVAudioFormat(commonFormat: .pcmFormatFloat32, sampleRate: Self.sampleRate, channels: 1, interleaved: false)!
        converter = AVAudioConverter(from: hardware, to: target)
        let queue = pending
        let converter = self.converter
        input.installTap(onBus: 0, bufferSize: 4096, format: hardware) { buffer, _ in
            guard let converter else { return }
            let ratio = Self.sampleRate / hardware.sampleRate
            let capacity = AVAudioFrameCount(Double(buffer.frameLength) * ratio) + 32
            guard let out = AVAudioPCMBuffer(pcmFormat: target, frameCapacity: capacity) else { return }
            var consumed = false
            var error: NSError?
            converter.convert(to: out, error: &error) { _, status in
                if consumed { status.pointee = .noDataNow; return nil }
                consumed = true
                status.pointee = .haveData
                return buffer
            }
            guard error == nil, let channel = out.floatChannelData else { return }
            queue.append(Array(UnsafeBufferPointer(start: channel[0], count: Int(out.frameLength))))
        }

        engine.attach(player)
        engine.connect(player, to: engine.mainMixerNode, format: outputFormat)
        engine.prepare()
        do {
            try engine.start()
            player.play()
        } catch {
            finish("audio engine: \(error.localizedDescription)")
            return
        }

        sendTask = Task { [weak self] in
            while !Task.isCancelled {
                try? await Task.sleep(for: .milliseconds(100))
                guard let self, self.isReady else { continue }
                while let chunk = self.pending.take(Self.samplesPerChunk) {
                    self.send(["type": "audio", "audio": Self.pcm16Data(from: chunk).base64EncodedString()])
                    self.chunksSent += 1
                }
            }
        }
    }

    private func stopAudio() {
        engine.inputNode.removeTap(onBus: 0)
        player.stop()
        if engine.isRunning { engine.stop() }
        engine.detach(player)
        pending.clear()
        try? AVAudioSession.sharedInstance().setCategory(.playAndRecord, mode: .default,
                                                         options: [.defaultToSpeaker, .allowBluetoothHFP, .duckOthers])
    }

    private func play(pcm16 data: Data) {
        let samples = Self.floats(fromPCM16: data)
        guard !samples.isEmpty,
              let buffer = AVAudioPCMBuffer(pcmFormat: outputFormat, frameCapacity: AVAudioFrameCount(samples.count)) else { return }
        buffer.frameLength = AVAudioFrameCount(samples.count)
        samples.withUnsafeBufferPointer { buffer.floatChannelData![0].update(from: $0.baseAddress!, count: samples.count) }
        player.scheduleBuffer(buffer, completionHandler: nil)
        if !player.isPlaying, engine.isRunning { player.play() }
        chunksPlayed += 1
    }

    // MARK: - PCM helpers (pure, unit tested)

    /// Float samples in -1...1 to little-endian signed 16-bit PCM.
    nonisolated static func pcm16Data(from samples: [Float]) -> Data {
        var data = Data(capacity: samples.count * 2)
        for sample in samples {
            let clamped = max(-1, min(1, sample))
            let value = Int16(clamped * Float(Int16.max)).littleEndian
            withUnsafeBytes(of: value) { data.append(contentsOf: $0) }
        }
        return data
    }

    nonisolated static func floats(fromPCM16 data: Data) -> [Float] {
        let count = data.count / 2
        var out = [Float](repeating: 0, count: count)
        data.withUnsafeBytes { raw in
            for i in 0..<count {
                let value = Int16(littleEndian: raw.loadUnaligned(fromByteOffset: i * 2, as: Int16.self))
                out[i] = Float(value) / Float(Int16.max)
            }
        }
        return out
    }
}

/// Samples captured on the audio thread, drained on the main actor.
final class SampleQueue: @unchecked Sendable {
    private var samples: [Float] = []
    private let lock = NSLock()

    func append(_ new: [Float]) {
        lock.lock(); samples.append(contentsOf: new); lock.unlock()
    }

    /// The next `count` samples, or nil when fewer are waiting.
    func take(_ count: Int) -> [Float]? {
        lock.lock(); defer { lock.unlock() }
        guard samples.count >= count else { return nil }
        let chunk = Array(samples[..<count])
        samples.removeFirst(count)
        return chunk
    }

    func clear() { lock.lock(); samples.removeAll(); lock.unlock() }
}
