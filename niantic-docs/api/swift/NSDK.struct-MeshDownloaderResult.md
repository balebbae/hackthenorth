---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.struct-MeshDownloaderResult/
title: MeshDownloaderResult
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") 

</div>

<div class="api-title">

#  MeshDownloaderResult

<div class="api-package">

Represents a single mesh result with geometry, texture, and transform data.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">struct</span><span class="ctoken plain"> </span><span class="ctoken class-name">MeshDownloaderResult</span></span>

------------------------------------------------------------------------

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">init</span><span class="ctoken plain">(</span><span class="ctoken plain">fromC</span><span class="ctoken plain"> </span><span class="ctoken plain">cResult</span><span class="ctoken plain">: </span><span class="ctoken class-name">ARDK_MeshDownloader_Data</span><span class="ctoken plain">, </span><span class="ctoken plain">owner</span><span class="ctoken plain">: </span><span class="ctoken class-name">[ResourceOwner](https://www.nianticspatial.com/docs/api/swift/NSDK.interface-ResourceOwner/ "Browse to ResourceOwner")</span><span class="ctoken plain">?)</span></span>

</div>

------------------------------------------------------------------------

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

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
<td><span id="property-imagedata"></span><span class="ctoken-line"><span class="ctoken keyword">let</span><span class="ctoken plain"> </span><span class="ctoken class-name">imageData</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKBuffer/" title="A buffer containing binary data for NSDK operations....">NSDKBuffer</a></span></span></td>
<td><div class="ctoken comment">
The texture image data for the mesh, or an empty buffer if texture was not requested.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-meshdata"></span><span class="ctoken-line"><span class="ctoken keyword">let</span><span class="ctoken plain"> </span><span class="ctoken class-name">meshData</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-MeshData/" title="Contains 3D mesh data for rendering and visualization....">MeshData</a></span></span></td>
<td><div class="ctoken comment">
The mesh geometry data containing vertices, faces, and texture coordinates.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-transform"></span><span class="ctoken-line"><span class="ctoken keyword">let</span><span class="ctoken plain"> </span><span class="ctoken class-name">transform</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float4x4</a></span></span></td>
<td><div class="ctoken comment">
The transform matrix that positions this mesh in world space.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
