---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMesh.IsOnNavMesh/
title: IsOnNavMesh
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.NavigationMesh](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh/ "NianticSpatial.NSDK.AR.NavigationMesh") <span class="api-breadcrumbs-nav">←</span>[NsdkNavMesh](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMesh/ "NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMesh") 

</div>

<div class="api-title">

#  IsOnNavMesh

<div class="api-package">

Checks if a particular 3d position is on the NsdkNavMesh (within a certain threshold).

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">bool</span><span class="ctoken plain"> </span><span class="ctoken class-name">IsOnNavMesh</span><span class="ctoken punctuation">(</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector3</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">position</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">float</span><span class="ctoken plain"> </span><span class="ctoken class-name">delta</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Checks if a particular 3d position is on the NsdkNavMesh (within a certain threshold).

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

true if the position provided is within delta meters of the NsdkNavMesh grid plane.

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
<td><span id="external parameter-position"></span><span class="ctoken-line"><span class="ctoken class-name">position</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector3</a></span></span></td>
<td><div class="ctoken comment">
The 3d position to check for.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-delta"></span><span class="ctoken-line"><span class="ctoken class-name">delta</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
The threshold distance from the NsdkNavMesh to check against.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
