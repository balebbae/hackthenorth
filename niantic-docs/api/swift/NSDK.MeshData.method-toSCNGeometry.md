---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.MeshData.method-toSCNGeometry/
title: toSCNGeometry
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[MeshData](https://www.nianticspatial.com/docs/api/swift/NSDK.class-MeshData/ "MeshData") 

</div>

<div class="api-title">

#  toSCNGeometry

<div class="api-package">

Creates a SceneKit geometry from this mesh chunk's vertex positions, normals and triangle indices.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">toSCNGeometry</span><span class="ctoken plain">(</span><span class="ctoken plain">material</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//scenekit/SCNMaterial" target="_blank" rel="noopener noreferrer" title="Opens an external reference">SCNMaterial</a></span><span class="ctoken plain">? = nil) -\> </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//scenekit/SCNGeometry" target="_blank" rel="noopener noreferrer" title="Opens an external reference">SCNGeometry</a></span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Creates a SceneKit geometry from this mesh chunk's vertex positions, normals and triangle indices.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

`SCNGeometry` representing the mesh.

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
<td><span id="external parameter-material"></span><span class="ctoken-line"><span class="ctoken class-name">material</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//scenekit/SCNMaterial" target="_blank" rel="noopener noreferrer" title="Opens an external reference">SCNMaterial</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Optional material to apply to the resulting geometry.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
