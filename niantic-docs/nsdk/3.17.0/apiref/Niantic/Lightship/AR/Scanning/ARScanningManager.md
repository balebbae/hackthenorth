---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/
title: class ARScanningManager
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class ARScanningManager

</div>

(Niantic.Lightship.AR.Scanning.ARScanningManager)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

A manager for recording scans of the [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) scene for Playback. The recording will start when the manager is enabled. Use [SaveScan()](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/#SaveScan) to stop and save the recording into the ScanPath.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class ARScanningManager: SubsystemLifecycleManager< XRScanningSubsystem, XRScanningSubsystemDescriptor, XRScanningSubsystem.Provider > {
    public:
       // fields
    
      NativeArray<Vector3> VoxelPositions => _voxelPositions;
       NativeArray<Color32> VoxelColors => _voxelColors;
         NativeArray<Vector3> VoxelNormals => _voxelNormals;
       float LatestVoxelSize => _latestVoxelSize;

     // properties
    
     string ScanPath;
      bool FullResolutionEnabled;
       int FullResolutionFramerate;
      string ScanTargetId;
      int ScanRecordingFramerate;
       bool EnableRaycastVisualization;
      bool EnableVoxelVisualization;
        bool UseEstimatedDepth;
       float MinimumVoxelSize;
       float NearDepth;
      float FarDepth;

       // methods
   
     Texture2D GetRaycastColorTexture();
     Texture2D GetRaycastNormalTexture();
        Texture2D GetRaycastPositionTexture();
      ScanStore GetScanStore();
       async Task SaveScan();
        async Task DiscardScan();
     string GetCurrentScanId();
        void RequestVoxelUpdate();
        bool TryGetVoxelBuffer();

 protected:
        // methods
   
     override void OnBeforeStart();
      override void OnDisable();
  };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

A manager for recording scans of the [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) scene for Playback. The recording will start when the manager is enabled. Use [SaveScan()](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/#SaveScan) to stop and save the recording into the ScanPath.

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### VoxelPositions<a href="#VoxelPositions" class="hash-link" aria-label="Direct link to VoxelPositions" title="Direct link to VoxelPositions">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
NativeArray<Vector3> VoxelPositions => _voxelPositions
```

</div>

</div>

The positions of voxels scanned with the camera. Each entry in the array corresponds to an entry in [VoxelColors](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/#VoxelColors) at the same index. These values can only be updated when [EnableVoxelVisualization](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/#EnableVoxelVisualization) is true and scanning is in the XRScanningState.Started state. Call RequestVoxelUpdate to update the underlying map, and then call TryGetVoxelBuffer to populate with the latest values.

#### VoxelColors<a href="#VoxelColors" class="hash-link" aria-label="Direct link to VoxelColors" title="Direct link to VoxelColors">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
NativeArray<Color32> VoxelColors => _voxelColors
```

</div>

</div>

The color of each voxel. Each entry in the array corresponds to an entry in [VoxelPositions](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/#VoxelPositions) at the same index. These values can only be updated when [EnableVoxelVisualization](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/#EnableVoxelVisualization) is true and scanning is in the XRScanningState.Started state. Call RequestVoxelUpdate to update the underlying map, and then call TryGetVoxelBuffer to populate with the latest values.

#### VoxelNormals<a href="#VoxelNormals" class="hash-link" aria-label="Direct link to VoxelNormals" title="Direct link to VoxelNormals">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
NativeArray<Vector3> VoxelNormals => _voxelNormals
```

</div>

</div>

The normal vector of each voxel. Each entry in the array corresponds to an entry in [VoxelPositions](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/#VoxelPositions) at the same index. These values can only be updated when [EnableVoxelVisualization](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/#EnableVoxelVisualization) is true and scanning is in the XRScanningState.Started state. Call RequestVoxelUpdate to update the underlying map, and then call TryGetVoxelBuffer to populate with the latest values.

#### LatestVoxelSize<a href="#LatestVoxelSize" class="hash-link" aria-label="Direct link to LatestVoxelSize" title="Direct link to LatestVoxelSize">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float LatestVoxelSize => _latestVoxelSize
```

</div>

</div>

The size of the voxels in [VoxelPositions](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/#VoxelPositions), in meters. The voxel visualizer attempts to use the voxel size requested by the [MinimumVoxelSize](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/#MinimumVoxelSize) parameter. As the number of voxels grows, the voxel visualizer periodically doubles the voxel size to keep memory use in check. This value should be used for rendering the voxels with the correct dimensions.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### ScanPath<a href="#ScanPath" class="hash-link" aria-label="Direct link to ScanPath" title="Direct link to ScanPath">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
string ScanPath
```

</div>

</div>

The scan path to store the scan data. If an absolute path is provided (starting with '/', '', or a drive name), the directory must be writable, and the application must have permissions to write to the folder. Otherwise, the path will be interpreted as relative to Application.persistentDataPath.

#### FullResolutionEnabled<a href="#FullResolutionEnabled" class="hash-link" aria-label="Direct link to FullResolutionEnabled" title="Direct link to FullResolutionEnabled">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool FullResolutionEnabled
```

</div>

</div>

Record full resolution images for scan reconstruction. Must be set before scanning starts to take effect.

#### FullResolutionFramerate<a href="#FullResolutionFramerate" class="hash-link" aria-label="Direct link to FullResolutionFramerate" title="Direct link to FullResolutionFramerate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
int FullResolutionFramerate
```

</div>

</div>

The framerate for full resolution frame recording. A framerate of zero means the system will use the default framerate of 2 FPS. Must be set before scanning starts to take effect.

#### ScanTargetId<a href="#ScanTargetId" class="hash-link" aria-label="Direct link to ScanTargetId" title="Direct link to ScanTargetId">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
string ScanTargetId
```

</div>

</div>

The scan target ID. Must be set before scanning starts to take effect.

#### ScanRecordingFramerate<a href="#ScanRecordingFramerate" class="hash-link" aria-label="Direct link to ScanRecordingFramerate" title="Direct link to ScanRecordingFramerate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
int ScanRecordingFramerate
```

</div>

</div>

The scan recording framerate. A framerate of zero means the system will use the default framerate of 15 FPS. Must be set before scanning starts to take effect.

#### EnableRaycastVisualization<a href="#EnableRaycastVisualization" class="hash-link" aria-label="Direct link to EnableRaycastVisualization" title="Direct link to EnableRaycastVisualization">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool EnableRaycastVisualization
```

</div>

</div>

Enable raycast visualization for scanning. Required to access the raycast textures. The data will be available from the [GetRaycastColorTexture](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/#GetRaycastColorTexture), [GetRaycastNormalTexture](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/#GetRaycastNormalTexture) and [GetRaycastPositionTexture](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/#GetRaycastPositionTexture) methods. Must be set before scanning starts to take effect.

#### EnableVoxelVisualization<a href="#EnableVoxelVisualization" class="hash-link" aria-label="Direct link to EnableVoxelVisualization" title="Direct link to EnableVoxelVisualization">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool EnableVoxelVisualization
```

</div>

</div>

Enable voxel visualization for scanning. Required to compute voxels. RequestVoxelUpdate must be called to asynchronously compute the voxel buffers. Then, TryGetVoxelBuffer can be called to get the voxel buffers. After TryGetVoxelBuffer returns true, the voxel data will be available in the [VoxelPositions](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/#VoxelPositions), [VoxelColors](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/#VoxelColors) and [LatestVoxelSize](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/#LatestVoxelSize) fields. Must be set before scanning starts to take effect.

#### UseEstimatedDepth<a href="#UseEstimatedDepth" class="hash-link" aria-label="Direct link to UseEstimatedDepth" title="Direct link to UseEstimatedDepth">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool UseEstimatedDepth
```

</div>

</div>

Record Niantic depth data if the device does not support platform depth such as lidar. If platform depth is present, it will be used instead of Niantic depth.

#### MinimumVoxelSize<a href="#MinimumVoxelSize" class="hash-link" aria-label="Direct link to MinimumVoxelSize" title="Direct link to MinimumVoxelSize">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float MinimumVoxelSize
```

</div>

</div>

The minimum size of voxels for voxel visualization, in meters. This parameter sets the initial resolution of the voxel grid used for voxel visualization (see [EnableVoxelVisualization](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/#EnableVoxelVisualization). Smaller values result in higher resolution but require more memory and computation. The actual voxel size may be larger due to memory constraints, so this is only a minimum value. Refer to [LatestVoxelSize](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ARScanningManager/#LatestVoxelSize) for the correct dimensions when rendering voxels. Must be set before scanning starts to take effect.

#### NearDepth<a href="#NearDepth" class="hash-link" aria-label="Direct link to NearDepth" title="Direct link to NearDepth">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float NearDepth
```

</div>

</div>

The near depth plane for depth range, in meters. This parameter controls the closest distance at which depth data will be integrated. Objects closer than this distance will not be visible in visualization or reconstruction. Must be set before scanning starts to take effect.

#### FarDepth<a href="#FarDepth" class="hash-link" aria-label="Direct link to FarDepth" title="Direct link to FarDepth">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float FarDepth
```

</div>

</div>

The far depth plane for depth range, in meters. This parameter controls the farthest distance at which depth data will be integrated. Objects farther than this distance will not be visible in visualization or reconstruction. Must be set before scanning starts to take effect.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### GetRaycastColorTexture<a href="#GetRaycastColorTexture" class="hash-link" aria-label="Direct link to GetRaycastColorTexture" title="Direct link to GetRaycastColorTexture">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Texture2D GetRaycastColorTexture()
```

</div>

</div>

Read the current raycast color texture.

The color texture for raycast visualization, if configured and ready. Otherwise, null.

#### GetRaycastNormalTexture<a href="#GetRaycastNormalTexture" class="hash-link" aria-label="Direct link to GetRaycastNormalTexture" title="Direct link to GetRaycastNormalTexture">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Texture2D GetRaycastNormalTexture()
```

</div>

</div>

Read the current raycast normal texture.

The normal texture for raycast visualization, if configured and ready. Otherwise, null.

#### GetRaycastPositionTexture<a href="#GetRaycastPositionTexture" class="hash-link" aria-label="Direct link to GetRaycastPositionTexture" title="Direct link to GetRaycastPositionTexture">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Texture2D GetRaycastPositionTexture()
```

</div>

</div>

Read the current raycast position texture.

The position texture for raycast visualization, if configured and ready. Otherwise, null.

#### SaveScan<a href="#SaveScan" class="hash-link" aria-label="Direct link to SaveScan" title="Direct link to SaveScan">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
async Task SaveScan()
```

</div>

</div>

Save the current scan. This stops any further recording immediately, and the coroutine finishes when the saving is fully complete.

Do not disable the component or exit the app when this is in progress. The scan will not be saved correctly if this process is interrupted.

    **Returns:**

    

#### DiscardScan<a href="#DiscardScan" class="hash-link" aria-label="Direct link to DiscardScan" title="Direct link to DiscardScan">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
async Task DiscardScan()
```

</div>

</div>

Discard the current scan. This stops further recording immediately, and the coroutine finishes when all existing data is deleted.

    **Returns:**

    

#### GetCurrentScanId<a href="#GetCurrentScanId" class="hash-link" aria-label="Direct link to GetCurrentScanId" title="Direct link to GetCurrentScanId">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
string GetCurrentScanId()
```

</div>

</div>

Returns the current scanID. The result is only present when scan is in progress.

    **Returns:**

    

</div>

</div>
