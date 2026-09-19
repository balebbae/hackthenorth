---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.MappingStorageSession.mergeUpdate/
title: mergeUpdate
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.mapping](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping/ "com.nianticspatial.nsdk.mapping") <span class="api-breadcrumbs-nav">←</span>[MappingStorageSession](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.MappingStorageSession/ "com.nianticspatial.nsdk.mapping.MappingStorageSession") 

</div>

<div class="api-title">

#  mergeUpdate

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">mergeUpdate</span><span class="ctoken punctuation">(</span><span class="ctoken plain">existingMap</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ByteArray</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">mapUpdate</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ByteArray</a></span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ByteArray</a></span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Merge a map update into an existing map.

\

Combines incremental map updates with existing map data to create an updated complete\
map dataset.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The merged map data if successful, or `null` if no merged map data exists.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `ArdkNullArgumentStatusException` — or `ArdkInvalidArgumentStatusException` indicating a problem with the `map` argument. Check ARDK's C logs for more information.

------------------------------------------------------------------------

</div>

</div>
