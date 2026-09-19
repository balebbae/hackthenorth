---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMeshAgentPathRenderer/
title: NsdkNavMeshAgentPathRenderer
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.NavigationMesh](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh/ "NianticSpatial.NSDK.AR.NavigationMesh") 

</div>

<div class="api-title">

#  NsdkNavMeshAgentPathRenderer

<div class="api-extends">

↳ extends UnityEngine.MonoBehaviour

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">NsdkNavMeshAgentPathRenderer</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">MonoBehaviour</a></span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

NsdkNavMeshAgentPathRenderer is a debug renderer to show you the path a NsdkNavMeshAgent is moving along while navigating the environment. You add it to the NsdkNavMeshAgentGameObject in your scene and it will draw that agent's current path.

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
<td><span id="field-_agent"></span><span class="ctoken-line"><span class="ctoken class-name">_agent</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMeshAgent/" title="NsdkNavMeshAgent is an example agent implementation that navigates a NsdkNavMesh based on logic programmed here....">NsdkNavMeshAgent</a></span></span></td>
<td><div class="ctoken comment">
The NsdkNavMeshAgent that you want to render the path for.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-_material"></span><span class="ctoken-line"><span class="ctoken class-name">_material</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Material</a></span></span></td>
<td><div class="ctoken comment">
The Material used to render the path. This Material will be applied on a LineRenderer.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
