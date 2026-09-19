import Foundation
import CoreHaptics
import UIKit

/// Plays a buzz on the side and back phones. Falls back to UIKit feedback where
/// Core Haptics is unavailable, and reports what it did so the UI can show it.
@MainActor
final class HapticController: ObservableObject {
    @Published private(set) var isAvailable = false
    @Published private(set) var lastBuzz: Date?
    @Published private(set) var buzzCount = 0

    private var engine: CHHapticEngine?

    init() {
        isAvailable = CHHapticEngine.capabilitiesForHardware().supportsHaptics
        guard isAvailable else { return }
        do {
            engine = try CHHapticEngine()
            engine?.resetHandler = { [weak self] in
                Task { @MainActor in try? self?.engine?.start() }
            }
            try engine?.start()
        } catch {
            print("[Haptics] engine error: \(error)")
            isAvailable = false
        }
    }

    /// A continuous buzz for `duration` seconds at `intensity` 0...1.
    func buzz(duration: TimeInterval = 0.4, intensity: Float = 0.9) {
        buzzCount += 1
        lastBuzz = Date()
        guard let engine, isAvailable else {
            UIImpactFeedbackGenerator(style: .heavy).impactOccurred()
            return
        }
        do {
            let event = CHHapticEvent(
                eventType: .hapticContinuous,
                parameters: [
                    CHHapticEventParameter(parameterID: .hapticIntensity, value: intensity),
                    CHHapticEventParameter(parameterID: .hapticSharpness, value: 0.5)
                ],
                relativeTime: 0,
                duration: duration
            )
            let pattern = try CHHapticPattern(events: [event], parameters: [])
            let player = try engine.makePlayer(with: pattern)
            try player.start(atTime: CHHapticTimeImmediate)
        } catch {
            print("[Haptics] play error: \(error)")
            UIImpactFeedbackGenerator(style: .heavy).impactOccurred()
        }
    }
}
