import Foundation

/// The hand-off link the web viewer shows as a QR code
/// (`shared/contracts/README.md` › "Phone hand-off link"):
///
///     wander://connect?v=1&world=<id>&site=<nianticSiteId>&backend=<url>&name=<name>
///
/// It tells the phone *which* world, site and backend to use. Secrets (API key,
/// Niantic developer token) are never in the link; they stay in LocalConfig / Settings.
struct WorldConnectLink: Equatable, Sendable {
    static let scheme = "wander"
    static let host = "connect"
    static let version = "1"

    let worldId: String
    var nianticSiteId: String?
    var backendURL: String?
    var name: String?

    init(worldId: String, nianticSiteId: String? = nil, backendURL: String? = nil, name: String? = nil) {
        self.worldId = worldId
        self.nianticSiteId = nianticSiteId
        self.backendURL = backendURL
        self.name = name
    }

    /// Parses a scanned string or opened URL. `nil` for anything that is not a v1 connect link.
    init?(string: String) {
        guard let url = URL(string: string.trimmingCharacters(in: .whitespacesAndNewlines)) else { return nil }
        self.init(url: url)
    }

    init?(url: URL) {
        guard url.scheme?.lowercased() == Self.scheme, url.host?.lowercased() == Self.host,
              let items = URLComponents(url: url, resolvingAgainstBaseURL: false)?.queryItems else { return nil }
        var query: [String: String] = [:]
        for item in items { query[item.name] = item.value ?? "" }
        guard (query["v"] ?? Self.version) == Self.version,
              let world = query["world"], Self.isValidWorldId(world) else { return nil }
        worldId = world
        nianticSiteId = Self.nonEmpty(query["site"])
        name = Self.nonEmpty(query["name"])
        if let backend = Self.nonEmpty(query["backend"]),
           let components = URLComponents(string: backend),
           let scheme = components.scheme?.lowercased(), scheme == "https" || scheme == "http",
           let host = components.host, !host.isEmpty {
            backendURL = backend.trimmingCharacters(in: CharacterSet(charactersIn: "/"))
        } else {
            backendURL = nil
        }
    }

    /// Same shape the web builds, for tests and for showing what a code contains.
    var url: URL {
        var components = URLComponents()
        components.scheme = Self.scheme
        components.host = Self.host
        var items = [URLQueryItem(name: "v", value: Self.version), URLQueryItem(name: "world", value: worldId)]
        if let nianticSiteId { items.append(URLQueryItem(name: "site", value: nianticSiteId)) }
        if let backendURL { items.append(URLQueryItem(name: "backend", value: backendURL)) }
        if let name { items.append(URLQueryItem(name: "name", value: name)) }
        components.queryItems = items
        return components.url!
    }

    /// What the phone will call this world in the confirmation.
    var displayName: String { name ?? worldId }

    /// Fill the settings the link knows about; everything else (tokens, keys, capture) is untouched.
    /// Returns a short description of what changed.
    @discardableResult
    func apply(to settings: inout CameraSettings) -> [String] {
        var changes: [String] = []
        if settings.worldId != worldId {
            settings.worldId = worldId
            changes.append("world \(worldId)")
        }
        if let nianticSiteId, settings.nianticSiteId != nianticSiteId {
            settings.nianticSiteId = nianticSiteId
            changes.append("site \(nianticSiteId)")
        }
        if let backendURL, settings.backendURL != backendURL {
            settings.backendURL = backendURL
            changes.append("backend \(backendURL)")
        }
        return changes
    }

    static func isValidWorldId(_ id: String) -> Bool {
        id.range(of: #"^[a-z0-9][a-z0-9._-]{0,63}$"#, options: .regularExpression) != nil
    }

    private static func nonEmpty(_ value: String?) -> String? {
        guard let value = value?.trimmingCharacters(in: .whitespacesAndNewlines), !value.isEmpty else { return nil }
        return value
    }
}
