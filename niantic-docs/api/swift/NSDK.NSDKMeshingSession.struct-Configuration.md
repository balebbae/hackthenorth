---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMeshingSession.struct-Configuration/
title: Configuration
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKMeshingSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKMeshingSession/ "NSDKMeshingSession") 

</div>

<div class="api-title">

#  Configuration

<div class="api-package">

The type of configuration used by this session

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">struct</span><span class="ctoken plain"> </span><span class="ctoken class-name">Configuration</span></span>

------------------------------------------------------------------------

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">init</span><span class="ctoken plain">(</span><span class="ctoken plain">frameRate</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/uint32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UInt32</a></span><span class="ctoken plain"> = 0, </span><span class="ctoken plain">fuseKeyframesOnly</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain"> = false, </span><span class="ctoken plain">maximumIntegrationDistance</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain"> = 0, </span><span class="ctoken plain">voxelSize</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain"> = 0, </span><span class="ctoken plain">enableDistanceBasedVolumetricCleanup</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain"> = false, </span><span class="ctoken plain">numVoxelLevels</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int32</a></span><span class="ctoken plain"> = 0, </span><span class="ctoken plain">meshBlockSize</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain"> = 0, </span><span class="ctoken plain">meshCullingDistance</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain"> = 0, </span><span class="ctoken plain">enableMeshDecimation</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain"> = true, </span><span class="ctoken plain">filterMeshWithSceneSegmentation</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain"> = false, </span><span class="ctoken plain">enableAllowlist</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain"> = false, </span><span class="ctoken plain">packedAllowlist</span><span class="ctoken plain">: </span><span class="ctoken class-name">[SceneSegmentationChannels](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-SceneSegmentationChannels/ "A set of semantic channels represented as a bitmask, matching the C SDK packed-channel layout....")</span><span class="ctoken plain"> = SceneSegmentationChannels(), </span><span class="ctoken plain">enableBlocklist</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain"> = false, </span><span class="ctoken plain">packedBlocklist</span><span class="ctoken plain">: </span><span class="ctoken class-name">[SceneSegmentationChannels](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-SceneSegmentationChannels/ "A set of semantic channels represented as a bitmask, matching the C SDK packed-channel layout....")</span><span class="ctoken plain"> = SceneSegmentationChannels())</span></span>

</div>

------------------------------------------------------------------------

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

<table class="api-table">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr class="api-table-row">
<td><span id="property-enableallowlist"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">enableAllowlist</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
If true, packedAllowlist will be used to filter the mesh.<br />
Requires filterMeshWithSceneSegmentation to be true.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-enableblocklist"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">enableBlocklist</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
If true, packedBlocklist will be used to filter the mesh.<br />
Requires filterMeshWithSceneSegmentation to be true.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-enabledistancebasedvolumetriccleanup"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">enableDistanceBasedVolumetricCleanup</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
If true, the feature will clean up internal data that is far away from the user<br />
to improve performance. This will not remove previously-generated mesh.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-enablemeshdecimation"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">enableMeshDecimation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
If true, mesh surfaces will be simplified to save compute and memory
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-filtermeshwithscenesegmentation"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">filterMeshWithSceneSegmentation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
If true, the mesh will be filtered according to the packedAllowlist and/or packedBlocklist.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-framerate"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">frameRate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/uint32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UInt32</a></span></span></td>
<td><div class="ctoken comment">
Target frame rate for the meshing feature
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-fusekeyframesonly"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">fuseKeyframesOnly</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
If true, only high-quality frames will be integrated into the mesh,<br />
but updates will be less frequent
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-maximumintegrationdistance"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">maximumIntegrationDistance</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
The maximum distance from the device sensor to incorporate depth data, in meters
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-meshblocksize"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">meshBlockSize</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
The size of the mesh blocks, in meters
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-meshcullingdistance"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">meshCullingDistance</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Mesh culling distance, in meters<br />
Setting meshCullingDistance less than maximumIntegrationDistance may lead<br />
to unexpected behaviour.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-numvoxellevels"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">numVoxelLevels</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int32</a></span></span></td>
<td><div class="ctoken comment">
The levels of detail in the voxel grid<br />
By default, this is 0.<br />
Setting this to a value greater than 1 will allow lower detail levels to be used<br />
in areas with less thorough coverage.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-packedallowlist"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">packedAllowlist</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-SceneSegmentationChannels/" title="A set of semantic channels represented as a bitmask, matching the C SDK packed-channel layout....">SceneSegmentationChannels</a></span></span></td>
<td><div class="ctoken comment">
Semantic channels to include in the mesh (e.g. <code>[.ground, .grass]</code>).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-packedblocklist"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">packedBlocklist</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-SceneSegmentationChannels/" title="A set of semantic channels represented as a bitmask, matching the C SDK packed-channel layout....">SceneSegmentationChannels</a></span></span></td>
<td><div class="ctoken comment">
Semantic channels to exclude from the mesh (e.g. <code>[.sky]</code>).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-voxelsize"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">voxelSize</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Voxel size for the meshing engine, in meters
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
