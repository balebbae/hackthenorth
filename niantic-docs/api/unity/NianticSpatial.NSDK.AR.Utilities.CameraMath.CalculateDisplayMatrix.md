---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.CameraMath.CalculateDisplayMatrix/
title: CalculateDisplayMatrix
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Utilities](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities/ "NianticSpatial.NSDK.AR.Utilities") <span class="api-breadcrumbs-nav">←</span>[CameraMath](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.CameraMath/ "NianticSpatial.NSDK.AR.Utilities.CameraMath") 

</div>

<div class="api-title">

#  CalculateDisplayMatrix

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">CalculateDisplayMatrix</span><span class="ctoken punctuation">(</span><span class="ctoken class-name keyword">int</span><span class="ctoken plain"> </span><span class="ctoken class-name">imageWidth</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">int</span><span class="ctoken plain"> </span><span class="ctoken class-name">imageHeight</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">int</span><span class="ctoken plain"> </span><span class="ctoken class-name">viewportWidth</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">int</span><span class="ctoken plain"> </span><span class="ctoken class-name">viewportHeight</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenOrientation.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ScreenOrientation</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">viewportOrientation</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">bool</span><span class="ctoken plain"> </span><span class="ctoken class-name">invertVertically</span><span class="ctoken plain"> </span><span class="ctoken punctuation">=</span><span class="ctoken plain"> </span><span class="ctoken plain">true</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">[MatrixLayout](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.CameraMath.MatrixLayout/ "Options to specify the expected layout of a matrix.")</span><span class="ctoken plain"> </span><span class="ctoken class-name">layout</span><span class="ctoken plain"> </span><span class="ctoken punctuation">=</span><span class="ctoken plain"> </span><span class="ctoken plain">MatrixLayout.ColumnMajor</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">bool</span><span class="ctoken plain"> </span><span class="ctoken class-name">reverseRotation</span><span class="ctoken plain"> </span><span class="ctoken punctuation">=</span><span class="ctoken plain"> </span><span class="ctoken plain">false</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns an affine transformation matrix for converting between normalized image\
coordinates and a coordinate space appropriate for rendering the camera image onscreen.

</div>

#### Remarks<a href="#remarks" class="hash-link" aria-label="Direct link to Remarks" title="Direct link to Remarks">​</a>

<div class="ctoken comment">

The viewport width and height arguments must conform with the current orientation.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

An affine 4x4 transformation matrix.

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
<td><span id="external parameter-imagewidth"></span><span class="ctoken-line"><span class="ctoken class-name">imageWidth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The width of the raw AR background image in pixels.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-imageheight"></span><span class="ctoken-line"><span class="ctoken class-name">imageHeight</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The height of the raw AR background image in pixels.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-viewportwidth"></span><span class="ctoken-line"><span class="ctoken class-name">viewportWidth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The width of the viewport in pixels.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-viewportheight"></span><span class="ctoken-line"><span class="ctoken class-name">viewportHeight</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The height of the viewport in pixels.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-viewportorientation"></span><span class="ctoken-line"><span class="ctoken class-name">viewportOrientation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenOrientation.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ScreenOrientation</a></span></span></td>
<td><div class="ctoken comment">
The orientation of the viewport.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-invertvertically"></span><span class="ctoken-line"><span class="ctoken class-name">invertVertically</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Whether to mirror the image across the X axis.<br />
This reverses the order of the horizontal rows, flipping the image upside down.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-layout"></span><span class="ctoken-line"><span class="ctoken class-name">layout</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.CameraMath.MatrixLayout/" title="Options to specify the expected layout of a matrix.">MatrixLayout</a></span></span></td>
<td><div class="ctoken comment">
The layout of the resulting matrix.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-reverserotation"></span><span class="ctoken-line"><span class="ctoken class-name">reverseRotation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
On some platforms, the direction of UI rotation is counter-clockwise.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
