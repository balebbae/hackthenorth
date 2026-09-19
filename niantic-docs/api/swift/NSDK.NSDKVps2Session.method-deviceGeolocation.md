---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKVps2Session.method-deviceGeolocation/
title: deviceGeolocation
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

#  deviceGeolocation

<div class="api-package">

Gets the geolocation of the device's last known camera pose.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">deviceGeolocation</span><span class="ctoken plain">(</span><span class="ctoken plain">headingMode</span><span class="ctoken plain">: </span><span class="ctoken class-name">[HeadingMode](https://www.nianticspatial.com/docs/api/swift/NSDK.enum-HeadingMode/ "Controls how the heading is computed from the device's orientation.")</span><span class="ctoken plain"> = .cameraDirection) -\> </span><span class="ctoken class-name">[Vps2GeolocationData](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2GeolocationData/ "Location and heading data calculated by VPS2.")</span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Gets the geolocation of the device's last known camera pose.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

Geolocation data corresponding to the device's current pose,\
or `nil` if VPS2 tracking is unavailable.

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
<td><span id="external parameter-headingmode"></span><span class="ctoken-line"><span class="ctoken class-name">headingMode</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-HeadingMode/" title="Controls how the heading is computed from the device&#39;s orientation.">HeadingMode</a></span></span></td>
<td><div class="ctoken comment">
Controls how the heading is derived.<br />
Use <code>.cameraDirection</code> when the device is upright,<br />
or <code>.deviceTop</code> when flat or for a compass-style heading.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
