---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath.displayTransform/
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

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.utils](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils/ "com.nianticspatial.nsdk.utils") <span class="api-breadcrumbs-nav">←</span>[ImageMath](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath/ "com.nianticspatial.nsdk.utils.ImageMath") 

</div>

<div class="api-title">

#  displayTransform

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">displayTransform</span><span class="ctoken punctuation">(</span><span class="ctoken plain"> </span><span class="ctoken plain">orientation</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[Orientation](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Orientation/ "Device orientation when capturing camera frames....")</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">viewportSize</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/util/Size" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Size</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">imageSize</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/util/Size" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Size</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">imageOrientationOverride</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[Orientation](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Orientation/ "Device orientation when capturing camera frames....")</span><span class="ctoken plain">?</span><span class="ctoken plain"> </span><span class="ctoken plain">=</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">null</span><span class="ctoken plain"> </span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Matrix" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix</a></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns an affine transform `Matrix` that maps normalized image coordinates\
into a coordinate space suitable for rendering the camera image in the\
given viewport and orientation.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A `Matrix` that converts normalized image coordinates (origin top-left, range 0.0–1.0) into the coordinate space of the viewport.

</div>

------------------------------------------------------------------------

</div>

</div>
