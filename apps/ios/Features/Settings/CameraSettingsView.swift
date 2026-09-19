import SwiftUI

/// Edits the shared camera and Niantic capture settings.
struct CameraSettingsView: View {
    @EnvironmentObject private var settingsStore: CameraSettingsStore
    @EnvironmentObject private var roleStore: RoleStore
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            Form {
                Section("ARKit session") {
                    Picker("Frame rate", selection: $settingsStore.settings.preferredFrameRate) {
                        Text("30 fps").tag(30)
                        Text("60 fps").tag(60)
                    }
                    .accessibilityIdentifier("settings.frameRate")
                    Toggle("LiDAR scene depth", isOn: $settingsStore.settings.sceneDepthEnabled)
                        .accessibilityIdentifier("settings.sceneDepth")
                    Toggle("Smoothed depth", isOn: $settingsStore.settings.smoothedDepth)
                        .disabled(!settingsStore.settings.sceneDepthEnabled)
                }

                Section {
                    Picker("Capture interval", selection: $settingsStore.settings.captureIntervalMs) {
                        ForEach([100, 200, 300, 500, 1000], id: \.self) { ms in
                            Text("\(ms) ms").tag(ms)
                        }
                    }
                    .pickerStyle(.menu)
                    .accessibilityIdentifier("settings.captureInterval")
                    Stepper(value: $settingsStore.settings.maxImageDimension, in: 160...1920, step: 160) {
                        LabeledContent("Max image side", value: "\(settingsStore.settings.maxImageDimension) px")
                    }
                    HStack {
                        Text("JPEG quality")
                        Slider(value: $settingsStore.settings.jpegQuality, in: 0.1...1.0, step: 0.1)
                        Text(String(format: "%.1f", settingsStore.settings.jpegQuality))
                            .font(.system(.body, design: .monospaced))
                    }
                } header: {
                    Text("Niantic capture")
                } footer: {
                    Text("The front phone snapshots the camera at this interval and posts each frame to Niantic Spatial.")
                }

                Section {
                    TextField("Endpoint URL", text: $settingsStore.settings.nianticEndpoint)
                        .textInputAutocapitalization(.never)
                        .autocorrectionDisabled()
                        .keyboardType(.URL)
                        .accessibilityIdentifier("settings.endpoint")
                    SecureField("Developer token", text: $settingsStore.settings.nianticToken)
                        .accessibilityIdentifier("settings.token")
                } header: {
                    Text("Niantic credentials")
                } footer: {
                    Text(settingsStore.settings.hasNianticCredentials
                         ? "Queries will be sent."
                         : "No token set. Queries are captured and logged but not sent.")
                }

                if let error = settingsStore.settings.validationError {
                    Section {
                        Label(error, systemImage: "exclamationmark.triangle.fill")
                            .foregroundStyle(AppTheme.coral)
                            .accessibilityIdentifier("settings.validationError")
                    }
                }

                Section("Device") {
                    LabeledContent("Role", value: roleStore.role?.title ?? "Not set")
                    Button("Change role") {
                        roleStore.clear()
                        dismiss()
                    }
                    .accessibilityIdentifier("settings.changeRole")
                    Button("Reset settings", role: .destructive) {
                        settingsStore.reset()
                    }
                    .accessibilityIdentifier("settings.reset")
                }
            }
            .scrollContentBackground(.hidden)
            .background(AppTheme.canvas)
            .navigationTitle("Settings")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .confirmationAction) {
                    Button("Done") { dismiss() }
                        .accessibilityIdentifier("settings.done")
                }
            }
        }
    }
}
