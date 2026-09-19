---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Networking/NetworkEventArgs/
title: struct NetworkEventArgs
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct NetworkEventArgs

</div>

(Niantic.Lightship.SharedAR.Networking.NetworkEventArgs)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Event args fired from INetworking.NetworkEvent.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
struct NetworkEventArgs {
     // properties
    
     NetworkEvents networkEvent;
     UInt32 errorCode;

       // methods
   
     NetworkEventArgs(NetworkEvents netEvent, UInt32 errCode);
  };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Event args fired from INetworking.NetworkEvent.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### networkEvent<a href="#networkEvent" class="hash-link" aria-label="Direct link to networkEvent" title="Direct link to networkEvent">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
NetworkEvents networkEvent
```

</div>

</div>

Type of networking event being fired.

#### errorCode<a href="#errorCode" class="hash-link" aria-label="Direct link to errorCode" title="Direct link to errorCode">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
UInt32 errorCode
```

</div>

</div>

Error code. Only valid in Disconnected and ConnectionError

</div>

</div>
