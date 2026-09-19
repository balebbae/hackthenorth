---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/ArdkFrameData.CameraPlane/
title: ArdkFrameData.CameraPlane
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `ArdkFrameData.CameraPlane`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct CameraPlane: Equatable
```

</div>

</div>

A single plane of camera image data.

Camera images often contain multiple planes of data (Y, U, V for YUV format, etc.). This structure describes the memory layout and dimensions of a single image plane.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `dataPtr`<a href="#dataptr" class="hash-link" aria-label="Direct link to dataptr" title="Direct link to dataptr">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var dataPtr: UnsafePointer\<UInt8\>
```

</div>

</div>

Pointer to the raw pixel data for this plane.

The data format depends on the image format and plane index. For example, in YUV format, plane 0 contains luminance data.

### `dataSize`<a href="#datasize" class="hash-link" aria-label="Direct link to datasize" title="Direct link to datasize">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var dataSize: UInt32
```

</div>

</div>

Total size of the data in bytes.

This represents the complete size of the memory buffer pointed to by `dataPtr`.

### `pixelStride`<a href="#pixelstride" class="hash-link" aria-label="Direct link to pixelstride" title="Direct link to pixelstride">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var pixelStride: UInt32
```

</div>

</div>

Number of bytes between adjacent pixels in the same row.

For packed formats this is typically 1, but some formats may have multiple bytes per pixel or padding between pixels.

### `rowStride`<a href="#rowstride" class="hash-link" aria-label="Direct link to rowstride" title="Direct link to rowstride">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var rowStride: UInt32
```

</div>

</div>

Number of bytes between the start of adjacent rows.

This may be larger than `width * pixelStride` if there is padding at the end of each row.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(dataPtr:dataSize:pixelStride:rowStride:)`<a href="#initdataptrdatasizepixelstriderowstride" class="hash-link" aria-label="Direct link to initdataptrdatasizepixelstriderowstride" title="Direct link to initdataptrdatasizepixelstriderowstride">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(dataPtr: UnsafePointer\<UInt8\>,
            dataSize: UInt32,
            pixelStride: UInt32,
            rowStride: UInt32)
```

</div>

</div>

Creates a camera plane with the specified memory layout parameters.

- Parameters:
  - dataPtr: Pointer to the raw pixel data
  - dataSize: Total size of the data in bytes
  - pixelStride: Bytes between adjacent pixels
  - rowStride: Bytes between adjacent rows

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name        | Description                     |
|-------------|---------------------------------|
| dataPtr     | Pointer to the raw pixel data   |
| dataSize    | Total size of the data in bytes |
| pixelStride | Bytes between adjacent pixels   |
| rowStride   | Bytes between adjacent rows     |

</div>

</div>
