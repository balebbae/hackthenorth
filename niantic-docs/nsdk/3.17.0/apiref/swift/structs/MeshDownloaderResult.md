---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/MeshDownloaderResult/
title: MeshDownloaderResult
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `MeshDownloaderResult`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct MeshDownloaderResult
```

</div>

</div>

Represents a single mesh result with geometry, texture, and transform data.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `meshData`<a href="#meshdata" class="hash-link" aria-label="Direct link to meshdata" title="Direct link to meshdata">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let meshData: MeshData
```

</div>

</div>

The mesh geometry data containing vertices, faces, and texture coordinates.

### `imageData`<a href="#imagedata" class="hash-link" aria-label="Direct link to imagedata" title="Direct link to imagedata">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let imageData: ArdkBuffer
```

</div>

</div>

The texture image data for the mesh, or an empty buffer if texture was not requested.

### `transform`<a href="#transform" class="hash-link" aria-label="Direct link to transform" title="Direct link to transform">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let transform: simd_float4x4
```

</div>

</div>

The transform matrix that positions this mesh in world space.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(fromC:owner:)`<a href="#initfromcowner" class="hash-link" aria-label="Direct link to initfromcowner" title="Direct link to initfromcowner">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(fromC cResult: ARDK_MeshDownloader_Data, owner: ResourceOwner?)
```

</div>

</div>

</div>

</div>
