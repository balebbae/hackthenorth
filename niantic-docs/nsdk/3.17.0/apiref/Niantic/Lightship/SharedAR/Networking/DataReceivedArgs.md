---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Networking/DataReceivedArgs/
title: struct DataReceivedArgs
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct DataReceivedArgs

</div>

(Niantic.Lightship.SharedAR.Networking.DataReceivedArgs)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Event args fired from INetworking.DataReceived.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
struct DataReceivedArgs {
     // properties
    
     PeerID PeerID;
      uint Tag;
     int DataLength;

       // methods
   
     DataReceivedArgs(PeerID peerID, uint tag, byte[] data);
       MemoryStream CreateDataReader();
        byte[] CopyData();
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Event args fired from INetworking.DataReceived.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### PeerID<a href="#PeerID" class="hash-link" aria-label="Direct link to PeerID" title="Direct link to PeerID">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
PeerID PeerID
```

</div>

</div>

Id of the peer that is sending the data.

#### Tag<a href="#Tag" class="hash-link" aria-label="Direct link to Tag" title="Direct link to Tag">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
uint Tag
```

</div>

</div>

The tag that catagorizes the sent message.

#### DataLength<a href="#DataLength" class="hash-link" aria-label="Direct link to DataLength" title="Direct link to DataLength">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
int DataLength
```

</div>

</div>

The length of the message.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### CreateDataReader<a href="#CreateDataReader" class="hash-link" aria-label="Direct link to CreateDataReader" title="Direct link to CreateDataReader">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
MemoryStream CreateDataReader()
```

</div>

</div>

Create a MemoryStream to read the message.     **Returns:**     A MemoryStream pointed at the message

#### CopyData<a href="#CopyData" class="hash-link" aria-label="Direct link to CopyData" title="Direct link to CopyData">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
byte[] CopyData()
```

</div>

</div>

Make a full copy of the message.     **Returns:**     A copy of the message

</div>

</div>
