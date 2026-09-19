---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/to-detected-objects/
title: to-detected-objects
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.objectdetection](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[toDetectedObjects](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/to-detected-objects/)

<div>

# toDetectedObjects

</div>

\[androidJvm\]\
fun [ObjectDetectionResult](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-object-detection-result/).[toDetectedObjects](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/to-detected-objects/)(confidenceThreshold: <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html" target="_blank" rel="noopener noreferrer">Float</a> = 0.4f): <a href="https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html" target="_blank" rel="noopener noreferrer">List</a>\<[DetectedObject](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/)\>

Converts this [ObjectDetectionResult](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-object-detection-result/) into a list of strongly typed [DetectedObject](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/) instances.

This method reads the raw buffers returned from the native object-detection inference (bounding boxes, per-class probabilities, and optional tracking IDs) and constructs high-level objects that are easier to work with in Kotlin.

### Processing steps:<a href="#processing-steps" class="hash-link" aria-label="Direct link to Processing steps:" title="Direct link to Processing steps:">​</a>

1.  For each detection, find the class index with the highest probability.
2.  Skip detections whose confidence is below [confidenceThreshold](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/to-detected-objects/).
3.  Extract the bounding box for each remaining detection (as left, top, right, bottom).
4.  Optionally include the tracking ID if available.
5.  Return all valid detections as a list of [DetectedObject](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/)s.

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

A list of [DetectedObject](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/)s representing valid detections. Returns an empty list if no detections are available or if required buffers are null.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|  |  |
|----|----|
| confidenceThreshold | The minimum probability required for a detection to be kept. Detections below this threshold are discarded. |

</div>

</div>
