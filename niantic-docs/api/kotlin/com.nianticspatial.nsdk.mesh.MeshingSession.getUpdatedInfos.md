---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mesh.MeshingSession.getUpdatedInfos/
title: getUpdatedInfos
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.mesh](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mesh/ "com.nianticspatial.nsdk.mesh") <span class="api-breadcrumbs-nav">←</span>[MeshingSession](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mesh.MeshingSession/ "com.nianticspatial.nsdk.mesh.MeshingSession") 

</div>

<div class="api-title">

#  getUpdatedInfos

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">getUpdatedInfos</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[MeshingUpdateInfo](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.MeshingUpdateInfo/ "Browse to MeshingUpdateInfo")</span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Gets the ids of all chunks in the current mesh and their update status.

\

The returned information contains the IDs and update status for all chunks currently\
in the mesh. If a chunk's updated flag is true, the mesh chunk has been updated since\
the last time its data was read with `getData`.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

Information about all the updated mesh chunks if available, null if there are no chunks.

</div>

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

- getData
- getLastUpdateTime

------------------------------------------------------------------------

</div>

</div>
