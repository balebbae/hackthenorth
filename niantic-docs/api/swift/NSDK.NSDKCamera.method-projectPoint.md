---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKCamera.method-projectPoint/
title: projectPoint
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKCamera](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKCamera/ "NSDKCamera") 

</div>

<div class="api-title">

#  projectPoint

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">projectPoint</span><span class="ctoken plain">(</span><span class="ctoken plain">\_</span><span class="ctoken plain"> </span><span class="ctoken plain">point</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float3" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float3</a></span><span class="ctoken plain">, </span><span class="ctoken plain">orientation</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//uikit/UIInterfaceOrientation" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UIInterfaceOrientation</a></span><span class="ctoken plain">, </span><span class="ctoken plain">viewportSize</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGSize" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGSize</a></span><span class="ctoken plain">) -\> </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGPoint" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGPoint</a></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Projects a 3D point in world space into 2D viewport coordinates (origin top-left, in pixels).\
Returns (-1, -1) if the point is behind the camera. Use with the same orientation and viewport size as rendering.

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
<td><span id="external parameter-point"></span><span class="ctoken-line"><span class="ctoken class-name">point</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float3" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float3</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-orientation"></span><span class="ctoken-line"><span class="ctoken class-name">orientation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//uikit/UIInterfaceOrientation" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UIInterfaceOrientation</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-viewportsize"></span><span class="ctoken-line"><span class="ctoken class-name">viewportSize</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGSize" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGSize</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
