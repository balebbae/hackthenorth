import SwiftUI

/// Design tokens from FRONTEND_STYLE.md expressed for SwiftUI.
enum AppTheme {
    // Colors
    static let canvas = Color(hex: 0xF6F5F4)        // Paper Warmth
    static let card = Color.white                    // Card surface
    static let ink = Color.black                     // Ink Black, use opacity for hierarchy
    static let inkSecondary = Color.black.opacity(0.6)
    static let inkTertiary = Color.black.opacity(0.4)
    static let graphite = Color(hex: 0x615D59)
    static let primary = Color(hex: 0x0075DE)        // Notion Blue, one filled action per screen
    static let skyTint = Color(hex: 0xE6F3FE)        // Ghost button background
    static let marigold = Color(hex: 0xFFB110)
    static let coral = Color(hex: 0xF64932)
    static let skyWash = Color(hex: 0x62AEF0)
    static let midnight = Color(hex: 0x02093A)
    static let hairline = Color.black.opacity(0.08)

    // Radii
    static let radiusButton: CGFloat = 8
    static let radiusCard: CGFloat = 12
    static let radiusPill: CGFloat = 9999
    static let radiusSmall: CGFloat = 4

    // Spacing (4px base)
    static let s4: CGFloat = 4
    static let s8: CGFloat = 8
    static let s12: CGFloat = 12
    static let s16: CGFloat = 16
    static let s24: CGFloat = 24
    static let s32: CGFloat = 32
}

extension Color {
    init(hex: UInt32) {
        self.init(
            red: Double((hex >> 16) & 0xFF) / 255,
            green: Double((hex >> 8) & 0xFF) / 255,
            blue: Double(hex & 0xFF) / 255
        )
    }
}

/// White feature card: white surface, 12px radius, hairline border, no shadow.
struct CardModifier: ViewModifier {
    var background: Color = AppTheme.card
    var bordered = true

    func body(content: Content) -> some View {
        content
            .padding(AppTheme.s24)
            .frame(maxWidth: .infinity, alignment: .leading)
            .background(background)
            .clipShape(RoundedRectangle(cornerRadius: AppTheme.radiusCard, style: .continuous))
            .overlay(
                RoundedRectangle(cornerRadius: AppTheme.radiusCard, style: .continuous)
                    .stroke(bordered ? AppTheme.hairline : .clear, lineWidth: 1)
            )
    }
}

extension View {
    func card(background: Color = AppTheme.card, bordered: Bool = true) -> some View {
        modifier(CardModifier(background: background, bordered: bordered))
    }
}

/// Primary CTA: filled Notion Blue, 8px radius. Use once per screen.
struct PrimaryButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.system(size: 16, weight: .medium))
            .foregroundStyle(.white)
            .padding(.vertical, AppTheme.s12)
            .padding(.horizontal, AppTheme.s16)
            .frame(maxWidth: .infinity)
            .background(AppTheme.primary.opacity(configuration.isPressed ? 0.85 : 1))
            .clipShape(RoundedRectangle(cornerRadius: AppTheme.radiusButton, style: .continuous))
            .animation(.easeInOut(duration: 0.2), value: configuration.isPressed)
    }
}

/// Ghost CTA: sky tint background, blue text, 8px radius.
struct GhostButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.system(size: 16, weight: .medium))
            .foregroundStyle(AppTheme.primary)
            .padding(.vertical, AppTheme.s12)
            .padding(.horizontal, AppTheme.s16)
            .frame(maxWidth: .infinity)
            .background(AppTheme.skyTint.opacity(configuration.isPressed ? 0.7 : 1))
            .clipShape(RoundedRectangle(cornerRadius: AppTheme.radiusButton, style: .continuous))
            .animation(.easeInOut(duration: 0.2), value: configuration.isPressed)
    }
}

/// Pill tag: colored fill, 9999px radius.
struct PillTag: View {
    let text: String
    var fill: Color = AppTheme.skyTint
    var foreground: Color = AppTheme.ink
    var identifier: String? = nil

    var body: some View {
        Text(text)
            .accessibilityIdentifier(identifier ?? "")
            .font(.system(size: 12, weight: .medium))
            .foregroundStyle(foreground)
            .padding(.vertical, AppTheme.s4)
            .padding(.horizontal, AppTheme.s12)
            .background(fill)
            .clipShape(Capsule())
    }
}

/// A labeled value row used inside status cards.
struct StatRow: View {
    let label: String
    let value: String
    var identifier: String? = nil

    var body: some View {
        HStack {
            Text(label)
                .font(.system(size: 14))
                .foregroundStyle(AppTheme.inkSecondary)
            Spacer()
            Text(value)
                .font(.system(size: 14, weight: .medium, design: .monospaced))
                .foregroundStyle(AppTheme.ink)
        }
        .accessibilityElement(children: .combine)
        .accessibilityLabel("\(label): \(value)")
        .accessibilityIdentifier(identifier ?? "")
    }
}
