---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/AwarenessResult/
title: AwarenessResult
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `AwarenessResult`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public class AwarenessResult
```

</div>

</div>

Base class for awarness results such as depth and segmentation. Provides common properties like frame ID, timestamp, camera pose, and intrinsics.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `frameId`<a href="#frameid" class="hash-link" aria-label="Direct link to frameid" title="Direct link to frameid">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let frameId: UInt64
```

</div>

</div>

Unique identifier for the processed frame

### `timestampMs`<a href="#timestampms" class="hash-link" aria-label="Direct link to timestampms" title="Direct link to timestampms">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let timestampMs: UInt64
```

</div>

</div>

The timestamp of the AR frame that this awareness result was generated from.

### `pose`<a href="#pose" class="hash-link" aria-label="Direct link to pose" title="Direct link to pose">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let pose: simd_float4x4
```

</div>

</div>

The camera pose matrix when the depth data was captured.

This 4x4 transformation matrix represents the camera's position and orientation in the world coordinate system. Use this for coordinate transformations between camera and world spaces.

### `intrinsics`<a href="#intrinsics" class="hash-link" aria-label="Direct link to intrinsics" title="Direct link to intrinsics">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let intrinsics: simd_float3x3
```

</div>

</div>

The camera intrinsic parameters.

This 3x3 matrix contains the camera's focal length, principal point, and other intrinsic parameters needed for coordinate transformations between image and camera coordinate systems.

</div>

</div>
