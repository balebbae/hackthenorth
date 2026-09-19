---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession.unpackChannelsFromBitmask/
title: unpackChannelsFromBitmask
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.awareness.scenesegmentation](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation/ "com.nianticspatial.nsdk.awareness.scenesegmentation") <span class="api-breadcrumbs-nav">←</span>[SceneSegmentationSession](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession/ "com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession") 

</div>

<div class="api-title">

#  unpackChannelsFromBitmask

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">unpackChannelsFromBitmask</span><span class="ctoken punctuation">(</span><span class="ctoken plain">bitmask</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EnumSet.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">EnumSet</a></span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">[SceneSegmentationChannel](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationChannel/ "Represents the different semantic segmentation channels that can be detected....")</span><span class="ctoken punctuation">\></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Unpacks semantic channels from a packed channel bitmask.

\

This converts a bitmask value (where each bit represents a semantic channel)\
into an EnumSet of SceneSegmentationChannel enum values representing the channels present\
in the bitmask.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

EnumSet of SceneSegmentationChannel values present in the bitmask

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `NsdkStatusException` — if there was an internal error

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

- latestPackedChannel

------------------------------------------------------------------------

</div>

</div>
