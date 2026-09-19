---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKVps2Session.struct-Configuration/
title: Configuration
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKVps2Session](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKVps2Session/ "NSDKVps2Session") 

</div>

<div class="api-title">

#  Configuration

<div class="api-package">

Configuration for the VPS2 session.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">struct</span><span class="ctoken plain"> </span><span class="ctoken class-name">Configuration</span></span>

------------------------------------------------------------------------

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">init</span><span class="ctoken plain">(</span><span class="ctoken plain">universalLocalizationEnabled</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain">? = nil, </span><span class="ctoken plain">universalLocalizationRequestsPerSecond</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain">? = nil, </span><span class="ctoken plain">vpsMapLocalizationEnabled</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain">? = nil, </span><span class="ctoken plain">initialVpsRequestsPerSecond</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain">? = nil, </span><span class="ctoken plain">continuousVpsRequestsPerSecond</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain">? = nil, </span><span class="ctoken plain">geolocationSmoothingEnabled</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain">? = nil, </span><span class="ctoken plain">deviceMapLocalizationEnabled</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain">? = nil, </span><span class="ctoken plain">deviceMapLocalizationFramerate</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int32</a></span><span class="ctoken plain">? = nil, </span><span class="ctoken plain">universalLocalizationRequestTimeoutMs</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int32</a></span><span class="ctoken plain">? = nil, </span><span class="ctoken plain">maxRequestsInTransitPerTarget</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/uint32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UInt32</a></span><span class="ctoken plain">? = nil, </span><span class="ctoken plain">anchorDistanceGateMeters</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain">? = nil)</span></span>

</div>

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
<td><span id="property-anchordistancegatemeters"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">anchorDistanceGateMeters</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Distance gate in meters for anchor candidate filtering when geo-corrected.<br />
Nodes farther than this distance from the device are skipped during anchor localization.<br />
When only GPS is available (no geo-correction), the effective gate is 2x this value.<br />
Use 0 to apply the default value (50 meters geo-corrected, 100 meters GPS-only).<br />
Use -1 to disable the distance check entirely.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-continuousvpsrequestspersecond"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">continuousVpsRequestsPerSecond</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Number of VPS localization requests per second to send the server while<br />
successfully localized on a VPS map.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-devicemaplocalizationenabled"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">deviceMapLocalizationEnabled</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
Device maps are created by the on-device mapping feature. They do not provide<br />
a georeference.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-devicemaplocalizationframerate"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">deviceMapLocalizationFramerate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int32</a></span></span></td>
<td><div class="ctoken comment">
Number of times per second to attempt localization on available device maps.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-geolocationsmoothingenabled"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">geolocationSmoothingEnabled</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
If true, geolocation smoothing is enabled.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-initialvpsrequestspersecond"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">initialVpsRequestsPerSecond</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Number of VPS localiziation requests per second to send the server prior to first<br />
successful localization on a VPS map.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-maxrequestsintransitpertarget"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">maxRequestsInTransitPerTarget</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/uint32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UInt32</a></span></span></td>
<td><div class="ctoken comment">
Maximum number of concurrent localization requests per target.<br />
Limits how many in-flight cloud localization requests can be active for a single target<br />
simultaneously. Use 0 to apply the default value (2).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-universallocalizationenabled"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">universalLocalizationEnabled</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
If true, universal localization is enabled.<br />
Universal localization provides geographic positioning that works anywhere<br />
without requiring pre-scanning.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-universallocalizationrequestspersecond"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">universalLocalizationRequestsPerSecond</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Number of requests per second to send the cloud for universal localization.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-universallocalizationrequesttimeoutms"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">universalLocalizationRequestTimeoutMs</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int32</a></span></span></td>
<td><div class="ctoken comment">
Timeout in milliseconds for universal localization requests.<br />
Responses in uncached areas may take 60+ seconds; subsequent requests are typically<br />
under 1 second. Use 0 to apply the default value (90000 ms).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-vpsmaplocalizationenabled"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">vpsMapLocalizationEnabled</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
If true, VPS map localization is enabled.<br />
VPS maps only exist in pre-scanned areas. Your device must be localized on<br />
a VPS map in order for VPS anchors to be placed with high accuracy.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
