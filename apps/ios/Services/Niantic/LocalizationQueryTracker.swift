import Foundation
import CoreVideo
import simd

/// One VPS image query as the Niantic SDK reported it: the camera frame the SDK
/// submitted, what the network request did, and (once known) the device pose
/// the query produced, expressed in the Site's anchor frame.
///
/// The SDK never exposes "send this image"; it pulls the newest ARKit frame on
/// every `NSDKSession.update()` and issues `vpsLocalize` requests at the
/// configured rate. `NSDKVps2Session.localizationRequestRecords` is the only
/// window into that: one record per request, keyed by the `frameId` of the
/// submitted frame. This tracker pairs those records with the frames we fed.
struct VPSImageQuery: Identifiable, Equatable, @unchecked Sendable {
    enum Status: String, Sendable { case pending, completed, failed, frameRejected, unknown }
    enum RequestType: String, Sendable { case vpsLocalize, universalLocalize, getGraph, getReplacedNodes, registerNode, unknown }
    enum FrameMatch: String, Sendable { case exact, nearest, fallback }

    /// SDK request identifier (32-char ARDK id).
    let id: String
    let type: RequestType
    var status: Status
    /// `Vps2LocalizationError` case name; "none" when the request succeeded.
    var error: String
    let frameId: UInt64
    let frameMatch: FrameMatch
    let startedAt: Date
    var endedAt: Date?
    /// Wall-clock capture time of the query frame.
    let capturedAt: Date
    /// ARKit camera transform at capture time (ARKit world space).
    let cameraTransform: simd_float4x4
    /// Camera intrinsics and raw (landscape) resolution of the query frame.
    let intrinsics: simd_float3x3
    let imageResolution: CGSize
    /// The submitted frame. Released once the reporter has encoded it.
    var pixelBuffer: CVPixelBuffer?

    /// Anchor pose from the SDK after the response; nil for failed / rejected
    /// queries or when no anchor update followed the completion.
    var anchorTransform: simd_float4x4?
    var anchorState: String?
    var confidence: Float?
    var trackingState: BackendTrackingState = .lost

    var latencyMs: Int? { endedAt.map { Int($0.timeIntervalSince(startedAt) * 1000) } }
    var succeeded: Bool { status == .completed && error == "none" }
    var isFinal: Bool { status != .pending }

    /// Device pose at capture time in the Site frame: anchor⁻¹ · camera.
    var sitePose: SitePose? {
        anchorTransform.map { SitePose.deviceInAnchorFrame(anchor: $0, device: cameraTransform) }
    }

    static func == (a: VPSImageQuery, b: VPSImageQuery) -> Bool {
        a.id == b.id && a.status == b.status && a.error == b.error && a.endedAt == b.endedAt
            && a.trackingState == b.trackingState && (a.anchorTransform == nil) == (b.anchorTransform == nil)
    }
}

/// Aggregate counters for the UI.
struct VPSQueryStats: Equatable, Sendable {
    var issued = 0
    var succeeded = 0
    var failed = 0
    var rejected = 0
    var lastLatencyMs: Int?
    var lastError: String?
    var lastFrameMatch: VPSImageQuery.FrameMatch?
}

/// Pairs the SDK's localization request records with the camera frames that
/// were fed into `NSDKSession.update()`.
///
/// ARKit hands out camera pixel buffers from a small pool, so we cannot hold
/// many: only the last few fed frames keep their buffer (`bufferDepth`), while
/// a longer ring keeps just pose + timing (`metadataDepth`). When a request
/// turns up as `pending` we resolve its frame immediately, hand the buffer to
/// the query and drop it from the ring, so at most `bufferDepth` buffers are
/// ever retained here.
@MainActor
final class LocalizationQueryTracker {
    struct FedFrame {
        let frameId: UInt64
        let cameraTimestampMs: UInt64
        let fedAt: Date
        let capturedAt: Date
        let cameraTransform: simd_float4x4
        let intrinsics: simd_float3x3
        let imageResolution: CGSize
        var pixelBuffer: CVPixelBuffer?
    }

    /// How long a completed query waits for an anchor update carrying its pose.
    var poseGrace: TimeInterval = 0.35
    let bufferDepth: Int
    let metadataDepth: Int

    private(set) var stats = VPSQueryStats()
    private var frames: [FedFrame] = []
    private var pending: [String: VPSImageQuery] = [:]
    /// Completed successfully, waiting for the anchor update that carries the pose.
    private var awaitingPose: [VPSImageQuery] = []
    private var finished: [VPSImageQuery] = []

    init(bufferDepth: Int = 3, metadataDepth: Int = 90) {
        self.bufferDepth = bufferDepth
        self.metadataDepth = metadataDepth
    }

    /// Call right after `NSDKSession.update()` with the frame the data source
    /// handed to the SDK and the ids the SDK assigned to it.
    func recordFedFrame(frameId: UInt64, cameraTimestampMs: UInt64, snapshot: FrameSnapshot) {
        let captured = Self.wallClock(forARTimestamp: snapshot.timestamp)
        frames.append(FedFrame(frameId: frameId, cameraTimestampMs: cameraTimestampMs, fedAt: Date(), capturedAt: captured,
                               cameraTransform: snapshot.cameraTransform, intrinsics: snapshot.intrinsics,
                               imageResolution: snapshot.imageResolution, pixelBuffer: snapshot.capturedImage))
        if frames.count > metadataDepth { frames.removeFirst(frames.count - metadataDepth) }
        // Keep pixel buffers only on the newest few frames.
        let cutoff = frames.count - bufferDepth
        if cutoff > 0 {
            for i in 0..<cutoff where frames[i].pixelBuffer != nil { frames[i].pixelBuffer = nil }
        }
    }

    /// Feed the delta from `NSDKVps2Session.localizationRequestRecords`.
    func ingest(identifier: String, type: VPSImageQuery.RequestType, status: VPSImageQuery.Status, error: String,
                frameId: UInt64, startTimeMs: UInt64, endTimeMs: UInt64) {
        guard type == .vpsLocalize || type == .universalLocalize else { return }
        let started = Date(timeIntervalSince1970: TimeInterval(startTimeMs) / 1000)
        let ended = endTimeMs > 0 ? Date(timeIntervalSince1970: TimeInterval(endTimeMs) / 1000) : nil

        var query: VPSImageQuery
        if let known = pending.removeValue(forKey: identifier) {
            query = known
        } else {
            let (frame, match) = resolveFrame(frameId: frameId, startedAt: started)
            query = VPSImageQuery(
                id: identifier, type: type, status: status, error: error, frameId: frameId, frameMatch: match,
                startedAt: started, endedAt: nil, capturedAt: frame.capturedAt, cameraTransform: frame.cameraTransform,
                intrinsics: frame.intrinsics, imageResolution: frame.imageResolution, pixelBuffer: frame.pixelBuffer)
            stats.issued += 1
            stats.lastFrameMatch = match
            releaseBuffer(frameId: frame.frameId)
        }
        query.status = status
        query.error = error
        query.endedAt = ended

        switch status {
        case .pending:
            pending[identifier] = query
        case .completed where error == "none":
            stats.succeeded += 1
            stats.lastLatencyMs = query.latencyMs
            stats.lastError = nil
            awaitingPose.append(query)
        case .frameRejected:
            stats.rejected += 1
            stats.lastError = error
            finished.append(query)
        default:
            stats.failed += 1
            stats.lastLatencyMs = query.latencyMs ?? stats.lastLatencyMs
            stats.lastError = error
            finished.append(query)
        }
    }

    /// An anchor update arrived: attach its pose to every query waiting for one.
    func attachAnchor(transform: simd_float4x4?, state: String, confidence: Float?, tracking: BackendTrackingState) {
        guard !awaitingPose.isEmpty else { return }
        for var query in awaitingPose {
            query.anchorTransform = transform
            query.anchorState = state
            query.confidence = confidence
            query.trackingState = transform == nil ? .lost : tracking
            finished.append(query)
        }
        awaitingPose.removeAll()
    }

    /// Give up on queries whose anchor update never came, using the last known
    /// anchor if there is one so the pose is still drawable.
    func expireAwaiting(now: Date = Date(), fallbackAnchor: simd_float4x4?, fallbackState: BackendTrackingState) {
        guard !awaitingPose.isEmpty else { return }
        var kept: [VPSImageQuery] = []
        for var query in awaitingPose {
            let age = now.timeIntervalSince(query.endedAt ?? query.startedAt)
            if age < poseGrace { kept.append(query); continue }
            query.anchorTransform = fallbackAnchor
            query.anchorState = fallbackAnchor == nil ? "notTracked" : "limited"
            query.trackingState = fallbackAnchor == nil ? .lost : fallbackState
            finished.append(query)
        }
        awaitingPose = kept
        // Requests that never left `pending` (e.g. the SDK stopped) are dropped after a while.
        let stale = pending.values.filter { now.timeIntervalSince($0.startedAt) > 30 }
        for query in stale { pending.removeValue(forKey: query.id) }
    }

    /// Finalised queries since the last call, oldest first.
    func drainFinished() -> [VPSImageQuery] {
        defer { finished.removeAll() }
        return finished
    }

    func reset() {
        frames.removeAll()
        pending.removeAll()
        awaitingPose.removeAll()
        finished.removeAll()
        stats = VPSQueryStats()
    }

    // MARK: - frame matching

    private func resolveFrame(frameId: UInt64, startedAt: Date) -> (FedFrame, VPSImageQuery.FrameMatch) {
        if frameId != 0, let exact = frames.last(where: { $0.frameId == frameId }) {
            return (exact, .exact)
        }
        // Newest frame fed before the request went out (small tolerance for clock skew).
        let limit = startedAt.addingTimeInterval(0.02)
        if let nearest = frames.last(where: { $0.fedAt <= limit }) {
            return (nearest, .nearest)
        }
        if let newest = frames.last { return (newest, .fallback) }
        // Nothing fed yet: synthesise an empty frame so the record is still reported.
        let empty = FedFrame(frameId: frameId, cameraTimestampMs: 0, fedAt: startedAt, capturedAt: startedAt,
                             cameraTransform: matrix_identity_float4x4, intrinsics: matrix_identity_float3x3,
                             imageResolution: .zero, pixelBuffer: nil)
        return (empty, .fallback)
    }

    private func releaseBuffer(frameId: UInt64) {
        guard let index = frames.lastIndex(where: { $0.frameId == frameId }) else { return }
        frames[index].pixelBuffer = nil
    }

    /// ARKit timestamps are seconds since boot (`systemUptime`); convert to wall clock.
    static func wallClock(forARTimestamp timestamp: TimeInterval) -> Date {
        let age = ProcessInfo.processInfo.systemUptime - timestamp
        return Date().addingTimeInterval(-max(0, age))
    }
}
