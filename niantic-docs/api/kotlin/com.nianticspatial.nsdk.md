---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk/
title: com.nianticspatial.nsdk
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") 

</div>

<div class="api-title">

#  nsdk

</div>

------------------------------------------------------------------------

## Classes<a href="#classes" class="hash-link" aria-label="Direct link to Classes" title="Direct link to Classes">​</a>

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
<td><span id="class-asyncresult"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AsyncResult/" title="Represents the final result of a completed asynchronous operation, which can either be...">AsyncResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AsyncResult/" title="Represents the final result of a completed asynchronous operation, which can either be...">AsyncResult</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name">TData</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name">TError</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ErrorCodeProvider/" title="Browse to ErrorCodeProvider">ErrorCodeProvider</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Represents the final result of a completed asynchronous operation, which can either be<br />
a success, a failure, or a timeout. *<br />
This is the public-facing result type returned by <code>suspend</code> functions. It intentionally<br />
omits an "in-progress" state, guaranteeing that the operation has reached a terminal state.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-awarenessimageparams"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessImageParams/" title="Describes inferred image results.">AwarenessImageParams</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessImageParams/" title="Describes inferred image results.">AwarenessImageParams</a></span></span></td>
<td><div class="ctoken comment">
Describes inferred image results.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-cameraintrinsics"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.CameraIntrinsics/" title="Camera intrinsics. This is a copy of the ARCore CameraIntrinsics class.">CameraIntrinsics</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.CameraIntrinsics/" title="Camera intrinsics. This is a copy of the ARCore CameraIntrinsics class.">CameraIntrinsics</a></span></span></td>
<td><div class="ctoken comment">
Camera intrinsics. This is a copy of the ARCore CameraIntrinsics class.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-cameraintrinsicsfromarcore"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.CameraIntrinsicsFromARCore/" title="Browse to CameraIntrinsicsFromARCore">CameraIntrinsicsFromARCore</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.CameraIntrinsicsFromARCore/" title="Browse to CameraIntrinsicsFromARCore">CameraIntrinsicsFromARCore</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-depthconfig"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.DepthConfig/" title="Configuration parameters for ARDK&#39;s Depth System....">DepthConfig</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.DepthConfig/" title="Configuration parameters for ARDK&#39;s Depth System....">DepthConfig</a></span></span></td>
<td><div class="ctoken comment">
Configuration parameters for ARDK's Depth System.<br />
## Basic Usage
</div>
<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">
<div class="codeBlockContent_QJqH">
<pre class="prism-code language-kotlin codeBlock_bY9V thin-scrollbar" tabindex="0" style="color:#393A34;background-color:#f6f8fa"><code>val config = DepthConfig(
framerate = 120
featureMode = AwarenessFeatureMode.SMOOTH,
)
ARDK.ConfigureDepth(handle, config)</code></pre>
</div>
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-devicemappingconfig"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.DeviceMappingConfig/" title="Browse to DeviceMappingConfig">DeviceMappingConfig</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.DeviceMappingConfig/" title="Browse to DeviceMappingConfig">DeviceMappingConfig</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-framedata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.FrameData/" title="Container for all frame data sent to ARDK for processing....">FrameData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.FrameData/" title="Container for all frame data sent to ARDK for processing....">FrameData</a></span></span></td>
<td><div class="ctoken comment">
Container for all frame data sent to ARDK for processing.<br />
FrameData encapsulates camera frames, sensor data, and metadata that ARDK<br />
uses for tracking, mapping, VPS localization, and other AR features.<br />
Create one FrameData instance per camera frame and populate it with<br />
available sensor data before calling [NSDKSession.sendFrame].<br />
## Required Data<br />
- [cameraTimestampMs] - Frame timestamp for synchronization<br />
- [frameId] - Unique identifier for this frame<br />
## Optional Data<br />
- [cameraImagePlanes] - Camera image data (YUV420_888 format)<br />
- [cameraImageWidth] - Width of the camera image in pixels<br />
- [cameraImageHeight] - Height of the camera image in pixels<br />
- [cameraImageFormat] - Format of the camera image (YUV_420_888 or 0 if none)<br />
- [cameraPose] - Camera pose in world coordinates<br />
- [cameraIntrinsics] - Camera calibration parameters<br />
- [depthImageData] - Depth buffer (Float32, meters per pixel)<br />
- [depthConfidenceData] - Per-pixel depth confidence (UInt8)<br />
- [depthImageDataWidth] - Width of the depth image in pixels<br />
- [depthImageDataHeight] - Height of the depth image in pixels<br />
- [depthImageIntrinsics] - Depth camera intrinsics (falls back to scaled camera intrinsics if null)<br />
- [location] - GPS location data<br />
- [compass] - Compass/magnetometer data<br />
- [screenOrientation] - Device orientation<br />
- [trackingState] - ARCore tracking state
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-image"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Image/" title="Browse to Image">Image</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Image/" title="Browse to Image">Image</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-meshingconfig"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.MeshingConfig/" title="Browse to MeshingConfig">MeshingConfig</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.MeshingConfig/" title="Browse to MeshingConfig">MeshingConfig</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkcamera"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkCamera/" title="Camera view over the current frame (live or playback). Mirrors ARCore [com.google.ar.core.Camera]...">NsdkCamera</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkCamera/" title="Camera view over the current frame (live or playback). Mirrors ARCore [com.google.ar.core.Camera]...">NsdkCamera</a></span></span></td>
<td><div class="ctoken comment">
Camera view over the current frame (live or playback). Mirrors ARCore [com.google.ar.core.Camera]<br />
so callers can use one API for both live and playback.<br />
Use [pose] and [getDisplayOrientedPose] for overlays, VPS2, etc. Use [imageIntrinsics] for<br />
CPU image coordinates, [trackingState] / [getTrackingFailureReason] for tracking status, and<br />
[getViewMatrix] for rendering. Use [backing] when you need ARCamera- or PlaybackCamera-specific APIs.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkfeaturealreadyinitializedstatusexception"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkFeatureAlreadyInitializedStatusException/" title="Thrown when a feature is already initialized....">NsdkFeatureAlreadyInitializedStatusException</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkFeatureAlreadyInitializedStatusException/" title="Thrown when a feature is already initialized....">NsdkFeatureAlreadyInitializedStatusException</a></span></span></td>
<td><div class="ctoken comment">
Thrown when a feature is already initialized.<br />
Corresponds to [NSDKStatus.FEATURE_ALREADY_INITIALIZED].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkfeaturenotinitializedstatusexception"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkFeatureNotInitializedStatusException/" title="Thrown when a required feature has not been initialized....">NsdkFeatureNotInitializedStatusException</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkFeatureNotInitializedStatusException/" title="Thrown when a required feature has not been initialized....">NsdkFeatureNotInitializedStatusException</a></span></span></td>
<td><div class="ctoken comment">
Thrown when a required feature has not been initialized.<br />
Corresponds to [NSDKStatus.FEATURE_NOT_INITIALIZED].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkframe"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkFrame/" title="Abstraction over the current frame so callers can use one API for both live AR (ARCore [Frame])...">NsdkFrame</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkFrame/" title="Abstraction over the current frame so callers can use one API for both live AR (ARCore [Frame])...">NsdkFrame</a></span></span></td>
<td><div class="ctoken comment">
Abstraction over the current frame so callers can use one API for both live AR (ARCore [Frame])<br />
and playback ([PlaybackFrame]). Use [camera] for pose, intrinsics, and tracking.<br />
Use [backing] when you need Frame- or PlaybackFrame-specific APIs (e.g. acquireCameraImage).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkinvalidargumentstatusexception"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkInvalidArgumentStatusException/" title="Thrown when a native argument has an invalid value....">NsdkInvalidArgumentStatusException</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkInvalidArgumentStatusException/" title="Thrown when a native argument has an invalid value....">NsdkInvalidArgumentStatusException</a></span></span></td>
<td><div class="ctoken comment">
Thrown when a native argument has an invalid value.<br />
Corresponds to [NSDKStatus.INVALID_ARGUMENT].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkinvalidhandlestatusexception"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkInvalidHandleStatusException/" title="Thrown when a native handle is invalid or has been destroyed....">NsdkInvalidHandleStatusException</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkInvalidHandleStatusException/" title="Thrown when a native handle is invalid or has been destroyed....">NsdkInvalidHandleStatusException</a></span></span></td>
<td><div class="ctoken comment">
Thrown when a native handle is invalid or has been destroyed.<br />
Corresponds to [NSDKStatus.INVALID_NSDK_HANDLE].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkinvalidoperationstatusexception"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkInvalidOperationStatusException/" title="Thrown when a native operation is not valid in the current state....">NsdkInvalidOperationStatusException</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkInvalidOperationStatusException/" title="Thrown when a native operation is not valid in the current state....">NsdkInvalidOperationStatusException</a></span></span></td>
<td><div class="ctoken comment">
Thrown when a native operation is not valid in the current state.<br />
Corresponds to [NSDKStatus.INVALID_OPERATION].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdknullargumentstatusexception"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkNullArgumentStatusException/" title="Thrown when a required native argument is null....">NsdkNullArgumentStatusException</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkNullArgumentStatusException/" title="Thrown when a required native argument is null....">NsdkNullArgumentStatusException</a></span></span></td>
<td><div class="ctoken comment">
Thrown when a required native argument is null.<br />
Corresponds to [NSDKStatus.NULL_ARGUMENT].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkresult"></span><span class="ctoken-line api-obsolete"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKResult/" title="ResultDeprecated wrapper for NSDK operations that can succeed or fail....">NSDKResult</a></span></span></td>
<td><span class="ctoken-line api-obsolete"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKResult/" title="ResultDeprecated wrapper for NSDK operations that can succeed or fail....">NSDKResult</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name">TData</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name">TError</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ErrorCodeProvider/" title="Browse to ErrorCodeProvider">ErrorCodeProvider</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
ResultDeprecated wrapper for NSDK operations that can succeed or fail.<br />
NSDKResult is a Kotlin sealed class designed to provide a type-safe abstraction<br />
over the return values of low-level C APIs. Instead of directly handling raw<br />
integer status codes from the C layer, Kotlin callers receive structured results<br />
as either Success or Error.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdksession"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKSession/" title="Creates a new NSDK instance with auth tokens or a configuration file....">NSDKSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKSession/" title="Creates a new NSDK instance with auth tokens or a configuration file....">NSDKSession</a></span></span></td>
<td><div class="ctoken comment">
Creates a new NSDK instance with auth tokens or a configuration file.<br />
This is the primary entry point for initializing NSDK functionality.<br />
You must call this before using any other NSDK features.<br />
Only one [NSDKSession] may be active at a time. Creating a second instance while one is<br />
active will throw [IllegalStateException]. Call [close] on the existing session before<br />
creating a new one.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkstatusexception"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkStatusException/" title="Base class for all NSDK-specific exceptions originating from the native layer.">NsdkStatusException</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkStatusException/" title="Base class for all NSDK-specific exceptions originating from the native layer.">NsdkStatusException</a></span></span></td>
<td><div class="ctoken comment">
Base class for all NSDK-specific exceptions originating from the native layer.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkunknownstatusexception"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkUnknownStatusException/" title="Thrown when an internal, unrecoverable error occurs in the native layer....">NsdkUnknownStatusException</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkUnknownStatusException/" title="Thrown when an internal, unrecoverable error occurs in the native layer....">NsdkUnknownStatusException</a></span></span></td>
<td><div class="ctoken comment">
Thrown when an internal, unrecoverable error occurs in the native layer.<br />
that is unexpected
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-scannerconfig"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ScannerConfig/" title="Configuration parameters for scanning functionality....">ScannerConfig</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ScannerConfig/" title="Configuration parameters for scanning functionality....">ScannerConfig</a></span></span></td>
<td><div class="ctoken comment">
Configuration parameters for scanning functionality.<br />
ScannerConfig allows you to customize scan recording behavior including recording<br />
framerate, visualization settings, depth range, and output resolution.<br />
Use this class to optimize scanning performance for your specific use case.<br />
## Basic Usage
</div>
<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">
<div class="codeBlockContent_QJqH">
<pre class="prism-code language-kotlin codeBlock_bY9V thin-scrollbar" tabindex="0" style="color:#393A34;background-color:#f6f8fa"><code>val config = ScannerConfig(
framerate = 30,
enableRaycastVisualization = true,
enableVoxelVisualization = true
)
scanningSession.configure(config)</code></pre>
</div>
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-sessionbase"></span><span class="ctoken-line"><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.SessionBase/" title="Browse to SessionBase">SessionBase</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.SessionBase/" title="Browse to SessionBase">SessionBase</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name">T</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.SessionBase/" title="Browse to SessionBase">SessionBase</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name">T</span><span class="ctoken punctuation">&gt;</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-uuidkey"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.UUIDKey/" title="Browse to UUIDKey">UUIDKey</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.UUIDKey/" title="Browse to UUIDKey">UUIDKey</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-vps2config"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Vps2Config/" title="Configuration structure for the VPS2 session.">Vps2Config</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Vps2Config/" title="Configuration structure for the VPS2 session.">Vps2Config</a></span></span></td>
<td><div class="ctoken comment">
Configuration structure for the VPS2 session.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Interfaces<a href="#interfaces" class="hash-link" aria-label="Direct link to Interfaces" title="Direct link to Interfaces">​</a>

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
<td><span id="interface-errorcodeprovider"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ErrorCodeProvider/" title="Browse to ErrorCodeProvider">ErrorCodeProvider</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ErrorCodeProvider/" title="Browse to ErrorCodeProvider">ErrorCodeProvider</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="interface-errorfactory"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ErrorFactory/" title="Browse to ErrorFactory">ErrorFactory</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ErrorFactory/" title="Browse to ErrorFactory">ErrorFactory</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name">E</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ErrorCodeProvider/" title="Browse to ErrorCodeProvider">ErrorCodeProvider</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="interface-nsdklogcallback"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkLogCallback/" title="Functional interface for receiving log messages from NSDK....">NsdkLogCallback</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkLogCallback/" title="Functional interface for receiving log messages from NSDK....">NsdkLogCallback</a></span></span></td>
<td><div class="ctoken comment">
Functional interface for receiving log messages from NSDK.<br />
This callback is invoked by the native NSDK library to send log messages<br />
to the Kotlin/Java layer. The callback receives the log level, message,<br />
and optional source location information.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="interface-nsdksessiondatasource"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkSessionDataSource/" title="Provides synchronous, pull-based access to the latest available sensor data...">NsdkSessionDataSource</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkSessionDataSource/" title="Provides synchronous, pull-based access to the latest available sensor data...">NsdkSessionDataSource</a></span></span></td>
<td><div class="ctoken comment">
Provides synchronous, pull-based access to the latest available sensor data<br />
required by [NSDKSession].<br />
All methods must be non-blocking and thread-safe. Returned values represent<br />
the most recent samples already captured by the underlying services.<br />
Implement this interface and assign it to [NSDKSession.dataSource], then call<br />
[NSDKSession.update] once per camera frame to submit data to the native layer.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Data Classes<a href="#data-classes" class="hash-link" aria-label="Direct link to Data Classes" title="Direct link to Data Classes">​</a>

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
<td><span id="data class-anchorupdate"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AnchorUpdate/" title="Contains the latest tracking information for a VPS anchor....">AnchorUpdate</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AnchorUpdate/" title="Contains the latest tracking information for a VPS anchor....">AnchorUpdate</a></span></span></td>
<td><div class="ctoken comment">
Contains the latest tracking information for a VPS anchor.<br />
<code>AnchorUpdate</code> provides comprehensive information about an anchor's current state,<br />
including its pose, tracking quality, and status information. This data is updated<br />
as VPS refines its localization.<br />
### Overview<br />
Anchor updates are retrieved via <code>getAnchorUpdate(uuid)</code> and provide the<br />
most current information about an anchor's position, orientation, and tracking status.<br />
The data includes confidence metrics and timestamps for quality assessment.<br />
### Example
</div>
<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">
<div class="codeBlockContent_QJqH">
<pre class="prism-code language-kotlin codeBlock_bY9V thin-scrollbar" tabindex="0" style="color:#393A34;background-color:#f6f8fa"><code>val update = vpsSession.getAnchorUpdate(anchorId)
println(&quot;Anchor ID: ${update.uuid}&quot;)
println(&quot;Pose: ${update.anchorToLocalTrackingTransform}&quot;)
println(&quot;Tracking State: ${update.trackingState}&quot;)
println(&quot;Confidence: ${update.trackingConfidence}&quot;)
if (update.trackingState == AnchorTrackingState.TRACKED &amp;&amp; update.trackingConfidence &gt; 0.8f) {
// Use anchor pose for AR content placement
placeARContent(update.anchorToLocalTrackingTransform)
}</code></pre>
</div>
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-areatarget"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AreaTarget/" title="Browse to AreaTarget">AreaTarget</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AreaTarget/" title="Browse to AreaTarget">AreaTarget</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-authinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AuthInfo/" title="Authentication information containing token claims....">AuthInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AuthInfo/" title="Authentication information containing token claims....">AuthInfo</a></span></span></td>
<td><div class="ctoken comment">
Authentication information containing token claims.<br />
Contains parsed JWT claims including token string, expiration, user information, and other standard JWT fields.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-awarenesscontext"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessContext/" title="Browse to AwarenessContext">AwarenessContext</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessContext/" title="Browse to AwarenessContext">AwarenessContext</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-camerasample"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.CameraSample/" title="A snapshot of camera sensor data for a single frame.">CameraSample</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.CameraSample/" title="A snapshot of camera sensor data for a single frame.">CameraSample</a></span></span></td>
<td><div class="ctoken comment">
A snapshot of camera sensor data for a single frame.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-compass"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Compass/" title="Browse to Compass">Compass</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Compass/" title="Browse to Compass">Compass</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-coveragearea"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.CoverageArea/" title="Browse to CoverageArea">CoverageArea</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.CoverageArea/" title="Browse to CoverageArea">CoverageArea</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-depthbuffer"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.DepthBuffer/" title="Depth result from ARDK&#39;s Depth System after computing disparity.">DepthBuffer</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.DepthBuffer/" title="Depth result from ARDK&#39;s Depth System after computing disparity.">DepthBuffer</a></span></span></td>
<td><div class="ctoken comment">
Depth result from ARDK's Depth System after computing disparity.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-depthsample"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.DepthSample/" title="A snapshot of platform depth data (e.g. LiDAR or ToF sensor) for a single frame.">DepthSample</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.DepthSample/" title="A snapshot of platform depth data (e.g. LiDAR or ToF sensor) for a single frame.">DepthSample</a></span></span></td>
<td><div class="ctoken comment">
A snapshot of platform depth data (e.g. LiDAR or ToF sensor) for a single frame.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-geolocationdata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.GeolocationData/" title="Browse to GeolocationData">GeolocationData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.GeolocationData/" title="Browse to GeolocationData">GeolocationData</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-latlng"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.LatLng/" title="Geographic coordinates representing latitude and longitude....">LatLng</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.LatLng/" title="Geographic coordinates representing latitude and longitude....">LatLng</a></span></span></td>
<td><div class="ctoken comment">
Geographic coordinates representing latitude and longitude.<br />
LatLng is used throughout ARDK for specifying geographic locations,<br />
particularly for VPS coverage queries and area-based operations.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-localizationtarget"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.LocalizationTarget/" title="Browse to LocalizationTarget">LocalizationTarget</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.LocalizationTarget/" title="Browse to LocalizationTarget">LocalizationTarget</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-mapmetadata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.MapMetadata/" title="Browse to MapMetadata">MapMetadata</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.MapMetadata/" title="Browse to MapMetadata">MapMetadata</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-meshdata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.MeshData/" title="Browse to MeshData">MeshData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.MeshData/" title="Browse to MeshData">MeshData</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-meshdownloaderdata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.MeshDownloaderData/" title="Browse to MeshDownloaderData">MeshDownloaderData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.MeshDownloaderData/" title="Browse to MeshDownloaderData">MeshDownloaderData</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-meshingupdateinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.MeshingUpdateInfo/" title="Browse to MeshingUpdateInfo">MeshingUpdateInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.MeshingUpdateInfo/" title="Browse to MeshingUpdateInfo">MeshingUpdateInfo</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-pathconfig"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.PathConfig/" title="Optional path overrides mirroring native ARDK_PathConfig....">PathConfig</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.PathConfig/" title="Optional path overrides mirroring native ARDK_PathConfig....">PathConfig</a></span></span></td>
<td><div class="ctoken comment">
Optional path overrides mirroring native ARDK_PathConfig.<br />
Null or empty values mean: let native auto-detect paths.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-recordinginfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.RecordingInfo/" title="Browse to RecordingInfo">RecordingInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.RecordingInfo/" title="Browse to RecordingInfo">RecordingInfo</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-scansaveinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ScanSaveInfo/" title="Information about a saved scan....">ScanSaveInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ScanSaveInfo/" title="Information about a saved scan....">ScanSaveInfo</a></span></span></td>
<td><div class="ctoken comment">
Information about a saved scan.<br />
This class contains details about a scan that has saved (or attempted to be saved),<br />
including its unique identifier, file system path, and ultimate state.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Enums<a href="#enums" class="hash-link" aria-label="Direct link to Enums" title="Direct link to Enums">​</a>

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
<td><span id="enum-agelevel"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AgeLevel/" title="Codes describing the age level of the user....">AgeLevel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AgeLevel/" title="Codes describing the age level of the user....">AgeLevel</a></span></span></td>
<td><div class="ctoken comment">
Codes describing the age level of the user.<br />
This enum represents the age classification for users of the NSDK
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-anchortrackingstate"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AnchorTrackingState/" title="Represents the current tracking state of a VPS anchor....">AnchorTrackingState</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AnchorTrackingState/" title="Represents the current tracking state of a VPS anchor....">AnchorTrackingState</a></span></span></td>
<td><div class="ctoken comment">
Represents the current tracking state of a VPS anchor.<br />
The tracking state indicates how well the system is able to track an anchor's position<br />
and orientation in the current environment. This information is crucial for determining<br />
the reliability of anchor pose data.<br />
### Overview<br />
Tracking states progress from not tracked to fully tracked, with limited tracking<br />
representing an intermediate state where tracking is possible but may be less reliable.<br />
### Example
</div>
<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">
<div class="codeBlockContent_QJqH">
<pre class="prism-code language-kotlin codeBlock_bY9V thin-scrollbar" tabindex="0" style="color:#393A34;background-color:#f6f8fa"><code>val update = vpsSession.getAnchorUpdate(anchorId)
when (update.trackingState) {
AnchorTrackingState.NOT_TRACKED -&gt;
println(&quot;Anchor is not currently being tracked&quot;)
AnchorTrackingState.LIMITED -&gt;
println(&quot;Anchor tracking is limited - pose may be unreliable&quot;)
AnchorTrackingState.TRACKED -&gt;
println(&quot;Anchor is fully tracked - pose is reliable&quot;)
}</code></pre>
</div>
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-anchortrackingstatereason"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AnchorTrackingStateReason/" title="Provides additional context about why an anchor is in a particular tracking state....">AnchorTrackingStateReason</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AnchorTrackingStateReason/" title="Provides additional context about why an anchor is in a particular tracking state....">AnchorTrackingStateReason</a></span></span></td>
<td><div class="ctoken comment">
Provides additional context about why an anchor is in a particular tracking state.<br />
When an anchor is not tracked or has limited tracking, this enum provides specific<br />
reasons that can help developers understand and respond to tracking issues.<br />
### Overview<br />
Tracking state reasons help diagnose why tracking may be failing or limited,<br />
enabling applications to provide appropriate user feedback or take corrective actions.<br />
### Example
</div>
<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">
<div class="codeBlockContent_QJqH">
<pre class="prism-code language-kotlin codeBlock_bY9V thin-scrollbar" tabindex="0" style="color:#393A34;background-color:#f6f8fa"><code>val update = vpsSession.getAnchorUpdate(anchorId)
when (update.trackingStateReason) {
AnchorTrackingStateReason.INITIALIZING -&gt;
println(&quot;Anchor is still initializing - tracking will improve&quot;)
AnchorTrackingStateReason.PERMISSION_DENIED -&gt;
println(&quot;Tracking failed due to permission issues&quot;)
AnchorTrackingStateReason.FATAL_NETWORK_ERROR -&gt;
println(&quot;Network error preventing tracking&quot;)
else -&gt;
println(&quot;Other tracking issue: ${update.trackingStateReason}&quot;)
}</code></pre>
</div>
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-awarenessfeaturemode"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessFeatureMode/" title="Browse to AwarenessFeatureMode">AwarenessFeatureMode</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessFeatureMode/" title="Browse to AwarenessFeatureMode">AwarenessFeatureMode</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-awarenessstatus"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessStatus/" title="Browse to AwarenessStatus">AwarenessStatus</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessStatus/" title="Browse to AwarenessStatus">AwarenessStatus</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-featurestatus"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.FeatureStatus/" title="Browse to FeatureStatus">FeatureStatus</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.FeatureStatus/" title="Browse to FeatureStatus">FeatureStatus</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-imagetype"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ImageType/" title="Browse to ImageType">ImageType</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ImageType/" title="Browse to ImageType">ImageType</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-inputdataflags"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.InputDataFlags/" title="Browse to InputDataFlags">InputDataFlags</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.InputDataFlags/" title="Browse to InputDataFlags">InputDataFlags</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-localizability"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Localizability/" title="Browse to Localizability">Localizability</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Localizability/" title="Browse to Localizability">Localizability</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-meshdownloadererror"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.MeshDownloaderError/" title="Browse to MeshDownloaderError">MeshDownloaderError</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.MeshDownloaderError/" title="Browse to MeshDownloaderError">MeshDownloaderError</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-nsdkstatus"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKStatus/" title="Status codes returned by NSDK operations....">NSDKStatus</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKStatus/" title="Status codes returned by NSDK operations....">NSDKStatus</a></span></span></td>
<td><div class="ctoken comment">
Status codes returned by NSDK operations.<br />
NSDKStatus represents the outcome of NSDK API calls, indicating<br />
success or various types of failures. These codes help diagnose<br />
issues with NSDK integration and usage.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-orientation"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Orientation/" title="Device orientation when capturing camera frames....">Orientation</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Orientation/" title="Device orientation when capturing camera frames....">Orientation</a></span></span></td>
<td><div class="ctoken comment">
Device orientation when capturing camera frames.<br />
Orientation affects how ARDK interprets camera data and poses.<br />
Ensure the correct orientation is set in [FrameData.screenOrientation]<br />
for accurate tracking and localization.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-scansaveerror"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ScanSaveError/" title="Error codes that can be returned when a scan fails to save.">ScanSaveError</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ScanSaveError/" title="Error codes that can be returned when a scan fails to save.">ScanSaveError</a></span></span></td>
<td><div class="ctoken comment">
Error codes that can be returned when a scan fails to save.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-scansavestate"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ScanSaveState/" title="Enumeration of possible scan recording save states....">ScanSaveState</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ScanSaveState/" title="Enumeration of possible scan recording save states....">ScanSaveState</a></span></span></td>
<td><div class="ctoken comment">
Enumeration of possible scan recording save states.<br />
This enum represents the current state of a scan recording operation,<br />
indicating whether the scan data has been successfully saved, discarded, or failed.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-vpscoverageerror"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.VpsCoverageError/" title="Browse to VpsCoverageError">VpsCoverageError</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.VpsCoverageError/" title="Browse to VpsCoverageError">VpsCoverageError</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-vpsgraphoperationerror"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.VpsGraphOperationError/" title="Error codes for VPS graph operations....">VpsGraphOperationError</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.VpsGraphOperationError/" title="Error codes for VPS graph operations....">VpsGraphOperationError</a></span></span></td>
<td><div class="ctoken comment">
Error codes for VPS graph operations.<br />
These errors can occur during VPS operations that query the internal graph structure,<br />
such as converting device poses to geolocations. Each error provides specific information<br />
about why the operation failed.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
