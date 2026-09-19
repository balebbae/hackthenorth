---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping.DeviceMapAccessController/
title: DeviceMapAccessController
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

#  DeviceMapAccessController

<div class="api-package">

Class to access primitive device map data and configs.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">DeviceMapAccessController</span></span>

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
<td><span id="method-acquire"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping.DeviceMapAccessController.Acquire/" title="Gets or creates the shared map access object.">Acquire</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">DeviceMapAccessController</span></span></td>
<td><div class="ctoken comment">
Gets or creates the shared map access object.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-addmap"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping.DeviceMapAccessController.AddMap/" title="Add serialized map data to the map storage.">AddMap</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Add serialized map data to the map storage.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-cleardevicemaps"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping.DeviceMapAccessController.ClearDeviceMaps/" title="Clear map storage.">ClearDeviceMaps</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Clear map storage.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-createrootanchor"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping.DeviceMapAccessController.CreateRootAnchor/" title="Creates an anchor on the existing map located at the origin of the current...">CreateRootAnchor</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Creates an anchor on the existing map located at the origin of the current<br />
AR session, if possible.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-extractmapmetadatafromanchor"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping.DeviceMapAccessController.ExtractMapMetadataFromAnchor/" title="Extract the metadata from a map relative to an anchor on the map.">ExtractMapMetadataFromAnchor</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Extract the metadata from a map relative to an anchor on the map.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getmapdata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping.DeviceMapAccessController.GetMapData/" title="Get the current map data.">GetMapData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Get the current map data.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getmapupdate"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping.DeviceMapAccessController.GetMapUpdate/" title="Get the latest map update data, which consists of the new nodes and edges...">GetMapUpdate</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Get the latest map update data, which consists of the new nodes and edges<br />
that have been added since the last call to this function.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-mergemapupdate"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping.DeviceMapAccessController.MergeMapUpdate/" title="Merge a map update into an existing map.">MergeMapUpdate</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Merge a map update into an existing map.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-release"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Mapping.DeviceMapAccessController.Release/" title="Browse to Release">Release</a></span></span></td>
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
