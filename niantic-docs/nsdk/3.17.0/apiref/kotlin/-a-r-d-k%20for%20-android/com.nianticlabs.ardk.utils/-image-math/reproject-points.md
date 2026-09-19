---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/-image-math/reproject-points/
title: reproject-points
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.utils](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/)/[ImageMath](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[reprojectPoints](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/-image-math/reproject-points/)

<div>

# reprojectPoints

</div>

\[androidJvm\]\
fun <a href="https://developer.android.com/reference/kotlin/android/graphics/Matrix.html" target="_blank" rel="noopener noreferrer">Matrix</a>.[reprojectPoints](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/-image-math/reproject-points/)(pts: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float-array/index.html" target="_blank" rel="noopener noreferrer">FloatArray</a>)

Applies a full 3×3 projective transformation (homography) to a set of 2D points, using this <a href="https://developer.android.com/reference/kotlin/android/graphics/Matrix.html" target="_blank" rel="noopener noreferrer">Matrix</a> as a homography matrix.

Unlike <a href="https://developer.android.com/reference/kotlin/android/graphics/Matrix.html#mappoints" target="_blank" rel="noopener noreferrer">Matrix.mapPoints</a>, this method correctly applies the bottom row of the matrix and performs the required perspective divide.

Transformed points are clamped to the -1f..2f range to ensure compatibility with UI constraints.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|  |  |
|----|----|
| pts | Array of x0, y0, x1, y1, ..., xn, yn. This array will be modified in-place. |

</div>

</div>
