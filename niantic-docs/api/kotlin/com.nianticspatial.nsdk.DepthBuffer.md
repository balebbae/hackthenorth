---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.DepthBuffer/
title: DepthBuffer
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

#  DepthBuffer

<div class="api-package">

Depth result from ARDK's Depth System after computing disparity.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">data</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">DepthBuffer</span></span>

## See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

- ARDK.GetLatestDepth
- ARDK.GetLatestDepthParams

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
<td><span id="property-disparitymax"></span><span class="ctoken-line"><span class="ctoken class-name">disparityMax</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
The maximum disparity value of the depth image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-disparitymin"></span><span class="ctoken-line"><span class="ctoken class-name">disparityMin</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
The minimum disparity value of the depth image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-frameid"></span><span class="ctoken-line"><span class="ctoken class-name">frameId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Long</a></span></span></td>
<td><div class="ctoken comment">
The unique identifier for the depth frame.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-image"></span><span class="ctoken-line"><span class="ctoken class-name">image</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">FloatArray</a></span></span></td>
<td><div class="ctoken comment">
The depth image. Each pixel contains the estimated disparity value from 0 to 1.<br />
The image size is \ref imageWidth x \ref imageHeight.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-imageheight"></span><span class="ctoken-line"><span class="ctoken class-name">imageHeight</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
The height of the depth image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-imagewidth"></span><span class="ctoken-line"><span class="ctoken class-name">imageWidth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
The width of the depth image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-intrinsics"></span><span class="ctoken-line"><span class="ctoken class-name">intrinsics</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.CameraIntrinsics/" title="Camera intrinsics. This is a copy of the ARCore CameraIntrinsics class.">CameraIntrinsics</a></span></span></td>
<td><div class="ctoken comment">
The camera intrinsics of the depth frame.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-orientation"></span><span class="ctoken-line"><span class="ctoken class-name">orientation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Orientation/" title="Device orientation when capturing camera frames....">Orientation</a></span></span></td>
<td><div class="ctoken comment">
The device orientation of the depth frame.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-pose"></span><span class="ctoken-line"><span class="ctoken class-name">pose</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developers.google.com/ar/reference/java/com/google/ar/core/Pose" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Pose</a></span></span></td>
<td><div class="ctoken comment">
The camera pose of the depth frame.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-timestampms"></span><span class="ctoken-line"><span class="ctoken class-name">timestampMs</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Long</a></span></span></td>
<td><div class="ctoken comment">
The timestamp of the depth frame.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
