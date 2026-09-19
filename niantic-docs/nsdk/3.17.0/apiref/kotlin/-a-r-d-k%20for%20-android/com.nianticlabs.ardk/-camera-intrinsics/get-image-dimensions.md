---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/get-image-dimensions/
title: get-image-dimensions
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[CameraIntrinsics](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[getImageDimensions](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/get-image-dimensions/)

<div>

# getImageDimensions

</div>

\[androidJvm\]\
open fun [getImageDimensions](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/get-image-dimensions/)(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int-array/index.html" target="_blank" rel="noopener noreferrer">IntArray</a>

Returns a `int[2]` containing the image dimensions. The order of values is {width, height}.

\[androidJvm\]\
open fun [getImageDimensions](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/get-image-dimensions/)(dimensions: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int-array/index.html" target="_blank" rel="noopener noreferrer">IntArray</a>?, offset: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>)

Returns the camera's image dimensions. The order of values is {width, height}.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|  |  |
|----|----|
| dimensions | storage for at least 2 ints representing the image's width and height. |
| offset | the offset in `dimensions` at which to begin writing the image dimension's values. |

</div>

</div>
