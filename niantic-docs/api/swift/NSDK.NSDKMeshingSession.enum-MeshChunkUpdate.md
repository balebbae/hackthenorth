---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMeshingSession.enum-MeshChunkUpdate/
title: MeshChunkUpdate
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKMeshingSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKMeshingSession/ "NSDKMeshingSession") 

</div>

<div class="api-title">

#  MeshChunkUpdate

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">enum</span><span class="ctoken plain"> </span><span class="ctoken class-name">MeshChunkUpdate</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Describes a change to a specific mesh chunk. Each case represents how a chunk identified by `id` should be handled:

- `insert`: A new chunk should be added.
- `update`: An existing chunk has new mesh data.
- `remove`: A chunk should be removed.

------------------------------------------------------------------------

## Cases<a href="#cases" class="hash-link" aria-label="Direct link to Cases" title="Direct link to Cases">​</a>

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
<td><span id="case-insert"></span><span class="ctoken-line"><span class="ctoken keyword">case</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMeshingSession.enum-MeshChunkUpdate/#case-insert" title="A new mesh chunk.">insert</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int64" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int64</a></span><span class="ctoken plain">, </span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-MeshData/" title="Contains 3D mesh data for rendering and visualization....">MeshData</a></span><span class="ctoken plain">)</span></span></td>
<td><div class="ctoken comment">
A new mesh chunk.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-remove"></span><span class="ctoken-line"><span class="ctoken keyword">case</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMeshingSession.enum-MeshChunkUpdate/#case-remove" title="Removal of an existing mesh chunk.">remove</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int64" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int64</a></span><span class="ctoken plain">)</span></span></td>
<td><div class="ctoken comment">
Removal of an existing mesh chunk.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-update"></span><span class="ctoken-line"><span class="ctoken keyword">case</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMeshingSession.enum-MeshChunkUpdate/#case-update" title="Updated data for an existing mesh chunk.">update</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int64" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int64</a></span><span class="ctoken plain">, </span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-MeshData/" title="Contains 3D mesh data for rendering and visualization....">MeshData</a></span><span class="ctoken plain">)</span></span></td>
<td><div class="ctoken comment">
Updated data for an existing mesh chunk.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
