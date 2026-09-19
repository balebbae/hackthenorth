---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/PlaybackDataset.CaptureRoot/
title: PlaybackDataset.CaptureRoot
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `PlaybackDataset.CaptureRoot`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct CaptureRoot: Codable
```

</div>

</div>

Root structure for the capture JSON file

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `app`<a href="#app" class="hash-link" aria-label="Direct link to app" title="Direct link to app">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let app: String
```

</div>

</div>

### `autofocus`<a href="#autofocus" class="hash-link" aria-label="Direct link to autofocus" title="Direct link to autofocus">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let autofocus: Int
```

</div>

</div>

### `coordinates`<a href="#coordinates" class="hash-link" aria-label="Direct link to coordinates" title="Direct link to coordinates">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let coordinates: String
```

</div>

</div>

### `duration`<a href="#duration" class="hash-link" aria-label="Direct link to duration" title="Direct link to duration">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let duration: Double
```

</div>

</div>

### `formatVersion`<a href="#formatversion" class="hash-link" aria-label="Direct link to formatversion" title="Direct link to formatversion">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let formatVersion: String
```

</div>

</div>

### `frameCount`<a href="#framecount" class="hash-link" aria-label="Direct link to framecount" title="Direct link to framecount">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let frameCount: Int
```

</div>

</div>

### `framerate`<a href="#framerate" class="hash-link" aria-label="Direct link to framerate" title="Direct link to framerate">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let framerate: Double
```

</div>

</div>

### `frames`<a href="#frames" class="hash-link" aria-label="Direct link to frames" title="Direct link to frames">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let frames: [FrameMetadata]
```

</div>

</div>

### `imageFormat`<a href="#imageformat" class="hash-link" aria-label="Direct link to imageformat" title="Direct link to imageformat">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let imageFormat: String
```

</div>

</div>

### `imageQuality`<a href="#imagequality" class="hash-link" aria-label="Direct link to imagequality" title="Direct link to imagequality">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let imageQuality: Int
```

</div>

</div>

### `manufacturer`<a href="#manufacturer" class="hash-link" aria-label="Direct link to manufacturer" title="Direct link to manufacturer">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let manufacturer: String
```

</div>

</div>

### `metadata`<a href="#metadata" class="hash-link" aria-label="Direct link to metadata" title="Direct link to metadata">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let metadata: CaptureMetadata?
```

</div>

</div>

### `model`<a href="#model" class="hash-link" aria-label="Direct link to model" title="Direct link to model">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let model: String
```

</div>

</div>

### `recorder`<a href="#recorder" class="hash-link" aria-label="Direct link to recorder" title="Direct link to recorder">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let recorder: String
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

### `timestamp`<a href="#timestamp" class="hash-link" aria-label="Direct link to timestamp" title="Direct link to timestamp">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let timestamp: Double
```

</div>

</div>

### `timezone`<a href="#timezone" class="hash-link" aria-label="Direct link to timezone" title="Direct link to timezone">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let timezone: Int
```

</div>

</div>

### `uuid`<a href="#uuid" class="hash-link" aria-label="Direct link to uuid" title="Direct link to uuid">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let uuid: String
```

</div>

</div>

### `depthFormat`<a href="#depthformat" class="hash-link" aria-label="Direct link to depthformat" title="Direct link to depthformat">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let depthFormat: String?
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

### `depthSource`<a href="#depthsource" class="hash-link" aria-label="Direct link to depthsource" title="Direct link to depthsource">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let depthSource: String?
```

</div>

</div>

</div>

</div>
