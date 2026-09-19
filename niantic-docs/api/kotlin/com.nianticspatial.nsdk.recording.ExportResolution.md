---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.recording.ExportResolution/
title: ExportResolution
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.recording](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.recording/ "com.nianticspatial.nsdk.recording") 

</div>

<div class="api-title">

#  ExportResolution

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">enum</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">ExportResolution</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Resolution option for exported scan images. When exporting a recording, this controls which image resolutions are included in the payload.

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
<td><span id="property-value"></span><span class="ctoken-line"><span class="ctoken class-name keyword">value</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Cases<a href="#cases" class="hash-link" aria-label="Direct link to Cases" title="Direct link to Cases">​</a>

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
<td><span id="case-high"></span><span class="ctoken-line"><span class="ctoken class-name">HIGH</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">HIGH</span></span></td>
<td><div class="ctoken comment">
This is the same resolution as the camera frame passed to NSDKSession.sendFrame
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-mixed"></span><span class="ctoken-line"><span class="ctoken class-name">MIXED</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">MIXED</span></span></td>
<td><div class="ctoken comment">
Export both 720p and high resolution images when available.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-res720_540"></span><span class="ctoken-line"><span class="ctoken class-name">RES720_540</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">RES720_540</span></span></td>
<td><div class="ctoken comment">
Export only the 720p resolution image.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
