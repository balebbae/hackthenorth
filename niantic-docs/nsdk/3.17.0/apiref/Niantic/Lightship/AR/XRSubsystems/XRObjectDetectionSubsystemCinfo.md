---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRObjectDetectionSubsystemCinfo/
title: struct XRObjectDetectionSubsystemCinfo
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct XRObjectDetectionSubsystemCinfo

</div>

(Niantic.Lightship.AR.XRSubsystems.XRObjectDetectionSubsystemCinfo)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Constructor parameters for the [XRObjectDetectionSubsystemDescriptor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRObjectDetectionSubsystemDescriptor/).

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   struct XRObjectDetectionSubsystemCinfo: IEquatable< XRObjectDetectionSubsystemCinfo > {
       // properties
    
     string id;
        Type providerType;
      Type subsystemTypeOverride;
     Func<Supported> objectDetectionSupportedDelegate;

       // methods
   
     bool Equals(XRObjectDetectionSubsystemCinfo other);
        override bool Equals(System.Object obj);
       override int GetHashCode();
 
     static bool operator == (
         XRObjectDetectionSubsystemCinfo lhs,
            XRObjectDetectionSubsystemCinfo rhs
       );
    
     static bool operator != (
         XRObjectDetectionSubsystemCinfo lhs,
            XRObjectDetectionSubsystemCinfo rhs
       );
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Constructor parameters for the [XRObjectDetectionSubsystemDescriptor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRObjectDetectionSubsystemDescriptor/).

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### id<a href="#id" class="hash-link" aria-label="Direct link to id" title="Direct link to id">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
string id
```

</div>

</div>

Specifies an identifier for the provider implementation of the subsystem.

The identifier for the provider implementation of the subsystem.

#### providerType<a href="#providerType" class="hash-link" aria-label="Direct link to providerType" title="Direct link to providerType">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Type providerType
```

</div>

</div>

Specifies the provider implementation type to use for instantiation.

The provider implementation type to use for instantiation.

#### subsystemTypeOverride<a href="#subsystemTypeOverride" class="hash-link" aria-label="Direct link to subsystemTypeOverride" title="Direct link to subsystemTypeOverride">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Type subsystemTypeOverride
```

</div>

</div>

Specifies the XRAnchorSubsystem-derived type that forwards casted calls to its provider.

The type of the subsystem to use for instantiation. If null, XRAnchorSubsystem will be instantiated.

#### objectDetectionSupportedDelegate<a href="#objectDetectionSupportedDelegate" class="hash-link" aria-label="Direct link to objectDetectionSupportedDelegate" title="Direct link to objectDetectionSupportedDelegate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Func<Supported> objectDetectionSupportedDelegate
```

</div>

</div>

Specifies if the current subsystem supports semantics segmentation image.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### Equals<a href="#Equals" class="hash-link" aria-label="Direct link to Equals" title="Direct link to Equals">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool Equals(XRObjectDetectionSubsystemCinfo other)
```

</div>

</div>

Tests for equality.

    **Parameters**:

    `other` - The other [XRObjectDetectionSubsystemCinfo](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRObjectDetectionSubsystemCinfo/) to compare against.

    **Returns:**

    `True` if every field in *other* is equal to this [XRObjectDetectionSubsystemCinfo](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRObjectDetectionSubsystemCinfo/), otherwise false.

#### Equals<a href="#Equals" class="hash-link" aria-label="Direct link to Equals" title="Direct link to Equals">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override bool Equals(System.Object obj)
```

</div>

</div>

Tests for equality.

    **Parameters**:

    `obj` - The `object` to compare against.

    **Returns:**

    `True` if *obj* is of type [XRObjectDetectionSubsystemCinfo](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRObjectDetectionSubsystemCinfo/) and [Equals(XRObjectDetectionSubsystemCinfo)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRObjectDetectionSubsystemCinfo/#Equals) also returns `true`; otherwise `false`.

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

#### operator==<a href="#operator==" class="hash-link" aria-label="Direct link to operator==" title="Direct link to operator==">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static bool operator == (
     XRObjectDetectionSubsystemCinfo lhs,
        XRObjectDetectionSubsystemCinfo rhs
   )
```

</div>

</div>

Tests for equality. Same as [Equals(XRObjectDetectionSubsystemCinfo)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRObjectDetectionSubsystemCinfo/#Equals).

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
     XRObjectDetectionSubsystemCinfo lhs,
        XRObjectDetectionSubsystemCinfo rhs
   )
```

</div>

</div>

Tests for inequality. Same as `!` [Equals(XRObjectDetectionSubsystemCinfo)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRObjectDetectionSubsystemCinfo/#Equals).

    **Parameters**:

    `lhs` - The left-hand side of the comparison.

    `rhs` - The right-hand side of the comparison.

    **Returns:**

    `True` if *lhs* is not equal to *rhs*, otherwise `false`.

</div>

</div>
