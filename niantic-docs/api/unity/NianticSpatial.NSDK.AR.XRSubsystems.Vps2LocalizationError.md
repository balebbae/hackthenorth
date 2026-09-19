---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.Vps2LocalizationError/
title: Vps2LocalizationError
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

#  Vps2LocalizationError

<div class="api-package">

Possible errors from VPS2 localization operations.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">enum</span><span class="ctoken plain"> </span><span class="ctoken class-name">Vps2LocalizationError</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">byte</span></span>

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
<td><span id="field-authfailure"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">AuthFailure</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Vps2LocalizationError</span></span></td>
<td><div class="ctoken comment">
The API gateway rejected the request due to an authentication or authorization<br />
failure (e.g. missing, invalid, or revoked credentials).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-badcameraangle"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">BadCameraAngle</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Vps2LocalizationError</span></span></td>
<td><div class="ctoken comment">
The frame was rejected because the camera is pointing at the ground or sky<br />
(no horizon crossing).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-badnetworkconnection"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">BadNetworkConnection</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Vps2LocalizationError</span></span></td>
<td><div class="ctoken comment">
The device cannot connect to the server.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-badtracking"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">BadTracking</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Vps2LocalizationError</span></span></td>
<td><div class="ctoken comment">
The frame was rejected because tracking state is not normal.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-internalclient"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">InternalClient</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Vps2LocalizationError</span></span></td>
<td><div class="ctoken comment">
The server sent a response that could not be parsed by the client.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-internalserver"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">InternalServer</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Vps2LocalizationError</span></span></td>
<td><div class="ctoken comment">
The server could not process the request due to an internal error,<br />
not due to malformed input.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-localizationfailed"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">LocalizationFailed</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Vps2LocalizationError</span></span></td>
<td><div class="ctoken comment">
The server processed the request but localization failed.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-nomapfound"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">NoMapFound</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Vps2LocalizationError</span></span></td>
<td><div class="ctoken comment">
The server could not find a map near the request GPS location.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-none"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">None</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Vps2LocalizationError</span></span></td>
<td><div class="ctoken comment">
No error has occurred.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-permissiondenied"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">PermissionDenied</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Vps2LocalizationError</span></span></td>
<td><div class="ctoken comment">
The server denied permission for the request.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-quotaexceeded"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">QuotaExceeded</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Vps2LocalizationError</span></span></td>
<td><div class="ctoken comment">
The API gateway rejected the request because the account or project quota<br />
has been exceeded (HTTP 429).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-requestslimitexceeded"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">RequestsLimitExceeded</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Vps2LocalizationError</span></span></td>
<td><div class="ctoken comment">
The request rate limit has been exceeded.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-unknown"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">Unknown</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Vps2LocalizationError</span></span></td>
<td><div class="ctoken comment">
Error is unknown or uninitialized.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
