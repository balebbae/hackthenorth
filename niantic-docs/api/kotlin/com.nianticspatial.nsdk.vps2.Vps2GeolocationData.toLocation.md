---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2GeolocationData.toLocation/
title: toLocation
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.vps2](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2/ "com.nianticspatial.nsdk.vps2") <span class="api-breadcrumbs-nav">←</span>[Vps2GeolocationData](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2GeolocationData/ "com.nianticspatial.nsdk.vps2.Vps2GeolocationData") 

</div>

<div class="api-title">

#  toLocation

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">toLocation</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">Location</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Converts this VPS2 geolocation to an Android `Location`.

\

The returned `Location` has `Location.getProvider` set to `LOCATION_PROVIDER_VPS2`,\
with `Location.getAccuracy` from `horizontalAccuracyMetres`, `Location.getBearing` from\
`heading` (device orientation relative to true north), and on API 26+ vertical accuracy\
from `verticalAccuracyMetres` and bearing accuracy from `rotationAccuracyDeg`.\
Timestamp is set to the time of conversion.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A new `Location` instance populated from this VPS2 geolocation data.

</div>

------------------------------------------------------------------------

</div>

</div>
