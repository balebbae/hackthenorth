---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession/
title: ScanningSession
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.scanning](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning/ "com.nianticspatial.nsdk.scanning") 

</div>

<div class="api-title">

#  ScanningSession

<div class="api-extends">

↳ extends [SessionBase](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.SessionBase/ "SessionBase") 

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">ScanningSession</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

A session for 3D scanning and visualization functionality. The scanning feature capabilities for capturing, processing, and exporting 3D scan data from AR sessions. Scans of a location can be processed by the Visual Positioning System's (VPS's) cloud services to enable VPS localization.

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
<td><span id="function-computevoxels"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession.computeVoxels/" title="Compute the voxelization of the scanned scene....">computeVoxels</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Compute the voxelization of the scanned scene.<br />
Processing is asynchronous. Call this function and then call [voxelBuffer]<br />
to retrieve voxel data.<br />
&gt; Note: Voxel visualization must have been enabled in the configuration.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-configure"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession.configure/" title="Configure the session with the specified settings....">configure</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Configure the session with the specified settings.<br />
&gt; Note: It is only valid to call this when the session is stopped.<br />
&gt; Note: Configuration is asynchronous and can fail later, even if this call<br />
does not throw an error. Use [getFeatureStatus()] to check there are no issues.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-create"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession.create/" title="Browse to create">create</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-exportscan"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession.exportScan/" title="Exports the scan data as an archive file....">exportScan</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Exports the scan data as an archive file.<br />
This method processes the saved scan data and exports it to a standard archive format<br />
that can be used with external 3D processing tools or Niantic's VPS map.<br />
&gt; Note: This function is blocking and may take a while to execute. See<br />
[RecordingExporter] for a non-blocking option.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-featurestatus"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession.featureStatus/" title="Reports errors that have occurred with processes running inside this feature....">featureStatus</a></span></span></td>
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
<td><span id="function-getrecordinginfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession.getRecordingInfo/" title="Browse to getRecordingInfo">getRecordingInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.RecordingInfo/" title="Browse to RecordingInfo">RecordingInfo</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-ondestroy"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession.onDestroy/" title="Browse to onDestroy">onDestroy</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-oninit"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession.onInit/" title="Browse to onInit">onInit</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-raycastbuffer"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession.raycastBuffer/" title="Get the most recently computed raycast buffers....">raycastBuffer</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.RaycastBuffer/" title="A read-only container for the raycast buffer information generated during scanning.">RaycastBuffer</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Get the most recently computed raycast buffers.<br />
Once the session has been started and all the requested data has been sent through the<br />
ARDK session, a buffer should become available after a brief computation period.<br />
&gt; Note: Raycast visualization must have been enabled in the configuration.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-save"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession.save/" title="Asynchronously saves the current scan and polls until the operation is complete....">save</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AsyncResult/" title="Represents the final result of a completed asynchronous operation, which can either be...">AsyncResult</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ScanSaveInfo/" title="Information about a saved scan....">ScanSaveInfo</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ScanSaveError/" title="Error codes that can be returned when a scan fails to save.">ScanSaveError</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Asynchronously saves the current scan and polls until the operation is complete.<br />
This function initiates the save operation and then suspends until the save<br />
process finishes, either with a success, a failure, or a timeout.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-start"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession.start/" title="Start scanning....">start</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Start scanning.<br />
"Scanning" here refers to up to three processes: recording the input AR<br />
data, raycasting, and voxelization, depending on how the feature is<br />
configured.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-stop"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession.stop/" title="Stop all scanning processes....">stop</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Stop all scanning processes.<br />
This halts active scanning while keeping the scanner instance alive.<br />
You can restart scanning later with [start].<br />
&gt; Note: If recording is in progress, this will stop recording (and all other<br />
processes) and discard any unsaved scan data.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-voxelbuffer"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession.voxelBuffer/" title="Get the most recently computed voxel data....">voxelBuffer</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.VoxelBuffer/" title="A read-only container for the voxel buffer information generated during scanning.">VoxelBuffer</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Get the most recently computed voxel data.<br />
Once the session has been started and all the requested data has been sent through the<br />
ARDK session, a new buffer should become available after a brief computation period after<br />
[computeVoxels] has been called.<br />
&gt; Note: Voxel visualization must have been enabled in the configuration.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
