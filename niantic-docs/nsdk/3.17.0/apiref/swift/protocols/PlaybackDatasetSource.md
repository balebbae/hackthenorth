---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/protocols/PlaybackDatasetSource/
title: PlaybackDatasetSource
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**PROTOCOL**

<div>

# `PlaybackDatasetSource`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public protocol PlaybackDatasetSource
```

</div>

</div>

Protocol for loading playback dataset data from various sources.

This protocol abstracts base retrieval, allowing for different implementations such as bundle loading, file system loading, remote loading, or mock data for testing.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `loadCaptureJSON()`<a href="#loadcapturejson" class="hash-link" aria-label="Direct link to loadcapturejson" title="Direct link to loadcapturejson">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
func loadCaptureJSON() -> Data?
```

</div>

</div>

Loads the capture JSON data from the data source.

- Parameter location: The location identifier/path for the dataset (e.g., a directory path, URL path, or dataset identifier)
- Returns: The JSON data as `Data`, or `nil` if loading fails

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| location | The location identifier/path for the dataset (e.g., a directory path, URL path, or dataset identifier) |

### `loadImage(imageName:)`<a href="#loadimageimagename" class="hash-link" aria-label="Direct link to loadimageimagename" title="Direct link to loadimageimagename">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
func loadImage(imageName: String) -> CGImage?
```

</div>

</div>

Loads an image from the data source.

- Parameters:
  - imageName: The filename of the image (e.g., "frame_00000000.jpg")
  - location: The location identifier/path for the dataset (e.g., a directory path, URL path, or dataset identifier)
- Returns: The image as a `CGImage`, or `nil` if loading fails

#### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| imageName | The filename of the image (e.g., “frame_00000000.jpg”) |
| location | The location identifier/path for the dataset (e.g., a directory path, URL path, or dataset identifier) |

### `info()`<a href="#info" class="hash-link" aria-label="Direct link to info" title="Direct link to info">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
func info() -> String
```

</div>

</div>

Returns details about the loader configuration.

- Returns: A string describing the loader configuration

</div>

</div>
