---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorSubsystemDescriptor/Cinfo/
title: struct Cinfo
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct Cinfo

</div>

(Niantic.Lightship.AR.XRSubsystems.XRPersistentAnchorSubsystemDescriptor.Cinfo)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Constructor info used to register a descriptor.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   struct Cinfo: IEquatable< Cinfo > {
       // properties
    
     string id;
        Type providerType;
      Type subsystemTypeOverride;
     bool supportsTrackableAttachments;

        // methods
   
     override int GetHashCode();
     override bool Equals(object obj);
      bool Equals(Cinfo other);
      static bool operator == (Cinfo lhs, Cinfo rhs);
     static bool operator != (Cinfo lhs, Cinfo rhs);
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Constructor info used to register a descriptor.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### id<a href="#id" class="hash-link" aria-label="Direct link to id" title="Direct link to id">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
string id
```

</div>

</div>

The string identifier for this subsystem.

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

Specifies the XRPersistentAnchorSubsystem-derived type that forwards casted calls to its provider.

The type of the subsystem to use for instantiation. If null, [XRPersistentAnchorSubsystem](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorSubsystem/) will be instantiated.

#### supportsTrackableAttachments<a href="#supportsTrackableAttachments" class="hash-link" aria-label="Direct link to supportsTrackableAttachments" title="Direct link to supportsTrackableAttachments">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool supportsTrackableAttachments
```

</div>

</div>

true if the subsystem supports attachments, i.e., the ability to attach an anchor to a trackable.

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

    `True` if *obj* is of type Cinfo and Equals(Cinfo) also returns `true`; otherwise `false`.

#### Equals<a href="#Equals" class="hash-link" aria-label="Direct link to Equals" title="Direct link to Equals">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool Equals(Cinfo other)
```

</div>

</div>

Tests for equality.

    **Parameters**:

    `other` - The other Cinfo to compare against.

    **Returns:**

    `True` if every field in *other* is equal to this Cinfo, otherwise false.

#### operator==<a href="#operator==" class="hash-link" aria-label="Direct link to operator==" title="Direct link to operator==">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static bool operator == (Cinfo lhs, Cinfo rhs)
```

</div>

</div>

Tests for equality. Same as Equals(Cinfo).

    **Parameters**:

    `lhs` - The left-hand side of the comparison.

    `rhs` - The right-hand side of the comparison.

    **Returns:**

    `True` if *lhs* is equal to *rhs*, otherwise `false`.

#### operator!=<a href="#operator!=" class="hash-link" aria-label="Direct link to operator!=" title="Direct link to operator!=">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static bool operator != (Cinfo lhs, Cinfo rhs)
```

</div>

</div>

Tests for inequality. Same as `!` Equals(Cinfo).

    **Parameters**:

    `lhs` - The left-hand side of the comparison.

    `rhs` - The right-hand side of the comparison.

    **Returns:**

    `True` if *lhs* is not equal to *rhs*, otherwise `false`.

</div>

</div>
