---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRScanningSubsystem/Provider/
title: class Provider
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class Provider

</div>

(Niantic.Lightship.AR.XRSubsystems.XRScanningSubsystem.Provider)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

An abstract class to be implemented by providers of this subsystem.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class Provider: SubsystemProvider< XRScanningSubsystem > {
    public:
       // properties
    
     XRScanningConfiguration CurrentConfiguration;

       // methods
   
     virtual string GetScanId();
     virtual XRScanningState GetState();
   
     virtual bool TryGetRaycastBuffer(
         out XRTextureDescriptor raycastBufferDescriptor,
          out XRTextureDescriptor raycastNormalBufferDescriptor,
            out XRTextureDescriptor raycastPositionAndConfidenceDescriptor
      );
    
     virtual void SaveCurrentScan();
     virtual void DiscardCurrentScan();
      virtual void ComputeVoxels();
       virtual bool TryGetVoxelBuffer(out XRScanningVoxelData voxelData);
     virtual void DisposeVoxelBuffer(XRScanningVoxelData voxelData);
      virtual float GetVoxelSize();
   };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

An abstract class to be implemented by providers of this subsystem.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### GetScanId<a href="#GetScanId" class="hash-link" aria-label="Direct link to GetScanId" title="Direct link to GetScanId">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual string GetScanId()
```

</div>

</div>

Get the current scan's ID.

</div>

</div>
