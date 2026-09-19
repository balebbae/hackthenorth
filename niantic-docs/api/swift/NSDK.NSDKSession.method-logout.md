---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-logout/
title: logout
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKSession/ "NSDKSession") 

</div>

<div class="api-title">

#  logout

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">logout</span><span class="ctoken plain">()</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Clears cached auth tokens from persistent storage without requiring an NSDK session.\
This is the preferred logout path. It can be called before NSDK is initialized or after\
it has been destroyed. Any running session will pick up the cleared tokens on its next\
reconciliation cycle.

</div>

------------------------------------------------------------------------

</div>

</div>
