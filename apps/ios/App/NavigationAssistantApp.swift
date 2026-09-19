import SwiftUI

@main
struct NavigationAssistantApp: App {
    @StateObject private var roleStore = RoleStore()
    @StateObject private var settingsStore = CameraSettingsStore()
    /// Set when a `wander://connect` link (the viewer's QR code) was opened from outside the app.
    @State private var openedLink: WorldConnectLink?
    @State private var openedChanges: [String] = []

    init() {
        LaunchArguments.applyOverrides()
    }

    var body: some Scene {
        WindowGroup {
            RootView()
                .environmentObject(roleStore)
                .environmentObject(settingsStore)
                .preferredColorScheme(.light)
                .onOpenURL { url in
                    guard let link = WorldConnectLink(url: url) else { return }
                    var settings = settingsStore.settings
                    openedChanges = link.apply(to: &settings)
                    settingsStore.settings = settings
                    openedLink = link
                }
                .alert(
                    "Connected to \(openedLink?.displayName ?? "world")",
                    isPresented: Binding(get: { openedLink != nil }, set: { if !$0 { openedLink = nil } }),
                    presenting: openedLink
                ) { _ in
                    Button("OK") {}
                } message: { link in
                    Text(openedChanges.isEmpty
                         ? "Settings already matched \(link.worldId)."
                         : "Updated " + openedChanges.joined(separator: ", ") + ". Tokens and keys are unchanged.")
                }
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
