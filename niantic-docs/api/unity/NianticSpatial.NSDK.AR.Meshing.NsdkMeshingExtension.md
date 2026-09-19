---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Meshing.NsdkMeshingExtension/
title: NsdkMeshingExtension
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Meshing](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Meshing/ "NianticSpatial.NSDK.AR.Meshing") 

</div>

<div class="api-title">

#  NsdkMeshingExtension

<div class="api-extends">

↳ extends UnityEngine.MonoBehaviour

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">NsdkMeshingExtension</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">MonoBehaviour</a></span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

This component allows configuration of the additional functionality available in NSDK's implementation of XRMeshingSubsystem.

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
<td><span id="property-allowlist"></span><span class="ctoken-line"><span class="ctoken class-name">AllowList</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">List</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.SceneSegmentation.SceneSegmentationChannel/" title="Represents the different semantic segmentation channels that can be detected....">SceneSegmentationChannel</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
The list of channels included in the mesh. Both the IsMeshFilteringEnabled and<br />
IsFilteringAllowListEnabled values must be true in order for the allow list to have an effect.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-blocklist"></span><span class="ctoken-line"><span class="ctoken class-name">BlockList</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">List</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.SceneSegmentation.SceneSegmentationChannel/" title="Represents the different semantic segmentation channels that can be detected....">SceneSegmentationChannel</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
The list of names of channels excluded from the mesh. Both the IsMeshFilteringEnabled and<br />
IsFilteringBlockListEnabled values must be true in order for the block list to have an effect.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-enabledistancebasedvolumetriccleanup"></span><span class="ctoken-line"><span class="ctoken class-name">EnableDistanceBasedVolumetricCleanup</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Get or set whether the volumetric representation will be cleaned up once it moves outside the region<br />
where new mesh is currently being generated. This saves memory and smooths latency.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-enablelevelsofdetail"></span><span class="ctoken-line"><span class="ctoken class-name">EnableLevelsOfDetail</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-enablemeshdecimation"></span><span class="ctoken-line"><span class="ctoken class-name">EnableMeshDecimation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Get or set whether excess triangles will be removed from the mesh.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-fusekeyframesonly"></span><span class="ctoken-line"><span class="ctoken class-name">FuseKeyframesOnly</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Get or set whether only depth keyframes will be fused into the mesh.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-isfilteringallowlistenabled"></span><span class="ctoken-line"><span class="ctoken class-name">IsFilteringAllowListEnabled</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Get or set whether to use the AllowList to determine which channels are included in the mesh.<br />
This property must be used in conjunction with the IsMeshFilteringEnabled property.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-isfilteringblocklistenabled"></span><span class="ctoken-line"><span class="ctoken class-name">IsFilteringBlockListEnabled</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Get or set whether to use the BlockList to determine which channels are included in the mesh.<br />
This property must be used in conjunction with the IsMeshFilteringEnabled property.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-ismeshfilteringenabled"></span><span class="ctoken-line"><span class="ctoken class-name">IsMeshFilteringEnabled</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Get or set whether filtering to select which semantic segmentation channels are included in the mesh<br />
is currently enabled.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-levelsofdetail"></span><span class="ctoken-line"><span class="ctoken class-name">LevelsOfDetail</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-maximumintegrationdistance"></span><span class="ctoken-line"><span class="ctoken class-name">MaximumIntegrationDistance</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
Get or set the maximum distance (in m) from the camera at which that the meshing system will<br />
integrate depth samples into the 3D scene representation.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-meshblocksize"></span><span class="ctoken-line"><span class="ctoken class-name">MeshBlockSize</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
Get or set the size (in m) of the Mesh Blocks used for generating the Mesh Filter and Mesh Collider.<br />
This value will be automatically rounded to be a multiple of the voxel size.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-meshcullingdistance"></span><span class="ctoken-line"><span class="ctoken class-name">MeshCullingDistance</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
Get or set the distance (in m) from the camera at which Mesh Blocks will be removed from the scene. A value of 0 indicates that Mesh Blocks will not be removed.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-targetframerate"></span><span class="ctoken-line"><span class="ctoken class-name">TargetFrameRate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
Get or set the frame rate that meshing will aim to run at.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-voxelsize"></span><span class="ctoken-line"><span class="ctoken class-name">VoxelSize</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
Get or set the size (in m) of individual voxel elements in the scene representation.<br />
Setting this to higher values will reduce memory usage but reduce the precision of the surface.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

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
<td><span id="method-configure"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Meshing.NsdkMeshingExtension.Configure/" title="Browse to Configure">Configure</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-update"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Meshing.NsdkMeshingExtension.Update/" title="Browse to Update">Update</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
