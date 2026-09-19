---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.API.VpsGraphOperationError/
title: VpsGraphOperationError
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.API](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.API/ "NianticSpatial.NSDK.AR.API") 

</div>

<div class="api-title">

#  VpsGraphOperationError

<div class="api-package">

Error codes returned by VPS graph-based functions.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">enum</span><span class="ctoken plain"> </span><span class="ctoken class-name">VpsGraphOperationError</span></span>

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
<td><span id="field-nogeoreferencedata"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">NoGeoreferenceData</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">VpsGraphOperationError</span></span></td>
<td><div class="ctoken comment">
Code returned when the VPS location that the device is localized to contains no nodes with georeference<br />
data. Currently, only publicly available VPS locations have georeference data.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-none"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">None</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">VpsGraphOperationError</span></span></td>
<td><div class="ctoken comment">
Code returned when no error has occurred.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-notinitialized"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">NotInitialized</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">VpsGraphOperationError</span></span></td>
<td><div class="ctoken comment">
Code returned when VPS is not initialized. Make sure the subsystem has been started.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-notlocalized"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">NotLocalized</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">VpsGraphOperationError</span></span></td>
<td><div class="ctoken comment">
Code returned when the device is not localized to any VPS location.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-notransformtotrackingnode"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">NoTransformToTrackingNode</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">VpsGraphOperationError</span></span></td>
<td><div class="ctoken comment">
Code returned when the device is not localized to a VPS location that contains the target node specified<br />
for the graph operation.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-targetnodenotfound"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">TargetNodeNotFound</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">VpsGraphOperationError</span></span></td>
<td><div class="ctoken comment">
Code returned when the VPS location that the device is localized to does not contain the target node<br />
specified for the graph operation.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
