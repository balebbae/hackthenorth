---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/ArdkObjectDetectionSession.Configuration/
title: ArdkObjectDetectionSession.Configuration
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `ArdkObjectDetectionSession.Configuration`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
struct Configuration
```

</div>

</div>

Configuration structure for the object detection session.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `frameRate`<a href="#framerate" class="hash-link" aria-label="Direct link to framerate" title="Direct link to framerate">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var frameRate: UInt32
```

</div>

</div>

Inference frequency

### `framesUntilSeen`<a href="#framesuntilseen" class="hash-link" aria-label="Direct link to framesuntilseen" title="Direct link to framesuntilseen">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var framesUntilSeen: UInt32
```

</div>

</div>

Number of consecutive frames and object must be detected in order to be considered "seen"

### `framesUntilDiscarded`<a href="#framesuntildiscarded" class="hash-link" aria-label="Direct link to framesuntildiscarded" title="Direct link to framesuntildiscarded">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var framesUntilDiscarded: UInt32
```

</div>

</div>

Number of consecutive frames an object can be missing before it is discarded from detection results

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init()`<a href="#init" class="hash-link" aria-label="Direct link to init" title="Direct link to init">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init()
```

</div>

</div>

Initializes a new object detection session configuration with default settings.

### `init(frameRate:framesUntilSeen:framesUntilDiscarded:)`<a href="#initframerateframesuntilseenframesuntildiscarded" class="hash-link" aria-label="Direct link to initframerateframesuntilseenframesuntildiscarded" title="Direct link to initframerateframesuntilseenframesuntildiscarded">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(frameRate: UInt32, framesUntilSeen: UInt32, framesUntilDiscarded: UInt32)
```

</div>

</div>

Initializes a new object detection session configuration with custom settings.

- Parameters:
  - frameRate: The number of frames per second to process for detection.
  - framesUntilSeen: The number of consecutive frames an object must be detected before it is considered "seen".
  - framesUntilDiscarded: The number of consecutive frames an object can be missing before it is discarded from detection results.

`framesUntilSeen` and `framesUntilDiscarded` help stabilize detection results, preventing objects from flickering in and out of view.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| frameRate | The number of frames per second to process for detection. |
| framesUntilSeen | The number of consecutive frames an object must be detected before it is considered “seen”. |
| framesUntilDiscarded | The number of consecutive frames an object can be missing before it is discarded from detection results. |

</div>

</div>
