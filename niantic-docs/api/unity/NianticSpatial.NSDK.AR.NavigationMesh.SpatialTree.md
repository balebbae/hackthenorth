---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.SpatialTree/
title: SpatialTree
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

#  SpatialTree

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">partial</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">SpatialTree</span></span>

------------------------------------------------------------------------

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name">SpatialTree</span><span class="ctoken punctuation">(</span><span class="ctoken class-name keyword">int</span><span class="ctoken plain"> </span><span class="ctoken class-name">approximateQuadSize</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Creates a new spatial tree instance.\
A spatial tree consists of a grid of quads, which themselves can subdivide.\
@param approximateQuadSize Defines the size of a quad. The actual size will\
be less than or equal to this number.

</div>

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
<td><span id="method-clear"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.SpatialTree.Clear/" title="Browse to Clear">Clear</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-drawgizmos"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.SpatialTree.DrawGizmos/" title="Visualizes the quad-tree in the editor&#39;s scene view....">DrawGizmos</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment">
Visualizes the quad-tree in the editor's scene view.<br />
@param setting The NsdkNavMesh's configuration.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getelement"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.SpatialTree.GetElement/" title="Returns the grid node at the specified location if exists....">GetElement</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Returns the grid node at the specified location if exists.<br />
@param atPosition The location of the grid node.<br />
@param result The element stored at the specified location.<br />
@returns True, if the grid node could be located.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-insert"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.SpatialTree.Insert/" title="Inserts the provided elements to the tree....">Insert</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Inserts the provided elements to the tree.<br />
@param gridNodes Grid nodes to insert.<br />
@returns Whether all nodes were inserted successfully.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-query"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.SpatialTree.Query/" title="Browse to Query">Query</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ienumerable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">IEnumerable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.GridNode/" title="Encloses data for grid elements used during scanning for walkable areas.">GridNode</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-remove"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.SpatialTree.Remove/" title="Removes the provided elements from the tree....">Remove</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.hashset-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">HashSet</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2Int.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector2Int</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Removes the provided elements from the tree.<br />
@param gridNodes Grid nodes to remove.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
