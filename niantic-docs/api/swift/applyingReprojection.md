---
source: https://www.nianticspatial.com/docs/api/swift/applyingReprojection/
title: applyingReprojection
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") 

</div>

<div class="api-title">

#  applyingReprojection

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">applyingReprojection</span><span class="ctoken plain">(</span><span class="ctoken plain">containerSize</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGSize" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGSize</a></span><span class="ctoken plain">, </span><span class="ctoken plain">transform</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float3x3" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float3x3</a></span><span class="ctoken plain">) -\> </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGRect" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGRect</a></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Applies a 3x3 homography (reprojection) to this rectangle and returns the resulting bounding box\
in a specified container coordinate space.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A new CGRect representing the transformed rectangle.

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
<td><span id="external parameter-containersize"></span><span class="ctoken-line"><span class="ctoken class-name">containerSize</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGSize" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGSize</a></span></span></td>
<td><div class="ctoken comment">
The size of the container coordinate space. Coordinates are assumed to be<br />
relative to this space (e.g., image or view size) when applying the homography.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-transform"></span><span class="ctoken-line"><span class="ctoken class-name">transform</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float3x3" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float3x3</a></span></span></td>
<td><div class="ctoken comment">
The 3x3 homography matrix that maps points from the source coordinate space<br />
to the target coordinate space.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
