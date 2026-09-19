---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMesh/
title: NsdkNavMesh
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

#  NsdkNavMesh

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">NsdkNavMesh</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

This class manages the data structures associated with a navigation mesh ("NsdkNavMesh"). It dynamically builds a 2d grid on the meshes detected in the environment for running navigation algorithms on. You are able to retrieve a number of properties of the "NsdkNavMesh" from it. There are also a number of methods to help you place and move NsdkNavMeshAgents on the board.

------------------------------------------------------------------------

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name">NsdkNavMesh</span><span class="ctoken punctuation">(</span><span class="ctoken class-name">[ModelSettings](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.ModelSettings/ "The ModelSettings struct provides a configuration for how NsdkNavMesh scans the real environment and creates a navigable space....")</span><span class="ctoken plain"> </span><span class="ctoken class-name">settings</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">bool</span><span class="ctoken plain"> </span><span class="ctoken class-name">visualise</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary-1" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Constructs a new NsdkNavMesh using the parameters given.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

Returns the newly created NsdkNavMesh.

</div>

------------------------------------------------------------------------

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

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
<td><span id="property-area"></span><span class="ctoken-line"><span class="ctoken class-name">Area</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
The discovered free area in square meters.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-settings"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Settings</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.ModelSettings/" title="The ModelSettings struct provides a configuration for how NsdkNavMesh scans the real environment and creates a navigable space....">ModelSettings</a></span></span></td>
<td><div class="ctoken comment">
The configuration of the NavMeshModel.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-surfaces"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Surfaces</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">List</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.Surface/" title="Represents a subset on the grid with cells of approximately the same elevation.">Surface</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

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
<td><span id="method-calculatepath"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMesh.CalculatePath/" title="Browse to CalculatePath">CalculatePath</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-checkfit"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMesh.CheckFit/" title="Browse to CheckFit">CheckFit</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-clear"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMesh.Clear/" title="Removes all surfaces from the NsdkNavMesh.">Clear</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment">
Removes all surfaces from the NsdkNavMesh.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-destroy"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMesh.Destroy/" title="Browse to Destroy">Destroy</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-findnearestfreeposition"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMesh.FindNearestFreePosition/" title="Browse to FindNearestFreePosition">FindNearestFreePosition</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-findrandomposition"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMesh.FindRandomPosition/" title="Browse to FindRandomPosition">FindRandomPosition</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-isonnavmesh"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMesh.IsOnNavMesh/" title="Checks if a particular 3d position is on the NsdkNavMesh (within a certain threshold).">IsOnNavMesh</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Checks if a particular 3d position is on the NsdkNavMesh (within a certain threshold).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-prune"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMesh.Prune/" title="Browse to Prune">Prune</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-raycast"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMesh.RayCast/" title="Browse to RayCast">RayCast</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-scan"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.NsdkNavMesh.Scan/" title="Browse to Scan">Scan</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
