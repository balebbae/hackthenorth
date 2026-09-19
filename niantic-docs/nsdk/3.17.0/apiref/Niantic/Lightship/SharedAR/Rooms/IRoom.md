---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Rooms/IRoom/
title: interface IRoom
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# interface IRoom

</div>

(Niantic.Lightship.SharedAR.Rooms.IRoom)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

A room is an entity to connect multiple peers through server relayed network. The [IRoom](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Rooms/IRoom/) provides access to properties and network connectivity of the room.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   interface IRoom: IDisposable {
      // properties
    
     RoomParams RoomParams;
      INetworking Networking;
     IDatastore Datastore;

       // methods
   
     void Initialize();
        void Join();
      void Leave();
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

A room is an entity to connect multiple peers through server relayed network. The [IRoom](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Rooms/IRoom/) provides access to properties and network connectivity of the room.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### RoomParams<a href="#RoomParams" class="hash-link" aria-label="Direct link to RoomParams" title="Direct link to RoomParams">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
RoomParams RoomParams
```

</div>

</div>

Room properties

#### Networking<a href="#Networking" class="hash-link" aria-label="Direct link to Networking" title="Direct link to Networking">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
INetworking Networking
```

</div>

</div>

Get INetworking object to send/receive data, as well as listening to networking events

#### Datastore<a href="#Datastore" class="hash-link" aria-label="Direct link to Datastore" title="Direct link to Datastore">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
IDatastore Datastore
```

</div>

</div>

Get IDatastore object to access realtime key-value store attached to the room

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### Initialize<a href="#Initialize" class="hash-link" aria-label="Direct link to Initialize" title="Direct link to Initialize">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void Initialize()
```

</div>

</div>

Initialize networking connectivity to connect to the room on the server. INetworking should be available after [Initialize()](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Rooms/IRoom/#Initialize) is called.

#### Join<a href="#Join" class="hash-link" aria-label="Direct link to Join" title="Direct link to Join">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void Join()
```

</div>

</div>

Join to the room. After joined to the room, data can be sent and/or received via INetworking.

#### Leave<a href="#Leave" class="hash-link" aria-label="Direct link to Leave" title="Direct link to Leave">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void Leave()
```

</div>

</div>

Leave from the room. Disconnect from the server and no longer can send/receive data afterwards.

</div>

</div>
