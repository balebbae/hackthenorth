---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.ScanningState/
title: ScanningState
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.XRSubsystems](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems/ "NianticSpatial.NSDK.AR.XRSubsystems") 

</div>

<div class="api-title">

#  ScanningState

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">enum</span><span class="ctoken plain"> </span><span class="ctoken class-name">ScanningState</span></span>

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
<td><span id="field-error"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">Error</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">ScanningState</span></span></td>
<td><div class="ctoken comment">
Scan processing has failed. From this state:<br />
- can be called to reset the scanner to the <em>Stopped</em> state.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-ready"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">Ready</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">ScanningState</span></span></td>
<td><div class="ctoken comment">
The scanner is created and ready to start. From this state:<br />
- can be called to begin scanning.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-saved"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">Saved</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">ScanningState</span></span></td>
<td><div class="ctoken comment">
The scan has been saved. From this state:<br />
- can be called to end the scan, transitioning to the <em>Stopped</em> state.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-saving"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">Saving</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">ScanningState</span></span></td>
<td><div class="ctoken comment">
The scan is currently being saved. From this state:<br />
- can be called to end the scan, transitioning to the <em>Stopped</em> state.<br />
- Automatically transitions to the "Saved" state when done.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-started"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">Started</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">ScanningState</span></span></td>
<td><div class="ctoken comment">
The scanner is started and scanning. From this state:<br />
- can be called to end the scan, transitioning to the <em>Stopped</em> state.<br />
- can be called to save the scan, transitioning to the <em>Saving</em> state.<br />
- can be called to discard the scan, transitioning to the <em>Discarding</em> state.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-stopped"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">Stopped</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">ScanningState</span></span></td>
<td><div class="ctoken comment">
Scanning is stopped. From this state:<br />
- can be called to re-start scanning, transitioning to the <em>Started</em> state.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-unknown"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">Unknown</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">ScanningState</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
