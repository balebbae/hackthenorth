---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Netcode/LightshipNetcodeTransport/
title: class LightshipNetcodeTransport
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class LightshipNetcodeTransport

</div>

(Niantic.Lightship.SharedAR.Netcode.LightshipNetcodeTransport)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Lightship's [Netcode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Netcode/) for GameObjects compatibility layer. Implemented using the Room and INetworking apis.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class LightshipNetcodeTransport: NetworkTransport {
 public:
   
     struct CachedEvent;
        struct NetcodeSessionStats;

        // properties
    
     override ulong ServerClientId;

      // methods
   
     NetcodeSessionStats GetNetcodeSessionStats();
   
     override void Send(
           ulong clientId,
           ArraySegment<byte> data,
          NetworkDelivery delivery = NetworkDelivery.Reliable
      );
    
     override NetworkEvent PollEvent(
            out ulong clientId,
         out ArraySegment<byte> payload,
         out float receiveTime
     );
    
     void SetRoom(IRoom room);
      override bool StartClient();
        override bool StartServer();
        override void DisconnectRemoteClient(ulong clientId);
      override void DisconnectLocalClient();
      override ulong GetCurrentRtt(ulong clientId);
      override void Shutdown();
       override void Initialize(NetworkManager manager);
        uint GetLastNetworkError();
   };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Lightship's [Netcode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Netcode/) for GameObjects compatibility layer. Implemented using the Room and INetworking apis.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### ServerClientId<a href="#ServerClientId" class="hash-link" aria-label="Direct link to ServerClientId" title="Direct link to ServerClientId">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override ulong ServerClientId
```

</div>

</div>

A constant netcode clientId that represents the server When this value is found in methods such as Send, it should be treated as a placeholder that means the server

    **Parameters**:

    `networkManager` - NetworkManager managing the netcode session

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### GetNetcodeSessionStats<a href="#GetNetcodeSessionStats" class="hash-link" aria-label="Direct link to GetNetcodeSessionStats" title="Direct link to GetNetcodeSessionStats">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
NetcodeSessionStats GetNetcodeSessionStats()
```

</div>

</div>

Poll the current stats of the active netcode session.

#### Send<a href="#Send" class="hash-link" aria-label="Direct link to Send" title="Direct link to Send">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override void Send(
       ulong clientId,
       ArraySegment<byte> data,
      NetworkDelivery delivery = NetworkDelivery.Reliable
  )
```

</div>

</div>

Send a payload to the specified clientId, data and networkDelivery.

    **Parameters**:

    `clientId` - The clientId to send to

    `payload` - The data to send

    `networkDelivery` - The delivery type (QoS) to send data with

#### PollEvent<a href="#PollEvent" class="hash-link" aria-label="Direct link to PollEvent" title="Direct link to PollEvent">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override NetworkEvent PollEvent(
        out ulong clientId,
     out ArraySegment<byte> payload,
     out float receiveTime
 )
```

</div>

</div>

Polls for incoming events, with an extra output parameter to report the precise time the event was received.

    **Parameters**:

    `clientId` - The clientId this event is for

    `payload` - The incoming data payload

    `receiveTime` - The time the event was received, as reported by Time.realtimeSinceStartup.

    **Returns:**

    Returns the event type

#### SetRoom<a href="#SetRoom" class="hash-link" aria-label="Direct link to SetRoom" title="Direct link to SetRoom">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void SetRoom(IRoom room)
```

</div>

</div>

Set the Lightship Room that we want to use [Netcode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Netcode/) for Gameobjects in. Set this before calling "StartClient" or "StartServer".

#### StartClient<a href="#StartClient" class="hash-link" aria-label="Direct link to StartClient" title="Direct link to StartClient">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override bool StartClient()
```

</div>

</div>

Connects client to the server

    **Returns:**

    Returns success or failure

#### StartServer<a href="#StartServer" class="hash-link" aria-label="Direct link to StartServer" title="Direct link to StartServer">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override bool StartServer()
```

</div>

</div>

Starts to listening for incoming clients

    **Returns:**

    Returns success or failure

#### DisconnectRemoteClient<a href="#DisconnectRemoteClient" class="hash-link" aria-label="Direct link to DisconnectRemoteClient" title="Direct link to DisconnectRemoteClient">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override void DisconnectRemoteClient(ulong clientId)
```

</div>

</div>

Disconnects a client from the server

    **Parameters**:

    `clientId` - The clientId to disconnect

#### DisconnectLocalClient<a href="#DisconnectLocalClient" class="hash-link" aria-label="Direct link to DisconnectLocalClient" title="Direct link to DisconnectLocalClient">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override void DisconnectLocalClient()
```

</div>

</div>

Disconnects the local client from the server

#### GetCurrentRtt<a href="#GetCurrentRtt" class="hash-link" aria-label="Direct link to GetCurrentRtt" title="Direct link to GetCurrentRtt">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override ulong GetCurrentRtt(ulong clientId)
```

</div>

</div>

Gets the round trip time for a specific client. This method is not implemented for Lightship

    **Parameters**:

    `clientId` - The clientId to get the RTT from

    **Returns:**

    Returns 0 always

#### Shutdown<a href="#Shutdown" class="hash-link" aria-label="Direct link to Shutdown" title="Direct link to Shutdown">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override void Shutdown()
```

</div>

</div>

Shuts down the transport

#### Initialize<a href="#Initialize" class="hash-link" aria-label="Direct link to Initialize" title="Direct link to Initialize">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override void Initialize(NetworkManager manager)
```

</div>

</div>

Initializes the transport. Automatically called by [Netcode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Netcode/).

    **Parameters**:

    `networkManager` - NetworkManager managing the netcode session

#### GetLastNetworkError<a href="#GetLastNetworkError" class="hash-link" aria-label="Direct link to GetLastNetworkError" title="Direct link to GetLastNetworkError">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
uint GetLastNetworkError()
```

</div>

</div>

Get error code from the last network error. If no error, returns 0. Error codes are defined as const in Niantic.Lightship.SharedAR.Networking.NetworkEventErrorCode

    **Returns:**

    Error code

</div>

</div>
