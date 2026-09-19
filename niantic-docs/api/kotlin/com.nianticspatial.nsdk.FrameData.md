---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.FrameData/
title: FrameData
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk/ "com.nianticspatial.nsdk") 

</div>

<div class="api-title">

#  FrameData

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">FrameData</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Container for all frame data sent to ARDK for processing. FrameData encapsulates camera frames, sensor data, and metadata that ARDK uses for tracking, mapping, VPS localization, and other AR features. Create one FrameData instance per camera frame and populate it with available sensor data before calling \[NSDKSession.sendFrame\].

## Required Data<a href="#required-data" class="hash-link" aria-label="Direct link to Required Data" title="Direct link to Required Data">​</a>

- \[cameraTimestampMs\] - Frame timestamp for synchronization
- \[frameId\] - Unique identifier for this frame

## Optional Data<a href="#optional-data" class="hash-link" aria-label="Direct link to Optional Data" title="Direct link to Optional Data">​</a>

- \[cameraImagePlanes\] - Camera image data (YUV420_888 format)
- \[cameraImageWidth\] - Width of the camera image in pixels
- \[cameraImageHeight\] - Height of the camera image in pixels
- \[cameraImageFormat\] - Format of the camera image (YUV_420_888 or 0 if none)
- \[cameraPose\] - Camera pose in world coordinates
- \[cameraIntrinsics\] - Camera calibration parameters
- \[depthImageData\] - Depth buffer (Float32, meters per pixel)
- \[depthConfidenceData\] - Per-pixel depth confidence (UInt8)
- \[depthImageDataWidth\] - Width of the depth image in pixels
- \[depthImageDataHeight\] - Height of the depth image in pixels
- \[depthImageIntrinsics\] - Depth camera intrinsics (falls back to scaled camera intrinsics if null)
- \[location\] - GPS location data
- \[compass\] - Compass/magnetometer data
- \[screenOrientation\] - Device orientation
- \[trackingState\] - ARCore tracking state

## Samples<a href="#samples" class="hash-link" aria-label="Direct link to Samples" title="Direct link to Samples">​</a>

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val frameData = FrameData(
    cameraTimestampMs = System.currentTimeMillis(),
    frameId = frameCounter++
).apply {
    cameraImagePlanes = image.planes
    cameraPose = camera.pose
    cameraIntrinsics = camera.intrinsics
    location = locationManager.lastKnownLocation
    screenOrientation = Orientation.PORTRAIT
    trackingState = frame.camera.trackingState
}
ARDK.SendFrame(handle, frameData)
```

</div>

</div>

## See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

- NSDKSession.sendFrame
- NSDKSession.getRequestedDataFormats

------------------------------------------------------------------------

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

<table class="api-table">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr class="api-table-row">
<td><span id="property-cameraimageformat"></span><span class="ctoken-line"><span class="ctoken class-name">cameraImageFormat</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
Format of the camera image data.<br />
Should be <code>ImageFormat.YUV_420_888</code> for valid image data,<br />
or <code>0</code> if no image data is provided.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-cameraimageheight"></span><span class="ctoken-line"><span class="ctoken class-name">cameraImageHeight</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
Height of the camera image in pixels.<br />
Should match the height of the image data in [cameraImagePlanes].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-cameraimageplanes"></span><span class="ctoken-line"><span class="ctoken class-name">cameraImagePlanes</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Array</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name">Plane</span><span class="ctoken punctuation">&gt;</span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Camera image data as YUV420_888 format planes.<br />
The raw camera image data used for computer vision processing.<br />
Should be in Android's YUV_420_888 format from the camera.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-cameraimagewidth"></span><span class="ctoken-line"><span class="ctoken class-name">cameraImageWidth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
Width of the camera image in pixels.<br />
Should match the width of the image data in [cameraImagePlanes].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-cameraintrinsics"></span><span class="ctoken-line"><span class="ctoken class-name">cameraIntrinsics</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.CameraIntrinsics/" title="Camera intrinsics. This is a copy of the ARCore CameraIntrinsics class.">CameraIntrinsics</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Camera intrinsic calibration parameters.<br />
Contains focal length, principal point, and lens distortion parameters<br />
needed for accurate 3D reconstruction and computer vision processing.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-camerapose"></span><span class="ctoken-line"><span class="ctoken class-name">cameraPose</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developers.google.com/ar/reference/java/com/google/ar/core/Pose" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Pose</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Camera pose in world coordinates.<br />
The 6-DOF pose (position and orientation) of the camera in world space.<br />
This is typically provided by ARCore's tracking system.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-cameratimestampms"></span><span class="ctoken-line"><span class="ctoken class-name">cameraTimestampMs</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Long</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-compass"></span><span class="ctoken-line"><span class="ctoken class-name">compass</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Compass/" title="Browse to Compass">Compass</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Most recent compass/magnetometer data from the device.<br />
Provides magnetic heading information that can improve ARDK's<br />
localization accuracy, especially for VPS.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-depthconfidencedata"></span><span class="ctoken-line"><span class="ctoken class-name">depthConfidenceData</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ByteArray</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Per-pixel depth confidence (UInt8). Same dimensions as [depthImageData].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-depthimagedata"></span><span class="ctoken-line"><span class="ctoken class-name">depthImageData</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">FloatArray</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Depth image buffer (Float32, meters per pixel). Used with [depthConfidenceData] and [depthImageDataWidth]/[depthImageDataHeight].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-depthimagedataheight"></span><span class="ctoken-line"><span class="ctoken class-name">depthImageDataHeight</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
Height of the depth image in pixels.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-depthimagedatawidth"></span><span class="ctoken-line"><span class="ctoken class-name">depthImageDataWidth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
Width of the depth image in pixels.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-depthimageintrinsics"></span><span class="ctoken-line"><span class="ctoken class-name">depthImageIntrinsics</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.CameraIntrinsics/" title="Camera intrinsics. This is a copy of the ARCore CameraIntrinsics class.">CameraIntrinsics</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Depth camera intrinsics; when null, native may use camera intrinsics with depth dimensions.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-frameid"></span><span class="ctoken-line"><span class="ctoken class-name">frameId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Long</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-location"></span><span class="ctoken-line"><span class="ctoken class-name">location</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Location</span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Most recent GPS location data from the device.<br />
Provides coarse geographic location that helps ARDK with<br />
area-based features like VPS coverage queries.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-screenorientation"></span><span class="ctoken-line"><span class="ctoken class-name">screenOrientation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Orientation/" title="Device orientation when capturing camera frames....">Orientation</a></span></span></td>
<td><div class="ctoken comment">
Device orientation when this frame was captured.<br />
The physical orientation of the device (portrait, landscape, etc.)<br />
which affects how ARDK interprets camera data.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-trackingstate"></span><span class="ctoken-line"><span class="ctoken class-name">trackingState</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developers.google.com/ar/reference/java/com/google/ar/core/TrackingState" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TrackingState</a></span></span></td>
<td><div class="ctoken comment">
ARCore tracking state when this frame was captured.<br />
Indicates the quality and reliability of the camera pose and<br />
tracking information for this frame.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
