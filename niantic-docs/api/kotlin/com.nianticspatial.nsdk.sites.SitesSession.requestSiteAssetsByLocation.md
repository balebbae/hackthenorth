---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession.requestSiteAssetsByLocation/
title: requestSiteAssetsByLocation
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.sites](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites/ "com.nianticspatial.nsdk.sites") <span class="api-breadcrumbs-nav">←</span>[SitesSession](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession/ "com.nianticspatial.nsdk.sites.SitesSession") 

</div>

<div class="api-title">

#  requestSiteAssetsByLocation

<div class="api-package">

Requests sites and assets near a GPS coordinate.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">suspend</span><span class="ctoken plain"> </span><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">requestSiteAssetsByLocation</span><span class="ctoken punctuation">(</span><span class="ctoken plain"> </span><span class="ctoken plain">lat</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Double</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">lng</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Double</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">radiusMeters</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Double</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">assetType</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[AssetType](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetType/ "Asset type - determines which typed asset data is present....")</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">timeoutMs</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Long</a></span><span class="ctoken plain"> </span><span class="ctoken plain">=</span><span class="ctoken plain"> </span><span class="ctoken class-name">DEFAULT_TIMEOUT_MS</span><span class="ctoken plain"> </span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[SiteAssetsResult](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SiteAssetsResult/ "Result of a site-assets location query from the Sites Manager service.")</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Requests sites and assets near a GPS coordinate.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

`SiteAssetsResult` containing the list of site-assets entries ordered by distance.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `SitesException` — if the request fails with an error.
- `kotlinx.coroutines.CancellationException` — if the coroutine is cancelled.

------------------------------------------------------------------------

</div>

</div>
