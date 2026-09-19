---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSceneSegmentationSession.method-latestSuppressionMask/
title: latestSuppressionMask
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

#  latestSuppressionMask

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">latestSuppressionMask</span><span class="ctoken plain">() -\> </span><span class="ctoken class-name">[NSDKAsyncState](https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKAsyncState/ "Reports the state of an asynchronous NSDK operation.")</span><span class="ctoken plain">\<</span><span class="ctoken class-name">[SceneSegmentationResult](https://www.nianticspatial.com/docs/api/swift/NSDK.class-SceneSegmentationResult/ "Contains semantic segmentation results from the NSDK scene segmentation processing system....")</span><span class="ctoken plain">, </span><span class="ctoken class-name">[AwarenessError](https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AwarenessError/ "Browse to AwarenessError")</span><span class="ctoken plain">\></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Retrieves the latest suppression mask for semantic processing.\
This method returns a binary mask indicating areas that should be ignored or suppressed\
during semantic processing. Suppression masks are useful for filtering out regions\
that are not relevant for semantic understanding, such as areas with poor image quality.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

An `NSDKAsyncState` containing either the latest `SceneSegmentationResult`,\
or an `AwarenessError`.

</div>

#### Suppression Mask Usage<a href="#suppression-mask-usage" class="hash-link" aria-label="Direct link to Suppression Mask Usage" title="Direct link to Suppression Mask Usage">​</a>

Suppression masks are binary images where:

- **0**: Areas to be suppressed (ignored in semantic processing)
- **1**: Areas to be processed normally Use suppression masks to improve semantic processing quality by excluding problematic regions from analysis.

------------------------------------------------------------------------

</div>

</div>
