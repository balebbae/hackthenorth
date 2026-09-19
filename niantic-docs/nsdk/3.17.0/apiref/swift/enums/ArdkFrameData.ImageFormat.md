---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/enums/ArdkFrameData.ImageFormat/
title: ArdkFrameData.ImageFormat
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**ENUM**

<div>

# `ArdkFrameData.ImageFormat`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public enum ImageFormat
```

</div>

</div>

Supported image formats for camera and depth data.

These formats define how pixel data is organized in memory and what each pixel value represents. Different formats are used for color images versus depth images.

## Cases<a href="#cases" class="hash-link" aria-label="Direct link to Cases" title="Direct link to Cases">​</a>

### `unknown`<a href="#unknown" class="hash-link" aria-label="Direct link to unknown" title="Direct link to unknown">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case unknown
```

</div>

</div>

Unknown or unsupported image format.

### `YUV420NV12`<a href="#yuv420nv12" class="hash-link" aria-label="Direct link to yuv420nv12" title="Direct link to yuv420nv12">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case YUV420NV12
```

</div>

</div>

YUV 4:2:0 format with NV12 plane arrangement.

Common format for camera data with Y plane followed by interleaved UV plane.

### `YUV420NV21`<a href="#yuv420nv21" class="hash-link" aria-label="Direct link to yuv420nv21" title="Direct link to yuv420nv21">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case YUV420NV21
```

</div>

</div>

YUV 4:2:0 format with NV21 plane arrangement.

Similar to NV12 but with interleaved VU plane instead of UV.

### `YUV420888`<a href="#yuv420888" class="hash-link" aria-label="Direct link to yuv420888" title="Direct link to yuv420888">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case YUV420888
```

</div>

</div>

YUV 4:2:0 format with separate Y, U, V planes.

Each color component is stored in a separate plane.

### `oneComponent8`<a href="#onecomponent8" class="hash-link" aria-label="Direct link to onecomponent8" title="Direct link to onecomponent8">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case oneComponent8
```

</div>

</div>

Single 8-bit component per pixel.

Typically used for grayscale images or single-channel data.

### `depthUInt16`<a href="#depthuint16" class="hash-link" aria-label="Direct link to depthuint16" title="Direct link to depthuint16">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case depthUInt16
```

</div>

</div>

Depth data as 16-bit unsigned integers.

Common format for depth cameras, with depth values in millimeters.

### `depthFloat32`<a href="#depthfloat32" class="hash-link" aria-label="Direct link to depthfloat32" title="Direct link to depthfloat32">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case depthFloat32
```

</div>

</div>

Depth data as 32-bit floating point values.

High-precision depth format, typically with values in meters.

### `oneComponent32`<a href="#onecomponent32" class="hash-link" aria-label="Direct link to onecomponent32" title="Direct link to onecomponent32">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case oneComponent32
```

</div>

</div>

Single 32-bit component per pixel.

Used for high-precision single-channel data.

### `ARGB32`<a href="#argb32" class="hash-link" aria-label="Direct link to argb32" title="Direct link to argb32">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case ARGB32
```

</div>

</div>

32-bit ARGB color format.

8 bits each for alpha, red, green, and blue channels.

### `RGBA32`<a href="#rgba32" class="hash-link" aria-label="Direct link to rgba32" title="Direct link to rgba32">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case RGBA32
```

</div>

</div>

32-bit RGBA color format.

8 bits each for red, green, blue, and alpha channels.

### `BGRA32`<a href="#bgra32" class="hash-link" aria-label="Direct link to bgra32" title="Direct link to bgra32">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case BGRA32
```

</div>

</div>

32-bit BGRA color format.

8 bits each for blue, green, red, and alpha channels.

### `RGB24`<a href="#rgb24" class="hash-link" aria-label="Direct link to rgb24" title="Direct link to rgb24">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case RGB24
```

</div>

</div>

24-bit RGB color format.

8 bits each for red, green, and blue channels (no alpha).

</div>

</div>
