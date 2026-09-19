---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.ImageSamplingUtils.Sample/
title: Sample
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

#  Sample

<div class="api-package">

Samples a native array as if it was an image. Employs nearest neighbour algorithm.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">T</span><span class="ctoken plain"> </span><span class="ctoken class-name">Sample</span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">T</span><span class="ctoken punctuation">\></span><span class="ctoken punctuation">(</span><span class="ctoken keyword">this</span><span class="ctoken plain"> </span><span class="ctoken class-name">NativeArray</span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">T</span><span class="ctoken punctuation">\></span><span class="ctoken plain"> </span><span class="ctoken class-name">data</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">int</span><span class="ctoken plain"> </span><span class="ctoken class-name">width</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">int</span><span class="ctoken plain"> </span><span class="ctoken class-name">height</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector2</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">uv</span><span class="ctoken punctuation">)</span><span class="ctoken plain"> </span><span class="ctoken keyword">where</span><span class="ctoken plain"> </span><span class="ctoken class-name">T</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken keyword">struct</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Samples a native array as if it was an image. Employs nearest neighbour algorithm.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The nearest value in the array to the normalized coordinates.

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
<td><span id="external parameter-data"></span><span class="ctoken-line"><span class="ctoken class-name">data</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">NativeArray</span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name">T</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
The native array containing the data.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-width"></span><span class="ctoken-line"><span class="ctoken class-name">width</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The width of the image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-height"></span><span class="ctoken-line"><span class="ctoken class-name">height</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The height of the image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-uv"></span><span class="ctoken-line"><span class="ctoken class-name">uv</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector2</a></span></span></td>
<td><div class="ctoken comment">
Normalized image coordinates to sample.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Overload 1<a href="#overload-1" class="hash-link" aria-label="Direct link to Overload 1" title="Direct link to Overload 1">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">T</span><span class="ctoken plain"> </span><span class="ctoken class-name">Sample</span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">T</span><span class="ctoken punctuation">\></span><span class="ctoken punctuation">(</span><span class="ctoken keyword">this</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XRCpuImage.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XRCpuImage</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">image</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector2</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">uv</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">transform</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">int</span><span class="ctoken plain"> </span><span class="ctoken class-name">plane</span><span class="ctoken plain"> </span><span class="ctoken punctuation">=</span><span class="ctoken plain"> </span><span class="ctoken plain">0</span><span class="ctoken punctuation">)</span><span class="ctoken plain"> </span><span class="ctoken keyword">where</span><span class="ctoken plain"> </span><span class="ctoken class-name">T</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken keyword">struct</span></span>

</div>

#### Summary<a href="#summary-1" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Samples a CPU image. Employs nearest neighbour algorithm.

</div>

#### Returns<a href="#returns-1" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The nearest value in the image to the transformed UV coordinates.

</div>

### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

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
<td><span id="external parameter-data"></span><span class="ctoken-line"><span class="ctoken class-name">data</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">NativeArray</span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name">T</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
The native array containing the data.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-width"></span><span class="ctoken-line"><span class="ctoken class-name">width</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The width of the image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-height"></span><span class="ctoken-line"><span class="ctoken class-name">height</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The height of the image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-uv"></span><span class="ctoken-line"><span class="ctoken class-name">uv</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector2</a></span></span></td>
<td><div class="ctoken comment">
Normalized image coordinates to sample.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Overload 2<a href="#overload-2" class="hash-link" aria-label="Direct link to Overload 2" title="Direct link to Overload 2">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">T</span><span class="ctoken plain"> </span><span class="ctoken class-name">Sample</span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">T</span><span class="ctoken punctuation">\></span><span class="ctoken punctuation">(</span><span class="ctoken keyword">this</span><span class="ctoken plain"> </span><span class="ctoken class-name">NativeArray</span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">T</span><span class="ctoken punctuation">\></span><span class="ctoken plain"> </span><span class="ctoken class-name">data</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">int</span><span class="ctoken plain"> </span><span class="ctoken class-name">width</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">int</span><span class="ctoken plain"> </span><span class="ctoken class-name">height</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector2</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">uv</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">transform</span><span class="ctoken punctuation">)</span><span class="ctoken plain"> </span><span class="ctoken keyword">where</span><span class="ctoken plain"> </span><span class="ctoken class-name">T</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken keyword">struct</span></span>

</div>

#### Summary<a href="#summary-2" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Samples a native array as if it was an image. Employs nearest neighbour algorithm.

</div>

#### Returns<a href="#returns-2" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The nearest value in the array to the transformed UV coordinates.

</div>

### Parameters<a href="#parameters-2" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

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
<td><span id="external parameter-data"></span><span class="ctoken-line"><span class="ctoken class-name">data</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">NativeArray</span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name">T</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
The native array containing the data.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-width"></span><span class="ctoken-line"><span class="ctoken class-name">width</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The width of the image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-height"></span><span class="ctoken-line"><span class="ctoken class-name">height</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The height of the image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-uv"></span><span class="ctoken-line"><span class="ctoken class-name">uv</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector2</a></span></span></td>
<td><div class="ctoken comment">
Normalized image coordinates to sample.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
