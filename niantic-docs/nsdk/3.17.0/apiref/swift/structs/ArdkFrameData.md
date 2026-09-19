---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/ArdkFrameData/
title: ArdkFrameData
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `ArdkFrameData`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct ArdkFrameData: Equatable
```

</div>

</div>

A complete frame of data captured from an AR session.

`ArdkFrameData` encapsulates all the sensor data, images, and tracking information from a single AR frame. This includes camera images, depth data, device pose, GPS location, compass heading, and camera intrinsics.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Frame data is the primary input to ARDK for all AR processing tasks including:

- Visual positioning and localization
- 3D scanning and reconstruction
- Map building and tracking
- AR location positioning

## Example Usage<a href="#example-usage" class="hash-link" aria-label="Direct link to Example Usage" title="Direct link to Example Usage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
// In your ARSession delegate
func session(_ session: ARSession, didUpdate frame: ARFrame) {
    let frameData = ArdkFrameData(
        timestampMs: UInt64(frame.timestamp * 1000),
        cameraImage: RawImage(from: frame.capturedImage),
        depthImage: frame.sceneDepth?.depthMap.flatMap { RawImage(from: $0) },
        // ... other data
    )
    ardkSession.sendFrame(frameData)
}
```

</div>

</div>

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `frameId`<a href="#frameid" class="hash-link" aria-label="Direct link to frameid" title="Direct link to frameid">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var frameId: UInt32
```

</div>

</div>

Unique identifier for this frame.

Used to track and correlate frame data across different processing stages.

### `compassData`<a href="#compassdata" class="hash-link" aria-label="Direct link to compassdata" title="Direct link to compassdata">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var compassData: CompassData?
```

</div>

</div>

Compass and magnetometer data for device heading.

Optional compass data providing device orientation relative to magnetic north. Used for location-based AR features and waypoint navigation.

### `gpsData`<a href="#gpsdata" class="hash-link" aria-label="Direct link to gpsdata" title="Direct link to gpsdata">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var gpsData: GpsData?
```

</div>

</div>

GPS location data for geographic positioning.

Optional GPS data providing device location coordinates and accuracy. Used for AR location positioning and location-based AR experiences.

### `cameraTimestampMs`<a href="#cameratimestampms" class="hash-link" aria-label="Direct link to cameratimestampms" title="Direct link to cameratimestampms">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var cameraTimestampMs: UInt64
```

</div>

</div>

Timestamp when the camera frame was captured (in milliseconds).

This timestamp is used to synchronize camera data with other sensor data and maintain temporal consistency across processing stages.

### `cameraTransform`<a href="#cameratransform" class="hash-link" aria-label="Direct link to cameratransform" title="Direct link to cameratransform">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var cameraTransform: simd_float4x4
```

</div>

</div>

4x4 transformation matrix representing camera pose in world coordinates.

This matrix transforms points from camera coordinate space to world coordinate space. It includes both the camera's position and orientation.

### `cameraPlane0`<a href="#cameraplane0" class="hash-link" aria-label="Direct link to cameraplane0" title="Direct link to cameraplane0">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var cameraPlane0: CameraPlane?
```

</div>

</div>

First plane of camera image data (typically Y/luminance for YUV formats).

For multi-plane image formats, this contains the primary image data. For single-plane formats, this contains all the image data.

### `cameraPlane1`<a href="#cameraplane1" class="hash-link" aria-label="Direct link to cameraplane1" title="Direct link to cameraplane1">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var cameraPlane1: CameraPlane?
```

</div>

</div>

Second plane of camera image data (typically U or interleaved UV for YUV formats).

Only used for multi-plane image formats. May be nil for single-plane formats.

### `cameraPlane2`<a href="#cameraplane2" class="hash-link" aria-label="Direct link to cameraplane2" title="Direct link to cameraplane2">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var cameraPlane2: CameraPlane?
```

</div>

</div>

Third plane of camera image data (typically V for YUV formats).

Only used for three-plane image formats. May be nil for single or dual-plane formats.

### `cameraIntrinsics`<a href="#cameraintrinsics" class="hash-link" aria-label="Direct link to cameraintrinsics" title="Direct link to cameraintrinsics">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var cameraIntrinsics: CameraIntrinsics?
```

</div>

</div>

Camera intrinsic parameters for the camera image.

Contains focal length, principal point, and resolution information needed for accurate 3D reconstruction and geometric processing.

### `cameraImageWidth`<a href="#cameraimagewidth" class="hash-link" aria-label="Direct link to cameraimagewidth" title="Direct link to cameraimagewidth">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var cameraImageWidth: UInt32
```

</div>

</div>

Width of the camera image in pixels.

### `cameraImageHeight`<a href="#cameraimageheight" class="hash-link" aria-label="Direct link to cameraimageheight" title="Direct link to cameraimageheight">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var cameraImageHeight: UInt32
```

</div>

</div>

Height of the camera image in pixels.

### `cameraImageFormat`<a href="#cameraimageformat" class="hash-link" aria-label="Direct link to cameraimageformat" title="Direct link to cameraimageformat">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var cameraImageFormat: ImageFormat
```

</div>

</div>

Format of the camera image data.

Specifies how the pixel data in the camera planes is organized and interpreted.

### `depthData`<a href="#depthdata" class="hash-link" aria-label="Direct link to depthdata" title="Direct link to depthdata">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var depthData: UnsafePointer\<Float\>?
```

</div>

</div>

Raw depth values as floating-point distances.

Each value represents the distance from the depth camera to the corresponding pixel in meters. May be nil if depth data is not available.

### `depthConfidenceData`<a href="#depthconfidencedata" class="hash-link" aria-label="Direct link to depthconfidencedata" title="Direct link to depthconfidencedata">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var depthConfidenceData: UnsafePointer\<UInt8\>?
```

</div>

</div>

Confidence values for each depth measurement.

Each byte represents the confidence of the corresponding depth value, with higher values indicating more reliable depth measurements.

### `depthCameraIntrinsics`<a href="#depthcameraintrinsics" class="hash-link" aria-label="Direct link to depthcameraintrinsics" title="Direct link to depthcameraintrinsics">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var depthCameraIntrinsics: CameraIntrinsics?
```

</div>

</div>

Camera intrinsic parameters for the depth camera.

May differ from camera intrinsics if the depth camera has different resolution or optical properties than the color camera.

### `depthCameraPose`<a href="#depthcamerapose" class="hash-link" aria-label="Direct link to depthcamerapose" title="Direct link to depthcamerapose">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var depthCameraPose: simd_float4x4
```

</div>

</div>

4x4 transformation matrix representing depth camera pose.

Transforms points from depth camera coordinate space to world coordinate space. May differ from camera transform if cameras are not perfectly aligned.

### `depthImageWidth`<a href="#depthimagewidth" class="hash-link" aria-label="Direct link to depthimagewidth" title="Direct link to depthimagewidth">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var depthImageWidth: UInt32
```

</div>

</div>

Width of the depth image in pixels.

### `depthImageHeight`<a href="#depthimageheight" class="hash-link" aria-label="Direct link to depthimageheight" title="Direct link to depthimageheight">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var depthImageHeight: UInt32
```

</div>

</div>

Height of the depth image in pixels.

### `depthAndConfidenceImageDataLength`<a href="#depthandconfidenceimagedatalength" class="hash-link" aria-label="Direct link to depthandconfidenceimagedatalength" title="Direct link to depthandconfidenceimagedatalength">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var depthAndConfidenceImageDataLength: UInt32
```

</div>

</div>

Total length of depth and confidence data arrays.

This represents the combined size of the depth and confidence data buffers.

### `screenOrientation`<a href="#screenorientation" class="hash-link" aria-label="Direct link to screenorientation" title="Direct link to screenorientation">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var screenOrientation: UIInterfaceOrientation
```

</div>

</div>

Current screen orientation of the device.

Used to properly orient AR content relative to the device's physical orientation.

### `trackingState`<a href="#trackingstate" class="hash-link" aria-label="Direct link to trackingstate" title="Direct link to trackingstate">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var trackingState: ARCamera.TrackingState
```

</div>

</div>

Current ARKit tracking state.

Indicates the quality and reliability of the device's pose tracking.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init()`<a href="#init" class="hash-link" aria-label="Direct link to init" title="Direct link to init">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init()
```

</div>

</div>

</div>

</div>
