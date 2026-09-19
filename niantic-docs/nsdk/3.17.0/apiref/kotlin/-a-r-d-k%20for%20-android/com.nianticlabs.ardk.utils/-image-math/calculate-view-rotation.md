---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/-image-math/calculate-view-rotation/
title: calculate-view-rotation
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.utils](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/)/[ImageMath](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[calculateViewRotation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/-image-math/calculate-view-rotation/)

<div>

# calculateViewRotation

</div>

\[androidJvm\]\
fun [calculateViewRotation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.utils/-image-math/calculate-view-rotation/)(fromOrientation: [Orientation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/), toOrientation: [Orientation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-orientation/)): <a href="https://developer.android.com/reference/kotlin/android/graphics/Matrix.html" target="_blank" rel="noopener noreferrer">Matrix</a>

Returns an affine transform that rotates between two interface orientations around the center.

This method models UI rotation (opposite to physical device rotation).

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

An affine <a href="https://developer.android.com/reference/kotlin/android/graphics/Matrix.html" target="_blank" rel="noopener noreferrer">Matrix</a> that rotates from the `fromOrientation` into the `toOrientation`.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|                 |                       |
|-----------------|-----------------------|
| fromOrientation | Starting orientation. |
| toOrientation   | Target orientation.   |

</div>

</div>
