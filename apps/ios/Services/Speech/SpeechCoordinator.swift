import Foundation
import AVFoundation

/// The one place speech is produced. Obstacle cues interrupt route cues, and the
/// same cue is not repeated inside the cooldown window.
@MainActor
final class SpeechCoordinator: NSObject, ObservableObject {
    @Published private(set) var lastSpoken: String?
    @Published private(set) var isSpeaking = false

    private let synthesizer = AVSpeechSynthesizer()
    private var lastCueText: String?
    private var lastCueTime = Date.distantPast
    private var currentPriority: SpokenCue.Priority = .route
    var cooldown: TimeInterval = 2.5

    override init() {
        super.init()
        synthesizer.delegate = self
        configureAudioSession()
    }

    /// Microphone in, loudspeaker out: the front phone both listens and talks. Falls
    /// back to playback-only if the record category is refused (e.g. no microphone access yet).
    private func configureAudioSession() {
        let session = AVAudioSession.sharedInstance()
        do {
            try session.setCategory(.playAndRecord, mode: .default,
                                    options: [.defaultToSpeaker, .allowBluetoothHFP, .duckOthers])
            try session.setActive(true)
        } catch {
            print("[Speech] play-and-record session refused (\(error)); using playback only")
            try? session.setCategory(.playback, mode: .spokenAudio, options: [.duckOthers])
            try? session.setActive(true)
        }
    }

    /// Ask for microphone access once; the result is published for the UI.
    @Published private(set) var microphoneGranted: Bool?

    func requestMicrophone() {
        let current = AVAudioApplication.shared.recordPermission
        if current == .granted { microphoneGranted = true; return }
        if current == .denied { microphoneGranted = false; return }
        AVAudioApplication.requestRecordPermission { granted in
            Task { @MainActor in
                self.microphoneGranted = granted
                self.configureAudioSession()
            }
        }
    }

    /// Nothing is spoken unless the wearer turned voice cues on in Settings.
    var isEnabled = false

    /// Returns true when the cue was actually spoken.
    @discardableResult
    func speak(_ cue: SpokenCue) -> Bool {
        guard isEnabled else { return false }
        let now = Date()
        if cue.text == lastCueText, now.timeIntervalSince(lastCueTime) < cooldown { return false }
        if isSpeaking, cue.priority < currentPriority { return false }
        if isSpeaking { synthesizer.stopSpeaking(at: .immediate) }

        let utterance = AVSpeechUtterance(string: cue.text)
        utterance.voice = AVSpeechSynthesisVoice(language: "en-US")
        utterance.rate = 0.52
        utterance.volume = 1
        synthesizer.speak(utterance)
        currentPriority = cue.priority
        lastCueText = cue.text
        lastCueTime = now
        lastSpoken = cue.text
        isSpeaking = true
        return true
    }

    func stop() {
        synthesizer.stopSpeaking(at: .immediate)
        isSpeaking = false
    }
}

extension SpeechCoordinator: AVSpeechSynthesizerDelegate {
    nonisolated func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didFinish utterance: AVSpeechUtterance) {
        Task { @MainActor in self.isSpeaking = false }
    }
    nonisolated func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didCancel utterance: AVSpeechUtterance) {
        Task { @MainActor in self.isSpeaking = false }
    }
}
