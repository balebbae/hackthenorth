---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorLocalizationStatus/
title: struct XRPersistentAnchorLocalizationStatus
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct XRPersistentAnchorLocalizationStatus

</div>

(Niantic.Lightship.AR.XRSubsystems.XRPersistentAnchorLocalizationStatus)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Reports the result of a localization request.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
struct XRPersistentAnchorLocalizationStatus {
     // fields
    
      Guid NodeId;
        LocalizationStatus Status;
      float LocalizationConfidence;
         UInt64 FrameId;
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Reports the result of a localization request.

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### NodeId<a href="#NodeId" class="hash-link" aria-label="Direct link to NodeId" title="Direct link to NodeId">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Guid NodeId
```

</div>

</div>

NodeId that this request was targeting

#### Status<a href="#Status" class="hash-link" aria-label="Direct link to Status" title="Direct link to Status">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
LocalizationStatus Status
```

</div>

</div>

Status of the localization request

#### LocalizationConfidence<a href="#LocalizationConfidence" class="hash-link" aria-label="Direct link to LocalizationConfidence" title="Direct link to LocalizationConfidence">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float LocalizationConfidence
```

</div>

</div>

Confidence of the localization.

.. note::

: Different algorithms may have different confidence scales. Confidences are a general guideline for now, until confidence scales are normalized, or the algorithm surfaced

#### FrameId<a href="#FrameId" class="hash-link" aria-label="Direct link to FrameId" title="Direct link to FrameId">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
UInt64 FrameId
```

</div>

</div>

Frame Id corresponding to frame sent used in Localization

</div>

</div>
