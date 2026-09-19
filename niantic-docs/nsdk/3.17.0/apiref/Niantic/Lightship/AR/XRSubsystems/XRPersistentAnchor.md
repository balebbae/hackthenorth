---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchor/
title: struct XRPersistentAnchor
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct XRPersistentAnchor

</div>

(Niantic.Lightship.AR.XRSubsystems.XRPersistentAnchor)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Describes session-relative data for an anchor.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
struct XRPersistentAnchor:
     ITrackable,
      IEquatable< XRPersistentAnchor > {
      // fields
    
      static XRPersistentAnchor defaultValue => s_Default;
        readonly TrackableId trackableId => m_Id;
       readonly Pose pose => m_Pose;
       readonly TrackingState trackingState => m_TrackingState;
        readonly TrackingStateReason trackingStateReason => m_TrackingStateReason;
      readonly float trackingConfidence => m_TrackingConfidence;
        readonly XRPersistentAnchorPayload xrPersistentAnchorPayload => m_XRPersistentAnchorPayload;
        readonly UInt64 timestampMs => m_timestampMs;
       IntPtr nativePtr => m_XRPersistentAnchorPayload.nativePtr;

     // methods
   
     XRPersistentAnchor(
          TrackableId trackableId,
            Pose pose,
          TrackingState trackingState,
            TrackingStateReason trackingStateReason,
            XRPersistentAnchorPayload xrPersistentAnchorPayload,
            UInt64 timestampMs,
         float trackingConfidence = 0.0f
     );
    
     XRPersistentAnchor(TrackableId trackableId);
        override int GetHashCode();
     bool Equals(XRPersistentAnchor other);
     override bool Equals(object obj);
      static bool operator == (XRPersistentAnchor lhs, XRPersistentAnchor rhs);
       static bool operator != (XRPersistentAnchor lhs, XRPersistentAnchor rhs);
   };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Describes session-relative data for an anchor.

    **See also**:

    [XRPersistentAnchor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchor/)

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### defaultValue<a href="#defaultValue" class="hash-link" aria-label="Direct link to defaultValue" title="Direct link to defaultValue">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static XRPersistentAnchor defaultValue => s_Default
```

</div>

</div>

Gets a default-initialized [XRPersistentAnchor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchor/). This may be different from the zero-initialized version (for example, the [pose](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchor/#pose) is Pose.identity instead of zero-initialized).

#### trackableId<a href="#trackableId" class="hash-link" aria-label="Direct link to trackableId" title="Direct link to trackableId">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly TrackableId trackableId => m_Id
```

</div>

</div>

Get the TrackableId associated with this anchor.

#### pose<a href="#pose" class="hash-link" aria-label="Direct link to pose" title="Direct link to pose">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly Pose pose => m_Pose
```

</div>

</div>

Get the Pose, in session space, for this anchor.

#### trackingState<a href="#trackingState" class="hash-link" aria-label="Direct link to trackingState" title="Direct link to trackingState">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly TrackingState trackingState => m_TrackingState
```

</div>

</div>

Get the TrackingState of this anchor.

#### trackingStateReason<a href="#trackingStateReason" class="hash-link" aria-label="Direct link to trackingStateReason" title="Direct link to trackingStateReason">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly TrackingStateReason trackingStateReason => m_TrackingStateReason
```

</div>

</div>

Get the [trackingStateReason](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchor/#trackingStateReason) of this anchor.

#### trackingConfidence<a href="#trackingConfidence" class="hash-link" aria-label="Direct link to trackingConfidence" title="Direct link to trackingConfidence">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly float trackingConfidence => m_TrackingConfidence
```

</div>

</div>

Get the [trackingConfidence](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchor/#trackingConfidence) of this anchor.

#### xrPersistentAnchorPayload<a href="#xrPersistentAnchorPayload" class="hash-link" aria-label="Direct link to xrPersistentAnchorPayload" title="Direct link to xrPersistentAnchorPayload">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly XRPersistentAnchorPayload xrPersistentAnchorPayload => m_XRPersistentAnchorPayload
```

</div>

</div>

The payload for this anchor

#### timestampMs<a href="#timestampMs" class="hash-link" aria-label="Direct link to timestampMs" title="Direct link to timestampMs">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly UInt64 timestampMs => m_timestampMs
```

</div>

</div>

Get the timestamp in miliseconds of the latest update for this anchor. The timestamp has the same base as the frame.

#### nativePtr<a href="#nativePtr" class="hash-link" aria-label="Direct link to nativePtr" title="Direct link to nativePtr">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
IntPtr nativePtr => m_XRPersistentAnchorPayload.nativePtr
```

</div>

</div>

A native pointer associated with the anchor. The data pointed to by this pointer is implementation-specific.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### XRPersistentAnchor<a href="#XRPersistentAnchor" class="hash-link" aria-label="Direct link to XRPersistentAnchor" title="Direct link to XRPersistentAnchor">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
XRPersistentAnchor(
      TrackableId trackableId,
        Pose pose,
      TrackingState trackingState,
        TrackingStateReason trackingStateReason,
        XRPersistentAnchorPayload xrPersistentAnchorPayload,
        UInt64 timestampMs,
     float trackingConfidence = 0.0f
 )
```

</div>

</div>

Constructs the session-relative data for an anchor. This is typically provided by an implementation of the [XRPersistentAnchor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchor/) and not invoked directly.

    **Parameters**:

    `trackableId` - The TrackableId associated with this anchor.

    `pose` - The Pose, in session space, of the anchor.

    `trackingState` - The TrackingState of the anchor.

    `trackingStateReason` - The reason for the current tracking state.

    `trackingConfidence` - Positive number representing confidence we have in latest tracking update.

    `xrPersistentAnchorPayload` - The payload associated with the anchor.

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
bool Equals(XRPersistentAnchor other)
```

</div>

</div>

Tests for equality.

    **Parameters**:

    `other` - The other [XRPersistentAnchor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchor/) to compare against.

    **Returns:**

    `True` if every field in *other* is equal to this [XRPersistentAnchor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchor/), otherwise false.

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

    `True` if *obj* is of type [XRPersistentAnchor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchor/) and [Equals(XRPersistentAnchor)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchor/#Equals) also returns `true`; otherwise `false`.

#### operator==<a href="#operator==" class="hash-link" aria-label="Direct link to operator==" title="Direct link to operator==">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static bool operator == (XRPersistentAnchor lhs, XRPersistentAnchor rhs)
```

</div>

</div>

Tests for equality. Same as [Equals(XRPersistentAnchor)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchor/#Equals).

    **Parameters**:

    `lhs` - The left-hand side of the comparison.

    `rhs` - The right-hand side of the comparison.

    **Returns:**

    `True` if *lhs* is equal to *rhs*, otherwise `false`.

#### operator!=<a href="#operator!=" class="hash-link" aria-label="Direct link to operator!=" title="Direct link to operator!=">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static bool operator != (XRPersistentAnchor lhs, XRPersistentAnchor rhs)
```

</div>

</div>

Tests for inequality. Same as `!` [Equals(XRPersistentAnchor)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchor/#Equals).

    **Parameters**:

    `lhs` - The left-hand side of the comparison.

    `rhs` - The right-hand side of the comparison.

    **Returns:**

    `True` if *lhs* is not equal to *rhs*, otherwise `false`.

</div>

</div>
