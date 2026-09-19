---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkSessionDataSource/
title: NsdkSessionDataSource
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

#  NsdkSessionDataSource

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">interface</span><span class="ctoken plain"> </span><span class="ctoken class-name">NsdkSessionDataSource</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Provides synchronous, pull-based access to the latest available sensor data required by \[NSDKSession\]. All methods must be non-blocking and thread-safe. Returned values represent the most recent samples already captured by the underlying services. Implement this interface and assign it to \[NSDKSession.dataSource\], then call \[NSDKSession.update\] once per camera frame to submit data to the native layer.

## See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

- DefaultSessionDataSource — for the standard ARCore + sensor implementation.
- PlaybackSessionDataSource — for dataset playback.

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
<td><span id="function-latestcamerasample"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkSessionDataSource.latestCameraSample/" title="Returns the most recent camera sample, or null if unavailable.">latestCameraSample</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.CameraSample/" title="A snapshot of camera sensor data for a single frame.">CameraSample</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Returns the most recent camera sample, or null if unavailable.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-latestcompasssample"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkSessionDataSource.latestCompassSample/" title="Returns the most recent compass/magnetometer reading, or null if unavailable.">latestCompassSample</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Compass/" title="Browse to Compass">Compass</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Returns the most recent compass/magnetometer reading, or null if unavailable.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-latestdepthsample"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkSessionDataSource.latestDepthSample/" title="Returns the most recent platform depth sample (e.g. LiDAR), or null if unavailable.">latestDepthSample</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.DepthSample/" title="A snapshot of platform depth data (e.g. LiDAR or ToF sensor) for a single frame.">DepthSample</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Returns the most recent platform depth sample (e.g. LiDAR), or null if unavailable.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-latestgpssample"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkSessionDataSource.latestGpsSample/" title="Returns the most recent GPS location, or null if unavailable.">latestGpsSample</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Location</span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Returns the most recent GPS location, or null if unavailable.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-latesttrackingstatesample"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkSessionDataSource.latestTrackingStateSample/" title="Returns the current VIO tracking state.">latestTrackingStateSample</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developers.google.com/ar/reference/java/com/google/ar/core/TrackingState" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TrackingState</a></span></span></td>
<td><div class="ctoken comment">
Returns the current VIO tracking state.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-prepareframe"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkSessionDataSource.prepareFrame/" title="Snapshots the current frame data so that [latestCameraSample] and the other accessors...">prepareFrame</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Boolean</a></span></span></td>
<td><div class="ctoken comment">
Snapshots the current frame data so that [latestCameraSample] and the other accessors<br />
can be called from any thread. Returns true when a frame is ready to be consumed, false<br />
if no frame was available — in which case the caller should skip [NSDKSession.update].<br />
The default implementation returns true and does nothing; data sources that hold no<br />
per-frame state do not need to override it.<br />
<strong>Threading contract</strong>: the caller must ensure that [prepareFrame], [NSDKSession.update],<br />
and any <code>latest*</code> accessor calls are serialized — i.e., a complete<br />
<code>prepareFrame → update → (accessors finish)</code> cycle must complete before the next<br />
[prepareFrame] call begins. This is typically achieved by driving the cycle from a<br />
single-threaded executor or a coroutine with an in-flight gate.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
