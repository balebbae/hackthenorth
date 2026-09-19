---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.LocationService.Start/
title: Start
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR/ "NianticSpatial.NSDK.AR") <span class="api-breadcrumbs-nav">←</span>[LocationService](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.LocationService/ "NianticSpatial.NSDK.AR.LocationService") 

</div>

<div class="api-title">

#  Start

<div class="api-package">

Starts location service updates.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">void</span><span class="ctoken plain"> </span><span class="ctoken class-name">Start</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Starts location service updates.

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
<td><span id="external parameter-desiredaccuracyinmeters"></span><span class="ctoken-line"><span class="ctoken class-name">desiredAccuracyInMeters</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
The service accuracy you want to use, in meters. This determines the accuracy of the device's last location coordinates. Higher values like 500 don't require the device to use its GPS chip and<br />
thus save battery power. Lower values like 5-10 provide the best accuracy but require the GPS chip and thus use more battery power. The default value is 10 meters.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-updatedistanceinmeters"></span><span class="ctoken-line"><span class="ctoken class-name">updateDistanceInMeters</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
The minimum distance, in meters, that the device must move laterally before Unity updates Input.location. Higher values like 500 produce fewer updates and are less resource intensive to process. The default is 10 meters.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Overload 1<a href="#overload-1" class="hash-link" aria-label="Direct link to Overload 1" title="Direct link to Overload 1">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">void</span><span class="ctoken plain"> </span><span class="ctoken class-name">Start</span><span class="ctoken punctuation">(</span><span class="ctoken class-name keyword">float</span><span class="ctoken plain"> </span><span class="ctoken class-name">desiredAccuracyInMeters</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary-1" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Starts location service updates.

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
<td><span id="external parameter-desiredaccuracyinmeters"></span><span class="ctoken-line"><span class="ctoken class-name">desiredAccuracyInMeters</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
The service accuracy you want to use, in meters. This determines the accuracy of the device's last location coordinates. Higher values like 500 don't require the device to use its GPS chip and<br />
thus save battery power. Lower values like 5-10 provide the best accuracy but require the GPS chip and thus use more battery power. The default value is 10 meters.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-updatedistanceinmeters"></span><span class="ctoken-line"><span class="ctoken class-name">updateDistanceInMeters</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
The minimum distance, in meters, that the device must move laterally before Unity updates Input.location. Higher values like 500 produce fewer updates and are less resource intensive to process. The default is 10 meters.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Overload 2<a href="#overload-2" class="hash-link" aria-label="Direct link to Overload 2" title="Direct link to Overload 2">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">void</span><span class="ctoken plain"> </span><span class="ctoken class-name">Start</span><span class="ctoken punctuation">(</span><span class="ctoken class-name keyword">float</span><span class="ctoken plain"> </span><span class="ctoken class-name">desiredAccuracyInMeters</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">float</span><span class="ctoken plain"> </span><span class="ctoken class-name">updateDistanceInMeters</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary-2" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Starts location service updates.

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
<td><span id="external parameter-desiredaccuracyinmeters"></span><span class="ctoken-line"><span class="ctoken class-name">desiredAccuracyInMeters</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
The service accuracy you want to use, in meters. This determines the accuracy of the device's last location coordinates. Higher values like 500 don't require the device to use its GPS chip and<br />
thus save battery power. Lower values like 5-10 provide the best accuracy but require the GPS chip and thus use more battery power. The default value is 10 meters.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-updatedistanceinmeters"></span><span class="ctoken-line"><span class="ctoken class-name">updateDistanceInMeters</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
The minimum distance, in meters, that the device must move laterally before Unity updates Input.location. Higher values like 500 produce fewer updates and are less resource intensive to process. The default is 10 meters.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
