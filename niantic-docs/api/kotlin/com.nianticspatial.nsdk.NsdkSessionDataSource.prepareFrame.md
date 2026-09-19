---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkSessionDataSource.prepareFrame/
title: prepareFrame
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk/ "com.nianticspatial.nsdk") <span class="api-breadcrumbs-nav">←</span>[NsdkSessionDataSource](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkSessionDataSource/ "com.nianticspatial.nsdk.NsdkSessionDataSource") 

</div>

<div class="api-title">

#  prepareFrame

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">suspend</span><span class="ctoken plain"> </span><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">prepareFrame</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Boolean</a></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Snapshots the current frame data so that `latestCameraSample` and the other accessors\
can be called from any thread. Returns true when a frame is ready to be consumed, false\
if no frame was available — in which case the caller should skip `NSDKSession.update`.

\

The default implementation returns true and does nothing; data sources that hold no\
per-frame state do not need to override it.

\

**Threading contract**: the caller must ensure that `prepareFrame`, `NSDKSession.update`,\
and any `latest*` accessor calls are serialized — i.e., a complete\
`prepareFrame → update → (accessors finish)` cycle must complete before the next\
`prepareFrame` call begins. This is typically achieved by driving the cycle from a\
single-threaded executor or a coroutine with an in-flight gate.

</div>

------------------------------------------------------------------------

</div>

</div>
