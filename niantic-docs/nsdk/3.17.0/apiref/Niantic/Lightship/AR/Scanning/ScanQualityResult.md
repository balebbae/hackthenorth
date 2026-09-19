---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ScanQualityResult/
title: class ScanQualityResult
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class ScanQualityResult

</div>

(Niantic.Lightship.AR.Scanning.ScanQualityResult)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Scan Quality Result.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class ScanQualityResult {
 public:
       // properties
    
     float ScanQualityScore;
       List<ScanningSqcScores> RejectionReasons;
   };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Scan Quality Result.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### ScanQualityScore<a href="#ScanQualityScore" class="hash-link" aria-label="Direct link to ScanQualityScore" title="Direct link to ScanQualityScore">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float ScanQualityScore
```

</div>

</div>

An overall score of the scan's quality. Range is 0-1, higher is better.

#### RejectionReasons<a href="#RejectionReasons" class="hash-link" aria-label="Direct link to RejectionReasons" title="Direct link to RejectionReasons">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
List<ScanningSqcScores> RejectionReasons
```

</div>

</div>

Returns a list of problems with the scan that may contribute to it receiving a lower scan quality score. This list will be empty for high-quality scans.

</div>

</div>
