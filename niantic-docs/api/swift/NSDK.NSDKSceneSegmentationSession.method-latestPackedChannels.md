---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSceneSegmentationSession.method-latestPackedChannels/
title: latestPackedChannels
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

#  latestPackedChannels

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">latestPackedChannels</span><span class="ctoken plain">() -\> </span><span class="ctoken class-name">[NSDKAsyncState](https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKAsyncState/ "Reports the state of an asynchronous NSDK operation.")</span><span class="ctoken plain">\<</span><span class="ctoken class-name">[SceneSegmentationResult](https://www.nianticspatial.com/docs/api/swift/NSDK.class-SceneSegmentationResult/ "Contains semantic segmentation results from the NSDK scene segmentation processing system....")</span><span class="ctoken plain">, </span><span class="ctoken class-name">[AwarenessError](https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AwarenessError/ "Browse to AwarenessError")</span><span class="ctoken plain">\></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Retrieves the latest packed semantic channels data.\
This method returns a multi-channel image where each channel represents a different\
semantic category. Packed channels provide an efficient way to access multiple\
semantic classifications in a single image, reducing the need for multiple API calls.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

An `NSDKAsyncState` containing either the latest `SceneSegmentationResult`,\
or an `AwarenessError`.

</div>

#### Packed Channels Format<a href="#packed-channels-format" class="hash-link" aria-label="Direct link to Packed Channels Format" title="Direct link to Packed Channels Format">​</a>

The packed channels image contains multiple semantic categories encoded as separate channels in a single image. Each channel corresponds to a semantic category, and pixel values represent classification confidence or probability scores.

#### Performance Benefits<a href="#performance-benefits" class="hash-link" aria-label="Direct link to Performance Benefits" title="Direct link to Performance Benefits">​</a>

Using packed channels is more efficient than calling `latestConfidence` multiple times, as it reduces the number of API calls and data transfers required.

------------------------------------------------------------------------

</div>

</div>
