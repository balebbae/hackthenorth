---
source: https://www.nianticspatial.com/docs/api/swift/toYUV420PixelBuffer/
title: toYUV420PixelBuffer
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") 

</div>

<div class="api-title">

#  toYUV420PixelBuffer

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">toYUV420PixelBuffer</span><span class="ctoken plain">(</span><span class="ctoken plain">width</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span><span class="ctoken plain">, </span><span class="ctoken plain">height</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span><span class="ctoken plain">) -\> </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreVideo/CVPixelBuffer" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CVPixelBuffer</a></span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Converts the CGImage to a CVPixelBuffer in YUV420NV12 (bi-planar) format for use as a camera feed.\
Uses Core Image to perform the color conversion. Returns nil if buffer creation or render fails.

</div>

### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

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
<td><span id="external parameter-width"></span><span class="ctoken-line"><span class="ctoken class-name">width</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
Target width for the pixel buffer (typically the image width).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-height"></span><span class="ctoken-line"><span class="ctoken class-name">height</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
Target height for the pixel buffer (typically the image height).
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
