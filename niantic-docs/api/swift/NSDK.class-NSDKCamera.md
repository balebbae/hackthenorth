---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKCamera/
title: NSDKCamera
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

#  NSDKCamera

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">NSDKCamera</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Single camera API for both modes. Holds either **ARCamera** (live) or **PlaybackCamera** (playback) and exposes transform, viewMatrix, projectionMatrix, viewportRect, etc. Relation to Apple AR: **Wraps** Apple's ARCamera in live mode; wraps our PlaybackCamera in playback. Callers use NSDKCamera and don't branch. Create via `NSDKCamera(arCamera:)` or `NSDKCamera(playbackCamera:)`.

------------------------------------------------------------------------

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

### Constructor<a href="#constructor" class="hash-link" aria-label="Direct link to Constructor" title="Direct link to Constructor">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">init</span><span class="ctoken plain">(</span><span class="ctoken plain">arCamera</span><span class="ctoken plain">: </span><span class="ctoken class-name">ARCamera</span><span class="ctoken plain">)</span></span>

</div>

#### Summary<a href="#summary-1" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Creates an NSDKCamera that delegates to Apple's ARCamera (live session).\
Use when the app is using a live ARSession and you have a current ARFrame's camera.

</div>

------------------------------------------------------------------------

### Overload<a href="#overload" class="hash-link" aria-label="Direct link to Overload" title="Direct link to Overload">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">init</span><span class="ctoken plain">(</span><span class="ctoken plain">playbackCamera</span><span class="ctoken plain">: </span><span class="ctoken class-name">[PlaybackCamera](https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackCamera/ "Camera representation built from frame **metadata** (pose4x4, intrinsics, resolution). Exposes the same...")</span><span class="ctoken plain">)</span></span>

</div>

#### Summary<a href="#summary-2" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Creates an NSDKCamera that delegates to PlaybackCamera (playback session).\
Use when playing back a recorded dataset; pass the frame's camera from `PlaybackFrame.camera`.

</div>

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
<td><span id="property-backing"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">backing</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKCamera.enum-Backing/" title="The underlying camera: either a live ARCamera or a playback PlaybackCamera....">Backing</a></span></span></td>
<td><div class="ctoken comment">
The underlying camera (live or playback). Use this to call ARCamera- or PlaybackCamera-specific APIs.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-effectiverenderingorientation"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">effectiveRenderingOrientation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//uikit/UIInterfaceOrientation" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UIInterfaceOrientation</a></span></span></td>
<td><div class="ctoken comment">
When in playback, the orientation the frame was recorded in. When in live, returns nil.<br />
View and projection matrices use the orientation passed by the caller so rendering can follow the device.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-eulerangles"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">eulerAngles</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float3" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float3</a></span></span></td>
<td><div class="ctoken comment">
The camera's orientation as Euler angles (pitch, yaw, roll) in radians.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-exposureduration"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">exposureDuration</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/timeinterval" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TimeInterval</a></span></span></td>
<td><div class="ctoken comment">
Camera exposure duration in seconds.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-exposureoffset"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">exposureOffset</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Camera exposure offset in EV.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-imageresolution"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">imageResolution</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGSize" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGSize</a></span></span></td>
<td><div class="ctoken comment">
The camera image resolution in pixels.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-intrinsics"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">intrinsics</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float3x3" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float3x3</a></span></span></td>
<td><div class="ctoken comment">
The camera intrinsics matrix (3×3) in row-major layout: [fx, 0, 0; 0, fy, 0; cx, cy, 1].<br />
Use for unprojecting image coordinates to camera rays or building projection matrices.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-projectionmatrix"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">projectionMatrix</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float4x4</a></span></span></td>
<td><div class="ctoken comment">
Default projection matrix (no far clipping).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-trackingstate"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">trackingState</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">ARCamera</span><span class="ctoken plain">.</span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/trackingstate" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TrackingState</a></span></span></td>
<td><div class="ctoken comment">
The camera's tracking state.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-transform"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">transform</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float4x4</a></span></span></td>
<td><div class="ctoken comment">
The 4×4 transformation matrix of the camera in world coordinates (camera-to-world).<br />
Same convention as ARCamera.transform; use for placing virtual content relative to the camera.
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
<td><span id="method-displayorientedtransform"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKCamera.method-displayOrientedTransform/" title="Returns the camera transform adjusted for the given display orientation (Z-axis rotation applied)....">displayOrientedTransform</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float4x4</a></span></span></td>
<td><div class="ctoken comment">
Returns the camera transform adjusted for the given display orientation (Z-axis rotation applied).<br />
Use when you need the camera pose in the same coordinate frame as the on-screen image (e.g. for overlay alignment).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-projectionmatrix"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKCamera.method-projectionMatrix/" title="Returns a projection matrix for the given orientation and viewport size, with optional near/far clipping....">projectionMatrix</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float4x4</a></span></span></td>
<td><div class="ctoken comment">
Returns a projection matrix for the given orientation and viewport size, with optional near/far clipping.<br />
Pass the same orientation and viewport size used for the view matrix so that 3D content projects correctly.<br />
zFar &gt; 0 uses a finite far plane; zFar &lt;= 0 yields an infinite far plane (e.g. for skyboxes).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-projectpoint"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKCamera.method-projectPoint/" title="Projects a 3D point in world space into 2D viewport coordinates (origin top-left, in pixels)....">projectPoint</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGPoint" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGPoint</a></span></span></td>
<td><div class="ctoken comment">
Projects a 3D point in world space into 2D viewport coordinates (origin top-left, in pixels).<br />
Returns (-1, -1) if the point is behind the camera. Use with the same orientation and viewport size as rendering.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-viewmatrix"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKCamera.method-viewMatrix/" title="Returns the view matrix (world-to-camera) for the given interface orientation....">viewMatrix</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float4x4</a></span></span></td>
<td><div class="ctoken comment">
Returns the view matrix (world-to-camera) for the given interface orientation.<br />
Pass the current device orientation (e.g. from the window scene) so that rendering follows the device when rotated.<br />
For both live and playback, the returned matrix matches the display-oriented camera transform.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-viewportrect"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKCamera.method-viewportRect/" title="Returns the viewport rect to use when rendering into the given drawable size....">viewportRect</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGRect" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGRect</a></span></span></td>
<td><div class="ctoken comment">
Returns the viewport rect to use when rendering into the given drawable size.<br />
- Live: returns the full drawable (origin zero, size = drawableSize).<br />
- Playback: returns an aspect-fill rect so the camera image aligns with the rendered content; pass <code>displayOrientation</code> (current device orientation) so the viewport fits correctly in portrait and landscape.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Nested Types<a href="#nested-types" class="hash-link" aria-label="Direct link to Nested Types" title="Direct link to Nested Types">​</a>

### Enums<a href="#enums" class="hash-link" aria-label="Direct link to Enums" title="Direct link to Enums">​</a>

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
<td><span id="enum-backing"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKCamera.enum-Backing/" title="The underlying camera: either a live ARCamera or a playback PlaybackCamera....">Backing</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKCamera.enum-Backing/" title="The underlying camera: either a live ARCamera or a playback PlaybackCamera....">Backing</a></span></span></td>
<td><div class="ctoken comment">
The underlying camera: either a live ARCamera or a playback PlaybackCamera.<br />
Switch on this when you need to call APIs that are specific to one type (e.g. <code>recordedOrientation</code> on PlaybackCamera).<br />
Example:
</div>
<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">
<div class="codeBlockContent_QJqH">
<pre class="prism-code language-swift codeBlock_bY9V thin-scrollbar" tabindex="0" style="color:#393A34;background-color:#f6f8fa"><code>switch camera.backing {
case .ar(let arCamera):
    // ARCamera-specific APIs
case .playback(let playbackCamera):
    let orientation = playbackCamera.recordedOrientation
}</code></pre>
</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
