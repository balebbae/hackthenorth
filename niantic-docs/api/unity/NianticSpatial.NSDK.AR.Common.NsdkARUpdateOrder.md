---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Common.NsdkARUpdateOrder/
title: NsdkARUpdateOrder
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Common](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Common/ "NianticSpatial.NSDK.AR.Common") 

</div>

<div class="api-title">

#  NsdkARUpdateOrder

<div class="api-package">

The update order for MonoBehaviours in NSDK.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">NsdkARUpdateOrder</span></span>

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
<td><span id="field-devicemappingmanager"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">DeviceMappingManager</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The ARDeviceMappingManager's update order.<br />
Should come after the ARSession.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-occlusionmanager"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">OcclusionManager</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The AROcclusionManager's update order.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-scanningmanager"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">ScanningManager</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The ARScanningManager's update order.<br />
Should come after the ARSession.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-scenesegmentationmanager"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">SceneSegmentationManager</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The ARSceneSegmentationManager's update order.<br />
Should come after the AROcclusionManager to ensure that the model choice is made by the<br />
occlusion manager before semantic segmentation starts.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-session"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">Session</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The ARSession's update order. Should come first.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-vps2anchor"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">Vps2Anchor</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The ARVps2Anchor's update order.<br />
Should come after Vps2Manager.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-vps2manager"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">Vps2Manager</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The ARVps2Manager's update order.<br />
Should come after the ARSession.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
