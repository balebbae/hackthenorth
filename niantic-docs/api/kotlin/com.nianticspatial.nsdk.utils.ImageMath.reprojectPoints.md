---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath.reprojectPoints/
title: reprojectPoints
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

#  reprojectPoints

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Matrix" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix</a></span><span class="ctoken punctuation">.</span><span class="ctoken class-name">reprojectPoints</span><span class="ctoken punctuation">(</span><span class="ctoken plain">pts</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">FloatArray</a></span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Applies a full 3×3 projective transformation (homography) to a set of 2D points,\
using this `Matrix` as a homography matrix.

\

Unlike `Matrix.mapPoints`, this method correctly applies the bottom row of the matrix\
and performs the required perspective divide.

\

Transformed points are clamped to the \[-1f..2f\] range to ensure compatibility with\
UI constraints.

</div>

------------------------------------------------------------------------

</div>

</div>
