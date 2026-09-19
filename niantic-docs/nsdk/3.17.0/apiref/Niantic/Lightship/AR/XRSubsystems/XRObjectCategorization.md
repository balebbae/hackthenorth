---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRObjectCategorization/
title: struct XRObjectCategorization
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct XRObjectCategorization

</div>

(Niantic.Lightship.AR.XRSubsystems.XRObjectCategorization)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

A structure representing an object detection categorization. The object detection algorithm surfaces at least one categorization per detected object, but usually there are multiple categorizations.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
struct XRObjectCategorization {
       // fields
    
      readonly string CategoryName;
       readonly int CategoryIndex;
         readonly float Confidence;

     // methods
   
     XRObjectCategorization(string name, int index, float confidence);
   };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

A structure representing an object detection categorization. The object detection algorithm surfaces at least one categorization per detected object, but usually there are multiple categorizations.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### CategoryName<a href="#CategoryName" class="hash-link" aria-label="Direct link to CategoryName" title="Direct link to CategoryName">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly string CategoryName
```

</div>

</div>

The category's name.

#### CategoryIndex<a href="#CategoryIndex" class="hash-link" aria-label="Direct link to CategoryIndex" title="Direct link to CategoryIndex">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly int CategoryIndex
```

</div>

</div>

The category's index in the list of category names obtained from the [XRObjectDetectionSubsystem.TryGetCategoryNames](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRObjectDetectionSubsystem/#TryGetCategoryNames) method.

#### Confidence<a href="#Confidence" class="hash-link" aria-label="Direct link to Confidence" title="Direct link to Confidence">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly float Confidence
```

</div>

</div>

The probability that the detected object this categorization belong to is actually of the class described by [CategoryName](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRObjectCategorization/#CategoryName).

</div>

</div>
