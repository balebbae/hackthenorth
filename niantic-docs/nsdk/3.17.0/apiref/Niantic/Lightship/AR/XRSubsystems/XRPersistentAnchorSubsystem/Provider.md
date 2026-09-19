---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorSubsystem/Provider/
title: class Provider
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class Provider

</div>

(Niantic.Lightship.AR.XRSubsystems.XRPersistentAnchorSubsystem.Provider)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

An abstract class to be implemented by providers of this subsystem.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class Provider: SubsystemProvider< XRPersistentAnchorSubsystem > {
    public:
       // properties
    
     bool IsMockProvider;
      XRPersistentAnchorConfiguration CurrentConfiguration;

       // methods
   
     virtual abstract TrackableChanges<XRPersistentAnchor> GetChanges(
         XRPersistentAnchor defaultAnchor,
           Allocator allocator
       ) = 0;
    
     virtual abstract bool GetNetworkStatusUpdate(out XRPersistentAnchorNetworkRequestStatus[] statuses) = 0;
     virtual abstract bool GetLocalizationStatusUpdate(out XRPersistentAnchorLocalizationStatus[] statuses) = 0;
      virtual abstract bool GetFrameDiagnosticsUpdate(out XRPersistentAnchorFrameDiagnostics[] statuses) = 0;
      virtual bool GetVpsSessionId(out string vpsSessionId);
       virtual abstract bool GetVpsDebuggerLog(out string vpsDebuggerLog) = 0;
    
     virtual VpsGraphOperationError TryGetDevicePoseAsGeolocation(
           Pose pose,
          out double latitude,
            out double longitude,
           out double altitude,
            out double verticalAccuracy,
            out double horizontalAccuracy,
          out double heading
        );
    
     virtual bool TryAddAnchor(Pose pose, out XRPersistentAnchor anchor);
      virtual bool TryRemoveAnchor(TrackableId anchorId);
  
     virtual bool TryRestoreAnchor(
            XRPersistentAnchorPayload anchorPayload,
            out XRPersistentAnchor anchor
       );
    
     virtual bool TryLocalize(
         XRPersistentAnchorPayload anchorPayload,
            out XRPersistentAnchor anchor
       );
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

An abstract class to be implemented by providers of this subsystem.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### CurrentConfiguration<a href="#CurrentConfiguration" class="hash-link" aria-label="Direct link to CurrentConfiguration" title="Direct link to CurrentConfiguration">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
XRPersistentAnchorConfiguration CurrentConfiguration
```

</div>

</div>

Get or set configuration with \<name\>XRPersistentAnchorConfiguration\</name\>

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### GetChanges<a href="#GetChanges" class="hash-link" aria-label="Direct link to GetChanges" title="Direct link to GetChanges">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract TrackableChanges<XRPersistentAnchor> GetChanges(
     XRPersistentAnchor defaultAnchor,
       Allocator allocator
   ) = 0
```

</div>

</div>

Invoked to get the changes to anchors (added, updated, and removed) since the last call to GetChanges(XRPersistentAnchor,Allocator).

    **Parameters**:

    `defaultAnchor` - The default anchor. This should be used to initialize the returned NativeArrays for backwards compatibility. See Allocator.

    `allocator` - An allocator to use for the NativeArrays in TrackableChanges\<T\>.

    **Returns:**

    Changes since the last call to GetChanges.

#### GetNetworkStatusUpdate<a href="#GetNetworkStatusUpdate" class="hash-link" aria-label="Direct link to GetNetworkStatusUpdate" title="Direct link to GetNetworkStatusUpdate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract bool GetNetworkStatusUpdate(out XRPersistentAnchorNetworkRequestStatus[] statuses) = 0
```

</div>

</div>

Get a list of network status updates, if any

    **Returns:**

    True if an update is present, false otherwise

#### GetLocalizationStatusUpdate<a href="#GetLocalizationStatusUpdate" class="hash-link" aria-label="Direct link to GetLocalizationStatusUpdate" title="Direct link to GetLocalizationStatusUpdate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract bool GetLocalizationStatusUpdate(out XRPersistentAnchorLocalizationStatus[] statuses) = 0
```

</div>

</div>

Get a list of localization status updates, if any

    **Returns:**

    True if an update is present, false otherwise

#### GetFrameDiagnosticsUpdate<a href="#GetFrameDiagnosticsUpdate" class="hash-link" aria-label="Direct link to GetFrameDiagnosticsUpdate" title="Direct link to GetFrameDiagnosticsUpdate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract bool GetFrameDiagnosticsUpdate(out XRPersistentAnchorFrameDiagnostics[] statuses) = 0
```

</div>

</div>

Get a list of frame diagnostics updates, if any

    **Returns:**

    True if an update is present, false otherwise

#### GetVpsSessionId<a href="#GetVpsSessionId" class="hash-link" aria-label="Direct link to GetVpsSessionId" title="Direct link to GetVpsSessionId">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual bool GetVpsSessionId(out string vpsSessionId)
```

</div>

</div>

Get the vps session id, if any

    **Parameters**:

    `vpsSessionId` - The vps session id as 32 character hexidecimal upper-case string.

    **Returns:**

    True if vps session id is present, false otherwise

#### TryGetDevicePoseAsGeolocation<a href="#TryGetDevicePoseAsGeolocation" class="hash-link" aria-label="Direct link to TryGetDevicePoseAsGeolocation" title="Direct link to TryGetDevicePoseAsGeolocation">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual VpsGraphOperationError TryGetDevicePoseAsGeolocation(
       Pose pose,
      out double latitude,
        out double longitude,
       out double altitude,
        out double verticalAccuracy,
        out double horizontalAccuracy,
      out double heading
    )
```

</div>

</div>

Provider converts a Unity pose to GPS with double precision. Implementations should flatten the TRS into a float\[16\] in column-major, [ARDK](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/ARDK/) coordinate space before invoking native.

#### TryAddAnchor<a href="#TryAddAnchor" class="hash-link" aria-label="Direct link to TryAddAnchor" title="Direct link to TryAddAnchor">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual bool TryAddAnchor(Pose pose, out XRPersistentAnchor anchor)
```

</div>

</div>

Should create a new anchor with the provided *pose*.

    **Parameters**:

    `pose` - The pose, in session space, of the new anchor.

    `anchor` - The new anchor. Must be valid only if this method returns true.

    **Returns:**

    Should return true if the new anchor was added, otherwise false.

#### TryRemoveAnchor<a href="#TryRemoveAnchor" class="hash-link" aria-label="Direct link to TryRemoveAnchor" title="Direct link to TryRemoveAnchor">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual bool TryRemoveAnchor(TrackableId anchorId)
```

</div>

</div>

Should remove an existing anchor with TrackableId *anchorId*.

    **Parameters**:

    `anchorId` - The id of an existing anchor to remove.

    **Returns:**

    Should return true if the anchor was removed, otherwise false. If the anchor does not exist, return false.

#### TryRestoreAnchor<a href="#TryRestoreAnchor" class="hash-link" aria-label="Direct link to TryRestoreAnchor" title="Direct link to TryRestoreAnchor">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual bool TryRestoreAnchor(
        XRPersistentAnchorPayload anchorPayload,
        out XRPersistentAnchor anchor
   )
```

</div>

</div>

Tries to restore an anchor

    **Parameters**:

    `anchorPayload` - The payload to restore the anchor with

    `anchor` - The restored anchor

    **Returns:**

    Whether or not the restoration was successful

</div>

</div>
