---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRScanningConfiguration/
title: class XRScanningConfiguration
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class XRScanningConfiguration

</div>

(Niantic.Lightship.AR.XRSubsystems.XRScanningConfiguration)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Configuration for scanning.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class XRScanningConfiguration {
   public:
       // properties
    
     int Framerate;
        bool RaycasterVisualizationEnabled;
       Vector2 RaycasterVisualizationResolution;
       float NearDepth;
      float FarDepth;
       bool VoxelVisualizationEnabled;
       float VoxelSize;
      bool UseEstimatedDepth;
       bool FullResolutionEnabled;
       int FullResolutionFramerate;
      string ScanBasePath;
      string? ScanTargetId;

     // methods
   
     XRScanningConfiguration();
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Configuration for scanning.

    **See also**:

    [XRScanningConfiguration](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRScanningConfiguration/)

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### RaycasterVisualizationResolution<a href="#RaycasterVisualizationResolution" class="hash-link" aria-label="Direct link to RaycasterVisualizationResolution" title="Direct link to RaycasterVisualizationResolution">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Vector2 RaycasterVisualizationResolution
```

</div>

</div>

The resolution of the raycast visualization's output images. The output quality is bound by both this resolution as well as the quality of the underlying 3D reconstruction data. On devices without native depth support, the underlying data is unlikely to be good enough to support resolution larger than 256x144.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### XRScanningConfiguration<a href="#XRScanningConfiguration" class="hash-link" aria-label="Direct link to XRScanningConfiguration" title="Direct link to XRScanningConfiguration">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
XRScanningConfiguration()
```

</div>

</div>

Default constructor for the [XRScanningConfiguration](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRScanningConfiguration/).

</div>

</div>
