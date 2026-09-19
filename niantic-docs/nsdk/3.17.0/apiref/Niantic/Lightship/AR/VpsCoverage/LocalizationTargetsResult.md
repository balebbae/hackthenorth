---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/LocalizationTargetsResult/
title: class LocalizationTargetsResult
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class LocalizationTargetsResult

</div>

(Niantic.Lightship.AR.VpsCoverage.LocalizationTargetsResult)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Received result from server request for LocalizationTargets.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class LocalizationTargetsResult {
 public:
       // properties
    
     ResponseStatus Status;
      IReadOnlyDictionary<string, LocalizationTarget> ActivationTargets;
  };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Received result from server request for LocalizationTargets.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### Status<a href="#Status" class="hash-link" aria-label="Direct link to Status" title="Direct link to Status">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ResponseStatus Status
```

</div>

</div>

Response status of server request.

#### ActivationTargets<a href="#ActivationTargets" class="hash-link" aria-label="Direct link to ActivationTargets" title="Direct link to ActivationTargets">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
IReadOnlyDictionary<string, LocalizationTarget> ActivationTargets
```

</div>

</div>

Found LocalizationTargets found for the request as a dictionary with their identifier as keys.

</div>

</div>
