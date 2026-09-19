---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Auth.AuthClient.StaticLogout/
title: StaticLogout
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Auth](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Auth/ "NianticSpatial.NSDK.AR.Auth") <span class="api-breadcrumbs-nav">←</span>[AuthClient](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Auth.AuthClient/ "NianticSpatial.NSDK.AR.Auth.AuthClient") 

</div>

<div class="api-title">

#  StaticLogout

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">void</span><span class="ctoken plain"> </span><span class="ctoken class-name">StaticLogout</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Clears cached auth tokens from persistent storage without requiring an NSDK context.\
This is the preferred logout path — safe to call before NSDK is initialized or after\
it has been destroyed. Any running session will pick up the cleared tokens on its next\
reconciliation cycle.

</div>

------------------------------------------------------------------------

</div>

</div>
