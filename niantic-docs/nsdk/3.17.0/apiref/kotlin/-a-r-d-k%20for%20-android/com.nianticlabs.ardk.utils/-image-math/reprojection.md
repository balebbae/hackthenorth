---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/-image-math/reprojection/
title: reprojection
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.utils](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/)/[ImageMath](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[reprojection](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/-image-math/reprojection/)

<div>

# reprojection

</div>

\[androidJvm\]\
fun [reprojection](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/-image-math/reprojection/)(aspect: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a>, fovRadians: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a>, zNear: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a>, zFar: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a>, referenceView: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float-array/index.html" target="_blank" rel="noopener noreferrer">FloatArray</a>, targetView: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float-array/index.html" target="_blank" rel="noopener noreferrer">FloatArray</a>, backProjectionDistance: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a> = 0.9f): <a href="https://developer.android.com/reference/kotlin/android/graphics/Matrix.html" target="_blank" rel="noopener noreferrer">Matrix</a>

Returns a 3×3 homography matrix (`android.graphics.Matrix`) that reprojects image coordinates from a reference camera view into a target camera view.

This is typically used to transform 2D image-space coordinates (normalized in 0..1) from one camera perspective to another, e.g. for aligning visual overlays between AR frames.

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

A 3×3 homography matrix represented as an `android.graphics.Matrix`.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|  |  |
|----|----|
| aspect | The image aspect ratio (width / height). |
| fovRadians | The vertical field of view in radians. |
| zNear | The near clipping plane distance. |
| zFar | The far clipping plane distance. |
| referenceView | The reference camera's 4×4 view matrix as a `FloatArray` (length 16), in **OpenGL-style column-major** order. This can typically be acquired from ARCore using `camera.getViewMatrix(viewMatrix, 0)`. |
| targetView | The target camera's 4×4 view matrix, same format and origin as `referenceView`. |
| backProjectionDistance | Non-linear depth at which to reproject (between `zNear` and `zFar`). A value of 0.0 corresponds to the near plane, 1.0 to the far plane. Recommended value: `0.9`. |

</div>

</div>
