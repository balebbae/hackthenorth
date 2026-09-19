---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics-from-a-r-core/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/)/[CameraIntrinsicsFromARCore](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# CameraIntrinsicsFromARCore

</div>

\[androidJvm\]\
class [CameraIntrinsicsFromARCore](https://www.nianticspatial.com/docs/nsdk/3.17.0/)(arcoreIntrinsics: CameraIntrinsics) : [CameraIntrinsics](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/)

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>CameraIntrinsicsFromARCore</td>
<td>[androidJvm]<br />
constructor(arcoreIntrinsics: CameraIntrinsics)</td>
</tr>
</tbody>
</table>

## Functions<a href="#functions" class="hash-link" aria-label="Direct link to Functions" title="Direct link to Functions">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Name</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/get-focal-length/">getFocalLength</a></td>
<td>[androidJvm]<br />
open fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/get-focal-length/">getFocalLength</a>(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float-array/index.html" target="_blank" rel="noopener noreferrer">FloatArray</a><br />
open fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/get-focal-length/">getFocalLength</a>(focalLength: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float-array/index.html" target="_blank" rel="noopener noreferrer">FloatArray</a>?, offset: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>)<br />
Returns the camera's focal length in pixels.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/get-image-dimensions/">getImageDimensions</a></td>
<td>[androidJvm]<br />
open fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/get-image-dimensions/">getImageDimensions</a>(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int-array/index.html" target="_blank" rel="noopener noreferrer">IntArray</a><br />
Returns a <code>int[2]</code> containing the image dimensions. The order of values is {width, height}.<br />
[androidJvm]<br />
open fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/get-image-dimensions/">getImageDimensions</a>(dimensions: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int-array/index.html" target="_blank" rel="noopener noreferrer">IntArray</a>?, offset: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>)<br />
Returns the camera's image dimensions. The order of values is {width, height}.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/get-principal-point/">getPrincipalPoint</a></td>
<td>[androidJvm]<br />
open fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/get-principal-point/">getPrincipalPoint</a>(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float-array/index.html" target="_blank" rel="noopener noreferrer">FloatArray</a><br />
Returns a <code>float[2]</code> containing the principal point. The order of values is {cx, cy}.<br />
[androidJvm]<br />
open fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/get-principal-point/">getPrincipalPoint</a>(principalPoint: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float-array/index.html" target="_blank" rel="noopener noreferrer">FloatArray</a>?, offset: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>)<br />
Returns the camera's principal point. The order of values is {cx, cy}.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/to-float-array/">toFloatArray</a></td>
<td>[androidJvm]<br />
open fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-camera-intrinsics/to-float-array/">toFloatArray</a>(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-array/index.html" target="_blank" rel="noopener noreferrer">Array</a>&lt;<a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float-array/index.html" target="_blank" rel="noopener noreferrer">FloatArray</a>&gt;<br />
Returns a <code>float[3][3]</code> representing the camera's intrinsic matrix.</td>
</tr>
</tbody>
</table>

</div>

</div>
