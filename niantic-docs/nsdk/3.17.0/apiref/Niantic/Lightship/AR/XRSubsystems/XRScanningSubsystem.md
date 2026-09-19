---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRScanningSubsystem/
title: class XRScanningSubsystem
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class XRScanningSubsystem

</div>

(Niantic.Lightship.AR.XRSubsystems.XRScanningSubsystem)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Defines an interface for interacting with scanning functionality.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class XRScanningSubsystem: SubsystemWithProvider< XRScanningSubsystem, XRScanningSubsystemDescriptor, XRScanningSubsystem.Provider > {
  public:
   
     class Provider;

        // properties
    
     XRScanningConfiguration CurrentConfiguration;

       // methods
   
     XRScanningSubsystem();
     XRScanningState GetState();
 
     bool TryGetRaycastBuffer(
           out XRTextureDescriptor colorBufferDescriptor,
            out XRTextureDescriptor normalBufferDescriptor,
           out XRTextureDescriptor positionTextureDescriptor
       );
    
     void ComputeVoxels();
     bool TryGetVoxelBuffer(out XRScanningVoxelData voxelData);
       void DisposeVoxelBuffer(XRScanningVoxelData voxelData);
        float GetVoxelSize();
     string GetScanId();
       void SaveCurrentScan();
       void DiscardCurrentScan();
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Defines an interface for interacting with scanning functionality.

This abstract class should be implemented by an XR provider and instantiated using the SubsystemManager to enumerate the available [XRScanningSubsystemDescriptor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRScanningSubsystemDescriptor/) s.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### CurrentConfiguration<a href="#CurrentConfiguration" class="hash-link" aria-label="Direct link to CurrentConfiguration" title="Direct link to CurrentConfiguration">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
XRScanningConfiguration CurrentConfiguration
```

</div>

</div>

Get or set configuration with \<name\> [XRScanningConfiguration](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRScanningConfiguration/) \</name\>

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### XRScanningSubsystem<a href="#XRScanningSubsystem" class="hash-link" aria-label="Direct link to XRScanningSubsystem" title="Direct link to XRScanningSubsystem">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
XRScanningSubsystem()
```

</div>

</div>

Constructor. Do not invoke directly; use the SubsystemManager to enumerate the available [XRScanningSubsystemDescriptor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRScanningSubsystemDescriptor/) s and call Create on the desired descriptor.

#### GetState<a href="#GetState" class="hash-link" aria-label="Direct link to GetState" title="Direct link to GetState">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
XRScanningState GetState()
```

</div>

</div>

Get the current state of the scanning subsystem.

#### TryGetRaycastBuffer<a href="#TryGetRaycastBuffer" class="hash-link" aria-label="Direct link to TryGetRaycastBuffer" title="Direct link to TryGetRaycastBuffer">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryGetRaycastBuffer(
       out XRTextureDescriptor colorBufferDescriptor,
        out XRTextureDescriptor normalBufferDescriptor,
       out XRTextureDescriptor positionTextureDescriptor
   )
```

</div>

</div>

Get the latest raycast textures.

#### ComputeVoxels<a href="#ComputeVoxels" class="hash-link" aria-label="Direct link to ComputeVoxels" title="Direct link to ComputeVoxels">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void ComputeVoxels()
```

</div>

</div>

Request a voxel buffer to be computed. This is an async operation that takes some time. Obtain the result with TryGetVoxels. "enableVoxels" must be set to true on the [XRScanningConfiguration](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRScanningConfiguration/)

#### TryGetVoxelBuffer<a href="#TryGetVoxelBuffer" class="hash-link" aria-label="Direct link to TryGetVoxelBuffer" title="Direct link to TryGetVoxelBuffer">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryGetVoxelBuffer(out XRScanningVoxelData voxelData)
```

</div>

</div>

Get latest computed voxel buffer. This then must be later disposed with [DisposeVoxelBuffer](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRScanningSubsystem/#DisposeVoxelBuffer)

#### DisposeVoxelBuffer<a href="#DisposeVoxelBuffer" class="hash-link" aria-label="Direct link to DisposeVoxelBuffer" title="Direct link to DisposeVoxelBuffer">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void DisposeVoxelBuffer(XRScanningVoxelData voxelData)
```

</div>

</div>

Dispose a voxel buffer previously obtained from [TryGetVoxelBuffer](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRScanningSubsystem/#TryGetVoxelBuffer)

#### GetVoxelSize<a href="#GetVoxelSize" class="hash-link" aria-label="Direct link to GetVoxelSize" title="Direct link to GetVoxelSize">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float GetVoxelSize()
```

</div>

</div>

Get the current voxel size in meters.

    **Returns:**

    The current voxel size in meters, or 0 if voxel visualization is not enabled.

#### GetScanId<a href="#GetScanId" class="hash-link" aria-label="Direct link to GetScanId" title="Direct link to GetScanId">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
string GetScanId()
```

</div>

</div>

Get the current scan's ID.

#### SaveCurrentScan<a href="#SaveCurrentScan" class="hash-link" aria-label="Direct link to SaveCurrentScan" title="Direct link to SaveCurrentScan">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void SaveCurrentScan()
```

</div>

</div>

Save the current scan. Recording will stop after save. ScanID will be reset.

#### DiscardCurrentScan<a href="#DiscardCurrentScan" class="hash-link" aria-label="Direct link to DiscardCurrentScan" title="Direct link to DiscardCurrentScan">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void DiscardCurrentScan()
```

</div>

</div>

Discards the current scan. Anything previously saved will be deleted. Recording will stop after discard. ScanID will be reset.

</div>

</div>
