---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Meshing/LightshipMeshingExtension/
title: class LightshipMeshingExtension
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class LightshipMeshingExtension

</div>

(Niantic.Lightship.AR.Meshing.LightshipMeshingExtension)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

This component allows configuration of the additional functionality available in Lightship's implementation of XRMeshingSubsystem.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class LightshipMeshingExtension: MonoBehaviour {
    public:
       // properties
    
     int TargetFrameRate;
      bool FuseKeyframesOnly;
       float MaximumIntegrationDistance;
     float VoxelSize;
      float MeshBlockSize;
      float MeshCullingDistance;
        bool EnableMeshDecimation;
        bool EnableDistanceBasedVolumetricCleanup;
        bool IsMeshFilteringEnabled;
      bool IsFilteringAllowListEnabled;
     List<string> AllowList;
       bool IsFilteringBlockListEnabled;
     List<string> BlockList;
       bool EnableLevelsOfDetail;
        int LevelsOfDetail;

       // methods
   
     void Configure();
     void Update();
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

This component allows configuration of the additional functionality available in Lightship's implementation of XRMeshingSubsystem.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### TargetFrameRate<a href="#TargetFrameRate" class="hash-link" aria-label="Direct link to TargetFrameRate" title="Direct link to TargetFrameRate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
int TargetFrameRate
```

</div>

</div>

Get or set the frame rate that meshing will aim to run at.

#### FuseKeyframesOnly<a href="#FuseKeyframesOnly" class="hash-link" aria-label="Direct link to FuseKeyframesOnly" title="Direct link to FuseKeyframesOnly">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool FuseKeyframesOnly
```

</div>

</div>

Get or set whether only depth keyframes will be fused into the mesh.

#### MaximumIntegrationDistance<a href="#MaximumIntegrationDistance" class="hash-link" aria-label="Direct link to MaximumIntegrationDistance" title="Direct link to MaximumIntegrationDistance">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float MaximumIntegrationDistance
```

</div>

</div>

Get or set the maximum distance (in m) from the camera at which that the meshing system will integrate depth samples into the 3D scene representation.

#### VoxelSize<a href="#VoxelSize" class="hash-link" aria-label="Direct link to VoxelSize" title="Direct link to VoxelSize">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float VoxelSize
```

</div>

</div>

Get or set the size (in m) of individual voxel elements in the scene representation. Setting this to higher values will reduce memory usage but reduce the precision of the surface.

#### MeshBlockSize<a href="#MeshBlockSize" class="hash-link" aria-label="Direct link to MeshBlockSize" title="Direct link to MeshBlockSize">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float MeshBlockSize
```

</div>

</div>

Get or set the size (in m) of the Mesh Blocks used for generating the Mesh Filter and Mesh Collider. This value will be automatically rounded to be a multiple of the voxel size.

#### MeshCullingDistance<a href="#MeshCullingDistance" class="hash-link" aria-label="Direct link to MeshCullingDistance" title="Direct link to MeshCullingDistance">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float MeshCullingDistance
```

</div>

</div>

Get or set the distance (in m) from the camera at which Mesh Blocks will be removed from the scene. A value of 0 indicates that Mesh Blocks will not be removed.

#### EnableMeshDecimation<a href="#EnableMeshDecimation" class="hash-link" aria-label="Direct link to EnableMeshDecimation" title="Direct link to EnableMeshDecimation">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool EnableMeshDecimation
```

</div>

</div>

Get or set whether excess triangles will be removed from the mesh.

#### EnableDistanceBasedVolumetricCleanup<a href="#EnableDistanceBasedVolumetricCleanup" class="hash-link" aria-label="Direct link to EnableDistanceBasedVolumetricCleanup" title="Direct link to EnableDistanceBasedVolumetricCleanup">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool EnableDistanceBasedVolumetricCleanup
```

</div>

</div>

Get or set whether the volumetric representation will be cleaned up once it moves outside the region where new mesh is currently being generated. This saves memory and smooths latency.

#### IsMeshFilteringEnabled<a href="#IsMeshFilteringEnabled" class="hash-link" aria-label="Direct link to IsMeshFilteringEnabled" title="Direct link to IsMeshFilteringEnabled">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool IsMeshFilteringEnabled
```

</div>

</div>

Get or set whether filtering to select which semantic segmentation channels are included in the mesh is currently enabled.

#### IsFilteringAllowListEnabled<a href="#IsFilteringAllowListEnabled" class="hash-link" aria-label="Direct link to IsFilteringAllowListEnabled" title="Direct link to IsFilteringAllowListEnabled">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool IsFilteringAllowListEnabled
```

</div>

</div>

Get or set whether to use the AllowList to determine which channels are included in the mesh. This property must be used in conjunction with the IsMeshFilteringEnabled property.

#### AllowList<a href="#AllowList" class="hash-link" aria-label="Direct link to AllowList" title="Direct link to AllowList">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
List<string> AllowList
```

</div>

</div>

The list of names of channels included in the mesh. Both the IsMeshFilteringEnabled and IsFilteringAllowListEnabled values must be true in order for the allow list to have an effect.

#### IsFilteringBlockListEnabled<a href="#IsFilteringBlockListEnabled" class="hash-link" aria-label="Direct link to IsFilteringBlockListEnabled" title="Direct link to IsFilteringBlockListEnabled">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool IsFilteringBlockListEnabled
```

</div>

</div>

Get or set whether to use the BlockList to determine which channels are included in the mesh. This property must be used in conjunction with the IsMeshFilteringEnabled property.

#### BlockList<a href="#BlockList" class="hash-link" aria-label="Direct link to BlockList" title="Direct link to BlockList">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
List<string> BlockList
```

</div>

</div>

The list of names of channels excluded from the mesh. Both the IsMeshFilteringEnabled and IsFilteringBlockListEnabled values must be true in order for the block list to have an effect.

</div>

</div>
