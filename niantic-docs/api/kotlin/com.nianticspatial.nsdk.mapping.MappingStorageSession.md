---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.MappingStorageSession/
title: MappingStorageSession
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.mapping](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping/ "com.nianticspatial.nsdk.mapping") 

</div>

<div class="api-title">

#  MappingStorageSession

<div class="api-extends">

↳ extends [SessionBase](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.SessionBase/ "SessionBase") 

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">MappingStorageSession</span></span>

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
<td><span id="property-mapupdates"></span><span class="ctoken-line"><span class="ctoken class-name">mapUpdates</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/kotlinx.coroutines.flow.-flow" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Flow</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ByteArray</a></span><span class="ctoken plain">?</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Flow of map updates. This is the primary way to receive map updates in Kotlin.<br />
The Flow emits [ByteArray] whenever new map updates are available, or <code>null</code> if no update is available.<br />
This provides incremental updates to the map that have been made since the last update.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Functions<a href="#functions" class="hash-link" aria-label="Direct link to Functions" title="Direct link to Functions">​</a>

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
<td><span id="function-add"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.MappingStorageSession.add/" title="Add serialized map data to the map storage.">add</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Add serialized map data to the map storage.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-clear"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.MappingStorageSession.clear/" title="Clear the map storage....">clear</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Clear the map storage.<br />
Removes all stored map data and resets the storage to an empty state.<br />
&gt; Note: Must not be called if VPS is running.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-createrootanchor"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.MappingStorageSession.createRootAnchor/" title="Creates an anchor on the existing map located at the origin of the current AR session,...">createRootAnchor</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Creates an anchor on the existing map located at the origin of the current AR session,<br />
if possible.<br />
The root anchor represents the origin point of the map coordinate system and can be<br />
used with VPS for localization.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-extractmetadata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.MappingStorageSession.extractMetadata/" title="Extract the metadata from a map relative to a specified anchor....">extractMetadata</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.MapMetadata/" title="Browse to MapMetadata">MapMetadata</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Extract the metadata from a map relative to a specified anchor.<br />
Render the feature points in the metadata relative to the specified anchor to visualize the map.<br />
This is only possible when the anchor is linked directly to the map's node(s), or if the<br />
anchor's nodes are reachable to the map's nodes from the currently active transform graph.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getdata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.MappingStorageSession.getData/" title="Get the complete map data....">getData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ByteArray</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Get the complete map data.<br />
This function returns all the map data accumulated during the AR session, serialized as a<br />
DeviceMap protobuf. This data can be saved, shared, and/or used for localization.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getupdate"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.MappingStorageSession.getUpdate/" title="Get the latest map update data....">getUpdate</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ByteArray</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Get the latest map update data.<br />
This function returns the incremental map changes (new nodes and edges) that have been added<br />
since the last update, encoded as a DeviceMap protobuf.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-mergeupdate"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.MappingStorageSession.mergeUpdate/" title="Merge a map update into an existing map....">mergeUpdate</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ByteArray</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Merge a map update into an existing map.<br />
Combines incremental map updates with existing map data to create an updated complete<br />
map dataset.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-ondestroy"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.MappingStorageSession.onDestroy/" title="Browse to onDestroy">onDestroy</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-oninit"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.MappingStorageSession.onInit/" title="Browse to onInit">onInit</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
