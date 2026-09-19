---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Rooms/RoomParams/
title: struct RoomParams
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct RoomParams

</div>

(Niantic.Lightship.SharedAR.Rooms.RoomParams)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The [RoomParams](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Rooms/RoomParams/) struct contains properties of the room

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
struct RoomParams {
       // properties
    
     string RoomID;
        RoomVisibility Visibility;
      int Capacity;
     string Name;
      string Description;
       string Passcode;

      // methods
   
     RoomParams(
          int capacity,
         string name = "",
            string description = "",
         string passcode = "",
            RoomVisibility visibility = RoomVisibility.Public
        );
    
     RoomParams(string id, RoomVisibility visibility = RoomVisibility.Public);
   };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The [RoomParams](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Rooms/RoomParams/) struct contains properties of the room

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### RoomID<a href="#RoomID" class="hash-link" aria-label="Direct link to RoomID" title="Direct link to RoomID">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
string RoomID
```

</div>

</div>

Room ID of the room. This is only set by RoomManagementService.

#### Visibility<a href="#Visibility" class="hash-link" aria-label="Direct link to Visibility" title="Direct link to Visibility">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
RoomVisibility Visibility
```

</div>

</div>

Visibility of the room

#### Capacity<a href="#Capacity" class="hash-link" aria-label="Direct link to Capacity" title="Direct link to Capacity">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
int Capacity
```

</div>

</div>

Capacity of the room. Value should be between 2 to 32 peers.

#### Name<a href="#Name" class="hash-link" aria-label="Direct link to Name" title="Direct link to Name">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
string Name
```

</div>

</div>

Name of the room. Name does not need to be unique between rooms

#### Description<a href="#Description" class="hash-link" aria-label="Direct link to Description" title="Direct link to Description">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
string Description
```

</div>

</div>

Description of the room

#### Passcode<a href="#Passcode" class="hash-link" aria-label="Direct link to Passcode" title="Direct link to Passcode">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
string Passcode
```

</div>

</div>

Passcode to access the room. Required when visibility is set to private.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### RoomParams<a href="#RoomParams" class="hash-link" aria-label="Direct link to RoomParams" title="Direct link to RoomParams">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
RoomParams(
      int capacity,
     string name = "",
        string description = "",
     string passcode = "",
        RoomVisibility visibility = RoomVisibility.Public
    )
```

</div>

</div>

Constructor

    **Parameters**:

    `capacity` - Capacity of the room. Value should be between 2 to 32 peers.

    `name` - Name of the room

    `description` - Description of the room

    `passcode` - Passcode of the room

    `visibility` - Visibility of the room

#### RoomParams<a href="#RoomParams" class="hash-link" aria-label="Direct link to RoomParams" title="Direct link to RoomParams">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
RoomParams(string id, RoomVisibility visibility = RoomVisibility.Public)
```

</div>

</div>

Constructor for construction through ID. Typically used in conjunction with Room.GetOrCreateRoomAsync which returns the necessary string ID.

    **Parameters**:

    `id` - The specific RoomID GUID from the backend

    `visibility` - Visibility of the room

</div>

</div>
