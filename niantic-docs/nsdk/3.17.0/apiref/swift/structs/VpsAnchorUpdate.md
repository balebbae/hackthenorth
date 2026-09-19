---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/VpsAnchorUpdate/
title: VpsAnchorUpdate
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `VpsAnchorUpdate`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct VpsAnchorUpdate: CustomStringConvertible
```

</div>

</div>

Contains the latest tracking information for a VPS anchor.

`AnchorUpdate` provides comprehensive information about an anchor's current state, including its pose, tracking quality, and status information. This data is updated as VPS refines its localization.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Anchor updates are retrieved via `getAnchorUpdate(anchorId:)` and provide the most current information about an anchor's position, orientation, and tracking status. The data includes confidence metrics and timestamps for quality assessment.

## Example Usage<a href="#example-usage" class="hash-link" aria-label="Direct link to Example Usage" title="Direct link to Example Usage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let (status, update) = vpsSession.getAnchorUpdate(anchorId: anchorId)
if status.isOk() {
    print("Anchor ID: \(update.anchorId)")
    print("Pose: \(update.anchorToLocalTransform)")
    print("Tracking State: \(update.trackingState)")
    print("Confidence: \(update.trackingConfidence)")

    if update.trackingState == .tracked && update.trackingConfidence > 0.8 {
        // Use anchor pose for AR content placement
        placeARContent(at: update.anchorToLocalTransform)
    }
}
```

</div>

</div>

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `anchorId`<a href="#anchorid" class="hash-link" aria-label="Direct link to anchorid" title="Direct link to anchorid">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var anchorId: ArdkVpsAnchorId
```

</div>

</div>

The unique identifier of the anchor.

### `anchorToLocalTransform`<a href="#anchortolocaltransform" class="hash-link" aria-label="Direct link to anchortolocaltransform" title="Direct link to anchortolocaltransform">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var anchorToLocalTransform: simd_float4x4?
```

</div>

</div>

The 4x4 transformation matrix from anchor space to local tracking space.

This matrix represents the anchor's position and orientation relative to the device's current local coordinate system. Use this for placing AR content relative to the anchor.

### `trackingState`<a href="#trackingstate" class="hash-link" aria-label="Direct link to trackingstate" title="Direct link to trackingstate">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var trackingState: AnchorTrackingState
```

</div>

</div>

The current tracking state of the anchor.

Indicates whether the anchor is being tracked and how reliable the pose data is. See `AnchorTrackingState` for detailed information about each state.

### `trackingStateReason`<a href="#trackingstatereason" class="hash-link" aria-label="Direct link to trackingstatereason" title="Direct link to trackingstatereason">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var trackingStateReason: AnchorTrackingStateReason
```

</div>

</div>

Additional context about the tracking state.

Provides specific reasons for tracking issues or state changes, helping applications understand and respond to tracking problems.

### `trackingConfidence`<a href="#trackingconfidence" class="hash-link" aria-label="Direct link to trackingconfidence" title="Direct link to trackingconfidence">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var trackingConfidence: Float?
```

</div>

</div>

Confidence score for the current tracking estimate.

A value between 0.0 and 1.0 indicating the reliability of the pose estimate. Higher values indicate more reliable tracking. Use this to determine whether the pose data is suitable for your application.

### `timestampMs`<a href="#timestampms" class="hash-link" aria-label="Direct link to timestampms" title="Direct link to timestampms">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var timestampMs: UInt64?
```

</div>

</div>

Timestamp when this update was generated (in milliseconds since epoch).

### `description`<a href="#description" class="hash-link" aria-label="Direct link to description" title="Direct link to description">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var description: String
```

</div>

</div>

</div>

</div>
