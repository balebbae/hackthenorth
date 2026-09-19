---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMapStorage.method-mapData/
title: mapData
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKMapStorage](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKMapStorage/ "NSDKMapStorage") 

</div>

<div class="api-title">

#  mapData

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">mapData</span><span class="ctoken plain">() -\> </span><span class="ctoken class-name">[NSDKBuffer](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKBuffer/ "A buffer containing binary data for NSDK operations....")</span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Gets the complete map data.\
This function returns all the map data accumulated during the AR session, serialized as a\
DeviceMap protobuf. This data can be saved, shared, and/or used for localization.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The serialized map data buffer if available, `nil` if no map data exists.

</div>

------------------------------------------------------------------------

</div>

</div>
