---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.PAM.NsdkCpuImage/
title: NsdkCpuImage
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.PAM](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.PAM/ "NianticSpatial.NSDK.AR.PAM") 

</div>

<div class="api-title">

#  NsdkCpuImage

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">struct</span><span class="ctoken plain"> </span><span class="ctoken class-name">NsdkCpuImage</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

A Niantic Spatial Development Kit intermediate class to hold image data before sending down to native via NsdkFrameData. Should be able to hold references to XRCpuImage, MagicLeap and others' data. Does not own any of it. Is not related to NsdkCpuImageApi.

------------------------------------------------------------------------

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name">NsdkCpuImage</span><span class="ctoken punctuation">(</span><span class="ctoken class-name">[ImageFormatCEnum](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.PAM.ImageFormatCEnum/ "Browse to ImageFormatCEnum")</span><span class="ctoken plain"> </span><span class="ctoken class-name">format</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">uint</span><span class="ctoken plain"> </span><span class="ctoken class-name">width</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">uint</span><span class="ctoken plain"> </span><span class="ctoken class-name">height</span><span class="ctoken punctuation">)</span></span>

</div>

------------------------------------------------------------------------

## Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

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
<td><span id="field-format"></span><span class="ctoken-line"><span class="ctoken class-name">Format</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.PAM.ImageFormatCEnum/" title="Browse to ImageFormatCEnum">ImageFormatCEnum</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-height"></span><span class="ctoken-line"><span class="ctoken class-name">Height</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">uint</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-maxplanes"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">MaxPlanes</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-planes"></span><span class="ctoken-line"><span class="ctoken class-name">Planes</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.PAM.NsdkCpuImagePlane/" title="Browse to NsdkCpuImagePlane">NsdkCpuImagePlane</a></span><span class="ctoken punctuation">[</span><span class="ctoken punctuation">]</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-width"></span><span class="ctoken-line"><span class="ctoken class-name">Width</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">uint</span></span></td>
<td><div class="ctoken comment deemphasize">
-
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
<td><span id="method-create"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.PAM.NsdkCpuImage.Create/" title="Browse to Create">Create</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">NsdkCpuImage</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-trygetfromxrcpuimage"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.PAM.NsdkCpuImage.TryGetFromXRCpuImage/" title="Browse to TryGetFromXRCpuImage">TryGetFromXRCpuImage</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
