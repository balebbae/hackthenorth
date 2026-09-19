---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping.ARDeviceMappingManager/
title: ARDeviceMappingManager
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Mapping](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping/ "NianticSpatial.NSDK.AR.Mapping") 

</div>

<div class="api-title">

#  ARDeviceMappingManager

<div class="api-extends">

↳ extends UnityEngine.XR.ARFoundation.SubsystemLifecycleManager

</div>

<div class="api-package">

ARDeviceMappingManager can be used to create and manage maps on the local device.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">ARDeviceMappingManager</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.0/api/UnityEngine.XR.ARFoundation.SubsystemLifecycleManager-3.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">SubsystemLifecycleManager</a></span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">[XRDeviceMappingSubsystem](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRDeviceMappingSubsystem/ "Browse to XRDeviceMappingSubsystem")</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">[XRDeviceMappingSubsystemDescriptor](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRDeviceMappingSubsystemDescriptor/ "Browse to XRDeviceMappingSubsystemDescriptor")</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">[Provider](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRDeviceMappingSubsystem.Provider/ "Browse to Provider")</span><span class="ctoken punctuation">\></span></span>

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
<td><span id="property-ismappinginprogress"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">IsMappingInProgress</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
A state if mapping is in progress or not. True is mapping is ongoing. Becomes false after calling StopMapping()
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-mappingsplittermaxdistancemeters"></span><span class="ctoken-line"><span class="ctoken class-name">MappingSplitterMaxDistanceMeters</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
Property access for map splitting criteria by distance
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-mappingsplittermaxdurationseconds"></span><span class="ctoken-line"><span class="ctoken class-name">MappingSplitterMaxDurationSeconds</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
Property access for map splitting criteria by time
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-mappingtargetframerate"></span><span class="ctoken-line"><span class="ctoken class-name">MappingTargetFrameRate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">uint</span></span></td>
<td><div class="ctoken comment">
Property access for mapping speed
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-rootanchorpayload"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">RootAnchorPayload</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
Get the root anchor payload if one has been created (as base64-encoded string).
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
<td><span id="method-clearmap"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping.ARDeviceMappingManager.ClearMap/" title="Browse to ClearMap">ClearMap</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-extractmapmetadatafromrootanchor"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping.ARDeviceMappingManager.ExtractMapMetadataFromRootAnchor/" title="Extract the metadata from a map relative to the stored root anchor.">ExtractMapMetadataFromRootAnchor</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Extract the metadata from a map relative to the stored root anchor.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-startmapping"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping.ARDeviceMappingManager.StartMapping/" title="Start map generation">StartMapping</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment">
Start map generation
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-stopmapping"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping.ARDeviceMappingManager.StopMapping/" title="Stop map generation">StopMapping</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment">
Stop map generation
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-trygetmapdata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping.ARDeviceMappingManager.TryGetMapData/" title="Browse to TryGetMapData">TryGetMapData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
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
<td><span id="event-mapfinalized"></span><span class="ctoken-line"><span class="ctoken class-name">MapFinalized</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.action-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Action</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name keyword">byte</span><span class="ctoken punctuation">[</span><span class="ctoken punctuation">]</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
An event when device map is finalized and ready to save
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="event-mapupdated"></span><span class="ctoken-line"><span class="ctoken class-name">MapUpdated</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.action-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Action</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name keyword">byte</span><span class="ctoken punctuation">[</span><span class="ctoken punctuation">]</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
An event when device map data has been updated. The surfaced map contains only the parts of the map that<br />
were updated since the last time this event was invoked. Use TryGetMapData to get the entire map.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
