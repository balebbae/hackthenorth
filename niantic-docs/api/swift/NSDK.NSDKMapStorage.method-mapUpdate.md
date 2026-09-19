---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMapStorage.method-mapUpdate/
title: mapUpdate
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

#  mapUpdate

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">mapUpdate</span><span class="ctoken plain">() -\> </span><span class="ctoken class-name">[NSDKBuffer](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKBuffer/ "A buffer containing binary data for NSDK operations....")</span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Gets the latest map update data.\
This method returns the incremental map changes (new nodes and edges) that have been added\
since the last update.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The serialized map update if available, `nil` if no updates exist.

</div>

------------------------------------------------------------------------

</div>

</div>
