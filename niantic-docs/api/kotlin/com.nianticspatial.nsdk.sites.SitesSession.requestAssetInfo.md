---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession.requestAssetInfo/
title: requestAssetInfo
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

#  requestAssetInfo

<div class="api-package">

Requests asset information by asset ID.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">suspend</span><span class="ctoken plain"> </span><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">requestAssetInfo</span><span class="ctoken punctuation">(</span><span class="ctoken plain"> </span><span class="ctoken plain">assetId</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">timeoutMs</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Long</a></span><span class="ctoken plain"> </span><span class="ctoken plain">=</span><span class="ctoken plain"> </span><span class="ctoken class-name">DEFAULT_TIMEOUT_MS</span><span class="ctoken plain"> </span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[AssetResult](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetResult/ "Result of an asset request from the Sites Manager service.")</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Requests asset information by asset ID.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

`AssetResult` containing the asset information.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `SitesException` — if the request fails with an error.
- `kotlinx.coroutines.CancellationException` — if the coroutine is cancelled.

------------------------------------------------------------------------

</div>

</div>
