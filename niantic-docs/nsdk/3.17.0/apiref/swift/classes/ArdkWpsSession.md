---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/ArdkWpsSession/
title: ArdkWpsSession
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `ArdkWpsSession`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public final class ArdkWpsSession: ArdkSession.IDisposable
```

</div>

</div>

A session for World Positioning System (WPS) functionality.

WPS provides the 3D position and orientation of the device in geographic coordinates as an alternative to using device GPS and compass heading data. WPS provides greater accuracy and frame-to-frame stability than standard GPS positioning, making it more suitable for AR applications. As the user moves around, WPS maintains the device's position, making it suitable for continuous use over long periods of time and long distances. WPS will work in any location where the phone has a GPS signal, but the accuracy will vary depending on GPS accuracy.

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

## Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let status = wpsSession.getFeatureStatus()
if !status.isOk() {
    print("WPS has encountered an error")
}
```

</div>

</div>

### `configure(with:)`<a href="#configurewith" class="hash-link" aria-label="Direct link to configurewith" title="Direct link to configurewith">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func configure(with config: Configuration) throws
```

</div>

</div>

Configures the session with the specified settings.

- Attention: This method must be called while the session is stopped, or else configuration will fail. In that case, while this function returns without throwing, configuration will still fail asynchronously. Use `featureStatus()` to check that configuration has not failed.
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

Starts the WPS system.

This begings the process of collecting some local device sensor data that is needed for localization.

### `stop()`<a href="#stop" class="hash-link" aria-label="Direct link to stop" title="Direct link to stop">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func stop()
```

</div>

</div>

Stops the WPS system.

This halts all WPS processing. The session can be reconfigured and restarted after stopping.

### `latestLocation()`<a href="#latestlocation" class="hash-link" aria-label="Direct link to latestlocation" title="Direct link to latestlocation">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func latestLocation() -> Result<WpsLocation, WpsError>
```

</div>

</div>

Gets the transform of the latest geolocation estimate.

This exposes the low level data that can be used to pin geolocated content into the AR coordinate system. To retrieve simplified device specific coordinates and heading, see `devicePoseAsGeolocation(_:)`.

- Note: An `ArdkError.invalidOperation` if the session is not started.
- Returns: The location transform, if available, or an error code otherwise.

### `devicePoseAsGeolocation(pose:)`<a href="#deviceposeasgeolocationpose" class="hash-link" aria-label="Direct link to deviceposeasgeolocationpose" title="Direct link to deviceposeasgeolocationpose">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func devicePoseAsGeolocation(pose: simd_float4x4) -> Result<GeolocationData, WpsError>
```

</div>

</div>

Use WPS to get an estimated geolocation for a pose in AR space.

- Parameter pose: A pose in the device's AR space.
- Returns: The estimated geolocation, if available, or an error code otherwise.

#### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description                      |
|------|----------------------------------|
| pose | A pose in the device’s AR space. |

</div>

</div>
