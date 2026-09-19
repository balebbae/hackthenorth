---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/VoxelBuffer/
title: VoxelBuffer
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `VoxelBuffer`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public class VoxelBuffer
```

</div>

</div>

A read-only container for the voxel buffer information generated during scanning.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `positions`<a href="#positions" class="hash-link" aria-label="Direct link to positions" title="Direct link to positions">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var positions: UnsafeMutableBufferPointer\<Float\>
```

</div>

</div>

The positions of the voxels. Array of 3 floats per voxel.

- Attention: These pointers are valid as long as this class does not go out of scope.

### `colors`<a href="#colors" class="hash-link" aria-label="Direct link to colors" title="Direct link to colors">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var colors: UnsafeMutableBufferPointer\<UInt8\>
```

</div>

</div>

The colors of the voxels. Array of 4 bytes per voxel.

- Attention: These pointers are valid as long as this class does not go out of scope.

### `normals`<a href="#normals" class="hash-link" aria-label="Direct link to normals" title="Direct link to normals">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var normals: UnsafeMutableBufferPointer\<Float\>
```

</div>

</div>

The normals of the voxels. Array of 3 floats per voxel.

- Attention: These pointers are valid as long as this class does not go out of scope.

### `voxelSize`<a href="#voxelsize" class="hash-link" aria-label="Direct link to voxelsize" title="Direct link to voxelsize">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var voxelSize: Float
```

</div>

</div>

The size of the voxels.

</div>

</div>
