---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath/
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

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.utils](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils/ "com.nianticspatial.nsdk.utils") 

</div>

<div class="api-title">

#  ImageMath

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">object</span><span class="ctoken plain"> </span><span class="ctoken class-name">ImageMath</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Kotlin wrapper for ARDK ImageMath functions. Each function returns an \[android.graphics.Matrix\] corresponding to a 3×3 affine or projective transformation.

------------------------------------------------------------------------

## Functions<a href="#functions" class="hash-link" aria-label="Direct link to Functions" title="Direct link to Functions">​</a>

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
<td><span id="function-affinecrop"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath.affineCrop/" title="Returns an affine transformation that crops the source size...">affineCrop</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Matrix" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix</a></span></span></td>
<td><div class="ctoken comment">
Returns an affine transformation that crops the source size<br />
to match the aspect ratio of the target size.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-affinefit"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath.affineFit/" title="Returns an affine transformation that maps normalized coordinates...">affineFit</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Matrix" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix</a></span></span></td>
<td><div class="ctoken comment">
Returns an affine transformation that maps normalized coordinates<br />
in the source frame to normalized coordinates in the target frame.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-affineinverthorizontal"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath.affineInvertHorizontal/" title="Returns an affine matrix for horizontal mirroring....">affineInvertHorizontal</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Matrix" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix</a></span></span></td>
<td><div class="ctoken comment">
Returns an affine matrix for horizontal mirroring.<br />
Maps <code>(u, v)</code> → <code>(1 - u, v)</code>.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-affineinvertvertical"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath.affineInvertVertical/" title="Returns an affine matrix for vertical mirroring....">affineInvertVertical</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Matrix" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix</a></span></span></td>
<td><div class="ctoken comment">
Returns an affine matrix for vertical mirroring.<br />
Maps <code>(u, v)</code> → <code>(u, 1 - v)</code>.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-affinerotation"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath.affineRotation/" title="Returns an (u, v) -&gt; (u&#39;, v&#39;) transformation that represents a 2D affine rotation.">affineRotation</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Matrix" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix</a></span></span></td>
<td><div class="ctoken comment">
Returns an (u, v) -&gt; (u', v') transformation that represents a 2D affine rotation.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-affinescaling"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath.affineScaling/" title="Returns an (u, v) -&gt; (u&#39;, v&#39;) transformation that represents a 2D affine scaling.">affineScaling</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Matrix" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix</a></span></span></td>
<td><div class="ctoken comment">
Returns an (u, v) -&gt; (u', v') transformation that represents a 2D affine scaling.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-affinetranslation"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath.affineTranslation/" title="Returns an (u, v) -&gt; (u&#39;, v&#39;) transformation that represents a 2D affine translation.">affineTranslation</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Matrix" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix</a></span></span></td>
<td><div class="ctoken comment">
Returns an (u, v) -&gt; (u', v') transformation that represents a 2D affine translation.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-calculatedevicerotation"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath.calculateDeviceRotation/" title="Returns an affine transform that rotates between two interface orientations around the center....">calculateDeviceRotation</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Matrix" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix</a></span></span></td>
<td><div class="ctoken comment">
Returns an affine transform that rotates between two interface orientations around the center.<br />
This method models physical device rotation.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-calculateviewrotation"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath.calculateViewRotation/" title="Returns an affine transform that rotates between two interface orientations around the center....">calculateViewRotation</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Matrix" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix</a></span></span></td>
<td><div class="ctoken comment">
Returns an affine transform that rotates between two interface orientations around the center.<br />
This method models UI rotation (opposite to physical device rotation).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-concatenating"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath.concatenating/" title="Returns a new [Matrix] representing the concatenation of this matrix...">concatenating</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Matrix" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix</a></span></span></td>
<td><div class="ctoken comment">
Returns a new [Matrix] representing the concatenation of this matrix<br />
with another matrix, mimicking the behavior of CoreGraphics’<br />
<code>concatenating(_:)</code> method on iOS.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-displaytransform"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath.displayTransform/" title="Returns an affine transform [Matrix] that maps normalized image coordinates...">displayTransform</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Matrix" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix</a></span></span></td>
<td><div class="ctoken comment">
Returns an affine transform [Matrix] that maps normalized image coordinates<br />
into a coordinate space suitable for rendering the camera image in the<br />
given viewport and orientation.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-logaffine"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath.logAffine/" title="Logs the affine components of this [Matrix] in a readable format....">logAffine</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Logs the affine components of this [Matrix] in a readable format.<br />
Prints the matrix in iOS-style notation:<br />
a, b, c, d, tx, ty<br />
corresponding to the 2×3 affine transform:<br />
[ a c tx ]<br />
[ b d ty ]
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-logmatrix"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath.logMatrix/" title="Logs the contents of this [Matrix] as a 3×3 matrix....">logMatrix</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Logs the contents of this [Matrix] as a 3×3 matrix.<br />
The matrix values are printed in row-major order, as used internally by [android.graphics.Matrix].<br />
Useful for debugging transformations like scale, rotation, skew, and perspective.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-reprojection"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath.reprojection/" title="Returns a 3×3 homography matrix (`android.graphics.Matrix`) that reprojects image coordinates...">reprojection</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Matrix" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix</a></span></span></td>
<td><div class="ctoken comment">
Returns a 3×3 homography matrix (<code>android.graphics.Matrix</code>) that reprojects image coordinates<br />
from a reference camera view into a target camera view.<br />
This is typically used to transform 2D image-space coordinates (normalized in [0..1])<br />
from one camera perspective to another, e.g. for aligning visual overlays between AR frames.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-reprojectpoints"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath.reprojectPoints/" title="Applies a full 3×3 projective transformation (homography) to a set of 2D points,...">reprojectPoints</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Applies a full 3×3 projective transformation (homography) to a set of 2D points,<br />
using this [Matrix] as a homography matrix.<br />
Unlike [Matrix.mapPoints], this method correctly applies the bottom row of the matrix<br />
and performs the required perspective divide.<br />
Transformed points are clamped to the [-1f..2f] range to ensure compatibility with<br />
UI constraints.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
