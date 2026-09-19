---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/SharedSpaceManager/
title: class SharedSpaceManager
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class SharedSpaceManager

</div>

(Niantic.Lightship.SharedAR.Colocalization.SharedSpaceManager)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The [SharedSpaceManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/SharedSpaceManager/) manages to set up necessary components for colocalization. The [SharedSpaceManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/SharedSpaceManager/) hides complexity in setting up colocalization related object hierarchy and networking room associated to the tracking target.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class SharedSpaceManager: MonoBehaviour {
   public:
   
     enumColocalizationType;

    
     struct SharedSpaceManagerStateChangeEventArgs;

     // properties
    
     GameObject SharedArOriginObject;
        ISharedSpaceTrackingOptions SharedSpaceTrackingOptions;
     ISharedSpaceRoomOptions SharedSpaceRoomOptions;

     // events
    
     event sharedSpaceManagerStateChanged();

      // methods
   
     ColocalizationType GetColocalizationType();
 
     void StartSharedSpace(
          ISharedSpaceTrackingOptions trackingOptions,
            ISharedSpaceRoomOptions roomOptions
       );
    
     void PrepareRoom(ISharedSpaceRoomOptions roomOptions);
     void LeaveRoom();
     SharedAROrigin CreateSharedOrigin(ARPersistentAnchor anchor);
        void DestroySharedArOrigin();
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The [SharedSpaceManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/SharedSpaceManager/) manages to set up necessary components for colocalization. The [SharedSpaceManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/SharedSpaceManager/) hides complexity in setting up colocalization related object hierarchy and networking room associated to the tracking target.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### SharedArOriginObject<a href="#SharedArOriginObject" class="hash-link" aria-label="Direct link to SharedArOriginObject" title="Direct link to SharedArOriginObject">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
GameObject SharedArOriginObject
```

</div>

</div>

Reference to the GameObject representing shared origin/root

#### SharedSpaceTrackingOptions<a href="#SharedSpaceTrackingOptions" class="hash-link" aria-label="Direct link to SharedSpaceTrackingOptions" title="Direct link to SharedSpaceTrackingOptions">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ISharedSpaceTrackingOptions SharedSpaceTrackingOptions
```

</div>

</div>

Getting currently active [ISharedSpaceTrackingOptions](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/ISharedSpaceTrackingOptions/) set in the [SharedSpaceManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/SharedSpaceManager/)

#### SharedSpaceRoomOptions<a href="#SharedSpaceRoomOptions" class="hash-link" aria-label="Direct link to SharedSpaceRoomOptions" title="Direct link to SharedSpaceRoomOptions">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ISharedSpaceRoomOptions SharedSpaceRoomOptions
```

</div>

</div>

Getting currently active [ISharedSpaceRoomOptions](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/ISharedSpaceRoomOptions/) set in the [SharedSpaceManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/SharedSpaceManager/)

### Events<a href="#events" class="hash-link" aria-label="Direct link to Events" title="Direct link to Events">​</a>

#### sharedSpaceManagerStateChanged<a href="#sharedSpaceManagerStateChanged" class="hash-link" aria-label="Direct link to sharedSpaceManagerStateChanged" title="Direct link to sharedSpaceManagerStateChanged">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
event sharedSpaceManagerStateChanged()
```

</div>

</div>

An event invoked when state colocalization related state changed. At the moment, only invoked when underlying tracking state changed

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### GetColocalizationType<a href="#GetColocalizationType" class="hash-link" aria-label="Direct link to GetColocalizationType" title="Direct link to GetColocalizationType">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ColocalizationType GetColocalizationType()
```

</div>

</div>

Get the ColocalizationType

    **Returns:**

    [Colocalization](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/) type set on the [SharedSpaceManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/SharedSpaceManager/)

#### StartSharedSpace<a href="#StartSharedSpace" class="hash-link" aria-label="Direct link to StartSharedSpace" title="Direct link to StartSharedSpace">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void StartSharedSpace(
      ISharedSpaceTrackingOptions trackingOptions,
        ISharedSpaceRoomOptions roomOptions
   )
```

</div>

</div>

Start tracking and prepare a Room.

    **Parameters**:

    `trackingOptions` - Tracking settings

    `roomOptions` - Room settings

#### PrepareRoom<a href="#PrepareRoom" class="hash-link" aria-label="Direct link to PrepareRoom" title="Direct link to PrepareRoom">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void PrepareRoom(ISharedSpaceRoomOptions roomOptions)
```

</div>

</div>

Prepare a Lightship networking Room for [Netcode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Netcode/)

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

    **Parameters**:

    `roomOptions` - Room settings

#### LeaveRoom<a href="#LeaveRoom" class="hash-link" aria-label="Direct link to LeaveRoom" title="Direct link to LeaveRoom">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void LeaveRoom()
```

</div>

</div>

Disconnect from the Lightship networking Room

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

#### CreateSharedOrigin<a href="#CreateSharedOrigin" class="hash-link" aria-label="Direct link to CreateSharedOrigin" title="Direct link to CreateSharedOrigin">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
SharedAROrigin CreateSharedOrigin(ARPersistentAnchor anchor)
```

</div>

</div>

Create a shared [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) origin object under the given persistent anchor.

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

    **Parameters**:

    `anchor` - A parent ARPersistentAnchor for the shared [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) origin

    **Returns:**

    [SharedAROrigin](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/SharedAROrigin/) object created

#### DestroySharedArOrigin<a href="#DestroySharedArOrigin" class="hash-link" aria-label="Direct link to DestroySharedArOrigin" title="Direct link to DestroySharedArOrigin">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void DestroySharedArOrigin()
```

</div>

</div>

Destroy the shared [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) origin

.. note::

This is an experimental feature, and is subject to breaking changes or deprecation without notice

</div>

</div>
