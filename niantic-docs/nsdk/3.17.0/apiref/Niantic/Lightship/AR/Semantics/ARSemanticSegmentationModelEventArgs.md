---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Semantics/ARSemanticSegmentationModelEventArgs/
title: struct ARSemanticSegmentationModelEventArgs
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct ARSemanticSegmentationModelEventArgs

</div>

(Niantic.Lightship.AR.Semantics.ARSemanticSegmentationModelEventArgs)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

A structure for information about the semantic segmentation model that's become ready. This is used to communicate information in the [ARSemanticSegmentationManager.MetadataInitialized](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Semantics/ARSemanticSegmentationManager/#MetadataInitialized) event.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   struct ARSemanticSegmentationModelEventArgs: IEquatable< ARSemanticSegmentationModelEventArgs > {
     // properties
    
     IReadOnlyList<string> ChannelNames;
       IReadOnlyDictionary<string, int> ChannelIndices;

        // methods
   
     override int GetHashCode();
     override bool Equals(object obj);
      bool Equals(ARSemanticSegmentationModelEventArgs other);
   
     static bool operator == (
         ARSemanticSegmentationModelEventArgs lhs,
           ARSemanticSegmentationModelEventArgs rhs
      );
    
     static bool operator != (
         ARSemanticSegmentationModelEventArgs lhs,
           ARSemanticSegmentationModelEventArgs rhs
      );
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

A structure for information about the semantic segmentation model that's become ready. This is used to communicate information in the [ARSemanticSegmentationManager.MetadataInitialized](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Semantics/ARSemanticSegmentationManager/#MetadataInitialized) event.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### ChannelNames<a href="#ChannelNames" class="hash-link" aria-label="Direct link to ChannelNames" title="Direct link to ChannelNames">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
IReadOnlyList<string> ChannelNames
```

</div>

</div>

The semantic channels detected by the semantic segmentation model.

#### ChannelIndices<a href="#ChannelIndices" class="hash-link" aria-label="Direct link to ChannelIndices" title="Direct link to ChannelIndices">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
IReadOnlyDictionary<string, int> ChannelIndices
```

</div>

</div>

The indices of the semantic channels detected by the semantic segmentation model.

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

    `True` if *obj* is of type [ARSemanticSegmentationModelEventArgs](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Semantics/ARSemanticSegmentationModelEventArgs/) and [Equals(ARSemanticSegmentationModelEventArgs)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Semantics/ARSemanticSegmentationModelEventArgs/#Equals) also returns `true`; otherwise `false`.

#### Equals<a href="#Equals" class="hash-link" aria-label="Direct link to Equals" title="Direct link to Equals">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool Equals(ARSemanticSegmentationModelEventArgs other)
```

</div>

</div>

Tests for equality.

    **Parameters**:

    `other` - The other [ARSemanticSegmentationModelEventArgs](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Semantics/ARSemanticSegmentationModelEventArgs/) to compare against.

    **Returns:**

    `True` if every field in *other* is equal to this [ARSemanticSegmentationModelEventArgs](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Semantics/ARSemanticSegmentationModelEventArgs/), otherwise false.

#### operator==<a href="#operator==" class="hash-link" aria-label="Direct link to operator==" title="Direct link to operator==">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static bool operator == (
     ARSemanticSegmentationModelEventArgs lhs,
       ARSemanticSegmentationModelEventArgs rhs
  )
```

</div>

</div>

Tests for equality. Same as [Equals(ARSemanticSegmentationModelEventArgs)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Semantics/ARSemanticSegmentationModelEventArgs/#Equals).

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
     ARSemanticSegmentationModelEventArgs lhs,
       ARSemanticSegmentationModelEventArgs rhs
  )
```

</div>

</div>

Tests for inequality. Same as `!` [Equals(ARSemanticSegmentationModelEventArgs)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Semantics/ARSemanticSegmentationModelEventArgs/#Equals).

    **Parameters**:

    `lhs` - The left-hand side of the comparison.

    `rhs` - The right-hand side of the comparison.

    **Returns:**

    `True` if *lhs* is not equal to *rhs*, otherwise `false`.

</div>

</div>
