---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRVps2LocalizationRequestRecord/
title: XRVps2LocalizationRequestRecord
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

#  XRVps2LocalizationRequestRecord

<div class="api-package">

Diagnostic information about a VPS2 network request.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">struct</span><span class="ctoken plain"> </span><span class="ctoken class-name">XRVps2LocalizationRequestRecord</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span>

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
<td><span id="field-endtimems"></span><span class="ctoken-line"><span class="ctoken class-name">EndTimeMs</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">ulong</span></span></td>
<td><div class="ctoken comment">
Time that the response was received, in milliseconds. It is only comparable<br />
to StartTimeMs.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-errorcode"></span><span class="ctoken-line"><span class="ctoken class-name">ErrorCode</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.Vps2LocalizationError/" title="Possible errors from VPS2 localization operations.">Vps2LocalizationError</a></span></span></td>
<td><div class="ctoken comment">
Error code, if any
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-frameid"></span><span class="ctoken-line"><span class="ctoken class-name">FrameId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">ulong</span></span></td>
<td><div class="ctoken comment">
Id of the frame containing data sent in the request, if available.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-requestid"></span><span class="ctoken-line"><span class="ctoken class-name">RequestId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.guid?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Guid</a></span></span></td>
<td><div class="ctoken comment">
Unique request identifier
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-requesttype"></span><span class="ctoken-line"><span class="ctoken class-name">RequestType</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.Vps2LocalizationRequestType/" title="Browse to Vps2LocalizationRequestType">Vps2LocalizationRequestType</a></span></span></td>
<td><div class="ctoken comment">
Type of request sent
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-starttimems"></span><span class="ctoken-line"><span class="ctoken class-name">StartTimeMs</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">ulong</span></span></td>
<td><div class="ctoken comment">
Time that the request was sent, in milliseconds. It is only comparable<br />
to EndTimeMs.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-status"></span><span class="ctoken-line"><span class="ctoken class-name">Status</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.Vps2LocalizationRequestStatus/" title="Browse to Vps2LocalizationRequestStatus">Vps2LocalizationRequestStatus</a></span></span></td>
<td><div class="ctoken comment">
Request status
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
<td><span id="method-tostring"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRVps2LocalizationRequestRecord.ToString/" title="Browse to ToString">ToString</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
