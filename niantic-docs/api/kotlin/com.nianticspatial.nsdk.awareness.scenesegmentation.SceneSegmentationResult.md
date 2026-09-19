---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationResult/
title: SceneSegmentationResult
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.awareness.scenesegmentation](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation/ "com.nianticspatial.nsdk.awareness.scenesegmentation") 

</div>

<div class="api-title">

#  SceneSegmentationResult

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">SceneSegmentationResult</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Represents the result of the scene segmentation processor. This class encapsulates all the data returned from a processed scene segmentation frame, including the semantic image data, camera pose, intrinsics, and timing information.

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
<td><span id="property-frameid"></span><span class="ctoken-line"><span class="ctoken class-name">frameId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Long</a></span></span></td>
<td><div class="ctoken comment">
The unique identifier of the AR frame that this result was generated from
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-image"></span><span class="ctoken-line"><span class="ctoken class-name">image</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Image/" title="Browse to Image">Image</a></span></span></td>
<td><div class="ctoken comment">
The scene segmentation result image (confidence, packed channels, or suppression mask)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-intrinsics"></span><span class="ctoken-line"><span class="ctoken class-name">intrinsics</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.CameraIntrinsics/" title="Camera intrinsics. This is a copy of the ARCore CameraIntrinsics class.">CameraIntrinsics</a></span></span></td>
<td><div class="ctoken comment">
The camera intrinsics used for this frame
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-pose"></span><span class="ctoken-line"><span class="ctoken class-name">pose</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developers.google.com/ar/reference/java/com/google/ar/core/Pose" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Pose</a></span></span></td>
<td><div class="ctoken comment">
The camera pose of the AR frame that this result was generated from
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-timestampms"></span><span class="ctoken-line"><span class="ctoken class-name">timestampMs</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Long</a></span></span></td>
<td><div class="ctoken comment">
The timestamp of the AR frame in milliseconds
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
