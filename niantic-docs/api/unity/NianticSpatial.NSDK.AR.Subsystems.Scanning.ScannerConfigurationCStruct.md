---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.Scanning.ScannerConfigurationCStruct/
title: ScannerConfigurationCStruct
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Subsystems.Scanning](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.Scanning/ "NianticSpatial.NSDK.AR.Subsystems.Scanning") 

</div>

<div class="api-title">

#  ScannerConfigurationCStruct

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">struct</span><span class="ctoken plain"> </span><span class="ctoken class-name">ScannerConfigurationCStruct</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

C struct for C# to send frame data to C++. Defined in ardk_scanner_configuration.h file. Note: It is not that great as we have both XRScanningConfiguration and this ScannerConfigurationCStruct. The reason why we don't move ScannerConfigurationCStruct into XRScanningConfiguration is for the benefits of decoupling internal and public code, and avoid easily breaking existing public contracts.

------------------------------------------------------------------------

## Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

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
<td><span id="field-basepath"></span><span class="ctoken-line"><span class="ctoken class-name">BasePath</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-basepathlen"></span><span class="ctoken-line"><span class="ctoken class-name">BasePathLen</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-enablefullresolution"></span><span class="ctoken-line"><span class="ctoken class-name">EnableFullResolution</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-enableraycastvisualization"></span><span class="ctoken-line"><span class="ctoken class-name">EnableRaycastVisualization</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-enablevoxelvisualization"></span><span class="ctoken-line"><span class="ctoken class-name">EnableVoxelVisualization</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-fardepth"></span><span class="ctoken-line"><span class="ctoken class-name">FarDepth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-framerate"></span><span class="ctoken-line"><span class="ctoken class-name">Framerate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-fullresolutionframerate"></span><span class="ctoken-line"><span class="ctoken class-name">FullResolutionFramerate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-neardepth"></span><span class="ctoken-line"><span class="ctoken class-name">NearDepth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-raycastheight"></span><span class="ctoken-line"><span class="ctoken class-name">RaycastHeight</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-raycastwidth"></span><span class="ctoken-line"><span class="ctoken class-name">RaycastWidth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-recordallsensors"></span><span class="ctoken-line"><span class="ctoken class-name">RecordAllSensors</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-scantargetid"></span><span class="ctoken-line"><span class="ctoken class-name">ScanTargetId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-scantargetidlen"></span><span class="ctoken-line"><span class="ctoken class-name">ScanTargetIdLen</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-usemultidepth"></span><span class="ctoken-line"><span class="ctoken class-name">UseMultidepth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-voxelsize"></span><span class="ctoken-line"><span class="ctoken class-name">VoxelSize</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
