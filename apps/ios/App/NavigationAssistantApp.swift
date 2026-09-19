import SwiftUI

@main
struct NavigationAssistantApp: App {
    @StateObject private var roleStore = RoleStore()
    @StateObject private var settingsStore = CameraSettingsStore()

    init() {
        LaunchArguments.applyOverrides()
    }

    var body: some Scene {
        WindowGroup {
            RootView()
                .environmentObject(roleStore)
                .environmentObject(settingsStore)
                .preferredColorScheme(.light)
        }
    }
}

/// Chooses the screen for the persisted device role, or the picker when none is set.
struct RootView: View {
    @EnvironmentObject private var roleStore: RoleStore

    var body: some View {
        Group {
            switch roleStore.role {
            case .none:
                RolePickerView()
            case .some(.front):
                FrontRoleView()
            case .some(let side):
                HapticRoleView(role: side)
            }
        }
        .background(AppTheme.canvas.ignoresSafeArea())
        .animation(.easeInOut(duration: 0.2), value: roleStore.role)
    }
}

/// Process arguments used by UI tests to put the app in a known state.
enum LaunchArguments {
    static let resetState = "-resetState"

    /// `-role front|left|right|back` presets the role for demos and screenshots.
    static let role = "-role"

    static func applyOverrides() {
        let args = ProcessInfo.processInfo.arguments
        if args.contains(resetState) {
            RoleStore.clearPersisted()
            CameraSettingsStore.clearPersisted()
        }
        if let index = args.firstIndex(of: role), index + 1 < args.count,
           let preset = DeviceRole(rawValue: args[index + 1]) {
            UserDefaults.standard.set(preset.rawValue, forKey: RoleStore.key)
        }
    }
}
