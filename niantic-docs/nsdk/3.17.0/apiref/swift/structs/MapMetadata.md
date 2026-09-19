---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/MapMetadata/
title: MapMetadata
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `MapMetadata`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct MapMetadata
```

</div>

</div>

Structure representing the metadata of a device map for visualization and processing.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `pointsCount`<a href="#pointscount" class="hash-link" aria-label="Direct link to pointscount" title="Direct link to pointscount">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let pointsCount: UInt32
```

</div>

</div>

The number of feature points in the map.

### `usesLearnedFeatures`<a href="#useslearnedfeatures" class="hash-link" aria-label="Direct link to useslearnedfeatures" title="Direct link to useslearnedfeatures">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let usesLearnedFeatures: Bool
```

</div>

</div>

Whether the map uses learned features.

### `owner`<a href="#owner" class="hash-link" aria-label="Direct link to owner" title="Direct link to owner">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let owner: ResourceOwner?
```

</div>

</div>

The owner of the map metadata.

- Attention: The owner must be released when the map metadata is no longer needed.

### `points`<a href="#points" class="hash-link" aria-label="Direct link to points" title="Direct link to points">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var points: [Float]
```

</div>

</div>

### `errors`<a href="#errors" class="hash-link" aria-label="Direct link to errors" title="Direct link to errors">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var errors: [Float]
```

</div>

</div>

</div>

</div>
