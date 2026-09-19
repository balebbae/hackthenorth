---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation/
title: NianticSpatial.NSDK.AR.SceneSegmentation
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") 

</div>

<div class="api-title">

#  SceneSegmentation

</div>

------------------------------------------------------------------------

## Classes<a href="#classes" class="hash-link" aria-label="Direct link to Classes" title="Direct link to Classes">​</a>

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
<td><span id="class-arscenesegmentationmanager"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager/" title="The ARSceneSegmentationManager controls the XRSceneSegmentationSubsystem and updates the scene segmentation...">ARSceneSegmentationManager</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.0/api/UnityEngine.XR.ARFoundation.SubsystemLifecycleManager-3.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">SubsystemLifecycleManager</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem/" title="Defines an interface for interacting with semantic segmentation functionality.">XRSceneSegmentationSubsystem</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystemDescriptor/" title="Descriptor for the XRSceneSegmentationSubsystem.">XRSceneSegmentationSubsystemDescriptor</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem.Provider/" title="The provider which will service the XRSceneSegmentationSubsystem.">Provider</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
The ARSceneSegmentationManager controls the XRSceneSegmentationSubsystem and updates the scene segmentation<br />
textures on each Update loop. Textures and XRCpuImages are available for confidence maps of individual semantic<br />
segmentation channels and a bit array indicating which semantic channels have surpassed the chosen confidence<br />
threshold per pixel. For cases where a semantic segmentation texture is overlaid on the screen, utilities are<br />
provided to read semantic properties at a given point on the screen.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkscenesegmentationoverlay"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.NsdkSceneSegmentationOverlay/" title="Browse to NsdkSceneSegmentationOverlay">NsdkSceneSegmentationOverlay</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Common.ConditionalRenderer/" title="Base class for rendering components that attach command buffers to the camera....">ConditionalRenderer</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Structs<a href="#structs" class="hash-link" aria-label="Direct link to Structs" title="Direct link to Structs">​</a>

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
<td><span id="struct-arscenesegmentationframeeventargs"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationFrameEventArgs/" title="A structure for camera-related information pertaining to a particular frame....">ARSceneSegmentationFrameEventArgs</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment">
A structure for camera-related information pertaining to a particular frame.<br />
This is used to communicate information in the frameReceived event.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-arscenesegmentationmodeleventargs"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationModelEventArgs/" title="A structure for information about the semantic segmentation model that&#39;s become ready. This is used to...">ARSceneSegmentationModelEventArgs</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.iequatable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">IEquatable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationModelEventArgs/" title="A structure for information about the semantic segmentation model that&#39;s become ready. This is used to...">ARSceneSegmentationModelEventArgs</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
A structure for information about the semantic segmentation model that's become ready. This is used to<br />
communicate information in the MetadataInitialized event.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
