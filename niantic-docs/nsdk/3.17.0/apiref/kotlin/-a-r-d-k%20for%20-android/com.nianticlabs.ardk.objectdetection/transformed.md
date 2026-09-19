---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/transformed/
title: transformed
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

[ARDK for Android](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/)/[com.nianticlabs.ardk.objectdetection](https://www.nianticspatial.com/docs/nsdk/3.17.0/)/[transformed](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/transformed/)

<div>

# transformed

</div>

\[androidJvm\]\
fun [DetectedObject](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/).[transformed](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/transformed/)(display: <a href="https://developer.android.com/reference/kotlin/android/graphics/Matrix.html" target="_blank" rel="noopener noreferrer">Matrix</a>?, reprojection: <a href="https://developer.android.com/reference/kotlin/android/graphics/Matrix.html" target="_blank" rel="noopener noreferrer">Matrix</a>? = null, containerSize: <a href="https://developer.android.com/reference/kotlin/android/util/Size.html" target="_blank" rel="noopener noreferrer">Size</a>, viewportSize: <a href="https://developer.android.com/reference/kotlin/android/util/Size.html" target="_blank" rel="noopener noreferrer">Size</a>): [DetectedObject](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/)

Transforms this [DetectedObject](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/)'s bounding box from model space into viewport space, using optional reprojection and display matrices.

The transformation happens in two stages:

1.  [reprojection](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/transformed/) — (optional) applies a full 3×3 projective homography to reproject bounding box coordinates from the camera pose at detection time to the current frame pose.
2.  [display](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/transformed/) — (optional) applies a 2D affine transformation to map normalized coordinates from model space into the screen's coordinate system (e.g. scale and offset into the viewport).

#### Return<a href="#return" class="hash-link" aria-label="Direct link to Return" title="Direct link to Return">​</a>

A new [DetectedObject](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/kotlin/-a-r-d-k%20for%20-android/com.nianticlabs.ardk.objectdetection/-detected-object/) with transformed pixel-space coordinates.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

androidJvm

|  |  |
|----|----|
| display | An optional affine <a href="https://developer.android.com/reference/kotlin/android/graphics/Matrix.html" target="_blank" rel="noopener noreferrer">Matrix</a> that maps normalized model-space coordinates into the screen or viewport coordinate system. |
| reprojection | An optional projective <a href="https://developer.android.com/reference/kotlin/android/graphics/Matrix.html" target="_blank" rel="noopener noreferrer">Matrix</a> that reprojects coordinates to match the current camera pose, compensating for camera motion since detection. |
| containerSize | The size of the model's input frame (used to normalize the bounding box). |
| viewportSize | The size of the current screen or viewport (used to scale up to pixels). |

</div>

</div>
