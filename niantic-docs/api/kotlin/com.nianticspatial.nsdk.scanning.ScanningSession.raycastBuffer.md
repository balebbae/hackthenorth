---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession.raycastBuffer/
title: raycastBuffer
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.scanning](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning/ "com.nianticspatial.nsdk.scanning") <span class="api-breadcrumbs-nav">←</span>[ScanningSession](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession/ "com.nianticspatial.nsdk.scanning.ScanningSession") 

</div>

<div class="api-title">

#  raycastBuffer

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">raycastBuffer</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[RaycastBuffer](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.RaycastBuffer/ "A read-only container for the raycast buffer information generated during scanning.")</span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Get the most recently computed raycast buffers.

\

Once the session has been started and all the requested data has been sent through the\
ARDK session, a buffer should become available after a brief computation period.

\

\> Note: Raycast visualization must have been enabled in the configuration.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The most recently computed raycast buffers if available, null if not.

</div>

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

- configure

------------------------------------------------------------------------

</div>

</div>
