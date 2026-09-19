---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ScanSaveState/
title: ScanSaveState
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk/ "com.nianticspatial.nsdk") 

</div>

<div class="api-title">

#  ScanSaveState

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">enum</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">ScanSaveState</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Enumeration of possible scan recording save states. This enum represents the current state of a scan recording operation, indicating whether the scan data has been successfully saved, discarded, or failed.

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
<td><span id="property-value"></span><span class="ctoken-line"><span class="ctoken class-name keyword">value</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Cases<a href="#cases" class="hash-link" aria-label="Direct link to Cases" title="Direct link to Cases">​</a>

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
<td><span id="case-discarded"></span><span class="ctoken-line"><span class="ctoken class-name">DISCARDED</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">DISCARDED</span></span></td>
<td><div class="ctoken comment">
Recording was discarded
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-failed_to_save"></span><span class="ctoken-line"><span class="ctoken class-name">FAILED_TO_SAVE</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">FAILED_TO_SAVE</span></span></td>
<td><div class="ctoken comment">
Recording failed to save
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-not_available"></span><span class="ctoken-line"><span class="ctoken class-name">NOT_AVAILABLE</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">NOT_AVAILABLE</span></span></td>
<td><div class="ctoken comment">
Save state is not available
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-saved"></span><span class="ctoken-line"><span class="ctoken class-name">SAVED</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">SAVED</span></span></td>
<td><div class="ctoken comment">
Recording was saved successfully
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
