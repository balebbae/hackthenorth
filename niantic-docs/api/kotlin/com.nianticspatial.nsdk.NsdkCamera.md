---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkCamera/
title: NsdkCamera
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

#  NsdkCamera

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">sealed</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">NsdkCamera</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Camera view over the current frame (live or playback). Mirrors ARCore \[com.google.ar.core.Camera\] so callers can use one API for both live and playback. Use \[pose\] and \[getDisplayOrientedPose\] for overlays, VPS2, etc. Use \[imageIntrinsics\] for CPU image coordinates, \[trackingState\] / \[getTrackingFailureReason\] for tracking status, and \[getViewMatrix\] for rendering. Use \[backing\] when you need ARCamera- or PlaybackCamera-specific APIs.

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
<td><span id="property-backing"></span><span class="ctoken-line"><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name">backing</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Backing</span></span></td>
<td><div class="ctoken comment">
The underlying camera (live or playback). Switch on this for type-specific APIs.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-imageintrinsics"></span><span class="ctoken-line"><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name">imageIntrinsics</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.CameraIntrinsics/" title="Camera intrinsics. This is a copy of the ARCore CameraIntrinsics class.">CameraIntrinsics</a></span></span></td>
<td><div class="ctoken comment">
Unrotated camera intrinsics for the CPU image. Matches ARCore [com.google.ar.core.Camera.getImageIntrinsics].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-pose"></span><span class="ctoken-line"><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name">pose</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developers.google.com/ar/reference/java/com/google/ar/core/Pose" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Pose</a></span></span></td>
<td><div class="ctoken comment">
Physical camera pose in world space. Matches ARCore [com.google.ar.core.Camera.getPose].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-trackingstate"></span><span class="ctoken-line"><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name">trackingState</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developers.google.com/ar/reference/java/com/google/ar/core/TrackingState" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TrackingState</a></span></span></td>
<td><div class="ctoken comment">
Current motion tracking state. Matches ARCore [com.google.ar.core.Camera.getTrackingState].
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
<td><span id="function-getdisplayorientedpose"></span><span class="ctoken-line"><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkCamera.getDisplayOrientedPose/" title="Display-oriented camera pose for overlays and UI. Matches ARCore [com.google.ar.core.Camera.getDisplayOrientedPose].">getDisplayOrientedPose</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developers.google.com/ar/reference/java/com/google/ar/core/Pose" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Pose</a></span></span></td>
<td><div class="ctoken comment">
Display-oriented camera pose for overlays and UI. Matches ARCore [com.google.ar.core.Camera.getDisplayOrientedPose].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-gettrackingfailurereason"></span><span class="ctoken-line"><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkCamera.getTrackingFailureReason/" title="Reason tracking is paused, or [TrackingFailureReason.NONE] when tracking. Matches ARCore [com.google.ar.core.Camera.getTrackingFailureReason].">getTrackingFailureReason</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developers.google.com/ar/reference/java/com/google/ar/core/TrackingFailureReason" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TrackingFailureReason</a></span></span></td>
<td><div class="ctoken comment">
Reason tracking is paused, or [TrackingFailureReason.NONE] when tracking. Matches ARCore [com.google.ar.core.Camera.getTrackingFailureReason].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getviewmatrix"></span><span class="ctoken-line"><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkCamera.getViewMatrix/" title="View matrix (column-major, 16 floats) for this frame. Matches ARCore [com.google.ar.core.Camera.getViewMatrix].">getViewMatrix</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">FloatArray</a></span></span></td>
<td><div class="ctoken comment">
View matrix (column-major, 16 floats) for this frame. Matches ARCore [com.google.ar.core.Camera.getViewMatrix].
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
