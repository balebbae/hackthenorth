---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.NsdkSceneSegmentationOverlay/
title: NsdkSceneSegmentationOverlay
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.SceneSegmentation](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation/ "NianticSpatial.NSDK.AR.SceneSegmentation") 

</div>

<div class="api-title">

#  NsdkSceneSegmentationOverlay

<div class="api-extends">

↳ extends [ConditionalRenderer](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Common.ConditionalRenderer/ "ConditionalRenderer") 

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">sealed</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">NsdkSceneSegmentationOverlay</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[ConditionalRenderer](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Common.ConditionalRenderer/ "Base class for rendering components that attach command buffers to the camera....")</span></span>

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
<td><span id="property-backprojectiondistance"></span><span class="ctoken-line"><span class="ctoken class-name">BackProjectionDistance</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
Distance in meters (from the camera) to back-project the image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-intrinsics"></span><span class="ctoken-line"><span class="ctoken class-name">Intrinsics</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arsubsystems@4.2/api/UnityEngine.XR.ARSubsystems.XRCameraIntrinsics.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">XRCameraIntrinsics</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
The intrinsics matrix of the semantics image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-ismetadataavailable"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">IsMetadataAvailable</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Whether the semantics metadata (such as number of channels) is available.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

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
<td><span id="field-kshadername"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">KShaderName</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
The shader name to use for the semantics overlay.
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
<td><span id="method-setchannel"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.NsdkSceneSegmentationOverlay.SetChannel/" title="Sets the current channel to display.">SetChannel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment">
Sets the current channel to display.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
