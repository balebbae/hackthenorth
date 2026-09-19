---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/-image-math/affine-fit/
title: affine-fit
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.utils](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/)/[ImageMath](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[affineFit](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/-image-math/affine-fit/)

<div>

# affineFit

</div>

\[androidJvm\]\
fun [affineFit](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/-image-math/affine-fit/)(source: <a href="https://developer.android.com/reference/kotlin/android/util/Size.html" target="_blank" rel="noopener noreferrer">Size</a>, srcOrientation: [Orientation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/), target: <a href="https://developer.android.com/reference/kotlin/android/util/Size.html" target="_blank" rel="noopener noreferrer">Size</a>, tgtOrientation: [Orientation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/)): <a href="https://developer.android.com/reference/kotlin/android/graphics/Matrix.html" target="_blank" rel="noopener noreferrer">Matrix</a>

Returns an affine transformation that maps normalized coordinates in the source frame to normalized coordinates in the target frame.

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

An affine transformation matrix that fits the source into the target.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|                |                                             |
|----------------|---------------------------------------------|
| source         | The size of the source container in pixels. |
| srcOrientation | The orientation of the source container.    |
| target         | The size of the target container in pixels. |
| tgtOrientation | The orientation of the target container.    |

</div>

</div>
