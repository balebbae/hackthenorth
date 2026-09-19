---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning/
title: NianticSpatial.NSDK.AR.Scanning
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

#  Scanning

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
<td><span id="class-arscanningmanager"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager/" title="A manager for recording scans of the AR scene for Playback....">ARScanningManager</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.0/api/UnityEngine.XR.ARFoundation.SubsystemLifecycleManager-3.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">SubsystemLifecycleManager</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem/" title="Defines an interface for interacting with scanning functionality.">XRScanningSubsystem</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystemDescriptor/" title="Browse to XRScanningSubsystemDescriptor">XRScanningSubsystemDescriptor</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem.Provider/" title="An abstract class to be implemented by providers of this subsystem.">Provider</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
A manager for recording scans of the AR scene for Playback.<br />
The recording will start when the manager is enabled.<br />
Use SaveScan() to stop and save the recording into the ScanPath.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-arscanqualityclassifier"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanQualityClassifier/" title="ARScanQualityClassifier is responsible for computing the scan quality....">ARScanQualityClassifier</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.IARScanQualityClassifier/" title="Browse to IARScanQualityClassifier">IARScanQualityClassifier</a></span></span></td>
<td><div class="ctoken comment">
ARScanQualityClassifier is responsible for computing the scan quality.<br />
- Run() will start a quality compute asynchronously.<br />
- CancelCurrentRun() will interrupt the current compute, if any.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-savedscan"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanStore.SavedScan/" title="Browse to SavedScan">SavedScan</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanStore.SavedScan/" title="Browse to SavedScan">SavedScan</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-scanarchivebuilder"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanArchiveBuilder/" title="Browse to ScanArchiveBuilder">ScanArchiveBuilder</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.idisposable?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">IDisposable</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-scanqualityresult"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanQualityResult/" title="Scan Quality Result.">ScanQualityResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanQualityResult/" title="Scan Quality Result.">ScanQualityResult</a></span></span></td>
<td><div class="ctoken comment">
Scan Quality Result.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-scanstore"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanStore/" title="Browse to ScanStore">ScanStore</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanStore/" title="Browse to ScanStore">ScanStore</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-uploaduserinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.UploadUserInfo/" title="Additional metadata relating to an uploaded scan.">UploadUserInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.UploadUserInfo/" title="Additional metadata relating to an uploaded scan.">UploadUserInfo</a></span></span></td>
<td><div class="ctoken comment">
Additional metadata relating to an uploaded scan.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Interfaces<a href="#interfaces" class="hash-link" aria-label="Direct link to Interfaces" title="Direct link to Interfaces">​</a>

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
<td><span id="interface-iarscanqualityclassifier"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.IARScanQualityClassifier/" title="Browse to IARScanQualityClassifier">IARScanQualityClassifier</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.idisposable?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">IDisposable</a></span></span></td>
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
<td><span id="struct-scanningsqcscores"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanningSqcScores/" title="This struct is used by publicly and internally....">ScanningSqcScores</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment">
This struct is used by publicly and internally.<br />
For internal usage, we will pass down an array of struct to native.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Enums<a href="#enums" class="hash-link" aria-label="Direct link to Enums" title="Direct link to Enums">​</a>

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
<td><span id="enum-scanqualitycategory"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanQualityCategory/" title="Scan quality categories....">ScanQualityCategory</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">uint</span></span></td>
<td><div class="ctoken comment">
Scan quality categories.<br />
Note, if changing this category, it needs to change the relevant native enum.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
