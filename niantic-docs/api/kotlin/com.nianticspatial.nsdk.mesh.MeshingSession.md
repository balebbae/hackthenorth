---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mesh.MeshingSession/
title: MeshingSession
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.mesh](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mesh/ "com.nianticspatial.nsdk.mesh") 

</div>

<div class="api-title">

#  MeshingSession

<div class="api-extends">

↳ extends [SessionBase](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.SessionBase/ "SessionBase") 

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">MeshingSession</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

A session for real-time 3D mesh generation from AR data. The meshing feature provides capabilities for processing AR session data and generating a triangle mesh representation of the physical environment in real-time. The mesh is divided into chunks that can be individually queried and updated as the environment is scanned.

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
<td><span id="property-meshupdates"></span><span class="ctoken-line"><span class="ctoken class-name">meshUpdates</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/kotlinx.coroutines.flow.-flow" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Flow</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.MeshingUpdateInfo/" title="Browse to MeshingUpdateInfo">MeshingUpdateInfo</a></span><span class="ctoken plain">?</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Flow of mesh updates.<br />
The Flow emits [MeshingUpdateInfo] whenever the mesh update timestamp changes,<br />
indicating that mesh chunks have been updated. The value may be null if there<br />
are no chunks available.<br />
<strong>Warning:</strong> Do not use this Flow together with manually calling [getUpdatedInfos].<br />
The Flow internally polls this method, and mixing manual calls with the Flow can<br />
cause updates to desynchronize. This happens because calling [getData] resets the<br />
updated flag for mesh chunks, so depending on which side calls [getData] first, the<br />
other side may miss updates or receive stale data. Use either the Flow API or the<br />
manual polling methods, but not both.
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
<td><span id="function-configure"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mesh.MeshingSession.configure/" title="Configures the meshing feature with the specified settings....">configure</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Configures the meshing feature with the specified settings.<br />
&gt; Note: If this method is called while meshing is running, the meshing feature will<br />
restart with the new configuration, and any mesh data that has been produced will<br />
be lost.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-featurestatus"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mesh.MeshingSession.featureStatus/" title="Reports errors that have occurred with processes running inside this feature....">featureStatus</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.FeatureStatus/" title="Browse to FeatureStatus">FeatureStatus</a></span></span></td>
<td><div class="ctoken comment">
Reports errors that have occurred with processes running inside this feature.<br />
Check this periodically to see if any errors have occurred with<br />
processes running inside this feature. Once an error has been<br />
flagged, it will remain flagged until the culprit process has<br />
been run again and completed successfully.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getdata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mesh.MeshingSession.getData/" title="Gets the data for a single mesh chunk....">getData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.MeshData/" title="Browse to MeshData">MeshData</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Gets the data for a single mesh chunk.<br />
Calling this function will reset the updated flag for the mesh chunk; i.e. after<br />
calling this function, future calls of [getUpdatedInfos] will only mark the<br />
chunk with <code>id</code> as having updated if its mesh data has changed since the call to<br />
this function.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getlastupdatetime"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mesh.MeshingSession.getLastUpdateTime/" title="Gets the timestamp of the latest mesh update.">getLastUpdateTime</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Long</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Gets the timestamp of the latest mesh update.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getupdatedinfos"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mesh.MeshingSession.getUpdatedInfos/" title="Gets the ids of all chunks in the current mesh and their update status....">getUpdatedInfos</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.MeshingUpdateInfo/" title="Browse to MeshingUpdateInfo">MeshingUpdateInfo</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Gets the ids of all chunks in the current mesh and their update status.<br />
The returned information contains the IDs and update status for all chunks currently<br />
in the mesh. If a chunk's updated flag is true, the mesh chunk has been updated since<br />
the last time its data was read with [getData].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-ondestroy"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mesh.MeshingSession.onDestroy/" title="Browse to onDestroy">onDestroy</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-oninit"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mesh.MeshingSession.onInit/" title="Browse to onInit">onInit</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-start"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mesh.MeshingSession.start/" title="Starts the meshing feature....">start</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Starts the meshing feature.<br />
The feature will begin processing input data and building a mesh according to the<br />
configuration.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-stop"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mesh.MeshingSession.stop/" title="Stops the meshing feature....">stop</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Stops the meshing feature.<br />
&gt; Note: This will clear the mesh data.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
