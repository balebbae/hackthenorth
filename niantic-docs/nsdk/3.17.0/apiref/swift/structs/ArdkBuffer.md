---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/ArdkBuffer/
title: ArdkBuffer
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `ArdkBuffer`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct ArdkBuffer
```

</div>

</div>

A buffer containing binary data for ARDK operations.

`ArdkBuffer` provides a safe wrapper around binary data buffers used by various ARDK features. It handles memory management and provides convenient access to buffer data.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

ARDK buffers are used for:

- Image data transfer
- Mesh data storage
- Configuration data
- Any binary data that needs to be passed between Swift and the native ARDK layer

## Example Usage<a href="#example-usage" class="hash-link" aria-label="Direct link to Example Usage" title="Direct link to Example Usage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
// Create buffer from Swift Data
let imageData = UIImage(named: "texture")?.pngData()
let buffer = ArdkBuffer(data: imageData!)

// Access buffer data
print("Buffer size: \(buffer.dataSize) bytes")

// Use buffer with ARDK APIs
let status = someArdkFunction(buffer: buffer)
```

</div>

</div>

## Memory Management<a href="#memory-management" class="hash-link" aria-label="Direct link to Memory Management" title="Direct link to Memory Management">​</a>

`ArdkBuffer` automatically manages memory allocation and deallocation. When created from Swift `Data`, it maintains a reference to prevent premature deallocation.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `data`<a href="#data" class="hash-link" aria-label="Direct link to data" title="Direct link to data">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let data: UnsafePointer\<UInt8\>
```

</div>

</div>

Pointer to the buffer's binary data.

This provides direct access to the buffer's contents. The data remains valid as long as the `ArdkBuffer` instance exists.

### `dataSize`<a href="#datasize" class="hash-link" aria-label="Direct link to datasize" title="Direct link to datasize">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let dataSize: UInt32
```

</div>

</div>

Size of the buffer data in bytes.

This indicates the total number of bytes available in the buffer.

### `owner`<a href="#owner" class="hash-link" aria-label="Direct link to owner" title="Direct link to owner">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let owner: ResourceOwner?
```

</div>

</div>

Resource owner for memory management.

This ensures the buffer's memory is properly managed and deallocated when the buffer is no longer needed.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(data:dataSize:)`<a href="#initdatadatasize" class="hash-link" aria-label="Direct link to initdatadatasize" title="Direct link to initdatadatasize">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(data: UnsafePointer\<UInt8\>, dataSize: UInt32)
```

</div>

</div>

### `init(data:)`<a href="#initdata" class="hash-link" aria-label="Direct link to initdata" title="Direct link to initdata">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(data: Data)
```

</div>

</div>

</div>

</div>
