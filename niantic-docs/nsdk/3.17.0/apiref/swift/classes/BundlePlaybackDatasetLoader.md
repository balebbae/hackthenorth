---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/BundlePlaybackDatasetLoader/
title: BundlePlaybackDatasetLoader
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `BundlePlaybackDatasetLoader`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public class BundlePlaybackDatasetLoader: PlaybackDatasetLoader
```

</div>

</div>

A loader that retrieves playback dataset data from the app bundle.

This is the default implementation for loading datasets from `Bundle.main`.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(directory:bundle:)`<a href="#initdirectorybundle" class="hash-link" aria-label="Direct link to initdirectorybundle" title="Direct link to initdirectorybundle">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(directory: String, bundle: Bundle = .main)
```

</div>

</div>

Initializes a bundle loader with the specified bundle.

- Parameter bundle: The bundle to load resources from (defaults to `Bundle.main`)

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name   | Description                                                   |
|--------|---------------------------------------------------------------|
| bundle | The bundle to load resources from (defaults to `Bundle.main`) |

### `loadCaptureJSON()`<a href="#loadcapturejson" class="hash-link" aria-label="Direct link to loadcapturejson" title="Direct link to loadcapturejson">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public override func loadCaptureJSON() -> Data?
```

</div>

</div>

### `loadImage(imageName:)`<a href="#loadimageimagename" class="hash-link" aria-label="Direct link to loadimageimagename" title="Direct link to loadimageimagename">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public override func loadImage(imageName: String) -> CGImage?
```

</div>

</div>

#### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name      | Description                                            |
|-----------|--------------------------------------------------------|
| imageName | The filename of the image (e.g., “frame_00000000.jpg”) |

### `info()`<a href="#info" class="hash-link" aria-label="Direct link to info" title="Direct link to info">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public override func info() -> String
```

</div>

</div>

</div>

</div>
