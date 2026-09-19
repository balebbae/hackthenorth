---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackCamera/
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

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.playback](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback/ "com.nianticspatial.nsdk.playback") 

</div>

<div class="api-title">

#  PlaybackCamera

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">PlaybackCamera</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Camera representation for playback, built from frame \[metadata\]. Exposes transform, intrinsics, resolution, tracking state, and orientation. Use \[toArCorePose\] to build a \[Pose\] for \[FrameData.cameraPose\]. Use \[getViewMatrix\] and \[getProjectionMatrix\] to drive a virtual camera for playback rendering.

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
<td><span id="property-imageresolution"></span><span class="ctoken-line"><span class="ctoken class-name">imageResolution</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Pair</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Image resolution (width, height) in pixels.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-intrinsics"></span><span class="ctoken-line"><span class="ctoken class-name">intrinsics</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.CameraIntrinsics/" title="Camera intrinsics. This is a copy of the ARCore CameraIntrinsics class.">CameraIntrinsics</a></span></span></td>
<td><div class="ctoken comment">
Camera intrinsics (focal length, principal point, dimensions).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-orientation"></span><span class="ctoken-line"><span class="ctoken class-name">orientation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Orientation/" title="Device orientation when capturing camera frames....">Orientation</a></span></span></td>
<td><div class="ctoken comment">
Screen orientation from metadata.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-trackingstate"></span><span class="ctoken-line"><span class="ctoken class-name">trackingState</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developers.google.com/ar/reference/java/com/google/ar/core/TrackingState" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TrackingState</a></span></span></td>
<td><div class="ctoken comment">
ARCore tracking state for this frame.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-transform"></span><span class="ctoken-line"><span class="ctoken class-name">transform</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">FloatArray</a></span></span></td>
<td><div class="ctoken comment">
Camera-to-world 4×4 transform (column-major) as FloatArray of 16 elements.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Functions<a href="#functions" class="hash-link" aria-label="Direct link to Functions" title="Direct link to Functions">​</a>

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
<td><span id="function-displayorientedtransform"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackCamera.displayOrientedTransform/" title="Display-oriented camera-to-world transform with Z rotation applied for the given orientation....">displayOrientedTransform</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">FloatArray</a></span></span></td>
<td><div class="ctoken comment">
Display-oriented camera-to-world transform with Z rotation applied for the given orientation.<br />
Sensor frame is landscape-right; portrait adds π/2, portrait-upside-down adds -π/2, landscape-left adds π.<br />
Use for rendering so the camera matches on-screen orientation.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getdisplayorientedpose"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackCamera.getDisplayOrientedPose/" title="Display-oriented camera pose (Z rotation applied for the given orientation)....">getDisplayOrientedPose</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developers.google.com/ar/reference/java/com/google/ar/core/Pose" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Pose</a></span></span></td>
<td><div class="ctoken comment">
Display-oriented camera pose (Z rotation applied for the given orientation).<br />
Use for VPS2 and UI that need heading aligned with the display.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getprojectionmatrix"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackCamera.getProjectionMatrix/" title="OpenGL-style projection matrix (column-major) from intrinsics for the given viewport and near/far....">getProjectionMatrix</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">FloatArray</a></span></span></td>
<td><div class="ctoken comment">
OpenGL-style projection matrix (column-major) from intrinsics for the given viewport and near/far.<br />
Use with [getViewMatrix] to render 3D content aligned with the playback camera.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getviewmatrix"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackCamera.getViewMatrix/" title="World-to-camera view matrix (column-major) for the given display orientation....">getViewMatrix</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">FloatArray</a></span></span></td>
<td><div class="ctoken comment">
World-to-camera view matrix (column-major) for the given display orientation.<br />
Inverse of [displayOrientedTransform]. Pass to OpenGL/GLES as the view matrix.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-toarcorepose"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackCamera.toArCorePose/" title="Builds an ARCore [Pose] from this frame&#39;s 4×4 transform (column-major)....">toArCorePose</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developers.google.com/ar/reference/java/com/google/ar/core/Pose" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Pose</a></span></span></td>
<td><div class="ctoken comment">
Builds an ARCore [Pose] from this frame's 4×4 transform (column-major).<br />
Use for [FrameData.cameraPose] when building frame data from playback.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
