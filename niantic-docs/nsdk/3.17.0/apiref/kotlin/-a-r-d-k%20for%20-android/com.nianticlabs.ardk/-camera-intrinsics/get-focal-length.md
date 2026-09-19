---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/get-focal-length/
title: get-focal-length
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[CameraIntrinsics](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[getFocalLength](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/get-focal-length/)

<div>

# getFocalLength

</div>

\[androidJvm\]\
open fun [getFocalLength](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/get-focal-length/)(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float-array/index.html" target="_blank" rel="noopener noreferrer">FloatArray</a>

Returns the camera's focal length in pixels.

The focal length is conventionally represented in pixels. For a detailed explanation, please see <a href="https://ksimek.github.io/2013/08/13/intrinsic" target="_blank" rel="noopener noreferrer">Disecting the Camera Matrix, Part 3: The Intrinsic Matrix</a>. Pixels-to-meters conversion can use `SENSOR_INFO_PHYSICAL_SIZE` and `SENSOR_INFO_PIXEL_ARRAY_SIZE` in the Android Characteristics API.

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

a `float[2]` containing the focal length. The order of values is {fx, fy}.

\[androidJvm\]\
open fun [getFocalLength](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/get-focal-length/)(focalLength: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float-array/index.html" target="_blank" rel="noopener noreferrer">FloatArray</a>?, offset: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>)

Returns the camera's focal length in pixels.

The focal length is conventionally represented in pixels. For a detailed explanation, please see <a href="https://ksimek.github.io/2013/08/13/intrinsic" target="_blank" rel="noopener noreferrer">Disecting the Camera Matrix, Part 3: The Intrinsic Matrix</a>. Pixels-to-meters conversion can use `SENSOR_INFO_PHYSICAL_SIZE` and `SENSOR_INFO_PIXEL_ARRAY_SIZE` in the Android Characteristics API.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|  |  |
|----|----|
| focalLength | storage for at least 2 floats representing the focal length. The order of values is {fx, fy}. |
| offset | the offset in `focalLength` at which to begin writing the focal length values. |

</div>

</div>
