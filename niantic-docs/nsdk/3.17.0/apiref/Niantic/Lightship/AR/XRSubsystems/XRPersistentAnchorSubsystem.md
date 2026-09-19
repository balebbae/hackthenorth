---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorSubsystem/
title: class XRPersistentAnchorSubsystem
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class XRPersistentAnchorSubsystem

</div>

(Niantic.Lightship.AR.XRSubsystems.XRPersistentAnchorSubsystem)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Base class for a persistent anchor subsystem.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class XRPersistentAnchorSubsystem: TrackingSubsystem< XRPersistentAnchor, XRPersistentAnchorSubsystem, XRPersistentAnchorSubsystemDescriptor, XRPersistentAnchorSubsystem.Provider > {
    public:
   
     class Provider;

        // fields
    
      bool IsMockProvider => provider.IsMockProvider;

      // properties
    
     XRPersistentAnchorConfiguration? CurrentConfiguration;

      // events
    
     event debugInfoProvided();
       event OnConfigurationChanged();
      event VpsDebuggerEvent();

        // methods
   
     XRPersistentAnchorSubsystem();
     new void Start();
       override TrackableChanges<XRPersistentAnchor> GetChanges(Allocator allocator);
     bool TryAddAnchor(Pose pose, out XRPersistentAnchor anchor);
        bool TryRemoveAnchor(TrackableId anchorId);
    
     bool TryRestoreAnchor(
          XRPersistentAnchorPayload anchorPayload,
            out XRPersistentAnchor anchor
       );
    
     bool TryLocalize(
           XRPersistentAnchorPayload anchorPayload,
            out XRPersistentAnchor anchor
       );
    
     bool GetVpsSessionId(out string vpsSessionId);
 
     VpsGraphOperationError TryGetDevicePoseAsGeolocation(
         Pose pose,
          out double latitude,
            out double longitude,
           out double altitude,
            out double verticalAccuracy,
            out double horizontalAccuracy,
          out double heading
        );

    protected:
        // methods
   
     override void OnStart();
        override void OnStop();
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Base class for a persistent anchor subsystem.

An anchor is a pose in the physical environment that is tracked by an XR device. As the device refines its understanding of the environment, anchors will be updated, allowing you to keep virtual content connected to a real-world position and orientation.

This abstract class should be implemented by an XR provider and instantiated using the SubsystemManager to enumerate the available [XRPersistentAnchorSubsystemDescriptor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorSubsystemDescriptor/) s.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### CurrentConfiguration<a href="#CurrentConfiguration" class="hash-link" aria-label="Direct link to CurrentConfiguration" title="Direct link to CurrentConfiguration">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
XRPersistentAnchorConfiguration? CurrentConfiguration
```

</div>

</div>

Get or set configuration with \<name\>XRPersistentAnchorConfiguration\</name\>

.. note::

This api calls into native, so getting or setting the configuration will return a deep copy Updated configurations need to be set to take effect

### Events<a href="#events" class="hash-link" aria-label="Direct link to Events" title="Direct link to Events">​</a>

#### debugInfoProvided<a href="#debugInfoProvided" class="hash-link" aria-label="Direct link to debugInfoProvided" title="Direct link to debugInfoProvided">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
event debugInfoProvided()
```

</div>

</div>

Called when debug info is available

Each invocation of this event contains a [XRPersistentAnchorDebugInfo](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorDebugInfo/) object that contains arrays of [XRPersistentAnchorNetworkRequestStatus](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorNetworkRequestStatus/), [XRPersistentAnchorLocalizationStatus](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorLocalizationStatus/), and XRPersistentAnchorFrameDiagnostics

#### OnConfigurationChanged<a href="#OnConfigurationChanged" class="hash-link" aria-label="Direct link to OnConfigurationChanged" title="Direct link to OnConfigurationChanged">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
event OnConfigurationChanged()
```

</div>

</div>

Called when the subsystem's configuration changes

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### XRPersistentAnchorSubsystem<a href="#XRPersistentAnchorSubsystem" class="hash-link" aria-label="Direct link to XRPersistentAnchorSubsystem" title="Direct link to XRPersistentAnchorSubsystem">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
XRPersistentAnchorSubsystem()
```

</div>

</div>

Constructor. Do not invoke directly; use the SubsystemManager to enumerate the available [XRPersistentAnchorSubsystemDescriptor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorSubsystemDescriptor/) s and call Create on the desired descriptor.

#### GetChanges<a href="#GetChanges" class="hash-link" aria-label="Direct link to GetChanges" title="Direct link to GetChanges">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override TrackableChanges<XRPersistentAnchor> GetChanges(Allocator allocator)
```

</div>

</div>

Get the changes to anchors (added, updated, and removed) since the last call to [GetChanges(Allocator)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorSubsystem/#GetChanges).

    **Parameters**:

    `allocator` - An allocator to use for the NativeArrays in TrackableChanges\<T\>.

    **Returns:**

    Changes since the last call to [GetChanges](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorSubsystem/#GetChanges).

#### TryAddAnchor<a href="#TryAddAnchor" class="hash-link" aria-label="Direct link to TryAddAnchor" title="Direct link to TryAddAnchor">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryAddAnchor(Pose pose, out XRPersistentAnchor anchor)
```

</div>

</div>

Attempts to create a new anchor with the provide *pose*.

    **Parameters**:

    `pose` - The pose, in session space, of the new anchor.

    `anchor` - The new anchor. Only valid if this method returns true.

    **Returns:**

    true if the new anchor was added, otherwise false.

#### TryRemoveAnchor<a href="#TryRemoveAnchor" class="hash-link" aria-label="Direct link to TryRemoveAnchor" title="Direct link to TryRemoveAnchor">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryRemoveAnchor(TrackableId anchorId)
```

</div>

</div>

Attempts to remove an existing anchor with TrackableId *anchorId*.

    **Parameters**:

    `anchorId` - The id of an existing anchor to remove.

    **Returns:**

    true if the anchor was removed, otherwise false.

#### TryRestoreAnchor<a href="#TryRestoreAnchor" class="hash-link" aria-label="Direct link to TryRestoreAnchor" title="Direct link to TryRestoreAnchor">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryRestoreAnchor(
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

#### GetVpsSessionId<a href="#GetVpsSessionId" class="hash-link" aria-label="Direct link to GetVpsSessionId" title="Direct link to GetVpsSessionId">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool GetVpsSessionId(out string vpsSessionId)
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
VpsGraphOperationError TryGetDevicePoseAsGeolocation(
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

Convert a Unity Pose to GPS using the provider with double precision.

</div>

</div>
