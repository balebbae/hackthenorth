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

    private func configureAudioSession() {
        do {
            let session = AVAudioSession.sharedInstance()
            try session.setCategory(.playback, mode: .spokenAudio, options: [.duckOthers])
            try session.setActive(true)
        } catch {
            print("[Speech] audio session error: \(error)")
        }
    }

    /// Returns true when the cue was actually spoken.
    @discardableResult
    func speak(_ cue: SpokenCue) -> Bool {
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
