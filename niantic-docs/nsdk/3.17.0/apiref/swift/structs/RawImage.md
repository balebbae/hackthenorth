---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/RawImage/
title: RawImage
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `RawImage`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct RawImage
```

</div>

</div>

A raw image containing pixel data for ARDK operations.

`RawImage` provides access to image data in various formats (RGB, grayscale, depth, etc.) used by ARDK features like depth processing, semantic segmentation, and image analysis.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Raw images are used throughout ARDK for:

- Camera frame processing
- Depth map representation
- Semantic segmentation results
- Image format conversions
- Computer vision operations

## Example Usage<a href="#example-usage" class="hash-link" aria-label="Direct link to Example Usage" title="Direct link to Example Usage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let (status, depthResult) = depthSession.getDepth()
if status.isOk() {
    let image = depthResult.image
    print("Image size: \(image.width) x \(image.height)")
    print("Image type: \(image.type)")
    
    // Access pixel data
    let pixelData = image.data
    // Process pixel data based on image type
}
```

</div>

</div>

## Memory Management<a href="#memory-management" class="hash-link" aria-label="Direct link to Memory Management" title="Direct link to Memory Management">​</a>

This object's pointers are only valid when the ARDK objects that holds it are still in scope.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `width`<a href="#width" class="hash-link" aria-label="Direct link to width" title="Direct link to width">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let width: UInt
```

</div>

</div>

Width of the image in pixels.

This represents the number of pixels in each row of the image.

### `height`<a href="#height" class="hash-link" aria-label="Direct link to height" title="Direct link to height">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let height: UInt
```

</div>

</div>

Height of the image in pixels.

This represents the number of rows in the image.

### `data`<a href="#data" class="hash-link" aria-label="Direct link to data" title="Direct link to data">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let data: UnsafeMutableRawPointer
```

</div>

</div>

Pointer to the raw pixel data.

This provides direct access to the image's pixel data. The format and interpretation of the data depends on the `type` property.

### `type`<a href="#type" class="hash-link" aria-label="Direct link to type" title="Direct link to type">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let type: ImageType
```

</div>

</div>

Format and type of the image data.

This indicates how the pixel data should be interpreted, including the number of channels, data type, and color space.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(ptr:width:height:type:)`<a href="#initptrwidthheighttype" class="hash-link" aria-label="Direct link to initptrwidthheighttype" title="Direct link to initptrwidthheighttype">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(ptr: UnsafeMutableRawPointer, width: UInt, height: UInt, type: ImageType)
```

</div>

</div>

</div>

</div>
