---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/PlaybackDataset.FrameMetadata/
title: PlaybackDataset.FrameMetadata
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `PlaybackDataset.FrameMetadata`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct FrameMetadata: Codable
```

</div>

</div>

Frame metadata structure matching the JSON format

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `image`<a href="#image" class="hash-link" aria-label="Direct link to image" title="Direct link to image">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let image: String
```

</div>

</div>

### `intrinsics`<a href="#intrinsics" class="hash-link" aria-label="Direct link to intrinsics" title="Direct link to intrinsics">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let intrinsics: [Double]
```

</div>

</div>

### `location`<a href="#location" class="hash-link" aria-label="Direct link to location" title="Direct link to location">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let location: LocationMetadata
```

</div>

</div>

### `screenOrientation`<a href="#screenorientation" class="hash-link" aria-label="Direct link to screenorientation" title="Direct link to screenorientation">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let screenOrientation: String?
```

</div>

</div>

### `pose`<a href="#pose" class="hash-link" aria-label="Direct link to pose" title="Direct link to pose">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let pose: [Double]
```

</div>

</div>

### `pose4x4`<a href="#pose4x4" class="hash-link" aria-label="Direct link to pose4x4" title="Direct link to pose4x4">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let pose4x4: [Double]
```

</div>

</div>

### `projection`<a href="#projection" class="hash-link" aria-label="Direct link to projection" title="Direct link to projection">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let projection: [Double]?
```

</div>

</div>

### `resolution`<a href="#resolution" class="hash-link" aria-label="Direct link to resolution" title="Direct link to resolution">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let resolution: [Int]
```

</div>

</div>

### `saveDuration`<a href="#saveduration" class="hash-link" aria-label="Direct link to saveduration" title="Direct link to saveduration">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let saveDuration: Double?
```

</div>

</div>

### `sequence`<a href="#sequence" class="hash-link" aria-label="Direct link to sequence" title="Direct link to sequence">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let sequence: Int
```

</div>

</div>

### `timestamp`<a href="#timestamp" class="hash-link" aria-label="Direct link to timestamp" title="Direct link to timestamp">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let timestamp: Double
```

</div>

</div>

### `tracking`<a href="#tracking" class="hash-link" aria-label="Direct link to tracking" title="Direct link to tracking">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let tracking: Int
```

</div>

</div>

### `trackingReason`<a href="#trackingreason" class="hash-link" aria-label="Direct link to trackingreason" title="Direct link to trackingreason">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let trackingReason: Int
```

</div>

</div>

### `depth`<a href="#depth" class="hash-link" aria-label="Direct link to depth" title="Direct link to depth">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let depth: String?
```

</div>

</div>

### `depthConfidence`<a href="#depthconfidence" class="hash-link" aria-label="Direct link to depthconfidence" title="Direct link to depthconfidence">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let depthConfidence: String?
```

</div>

</div>

### `depthResolution`<a href="#depthresolution" class="hash-link" aria-label="Direct link to depthresolution" title="Direct link to depthresolution">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let depthResolution: [Int]?
```

</div>

</div>

### `depthTimestamp`<a href="#depthtimestamp" class="hash-link" aria-label="Direct link to depthtimestamp" title="Direct link to depthtimestamp">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let depthTimestamp: Double?
```

</div>

</div>

</div>

</div>
