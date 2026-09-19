---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Networking/INetworking/
title: interface INetworking
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# interface INetworking

</div>

(Niantic.Lightship.SharedAR.Networking.INetworking)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Low level networking interface used by the LightshipNetcodeTransport to talk to the Lightship relay servers. This interface allows you to relay a message directly to another user, halfing the latency of [Netcode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Netcode/) For Gameobject messages which have to be double-relayed by the "Host" client.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   interface INetworking: IDisposable {
        // properties
    
     NetworkState NetworkState;
      PeerID SelfPeerID;
      List<PeerID> PeerIDs;

       // events
    
     event NetworkEvent();
        event PeerAdded();
       event PeerRemoved();
     event DataReceived();

        // methods
   
     void SendData(List<PeerID> dest, uint tag, byte[] data);
     void Join();
      void Leave();
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Low level networking interface used by the LightshipNetcodeTransport to talk to the Lightship relay servers. This interface allows you to relay a message directly to another user, halfing the latency of [Netcode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Netcode/) For Gameobject messages which have to be double-relayed by the "Host" client.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### NetworkState<a href="#NetworkState" class="hash-link" aria-label="Direct link to NetworkState" title="Direct link to NetworkState">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
NetworkState NetworkState
```

</div>

</div>

Get the latest connection state

#### SelfPeerID<a href="#SelfPeerID" class="hash-link" aria-label="Direct link to SelfPeerID" title="Direct link to SelfPeerID">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
PeerID SelfPeerID
```

</div>

</div>

This client's [PeerID](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Networking/PeerID/).

#### PeerIDs<a href="#PeerIDs" class="hash-link" aria-label="Direct link to PeerIDs" title="Direct link to PeerIDs">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
List<PeerID> PeerIDs
```

</div>

</div>

Get all PeerIDs actively connected to the room.

### Events<a href="#events" class="hash-link" aria-label="Direct link to Events" title="Direct link to Events">​</a>

#### NetworkEvent<a href="#NetworkEvent" class="hash-link" aria-label="Direct link to NetworkEvent" title="Direct link to NetworkEvent">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
event NetworkEvent()
```

</div>

</div>

Event fired when the client's connection to the network changes state.

#### PeerAdded<a href="#PeerAdded" class="hash-link" aria-label="Direct link to PeerAdded" title="Direct link to PeerAdded">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
event PeerAdded()
```

</div>

</div>

Event fired when a peer joins the room. All other clients in the room are considered "Peers" by this API.

#### PeerRemoved<a href="#PeerRemoved" class="hash-link" aria-label="Direct link to PeerRemoved" title="Direct link to PeerRemoved">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
event PeerRemoved()
```

</div>

</div>

Event fired when a peer is removed, either from intentional action, timeout, or error. All other clients in the room are considered "Peers" by this API.

#### DataReceived<a href="#DataReceived" class="hash-link" aria-label="Direct link to DataReceived" title="Direct link to DataReceived">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
event DataReceived()
```

</div>

</div>

Data received from another peer in the room sent through the SendData method.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### SendData<a href="#SendData" class="hash-link" aria-label="Direct link to SendData" title="Direct link to SendData">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void SendData(List<PeerID> dest, uint tag, byte[] data)
```

</div>

</div>

Send data to the specified peers. Receiving peers will have a DataReceived event fired. This function is used by LightshipNetcodeTransport to send all [Netcode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Netcode/) messages.     **Parameters**:     `dest` - Destination of the message. Passing an empty list will broadcast the message to all other peers in the room.     `tag` - Data tag that peers will receive     `data` - Byte\[\] to send

#### Join<a href="#Join" class="hash-link" aria-label="Direct link to Join" title="Direct link to Join">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void Join()
```

</div>

</div>

Establish the network connection configured by the network's construction. Calling "Join" on the Room automatically calls this method, consider using the Room API instead!

#### Leave<a href="#Leave" class="hash-link" aria-label="Direct link to Leave" title="Direct link to Leave">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void Leave()
```

</div>

</div>

Disconnect from the room. Calling "Leave" on the Room automatically calls this method, consider using the Room API instead!

</div>

</div>
