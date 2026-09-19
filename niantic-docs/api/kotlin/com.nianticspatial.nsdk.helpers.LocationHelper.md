---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers.LocationHelper/
title: LocationHelper
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.helpers](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers/ "com.nianticspatial.nsdk.helpers") 

</div>

<div class="api-title">

#  LocationHelper

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">LocationHelper</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Subscribes to GPS updates via the Fused Location Provider and notifies an \[OnUpdateListener\] on each new fix. Used internally by \[DefaultSessionDataSource\].

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
<td><span id="function-startlocationupdates"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers.LocationHelper.startLocationUpdates/" title="Begins receiving GPS updates. Delivers the last known location immediately (if available),...">startLocationUpdates</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Begins receiving GPS updates. Delivers the last known location immediately (if available),<br />
then streams new fixes at ~5-second intervals via [OnUpdateListener.onLocationUpdate].<br />
Requires [ACCESS_FINE_LOCATION][android.Manifest.permission.ACCESS_FINE_LOCATION]; no-op if<br />
the permission is not granted.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-stoplocationupdates"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers.LocationHelper.stopLocationUpdates/" title="Stops receiving GPS updates. Safe to call even if [startLocationUpdates] was never called.">stopLocationUpdates</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Stops receiving GPS updates. Safe to call even if [startLocationUpdates] was never called.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
