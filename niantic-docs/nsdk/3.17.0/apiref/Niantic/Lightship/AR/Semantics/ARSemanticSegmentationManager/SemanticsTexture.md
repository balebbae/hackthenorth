---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Semantics/ARSemanticSegmentationManager/SemanticsTexture/
title: struct SemanticsTexture
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct SemanticsTexture

</div>

(Niantic.Lightship.AR.Semantics.ARSemanticSegmentationManager.SemanticsTexture)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

A type that holds a semantic segmentation texture along with its associated metadata for warping.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
struct SemanticsTexture {
     // fields
    
      LightshipExternalTexture ExternalTexture;
       Matrix4x4 SamplerMatrix;
        XRCameraParams CameraParams;
        readonly bool IsOutOfDate => LastUpdatedFrameId != Time.frameCount;
      int LastUpdatedFrameId;

      // methods
   
     void Reset();
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

A type that holds a semantic segmentation texture along with its associated metadata for warping.

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### IsOutOfDate<a href="#IsOutOfDate" class="hash-link" aria-label="Direct link to IsOutOfDate" title="Direct link to IsOutOfDate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly bool IsOutOfDate => LastUpdatedFrameId != Time.frameCount
```

</div>

</div>

True if the texture has not been updated this frame.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### Reset<a href="#Reset" class="hash-link" aria-label="Direct link to Reset" title="Direct link to Reset">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void Reset()
```

</div>

</div>

Disposes of the external texture and resets metadata.

</div>

</div>
