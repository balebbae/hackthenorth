---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKVps2Session.method-getPose/
title: getPose
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

#  getPose

<div class="api-package">

Converts a geolocation to an AR pose using the provided localization snapshot.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">getPose</span><span class="ctoken plain">(</span><span class="ctoken plain">localization</span><span class="ctoken plain">: </span><span class="ctoken class-name">[Vps2Localization](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2Localization/ "Spatial mapping between the device's AR coordinate space and real-world...")</span><span class="ctoken plain">, </span><span class="ctoken plain">location</span><span class="ctoken plain">: </span><span class="ctoken class-name">[GeolocationData](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-GeolocationData/ "Struct representing geolocation data including latitude, longitude, altitude,...")</span><span class="ctoken plain">) -\> </span><span class="ctoken class-name">[Vps2Pose](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2Pose/ "Pose in AR coordinate space calculated by VPS2 from a geolocation.")</span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Converts a geolocation to an AR pose using the provided localization snapshot.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The pose in ARKit coordinate space corresponding to the given geolocation,\
or `nil` if unavailable.

</div>

### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

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
<td><span id="external parameter-localization"></span><span class="ctoken-line"><span class="ctoken class-name">localization</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2Localization/" title="Spatial mapping between the device&#39;s AR coordinate space and real-world...">Vps2Localization</a></span></span></td>
<td><div class="ctoken comment">
The localization to use for the conversion.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-location"></span><span class="ctoken-line"><span class="ctoken class-name">location</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-GeolocationData/" title="Struct representing geolocation data including latitude, longitude, altitude,...">GeolocationData</a></span></span></td>
<td><div class="ctoken comment">
The geolocation to convert.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Overload 1<a href="#overload-1" class="hash-link" aria-label="Direct link to Overload 1" title="Direct link to Overload 1">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">getPose</span><span class="ctoken plain">(</span><span class="ctoken plain">localization</span><span class="ctoken plain">: </span><span class="ctoken class-name">[Vps2Localization](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2Localization/ "Spatial mapping between the device's AR coordinate space and real-world...")</span><span class="ctoken plain">, </span><span class="ctoken plain">location</span><span class="ctoken plain">: </span><span class="ctoken class-name">CLLocation</span><span class="ctoken plain">) -\> </span><span class="ctoken class-name">[Vps2Pose](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2Pose/ "Pose in AR coordinate space calculated by VPS2 from a geolocation.")</span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary-1" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Converts a CLLocation to an AR pose using the provided localization snapshot.

</div>

#### Returns<a href="#returns-1" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The pose in the device's AR coordinate space, or `nil` if unavailable.

</div>

### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

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
<td><span id="external parameter-localization"></span><span class="ctoken-line"><span class="ctoken class-name">localization</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2Localization/" title="Spatial mapping between the device&#39;s AR coordinate space and real-world...">Vps2Localization</a></span></span></td>
<td><div class="ctoken comment">
The localization to use for the conversion.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-location"></span><span class="ctoken-line"><span class="ctoken class-name">location</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-GeolocationData/" title="Struct representing geolocation data including latitude, longitude, altitude,...">GeolocationData</a></span></span></td>
<td><div class="ctoken comment">
The geolocation to convert.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Overload 2<a href="#overload-2" class="hash-link" aria-label="Direct link to Overload 2" title="Direct link to Overload 2">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">getPose</span><span class="ctoken plain">(</span><span class="ctoken plain">localization</span><span class="ctoken plain">: </span><span class="ctoken class-name">[Vps2Localization](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2Localization/ "Spatial mapping between the device's AR coordinate space and real-world...")</span><span class="ctoken plain">, </span><span class="ctoken plain">coordinate</span><span class="ctoken plain">: </span><span class="ctoken class-name">CLLocationCoordinate2D</span><span class="ctoken plain">, </span><span class="ctoken plain">altitude</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/double" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Double</a></span><span class="ctoken plain"> = 0) -\> </span><span class="ctoken class-name">[Vps2Pose](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2Pose/ "Pose in AR coordinate space calculated by VPS2 from a geolocation.")</span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary-2" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Converts a coordinate and altitude to an AR pose using the provided localization snapshot.

</div>

#### Returns<a href="#returns-2" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The pose in the device's AR coordinate space, or `nil` if unavailable.

</div>

### Parameters<a href="#parameters-2" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

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
<td><span id="external parameter-localization"></span><span class="ctoken-line"><span class="ctoken class-name">localization</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2Localization/" title="Spatial mapping between the device&#39;s AR coordinate space and real-world...">Vps2Localization</a></span></span></td>
<td><div class="ctoken comment">
The localization to use for the conversion.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-location"></span><span class="ctoken-line"><span class="ctoken class-name">location</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-GeolocationData/" title="Struct representing geolocation data including latitude, longitude, altitude,...">GeolocationData</a></span></span></td>
<td><div class="ctoken comment">
The geolocation to convert.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
