---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Occlusion.NsdkOcclusionExtension.RemoveSceneSegmentationSuppressionChannel/
title: RemoveSceneSegmentationSuppressionChannel
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Occlusion](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Occlusion/ "NianticSpatial.NSDK.AR.Occlusion") <span class="api-breadcrumbs-nav">←</span>[NsdkOcclusionExtension](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Occlusion.NsdkOcclusionExtension/ "NianticSpatial.NSDK.AR.Occlusion.NsdkOcclusionExtension") 

</div>

<div class="api-title">

#  RemoveSceneSegmentationSuppressionChannel

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">bool</span><span class="ctoken plain"> </span><span class="ctoken class-name">RemoveSceneSegmentationSuppressionChannel</span><span class="ctoken punctuation">(</span><span class="ctoken class-name">[SceneSegmentationChannel](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.SceneSegmentation.SceneSegmentationChannel/ "Represents the different semantic segmentation channels that can be detected....")</span><span class="ctoken plain"> </span><span class="ctoken class-name">channel</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Removes a semantic segmentation channel, if it exists, from the collection of channels\
that are suppressed in the depth buffer.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

True if the channel was found and removed.

</div>

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
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.SceneSegmentation.SceneSegmentationChannel/" title="Represents the different semantic segmentation channels that can be detected....">SceneSegmentationChannel</a></span></span></td>
<td><div class="ctoken comment">
Semantic segmentation channel to remove.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
