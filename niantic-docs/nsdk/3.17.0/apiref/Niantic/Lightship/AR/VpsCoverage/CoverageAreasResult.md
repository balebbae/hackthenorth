---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/CoverageAreasResult/
title: class CoverageAreasResult
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class CoverageAreasResult

</div>

(Niantic.Lightship.AR.VpsCoverage.CoverageAreasResult)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Received result from server request for CoverageAreas.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class CoverageAreasResult {
   public:
       // properties
    
     ResponseStatus Status;
      CoverageArea[] Areas;
   };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Received result from server request for CoverageAreas.

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

#### Areas<a href="#Areas" class="hash-link" aria-label="Direct link to Areas" title="Direct link to Areas">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
CoverageArea[] Areas
```

</div>

</div>

CoverageAreas found from the request.

</div>

</div>
