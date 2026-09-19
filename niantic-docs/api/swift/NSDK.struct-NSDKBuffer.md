---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKBuffer/
title: NSDKBuffer
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") 

</div>

<div class="api-title">

#  NSDKBuffer

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">struct</span><span class="ctoken plain"> </span><span class="ctoken class-name">NSDKBuffer</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

A buffer containing binary data for NSDK operations. `NSDKBuffer` provides a safe wrapper around binary data buffers used by various NSDK features. It handles memory management and provides convenient access to buffer data.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

NSDK buffers are used for:

- Image data transfer
- Mesh data storage
- Configuration data
- Any binary data that needs to be passed between Swift and the native NSDK layer

## Example Usage<a href="#example-usage" class="hash-link" aria-label="Direct link to Example Usage" title="Direct link to Example Usage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
// Create buffer from Swift Data
let imageData = UIImage(named: "texture")?.pngData()
let buffer = NSDKBuffer(data: imageData!)
// Access buffer data
print("Buffer size: \(buffer.dataSize) bytes")
// Use buffer with NSDK APIs
let status = someArdkFunction(buffer: buffer)
```

</div>

</div>

## Memory Management<a href="#memory-management" class="hash-link" aria-label="Direct link to Memory Management" title="Direct link to Memory Management">​</a>

`NSDKBuffer` automatically manages memory allocation and deallocation. When created from Swift `Data`, it maintains a reference to prevent premature deallocation.

------------------------------------------------------------------------

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

### Constructor<a href="#constructor" class="hash-link" aria-label="Direct link to Constructor" title="Direct link to Constructor">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">init</span><span class="ctoken plain">(</span><span class="ctoken plain">data</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//foundation/data" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Data</a></span><span class="ctoken plain">)</span></span>

</div>

------------------------------------------------------------------------

### Overload<a href="#overload" class="hash-link" aria-label="Direct link to Overload" title="Direct link to Overload">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">init</span><span class="ctoken plain">(</span><span class="ctoken plain">data</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/unsafepointer" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UnsafePointer</a></span><span class="ctoken plain">\<</span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/uint8" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UInt8</a></span><span class="ctoken plain">\>, </span><span class="ctoken plain">dataSize</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/uint32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UInt32</a></span><span class="ctoken plain">)</span></span>

</div>

------------------------------------------------------------------------

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

<table class="api-table">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr class="api-table-row">
<td><span id="property-data"></span><span class="ctoken-line"><span class="ctoken keyword">let</span><span class="ctoken plain"> </span><span class="ctoken class-name">data</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/unsafepointer" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UnsafePointer</a></span><span class="ctoken plain">&lt;</span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/uint8" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UInt8</a></span><span class="ctoken plain">&gt;</span></span></td>
<td><div class="ctoken comment">
Pointer to the buffer's binary data.<br />
This provides direct access to the buffer's contents. The data remains<br />
valid as long as the <code>NSDKBuffer</code> instance exists.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-datasize"></span><span class="ctoken-line"><span class="ctoken keyword">let</span><span class="ctoken plain"> </span><span class="ctoken class-name">dataSize</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/uint32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UInt32</a></span></span></td>
<td><div class="ctoken comment">
Size of the buffer data in bytes.<br />
This indicates the total number of bytes available in the buffer.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-owner"></span><span class="ctoken-line"><span class="ctoken keyword">let</span><span class="ctoken plain"> </span><span class="ctoken class-name">owner</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.interface-ResourceOwner/" title="Browse to ResourceOwner">ResourceOwner</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Resource owner for memory management.<br />
This ensures the buffer's memory is properly managed and deallocated<br />
when the buffer is no longer needed.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
