---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mesh.MeshingSession.getData/
title: getData
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

#  getData

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">getData</span><span class="ctoken punctuation">(</span><span class="ctoken plain">id</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Long</a></span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[MeshData](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.MeshData/ "Browse to MeshData")</span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Gets the data for a single mesh chunk.

\

Calling this function will reset the updated flag for the mesh chunk; i.e. after\
calling this function, future calls of `getUpdatedInfos` will only mark the\
chunk with `id` as having updated if its mesh data has changed since the call to\
this function.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The mesh data if a mesh chunk with `id` exists, null if otherwise.

</div>

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

- getUpdatedInfos
- MeshData

------------------------------------------------------------------------

</div>

</div>
