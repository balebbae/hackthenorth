---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackFrame/
title: PlaybackFrame
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

#  PlaybackFrame

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">data</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">PlaybackFrame</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

One frame of playback: metadata, camera representation, optional image and depth. Created when a frame is loaded (e.g. by \[PlaybackSession\]). Use \[camera\] for pose/intrinsics and \[metadata\] for building \[FrameData\].

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
<td><span id="property-camera"></span><span class="ctoken-line"><span class="ctoken class-name">camera</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackCamera/" title="Camera representation for playback, built from frame [metadata]. Exposes transform, intrinsics, resolution,...">PlaybackCamera</a></span></span></td>
<td><div class="ctoken comment">
Camera representation for this frame (transform, intrinsics, [PlaybackCamera.toArCorePose]).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-depthconfidence"></span><span class="ctoken-line"><span class="ctoken class-name">depthConfidence</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ByteArray</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Per-pixel depth confidence (UInt8) when available; null otherwise.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-depthdata"></span><span class="ctoken-line"><span class="ctoken class-name">depthData</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ByteArray</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Depth buffer (Float32, meters) for this frame if available; null otherwise.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-image"></span><span class="ctoken-line"><span class="ctoken class-name">image</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Bitmap" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bitmap</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
RGB camera image for this frame (e.g. for background display); null if not loaded.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-metadata"></span><span class="ctoken-line"><span class="ctoken class-name">metadata</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.FrameMetadata/" title="Per-frame metadata from the capture JSON. Required fields per spec; optional may be null.">FrameMetadata</a></span></span></td>
<td><div class="ctoken comment">
Frame metadata from the dataset (pose4x4, intrinsics, resolution, tracking, orientation, location, etc.).
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
