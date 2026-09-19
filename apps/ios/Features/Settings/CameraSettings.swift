import Foundation
import ARKit

/// One set of camera and capture settings shared by obstacle detection and the
/// Niantic query loop, so both consumers see the same ARKit session configuration.
struct CameraSettings: Codable, Equatable, Sendable {
    /// Preferred ARKit video frame rate. Falls back to the first supported format.
    var preferredFrameRate: Int = 60
    /// Request LiDAR scene depth when the device supports it.
    var sceneDepthEnabled: Bool = true
    /// Use ARKit's temporally smoothed depth instead of raw depth.
    var smoothedDepth: Bool = false
    /// How often the front phone snapshots a frame for Niantic, in milliseconds.
    var captureIntervalMs: Int = 200
    /// JPEG quality for uploaded frames, 0...1.
    var jpegQuality: Double = 0.6
    /// Longest side of the uploaded image, in pixels.
    var maxImageDimension: Int = 640
    /// Niantic Spatial endpoint the snapshots are posted to.
    var nianticEndpoint: String = "https://api.nianticspatial.com/web/v1/localize"
    /// Developer token from Scaniverse web. Empty means queries are logged, not sent.
    var nianticToken: String = ""

    static let `default` = CameraSettings()

    var captureInterval: TimeInterval { Double(captureIntervalMs) / 1000 }

    /// The endpoint as a URL, only when it is an absolute http(s) URL with a host.
    var endpointURL: URL? {
        guard let components = URLComponents(string: nianticEndpoint),
              let scheme = components.scheme?.lowercased(), scheme == "https" || scheme == "http",
              let host = components.host, !host.isEmpty,
              !nianticEndpoint.contains(" ") else { return nil }
        return components.url
    }

    var hasNianticCredentials: Bool {
        !nianticToken.trimmingCharacters(in: .whitespaces).isEmpty && endpointURL != nil
    }

    /// The single ARKit configuration every consumer runs against.
    func makeARConfiguration() -> ARWorldTrackingConfiguration {
        let config = ARWorldTrackingConfiguration()
        config.planeDetection = []
        config.isAutoFocusEnabled = true
        config.worldAlignment = .gravity

        if sceneDepthEnabled {
            if smoothedDepth, ARWorldTrackingConfiguration.supportsFrameSemantics(.smoothedSceneDepth) {
                config.frameSemantics.insert(.smoothedSceneDepth)
            } else if ARWorldTrackingConfiguration.supportsFrameSemantics(.sceneDepth) {
                config.frameSemantics.insert(.sceneDepth)
            }
        }

        let formats = ARWorldTrackingConfiguration.supportedVideoFormats
        if let match = formats.first(where: { $0.framesPerSecond == preferredFrameRate }) {
            config.videoFormat = match
        } else if let first = formats.first {
            config.videoFormat = first
        }
        return config
    }

    /// Validation used by the settings form and tests.
    var validationError: String? {
        if captureIntervalMs < 50 { return "Capture interval must be at least 50 ms." }
        if !(0.1...1.0).contains(jpegQuality) { return "JPEG quality must be between 0.1 and 1.0." }
        if maxImageDimension < 160 { return "Image dimension must be at least 160 px." }
        if endpointURL == nil { return "Endpoint must be an http(s) URL." }
        return nil
    }
}

/// Loads and saves `CameraSettings` as JSON in UserDefaults.
@MainActor
final class CameraSettingsStore: ObservableObject {
    nonisolated static let key = "cameraSettings.v1"

    @Published var settings: CameraSettings {
        didSet { persist() }
    }

    private let defaults: UserDefaults

    init(defaults: UserDefaults = .standard) {
        self.defaults = defaults
        if let data = defaults.data(forKey: Self.key),
           let decoded = try? JSONDecoder().decode(CameraSettings.self, from: data) {
            settings = decoded
        } else {
            settings = .default
        }
    }

    func reset() { settings = .default }

    private func persist() {
        if let data = try? JSONEncoder().encode(settings) {
            defaults.set(data, forKey: Self.key)
        }
    }

    nonisolated static func clearPersisted(defaults: UserDefaults = .standard) {
        defaults.removeObject(forKey: key)
    }
}
