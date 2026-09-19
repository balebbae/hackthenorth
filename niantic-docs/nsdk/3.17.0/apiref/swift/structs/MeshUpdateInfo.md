---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/MeshUpdateInfo/
title: MeshUpdateInfo
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `MeshUpdateInfo`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct MeshUpdateInfo
```

</div>

</div>

Information about mesh chunk updates from live meshing operations.

Returned by `ArdkMeshingSession.updatedMeshInfos()` to indicate which mesh chunks have been modified or removed since the last update.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `ids`<a href="#ids" class="hash-link" aria-label="Direct link to ids" title="Direct link to ids">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var ids: UnsafeBufferPointer\<Int64\>
```

</div>

</div>

Array of all mesh chunk IDs.

When a chunk is removed from the mesh, it will no longer be present in this array. The application should keep track of its current mesh chunk IDs to determine when a chunk has been removed.

### `updated`<a href="#updated" class="hash-link" aria-label="Direct link to updated" title="Direct link to updated">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var updated: UnsafeBufferPointer\<UInt8\>
```

</div>

</div>

Array indicating whether each chunk was updated or removed.

For each corresponding ID in `ids`, this array indicates:

- **Non-zero value**: The chunk has been updated since the last call to `meshDataById`. Call `meshDataById` to read the latest mesh data. Calling `meshDataById` will reset the update status for that chunk to 0.
- **Zero value**: The chunk has not been updated since the last call to `meshDataById`, so there is no need to read its mesh data.

</div>

</div>
