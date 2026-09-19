import Foundation
import SwiftUI

/// Where this phone is mounted on the wearer. The front phone senses and speaks;
/// the other three only buzz.
enum DeviceRole: String, CaseIterable, Codable, Identifiable, Sendable {
    case front, left, right, back

    var id: String { rawValue }

    var title: String {
        switch self {
        case .front: "Front"
        case .left: "Left shoulder"
        case .right: "Right shoulder"
        case .back: "Back"
        }
    }

    var summary: String {
        switch self {
        case .front: "Chest mount. Runs the camera, obstacle detection, localization, and speech."
        case .left: "Buzzes when the wearer should move right."
        case .right: "Buzzes when the wearer should move left."
        case .back: "Buzzes when the wearer should stop."
        }
    }

    var usesCamera: Bool { self == .front }

    var symbolName: String {
        switch self {
        case .front: "camera.fill"
        case .left: "arrow.left"
        case .right: "arrow.right"
        case .back: "hand.raised.fill"
        }
    }
}

/// Persists the chosen role in UserDefaults so the phone comes back in the same mode.
@MainActor
final class RoleStore: ObservableObject {
    nonisolated static let key = "deviceRole"

    @Published var role: DeviceRole? {
        didSet { persist() }
    }

    private let defaults: UserDefaults

    init(defaults: UserDefaults = .standard) {
        self.defaults = defaults
        if let raw = defaults.string(forKey: Self.key) {
            role = DeviceRole(rawValue: raw)
        } else {
            role = nil
        }
    }

    func clear() { role = nil }

    private func persist() {
        if let role {
            defaults.set(role.rawValue, forKey: Self.key)
        } else {
            defaults.removeObject(forKey: Self.key)
        }
    }

    nonisolated static func clearPersisted(defaults: UserDefaults = .standard) {
        defaults.removeObject(forKey: key)
    }
}
