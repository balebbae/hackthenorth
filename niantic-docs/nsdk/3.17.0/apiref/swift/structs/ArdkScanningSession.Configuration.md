---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/ArdkScanningSession.Configuration/
title: ArdkScanningSession.Configuration
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `ArdkScanningSession.Configuration`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
struct Configuration
```

</div>

</div>

Configuration structure for the scanning session.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `framerate`<a href="#framerate" class="hash-link" aria-label="Direct link to framerate" title="Direct link to framerate">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var framerate: Int32
```

</div>

</div>

Target FPS for recording and visualization processes.

The target framerate is the cap for how often the feature will process new input frames. The actual framerate may differ. If set to `0`, this defaults to 30 FPS. The recording FPS cannot exceed the rate at which frames are delivered to the scanning session.

- Note: Recording NSDK depth with `generateDepthsIfLidarUnavailable` can result in a lower recording FPS than the target framerate.

### `enableRaycastVisualization`<a href="#enableraycastvisualization" class="hash-link" aria-label="Direct link to enableraycastvisualization" title="Direct link to enableraycastvisualization">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var enableRaycastVisualization: Bool
```

</div>

</div>

Controls whether raycast visualization images are generated.

When `true`, images for the raycast visualization will be generated each time a new input frame is available. The scanning feature provides buffers that can be used to generate a 2D image that visualizes what parts of the scene have been thoroughly scanned. See the `RaycastBuffer` class for more information.

### `enableVoxelVisualization`<a href="#enablevoxelvisualization" class="hash-link" aria-label="Direct link to enablevoxelvisualization" title="Direct link to enablevoxelvisualization">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var enableVoxelVisualization: Bool
```

</div>

</div>

Controls whether voxel visualization is enabled.

When `true`, voxels can be computed, and computed voxels will be updated each time a new input frame is available. Use `computeVoxels` to update the voxel grid and `voxelBuffer` to read the data.

### `raycastWidth`<a href="#raycastwidth" class="hash-link" aria-label="Direct link to raycastwidth" title="Direct link to raycastwidth">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var raycastWidth: Int32
```

</div>

</div>

Width of the raycast visualization's output image in pixel units.

The output quality is bound by both the configured resolution and the quality of the underlying 3D reconstruction data. On devices without native depth support, the data is unlikely to be sufficient to support resolutions above 256x144. If set to `0`, this is configured to 256 pixels.

### `raycastHeight`<a href="#raycastheight" class="hash-link" aria-label="Direct link to raycastheight" title="Direct link to raycastheight">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var raycastHeight: Int32
```

</div>

</div>

Height of the raycast visualization's output image in pixel units.

The output quality is bound by both the configured resolution and the quality of the underlying 3D reconstruction data. On devices without native depth support, the data is unlikely to be sufficient to support resolutions above 256x144. If set to `0`, this is configured to 144 pixels.

### `nearDepth`<a href="#neardepth" class="hash-link" aria-label="Direct link to neardepth" title="Direct link to neardepth">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var nearDepth: Float
```

</div>

</div>

Near depth plane for scan depth range, in meters.

This parameter controls the closest distance at which depth data will be integrated. Objects closer than this distance will not be visible in visualization or reconstruction. This does not affect the range of the recorded depth frames. If set to `-1.0`, this is configured to 0.02 m in the default configuration. Must be greater than or equal to 0 and less than `farDepth`, or set to `-1.0` to use the default range.

### `farDepth`<a href="#fardepth" class="hash-link" aria-label="Direct link to fardepth" title="Direct link to fardepth">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var farDepth: Float
```

</div>

</div>

Far depth plane for scan depth range, in meters.

This parameter controls the farthest distance at which depth data will be integrated. Objects farther than this distance will not be visible in visualization or reconstruction. This does not affect the range of the recorded depth frames. If set to `0.0`, this is configured to 5.0 m in the default configuration. Values greater than 5.0 m are not recommended. Must be greater than `nearDepth`, or set to `0` to use the default range.

### `voxelSize`<a href="#voxelsize" class="hash-link" aria-label="Direct link to voxelsize" title="Direct link to voxelsize">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var voxelSize: Float
```

</div>

</div>

Minimum size of voxels for the voxel visualization, in meters.

This parameter controls the resolution of the voxel grid used for voxel visualization. Smaller values result in higher resolution but require more memory and computation. Larger values result in lower resolution but are more efficient. The actual voxel size may become larger due to memory constraints, so this is only a minimum value. If set to `0.0`, this is configured to 0.01 m in the default configuration.

### `path`<a href="#path" class="hash-link" aria-label="Direct link to path" title="Direct link to path">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var path: String?
```

</div>

</div>

Optional field to set a base path for writing scan data.

If an absolute path (starting with '/', '', or a drive name) is provided, the directory must be writeable by the application. All other paths will be interpreted as relative to the public application path configured when the NSDK object was created. If left `nil`, NSDK uses the public application path which was configured when creating the NSDK object.

### `scanTargetId`<a href="#scantargetid" class="hash-link" aria-label="Direct link to scantargetid" title="Direct link to scantargetid">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var scanTargetId: String?
```

</div>

</div>

Optional field to set a scan target identifier for use with Niantic Spatial's mapping services.

### `generateDepthsIfLidarUnavailable`<a href="#generatedepthsiflidarunavailable" class="hash-link" aria-label="Direct link to generatedepthsiflidarunavailable" title="Direct link to generatedepthsiflidarunavailable">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var generateDepthsIfLidarUnavailable: Bool
```

</div>

</div>

Whether to use and record NSDK's estimated depths, if platform depths are unavailable.

Depths are recorded as part of the scan data, and are also required to generate voxels or raycast visualization images. If NSDK was configured to use platform depths, this value is ignored, and depths are expected to come through the scanning session. Otherwise:

- When `true`, NSDK will generate estimated depths for use by the scanning feature

- When `false`, the scanning feature will not be able to generate voxels or raycast visualization images, but will still be able to record other scan data.

- Attention: If NSDK depth is being recorded because `generateDepthsIfLidarUnavailable` is `true` and lidar is unavailable, the recording FPS will be limited to the update rate of the depth feature, which defaults to 10 FPS. To change the update rate of the depth feature, set `ArdkDepthSession.Configuration.framerate` to match `ScanningConfiguration.framerate`.

### `enableFullResolution`<a href="#enablefullresolution" class="hash-link" aria-label="Direct link to enablefullresolution" title="Direct link to enablefullresolution">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var enableFullResolution: Bool
```

</div>

</div>

Controls whether full-resolution camera images are recorded.

When `true`, the scanning feature will record a JPEG image that is the same resolution as the raw camera image passed to the NSDK session with the `sendFrame` function. When `false`, the scanning feature records a 720x540 resolution JPEG image generated by cropping and/or scaling and compressing the raw camera image.

- Note: Compressing the camera image to JPEG format is relatively expensive, so enable this option with that in mind.

- Note: The quality of voxel and raycast visualizations is not affected by this value.

### `fullResolutionFramerate`<a href="#fullresolutionframerate" class="hash-link" aria-label="Direct link to fullresolutionframerate" title="Direct link to fullresolutionframerate">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var fullResolutionFramerate: Int32
```

</div>

</div>

Target FPS for full resolution frame recording.

The target framerate for recording full resolution frames when `enableFullResolution` is `true`. The actual framerate for full-resolution frames may differ from the target framerate. If set to `0`, this is configured to 2 FPS in the default configuration.

- Note: Recording NSDK depth with `generateDepthsIfLidarUnavailable` can result in a lower recording FPS than the target framerate.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(framerate:enableRaycastVisualization:enableVoxelVisualization:raycastWidth:raycastHeight:nearDepth:farDepth:voxelSize:path:scanTargetId:generateDepthsIfLidarUnavailable:enableFullResolution:fullResolutionFramerate:)`<a href="#initframerateenableraycastvisualizationenablevoxelvisualizationraycastwidthraycastheightneardepthfardepthvoxelsizepathscantargetidgeneratedepthsiflidarunavailableenablefullresolutionfullresolutionframerate" class="hash-link" aria-label="Direct link to initframerateenableraycastvisualizationenablevoxelvisualizationraycastwidthraycastheightneardepthfardepthvoxelsizepathscantargetidgeneratedepthsiflidarunavailableenablefullresolutionfullresolutionframerate" title="Direct link to initframerateenableraycastvisualizationenablevoxelvisualizationraycastwidthraycastheightneardepthfardepthvoxelsizepathscantargetidgeneratedepthsiflidarunavailableenablefullresolutionfullresolutionframerate">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(
    framerate: Int = 0,
    enableRaycastVisualization: Bool = false,
    enableVoxelVisualization: Bool = false,
    raycastWidth: Int = 0,
    raycastHeight: Int = 0,
    nearDepth: Float = 0.02,
    farDepth: Float = 0.0,
    voxelSize: Float = 0.0,
    path: String? = nil,
    scanTargetId: String? = nil,
    generateDepthsIfLidarUnavailable: Bool = false,
    enableFullResolution: Bool = false,
    fullResolutionFramerate: Int = 0
)
```

</div>

</div>

Initializes a new scanning session configuration with provided settings.

</div>

</div>
