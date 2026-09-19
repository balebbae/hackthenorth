---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.getDeviceGeolocation/
title: getDeviceGeolocation
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.vps2](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2/ "com.nianticspatial.nsdk.vps2") <span class="api-breadcrumbs-nav">←</span>[Vps2Session](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session/ "com.nianticspatial.nsdk.vps2.Vps2Session") 

</div>

<div class="api-title">

#  getDeviceGeolocation

<div class="api-package">

Get the geolocation of the device's last known camera pose.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">getDeviceGeolocation</span><span class="ctoken punctuation">(</span><span class="ctoken plain">headingMode</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[HeadingMode](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.HeadingMode/ "Controls how the heading is computed from the device's orientation....")</span><span class="ctoken plain"> </span><span class="ctoken plain">=</span><span class="ctoken plain"> </span><span class="ctoken class-name">[HeadingMode](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.HeadingMode/ "Controls how the heading is computed from the device's orientation....")</span><span class="ctoken punctuation">.</span><span class="ctoken class-name">CAMERA_DIRECTION</span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[Vps2GeolocationData](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2GeolocationData/ "Geolocation data from VPS2 localization with accuracy information.")</span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Get the geolocation of the device's last known camera pose.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

`Vps2GeolocationData` if available, `null` otherwise.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `NsdkInvalidOperationStatusException` — if the current localization tracking state is `Vps2TrackingState.UNAVAILABLE`.

------------------------------------------------------------------------

</div>

</div>
