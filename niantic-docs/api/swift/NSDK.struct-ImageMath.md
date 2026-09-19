---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.struct-ImageMath/
title: ImageMath
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

#  ImageMath

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">struct</span><span class="ctoken plain"> </span><span class="ctoken class-name">ImageMath</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Provides affine transformation utilities for image processing. All affine matrices returned by this class operate in **normalized coordinates**, where image space is mapped to the \[0, 1\] range in both axes with origin at top-left.

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
<td><span id="method-affinecrop"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.ImageMath.method-affineCrop/" title="Returns an affine transformation that crops the source size to match the aspect ratio of the target size.">affineCrop</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGAffineTransform" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGAffineTransform</a></span></span></td>
<td><div class="ctoken comment">
Returns an affine transformation that crops the source size to match the aspect ratio of the target size.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-affinefit"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.ImageMath.method-affineFit/" title="Returns an affine transformation that maps normalized coordinates in the source frame to normalized coordinates in the target frame.">affineFit</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGAffineTransform" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGAffineTransform</a></span></span></td>
<td><div class="ctoken comment">
Returns an affine transformation that maps normalized coordinates in the source frame to normalized coordinates in the target frame.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-affineinverthorizontal"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.ImageMath.method-affineInvertHorizontal/" title="Returns an (u, v) -&gt; (u&#39;, v&#39;) transformation that represents a horizontal mirroring, i.e. (u, v) -&gt; (1 - u, v).">affineInvertHorizontal</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGAffineTransform" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGAffineTransform</a></span></span></td>
<td><div class="ctoken comment">
Returns an (u, v) -&gt; (u', v') transformation that represents a horizontal mirroring, i.e. (u, v) -&gt; (1 - u, v).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-affineinvertvertical"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.ImageMath.method-affineInvertVertical/" title="Returns an (u, v) -&gt; (u&#39;, v&#39;) transformation that represents a vertical mirroring, i.e. (u, v) -&gt; (u, 1 - v).">affineInvertVertical</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGAffineTransform" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGAffineTransform</a></span></span></td>
<td><div class="ctoken comment">
Returns an (u, v) -&gt; (u', v') transformation that represents a vertical mirroring, i.e. (u, v) -&gt; (u, 1 - v).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-affinerotation"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.ImageMath.method-affineRotation/" title="Returns an (u, v) -&gt; (u&#39;, v&#39;) transformation that represents a 2D affine rotation.">affineRotation</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGAffineTransform" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGAffineTransform</a></span></span></td>
<td><div class="ctoken comment">
Returns an (u, v) -&gt; (u', v') transformation that represents a 2D affine rotation.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-affinescaling"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.ImageMath.method-affineScaling/" title="Returns an (u, v) -&gt; (u&#39;, v&#39;) transformation that represents a 2D affine scaling.">affineScaling</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGAffineTransform" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGAffineTransform</a></span></span></td>
<td><div class="ctoken comment">
Returns an (u, v) -&gt; (u', v') transformation that represents a 2D affine scaling.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-affinetranslation"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.ImageMath.method-affineTranslation/" title="Returns an (u, v) -&gt; (u&#39;, v&#39;) transformation that represents a 2D affine translation.">affineTranslation</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGAffineTransform" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGAffineTransform</a></span></span></td>
<td><div class="ctoken comment">
Returns an (u, v) -&gt; (u', v') transformation that represents a 2D affine translation.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-devicerotation"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.ImageMath.method-deviceRotation/" title="Returns an affine transform that rotates between two interface orientations around the center....">deviceRotation</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGAffineTransform" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGAffineTransform</a></span></span></td>
<td><div class="ctoken comment">
Returns an affine transform that rotates between two interface orientations around the center.<br />
This method models physical device rotation.<br />
For example, rotating from <code>.landscapeRight</code> to <code>.portrait</code> results in a clockwise transform.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-displaytransform"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.ImageMath.method-displayTransform/" title="Returns an affine transform that maps normalized image coordinates...">displayTransform</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGAffineTransform" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGAffineTransform</a></span></span></td>
<td><div class="ctoken comment">
Returns an affine transform that maps normalized image coordinates<br />
into a coordinate space suitable for rendering the camera image<br />
in the given viewport and orientation.<br />
This method replicates ARKit’s <code>displayTransform(for:viewportSize:)</code><br />
by computing a transform that accounts for the camera image’s<br />
aspect ratio, the device’s interface orientation, and the desired<br />
viewport size.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-reprojection"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.ImageMath.method-reprojection/" title="Returns a 3×3 homography matrix as `matrix_float3x3` that reprojects...">reprojection</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/matrix_float3x3" target="_blank" rel="noopener noreferrer" title="Opens an external reference">matrix_float3x3</a></span></span></td>
<td><div class="ctoken comment">
Returns a 3×3 homography matrix as <code>matrix_float3x3</code> that reprojects<br />
image coordinates from a reference camera view into a target camera view.<br />
The image coordinates are expected to be normalized [0..1].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-viewrotation"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.ImageMath.method-viewRotation/" title="Returns an affine transform that rotates between two interface orientations around the center....">viewRotation</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//CoreFoundation/CGAffineTransform" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CGAffineTransform</a></span></span></td>
<td><div class="ctoken comment">
Returns an affine transform that rotates between two interface orientations around the center.<br />
This method models UI rotation (opposite to physical device rotation).<br />
For example, rotating from <code>.landscapeRight</code> to <code>.portrait</code> results in a counter-clockwise transform.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
