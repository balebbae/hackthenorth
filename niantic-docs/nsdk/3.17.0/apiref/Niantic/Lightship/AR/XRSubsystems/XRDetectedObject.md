---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRDetectedObject/
title: class XRDetectedObject
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class XRDetectedObject

</div>

(Niantic.Lightship.AR.XRSubsystems.XRDetectedObject)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

A class representing an object in the XR camera's view detected by the object detection model.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class XRDetectedObject {
  public:
       // properties
    
     abstract float[] Confidences;

       // methods
   
     virtual abstract float GetConfidence(string categoryName) = 0;
       virtual abstract List<XRObjectCategorization> GetConfidentCategorizations(float threshold = 0.4f) = 0;
  
     virtual abstract Rect CalculateRect(
          int viewportWidth,
            int viewportHeight,
           ScreenOrientation orientation
     ) = 0;
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

A class representing an object in the XR camera's view detected by the object detection model.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### Confidences<a href="#Confidences" class="hash-link" aria-label="Direct link to Confidences" title="Direct link to Confidences">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
abstract float[] Confidences
```

</div>

</div>

The confidences of all the categories that can possibly be detected. The element at index i is the confidence for the category with index i.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### GetConfidence<a href="#GetConfidence" class="hash-link" aria-label="Direct link to GetConfidence" title="Direct link to GetConfidence">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract float GetConfidence(string categoryName) = 0
```

</div>

</div>

Gets the confidence value between 0 and 1.0 for the specified category for this detected object.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

    **Parameters**:

    `categoryName` - The name of the category to query. This collection of valid names can be obtained from the [XRObjectDetectionSubsystem.TryGetCategoryNames](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRObjectDetectionSubsystem/#TryGetCategoryNames) method

    **Returns:**

    The confidence value for the specified category for this detected object.

#### GetConfidentCategorizations<a href="#GetConfidentCategorizations" class="hash-link" aria-label="Direct link to GetConfidentCategorizations" title="Direct link to GetConfidentCategorizations">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract List<XRObjectCategorization> GetConfidentCategorizations(float threshold = 0.4f) = 0
```

</div>

</div>

Gets the object categorizations for this detected object.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

    **Parameters**:

    `threshold` - The minimum confidence value needed for a categorization to be included in the returned list. Defaults to 0.4 if not provided.

    **Returns:**

    A list of all the confident categorizations for this detected object.

#### CalculateRect<a href="#CalculateRect" class="hash-link" aria-label="Direct link to CalculateRect" title="Direct link to CalculateRect">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract Rect CalculateRect(
      int viewportWidth,
        int viewportHeight,
       ScreenOrientation orientation
 ) = 0
```

</div>

</div>

The 2D bounding box of the detected object, transformed to be displayed in the given viewport. Usually this will be the same viewport the XR camera image is being rendered to.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

    **Parameters**:

    `viewportWidth` - The pixel width of the viewport.

    `viewportHeight` - The pixel height of the viewport.

    `orientation` - The orientation of the viewport.

    **Returns:**

    The Rect describing the position and bounds of the detected object in the given viewport.

</div>

</div>
