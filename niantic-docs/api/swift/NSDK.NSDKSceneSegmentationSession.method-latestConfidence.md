---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSceneSegmentationSession.method-latestConfidence/
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

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKSceneSegmentationSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKSceneSegmentationSession/ "NSDKSceneSegmentationSession") 

</div>

<div class="api-title">

#  latestConfidence

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">latestConfidence</span><span class="ctoken plain">(</span><span class="ctoken plain">channel</span><span class="ctoken plain">: </span><span class="ctoken class-name">[SceneSegmentationChannels](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-SceneSegmentationChannels/ "A set of semantic channels represented as a bitmask, matching the C SDK packed-channel layout....")</span><span class="ctoken plain">) </span><span class="ctoken keyword">throws</span><span class="ctoken plain">(</span><span class="ctoken class-name">[NSDKError](https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKError/ "Errors thrown by the NSDK API....")</span><span class="ctoken plain">) -\> </span><span class="ctoken class-name">[NSDKAsyncState](https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKAsyncState/ "Reports the state of an asynchronous NSDK operation.")</span><span class="ctoken plain">\<</span><span class="ctoken class-name">[SceneSegmentationResult](https://www.nianticspatial.com/docs/api/swift/NSDK.class-SceneSegmentationResult/ "Contains semantic segmentation results from the NSDK scene segmentation processing system....")</span><span class="ctoken plain">, </span><span class="ctoken class-name">[AwarenessError](https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AwarenessError/ "Browse to AwarenessError")</span><span class="ctoken plain">\></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Retrieves the latest confidence map for a specific semantic channel.\
This method returns a confidence map where each pixel value represents the confidence\
score (0.0–1.0) that the pixel belongs to the specified semantic category. Higher\
confidence values indicate stronger belief in the semantic classification.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

An `NSDKAsyncState` containing either the latest `SceneSegmentationResult`,\
or an `AwarenessError`.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `NSDKError.invalidArgument` if zero or more than one channel is specified.

#### Confidence Interpretation<a href="#confidence-interpretation" class="hash-link" aria-label="Direct link to Confidence Interpretation" title="Direct link to Confidence Interpretation">​</a>

Confidence values range from 0.0 to 1.0:

- **0.0**: Definitely not the specified semantic category

- **0.5**: Uncertain classification

- **1.0**: Definitely the specified semantic category Use confidence thresholds to filter results based on your application's needs.

  ### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

<table class="api-table">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr class="api-table-row">
<td><span id="external parameter-channel"></span><span class="ctoken-line"><span class="ctoken class-name">channel</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-SceneSegmentationChannels/" title="A set of semantic channels represented as a bitmask, matching the C SDK packed-channel layout....">SceneSegmentationChannels</a></span></span></td>
<td><div class="ctoken comment">
The semantic channel; throws if multiple channels are given.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
