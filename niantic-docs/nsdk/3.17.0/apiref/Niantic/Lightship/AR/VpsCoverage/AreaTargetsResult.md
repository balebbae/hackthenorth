---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/AreaTargetsResult/
title: class AreaTargetsResult
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class AreaTargetsResult

</div>

(Niantic.Lightship.AR.VpsCoverage.AreaTargetsResult)

Received result from server request for CoverageAreas and LocalizationTargets together.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class AreaTargetsResult {
 public:
       // properties
    
     LatLng QueryLocation;
       int QueryRadius;
      ResponseStatus Status;
      List<AreaTarget> AreaTargets;

       // methods
   
     AreaTargetsResult(
           LatLng queryLocation,
           int queryRadius,
          ResponseStatus status,
          CoverageAreasResult areasResult,
            LocalizationTargetsResult targetsResult,
            LocalizationTarget[] privateScanLocalizationTargets
       );
    };
```

</div>

</div>

</div>

</div>
