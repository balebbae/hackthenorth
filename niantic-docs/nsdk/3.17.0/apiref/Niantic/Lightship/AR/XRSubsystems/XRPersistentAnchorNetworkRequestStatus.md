---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorNetworkRequestStatus/
title: struct XRPersistentAnchorNetworkRequestStatus
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct XRPersistentAnchorNetworkRequestStatus

</div>

(Niantic.Lightship.AR.XRSubsystems.XRPersistentAnchorNetworkRequestStatus)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Diagnostic information about a persistent anchor network request

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
struct XRPersistentAnchorNetworkRequestStatus {
       // fields
    
      Guid RequestId;
         RequestStatus Status;
       RequestType Type;
       ErrorCode Error;
        ulong StartTimeMs;
        ulong EndTimeMs;
      UInt64 FrameId;
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Diagnostic information about a persistent anchor network request

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### RequestId<a href="#RequestId" class="hash-link" aria-label="Direct link to RequestId" title="Direct link to RequestId">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Guid RequestId
```

</div>

</div>

Id of the request

#### Status<a href="#Status" class="hash-link" aria-label="Direct link to Status" title="Direct link to Status">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
RequestStatus Status
```

</div>

</div>

Status of the request

#### Type<a href="#Type" class="hash-link" aria-label="Direct link to Type" title="Direct link to Type">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
RequestType Type
```

</div>

</div>

Type of request sent

#### Error<a href="#Error" class="hash-link" aria-label="Direct link to Error" title="Direct link to Error">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ErrorCode Error
```

</div>

</div>

Error code of the request, if any

#### StartTimeMs<a href="#StartTimeMs" class="hash-link" aria-label="Direct link to StartTimeMs" title="Direct link to StartTimeMs">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ulong StartTimeMs
```

</div>

</div>

Time in ms that the request was sent Only comparable to EndTimeMs

#### EndTimeMs<a href="#EndTimeMs" class="hash-link" aria-label="Direct link to EndTimeMs" title="Direct link to EndTimeMs">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ulong EndTimeMs
```

</div>

</div>

Time in ms that the response was received Only comparable to StartTimeMs

#### FrameId<a href="#FrameId" class="hash-link" aria-label="Direct link to FrameId" title="Direct link to FrameId">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
UInt64 FrameId
```

</div>

</div>

Frame Id corresponding to frame sent in NetworkRequest, if available

</div>

</div>
