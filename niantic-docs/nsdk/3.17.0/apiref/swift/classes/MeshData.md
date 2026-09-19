---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/MeshData/
title: MeshData
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `MeshData`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public class MeshData
```

</div>

</div>

Contains 3D mesh data for rendering and visualization.

`MeshData` provides access to 3D mesh geometry including vertices, indices, normals, and texture coordinates.

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

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `verticesPtr`<a href="#verticesptr" class="hash-link" aria-label="Direct link to verticesptr" title="Direct link to verticesptr">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let verticesPtr: UnsafeBufferPointer\<Float\>
```

</div>

</div>

Pointer to the vertices data. Array of 3 floats per vertex.

### `uvsPtr`<a href="#uvsptr" class="hash-link" aria-label="Direct link to uvsptr" title="Direct link to uvsptr">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let uvsPtr: UnsafeBufferPointer\<Float\>?
```

</div>

</div>

Pointer to the UVs data. Array of 2 floats per UV.

### `indicesPtr`<a href="#indicesptr" class="hash-link" aria-label="Direct link to indicesptr" title="Direct link to indicesptr">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let indicesPtr: UnsafeBufferPointer\<UInt32\>
```

</div>

</div>

Pointer to the indices data. Array of 3 indices per triangle.

### `normalsPtr`<a href="#normalsptr" class="hash-link" aria-label="Direct link to normalsptr" title="Direct link to normalsptr">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let normalsPtr: UnsafeBufferPointer\<Float\>?
```

</div>

</div>

Pointer to the normals data. Array of 3 floats per normal. Only available for live meshing.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(fromC:owner:)`<a href="#initfromcowner" class="hash-link" aria-label="Direct link to initfromcowner" title="Direct link to initfromcowner">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(fromC cMeshData: ARDK_MeshData, owner: ResourceOwner? = nil)
```

</div>

</div>

### `toSCNGeometry(material:)`<a href="#toscngeometrymaterial" class="hash-link" aria-label="Direct link to toscngeometrymaterial" title="Direct link to toscngeometrymaterial">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func toSCNGeometry(material: SCNMaterial? = nil) -> SCNGeometry?
```

</div>

</div>

Creates a SceneKit geometry from this mesh chunk's vertex positions, normals and triangle indices.

- Parameter material: Optional material to apply to the resulting geometry.
- Returns: `SCNGeometry` representing the mesh.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name     | Description                                           |
|----------|-------------------------------------------------------|
| material | Optional material to apply to the resulting geometry. |

</div>

</div>
