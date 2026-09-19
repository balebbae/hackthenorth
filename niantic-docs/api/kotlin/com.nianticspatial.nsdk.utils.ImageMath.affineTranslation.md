---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.utils.ImageMath.affineTranslation/
title: affineTranslation
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

#  affineTranslation

<div class="api-package">

Returns an (u, v) -\> (u', v') transformation that represents a 2D affine translation.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">affineTranslation</span><span class="ctoken punctuation">(</span><span class="ctoken plain">tx</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">ty</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Matrix" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix</a></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns an (u, v) -\> (u', v') transformation that represents a 2D affine translation.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

An affine `Matrix` that shifts coordinates by `(tx, ty)`.

</div>

------------------------------------------------------------------------

</div>

</div>
