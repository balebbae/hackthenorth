---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Occlusion.NsdkOcclusionExtension.TryGetDepth/
title: TryGetDepth
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Occlusion](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Occlusion/ "NianticSpatial.NSDK.AR.Occlusion") <span class="api-breadcrumbs-nav">←</span>[NsdkOcclusionExtension](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Occlusion.NsdkOcclusionExtension/ "NianticSpatial.NSDK.AR.Occlusion.NsdkOcclusionExtension") 

</div>

<div class="api-title">

#  TryGetDepth

<div class="api-package">

Returns the metric eye depth at the specified pixel coordinates.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">bool</span><span class="ctoken plain"> </span><span class="ctoken class-name">TryGetDepth</span><span class="ctoken punctuation">(</span><span class="ctoken class-name keyword">int</span><span class="ctoken plain"> </span><span class="ctoken class-name">screenX</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">int</span><span class="ctoken plain"> </span><span class="ctoken class-name">screenY</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">float</span><span class="ctoken plain"> </span><span class="ctoken class-name">depth</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns the metric eye depth at the specified pixel coordinates.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

Whether retrieving the depth value was successful.

</div>

### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

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
<td><span id="external parameter-screenx"></span><span class="ctoken-line"><span class="ctoken class-name">screenX</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The x position on the screen.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-screeny"></span><span class="ctoken-line"><span class="ctoken class-name">screenY</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The y position on the screen.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-depth"></span><span class="ctoken-line"><span class="ctoken class-name">depth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
The resulting depth value.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
