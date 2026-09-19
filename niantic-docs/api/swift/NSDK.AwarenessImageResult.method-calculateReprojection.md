---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.AwarenessImageResult.method-calculateReprojection/
title: calculateReprojection
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[AwarenessImageResult](https://www.nianticspatial.com/docs/api/swift/NSDK.class-AwarenessImageResult/ "AwarenessImageResult") 

</div>

<div class="api-title">

#  calculateReprojection

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">calculateReprojection</span><span class="ctoken plain">(</span><span class="ctoken plain">to</span><span class="ctoken plain"> </span><span class="ctoken plain">targetPose</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/matrix_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">matrix_float4x4</a></span><span class="ctoken plain">) -\> </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/matrix_float3x3" target="_blank" rel="noopener noreferrer" title="Opens an external reference">matrix_float3x3</a></span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

A helper function that computes a 3×3 homography to reproject the image\
into the coordinate frame of the given target pose.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A 3×3 homography matrix, or `nil` if the computation fails.

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
<td><span id="external parameter-to"></span><span class="ctoken-line"><span class="ctoken class-name">targetPose</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/matrix_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">matrix_float4x4</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
