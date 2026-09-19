---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession.latestConfidence/
title: latestConfidence
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

#  latestConfidence

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">latestConfidence</span><span class="ctoken punctuation">(</span><span class="ctoken plain">channel</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[SceneSegmentationChannel](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationChannel/ "Represents the different semantic segmentation channels that can be detected....")</span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[NSDKResult](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKResult/ "ResultDeprecated wrapper for NSDK operations that can succeed or fail....")</span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">[SceneSegmentationResult](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationResult/ "Represents the result of the scene segmentation processor....")</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">[AwarenessStatus](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessStatus/ "Browse to AwarenessStatus")</span><span class="ctoken punctuation">\></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Gets the latest scene segmentation confidence data.

\

This retrieves the most recent confidence values for semantic\
classification of the current frame.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

ARDKResult containing scene segmentation confidence data if successful, or error information

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `NsdkStatusException` — if there was an internal error

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

- channelNames
- latestPackedChannel
- latestSuppressionMask
- confidenceUpdates

------------------------------------------------------------------------

</div>

</div>
