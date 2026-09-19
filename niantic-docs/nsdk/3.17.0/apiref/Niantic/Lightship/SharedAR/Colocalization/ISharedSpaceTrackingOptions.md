---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/ISharedSpaceTrackingOptions/
title: interface ISharedSpaceTrackingOptions
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# interface ISharedSpaceTrackingOptions

</div>

(Niantic.Lightship.SharedAR.Colocalization.ISharedSpaceTrackingOptions)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Tracking settings to use in Shared Space

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
interface ISharedSpaceTrackingOptions {
       // methods
   
     static ISharedSpaceTrackingOptions CreateVpsTrackingOptions(string payload);
     static ISharedSpaceTrackingOptions CreateVpsTrackingOptions(ARLocation location);
  
     static ISharedSpaceTrackingOptions CreateImageTrackingOptions(
          Texture2D targetImage,
          float widthInMeters
     );
    
     static ISharedSpaceTrackingOptions CreateMockTrackingOptions();
   };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Tracking settings to use in Shared Space

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### CreateVpsTrackingOptions<a href="#CreateVpsTrackingOptions" class="hash-link" aria-label="Direct link to CreateVpsTrackingOptions" title="Direct link to CreateVpsTrackingOptions">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static ISharedSpaceTrackingOptions CreateVpsTrackingOptions(string payload)
```

</div>

</div>

Vps tracking settings with Wayspot anchor payload string

    **Parameters**:

    `payload` - Wayspot anchor payload

    **Returns:**

    [ISharedSpaceTrackingOptions](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/ISharedSpaceTrackingOptions/) object using VPS

#### CreateVpsTrackingOptions<a href="#CreateVpsTrackingOptions" class="hash-link" aria-label="Direct link to CreateVpsTrackingOptions" title="Direct link to CreateVpsTrackingOptions">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static ISharedSpaceTrackingOptions CreateVpsTrackingOptions(ARLocation location)
```

</div>

</div>

Vps tracking settings with ARLocation

    **Parameters**:

    `location` - The target ARLocation object to track

    **Returns:**

    [ISharedSpaceTrackingOptions](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/ISharedSpaceTrackingOptions/) object using VPS

#### CreateImageTrackingOptions<a href="#CreateImageTrackingOptions" class="hash-link" aria-label="Direct link to CreateImageTrackingOptions" title="Direct link to CreateImageTrackingOptions">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static ISharedSpaceTrackingOptions CreateImageTrackingOptions(
      Texture2D targetImage,
      float widthInMeters
 )
```

</div>

</div>

Image tracking settings

    **Parameters**:

    `targetImage` - Target image to track as Texture2D

    `widthInMeters` - Physical width of the target image in meters

    **Returns:**

    [ISharedSpaceTrackingOptions](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/ISharedSpaceTrackingOptions/) object using image tracking

#### CreateMockTrackingOptions<a href="#CreateMockTrackingOptions" class="hash-link" aria-label="Direct link to CreateMockTrackingOptions" title="Direct link to CreateMockTrackingOptions">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static ISharedSpaceTrackingOptions CreateMockTrackingOptions()
```

</div>

</div>

Use mock tracking, which the tracking event happens immediately when calling StartSharedSpace()

    **Returns:**

    [ISharedSpaceTrackingOptions](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Colocalization/ISharedSpaceTrackingOptions/) object with mock tracking

</div>

</div>
