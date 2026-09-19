---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Vps2Config/
title: Vps2Config
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

#  Vps2Config

<div class="api-package">

Configuration structure for the VPS2 session.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">Vps2Config</span></span>

## See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

- Vps2Session.configure

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
<td><span id="property-anchordistancegatemeters"></span><span class="ctoken-line"><span class="ctoken class-name">anchorDistanceGateMeters</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Distance gate in meters for anchor candidate filtering when geo-corrected.<br />
Nodes farther than this distance from the device are skipped during anchor localization.<br />
When only GPS is available (no geo-correction), the effective gate is 2x this value.<br />
Use 0 to apply the default value (50m geo-corrected, 100m GPS-only).<br />
Use -1 to disable the distance check entirely.<br />
<strong>Default:</strong> 0 (uses native default of 50m geo-corrected / 100m GPS-only)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-continuousvpsrequestspersecond"></span><span class="ctoken-line"><span class="ctoken class-name">continuousVpsRequestsPerSecond</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Number of VPS localization requests per second to send the server while successfully<br />
localized on a VPS map.<br />
<strong>Default:</strong> 0.2f (native default)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-devicemaplocalizationframerate"></span><span class="ctoken-line"><span class="ctoken class-name">deviceMapLocalizationFramerate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
Number of times per second to attempt localization on available device maps.<br />
<strong>Default:</strong> 10 (native default)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-enabledevicemaplocalization"></span><span class="ctoken-line"><span class="ctoken class-name">enableDeviceMapLocalization</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Boolean</a></span></span></td>
<td><div class="ctoken comment">
If true, localization on device maps is enabled.<br />
Device maps are created by the on-device mapping feature. They do not provide<br />
a georeference.<br />
<strong>Default:</strong> false (native default)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-enablegeolocationsmoothing"></span><span class="ctoken-line"><span class="ctoken class-name">enableGeolocationSmoothing</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Boolean</a></span></span></td>
<td><div class="ctoken comment">
If true, geolocation smoothing is enabled.<br />
<strong>Default:</strong> true (native default)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-enableuniversallocalization"></span><span class="ctoken-line"><span class="ctoken class-name">enableUniversalLocalization</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Boolean</a></span></span></td>
<td><div class="ctoken comment">
If true, universal localization is enabled.<br />
Universal localization provides geographic positioning that works anywhere without requiring<br />
pre-scanned maps.<br />
<strong>Default:</strong> false (native default is applied if you leave this unset/zeroed).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-enablevpsmaplocalization"></span><span class="ctoken-line"><span class="ctoken class-name">enableVpsMapLocalization</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Boolean</a></span></span></td>
<td><div class="ctoken comment">
If true, VPS map localization is enabled.<br />
VPS maps only exist in pre-scanned areas. Your device must be localized on a VPS map in order<br />
for VPS anchors to be placed with high accuracy.<br />
<strong>Default:</strong> true (native default)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-initialvpsrequestspersecond"></span><span class="ctoken-line"><span class="ctoken class-name">initialVpsRequestsPerSecond</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Number of VPS localization requests per second to send the server prior to the first<br />
successful localization on a VPS map.<br />
<strong>Default:</strong> 1.0f (native default)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-maxrequestsintransitpertarget"></span><span class="ctoken-line"><span class="ctoken class-name">maxRequestsInTransitPerTarget</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
Maximum number of concurrent localization requests per target.<br />
Limits how many in-flight cloud localization requests can be active for a single target<br />
simultaneously. Use 0 to apply the default value (2).<br />
<strong>Default:</strong> 0 (uses native default of 2)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-universallocalizationrequestspersecond"></span><span class="ctoken-line"><span class="ctoken class-name">universalLocalizationRequestsPerSecond</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Number of requests per second to send to server for universal localization.<br />
<strong>Default:</strong> 1.0f (native default)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-universallocalizationrequesttimeoutms"></span><span class="ctoken-line"><span class="ctoken class-name">universalLocalizationRequestTimeoutMs</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
Timeout in milliseconds for universal localization requests.<br />
Responses in uncached areas may take 60+ seconds; subsequent requests are typically under<br />
1 second. Use 0 to apply the default value (90000 ms).<br />
<strong>Default:</strong> 90000 (90 seconds)
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
