---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKVps2Session.method-getLatestLocalization/
title: getLatestLocalization
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

#  getLatestLocalization

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">getLatestLocalization</span><span class="ctoken plain">() -\> </span><span class="ctoken class-name">[Vps2Localization](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2Localization/ "Spatial mapping between the device's AR coordinate space and real-world...")</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Gets a copy of the latest VPS2 localization.\
The localization contains all data required to convert between AR space and geolocation.\
If VPS2 has not yet localized, the localization's `trackingState` will be `.unavailable`\
and the other fields should be considered invalid.\
For reactive use, subscribe to `$latestLocalization` instead of calling this directly.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The latest VPS2 localization.

</div>

------------------------------------------------------------------------

</div>

</div>
