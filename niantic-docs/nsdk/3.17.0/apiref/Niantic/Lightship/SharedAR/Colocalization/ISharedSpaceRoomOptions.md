---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/ISharedSpaceRoomOptions/
title: interface ISharedSpaceRoomOptions
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# interface ISharedSpaceRoomOptions

</div>

(Niantic.Lightship.SharedAR.Colocalization.ISharedSpaceRoomOptions)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Room settings to use in Shared Space

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
interface ISharedSpaceRoomOptions {
       // properties
    
     IRoom Room;

     // methods
   
     static ISharedSpaceRoomOptions CreateVpsRoomOptions(
            ISharedSpaceTrackingOptions trackingVpsLocation,
            string roomTag = "",
         int capacity = 10,
         string description = "",
         bool useNetcode = true
     );
    
     static ISharedSpaceRoomOptions CreateLightshipRoomOptions(
          string name,
          int capacity = 10,
         string description = "",
         bool useNetcode = true
     );
    
     static ISharedSpaceRoomOptions CreateCustomRoomOptions();
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Room settings to use in Shared Space

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### CreateVpsRoomOptions<a href="#CreateVpsRoomOptions" class="hash-link" aria-label="Direct link to CreateVpsRoomOptions" title="Direct link to CreateVpsRoomOptions">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static ISharedSpaceRoomOptions CreateVpsRoomOptions(
        ISharedSpaceTrackingOptions trackingVpsLocation,
        string roomTag = "",
     int capacity = 10,
     string description = "",
     bool useNetcode = true
 )
```

</div>

</div>

Use to create [ISharedSpaceRoomOptions](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/ISharedSpaceRoomOptions/) when a Lightship Room is associated to a Wayspot

    **Parameters**:

    `trackingVpsLocation` - VPS tracking options

    `roomTag` - A prefix to the room name

    `capacity` - Capacity of the room

    `description` - Description of the room

    `useNetcode` - If true, a Room is assigned to LightshipNetcodeTransport

    **Returns:**

    Returns [ISharedSpaceRoomOptions](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/ISharedSpaceRoomOptions/) object

#### CreateLightshipRoomOptions<a href="#CreateLightshipRoomOptions" class="hash-link" aria-label="Direct link to CreateLightshipRoomOptions" title="Direct link to CreateLightshipRoomOptions">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static ISharedSpaceRoomOptions CreateLightshipRoomOptions(
      string name,
      int capacity = 10,
     string description = "",
     bool useNetcode = true
 )
```

</div>

</div>

Use to create [ISharedSpaceRoomOptions](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/ISharedSpaceRoomOptions/) for mock tracking or image target tracking, which requires to give a custom Room name

    **Parameters**:

    `name` - Name of the room

    `capacity` - Capacity of the room

    `description` - Description of the room

    `useNetcode` - If true, a Room is assigned to LightshipNetcodeTransport

    **Returns:**

    Returns [ISharedSpaceRoomOptions](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/ISharedSpaceRoomOptions/) object

#### CreateCustomRoomOptions<a href="#CreateCustomRoomOptions" class="hash-link" aria-label="Direct link to CreateCustomRoomOptions" title="Direct link to CreateCustomRoomOptions">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static ISharedSpaceRoomOptions CreateCustomRoomOptions()
```

</div>

</div>

Use when managing [Rooms](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Rooms/) by application or using custom networking

    **Returns:**

    Returns [ISharedSpaceRoomOptions](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/ISharedSpaceRoomOptions/) object

</div>

</div>
