import SwiftUI

/// First-launch screen: choose which position this phone is mounted in.
struct RolePickerView: View {
    @EnvironmentObject private var roleStore: RoleStore
    @State private var selection: DeviceRole?

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: AppTheme.s24) {
                VStack(alignment: .leading, spacing: AppTheme.s8) {
                    Text("Where is this phone?")
                        .font(.system(size: 40, weight: .semibold))
                        .tracking(-1)
                        .foregroundStyle(AppTheme.ink)
                    Text("Pick the mount position. Only the front phone uses its camera.")
                        .font(.system(size: 16))
                        .foregroundStyle(AppTheme.graphite)
                }
                .padding(.top, AppTheme.s32)

                VStack(spacing: AppTheme.s12) {
                    ForEach(DeviceRole.allCases) { role in
                        RoleOptionCard(role: role, isSelected: selection == role) {
                            selection = role
                        }
                    }
                }

                Button("Continue") {
                    if let selection { roleStore.role = selection }
                }
                .buttonStyle(PrimaryButtonStyle())
                .disabled(selection == nil)
                .opacity(selection == nil ? 0.5 : 1)
                .accessibilityIdentifier("rolePicker.continue")
            }
            .padding(.horizontal, AppTheme.s16)
            .padding(.bottom, AppTheme.s32)
        }
        .background(AppTheme.canvas.ignoresSafeArea())
    }
}

private struct RoleOptionCard: View {
    let role: DeviceRole
    let isSelected: Bool
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            HStack(spacing: AppTheme.s16) {
                Image(systemName: role.symbolName)
                    .font(.system(size: 20, weight: .medium))
                    .foregroundStyle(isSelected ? .white : AppTheme.ink)
                    .frame(width: 44, height: 44)
                    .background(isSelected ? AppTheme.primary : AppTheme.skyTint)
                    .clipShape(RoundedRectangle(cornerRadius: AppTheme.radiusButton, style: .continuous))
                VStack(alignment: .leading, spacing: AppTheme.s4) {
                    HStack(spacing: AppTheme.s8) {
                        Text(role.title)
                            .font(.system(size: 20, weight: .medium))
                            .foregroundStyle(AppTheme.ink)
                        if role.usesCamera {
                            PillTag(text: "Camera", fill: AppTheme.marigold)
                        } else {
                            PillTag(text: "Haptic")
                        }
                    }
                    Text(role.summary)
                        .font(.system(size: 14))
                        .foregroundStyle(AppTheme.graphite)
                        .multilineTextAlignment(.leading)
                }
                Spacer(minLength: 0)
            }
            .padding(AppTheme.s16)
            .background(AppTheme.card)
            .clipShape(RoundedRectangle(cornerRadius: AppTheme.radiusCard, style: .continuous))
            .overlay(
                RoundedRectangle(cornerRadius: AppTheme.radiusCard, style: .continuous)
                    .stroke(isSelected ? AppTheme.primary : AppTheme.hairline, lineWidth: isSelected ? 2 : 1)
            )
        }
        .buttonStyle(.plain)
        .accessibilityIdentifier("rolePicker.option.\(role.rawValue)")
        .accessibilityAddTraits(isSelected ? .isSelected : [])
    }
}
