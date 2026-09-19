---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/MeshDownloaderResults/
title: MeshDownloaderResults
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `MeshDownloaderResults`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public final class MeshDownloaderResults: @unchecked Sendable
```

</div>

</div>

Contains the downloaded mesh geometry data for a VPS location.

This object holds an array of mesh results, where each result includes mesh geometry, texture data (if requested), and the transform matrix that positions the mesh in world space.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `results`<a href="#results" class="hash-link" aria-label="Direct link to results" title="Direct link to results">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let results: [MeshDownloaderResult]
```

</div>

</div>

The array of mesh results for the requested location.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(fromC:owner:)`<a href="#initfromcowner" class="hash-link" aria-label="Direct link to initfromcowner" title="Direct link to initfromcowner">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(fromC cResults: ARDK_MeshDownloader_Results, owner: ResourceOwner?)
```

</div>

</div>

</div>

</div>
