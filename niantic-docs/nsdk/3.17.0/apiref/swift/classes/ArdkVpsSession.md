---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/ArdkVpsSession/
title: ArdkVpsSession
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `ArdkVpsSession`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public final class ArdkVpsSession: ArdkSession.IDisposable, ArdkFeatureSession
```

</div>

</div>

A session for Visual Positioning System (VPS) functionality.

`ArdkVpsSession` provides capabilities for precise localization using visual features. VPS can determine device position and orientation relative to a pre-mapped environment, enabling persistent AR experiences that maintain accuracy across sessions.

## Example Usage<a href="#example-usage" class="hash-link" aria-label="Direct link to Example Usage" title="Direct link to Example Usage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
// 1. Create the VPS session from your ARDK session
let vpsSession = ardkSession.createVpsSession()

// 2. Configure the session (must be done before starting)
let config = ArdkVpsSession.Configuration(
    continuousLocalizationEnabled: true,
    temporalFusionEnabled: true
)
try vpsSession.configure(with: config)

// 3. Start the session
vpsSession.start()

// 4. Track an anchor using a payload (from Geospatial Browser or previously created)
let anchorId = try vpsSession.trackAnchor(payload: anchorPayload)

// 5. Poll for anchor updates regularly (e.g., using a Timer)
// Check feature status to ensure VPS is working correctly
let featureStatus = vpsSession.featureStatus()
if !featureStatus.isOk() {
    print("VPS Feature Status Error: \(featureStatus)")
}

// Get the latest anchor update
if let update = vpsSession.anchorUpdate(anchorId: anchorId) {
    // 6. Check tracking state before placing content
    switch update.trackingState {
    case .notTracked:
        print("Anchor not tracked - waiting for localization")
    case .limited:
        print("Limited tracking - pose may be unreliable")
    case .tracked:
        // Anchor is fully tracked - safe to place content
        if let transform = update.anchorToLocalTransform {
            // Update your AR content with the anchor's transform
            anchorEntity.transform = Transform(matrix: transform)
        }
    }
}

// Optional: Create new anchors at specific poses (requires successful localization)
let newAnchorId = try vpsSession.createAnchor(at: cameraPose)

// Optional: Get payload for created anchor (only available when tracked)
if let payloadState = vpsSession.anchorPayload(anchorId: newAnchorId) {
    switch payloadState {
    case .inProgress:
        print("Payload not yet available")
    case .success(let payload):
        print("Anchor payload: \(payload)")
        // Store or share this payload for future sessions
    }
}

// Optional: Get GPS coordinates from VPS localization
// (requires gpsCorrectionForContinuousLocalization enabled in config)
let result = vpsSession.devicePoseAsGeolocation(pose: cameraPose)
switch result {
case .success(let geolocation):
    print("Lat: \(geolocation.latitude), Lon: \(geolocation.longitude)")
case .failure(let error):
    print("Geolocation error: \(error)")
}

// Stop the session when done
vpsSession.stop()
```

</div>

</div>

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `featureStatus()`<a href="#featurestatus" class="hash-link" aria-label="Direct link to featurestatus" title="Direct link to featurestatus">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func featureStatus() -> ArdkFeatureStatus
```

</div>

</div>

Reports errors that have occurred within processes running inside this feature.

Check this periodically to see if any errors have occurred with processes running inside this feature. Once an error has been flagged, it will remain flagged until the culprit process has been run again and completed successfully.

- Returns: Feature status flags for any issues that have occurred

### `configure(with:)`<a href="#configurewith" class="hash-link" aria-label="Direct link to configurewith" title="Direct link to configurewith">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func configure(with config: Configuration) throws
```

</div>

</div>

Configures the session with the specified settings.

- Attention: This method must be called while the session is stopped, or configuration will fail. In that case, while this function returns without throwing, configuration will still fail asynchronously. Use `featureStatus()` to check that configuration has not failed.
- Parameter config: An object that defines this session's behavior. Only settings that differ from the defaults will be applied.
- Throws: `ArdkError.invalidArgument` if the configuration is invalid. Check ARDK's C logs for more information.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| config | An object that defines this session’s behavior. Only settings that differ from the defaults will be applied. |

### `start()`<a href="#start" class="hash-link" aria-label="Direct link to start" title="Direct link to start">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func start()
```

</div>

</div>

Starts the VPS session.

This begings the process of collecting some local device sensor data that is needed for localization. In order to actually localize, `trackAnchor(payload:)` must be called.

### `stop()`<a href="#stop" class="hash-link" aria-label="Direct link to stop" title="Direct link to stop">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func stop()
```

</div>

</div>

Stops the VPS.

This halts all VPS processing and anchor tracking. The session can be reconfigured and restarted after stopping.

### `createAnchor(at:)`<a href="#createanchorat" class="hash-link" aria-label="Direct link to createanchorat" title="Direct link to createanchorat">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func createAnchor(at pose: simd_float4x4) throws -> ArdkVpsAnchorId
```

</div>

</div>

Requests to create an anchor at the specified pose. This will create an anchor relative to the currently tracked location that can be used to localize in future sessions.

- Attention: This method requires that the session has successfully localized (an anchor was successfully tracked) before it returns a valid anchor payload for future sessions.
- Parameter pose: The 4x4 transformation matrix representing the anchor's position and orientation
- Returns: A unique identifier for the created anchor

#### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| pose | The 4x4 transformation matrix representing the anchor’s position and orientation |

### `trackAnchor(payload:)`<a href="#trackanchorpayload" class="hash-link" aria-label="Direct link to trackanchorpayload" title="Direct link to trackanchorpayload">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func trackAnchor(payload: String) throws -> ArdkVpsAnchorId
```

</div>

</div>

Requests to start tracking an anchor specified by a payload.

A VPS payload contains all the data needed to localize at a VPS-activated location. A default payload for a VPS-activated location can be obtained from the "blob" field in the details view of an entry in the Geospatial Browser, or via `anchorPayload(anchorId:)` for user-generated anchors.

- Parameter payload: Base64-encoded anchor payload
- Returns: The unique identifier of the anchor encoded in the payload
- Throws: `ArdkError.invalidArgument` if the payload is not valid.

#### Parameters<a href="#parameters-2" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name    | Description                   |
|---------|-------------------------------|
| payload | Base64-encoded anchor payload |

### `removeAnchor(withId:)`<a href="#removeanchorwithid" class="hash-link" aria-label="Direct link to removeanchorwithid" title="Direct link to removeanchorwithid">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func removeAnchor(withId anchorId: ArdkVpsAnchorId) -> Bool
```

</div>

</div>

Request to stop tracking an anchor.

Once removed, the anchor will no longer receive updates or consume processing resources.

- Precondition: `anchorId` must be exactly 32 characters long.
- Parameter anchorId: The unique identifier of the anchor to remove
- Returns: True if the anchor was removed, false if otherwise

#### Parameters<a href="#parameters-3" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name     | Description                                   |
|----------|-----------------------------------------------|
| anchorId | The unique identifier of the anchor to remove |

### `anchorUpdate(anchorId:)`<a href="#anchorupdateanchorid" class="hash-link" aria-label="Direct link to anchorupdateanchorid" title="Direct link to anchorupdateanchorid">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func anchorUpdate(anchorId: ArdkVpsAnchorId) -> VpsAnchorUpdate?
```

</div>

</div>

Gets the latest tracking update for a specified anchor.

Call this regularly to get updated anchor poses as the device moves and VPS refines the localization.

- Precondition: `anchorId` must be exactly 32 characters long.
- Parameter anchorId: The unique identifier of an anchor
- Returns: The anchor update, if it is available, `nil` if otherwise.

#### Parameters<a href="#parameters-4" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name     | Description                        |
|----------|------------------------------------|
| anchorId | The unique identifier of an anchor |

### `anchorPayload(anchorId:)`<a href="#anchorpayloadanchorid" class="hash-link" aria-label="Direct link to anchorpayloadanchorid" title="Direct link to anchorpayloadanchorid">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func anchorPayload(anchorId: ArdkVpsAnchorId) -> ArdkAsyncState<String, Never>?
```

</div>

</div>

Gets the payload data of a specified anchor.

The payload encodes the data needed to localize an anchor across multiple devices or sessions. It can be shared or stored for later use with `trackAnchor(payload:)`.

Payloads are only available after the anchor is tracked.

- Precondition: `anchorId` must be exactly 32 characters long.
- Parameter anchorId: The unique identifier of the anchor
- Returns: An `AnchorTrackingBound` representing the state of the anchor payload request:
  - `.inProgress(nil)`: The anchor is not yet tracked, so the payload is not yet available.
  - `.success(Value)`: The request completed successfully. Contains the base64-encoded payload.
  - `nil`: No anchor with id `anchorId` was found.

#### Parameters<a href="#parameters-5" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name     | Description                         |
|----------|-------------------------------------|
| anchorId | The unique identifier of the anchor |

### `sessionId()`<a href="#sessionid" class="hash-link" aria-label="Direct link to sessionid" title="Direct link to sessionid">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func sessionId() -> String?
```

</div>

</div>

Gets the unique session identifier for this VPS session.

The session identifier can be used to distinguish between different VPS sessions, useful for debugging. The ID only exists after at least one anchor has been created via `createAnchor(at:)` or `trackAnchor(payload:)`.

- Returns: The session identifier if available, `nil` if otherwise.

### `devicePoseAsGeolocation(pose:)`<a href="#deviceposeasgeolocationpose" class="hash-link" aria-label="Direct link to deviceposeasgeolocationpose" title="Direct link to deviceposeasgeolocationpose">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func devicePoseAsGeolocation(
    pose: simd_float4x4
) -> Result<GeolocationData, VpsGraphOperationError>
```

</div>

</div>

Use VPS to get an estimated geolocation for a pose in AR space.

Requires that the session was configured with `gpsCorrectionForContinuousLocalization`, enabled and the user be currently localized.

- Note: Test (private) scans currently don't have GPS data so they cannot be used with this functionality.

- Parameter pose: A pose in the device's AR space.

- Returns: The estimated geolocation, if available, or an error code otherwise.

#### Parameters<a href="#parameters-6" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description                      |
|------|----------------------------------|
| pose | A pose in the device’s AR space. |

</div>

</div>
