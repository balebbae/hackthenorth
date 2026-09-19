---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackCamera/
title: PlaybackCamera
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") 

</div>

<div class="api-title">

#  PlaybackCamera

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">PlaybackCamera</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Camera representation built from frame **metadata** (pose4x4, intrinsics, resolution). Exposes the same concepts as **ARCamera**: transform, viewMatrix, projectionMatrix, viewportRect, displayOrientedTransform. Relation to Apple AR: **Stands in for** ARCamera during playback. No Apple camera; we synthesize view/projection from recorded intrinsics and pose. Use `PlaybackFrame.camera` to obtain an instance.

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
<td><span id="property-eulerangles"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">eulerAngles</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float3" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float3</a></span></span></td>
<td><div class="ctoken comment">
Euler angles (pitch, yaw, roll) in radians, extracted from the transform; order matches ARKit.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-exposureduration"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">exposureDuration</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/timeinterval" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TimeInterval</a></span></span></td>
<td><div class="ctoken comment">
Exposure duration in seconds. Playback has no exposure data; returns a default.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-exposureoffset"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">exposureOffset</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Exposure offset in EV. Playback has no exposure data; returns 0.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-imageresolution"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">imageResolution</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGSize" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGSize</a></span></span></td>
<td><div class="ctoken comment">
The camera's image resolution in pixels.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-intrinsics"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">intrinsics</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float3x3" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float3x3</a></span></span></td>
<td><div class="ctoken comment">
The camera's intrinsic matrix (fx, fy, cx, cy layout).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-projectionmatrix"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">projectionMatrix</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float4x4</a></span></span></td>
<td><div class="ctoken comment">
Default projection matrix (infinite far plane). Uses <code>metadata.projection</code> when available; otherwise built from intrinsics using orientation from metadata (<code>screenOrientation</code>), or inferred from image resolution (portrait if height &gt; width, else landscape-right), or landscape-right as last resort.<br />
For display-time orientation or custom near/far, use <code>projectionMatrix(for:viewportSize:zNear:zFar:)</code>.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-recordedorientation"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">recordedOrientation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//uikit/UIInterfaceOrientation" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UIInterfaceOrientation</a></span></span></td>
<td><div class="ctoken comment">
The interface orientation the frame was recorded in. Uses metadata <code>screenOrientation</code> when set; else inferred from image resolution (height &gt; width → portrait, else landscape-right); else landscape-right.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-trackingstate"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">trackingState</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">ARCamera</span><span class="ctoken plain">.</span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/trackingstate" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TrackingState</a></span></span></td>
<td><div class="ctoken comment">
Camera tracking state (from metadata.tracking).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-transform"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">transform</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float4x4</a></span></span></td>
<td><div class="ctoken comment">
The 4×4 camera-to-world transformation matrix from the frame metadata (pose4x4).
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

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
<td><span id="method-displayorientedtransform"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackCamera.method-displayOrientedTransform/" title="Returns the camera transform with a Z-axis rotation applied so it matches the given screen orientation....">displayOrientedTransform</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float4x4</a></span></span></td>
<td><div class="ctoken comment">
Returns the camera transform with a Z-axis rotation applied so it matches the given screen orientation.<br />
Sensor frame is landscape-right; portrait adds π/2, portrait-upside-down adds -π/2, landscape-left adds π.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-projectionmatrix"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackCamera.method-projectionMatrix/" title="Returns a projection matrix for the given orientation and viewport, with the requested near/far planes....">projectionMatrix</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float4x4</a></span></span></td>
<td><div class="ctoken comment">
Returns a projection matrix for the given orientation and viewport, with the requested near/far planes.<br />
Built from intrinsics with orientation applied: portrait swaps fx/fy and dimensions; landscape-left flips principal point.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-projectpoint"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackCamera.method-projectPoint/" title="Projects a 3D world-space point into 2D viewport pixel coordinates (origin top-left)....">projectPoint</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGPoint" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGPoint</a></span></span></td>
<td><div class="ctoken comment">
Projects a 3D world-space point into 2D viewport pixel coordinates (origin top-left).<br />
Returns (-1, -1) if the point is behind the camera. Uses intrinsics and view for the given orientation.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-viewmatrix"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackCamera.method-viewMatrix/" title="Returns the view matrix (world-to-camera) for the given interface orientation....">viewMatrix</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float4x4</a></span></span></td>
<td><div class="ctoken comment">
Returns the view matrix (world-to-camera) for the given interface orientation.<br />
Implemented as the inverse of the display-oriented transform so rendering matches the on-screen camera.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-viewportrect"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackCamera.method-viewportRect/" title="Viewport rect that covers the drawable via aspect-fill, matching how NSDKView renders the camera background....">viewportRect</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGRect" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGRect</a></span></span></td>
<td><div class="ctoken comment">
Viewport rect that covers the drawable via aspect-fill, matching how NSDKView renders the camera background.<br />
ARKit sensor images are always in landscape orientation.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
