---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession.latestImageParams/
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

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.awareness.scenesegmentation](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation/ "com.nianticspatial.nsdk.awareness.scenesegmentation") <span class="api-breadcrumbs-nav">←</span>[SceneSegmentationSession](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession/ "com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession") 

</div>

<div class="api-title">

#  latestImageParams

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">latestImageParams</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[NSDKResult](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKResult/ "ResultDeprecated wrapper for NSDK operations that can succeed or fail....")</span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">[AwarenessImageParams](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessImageParams/ "Describes inferred image results.")</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">[AwarenessStatus](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessStatus/ "Browse to AwarenessStatus")</span><span class="ctoken punctuation">\></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Gets the latest image parameters for scene segmentation processing.

\

This retrieves the most recent image parameters used for\
semantic analysis of the current frame.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

ARDKResult containing image parameters if successful, or error information

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `NsdkStatusException` — if there was an internal error

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

- latestConfidence
- latestPackedChannel
- latestSuppressionMask

------------------------------------------------------------------------

</div>

</div>
