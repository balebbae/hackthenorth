---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.MappingStorageSession.getData/
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

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.mapping](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping/ "com.nianticspatial.nsdk.mapping") <span class="api-breadcrumbs-nav">←</span>[MappingStorageSession](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.MappingStorageSession/ "com.nianticspatial.nsdk.mapping.MappingStorageSession") 

</div>

<div class="api-title">

#  getData

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">getData</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ByteArray</a></span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Get the complete map data.

\

This function returns all the map data accumulated during the AR session, serialized as a\
DeviceMap protobuf. This data can be saved, shared, and/or used for localization.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The map data if successful, or `null` if no map data exists.

</div>

------------------------------------------------------------------------

</div>

</div>
