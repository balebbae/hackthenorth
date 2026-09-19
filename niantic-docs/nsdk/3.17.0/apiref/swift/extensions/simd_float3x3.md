---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/extensions/simd_float3x3/
title: simd_float3x3
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**EXTENSION**

<div>

# `simd_float3x3`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public extension simd_float3x3
```

</div>

</div>

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(fromCGAffineTransform:)`<a href="#initfromcgaffinetransform" class="hash-link" aria-label="Direct link to initfromcgaffinetransform" title="Direct link to initfromcgaffinetransform">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
init(fromCGAffineTransform transform: CGAffineTransform)
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

Initialize from a 3×3 column-major float array.

- Parameter array: Pointer to 9 floats in column-major order.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name  | Description                                |
|-------|--------------------------------------------|
| array | Pointer to 9 floats in column-major order. |

### `init(fromColumnMajorTuple:)`<a href="#initfromcolumnmajortuple" class="hash-link" aria-label="Direct link to initfromcolumnmajortuple" title="Direct link to initfromcolumnmajortuple">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
init(fromColumnMajorTuple tuple: (
    Float, Float, Float,
    Float, Float, Float,
    Float, Float, Float))
```

</div>

</div>

</div>

</div>
