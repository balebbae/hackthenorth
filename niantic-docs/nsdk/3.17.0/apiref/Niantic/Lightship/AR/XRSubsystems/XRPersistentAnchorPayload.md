---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorPayload/
title: struct XRPersistentAnchorPayload
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct XRPersistentAnchorPayload

</div>

(Niantic.Lightship.AR.XRSubsystems.XRPersistentAnchorPayload)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Represents the payload for a persistent anchor.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   struct XRPersistentAnchorPayload: IEquatable< XRPersistentAnchorPayload > {
       // fields
    
      IntPtr nativePtr => m_NativePtr;
      int size => m_Size;

        // methods
   
     XRPersistentAnchorPayload(IntPtr nativePayloadPtr, int size);
        bool Equals(XRPersistentAnchorPayload other);
      override bool Equals(object obj);
      override int GetHashCode();
     byte[] GetDataAsBytes();
  
     static bool operator == (
         XRPersistentAnchorPayload lhs,
          XRPersistentAnchorPayload rhs
     );
    
     static bool operator != (
         XRPersistentAnchorPayload lhs,
          XRPersistentAnchorPayload rhs
     );
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Represents the payload for a persistent anchor.

    **See also**:

    [XRPersistentAnchorPayload](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorPayload/)

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### nativePtr<a href="#nativePtr" class="hash-link" aria-label="Direct link to nativePtr" title="Direct link to nativePtr">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
IntPtr nativePtr => m_NativePtr
```

</div>

</div>

A native pointer associated with the anchor payload. The data pointed to by this pointer is implementation-specific.

#### size<a href="#size" class="hash-link" aria-label="Direct link to size" title="Direct link to size">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
int size => m_Size
```

</div>

</div>

The size of the payload

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### XRPersistentAnchorPayload<a href="#XRPersistentAnchorPayload" class="hash-link" aria-label="Direct link to XRPersistentAnchorPayload" title="Direct link to XRPersistentAnchorPayload">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
XRPersistentAnchorPayload(IntPtr nativePayloadPtr, int size)
```

</div>

</div>

Constructs the payload data for an anchor from native code.

    **Parameters**:

    `nativePayloadPtr` - A native pointer associated with the anchor payload. The data pointed to by this pointer is implementation-specific.

#### Equals<a href="#Equals" class="hash-link" aria-label="Direct link to Equals" title="Direct link to Equals">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool Equals(XRPersistentAnchorPayload other)
```

</div>

</div>

Tests for equality.

    **Parameters**:

    `other` - The other [XRPersistentAnchorPayload](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorPayload/) to compare against.

    **Returns:**

    `True` if every field in *other* is equal to this [XRPersistentAnchorPayload](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorPayload/), otherwise false.

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

    `True` if *obj* is of type [XRPersistentAnchorPayload](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorPayload/) and [Equals(XRPersistentAnchorPayload)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorPayload/#Equals) also returns `true`; otherwise `false`.

#### GetDataAsBytes<a href="#GetDataAsBytes" class="hash-link" aria-label="Direct link to GetDataAsBytes" title="Direct link to GetDataAsBytes">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
byte[] GetDataAsBytes()
```

</div>

</div>

Get the data associated with this [XRPersistentAnchorPayload](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorPayload/). This is an expensive operation! Returns empty byte\[\] if payload is invalid

#### operator==<a href="#operator==" class="hash-link" aria-label="Direct link to operator==" title="Direct link to operator==">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static bool operator == (
     XRPersistentAnchorPayload lhs,
      XRPersistentAnchorPayload rhs
 )
```

</div>

</div>

Tests for equality. Same as [Equals(XRPersistentAnchorPayload)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorPayload/#Equals).

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
     XRPersistentAnchorPayload lhs,
      XRPersistentAnchorPayload rhs
 )
```

</div>

</div>

Tests for inequality. Same as `!` [Equals(XRPersistentAnchorPayload)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorPayload/#Equals).

    **Parameters**:

    `lhs` - The left-hand side of the comparison.

    `rhs` - The right-hand side of the comparison.

    **Returns:**

    `True` if *lhs* is not equal to *rhs*, otherwise `false`.

</div>

</div>
