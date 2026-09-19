import Foundation

/// Which phones should buzz. The phone on the side of the obstacle buzzes so the
/// wearer moves away from it; the back phone buzzes for a full stop.
struct HapticCommand: Equatable, Sendable {
    var left = false
    var right = false
    var back = false

    static let none = HapticCommand()
}

/// A spoken cue with a priority so obstacle warnings interrupt route guidance.
struct SpokenCue: Equatable, Sendable {
    enum Priority: Int, Comparable, Sendable {
        case route = 0
        case obstacle = 1
        static func < (a: Priority, b: Priority) -> Bool { a.rawValue < b.rawValue }
    }
    let text: String
    let priority: Priority
}

/// Turns obstacle zones into a spoken cue and a haptic command. Pure so it can be
/// unit tested without ARKit.
struct ObstacleCuePolicy {
    /// Obstacles closer than this in the center zone mean stop.
    var stopDistance: Float = 0.9
    /// Obstacles closer than this on a side mean veer away.
    var veerDistance: Float = 0.7

    struct Decision: Equatable {
        var cue: SpokenCue?
        var haptics: HapticCommand
        static let clear = Decision(cue: nil, haptics: .none)
    }

    func decide(_ zones: ObstacleZones) -> Decision {
        if let center = zones.center, center < stopDistance {
            let side = zones.gapDirection < 0 ? "left" : "right"
            return Decision(
                cue: SpokenCue(text: "Stop. Obstacle ahead. Clear path to the \(side).", priority: .obstacle),
                haptics: HapticCommand(left: side == "right", right: side == "left", back: true)
            )
        }
        if let left = zones.left, left < veerDistance {
            return Decision(
                cue: SpokenCue(text: "Obstacle on your left. Move right.", priority: .obstacle),
                haptics: HapticCommand(left: true)
            )
        }
        if let right = zones.right, right < veerDistance {
            return Decision(
                cue: SpokenCue(text: "Obstacle on your right. Move left.", priority: .obstacle),
                haptics: HapticCommand(right: true)
            )
        }
        return .clear
    }
}
