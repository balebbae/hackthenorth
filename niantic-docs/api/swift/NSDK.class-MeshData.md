---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.class-MeshData/
title: MeshData
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

#  MeshData

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">MeshData</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Contains 3D mesh data for rendering and visualization. `MeshData` provides access to 3D mesh geometry including vertices, indices, normals, and texture coordinates.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

MeshData includes:

- **Vertices**: 3D position data for mesh geometry
- **Indices**: The triangles that make up the mesh
- **Normals**: Surface normal vectors for the vertices, commonly used for lighting calculations (only available for live meshing)
- **UVs**: Texture coordinates for the vertices, used for mapping textures to the mesh (only available for mesh downloader)

## Example Usage<a href="#example-usage" class="hash-link" aria-label="Direct link to Example Usage" title="Direct link to Example Usage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let (status, meshData) = meshDownloader.downloadMesh(meshId: meshId)
if status.isOk() {
    print("Mesh vertices: \(meshData.vertices.count)")
    print("Mesh triangles: \(meshData.indices.count / 3)")
    // Convert to SceneKit geometry for rendering
    if let geometry = meshData.toSCNGeometry() {
        let node = SCNNode(geometry: geometry)
        sceneView.scene.rootNode.addChildNode(node)
    }
}
```

</div>

</div>

## Memory Management<a href="#memory-management" class="hash-link" aria-label="Direct link to Memory Management" title="Direct link to Memory Management">​</a>

Mesh data is backed by native memory that is automatically managed. The data remains valid as long as the `MeshData` instance exists.

------------------------------------------------------------------------

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">init</span><span class="ctoken plain">(</span><span class="ctoken plain">fromC</span><span class="ctoken plain"> </span><span class="ctoken plain">cMeshData</span><span class="ctoken plain">: </span><span class="ctoken class-name">ARDK_MeshData</span><span class="ctoken plain">, </span><span class="ctoken plain">owner</span><span class="ctoken plain">: </span><span class="ctoken class-name">[ResourceOwner](https://www.nianticspatial.com/docs/api/swift/NSDK.interface-ResourceOwner/ "Browse to ResourceOwner")</span><span class="ctoken plain">? = nil)</span></span>

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
<td><span id="property-indicesptr"></span><span class="ctoken-line"><span class="ctoken keyword">let</span><span class="ctoken plain"> </span><span class="ctoken class-name">indicesPtr</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/unsafebufferpointer" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UnsafeBufferPointer</a></span><span class="ctoken plain">&lt;</span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/uint32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UInt32</a></span><span class="ctoken plain">&gt;</span></span></td>
<td><div class="ctoken comment">
Pointer to the indices data. Array of 3 indices per triangle.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-normalsptr"></span><span class="ctoken-line"><span class="ctoken keyword">let</span><span class="ctoken plain"> </span><span class="ctoken class-name">normalsPtr</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/unsafebufferpointer" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UnsafeBufferPointer</a></span><span class="ctoken plain">&lt;</span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain">&gt;?</span></span></td>
<td><div class="ctoken comment">
Pointer to the normals data. Array of 3 floats per normal. Only available for live meshing.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-uvsptr"></span><span class="ctoken-line"><span class="ctoken keyword">let</span><span class="ctoken plain"> </span><span class="ctoken class-name">uvsPtr</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/unsafebufferpointer" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UnsafeBufferPointer</a></span><span class="ctoken plain">&lt;</span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain">&gt;?</span></span></td>
<td><div class="ctoken comment">
Pointer to the UVs data. Array of 2 floats per UV.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-verticesptr"></span><span class="ctoken-line"><span class="ctoken keyword">let</span><span class="ctoken plain"> </span><span class="ctoken class-name">verticesPtr</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/unsafebufferpointer" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UnsafeBufferPointer</a></span><span class="ctoken plain">&lt;</span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain">&gt;</span></span></td>
<td><div class="ctoken comment">
Pointer to the vertices data. Array of 3 floats per vertex.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

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
<td><span id="method-toscngeometry"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.MeshData.method-toSCNGeometry/" title="Creates a SceneKit geometry from this mesh chunk&#39;s vertex positions, normals and triangle indices.">toSCNGeometry</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//scenekit/SCNGeometry" target="_blank" rel="noopener noreferrer" title="Opens an external reference">SCNGeometry</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Creates a SceneKit geometry from this mesh chunk's vertex positions, normals and triangle indices.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
