---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.Vps2LocalizationRequestStatus/
title: Vps2LocalizationRequestStatus
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

#  Vps2LocalizationRequestStatus

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">enum</span><span class="ctoken plain"> </span><span class="ctoken class-name">Vps2LocalizationRequestStatus</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">byte</span></span>

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
<td><span id="field-completed"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">Completed</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Vps2LocalizationRequestStatus</span></span></td>
<td><div class="ctoken comment">
The request completed and a response was received.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-failed"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">Failed</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Vps2LocalizationRequestStatus</span></span></td>
<td><div class="ctoken comment">
The request failed (e.g. network error, HTTP error, or unparseable response).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-framerejected"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">FrameRejected</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Vps2LocalizationRequestStatus</span></span></td>
<td><div class="ctoken comment">
The request was not sent because the frame was rejected (e.g. camera pointed downward).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-pending"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">Pending</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Vps2LocalizationRequestStatus</span></span></td>
<td><div class="ctoken comment">
The request has been sent and is awaiting a response.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-unknown"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">Unknown</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Vps2LocalizationRequestStatus</span></span></td>
<td><div class="ctoken comment">
Status is unknown or uninitialized.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
