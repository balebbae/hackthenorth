import SwiftUI
import VisionKit

/// Scans the QR code from the web viewer's "Connect a phone" dialog and applies
/// the world, Niantic site and backend it names to Settings. Falls back to
/// pasting the link where the camera is unavailable (simulator, or while the
/// AR session owns it).
struct ConnectWorldSheet: View {
    @EnvironmentObject private var settingsStore: CameraSettingsStore
    @Environment(\.dismiss) private var dismiss

    @State private var connected: WorldConnectLink?
    @State private var changes: [String] = []
    @State private var scannerError: String?
    @State private var pasted = ""
    @State private var pasteError: String?

    private var scannerSupported: Bool {
        DataScannerViewController.isSupported && DataScannerViewController.isAvailable
    }

    var body: some View {
        NavigationStack {
            Group {
                if let connected {
                    confirmation(for: connected)
                } else {
                    scannerBody
                }
            }
            .background(AppTheme.canvas.ignoresSafeArea())
            .navigationTitle("Connect to a world")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button(connected == nil ? "Cancel" : "Done") { dismiss() }
                        .accessibilityIdentifier("connect.dismiss")
                }
            }
        }
    }

    private var scannerBody: some View {
        VStack(spacing: AppTheme.s16) {
            if scannerSupported && scannerError == nil {
                WorldQRScannerView(onLink: apply, onError: { scannerError = $0 })
                    .frame(maxWidth: .infinity)
                    .frame(height: 360)
                    .clipShape(RoundedRectangle(cornerRadius: AppTheme.radiusCard, style: .continuous))
                    .overlay(
                        RoundedRectangle(cornerRadius: AppTheme.radiusCard, style: .continuous)
                            .stroke(AppTheme.hairline)
                    )
                    .accessibilityLabel("QR code scanner")
                Text("Point the camera at the QR code in the world viewer (Live tab or the phone button).")
                    .font(.system(size: 14))
                    .foregroundStyle(AppTheme.inkSecondary)
                    .multilineTextAlignment(.center)
            } else {
                VStack(spacing: AppTheme.s8) {
                    Image(systemName: "qrcode.viewfinder")
                        .font(.system(size: 34))
                        .foregroundStyle(AppTheme.inkSecondary)
                    Text(scannerError ?? "The camera scanner is not available here.")
                        .font(.system(size: 14))
                        .foregroundStyle(AppTheme.inkSecondary)
                        .multilineTextAlignment(.center)
                    if scannerError != nil {
                        Text("Stop the front camera first, or paste the link below.")
                            .font(.system(size: 12))
                            .foregroundStyle(AppTheme.inkTertiary)
                    }
                }
                .frame(maxWidth: .infinity)
                .padding(.vertical, AppTheme.s32)
                .card()
            }

            VStack(alignment: .leading, spacing: AppTheme.s8) {
                Text("Or paste the link")
                    .font(.system(size: 14, weight: .medium))
                    .foregroundStyle(AppTheme.ink)
                TextField("wander://connect?world=…", text: $pasted)
                    .textInputAutocapitalization(.never)
                    .autocorrectionDisabled()
                    .keyboardType(.URL)
                    .font(.system(size: 13, design: .monospaced))
                    .padding(AppTheme.s12)
                    .background(AppTheme.card)
                    .clipShape(RoundedRectangle(cornerRadius: AppTheme.radiusButton, style: .continuous))
                    .overlay(RoundedRectangle(cornerRadius: AppTheme.radiusButton, style: .continuous).stroke(AppTheme.hairline))
                    .accessibilityIdentifier("connect.paste")
                if let pasteError {
                    Text(pasteError)
                        .font(.system(size: 12))
                        .foregroundStyle(AppTheme.coral)
                }
                Button("Use link") {
                    if let link = WorldConnectLink(string: pasted) {
                        apply(link)
                    } else {
                        pasteError = "That is not a wander://connect link."
                    }
                }
                .buttonStyle(GhostButtonStyle())
                .disabled(pasted.trimmingCharacters(in: .whitespaces).isEmpty)
                .accessibilityIdentifier("connect.useLink")
            }
            Spacer(minLength: 0)
        }
        .padding(AppTheme.s16)
    }

    private func confirmation(for link: WorldConnectLink) -> some View {
        VStack(alignment: .leading, spacing: AppTheme.s16) {
            HStack(spacing: AppTheme.s12) {
                Image(systemName: "checkmark.circle.fill")
                    .font(.system(size: 28))
                    .foregroundStyle(AppTheme.primary)
                VStack(alignment: .leading, spacing: AppTheme.s4) {
                    Text("Connected to \(link.displayName)")
                        .font(.system(size: 22, weight: .bold))
                        .tracking(-0.24)
                        .foregroundStyle(AppTheme.ink)
                    Text(changes.isEmpty ? "Settings already matched this world." : "Updated: " + changes.joined(separator: ", "))
                        .font(.system(size: 14))
                        .foregroundStyle(AppTheme.inkSecondary)
                }
            }
            VStack(alignment: .leading, spacing: AppTheme.s8) {
                StatRow(label: "World", value: link.worldId, identifier: "connect.world")
                StatRow(label: "Niantic site", value: link.nianticSiteId ?? "not published")
                StatRow(label: "Backend", value: link.backendURL ?? "unchanged")
                Divider()
                StatRow(label: "Niantic token", value: settingsStore.settings.nianticToken.isEmpty ? "missing" : "set")
                StatRow(label: "API key", value: settingsStore.settings.backendAPIKey.isEmpty ? "missing" : "set")
            }
            .card()
            if settingsStore.settings.nianticToken.isEmpty || settingsStore.settings.backendAPIKey.isEmpty {
                Text("The QR code never carries secrets. Add the Niantic developer token and the backend API key in Settings (or LocalConfig.plist) before starting.")
                    .font(.system(size: 13))
                    .foregroundStyle(AppTheme.inkSecondary)
            }
            Spacer()
            Button("Done") { dismiss() }
                .buttonStyle(PrimaryButtonStyle())
                .accessibilityIdentifier("connect.done")
        }
        .padding(AppTheme.s16)
    }

    private func apply(_ link: WorldConnectLink) {
        var settings = settingsStore.settings
        changes = link.apply(to: &settings)
        settingsStore.settings = settings
        connected = link
        pasteError = nil
        UINotificationFeedbackGenerator().notificationOccurred(.success)
    }
}

/// VisionKit QR scanner limited to `wander://connect` codes.
struct WorldQRScannerView: UIViewControllerRepresentable {
    let onLink: (WorldConnectLink) -> Void
    let onError: (String) -> Void

    func makeUIViewController(context: Context) -> DataScannerViewController {
        let scanner = DataScannerViewController(
            recognizedDataTypes: [.barcode(symbologies: [.qr])],
            qualityLevel: .balanced,
            recognizesMultipleItems: false,
            isHighFrameRateTrackingEnabled: false,
            isHighlightingEnabled: true
        )
        scanner.delegate = context.coordinator
        return scanner
    }

    func updateUIViewController(_ scanner: DataScannerViewController, context: Context) {
        context.coordinator.parent = self
        guard !scanner.isScanning, !context.coordinator.finished else { return }
        do {
            try scanner.startScanning()
        } catch {
            onError(error.localizedDescription)
        }
    }

    static func dismantleUIViewController(_ scanner: DataScannerViewController, coordinator: Coordinator) {
        scanner.stopScanning()
    }

    func makeCoordinator() -> Coordinator { Coordinator(parent: self) }

    @MainActor
    final class Coordinator: NSObject, DataScannerViewControllerDelegate {
        var parent: WorldQRScannerView
        private(set) var finished = false

        init(parent: WorldQRScannerView) { self.parent = parent }

        func dataScanner(_ dataScanner: DataScannerViewController, didAdd addedItems: [RecognizedItem], allItems: [RecognizedItem]) {
            handle(addedItems, in: dataScanner)
        }

        func dataScanner(_ dataScanner: DataScannerViewController, didTapOn item: RecognizedItem) {
            handle([item], in: dataScanner)
        }

        func dataScanner(_ dataScanner: DataScannerViewController, becameUnavailableWithError error: DataScannerViewController.ScanningUnavailable) {
            parent.onError("Scanner unavailable: \(error)")
        }

        private func handle(_ items: [RecognizedItem], in scanner: DataScannerViewController) {
            guard !finished else { return }
            for item in items {
                guard case .barcode(let barcode) = item,
                      let payload = barcode.payloadStringValue,
                      let link = WorldConnectLink(string: payload) else { continue }
                finished = true
                scanner.stopScanning()
                parent.onLink(link)
                return
            }
        }
    }
}
