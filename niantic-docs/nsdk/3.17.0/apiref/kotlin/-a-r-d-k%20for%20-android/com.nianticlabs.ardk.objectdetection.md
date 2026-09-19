---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/
title: index
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.objectdetection](https://www.nianticspatial.com/docs/nsdk/3.17.0/)

<div>

# Package-level declarations

</div>

## Types<a href="#types" class="hash-link" aria-label="Direct link to Types" title="Direct link to Types">​</a>

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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/">DetectedObject</a></td>
<td>[androidJvm]<br />
class <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/">DetectedObject</a>(val trackingId: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>, val classId: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>, val probability: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a>, val left: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a>, val right: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a>, val top: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a>, val bottom: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a>)<br />
Represents a single detected object.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-object-detection-config/">ObjectDetectionConfig</a></td>
<td>[androidJvm]<br />
class <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-object-detection-config/">ObjectDetectionConfig</a>(val frameRate: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>, val framesUntilSeen: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>, val framesUntilDiscarded: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>)<br />
Wrapper for the native ARDK_ObjectDetection_Configuration type.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-object-detection-image-params/">ObjectDetectionImageParams</a></td>
<td>[androidJvm]<br />
data class <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-object-detection-image-params/">ObjectDetectionImageParams</a>(val sourceFrameSize: <a href="https://developer.android.com/reference/kotlin/android/util/Size.html" target="_blank" rel="noopener noreferrer">Size</a>, val modelFrameSize: <a href="https://developer.android.com/reference/kotlin/android/util/Size.html" target="_blank" rel="noopener noreferrer">Size</a>)<br />
Container for information about the camera image input that generated an awareness image, along with the model input size.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-object-detection-metadata/">ObjectDetectionMetadata</a></td>
<td>[androidJvm]<br />
data class <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-object-detection-metadata/">ObjectDetectionMetadata</a>(val awarenessParams: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-awareness-image-params/">AwarenessImageParams</a>, val imageParams: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-object-detection-image-params/">ObjectDetectionImageParams</a>)</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-object-detection-result/">ObjectDetectionResult</a></td>
<td>[androidJvm]<br />
class <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-object-detection-result/">ObjectDetectionResult</a>(val awarenessParams: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-awareness-image-params/">AwarenessImageParams</a>, val numDetections: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>, val numClasses: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html" target="_blank" rel="noopener noreferrer">Int</a>, val boundingBoxLocations: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float-array/index.html" target="_blank" rel="noopener noreferrer">FloatArray</a>?, val probabilities: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float-array/index.html" target="_blank" rel="noopener noreferrer">FloatArray</a>?, val trackingIds: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int-array/index.html" target="_blank" rel="noopener noreferrer">IntArray</a>?, val imageParams: <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-object-detection-image-params/">ObjectDetectionImageParams</a>)<br />
Wrapper for the native object detection result buffer.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-object-detection-session/">ObjectDetectionSession</a></td>
<td>[androidJvm]<br />
class <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-object-detection-session/">ObjectDetectionSession</a> : <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk/-session-base/">SessionBase</a>&lt;<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-object-detection-session/">ObjectDetectionSession</a>&gt;<br />
Creates and manages an instance of the Object Detection ARDK feature.</td>
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
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/height/">height</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/">DetectedObject</a>.<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/height/">height</a>(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a><br />
Returns the height of this <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/">DetectedObject</a>'s bounding box.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/to-detected-objects/">toDetectedObjects</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-object-detection-result/">ObjectDetectionResult</a>.<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/to-detected-objects/">toDetectedObjects</a>(confidenceThreshold: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a> = 0.4f): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html" target="_blank" rel="noopener noreferrer">List</a>&lt;<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/">DetectedObject</a>&gt;<br />
Converts this <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-object-detection-result/">ObjectDetectionResult</a> into a list of strongly typed <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/">DetectedObject</a> instances.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/transformed/">transformed</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/">DetectedObject</a>.<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/transformed/">transformed</a>(display: <a href="https://developer.android.com/reference/kotlin/android/graphics/Matrix.html" target="_blank" rel="noopener noreferrer">Matrix</a>?, reprojection: <a href="https://developer.android.com/reference/kotlin/android/graphics/Matrix.html" target="_blank" rel="noopener noreferrer">Matrix</a>? = null, containerSize: <a href="https://developer.android.com/reference/kotlin/android/util/Size.html" target="_blank" rel="noopener noreferrer">Size</a>, viewportSize: <a href="https://developer.android.com/reference/kotlin/android/util/Size.html" target="_blank" rel="noopener noreferrer">Size</a>): <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/">DetectedObject</a><br />
Transforms this <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/">DetectedObject</a>'s bounding box from model space into viewport space, using optional reprojection and display matrices.</td>
</tr>
<tr>
<td><a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/width/">width</a></td>
<td>[androidJvm]<br />
fun <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/">DetectedObject</a>.<a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/width/">width</a>(): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a><br />
Returns the width of this <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/">DetectedObject</a>'s bounding box.</td>
</tr>
</tbody>
</table>

</div>

</div>
