---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem.Provider/
title: Provider
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.XRSubsystems](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems/ "NianticSpatial.NSDK.AR.XRSubsystems") <span class="api-breadcrumbs-nav">←</span>[XRSceneSegmentationSubsystem](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem/ "NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem") 

</div>

<div class="api-title">

#  Provider

<div class="api-extends">

↳ extends UnityEngine.SubsystemsImplementation.SubsystemProvider

</div>

<div class="api-package">

The provider which will service the XRSceneSegmentationSubsystem.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">Provider</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemsImplementation.SubsystemProvider.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">SubsystemProvider</a></span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">[XRSceneSegmentationSubsystem](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem/ "Defines an interface for interacting with semantic segmentation functionality.")</span><span class="ctoken punctuation">\></span></span>

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
<td><span id="property-latestframeid"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">LatestFrameId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name keyword">uint</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-suppressionmaskchannels"></span><span class="ctoken-line"><span class="ctoken class-name">SuppressionMaskChannels</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.hashset-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">HashSet</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.SceneSegmentation.SceneSegmentationChannel/" title="Represents the different semantic segmentation channels that can be detected....">SceneSegmentationChannel</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Property to be implemented by the provider to get or set the list of suppression channels for the platform's semantic<br />
segmentation feature.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-targetframerate"></span><span class="ctoken-line"><span class="ctoken class-name">TargetFrameRate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">uint</span></span></td>
<td><div class="ctoken comment">
Property to be implemented by the provider to get or set the frame rate for the platform's semantic<br />
segmentation feature.
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
<td><span id="method-getchannels"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem.Provider.GetChannels/" title="Method to be implemented by the provider to get a list of the semantic channels for the current...">GetChannels</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ireadonlylist-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">IReadOnlyList</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.SceneSegmentation.SceneSegmentationChannel/" title="Represents the different semantic segmentation channels that can be detected....">SceneSegmentationChannel</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Method to be implemented by the provider to get a list of the semantic channels for the current<br />
semantic model.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-tryacquirepackedscenesegmentationchannelscpuimage"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem.Provider.TryAcquirePackedSceneSegmentationChannelsCpuImage/" title="Acquire the latest packed semantic channels XRCpuImage.">TryAcquirePackedSceneSegmentationChannelsCpuImage</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Acquire the latest packed semantic channels XRCpuImage.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-tryacquirescenesegmentationchannelcpuimage"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem.Provider.TryAcquireSceneSegmentationChannelCpuImage/" title="Acquire the latest semantic channel CPU image.">TryAcquireSceneSegmentationChannelCpuImage</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Acquire the latest semantic channel CPU image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-tryacquiresuppressionmaskcpuimage"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem.Provider.TryAcquireSuppressionMaskCpuImage/" title="Acquire the latest suppression mask XRCpuImage.">TryAcquireSuppressionMaskCpuImage</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Acquire the latest suppression mask XRCpuImage.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-trygetpackedscenesegmentationchannels"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem.Provider.TryGetPackedSceneSegmentationChannels/" title="Get the packed semantics texture descriptor.">TryGetPackedSceneSegmentationChannels</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Get the packed semantics texture descriptor.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-trygetscenesegmentationchannel"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem.Provider.TryGetSceneSegmentationChannel/" title="Get the XRTextureDescriptor for the specified semantic channel.">TryGetSceneSegmentationChannel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Get the XRTextureDescriptor for the specified semantic channel.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-trygetsuppressionmasktexture"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem.Provider.TryGetSuppressionMaskTexture/" title="Get a semantic suppression texture descriptor.">TryGetSuppressionMaskTexture</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Get a semantic suppression texture descriptor.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-trypreparesubsystem"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem.Provider.TryPrepareSubsystem/" title="If the semantic segmentation model is ready, prepare the subsystem&#39;s data structures.">TryPrepareSubsystem</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
If the semantic segmentation model is ready, prepare the subsystem's data structures.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-tryresetchannelconfidencethresholds"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem.Provider.TryResetChannelConfidenceThresholds/" title="Resets the confidence thresholds for all semantic channels to the default values from the current model.">TryResetChannelConfidenceThresholds</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Resets the confidence thresholds for all semantic channels to the default values from the current model.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-trysetchannelconfidencethresholds"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem.Provider.TrySetChannelConfidenceThresholds/" title="Sets the confidence threshold for including the specified semantic channel in the packed semantic...">TrySetChannelConfidenceThresholds</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Sets the confidence threshold for including the specified semantic channel in the packed semantic<br />
channel buffer.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
