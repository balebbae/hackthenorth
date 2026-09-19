---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AsyncResult/
title: AsyncResult
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk/ "com.nianticspatial.nsdk") 

</div>

<div class="api-title">

#  AsyncResult

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">sealed</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">AsyncResult</span><span class="ctoken punctuation">\<</span><span class="ctoken class-name keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name">TData</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name">TError</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[ErrorCodeProvider](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ErrorCodeProvider/ "Browse to ErrorCodeProvider")</span><span class="ctoken punctuation">\></span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Represents the final result of a completed asynchronous operation, which can either be a success, a failure, or a timeout. \* This is the public-facing result type returned by `suspend` functions. It intentionally omits an "in-progress" state, guaranteeing that the operation has reached a terminal state.

------------------------------------------------------------------------

</div>

</div>
