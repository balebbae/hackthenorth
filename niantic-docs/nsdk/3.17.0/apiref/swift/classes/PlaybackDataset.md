---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/PlaybackDataset/
title: PlaybackDataset
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `PlaybackDataset`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public class PlaybackDataset
```

</div>

</div>

A dataset loaded from a capture JSON file containing frame metadata and images.

This class loads all frame images into memory during initialization. For large datasets, consider implementing lazy loading to reduce memory pressure.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `hasDepth()`<a href="#hasdepth" class="hash-link" aria-label="Direct link to hasdepth" title="Direct link to hasdepth">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func hasDepth() -> Bool
```

</div>

</div>

Checks if the dataset has depth data from a LiDAR source.

- Returns: `true` if `depthSource` exists and equals "lidar", `false` otherwise

</div>

</div>
