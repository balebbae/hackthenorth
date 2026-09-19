---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem.Provider/
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

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.XRSubsystems](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems/ "NianticSpatial.NSDK.AR.XRSubsystems") <span class="api-breadcrumbs-nav">←</span>[XRScanningSubsystem](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem/ "NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem") 

</div>

<div class="api-title">

#  Provider

<div class="api-extends">

↳ extends UnityEngine.SubsystemsImplementation.SubsystemProvider

</div>

<div class="api-package">

An abstract class to be implemented by providers of this subsystem.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">Provider</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemsImplementation.SubsystemProvider.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">SubsystemProvider</a></span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">[XRScanningSubsystem](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem/ "Defines an interface for interacting with scanning functionality.")</span><span class="ctoken punctuation">\></span></span>

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
<td><span id="property-currentconfiguration"></span><span class="ctoken-line"><span class="ctoken class-name">CurrentConfiguration</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningConfiguration/" title="Configuration for scanning.">XRScanningConfiguration</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
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
<td><span id="method-computevoxels"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem.Provider.ComputeVoxels/" title="Browse to ComputeVoxels">ComputeVoxels</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-discardcurrentscan"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem.Provider.DiscardCurrentScan/" title="Browse to DiscardCurrentScan">DiscardCurrentScan</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-disposevoxelbuffer"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem.Provider.DisposeVoxelBuffer/" title="Browse to DisposeVoxelBuffer">DisposeVoxelBuffer</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getframecount"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem.Provider.GetFrameCount/" title="Browse to GetFrameCount">GetFrameCount</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getscanid"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem.Provider.GetScanId/" title="Get the current scan&#39;s ID.">GetScanId</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
Get the current scan's ID.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getstate"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem.Provider.GetState/" title="Browse to GetState">GetState</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.ScanningState/" title="Browse to ScanningState">ScanningState</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getvoxelsize"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem.Provider.GetVoxelSize/" title="Browse to GetVoxelSize">GetVoxelSize</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-savecurrentscan"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem.Provider.SaveCurrentScan/" title="Browse to SaveCurrentScan">SaveCurrentScan</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-trygetraycastbuffer"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem.Provider.TryGetRaycastBuffer/" title="Browse to TryGetRaycastBuffer">TryGetRaycastBuffer</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-trygetvoxelbuffer"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem.Provider.TryGetVoxelBuffer/" title="Browse to TryGetVoxelBuffer">TryGetVoxelBuffer</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
