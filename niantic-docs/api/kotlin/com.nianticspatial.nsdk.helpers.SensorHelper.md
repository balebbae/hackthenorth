---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers.SensorHelper/
title: SensorHelper
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

#  SensorHelper

<div class="api-extends">

↳ extends SensorEventListener

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">SensorHelper</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Reads compass (heading) and raw magnetometer data from Android sensors and exposes it as a \[Compass\] snapshot. Used internally by \[DefaultSessionDataSource\]. Call \[resume\] when the owning component becomes active and \[pause\] when it is paused to conserve battery.

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
<td><span id="function-compass"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers.SensorHelper.compass/" title="Returns a snapshot of the latest compass reading. Check [Compass.headingAccuracy] &gt;= 0 to confirm data has arrived.">compass</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Compass/" title="Browse to Compass">Compass</a></span></span></td>
<td><div class="ctoken comment">
Returns a snapshot of the latest compass reading. Check [Compass.headingAccuracy] &gt;= 0 to confirm data has arrived.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-isdeviceflat"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers.SensorHelper.isDeviceFlat/" title="Returns true when the device is roughly flat (face-up or face-down).">isDeviceFlat</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Boolean</a></span></span></td>
<td><div class="ctoken comment">
Returns true when the device is roughly flat (face-up or face-down).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-onaccuracychanged"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers.SensorHelper.onAccuracyChanged/" title="Browse to onAccuracyChanged">onAccuracyChanged</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-onsensorchanged"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers.SensorHelper.onSensorChanged/" title="Browse to onSensorChanged">onSensorChanged</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-pause"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers.SensorHelper.pause/" title="Unregisters all sensor listeners. Call from [androidx.lifecycle.DefaultLifecycleObserver.onPause].">pause</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Unregisters all sensor listeners. Call from [androidx.lifecycle.DefaultLifecycleObserver.onPause].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-resume"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers.SensorHelper.resume/" title="Registers sensor listeners. Call from [androidx.lifecycle.DefaultLifecycleObserver.onResume].">resume</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Registers sensor listeners. Call from [androidx.lifecycle.DefaultLifecycleObserver.onResume].
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
