---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClient.Dispose/
title: Dispose
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Sites](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites/ "NianticSpatial.NSDK.AR.Sites") <span class="api-breadcrumbs-nav">←</span>[SitesClient](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClient/ "NianticSpatial.NSDK.AR.Sites.SitesClient") 

</div>

<div class="api-title">

#  Dispose

<div class="api-package">

Releases native resources.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">void</span><span class="ctoken plain"> </span><span class="ctoken class-name">Dispose</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Releases native resources.

</div>

#### Remarks<a href="#remarks" class="hash-link" aria-label="Direct link to Remarks" title="Direct link to Remarks">​</a>

<div class="ctoken comment">

The Unity SDK does not explicitly destroy the SitesManager component because\
we can't easily guarantee the component will be destroyed before NsdkUnityContext is.\
The native NSDK holds a shared pointer to its components, so when it is destroyed,\
all its components will be released too.

</div>

------------------------------------------------------------------------

</div>

</div>
