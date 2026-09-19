---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.ImageMath.method-reprojection/
title: reprojection
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[ImageMath](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-ImageMath/ "ImageMath") 

</div>

<div class="api-title">

#  reprojection

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">reprojection</span><span class="ctoken plain">(</span><span class="ctoken plain">aspect</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain">, </span><span class="ctoken plain">fovRadians</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain">, </span><span class="ctoken plain">zNear</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain">, </span><span class="ctoken plain">zFar</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain">, </span><span class="ctoken plain">referenceView</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/matrix_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">matrix_float4x4</a></span><span class="ctoken plain">, </span><span class="ctoken plain">targetView</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/matrix_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">matrix_float4x4</a></span><span class="ctoken plain">, </span><span class="ctoken plain">backProjectionDistance</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain"> = 0.9) -\> </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/matrix_float3x3" target="_blank" rel="noopener noreferrer" title="Opens an external reference">matrix_float3x3</a></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns a 3×3 homography matrix as `matrix_float3x3` that reprojects\
image coordinates from a reference camera view into a target camera view.\
The image coordinates are expected to be normalized \[0..1\].

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A 3×3 homography matrix in column-major order.

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
<td><span id="external parameter-aspect"></span><span class="ctoken-line"><span class="ctoken class-name">aspect</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
The aspect ratio of the image (width / height).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-fovradians"></span><span class="ctoken-line"><span class="ctoken class-name">fovRadians</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
The vertical field of view in radians.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-znear"></span><span class="ctoken-line"><span class="ctoken class-name">zNear</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Near clipping plane distance.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-zfar"></span><span class="ctoken-line"><span class="ctoken class-name">zFar</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Far clipping plane distance.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-referenceview"></span><span class="ctoken-line"><span class="ctoken class-name">referenceView</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/matrix_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">matrix_float4x4</a></span></span></td>
<td><div class="ctoken comment">
The reference camera view.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-targetview"></span><span class="ctoken-line"><span class="ctoken class-name">targetView</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/matrix_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">matrix_float4x4</a></span></span></td>
<td><div class="ctoken comment">
The target camera view.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-backprojectiondistance"></span><span class="ctoken-line"><span class="ctoken class-name">backProjectionDistance</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Depth at which to reproject, normalized between clipping planes near (0) and far (1).<br />
Recommended: 0.9.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
