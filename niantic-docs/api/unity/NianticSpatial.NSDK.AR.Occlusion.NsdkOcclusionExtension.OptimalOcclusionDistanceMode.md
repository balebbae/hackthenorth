---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Occlusion.NsdkOcclusionExtension.OptimalOcclusionDistanceMode/
title: OptimalOcclusionDistanceMode
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

#  OptimalOcclusionDistanceMode

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">enum</span><span class="ctoken plain"> </span><span class="ctoken class-name">OptimalOcclusionDistanceMode</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

The sampling mode for determining the distance to the occluder. This distance is used to transform the depth buffer to provide accurate occlusions.

------------------------------------------------------------------------

## Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

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
<td><span id="field-closestoccluder"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">ClosestOccluder</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">OptimalOcclusionDistanceMode</span></span></td>
<td><div class="ctoken comment">
Take a few samples of the full depth buffer to<br />
determine the closest occluder on the screen.<br />
This will provide the best available occlusions<br />
if there are many occluded virtual objects of similar<br />
size and importance.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-specifiedgameobject"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">SpecifiedGameObject</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">OptimalOcclusionDistanceMode</span></span></td>
<td><div class="ctoken comment">
Sample the sub-region of the buffer that is directly over<br />
the main CG object, to determine the distance of its occluder<br />
in the world. This will provide the best quality occlusions<br />
if there is only one occluded virtual object, or if one is more<br />
visually prominent than the others
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-static"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">Static</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">OptimalOcclusionDistanceMode</span></span></td>
<td><div class="ctoken comment">
Stabilize the depth buffer relative to a pre-determined,<br />
unchanging depth. Not recommended if there are occluded virtual objects<br />
in the scene, but is more performant and thus optimal when<br />
occlusions are not needed.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
