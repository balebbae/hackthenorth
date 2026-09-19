---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/ArdkInputDataFlags/
title: ArdkInputDataFlags
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `ArdkInputDataFlags`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct ArdkInputDataFlags: OptionSet, CustomStringConvertible, @unchecked Sendable
```

</div>

</div>

Flags indicating which types of input data are required by ARDK.

`ArdkInputDataFlags` is an option set that specifies which data types should be included in frames sent to ARDK. Use `getRequestedDataInputs()` to determine which data is currently needed, then include only the requested data types in your frame data for optimal performance.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

ARDK features dynamically request different types of input data based on:

- Which features are active (VPS, WPS, scanning, mapping)
- Current processing state and requirements
- Device capabilities and available sensors

## Example Usage<a href="#example-usage" class="hash-link" aria-label="Direct link to Example Usage" title="Direct link to Example Usage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let requiredInputs = ardkSession.getRequestedDataInputs()
var frameData = ArdkFrameData()

if requiredInputs.contains(.pose) {
    frameData.cameraTransform = currentPose
}
if requiredInputs.contains(.cameraImage) {
    frameData.cameraPlane0 = cameraPlane
}
if requiredInputs.contains(.platformDepth) {
    frameData.depthData = depthBuffer
}

ardkSession.sendFrame(frameData)
```

</div>

</div>

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `rawValue`<a href="#rawvalue" class="hash-link" aria-label="Direct link to rawvalue" title="Direct link to rawvalue">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let rawValue: UInt32
```

</div>

</div>

The raw value representing the input data flags.

### `none`<a href="#none" class="hash-link" aria-label="Direct link to none" title="Direct link to none">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static let none = ArdkInputDataFlags([])
```

</div>

</div>

No input data is required.

This indicates that ARDK doesn't currently need any input data, which may occur when all features are stopped or inactive.

### `pose`<a href="#pose" class="hash-link" aria-label="Direct link to pose" title="Direct link to pose">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static let pose = ArdkInputDataFlags(rawValue: 1 << 0)
```

</div>

</div>

Device pose (position and orientation) is required.

This includes the camera transform matrix that defines the device's position and orientation in world coordinate space.

### `deviceOrientation`<a href="#deviceorientation" class="hash-link" aria-label="Direct link to deviceorientation" title="Direct link to deviceorientation">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static let deviceOrientation = ArdkInputDataFlags(rawValue: 1 << 1)
```

</div>

</div>

Device screen orientation is required.

This indicates the physical orientation of the device screen, used for proper alignment of AR content.

### `trackingState`<a href="#trackingstate" class="hash-link" aria-label="Direct link to trackingstate" title="Direct link to trackingstate">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static let trackingState = ArdkInputDataFlags(rawValue: 1 << 2)
```

</div>

</div>

ARKit tracking state is required.

This provides information about the quality and reliability of the device's pose tracking system.

### `cameraImage`<a href="#cameraimage" class="hash-link" aria-label="Direct link to cameraimage" title="Direct link to cameraimage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static let cameraImage = ArdkInputDataFlags(rawValue: 1 << 3)
```

</div>

</div>

Camera image data is required.

This includes the color camera image planes and associated metadata like intrinsics and timestamps.

### `gpsLocation`<a href="#gpslocation" class="hash-link" aria-label="Direct link to gpslocation" title="Direct link to gpslocation">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static let gpsLocation = ArdkInputDataFlags(rawValue: 1 << 4)
```

</div>

</div>

GPS location data is required.

This includes latitude, longitude, altitude, and accuracy information from the device's location services.

### `compass`<a href="#compass" class="hash-link" aria-label="Direct link to compass" title="Direct link to compass">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static let compass = ArdkInputDataFlags(rawValue: 1 << 5)
```

</div>

</div>

Compass heading data is required.

This includes magnetic and true heading information from the device's magnetometer and compass.

### `platformDepth`<a href="#platformdepth" class="hash-link" aria-label="Direct link to platformdepth" title="Direct link to platformdepth">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public static let platformDepth = ArdkInputDataFlags(rawValue: 1 << 6)
```

</div>

</div>

Platform depth data is required.

This includes depth measurements and confidence data from LiDAR or structured light depth sensors.

### `description`<a href="#description" class="hash-link" aria-label="Direct link to description" title="Direct link to description">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var description: String
```

</div>

</div>

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(rawValue:)`<a href="#initrawvalue" class="hash-link" aria-label="Direct link to initrawvalue" title="Direct link to initrawvalue">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(rawValue: UInt32)
```

</div>

</div>

Creates input data flags with the specified raw value.

- Parameter rawValue: The raw flags value

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name     | Description         |
|----------|---------------------|
| rawValue | The raw flags value |

</div>

</div>
