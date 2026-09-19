---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/IARScanQualityClassifier/
title: interface IARScanQualityClassifier
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# interface IARScanQualityClassifier

</div>

(Niantic.Lightship.AR.Scanning.IARScanQualityClassifier)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   interface IARScanQualityClassifier: IDisposable {
       // properties
    
     bool Running;
     float Progress;

       // methods
   
     bool Run(float framerate, string scanPath);
       void CancelCurrentRun();
      ScanQualityResult GetResult(string scanPath);
  };

    // direct descendants

    class ARScanQualityClassifier;
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### Running<a href="#Running" class="hash-link" aria-label="Direct link to Running" title="Direct link to Running">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool Running
```

</div>

</div>

Flag tells if a scan quality compute is running or not.

    **Returns:**

    Whether or not a run of quality computer is ongoing.

#### Progress<a href="#Progress" class="hash-link" aria-label="Direct link to Progress" title="Direct link to Progress">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float Progress
```

</div>

</div>

Progress of current quality compute, range is in percent between \[0, 100.0\].

    **Returns:**

    Percentage of existing run. 0 will be returned if not running a quality compute.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### Run<a href="#Run" class="hash-link" aria-label="Direct link to Run" title="Direct link to Run">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool Run(float framerate, string scanPath)
```

</div>

</div>

Start a run to compute the scan quality asynchoursly.

    **Parameters**:

    `scanPath` - Identifier of a scan.

    **Returns:**

    Whether or not the run will start, if ARScanQualityClassifier has already running, it will return false.

#### CancelCurrentRun<a href="#CancelCurrentRun" class="hash-link" aria-label="Direct link to CancelCurrentRun" title="Direct link to CancelCurrentRun">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void CancelCurrentRun()
```

</div>

</div>

Cancel current run. When the function returns, it is guaranteed the ARScanQualityClassifier is not running a scan. Do nothing if it is not running.

#### GetResult<a href="#GetResult" class="hash-link" aria-label="Direct link to GetResult" title="Direct link to GetResult">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ScanQualityResult GetResult(string scanPath)
```

</div>

</div>

Returns a [ScanQualityResult](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ScanQualityResult/) of current quality compute, Scores are in range of \[0, 1.0\]. Higher values means high scan quality. Categories are within ScanQualityCategory.

    **Returns:**

    A [ScanQualityResult](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ScanQualityResult/) with overall score and RejectionReasons. RejectionReasons will be empty if all scores pass the quality bar.

</div>

</div>
