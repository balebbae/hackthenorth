---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.Scanning/
title: NianticSpatial.NSDK.AR.Subsystems.Scanning
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
<td><span id="class-nsdkscanningsubsystem"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.Scanning.NsdkScanningSubsystem/" title="The NSDK implementation of the XRScanningSubsystem. Do not create this directly....">NsdkScanningSubsystem</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem/" title="Defines an interface for interacting with scanning functionality.">XRScanningSubsystem</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">ISubsystemWithMutableApi</span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name">IApi</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
The NSDK implementation of the XRScanningSubsystem. Do not create this directly.<br />
Use the SubsystemManager instead.
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
<td><span id="struct-scannerconfigurationcstruct"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.Scanning.ScannerConfigurationCStruct/" title="C struct for C# to send frame data to C++. Defined in ardk_scanner_configuration.h file....">ScannerConfigurationCStruct</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment">
C struct for C# to send frame data to C++. Defined in ardk_scanner_configuration.h file.<br />
Note: It is not that great as we have both XRScanningConfiguration and this ScannerConfigurationCStruct.<br />
The reason why we don't move ScannerConfigurationCStruct into XRScanningConfiguration is for the benefits<br />
of decoupling internal and public code, and avoid easily breaking existing public contracts.
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
<td><span id="enum-recordingstatus"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.Scanning.RecordingStatus/" title="Browse to RecordingStatus">RecordingStatus</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.Scanning.RecordingStatus/" title="Browse to RecordingStatus">RecordingStatus</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
