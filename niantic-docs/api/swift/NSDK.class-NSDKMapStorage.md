---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKMapStorage/
title: NSDKMapStorage
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") 

</div>

<div class="api-title">

#  NSDKMapStorage

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">NSDKMapStorage</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

A storage system for managing device-generated maps. The map storage feature provides capabilities for capturing, storing, and managing map data from AR sessions. This data can be persisted and used for Visual Positioning System (VPS) localization and map updates.

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
<td><span id="method-addmap"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMapStorage.method-addMap/" title="Adds previously serialized map data to the map storage.">addMap</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Adds previously serialized map data to the map storage.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-clear"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMapStorage.method-clear/" title="Clears the map storage....">clear</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Clears the map storage.<br />
This method removes all stored map data and localization data
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-createrootanchor"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMapStorage.method-createRootAnchor/" title="Creates an anchor on the existing map located at the origin of the current AR session, if possible....">createRootAnchor</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Creates an anchor on the existing map located at the origin of the current AR session, if possible.<br />
The root anchor represents the origin point of the map coordinate system and can be<br />
used with VPS for localization.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-extractmapmetadata"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMapStorage.method-extractMapMetadata/" title="Extracts metadata from a map relative to a specified anchor....">extractMapMetadata</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-MapMetadata/" title="Structure representing the metadata of a device map for visualization and processing.">MapMetadata</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Extracts metadata from a map relative to a specified anchor.<br />
Render the feature points in the metadata relative to the specified anchor to visualize the map.<br />
This is only possible when the anchor is linked directly to the map's node(s), or if<br />
the anchor's nodes are reachable to the map's nodes from the currently active<br />
transform graph.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-mapdata"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMapStorage.method-mapData/" title="Gets the complete map data....">mapData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKBuffer/" title="A buffer containing binary data for NSDK operations....">NSDKBuffer</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Gets the complete map data.<br />
This function returns all the map data accumulated during the AR session, serialized as a<br />
DeviceMap protobuf. This data can be saved, shared, and/or used for localization.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-mapupdate"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMapStorage.method-mapUpdate/" title="Gets the latest map update data....">mapUpdate</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKBuffer/" title="A buffer containing binary data for NSDK operations....">NSDKBuffer</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Gets the latest map update data.<br />
This method returns the incremental map changes (new nodes and edges) that have been added<br />
since the last update.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-mergemapupdate"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMapStorage.method-mergeMapUpdate/" title="Merges a map update into an existing map....">mergeMapUpdate</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKBuffer/" title="A buffer containing binary data for NSDK operations....">NSDKBuffer</a></span></span></td>
<td><div class="ctoken comment">
Merges a map update into an existing map.<br />
This method combines incremental map updates with a base map to produce<br />
a merged map buffer containing the complete map data.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
