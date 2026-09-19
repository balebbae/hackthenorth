---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/ArdkObjectDetectionSession/
title: ArdkObjectDetectionSession
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `ArdkObjectDetectionSession`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public final class ArdkObjectDetectionSession: ArdkSession.IDisposable, ArdkFeatureSession
```

</div>

</div>

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `classNames`<a href="#classnames" class="hash-link" aria-label="Direct link to classnames" title="Direct link to classnames">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var classNames: ObjectDetectionClassNamesBuffer?
```

</div>

</div>

Returns the list of possible object detection classifications, if available. Reads from the currently loaded native model and returns its data.

- Returns: The list of possible object detection classifications, or `nil` if not available.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `modelToImageTransform(forPhysicalOrientation:)`<a href="#modeltoimagetransformforphysicalorientation" class="hash-link" aria-label="Direct link to modeltoimagetransformforphysicalorientation" title="Direct link to modeltoimagetransformforphysicalorientation">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func modelToImageTransform(forPhysicalOrientation orientation: UIInterfaceOrientation) -> CGAffineTransform?
```

</div>

</div>

Returns an affine transform that maps coordinates from the model's frame to the image frame, accounting for the model image being rotated to align with gravity, while the source image is always oriented in landscape.

- Parameter orientation: The gravity aligned interface orientation.
- Returns: A `CGAffineTransform` to convert model coordinates to image coordinates, or `nil` if the model frame size, source frame size, or orientation is unavailable.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name        | Description                                |
|-------------|--------------------------------------------|
| orientation | The gravity aligned interface orientation. |

### `featureStatus()`<a href="#featurestatus" class="hash-link" aria-label="Direct link to featurestatus" title="Direct link to featurestatus">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func featureStatus() -> ArdkFeatureStatus
```

</div>

</div>

Reports the current status of the object detection feature.

This method can be used to detect errors that have occurred within the feature’s internal processes. Once an error is flagged, it will remain flagged until the relevant process has been rerun and completed successfully.

Typical usage is to call this at the beginning of a session to check whether object detection is still initializing or if a previous failure has occurred.

- Returns: An `ArdkFeatureStatus` value

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

#### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

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

Starts the object detection session.

### `stop()`<a href="#stop" class="hash-link" aria-label="Direct link to stop" title="Direct link to stop">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func stop()
```

</div>

</div>

Stops the object detection session. After stopping, the session can be reconfigured and restarted.

### `latestDetections()`<a href="#latestdetections" class="hash-link" aria-label="Direct link to latestdetections" title="Direct link to latestdetections">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func latestDetections() -> ArdkAsyncState<ObjectDetectionResult, AwarenessError>
```

</div>

</div>

Retrieves the latest object detection results from the object detection session.

- Returns: An `ArdkAsyncState` containing either the latest `ObjectDetectionResult`, or an `AwarenessError`.

### `metadata()`<a href="#metadata" class="hash-link" aria-label="Direct link to metadata" title="Direct link to metadata">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func metadata() -> ArdkAsyncState<ObjectDetectionMetadata, AwarenessError>
```

</div>

</div>

Retrieves the metadata for object detection.

- Returns: An `ArdkAsyncState` containing either the latest `ObjectDetectionMetadata`, or an `AwarenessError`.

</div>

</div>
