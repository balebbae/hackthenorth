---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKDepthSession.method-latestDepth/
title: latestDepth
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKDepthSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKDepthSession/ "NSDKDepthSession") 

</div>

<div class="api-title">

#  latestDepth

<div class="api-package">

Retrieves the latest depth result from the depth session.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">latestDepth</span><span class="ctoken plain">() -\> </span><span class="ctoken class-name">[NSDKAsyncState](https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKAsyncState/ "Reports the state of an asynchronous NSDK operation.")</span><span class="ctoken plain">\<</span><span class="ctoken class-name">[DepthResult](https://www.nianticspatial.com/docs/api/swift/NSDK.class-DepthResult/ "Contains depth estimation results from the NSDK depth processing system.")</span><span class="ctoken plain">, </span><span class="ctoken class-name">[AwarenessError](https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AwarenessError/ "Browse to AwarenessError")</span><span class="ctoken plain">\></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Retrieves the latest depth result from the depth session.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

An `NSDKAsyncState` containing either the latest `DepthResult`,\
or an `AwarenessError`.

</div>

------------------------------------------------------------------------

</div>

</div>
