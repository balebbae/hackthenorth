---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Netcode/LightshipNetcodeTransport/NetcodeSessionStats/
title: struct NetcodeSessionStats
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct NetcodeSessionStats

</div>

(Niantic.Lightship.SharedAR.Netcode.LightshipNetcodeTransport.NetcodeSessionStats)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Session stats describing network usage.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
struct NetcodeSessionStats {
      // fields
    
      ulong TotalBytesSent;
         ulong TotalBytesReceived;
         uint TotalMessagesSent;
       uint TotalMessagesReceived;
       int PeerCount;
        float Timestamp;

     // methods
   
     static void GetPerSecondStats(
            NetcodeSessionStats stats1,
         NetcodeSessionStats stats2,
         out float bytesSentPerSec,
          out float messagesSentPerSec,
           out float bytesReceivedPerSec,
          out float messagesReceivedPerSec
      );
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Session stats describing network usage.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### GetPerSecondStats<a href="#GetPerSecondStats" class="hash-link" aria-label="Direct link to GetPerSecondStats" title="Direct link to GetPerSecondStats">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static void GetPerSecondStats(
        NetcodeSessionStats stats1,
     NetcodeSessionStats stats2,
     out float bytesSentPerSec,
      out float messagesSentPerSec,
       out float bytesReceivedPerSec,
      out float messagesReceivedPerSec
  )
```

</div>

</div>

Compare two NetcodeSessionStats to calculate bandwidth usage. Order is determined automatically.

    **Parameters**:

    `stats1` - First stat snapshot.

    `stats2` - Second stat snapshot.

    `bytesSentPerSec` - Outgoing bytes per second.

    `messagesSentPerSec` - Outgoing messages per second.

    `bytesReceivedPerSec` - Incoming bytes per second.

    `messagesReceivedPerSec` - Incoming messages per second.

</div>

</div>
