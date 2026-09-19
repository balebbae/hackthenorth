---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem.TryResetChannelConfidenceThresholds/
title: TryResetChannelConfidenceThresholds
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.XRSubsystems](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems/ "NianticSpatial.NSDK.AR.XRSubsystems") <span class="api-breadcrumbs-nav">←</span>[XRSceneSegmentationSubsystem](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem/ "NianticSpatial.NSDK.AR.XRSubsystems.XRSceneSegmentationSubsystem") 

</div>

<div class="api-title">

#  TryResetChannelConfidenceThresholds

<div class="api-package">

Resets the confidence thresholds for all semantic channels to the default values from the current model.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">bool</span><span class="ctoken plain"> </span><span class="ctoken class-name">TryResetChannelConfidenceThresholds</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Resets the confidence thresholds for all semantic channels to the default values from the current model.

</div>

#### Remarks<a href="#remarks" class="hash-link" aria-label="Direct link to Remarks" title="Direct link to Remarks">​</a>

<div class="ctoken comment">

This reverts any changes made with TrySetChannelConfidenceThresholds.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

True if the thresholds were reset. Otherwise, false.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `NotSupportedException` — Thrown when resetting confidence thresholds is not supported by the implementation.

------------------------------------------------------------------------

</div>

</div>
