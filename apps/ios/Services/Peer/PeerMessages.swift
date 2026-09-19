import Foundation

/// What a side phone saw in its own LiDAR field of view.
struct SideClearance: Codable, Equatable, Sendable {
    let role: DeviceRole
    /// Nearest obstacle in that phone's view, nil when nothing is in range.
    let nearest: Float?
    /// Seconds since 1970 when it was measured, so stale readings can be ignored.
    let timestamp: TimeInterval
}

/// Everything that travels between the phones. Small JSON payloads over Multipeer.
enum PeerMessage: Codable, Equatable, Sendable {
    /// Front phone tells side and back phones who should buzz and how close the obstacle is.
    case haptic(HapticCommand)
    /// Side phone reports its clearance to the front.
    case clearance(SideClearance)
    /// Sent on connect so the receiver knows which mount the peer is.
    case hello(DeviceRole)
}

