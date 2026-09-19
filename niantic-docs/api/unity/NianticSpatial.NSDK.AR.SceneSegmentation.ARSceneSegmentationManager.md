---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager/
title: ARSceneSegmentationManager
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

#  ARSceneSegmentationManager

<div class="api-extends">

↳ extends UnityEngine.XR.ARFoundation.SubsystemLifecycleManager

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">ARSceneSegmentationManager</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.0/api/UnityEngine.XR.ARFoundation.SubsystemLifecycleManager-3.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">SubsystemLifecycleManager</a></span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">[XRSceneSegmentationSubsystem](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem/ "Defines an interface for interacting with semantic segmentation functionality.")</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">[XRSceneSegmentationSubsystemDescriptor](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystemDescriptor/ "Descriptor for the XRSceneSegmentationSubsystem.")</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">[Provider](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem.Provider/ "The provider which will service the XRSceneSegmentationSubsystem.")</span><span class="ctoken punctuation">\></span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

The ARSceneSegmentationManager controls the XRSceneSegmentationSubsystem and updates the scene segmentation textures on each Update loop. Textures and XRCpuImages are available for confidence maps of individual semantic segmentation channels and a bit array indicating which semantic channels have surpassed the chosen confidence threshold per pixel. For cases where a semantic segmentation texture is overlaid on the screen, utilities are provided to read semantic properties at a given point on the screen.

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
<td><span id="property-channelindices"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">ChannelIndices</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ireadonlydictionary-2?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">IReadOnlyDictionary</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.SceneSegmentation.SceneSegmentationChannel/" title="Represents the different semantic segmentation channels that can be detected....">SceneSegmentationChannel</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">int</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
The indices of the semantic channels that the current model is able to detect.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-channels"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Channels</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ireadonlylist-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">IReadOnlyList</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.SceneSegmentation.SceneSegmentationChannel/" title="Represents the different semantic segmentation channels that can be detected....">SceneSegmentationChannel</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
The semantic channels that the current model is able to detect.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-ismetadataavailable"></span><span class="ctoken-line"><span class="ctoken class-name">IsMetadataAvailable</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
True if the underlying subsystem has finished initialization.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-targetframerate"></span><span class="ctoken-line"><span class="ctoken class-name">TargetFrameRate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">uint</span></span></td>
<td><div class="ctoken comment">
Frame rate that semantic segmentation inference will aim to run at.
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
<td><span id="method-doeschannelexistat"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager.DoesChannelExistAt/" title="Check if a semantic class is detected at the specified location in screen space, based on the confidence...">DoesChannelExistAt</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Check if a semantic class is detected at the specified location in screen space, based on the confidence<br />
threshold set for this channel. (See TrySetChannelConfidenceThresholds)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getchannelfromname"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager.GetChannelFromName/" title="Converts a channel name string to its corresponding SceneSegmentationChannel enum value.">GetChannelFromName</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.SceneSegmentation.SceneSegmentationChannel/" title="Represents the different semantic segmentation channels that can be detected....">SceneSegmentationChannel</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Converts a channel name string to its corresponding SceneSegmentationChannel enum value.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getchannelindex"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager.GetChannelIndex/" title="Get the channel index of a specified semantic class. This corresponds to a bit position in the packed...">GetChannelIndex</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
Get the channel index of a specified semantic class. This corresponds to a bit position in the packed<br />
scene segmentation buffer, with index 0 being the most-significant bit.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getchannelindicesat"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager.GetChannelIndicesAt/" title="Returns an array of channel indices that are present at the specified pixel onscreen.">GetChannelIndicesAt</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">List</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name keyword">int</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Returns an array of channel indices that are present at the specified pixel onscreen.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getchannelnamefromenum"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager.GetChannelNameFromEnum/" title="Converts a SceneSegmentationChannel enum value to its string representation for display purposes.">GetChannelNameFromEnum</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
Converts a SceneSegmentationChannel enum value to its string representation for display purposes.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getchannelnamesat"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager.GetChannelNamesAt/" title="Returns an array of channel names that are present for the specified pixel onscreen (for display purposes).">GetChannelNamesAt</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">List</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name keyword">string</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Returns an array of channel names that are present for the specified pixel onscreen (for display purposes).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getchannelsat"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager.GetChannelsAt/" title="Returns an array of channels that are present for the specified pixel onscreen.">GetChannelsAt</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">List</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.SceneSegmentation.SceneSegmentationChannel/" title="Represents the different semantic segmentation channels that can be detected....">SceneSegmentationChannel</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Returns an array of channels that are present for the specified pixel onscreen.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getpackedscenesegmentationchannelstexture"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager.GetPackedSceneSegmentationChannelsTexture/" title="Retrieves the texture of semantic data where each pixel can be interpreted as a uint with bits...">GetPackedSceneSegmentationChannelsTexture</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Texture2D</a></span></span></td>
<td><div class="ctoken comment">
Retrieves the texture of semantic data where each pixel can be interpreted as a uint with bits<br />
corresponding to different classifications.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getscenesegmentation"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager.GetSceneSegmentation/" title="Returns the scene segmentation at the specified pixel on screen.">GetSceneSegmentation</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">uint</span></span></td>
<td><div class="ctoken comment">
Returns the scene segmentation at the specified pixel on screen.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getscenesegmentationchanneltexture"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager.GetSceneSegmentationChannelTexture/" title="Returns semantic segmentation texture for the specified semantic channel.">GetSceneSegmentationChannelTexture</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Texture2D</a></span></span></td>
<td><div class="ctoken comment">
Returns semantic segmentation texture for the specified semantic channel.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getsuppressionmasktexture"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager.GetSuppressionMaskTexture/" title="Retrieves the suppression mask texture, where each pixel contains a uint which can be used to interpolate...">GetSuppressionMaskTexture</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Texture2D</a></span></span></td>
<td><div class="ctoken comment">
Retrieves the suppression mask texture, where each pixel contains a uint which can be used to interpolate<br />
between the predicted depth and the far field depth of the scene. This is useful for enabling smooth occlusion suppression.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-tryacquirepackedscenesegmentationchannelscpuimage"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager.TryAcquirePackedSceneSegmentationChannelsCpuImage/" title="Tries to acquire the latest packed semantic channels XRCpuImage. Each element of the XRCpuImage is a bit field...">TryAcquirePackedSceneSegmentationChannelsCpuImage</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Tries to acquire the latest packed semantic channels XRCpuImage. Each element of the XRCpuImage is a bit field<br />
indicating which semantic channels have surpassed their respective detection confidence thresholds for that<br />
pixel. (See GetChannelIndex)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-tryacquirescenesegmentationchannelcpuimage"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager.TryAcquireSceneSegmentationChannelCpuImage/" title="Attempt to acquire the latest semantic segmentation XRCpuImage for the specified semantic class. This...">TryAcquireSceneSegmentationChannelCpuImage</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Attempt to acquire the latest semantic segmentation XRCpuImage for the specified semantic class. This<br />
provides direct access to the raw pixel data.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-tryacquiresuppressionmaskcpuimage"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager.TryAcquireSuppressionMaskCpuImage/" title="Tries to acquire the latest suppression mask XRCpuImage. Each element of the XRCpuImage is a uint32 value...">TryAcquireSuppressionMaskCpuImage</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Tries to acquire the latest suppression mask XRCpuImage. Each element of the XRCpuImage is a uint32 value<br />
which can be used to interpolate between instantaneous depth and far field depth.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-tryresetchannelconfidencethresholds"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager.TryResetChannelConfidenceThresholds/" title="Resets the confidence thresholds for all semantic channels to the default values from the current model.">TryResetChannelConfidenceThresholds</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Resets the confidence thresholds for all semantic channels to the default values from the current model.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-trysetchannelconfidencethresholds"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager.TrySetChannelConfidenceThresholds/" title="Sets the confidence threshold for including the specified semantic channel in the packed semantic...">TrySetChannelConfidenceThresholds</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Sets the confidence threshold for including the specified semantic channel in the packed semantic<br />
channel buffer.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-update"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationManager.Update/" title="Callback as the manager is being updated.">Update</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment">
Callback as the manager is being updated.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Events<a href="#events" class="hash-link" aria-label="Direct link to Events" title="Direct link to Events">​</a>

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
<td><span id="event-framereceived"></span><span class="ctoken-line"><span class="ctoken class-name">FrameReceived</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.action-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Action</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationFrameEventArgs/" title="A structure for camera-related information pertaining to a particular frame....">ARSceneSegmentationFrameEventArgs</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="event-metadatainitialized"></span><span class="ctoken-line"><span class="ctoken class-name">MetadataInitialized</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.action-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Action</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SceneSegmentation.ARSceneSegmentationModelEventArgs/" title="A structure for information about the semantic segmentation model that&#39;s become ready. This is used to...">ARSceneSegmentationModelEventArgs</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
An event which fires when the underlying subsystem has finished initializing.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
