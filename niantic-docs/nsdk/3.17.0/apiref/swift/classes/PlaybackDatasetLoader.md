---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/PlaybackDatasetLoader/
title: PlaybackDatasetLoader
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `PlaybackDatasetLoader`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
open class PlaybackDatasetLoader : PlaybackDatasetSource
```

</div>

</div>

Base class for loading playback dataset data from various sources.

This class provides a base implementation that must be subclassed. Subclasses must override `loadCaptureJSON()` and `loadImage(imageName:)` to provide concrete implementations.

- Note: This class acts as an abstract base class. Do not instantiate directly. Subclasses must override `loadCaptureJSON()` and `loadImage(imageName:)`.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `loadCaptureJSON()`<a href="#loadcapturejson" class="hash-link" aria-label="Direct link to loadcapturejson" title="Direct link to loadcapturejson">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func loadCaptureJSON() -> Data?
```

</div>

</div>

Loads the capture JSON data from the data source.

This method must be overridden by subclasses. The base implementation will crash if called.

- Returns: The JSON data as `Data`, or `nil` if loading fails
- Important: Subclasses must override this method. Do not call the base implementation.

### `loadImage(imageName:)`<a href="#loadimageimagename" class="hash-link" aria-label="Direct link to loadimageimagename" title="Direct link to loadimageimagename">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func loadImage(imageName: String) -> CGImage?
```

</div>

</div>

Loads an image from the data source.

This method must be overridden by subclasses. The base implementation will crash if called.

- Parameter imageName: The filename of the image (e.g., "frame_00000000.jpg")
- Returns: The image as a `CGImage`, or `nil` if loading fails
- Important: Subclasses must override this method. Do not call the base implementation.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name      | Description                                            |
|-----------|--------------------------------------------------------|
| imageName | The filename of the image (e.g., “frame_00000000.jpg”) |

### `info()`<a href="#info" class="hash-link" aria-label="Direct link to info" title="Direct link to info">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func info() -> String
```

</div>

</div>

### `loadDataset()`<a href="#loaddataset" class="hash-link" aria-label="Direct link to loaddataset" title="Direct link to loaddataset">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func loadDataset() -> PlaybackDataset?
```

</div>

</div>

</div>

</div>
