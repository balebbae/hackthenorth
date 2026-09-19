---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKCamera.method-projectionMatrix/
title: projectionMatrix
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

#  projectionMatrix

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">projectionMatrix</span><span class="ctoken plain">(</span><span class="ctoken plain">for</span><span class="ctoken plain"> </span><span class="ctoken plain">orientation</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//uikit/UIInterfaceOrientation" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UIInterfaceOrientation</a></span><span class="ctoken plain">, </span><span class="ctoken plain">viewportSize</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGSize" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGSize</a></span><span class="ctoken plain">, </span><span class="ctoken plain">zNear</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/cgfloat" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGFloat</a></span><span class="ctoken plain">, </span><span class="ctoken plain">zFar</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/cgfloat" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGFloat</a></span><span class="ctoken plain">) -\> </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float4x4</a></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns a projection matrix for the given orientation and viewport size, with optional near/far clipping.\
Pass the same orientation and viewport size used for the view matrix so that 3D content projects correctly.\
zFar \> 0 uses a finite far plane; zFar \<= 0 yields an infinite far plane (e.g. for skyboxes).

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
<td><span id="external parameter-for"></span><span class="ctoken-line"><span class="ctoken class-name">orientation</span></span></td>
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
<tr class="api-table-row">
<td><span id="external parameter-znear"></span><span class="ctoken-line"><span class="ctoken class-name">zNear</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/cgfloat" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGFloat</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-zfar"></span><span class="ctoken-line"><span class="ctoken class-name">zFar</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/cgfloat" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGFloat</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
