---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/ObjectDetection/ARObjectDetectionModelEventArgs/
title: struct ARObjectDetectionModelEventArgs
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct ARObjectDetectionModelEventArgs

</div>

(Niantic.Lightship.AR.ObjectDetection.ARObjectDetectionModelEventArgs)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

A structure for information about the object detection model that's become ready. This is used to communicate information in the [ARObjectDetectionManager.MetadataInitialized](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/ObjectDetection/ARObjectDetectionManager/#MetadataInitialized) event.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   struct ARObjectDetectionModelEventArgs: IEquatable< ARObjectDetectionModelEventArgs > {
       // properties
    
     IReadOnlyList<string> CategoryNames;

      // methods
   
     override int GetHashCode();
     override bool Equals(object obj);
      bool Equals(ARObjectDetectionModelEventArgs other);
    
     static bool operator == (
         ARObjectDetectionModelEventArgs lhs,
            ARObjectDetectionModelEventArgs rhs
       );
    
     static bool operator != (
         ARObjectDetectionModelEventArgs lhs,
            ARObjectDetectionModelEventArgs rhs
       );
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

A structure for information about the object detection model that's become ready. This is used to communicate information in the [ARObjectDetectionManager.MetadataInitialized](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/ObjectDetection/ARObjectDetectionManager/#MetadataInitialized) event.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### CategoryNames<a href="#CategoryNames" class="hash-link" aria-label="Direct link to CategoryNames" title="Direct link to CategoryNames">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
IReadOnlyList<string> CategoryNames
```

</div>

</div>

The names of all the categories that the currently active object detection model is able to detect.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

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

    `True` if *obj* is of type [ARObjectDetectionModelEventArgs](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/ObjectDetection/ARObjectDetectionModelEventArgs/) and [Equals(ARObjectDetectionModelEventArgs)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/ObjectDetection/ARObjectDetectionModelEventArgs/#Equals) also returns `true`; otherwise `false`.

#### Equals<a href="#Equals" class="hash-link" aria-label="Direct link to Equals" title="Direct link to Equals">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool Equals(ARObjectDetectionModelEventArgs other)
```

</div>

</div>

Tests for equality.

    **Parameters**:

    `other` - The other [ARObjectDetectionModelEventArgs](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/ObjectDetection/ARObjectDetectionModelEventArgs/) to compare against.

    **Returns:**

    `True` if every field in *other* is equal to this [ARObjectDetectionModelEventArgs](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/ObjectDetection/ARObjectDetectionModelEventArgs/), otherwise false.

#### operator==<a href="#operator==" class="hash-link" aria-label="Direct link to operator==" title="Direct link to operator==">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static bool operator == (
     ARObjectDetectionModelEventArgs lhs,
        ARObjectDetectionModelEventArgs rhs
   )
```

</div>

</div>

Tests for equality. Same as [Equals(ARObjectDetectionModelEventArgs)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/ObjectDetection/ARObjectDetectionModelEventArgs/#Equals).

    **Parameters**:

    `lhs` - The left-hand side of the comparison.

    `rhs` - The right-hand side of the comparison.

    **Returns:**

    `True` if *lhs* is equal to *rhs*, otherwise `false`.

#### operator!=<a href="#operator!=" class="hash-link" aria-label="Direct link to operator!=" title="Direct link to operator!=">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static bool operator != (
     ARObjectDetectionModelEventArgs lhs,
        ARObjectDetectionModelEventArgs rhs
   )
```

</div>

</div>

Tests for inequality. Same as `!` [Equals(ARObjectDetectionModelEventArgs)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/ObjectDetection/ARObjectDetectionModelEventArgs/#Equals).

    **Parameters**:

    `lhs` - The left-hand side of the comparison.

    `rhs` - The right-hand side of the comparison.

    **Returns:**

    `True` if *lhs* is not equal to *rhs*, otherwise `false`.

</div>

</div>
