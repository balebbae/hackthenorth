---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers/
title: com.nianticspatial.nsdk.helpers
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

#  helpers

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
<td><span id="class-locationhelper"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers.LocationHelper/" title="Subscribes to GPS updates via the Fused Location Provider and notifies an [OnUpdateListener]...">LocationHelper</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers.LocationHelper/" title="Subscribes to GPS updates via the Fused Location Provider and notifies an [OnUpdateListener]...">LocationHelper</a></span></span></td>
<td><div class="ctoken comment">
Subscribes to GPS updates via the Fused Location Provider and notifies an [OnUpdateListener]<br />
on each new fix. Used internally by [DefaultSessionDataSource].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-sensorhelper"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers.SensorHelper/" title="Reads compass (heading) and raw magnetometer data from Android sensors and exposes it as a...">SensorHelper</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers.SensorHelper/" title="Reads compass (heading) and raw magnetometer data from Android sensors and exposes it as a...">SensorHelper</a></span></span></td>
<td><div class="ctoken comment">
Reads compass (heading) and raw magnetometer data from Android sensors and exposes it as a<br />
[Compass] snapshot. Used internally by [DefaultSessionDataSource].<br />
Call [resume] when the owning component becomes active and [pause] when it is paused to<br />
conserve battery.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
