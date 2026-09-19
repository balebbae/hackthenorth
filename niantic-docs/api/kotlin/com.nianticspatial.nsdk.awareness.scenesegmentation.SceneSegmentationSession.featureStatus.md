---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession.featureStatus/
title: featureStatus
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

#  featureStatus

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">featureStatus</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[FeatureStatus](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.FeatureStatus/ "Browse to FeatureStatus")</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Reports errors that have occurred with processes running inside this session.

\

Check this periodically to see if any errors have occurred with\
processes running inside this feature. Once an error has been\
flagged, it will remain flagged until the culprit process has\
been run again and completed successfully.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

Status that may occur within the process of feature

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `NsdkStatusException` — if there was an internal error

------------------------------------------------------------------------

</div>

</div>
