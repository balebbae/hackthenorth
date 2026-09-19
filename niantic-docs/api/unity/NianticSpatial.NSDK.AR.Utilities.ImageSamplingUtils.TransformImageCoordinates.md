---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.ImageSamplingUtils.TransformImageCoordinates/
title: TransformImageCoordinates
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Utilities](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities/ "NianticSpatial.NSDK.AR.Utilities") <span class="api-breadcrumbs-nav">←</span>[ImageSamplingUtils](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.ImageSamplingUtils/ "NianticSpatial.NSDK.AR.Utilities.ImageSamplingUtils") 

</div>

<div class="api-title">

#  TransformImageCoordinates

<div class="api-package">

Transforms pixel coordinates using the specified matrix.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2Int.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector2Int</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">TransformImageCoordinates</span><span class="ctoken punctuation">(</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2Int.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector2Int</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">coordinates</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2Int.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector2Int</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">sourceContainer</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2Int.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector2Int</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">targetContainer</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">transform</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">bool</span><span class="ctoken plain"> </span><span class="ctoken class-name">clampToContainer</span><span class="ctoken plain"> </span><span class="ctoken punctuation">=</span><span class="ctoken plain"> </span><span class="ctoken plain">false</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Transforms pixel coordinates using the specified matrix.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The transformed pixel coordinates.

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
<td><span id="external parameter-coordinates"></span><span class="ctoken-line"><span class="ctoken class-name">coordinates</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2Int.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector2Int</a></span></span></td>
<td><div class="ctoken comment">
The pixel coordinates to transform.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-sourcecontainer"></span><span class="ctoken-line"><span class="ctoken class-name">sourceContainer</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2Int.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector2Int</a></span></span></td>
<td><div class="ctoken comment">
The resolution of the container the coordinates are interpreted in.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-targetcontainer"></span><span class="ctoken-line"><span class="ctoken class-name">targetContainer</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2Int.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector2Int</a></span></span></td>
<td><div class="ctoken comment">
The resolution of the container the resulting coordinates are interpreted in.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-transform"></span><span class="ctoken-line"><span class="ctoken class-name">transform</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span></span></td>
<td><div class="ctoken comment">
The transformation matrix.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-clamptocontainer"></span><span class="ctoken-line"><span class="ctoken class-name">clampToContainer</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Whether to clamp the resulting coordinates to the bounds of the target container.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
