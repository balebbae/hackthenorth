---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.ImageMath.method-displayTransform/
title: displayTransform
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[ImageMath](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-ImageMath/ "ImageMath") 

</div>

<div class="api-title">

#  displayTransform

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">displayTransform</span><span class="ctoken plain">(</span><span class="ctoken plain">for</span><span class="ctoken plain"> </span><span class="ctoken plain">orientation</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//uikit/UIInterfaceOrientation" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UIInterfaceOrientation</a></span><span class="ctoken plain">, </span><span class="ctoken plain">viewportSize</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGSize" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGSize</a></span><span class="ctoken plain">, </span><span class="ctoken plain">imageSize</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGSize" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGSize</a></span><span class="ctoken plain">) -\> </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGAffineTransform" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGAffineTransform</a></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns an affine transform that maps normalized image coordinates\
into a coordinate space suitable for rendering the camera image\
in the given viewport and orientation.\
This method replicates ARKit’s `displayTransform(for:viewportSize:)`\
by computing a transform that accounts for the camera image’s\
aspect ratio, the device’s interface orientation, and the desired\
viewport size.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A `CGAffineTransform` that converts normalized image coordinates\
(with origin at top-left, ranging from 0.0 to 1.0) into the coordinate\
space of the viewport, accounting for orientation and aspect ratio.

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
<td><span id="external parameter-for"></span><span class="ctoken-line"><span class="ctoken class-name">orientation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//uikit/UIInterfaceOrientation" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UIInterfaceOrientation</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-viewportsize"></span><span class="ctoken-line"><span class="ctoken class-name">viewportSize</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGSize" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGSize</a></span></span></td>
<td><div class="ctoken comment">
The size of the viewport in which the image will be rendered.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-imagesize"></span><span class="ctoken-line"><span class="ctoken class-name">imageSize</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGSize" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGSize</a></span></span></td>
<td><div class="ctoken comment">
The dimensions of the camera image.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
