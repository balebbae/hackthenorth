import Foundation

/// Which phones should buzz. A phone buzzes when there is an obstacle on its side:
/// front for anything ahead, left or right when that side is blocked as well or
/// something is very close on that side. The back phone is reserved for route cues.
struct HapticCommand: Codable, Equatable, Sendable {
    var front = false
    var left = false
    var right = false
    var back = false
    /// Distance to the nearest triggering obstacle, driving pulse speed.
    var distance: Float? = nil

    static let none = HapticCommand()

    func shouldBuzz(_ role: DeviceRole) -> Bool {
        switch role {
        case .front: front
        case .left: left
        case .right: right
        case .back: back
        }
    }
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

/// Turns the front phone's zones plus the side phones' clearances into a spoken
/// cue and a haptic command. Pure so it can be unit tested without ARKit.
struct ObstacleCuePolicy {
    /// Obstacles closer than this in the center zone mean stop; the front phone buzzes.
    var stopDistance: Float = 0.9
    /// With the front blocked, a side closer than this buzzes as well.
    var sideBlockedDistance: Float = 1.0
    /// On its own, a side closer than this buzzes and speaks a veer cue.
    var veerDistance: Float = 0.6
    /// A side counts as open when nothing is closer than this on that side.
    var openDistance: Float = 1.2
    /// Side readings older than this are ignored.
    var maxClearanceAge: TimeInterval = 1.0
    /// Assumed distance when a phone reports nothing in range.
    var farDistance: Float = 5.0

    struct Decision: Equatable {
        var cue: SpokenCue?
        var haptics: HapticCommand
        /// Side the wearer should move toward when the center is blocked.
        var openSide: DeviceRole?
        static let clear = Decision(cue: nil, haptics: .none, openSide: nil)
    }

    func decide(_ zones: ObstacleZones,
                sides: [DeviceRole: SideClearance] = [:],
                now: TimeInterval = Date().timeIntervalSince1970) -> Decision {
        // Each phone's buzz comes only from its own LiDAR. The side phones' readings
        // decide the side buzzes; the front phone's zones decide the front buzz.
        let leftPhone = sideReading(.left, sides: sides, now: now)
        let rightPhone = sideReading(.right, sides: sides, now: now)
        let leftBlocked = (leftPhone ?? farDistance) < sideBlockedDistance
        let rightBlocked = (rightPhone ?? farDistance) < sideBlockedDistance

        // For choosing where to go, everything funnels together: the front's side
        // zones plus whatever the side phones report.
        let leftSpace = clearance(.left, frontZone: zones.left, sides: sides, now: now)
        let rightSpace = clearance(.right, frontZone: zones.right, sides: sides, now: now)

        if let center = zones.center, center < stopDistance {
            var nearest = center
            if leftBlocked, let d = leftPhone { nearest = min(nearest, d) }
            if rightBlocked, let d = rightPhone { nearest = min(nearest, d) }
            let haptics = HapticCommand(front: true, left: leftBlocked, right: rightBlocked, distance: nearest)

            if leftSpace < openDistance && rightSpace < openDistance {
                return Decision(
                    cue: SpokenCue(text: "Stop. Obstacle ahead. No open path. Turn around.", priority: .obstacle),
                    haptics: haptics,
                    openSide: nil
                )
            }
            let openSide: DeviceRole
            if abs(leftSpace - rightSpace) < 0.15 {
                openSide = zones.gapDirection < 0 ? .left : .right
            } else {
                openSide = leftSpace > rightSpace ? .left : .right
            }
            return Decision(
                cue: SpokenCue(text: "Stop. Obstacle ahead. Open path to the \(openSide.rawValue).", priority: .obstacle),
                haptics: haptics,
                openSide: openSide
            )
        }
        // A side phone alone sees something very close: that phone buzzes.
        if let d = leftPhone, d < veerDistance {
            return Decision(
                cue: SpokenCue(text: "Obstacle on your left. Move right.", priority: .obstacle),
                haptics: HapticCommand(left: true, distance: d),
                openSide: .right
            )
        }
        if let d = rightPhone, d < veerDistance {
            return Decision(
                cue: SpokenCue(text: "Obstacle on your right. Move left.", priority: .obstacle),
                haptics: HapticCommand(right: true, distance: d),
                openSide: .left
            )
        }
        // The front phone's own edge zones see something very close: the front buzzes.
        if let d = zones.left, d < veerDistance {
            return Decision(
                cue: SpokenCue(text: "Obstacle close on your left. Move right.", priority: .obstacle),
                haptics: HapticCommand(front: true, distance: d),
                openSide: .right
            )
        }
        if let d = zones.right, d < veerDistance {
            return Decision(
                cue: SpokenCue(text: "Obstacle close on your right. Move left.", priority: .obstacle),
                haptics: HapticCommand(front: true, distance: d),
                openSide: .left
            )
        }
        return .clear
    }

    /// A side phone's fresh reading as a distance, nil when that phone is absent or stale.
    func sideReading(_ side: DeviceRole, sides: [DeviceRole: SideClearance], now: TimeInterval) -> Float? {
        guard let reading = sides[side], now - reading.timestamp <= maxClearanceAge else { return nil }
        return reading.nearest ?? farDistance
    }

    /// Space on one side: the smaller of what the front phone's side zone sees and
    /// what that side's own phone sees, when its reading is fresh.
    func clearance(_ side: DeviceRole, frontZone: Float?, sides: [DeviceRole: SideClearance], now: TimeInterval) -> Float {
        var space = frontZone ?? farDistance
        if let reading = sides[side], now - reading.timestamp <= maxClearanceAge {
            space = min(space, reading.nearest ?? farDistance)
        }
        return space
    }
}
