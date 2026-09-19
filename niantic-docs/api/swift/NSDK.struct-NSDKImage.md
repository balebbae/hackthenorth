---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKImage/
title: NSDKImage
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

#  NSDKImage

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">struct</span><span class="ctoken plain"> </span><span class="ctoken class-name">NSDKImage</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Provides a view into the data buffer of an image output by the NSDK. `NSDKImage` provides access to image data in various formats (RGB, grayscale, depth, etc.) used by NSDK features like depth processing, semantic segmentation, and image analysis.

## Memory Management<a href="#memory-management" class="hash-link" aria-label="Direct link to Memory Management" title="Direct link to Memory Management">​</a>

The image provides a non-copying view into native image data managed by NSDK. Access to the pixel buffer is only valid for the duration of `withUnsafeBytes(_:)`. The raw pointer passed to the closure must not be stored or used outside its scope.

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
<td><span id="property-height"></span><span class="ctoken-line"><span class="ctoken keyword">let</span><span class="ctoken plain"> </span><span class="ctoken class-name">height</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/uint" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UInt</a></span></span></td>
<td><div class="ctoken comment">
Height of the image in pixels.<br />
This represents the number of rows in the image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-type"></span><span class="ctoken-line"><span class="ctoken keyword">let</span><span class="ctoken plain"> </span><span class="ctoken class-name">type</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKImage.enum-ImageType/" title="Enum representing various image types supported by NSDK.">ImageType</a></span></span></td>
<td><div class="ctoken comment">
Format and type of the image data.<br />
This indicates how the pixel data should be interpreted, including<br />
the number of channels, data type, and color space.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-width"></span><span class="ctoken-line"><span class="ctoken keyword">let</span><span class="ctoken plain"> </span><span class="ctoken class-name">width</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/uint" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UInt</a></span></span></td>
<td><div class="ctoken comment">
Width of the image in pixels.<br />
This represents the number of pixels in each row of the image.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

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
<td><span id="method-withunsafebytes"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKImage.method-withUnsafeBytes/" title="Provides temporary, read-only access to the raw pixel buffer backing the image.">withUnsafeBytes</a></span><span class="ctoken plain">&lt;</span><span class="ctoken plain">R</span><span class="ctoken plain">&gt;(</span><span class="ctoken plain">_</span><span class="ctoken plain"> </span><span class="ctoken plain">body</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">R</span></span></td>
<td><div class="ctoken comment">
Provides temporary, read-only access to the raw pixel buffer backing the image.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Nested Types<a href="#nested-types" class="hash-link" aria-label="Direct link to Nested Types" title="Direct link to Nested Types">​</a>

### Enums<a href="#enums" class="hash-link" aria-label="Direct link to Enums" title="Direct link to Enums">​</a>

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
<td><span id="enum-imagetype"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKImage.enum-ImageType/" title="Enum representing various image types supported by NSDK.">ImageType</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKImage.enum-ImageType/" title="Enum representing various image types supported by NSDK.">ImageType</a></span></span></td>
<td><div class="ctoken comment">
Enum representing various image types supported by NSDK.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
