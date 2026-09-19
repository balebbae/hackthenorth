import SwiftUI

/// Shoulder and back phones: no camera, just a buzzer waiting for commands.
struct HapticRoleView: View {
    let role: DeviceRole
    @EnvironmentObject private var roleStore: RoleStore
    @StateObject private var haptics = HapticController()
    @State private var showSettings = false

    var body: some View {
        VStack(spacing: AppTheme.s16) {
            HStack(alignment: .firstTextBaseline) {
                VStack(alignment: .leading, spacing: AppTheme.s4) {
                    Text(role.title)
                        .font(.system(size: 40, weight: .semibold))
                        .tracking(-1)
                        .foregroundStyle(AppTheme.ink)
                        .accessibilityIdentifier("haptic.title")
                    Text(role.summary)
                        .font(.system(size: 14))
                        .foregroundStyle(AppTheme.inkSecondary)
                }
                Spacer()
                Button {
                    showSettings = true
                } label: {
                    Image(systemName: "gearshape")
                        .font(.system(size: 18, weight: .medium))
                        .foregroundStyle(AppTheme.ink)
                        .frame(width: 44, height: 44)
                        .background(AppTheme.card)
                        .clipShape(RoundedRectangle(cornerRadius: AppTheme.radiusButton, style: .continuous))
                        .overlay(RoundedRectangle(cornerRadius: AppTheme.radiusButton, style: .continuous).stroke(AppTheme.hairline))
                }
                .accessibilityLabel("Settings")
                .accessibilityIdentifier("haptic.settings")
            }
            .padding(.top, AppTheme.s16)

            VStack(alignment: .leading, spacing: AppTheme.s12) {
                HStack {
                    Image(systemName: role.symbolName)
                        .font(.system(size: 28, weight: .medium))
                    Spacer()
                    PillTag(text: haptics.isAvailable ? "Haptics ready" : "Haptics unavailable",
                            fill: haptics.isAvailable ? AppTheme.marigold : AppTheme.skyTint,
                            identifier: "haptic.availability")
                }
                StatRow(label: "Buzzes", value: "\(haptics.buzzCount)")
                StatRow(label: "Last buzz", value: haptics.lastBuzz.map { Self.time.string(from: $0) } ?? "–")
                StatRow(label: "Link", value: "not connected")
            }
            .card(background: AppTheme.skyWash.opacity(0.35), bordered: false)

            Spacer()

            Button("Test buzz") { haptics.buzz() }
                .buttonStyle(PrimaryButtonStyle())
                .accessibilityIdentifier("haptic.testBuzz")
        }
        .padding(.horizontal, AppTheme.s16)
        .padding(.bottom, AppTheme.s32)
        .background(AppTheme.canvas.ignoresSafeArea())
        .sheet(isPresented: $showSettings) { CameraSettingsView() }
        .onAppear { UIApplication.shared.isIdleTimerDisabled = true }
        .onDisappear { UIApplication.shared.isIdleTimerDisabled = false }
    }

    private static let time: DateFormatter = {
        let f = DateFormatter()
        f.dateFormat = "HH:mm:ss"
        return f
    }()
}
