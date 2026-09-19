---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSceneSegmentationSession.method-latestImageParams/
title: latestImageParams
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKSceneSegmentationSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKSceneSegmentationSession/ "NSDKSceneSegmentationSession") 

</div>

<div class="api-title">

#  latestImageParams

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">latestImageParams</span><span class="ctoken plain">() -\> </span><span class="ctoken class-name">[NSDKAsyncState](https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKAsyncState/ "Reports the state of an asynchronous NSDK operation.")</span><span class="ctoken plain">\<</span><span class="ctoken class-name">[AwarenessImageParams](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AwarenessImageParams/ "Browse to AwarenessImageParams")</span><span class="ctoken plain">, </span><span class="ctoken class-name">[AwarenessError](https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AwarenessError/ "Browse to AwarenessError")</span><span class="ctoken plain">\></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Retrieves the latest camera intrinsic parameters for semantic processing.\
This method returns the camera intrinsic parameters that were used during semantic\
processing. These parameters are essential for coordinate transformations between\
image coordinates and 3D world coordinates.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

An `NSDKAsyncState` containing either the latest `AwarenessImageParams`,\
or an `AwarenessError`.

</div>

------------------------------------------------------------------------

</div>

</div>
