---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/PlaybackSession/
title: PlaybackSession
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `PlaybackSession`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public class PlaybackSession
```

</div>

</div>

A session that plays back frame metadata and images from a loaded dataset.

Playback runs on a background queue and continuously loops through frames at the framerate specified in the dataset. The session notifies its delegate of each frame update.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `delegate`<a href="#delegate" class="hash-link" aria-label="Direct link to delegate" title="Direct link to delegate">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
open var delegate: (any PlaybackSessionDelegate)?
```

</div>

</div>

Delegate that receives frame updates during playback

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(dataset:)`<a href="#initdataset" class="hash-link" aria-label="Direct link to initdataset" title="Direct link to initdataset">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(dataset: PlaybackDataset)
```

</div>

</div>

Initializes a new playback session with an existing dataset.

- Parameter dataset: The playback dataset to use

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name    | Description                 |
|---------|-----------------------------|
| dataset | The playback dataset to use |

### `run()`<a href="#run" class="hash-link" aria-label="Direct link to run" title="Direct link to run">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func run()
```

</div>

</div>

Starts playback of the dataset.

Playback runs asynchronously on a background queue. Call `pause()` to stop playback.

### `pause()`<a href="#pause" class="hash-link" aria-label="Direct link to pause" title="Direct link to pause">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func pause()
```

</div>

</div>

Pauses playback.

The playback loop will exit on the next iteration after this is called. The current frame index is preserved, so calling `run()` again will resume from the same position.

### `hasDepth()`<a href="#hasdepth" class="hash-link" aria-label="Direct link to hasdepth" title="Direct link to hasdepth">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func hasDepth() -> Bool
```

</div>

</div>

Checks if the playback dataset has depth data from a LiDAR source.

- Returns: `true` if `depthSource` exists and equals "lidar", `false` otherwise

### `deinit`<a href="#deinit" class="hash-link" aria-label="Direct link to deinit" title="Direct link to deinit">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
deinit
```

</div>

</div>

</div>

</div>
