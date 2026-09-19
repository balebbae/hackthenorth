---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/-image-math/display-transform/
title: display-transform
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.utils](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/)/[ImageMath](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[displayTransform](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/-image-math/display-transform/)

<div>

# displayTransform

</div>

\[androidJvm\]\
fun [displayTransform](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/-image-math/display-transform/)(orientation: [Orientation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/), viewportSize: <a href="https://developer.android.com/reference/kotlin/android/util/Size.html" target="_blank" rel="noopener noreferrer">Size</a>, imageSize: <a href="https://developer.android.com/reference/kotlin/android/util/Size.html" target="_blank" rel="noopener noreferrer">Size</a>): <a href="https://developer.android.com/reference/kotlin/android/graphics/Matrix.html" target="_blank" rel="noopener noreferrer">Matrix</a>

Returns an affine transform <a href="https://developer.android.com/reference/kotlin/android/graphics/Matrix.html" target="_blank" rel="noopener noreferrer">Matrix</a> that maps normalized image coordinates into a coordinate space suitable for rendering the camera image in the given viewport and orientation.

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

A <a href="https://developer.android.com/reference/kotlin/android/graphics/Matrix.html" target="_blank" rel="noopener noreferrer">Matrix</a> that converts normalized image coordinates (origin top-left, range 0.0–1.0) into the coordinate space of the viewport.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|  |  |
|----|----|
| orientation | The current interface orientation of the device’s UI. |
| viewportSize | The size of the viewport in which the image will be rendered, in pixels. |
| imageSize | The dimensions of the camera image, in pixels. |

</div>

</div>
