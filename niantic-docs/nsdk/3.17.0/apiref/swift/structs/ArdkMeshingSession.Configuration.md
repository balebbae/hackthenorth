---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/ArdkMeshingSession.Configuration/
title: ArdkMeshingSession.Configuration
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `ArdkMeshingSession.Configuration`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
struct Configuration
```

</div>

</div>

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `frameRate`<a href="#framerate" class="hash-link" aria-label="Direct link to framerate" title="Direct link to framerate">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var frameRate: Int
```

</div>

</div>

Target frame rate for the meshing feature

### `fuseKeyframesOnly`<a href="#fusekeyframesonly" class="hash-link" aria-label="Direct link to fusekeyframesonly" title="Direct link to fusekeyframesonly">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var fuseKeyframesOnly: Bool
```

</div>

</div>

If true, only high-quality frames will be integrated into the mesh, but updates will be less frequent

### `maximumIntegrationDistance`<a href="#maximumintegrationdistance" class="hash-link" aria-label="Direct link to maximumintegrationdistance" title="Direct link to maximumintegrationdistance">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var maximumIntegrationDistance: Float
```

</div>

</div>

The maximum distance from the device sensor to incorporate depth data, in meters

### `voxelSize`<a href="#voxelsize" class="hash-link" aria-label="Direct link to voxelsize" title="Direct link to voxelsize">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var voxelSize: Float
```

</div>

</div>

Voxel size for the meshing engine, in meters

### `enableDistanceBasedVolumetricCleanup`<a href="#enabledistancebasedvolumetriccleanup" class="hash-link" aria-label="Direct link to enabledistancebasedvolumetriccleanup" title="Direct link to enabledistancebasedvolumetriccleanup">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var enableDistanceBasedVolumetricCleanup: Bool
```

</div>

</div>

If true, the feature will clean up internal data that is far away from the user to improve performance. This will not remove previously-generated mesh.

### `numVoxelLevels`<a href="#numvoxellevels" class="hash-link" aria-label="Direct link to numvoxellevels" title="Direct link to numvoxellevels">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var numVoxelLevels: Int
```

</div>

</div>

The levels of detail in the voxel grid By default, this is 0. Setting this to a value greater than 1 will allow lower detail levels to be used in areas with less thorough coverage.

### `meshBlockSize`<a href="#meshblocksize" class="hash-link" aria-label="Direct link to meshblocksize" title="Direct link to meshblocksize">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var meshBlockSize: Float
```

</div>

</div>

The size of the mesh blocks, in meters

### `meshCullingDistance`<a href="#meshcullingdistance" class="hash-link" aria-label="Direct link to meshcullingdistance" title="Direct link to meshcullingdistance">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var meshCullingDistance: Float
```

</div>

</div>

Mesh culling distance, in meters Setting meshCullingDistance less than maximumIntegrationDistance may lead to unexpected behaviour.

### `enableMeshDecimation`<a href="#enablemeshdecimation" class="hash-link" aria-label="Direct link to enablemeshdecimation" title="Direct link to enablemeshdecimation">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var enableMeshDecimation: Bool
```

</div>

</div>

If true, mesh surfaces will be simplified to save compute and memory

### `filterMeshWithSemantics`<a href="#filtermeshwithsemantics" class="hash-link" aria-label="Direct link to filtermeshwithsemantics" title="Direct link to filtermeshwithsemantics">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var filterMeshWithSemantics: Bool
```

</div>

</div>

If true, the mesh will be filtered according to the packedAllowlist and/or packedBlocklist.

### `enableAllowlist`<a href="#enableallowlist" class="hash-link" aria-label="Direct link to enableallowlist" title="Direct link to enableallowlist">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var enableAllowlist: Bool
```

</div>

</div>

If true, packedAllowlist will be used to filter the mesh. Requires filterMeshWithSemantics to be true.

### `packedAllowlist`<a href="#packedallowlist" class="hash-link" aria-label="Direct link to packedallowlist" title="Direct link to packedallowlist">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var packedAllowlist: UInt32
```

</div>

</div>

A bitmask of semantic classes to include in the mesh

### `enableBlocklist`<a href="#enableblocklist" class="hash-link" aria-label="Direct link to enableblocklist" title="Direct link to enableblocklist">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var enableBlocklist: Bool
```

</div>

</div>

If true, packedBlocklist will be used to filter the mesh. Requires filterMeshWithSemantics to be true.

### `packedBlocklist`<a href="#packedblocklist" class="hash-link" aria-label="Direct link to packedblocklist" title="Direct link to packedblocklist">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var packedBlocklist: UInt32
```

</div>

</div>

A bitmask of semantic classes to exclude from the mesh

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(frameRate:fuseKeyframesOnly:maximumIntegrationDistance:voxelSize:enableDistanceBasedVolumetricCleanup:numVoxelLevels:meshBlockSize:meshCullingDistance:enableMeshDecimation:filterMeshWithSemantics:enableAllowlist:packedAllowlist:enableBlocklist:packedBlocklist:)`<a href="#initframeratefusekeyframesonlymaximumintegrationdistancevoxelsizeenabledistancebasedvolumetriccleanupnumvoxellevelsmeshblocksizemeshcullingdistanceenablemeshdecimationfiltermeshwithsemanticsenableallowlistpackedallowlistenableblocklistpackedblocklist" class="hash-link" aria-label="Direct link to initframeratefusekeyframesonlymaximumintegrationdistancevoxelsizeenabledistancebasedvolumetriccleanupnumvoxellevelsmeshblocksizemeshcullingdistanceenablemeshdecimationfiltermeshwithsemanticsenableallowlistpackedallowlistenableblocklistpackedblocklist" title="Direct link to initframeratefusekeyframesonlymaximumintegrationdistancevoxelsizeenabledistancebasedvolumetriccleanupnumvoxellevelsmeshblocksizemeshcullingdistanceenablemeshdecimationfiltermeshwithsemanticsenableallowlistpackedallowlistenableblocklistpackedblocklist">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(
    frameRate: Int = 0,
    fuseKeyframesOnly: Bool = false,
    maximumIntegrationDistance: Float = 0,
    voxelSize: Float = 0,
    enableDistanceBasedVolumetricCleanup: Bool = false,
    numVoxelLevels: Int = 0,
    meshBlockSize: Float = 0,
    meshCullingDistance: Float = 0,
    enableMeshDecimation: Bool = true,
    filterMeshWithSemantics: Bool = false,
    enableAllowlist: Bool = false,
    packedAllowlist: UInt32 = 0,
    enableBlocklist: Bool = false,
    packedBlocklist: UInt32 = 0
)
```

</div>

</div>

</div>

</div>
