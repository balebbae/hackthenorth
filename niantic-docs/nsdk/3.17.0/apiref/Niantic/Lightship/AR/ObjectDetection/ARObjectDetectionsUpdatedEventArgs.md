---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/ObjectDetection/ARObjectDetectionsUpdatedEventArgs/
title: struct ARObjectDetectionsUpdatedEventArgs
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct ARObjectDetectionsUpdatedEventArgs

</div>

(Niantic.Lightship.AR.ObjectDetection.ARObjectDetectionsUpdatedEventArgs)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

A structure for information about the latest object detections that have been surfaced. This is used to communicate information in the ARObjectDetectionManager.ObjectDetectionsUpdated event.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   struct ARObjectDetectionsUpdatedEventArgs: IEquatable< ARObjectDetectionsUpdatedEventArgs > {
     // fields
    
      IReadOnlyList<XRDetectedObject> Results;

       // methods
   
     override bool Equals(object obj);
      bool Equals(ARObjectDetectionsUpdatedEventArgs other);
     override int GetHashCode();
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

A structure for information about the latest object detections that have been surfaced. This is used to communicate information in the ARObjectDetectionManager.ObjectDetectionsUpdated event.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### Results<a href="#Results" class="hash-link" aria-label="Direct link to Results" title="Direct link to Results">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
IReadOnlyList<XRDetectedObject> Results
```

</div>

</div>

The list of objects detected in the latest input camera frame.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### Equals<a href="#Equals" class="hash-link" aria-label="Direct link to Equals" title="Direct link to Equals">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override bool Equals(object obj)
```

</div>

</div>

Tests for equality.

    **Parameters**:

    `obj` - The `object` to compare against.

    **Returns:**

    `True` if *obj* is of type [ARObjectDetectionsUpdatedEventArgs](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/ObjectDetection/ARObjectDetectionsUpdatedEventArgs/) and [Equals(ARObjectDetectionsUpdatedEventArgs)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/ObjectDetection/ARObjectDetectionsUpdatedEventArgs/#Equals) also returns `true`; otherwise `false`.

#### Equals<a href="#Equals" class="hash-link" aria-label="Direct link to Equals" title="Direct link to Equals">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool Equals(ARObjectDetectionsUpdatedEventArgs other)
```

</div>

</div>

Tests for equality.

    **Parameters**:

    `other` - The other [ARObjectDetectionsUpdatedEventArgs](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/ObjectDetection/ARObjectDetectionsUpdatedEventArgs/) to compare against.

    **Returns:**

    `True` if every field in *other* is equal to this [ARObjectDetectionsUpdatedEventArgs](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/ObjectDetection/ARObjectDetectionsUpdatedEventArgs/), otherwise false.

#### GetHashCode<a href="#GetHashCode" class="hash-link" aria-label="Direct link to GetHashCode" title="Direct link to GetHashCode">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override int GetHashCode()
```

</div>

</div>

Generates a hash suitable for use with containers like `HashSet` and `Dictionary`.

    **Returns:**

    A hash code generated from this object's fields.

</div>

</div>
