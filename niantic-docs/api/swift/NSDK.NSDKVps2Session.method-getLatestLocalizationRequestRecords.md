---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKVps2Session.method-getLatestLocalizationRequestRecords/
title: getLatestLocalizationRequestRecords
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

#  getLatestLocalizationRequestRecords

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">getLatestLocalizationRequestRecords</span><span class="ctoken plain">() -\> \[</span><span class="ctoken class-name">[Vps2LocalizationRequestRecord](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2LocalizationRequestRecord/ "Browse to Vps2LocalizationRequestRecord")</span><span class="ctoken plain">\]</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Gets the latest localization request records from the VPS2 feature.\
Returns only records that occurred since the last call — this is a delta, not cumulative.\
For reactive use, subscribe to `localizationRequestRecords` instead.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

Localization request state changes since the last call.

</div>

------------------------------------------------------------------------

</div>

</div>
