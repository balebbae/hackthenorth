---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/ObjectDetectionResult/
title: ObjectDetectionResult
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `ObjectDetectionResult`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public final class ObjectDetectionResult : AwarenessResult
```

</div>

</div>

A read-only container for the results of a single, successful object detection frame.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `numDetections`<a href="#numdetections" class="hash-link" aria-label="Direct link to numdetections" title="Direct link to numdetections">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let numDetections: UInt32
```

</div>

</div>

The number of detections in the frame

### `numClasses`<a href="#numclasses" class="hash-link" aria-label="Direct link to numclasses" title="Direct link to numclasses">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let numClasses: UInt32
```

</div>

</div>

The number of classes in the frame

### `boundingBoxLocations`<a href="#boundingboxlocations" class="hash-link" aria-label="Direct link to boundingboxlocations" title="Direct link to boundingboxlocations">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let boundingBoxLocations: UnsafeBufferPointer\<Float\>?
```

</div>

</div>

The bounding box locations in the frame. Array of 4 floats per detection. Indices within this array correspond to the indices in the `trackingIds` array.

### `probabilities`<a href="#probabilities" class="hash-link" aria-label="Direct link to probabilities" title="Direct link to probabilities">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let probabilities: UnsafeBufferPointer\<Float\>?
```

</div>

</div>

The probabilities in the frame. Array of floats per detection. Indices within this array correspond to the indices in the `trackingIds` array.

### `trackingIds`<a href="#trackingids" class="hash-link" aria-label="Direct link to trackingids" title="Direct link to trackingids">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let trackingIds: UnsafeBufferPointer\<UInt32\>?
```

</div>

</div>

The tracking ids in the frame. Array of uint32_t per detection. Indices within this array correspond to the indices in the `boundingBoxLocations` and `probabilities` arrays.

### `imageParams`<a href="#imageparams" class="hash-link" aria-label="Direct link to imageparams" title="Direct link to imageparams">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let imageParams: ObjectDetectionImageParams
```

</div>

</div>

Information about the image parameters used for object detection on this frame

</div>

</div>
