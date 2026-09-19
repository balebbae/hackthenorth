import SwiftUI
import RealityKit
import ARKit

/// Chest phone screen: live camera, obstacle readout, and the Niantic query loop status.
struct FrontRoleView: View {
    @EnvironmentObject private var settingsStore: CameraSettingsStore
    @StateObject private var pipeline: FrontPipeline
    @State private var showSettings = false

    init() {
        // The store is read again in onAppear; this seeds the pipeline with defaults.
        _pipeline = StateObject(wrappedValue: FrontPipeline(settings: CameraSettingsStore().settings))
    }

    var body: some View {
        ScrollView {
            VStack(spacing: AppTheme.s16) {
                header
                cameraCard
                nianticCard
                localizationCard
                obstacleCard
                controls
            }
            .padding(.horizontal, AppTheme.s16)
            .padding(.bottom, AppTheme.s32)
        }
        .background(AppTheme.canvas.ignoresSafeArea())
        .sheet(isPresented: $showSettings) { CameraSettingsView() }
        .onChange(of: settingsStore.settings) { _, new in pipeline.applySettings(new) }
        .onDisappear { pipeline.stop() }
    }

    private var header: some View {
        HStack(alignment: .firstTextBaseline) {
            VStack(alignment: .leading, spacing: AppTheme.s4) {
                Text("Front")
                    .font(.system(size: 40, weight: .semibold))
                    .tracking(-1)
                    .foregroundStyle(AppTheme.ink)
                Text("Camera, obstacles, localization")
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
            .accessibilityIdentifier("front.settings")
        }
        .padding(.top, AppTheme.s16)
    }

    private var cameraCard: some View {
        ZStack(alignment: .topLeading) {
            Group {
                if ARSessionController.isSupported {
                    ARPreview(session: pipeline.arSession.session)
                } else {
                    VStack(spacing: AppTheme.s8) {
                        Image(systemName: "camera.metering.unknown")
                            .font(.system(size: 28))
                        Text("ARKit is not available here. Using placeholder frames.")
                            .font(.system(size: 14))
                            .multilineTextAlignment(.center)
                    }
                    .foregroundStyle(.white.opacity(0.9))
                    .padding(AppTheme.s24)
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                    .background(AppTheme.midnight)
                }
            }
            .frame(height: 260)
            .clipShape(RoundedRectangle(cornerRadius: AppTheme.radiusCard, style: .continuous))

            PillTag(text: sessionLabel, fill: sessionColor, foreground: .white, identifier: "front.sessionState")
                .padding(AppTheme.s12)
        }
    }

    private var sessionLabel: String {
        switch pipeline.arSession.state {
        case .idle: "Idle"
        case .unsupported: "No ARKit"
        case .running: pipeline.arSession.depthAvailable ? "Running · LiDAR" : "Running · no depth"
        case .failed: "Failed"
        }
    }

    private var sessionColor: Color {
        switch pipeline.arSession.state {
        case .running: AppTheme.primary
        case .failed: AppTheme.coral
        default: AppTheme.graphite
        }
    }

    private var nianticCard: some View {
        VStack(alignment: .leading, spacing: AppTheme.s12) {
            HStack {
                Text("Localization")
                    .font(.system(size: 22, weight: .bold))
                    .tracking(-0.24)
                Spacer()
                PillTag(text: pipeline.usingNSDK ? "Niantic SDK" : "No SDK", fill: pipeline.usingNSDK ? AppTheme.marigold : AppTheme.skyTint,
                        identifier: "front.nsdkMode")
            }
            let loc = pipeline.localizer
            StatRow(label: "Site", value: settingsStore.settings.nianticSiteId.isEmpty ? "not set" : settingsStore.settings.nianticSiteId)
            StatRow(label: "State", value: loc.phase.label, identifier: "front.nsdkState")
            StatRow(label: "Authorized", value: loc.isAuthorized ? "yes" : "no")
            StatRow(label: "Frames to SDK", value: "\(loc.framesSubmitted)")
            StatRow(label: "Anchor updates", value: "\(loc.anchorUpdates)")
            if let fix = loc.latestFix {
                StatRow(label: "Site position", value: String(format: "%.2f, %.2f, %.2f", fix.pose.position.x, fix.pose.position.y, fix.pose.position.z))
                StatRow(label: "Confidence", value: String(format: "%.2f", fix.confidence))
            }
            Divider()
            let rep = pipeline.reporter
            StatRow(label: "Backend", value: rep.isConfigured ? (rep.worldId ?? "resolving world") : "not configured")
            StatRow(label: "Session", value: rep.sessionId.map { String($0.prefix(8)) } ?? "–")
            StatRow(label: "Fixes / poses sent", value: "\(rep.fixesSent) / \(rep.posesSent)")
            if let node = rep.lastResponse?.nearestNode {
                StatRow(label: "Nearest node", value: String(format: "%@ · %.1f m", node.name ?? node.id, node.distanceMetres))
            }
            if let error = rep.lastError {
                StatRow(label: "Last error", value: error)
            }
        }
        .card()
    }

    private var localizationCard: some View {
        VStack(alignment: .leading, spacing: AppTheme.s12) {
            HStack {
                Text(pipeline.usingNSDK ? "REST fallback (off)" : "Niantic queries")
                    .font(.system(size: 22, weight: .bold))
                    .tracking(-0.24)
                Spacer()
                PillTag(text: pipeline.queryLoop.isRunning ? "Every \(settingsStore.settings.captureIntervalMs) ms" : "Stopped",
                        fill: pipeline.queryLoop.isRunning ? AppTheme.marigold : AppTheme.skyTint,
                        identifier: "front.queryInterval")
            }
            let s = pipeline.queryLoop.stats
            StatRow(label: "Ticks", value: "\(s.ticks)", identifier: "front.stat.ticks")
            StatRow(label: "Sent", value: "\(s.sent)", identifier: "front.stat.sent")
            StatRow(label: "Skipped (no token)", value: "\(s.skipped)", identifier: "front.stat.skipped")
            StatRow(label: "Failed", value: "\(s.failed)", identifier: "front.stat.failed")
            StatRow(label: "Dropped", value: "\(s.droppedNoFrame + s.droppedBusy)")
            StatRow(label: "Last payload", value: s.lastPayloadBytes > 0 ? "\(s.lastPayloadBytes / 1024) KB" : "–")
            StatRow(label: "Last result", value: s.lastOutcome?.label ?? "–")
        }
        .card()
    }

    private var obstacleCard: some View {
        VStack(alignment: .leading, spacing: AppTheme.s12) {
            HStack {
                Text("Obstacles")
                    .font(.system(size: 22, weight: .bold))
                    .tracking(-0.24)
                Spacer()
                PillTag(text: String(format: "Range %.1f m", settingsStore.settings.obstacleRangeMeters))
            }
            HStack(spacing: AppTheme.s8) {
                ZoneTile(title: "Left", distance: pipeline.zones.left, active: pipeline.lastDecision.haptics.left)
                ZoneTile(title: "Center", distance: pipeline.zones.center, active: pipeline.lastDecision.haptics.front)
                ZoneTile(title: "Right", distance: pipeline.zones.right, active: pipeline.lastDecision.haptics.right)
            }
            StatRow(label: "Clear path", value: String(format: "%+.2f", pipeline.zones.gapDirection))
            StatRow(label: "Open side", value: pipeline.lastDecision.openSide?.rawValue ?? "–")
            StatRow(label: "Last cue", value: pipeline.speech.lastSpoken ?? "–")
            Divider()
            StatRow(label: "Linked phones", value: pipeline.link.connectedRoles.isEmpty ? "none" : pipeline.link.connectedRoles.map(\.rawValue).joined(separator: ", "),
                    identifier: "front.link")
            StatRow(label: "Left phone sees", value: sideReading(.left))
            StatRow(label: "Right phone sees", value: sideReading(.right))
        }
        .card()
    }

    private var controls: some View {
        VStack(spacing: AppTheme.s8) {
            if pipeline.isActive {
                Button("Stop") { pipeline.stop() }
                    .buttonStyle(GhostButtonStyle())
                    .accessibilityIdentifier("front.stop")
            } else {
                Button("Start") { pipeline.start(settings: settingsStore.settings, deviceId: settingsStore.deviceId) }
                    .buttonStyle(PrimaryButtonStyle())
                    .accessibilityIdentifier("front.start")
            }
            Button("Test speech") {
                pipeline.speech.speak(SpokenCue(text: "Navigation assistant ready.", priority: .route))
            }
            .buttonStyle(GhostButtonStyle())
            .accessibilityIdentifier("front.testSpeech")
        }
    }
}

extension FrontRoleView {
    fileprivate func sideReading(_ side: DeviceRole) -> String {
        guard let reading = pipeline.sideClearances[side] else { return "no reports" }
        let age = Date().timeIntervalSince1970 - reading.timestamp
        if age > 1 { return String(format: "stale %.0fs", age) }
        return reading.nearest.map { String(format: "%.2f m", $0) } ?? "clear"
    }
}

private struct ZoneTile: View {
    let title: String
    let distance: Float?
    let active: Bool

    var body: some View {
        VStack(spacing: AppTheme.s4) {
            Text(title)
                .font(.system(size: 12, weight: .medium))
                .foregroundStyle(active ? .white : AppTheme.inkSecondary)
            Text(distance.map { String(format: "%.1f m", $0) } ?? "clear")
                .font(.system(size: 20, weight: .semibold, design: .monospaced))
                .foregroundStyle(active ? .white : AppTheme.ink)
        }
        .frame(maxWidth: .infinity)
        .padding(.vertical, AppTheme.s12)
        .background(active ? AppTheme.coral : AppTheme.canvas)
        .clipShape(RoundedRectangle(cornerRadius: AppTheme.radiusButton, style: .continuous))
        .animation(.easeInOut(duration: 0.2), value: active)
    }
}

/// RealityKit view bound to the shared session; it never configures the session itself.
private struct ARPreview: UIViewRepresentable {
    let session: ARSession

    func makeUIView(context: Context) -> ARView {
        let view = ARView(frame: .zero, cameraMode: .ar, automaticallyConfigureSession: false)
        view.session = session
        view.renderOptions = [.disableMotionBlur, .disableDepthOfField, .disablePersonOcclusion]
        return view
    }

    func updateUIView(_ uiView: ARView, context: Context) {}
}
