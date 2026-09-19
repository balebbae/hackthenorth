---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/extensions/simd_float4x4/
title: simd_float4x4
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**EXTENSION**

<div>

# `simd_float4x4`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public extension simd_float4x4
```

</div>

</div>

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(fromArdkTransform:)`<a href="#initfromardktransform" class="hash-link" aria-label="Direct link to initfromardktransform" title="Direct link to initfromardktransform">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
init(fromArdkTransform t: ARDK_Transform)
```

</div>

</div>

### `init(fromColumnMajorArray:)`<a href="#initfromcolumnmajorarray" class="hash-link" aria-label="Direct link to initfromcolumnmajorarray" title="Direct link to initfromcolumnmajorarray">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
init(fromColumnMajorArray array: UnsafePointer\<Float\>)
```

</div>

</div>

Initialize from a 4x4 column-major float array.

- Parameter array: Pointer to 16 floats in column-major order.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name  | Description                                 |
|-------|---------------------------------------------|
| array | Pointer to 16 floats in column-major order. |

### `init(fromColumnMajorTuple:)`<a href="#initfromcolumnmajortuple" class="hash-link" aria-label="Direct link to initfromcolumnmajortuple" title="Direct link to initfromcolumnmajortuple">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
init(fromColumnMajorTuple tuple: (
    Float, Float, Float, Float,
    Float, Float, Float, Float,
    Float, Float, Float, Float,
    Float, Float, Float, Float))
```

</div>

</div>

Initialize from a 4x4 column-major float tuple.

- Parameter tuple: 16 floats in column-major order.

#### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name  | Description                      |
|-------|----------------------------------|
| tuple | 16 floats in column-major order. |

### `fromARKitToArdk()`<a href="#fromarkittoardk" class="hash-link" aria-label="Direct link to fromarkittoardk" title="Direct link to fromarkittoardk">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
func fromARKitToArdk() -> simd_float4x4
```

</div>

</div>

Convert from ARKit coordinates to ARDK coordinates.

The conversion from ARKit to ARDK space is a 180º rotation about the x-axis

### `fromArdkToARKit()`<a href="#fromardktoarkit" class="hash-link" aria-label="Direct link to fromardktoarkit" title="Direct link to fromardktoarkit">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
func fromArdkToARKit() -> simd_float4x4
```

</div>

</div>

Convert from ARDK coordinates to ARKit coordinates.

The conversion from ARDK to ARKit is a 180º rotation about the x-axis

### `fromARKitToArdkTransform()`<a href="#fromarkittoardktransform" class="hash-link" aria-label="Direct link to fromarkittoardktransform" title="Direct link to fromarkittoardktransform">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
func fromARKitToArdkTransform() -> ARDK_Transform
```

</div>

</div>

Convert this transform to an ARDK_Transform structure.

### `flatten()`<a href="#flatten" class="hash-link" aria-label="Direct link to flatten" title="Direct link to flatten">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
func flatten() -> [Float]
```

</div>

</div>

Flattens the matrix into a column-major array of 16 floats.

</div>

</div>
