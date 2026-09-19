---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2/
title: com.nianticspatial.nsdk.vps2
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") 

</div>

<div class="api-title">

#  vps2

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
<td><span id="class-vps2session"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session/" title="A session for VPS2 localization.">Vps2Session</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session/" title="A session for VPS2 localization.">Vps2Session</a></span></span></td>
<td><div class="ctoken comment">
A session for VPS2 localization.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Data Classes<a href="#data-classes" class="hash-link" aria-label="Direct link to Data Classes" title="Direct link to Data Classes">​</a>

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
<td><span id="data class-vps2geolocationdata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2GeolocationData/" title="Geolocation data from VPS2 localization with accuracy information.">Vps2GeolocationData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2GeolocationData/" title="Geolocation data from VPS2 localization with accuracy information.">Vps2GeolocationData</a></span></span></td>
<td><div class="ctoken comment">
Geolocation data from VPS2 localization with accuracy information.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-vps2localization"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Localization/" title="Spatial mapping between the device&#39;s AR coordinate space and real-world...">Vps2Localization</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Localization/" title="Spatial mapping between the device&#39;s AR coordinate space and real-world...">Vps2Localization</a></span></span></td>
<td><div class="ctoken comment">
Spatial mapping between the device's AR coordinate space and real-world<br />
geolocation, as determined by VPS2.<br />
If [trackingState] is [Vps2TrackingState.UNAVAILABLE], conversions are<br />
invalid and native conversion APIs will throw<br />
<code>ArdkInvalidOperationStatusException</code>.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-vps2localizationrequestrecord"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2LocalizationRequestRecord/" title="Diagnostics record describing a VPS2 localization request....">Vps2LocalizationRequestRecord</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2LocalizationRequestRecord/" title="Diagnostics record describing a VPS2 localization request....">Vps2LocalizationRequestRecord</a></span></span></td>
<td><div class="ctoken comment">
Diagnostics record describing a VPS2 localization request.<br />
The identifier is a 32-byte ASCII hex string (uppercase) returned by native.
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
<td><span id="enum-headingmode"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.HeadingMode/" title="Controls how the heading is computed from the device&#39;s orientation....">HeadingMode</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.HeadingMode/" title="Controls how the heading is computed from the device&#39;s orientation....">HeadingMode</a></span></span></td>
<td><div class="ctoken comment">
Controls how the heading is computed from the device's orientation.<br />
Mirrors <code>ARDK_HeadingMode</code>.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-vps2localizationerror"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2LocalizationError/" title="Error codes from VPS localization operations....">Vps2LocalizationError</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2LocalizationError/" title="Error codes from VPS localization operations....">Vps2LocalizationError</a></span></span></td>
<td><div class="ctoken comment">
Error codes from VPS localization operations.<br />
Mirrors <code>ARDK_VPS2_LocalizationError</code>.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-vps2localizationrequeststatus"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2LocalizationRequestStatus/" title="Localization request lifecycle status....">Vps2LocalizationRequestStatus</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2LocalizationRequestStatus/" title="Localization request lifecycle status....">Vps2LocalizationRequestStatus</a></span></span></td>
<td><div class="ctoken comment">
Localization request lifecycle status.<br />
Mirrors <code>ARDK_VPS2_LocalizationRequestStatus</code>.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-vps2localizationrequesttype"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2LocalizationRequestType/" title="VPS2 localization request type....">Vps2LocalizationRequestType</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2LocalizationRequestType/" title="VPS2 localization request type....">Vps2LocalizationRequestType</a></span></span></td>
<td><div class="ctoken comment">
VPS2 localization request type.<br />
Mirrors <code>ARDK_VPS2_LocalizationRequestType</code>.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-vps2trackingstate"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2TrackingState/" title="Tracking quality for VPS2 localization....">Vps2TrackingState</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2TrackingState/" title="Tracking quality for VPS2 localization....">Vps2TrackingState</a></span></span></td>
<td><div class="ctoken comment">
Tracking quality for VPS2 localization.<br />
Mirrors <code>ARDK_VPS2_TrackingState</code>.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
