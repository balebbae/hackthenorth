---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2GeolocationData/
title: Vps2GeolocationData
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.vps2](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2/ "com.nianticspatial.nsdk.vps2") 

</div>

<div class="api-title">

#  Vps2GeolocationData

<div class="api-package">

Geolocation data from VPS2 localization with accuracy information.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">data</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">Vps2GeolocationData</span></span>

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
<td><span id="property-altitude"></span><span class="ctoken-line"><span class="ctoken class-name">altitude</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Double</a></span></span></td>
<td><div class="ctoken comment">
Altitude in metres
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-heading"></span><span class="ctoken-line"><span class="ctoken class-name">heading</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Double</a></span></span></td>
<td><div class="ctoken comment">
Heading in degrees
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-horizontalaccuracymetres"></span><span class="ctoken-line"><span class="ctoken class-name">horizontalAccuracyMetres</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Horizontal accuracy in metres
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-latitude"></span><span class="ctoken-line"><span class="ctoken class-name">latitude</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Double</a></span></span></td>
<td><div class="ctoken comment">
Latitude in degrees
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-longitude"></span><span class="ctoken-line"><span class="ctoken class-name">longitude</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Double</a></span></span></td>
<td><div class="ctoken comment">
Longitude in degrees
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-orientationedn"></span><span class="ctoken-line"><span class="ctoken class-name">orientationEdn</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">FloatArray</a></span></span></td>
<td><div class="ctoken comment">
Orientation quaternion in ENU-to-device-north convention
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-rotationaccuracydeg"></span><span class="ctoken-line"><span class="ctoken class-name">rotationAccuracyDeg</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Rotation accuracy in degrees
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-trackingstate"></span><span class="ctoken-line"><span class="ctoken class-name">trackingState</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2TrackingState/" title="Tracking quality for VPS2 localization....">Vps2TrackingState</a></span></span></td>
<td><div class="ctoken comment">
The tracking state indicating availability and quality of the geolocation data
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-verticalaccuracymetres"></span><span class="ctoken-line"><span class="ctoken class-name">verticalAccuracyMetres</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Vertical accuracy in metres
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Functions<a href="#functions" class="hash-link" aria-label="Direct link to Functions" title="Direct link to Functions">​</a>

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
<td><span id="function-tolocation"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2GeolocationData.toLocation/" title="Converts this VPS2 geolocation to an Android [Location]....">toLocation</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Location</span></span></td>
<td><div class="ctoken comment">
Converts this VPS2 geolocation to an Android [Location].<br />
The returned [Location] has [Location.getProvider] set to [LOCATION_PROVIDER_VPS2],<br />
with [Location.getAccuracy] from [horizontalAccuracyMetres], [Location.getBearing] from<br />
[heading] (device orientation relative to true north), and on API 26+ vertical accuracy<br />
from [verticalAccuracyMetres] and bearing accuracy from [rotationAccuracyDeg].<br />
Timestamp is set to the time of conversion.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
