---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager.TryGetDeviceGeolocation/
title: TryGetDeviceGeolocation
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.VPS2](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2/ "NianticSpatial.NSDK.AR.VPS2") <span class="api-breadcrumbs-nav">←</span>[ARVps2Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager/ "NianticSpatial.NSDK.AR.VPS2.ARVps2Manager") 

</div>

<div class="api-title">

#  TryGetDeviceGeolocation

<div class="api-package">

Attempts to get the geolocation of the device's last known camera pose.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">bool</span><span class="ctoken plain"> </span><span class="ctoken class-name">TryGetDeviceGeolocation</span><span class="ctoken punctuation">(</span><span class="ctoken keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name">[XRVps2Geolocation](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRVps2Geolocation/ "Structure describing device location and heading as calculated by VPS2.")</span><span class="ctoken plain"> </span><span class="ctoken class-name">geolocationOut</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">[HeadingMode](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.HeadingMode/ "Controls how the heading is computed from the device's orientation....")</span><span class="ctoken plain"> </span><span class="ctoken class-name">headingMode</span><span class="ctoken plain"> </span><span class="ctoken punctuation">=</span><span class="ctoken plain"> </span><span class="ctoken plain">HeadingMode.CameraDirection</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Attempts to get the geolocation of the device's last known camera pose.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

true if the subsystem is available; otherwise false.

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
<td><span id="external parameter-geolocationout"></span><span class="ctoken-line"><span class="ctoken class-name">geolocationOut</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRVps2Geolocation/" title="Structure describing device location and heading as calculated by VPS2.">XRVps2Geolocation</a></span></span></td>
<td><div class="ctoken comment">
Receives the geolocation data on success.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-headingmode"></span><span class="ctoken-line"><span class="ctoken class-name">headingMode</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.HeadingMode/" title="Controls how the heading is computed from the device&#39;s orientation....">HeadingMode</a></span></span></td>
<td><div class="ctoken comment">
Controls how the heading is derived.<br />
Use CameraDirection when the device is upright,<br />
or DeviceTop when flat or for a compass-style heading.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
