---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Occlusion.NsdkOcclusionExtension/
title: NsdkOcclusionExtension
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Occlusion](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Occlusion/ "NianticSpatial.NSDK.AR.Occlusion") 

</div>

<div class="api-title">

#  NsdkOcclusionExtension

<div class="api-extends">

↳ extends [CompositeRenderer](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Common.CompositeRenderer/ "CompositeRenderer") 

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">partial</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">NsdkOcclusionExtension</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[CompositeRenderer](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Common.CompositeRenderer/ "The composite renderer is an abstraction for renderers that perform multiple,...")</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

This component allows configuration of the additional functionality available in NSDK's implementation of XROcclusionSubsystem.

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
<td><span id="property-bypassocclusionmanagerupdates"></span><span class="ctoken-line"><span class="ctoken class-name">BypassOcclusionManagerUpdates</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Whether to disable automatically updating the depth texture of the occlusion manager.<br />
This feature can be used to avoid redundant texture operations since depth is ultimately<br />
going to be overriden by the NSDK Occlusion Extension anyway. Not using this setting<br />
may result in undesired synchronization with the rendering thread that impacts performance.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-custommaterial"></span><span class="ctoken-line"><span class="ctoken class-name">CustomMaterial</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Material</a></span></span></td>
<td><div class="ctoken comment">
Get or set the custom material used for processing the AR background depth buffer.<br />
If set to null, the default material will be used.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-depthtexture"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">DepthTexture</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Texture2D</a></span></span></td>
<td><div class="ctoken comment">
Returns the raw depth texture used in rendering.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-depthtransform"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">DepthTransform</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span></span></td>
<td><div class="ctoken comment">
Returns a transform for converting between normalized image coordinates and a coordinate space<br />
appropriate for rendering DepthTexture on the viewport.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-isocclusionstabilizationenabled"></span><span class="ctoken-line"><span class="ctoken class-name">IsOcclusionStabilizationEnabled</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Get or set whether meshing based occlusion stabilization is enabled.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-isocclusionsuppressionenabled"></span><span class="ctoken-line"><span class="ctoken class-name">IsOcclusionSuppressionEnabled</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Get or set whether semantic segmentation based occlusion suppression is enabled.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-isrenderingactive"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">IsRenderingActive</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Whether the second pass of background rendering is active to satisfy custom occlusion features.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-latestextrinsicsmatrix"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">LatestExtrinsicsMatrix</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Returns the extrinsics matrix for DepthTexture.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-latestintrinsicsmatrix"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">LatestIntrinsicsMatrix</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Matrix4x4</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Returns the intrinsics matrix for DepthTexture. Contains values for the<br />
camera's focal length and principal point. Converts between 2D image pixel coordinates<br />
and 3D world coordinates relative to the camera.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-occlusiondistancemode"></span><span class="ctoken-line"><span class="ctoken class-name">OcclusionDistanceMode</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Occlusion.NsdkOcclusionExtension.OptimalOcclusionDistanceMode/" title="The sampling mode for determining the distance to the occluder....">OptimalOcclusionDistanceMode</a></span></span></td>
<td><div class="ctoken comment">
Get or set the current mode in use for determining the distance at which occlusions<br />
will have the best visual quality.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-overrideocclusionmanagersettings"></span><span class="ctoken-line"><span class="ctoken class-name">OverrideOcclusionManagerSettings</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Whether to override the occlusion manager's settings to set the most optimal configuration<br />
for the occlusion extension. Currently, the following overrides are applied:<br />
1) On iPhone devices with Lidar sensor, the best and medium occlusion mode will cause a<br />
significant performance hit as well as a crash. We will override the occlusion mode to<br />
fastest to avoid this issue and enable smooth edges for the best results.<br />
2) The occlusion preference mode is set to NoOcclusion when the occlusion extension is active.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-prefersmoothedges"></span><span class="ctoken-line"><span class="ctoken class-name">PreferSmoothEdges</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
When enabled, the depth image will be sampled bilinearly during rendering.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-stabilizationthreshold"></span><span class="ctoken-line"><span class="ctoken class-name">StabilizationThreshold</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
The stabilization threshold determines whether to prefer per-frame (0)<br />
or fused depth (1) during occlusion stabilization.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-stabledepthmaterial"></span><span class="ctoken-line"><span class="ctoken class-name">StableDepthMaterial</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Material</a></span></span></td>
<td><div class="ctoken comment">
Get or set the material used for rendering the fused depth texture.<br />
This is relevant when the occlusion stabilization feature is enabled.<br />
The shader used by this material should output metric eye depth.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-supportstargetframerate"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">SupportsTargetFrameRate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Determines whether the TargetFrameRate API is supported with the current configuration.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-targetframerate"></span><span class="ctoken-line"><span class="ctoken class-name">TargetFrameRate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">uint</span></span></td>
<td><div class="ctoken comment">
The framerate that depth inference will aim to run at. Setting the value to 0 will result<br />
in using the recommended frame rate.<br />
Call SupportsTargetFrameRate to check if the target frame rate is supported.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-visualization"></span><span class="ctoken-line"><span class="ctoken class-name">Visualization</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
When enabled, the component displays the depth image used for occlusions.<br />
Note that visualization can only be used if a custom occlusion feature is<br />
active, e.g. suppression or stabilization.
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
<td><span id="method-addscenesegmentationsuppressionchannel"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Occlusion.NsdkOcclusionExtension.AddSceneSegmentationSuppressionChannel/" title="Adds a semantic segmentation channel to the collection of channels that are suppressed in the depth buffer.">AddSceneSegmentationSuppressionChannel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Adds a semantic segmentation channel to the collection of channels that are suppressed in the depth buffer.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-removescenesegmentationsuppressionchannel"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Occlusion.NsdkOcclusionExtension.RemoveSceneSegmentationSuppressionChannel/" title="Removes a semantic segmentation channel, if it exists, from the collection of channels...">RemoveSceneSegmentationSuppressionChannel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Removes a semantic segmentation channel, if it exists, from the collection of channels<br />
that are suppressed in the depth buffer.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-trackoccludee"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Occlusion.NsdkOcclusionExtension.TrackOccludee/" title="Sets the principal virtual object being occluded in the SpecifiedGameObject occlusion mode....">TrackOccludee</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment">
Sets the principal virtual object being occluded in the SpecifiedGameObject occlusion mode.<br />
This method changes the optimal occlusion distance mode setting.&gt;
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-trygetdepth"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Occlusion.NsdkOcclusionExtension.TryGetDepth/" title="Returns the metric eye depth at the specified pixel coordinates.">TryGetDepth</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Returns the metric eye depth at the specified pixel coordinates.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
