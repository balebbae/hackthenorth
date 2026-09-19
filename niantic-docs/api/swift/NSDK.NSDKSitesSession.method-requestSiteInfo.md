---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSitesSession.method-requestSiteInfo/
title: requestSiteInfo
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKSitesSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKSitesSession/ "NSDKSitesSession") 

</div>

<div class="api-title">

#  requestSiteInfo

<div class="api-package">

Requests site info and waits for the result.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">requestSiteInfo</span><span class="ctoken plain">(</span><span class="ctoken plain">siteId</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">, </span><span class="ctoken plain">pollingInterval</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/timeinterval" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TimeInterval</a></span><span class="ctoken plain"> = 0.5, </span><span class="ctoken plain">timeout</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/timeinterval" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TimeInterval</a></span><span class="ctoken plain"> = 60.0) </span><span class="ctoken keyword">async</span><span class="ctoken plain"> </span><span class="ctoken keyword">throws</span><span class="ctoken plain"> -\> </span><span class="ctoken class-name">[SiteResult](https://www.nianticspatial.com/docs/api/swift/NSDK.class-SiteResult/ "Contains all the ``SiteInfo`` objects returned by a query to the Sites Manager service.")</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Requests site info and waits for the result.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A `SiteResult` containing the site info.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- \- `CancellationError` if the Task running this function was cancelled. - `TimeoutError` if the function timed out before it could complete execution. - `SitesResult.Error` if there was an error specific to the network query.

### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

<table class="api-table">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr class="api-table-row">
<td><span id="external parameter-siteid"></span><span class="ctoken-line"><span class="ctoken class-name">siteId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span></span></td>
<td><div class="ctoken comment">
The site ID to fetch info for.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-pollinginterval"></span><span class="ctoken-line"><span class="ctoken class-name">pollingInterval</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/timeinterval" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TimeInterval</a></span></span></td>
<td><div class="ctoken comment">
The interval between status checks (default: 0.5 seconds).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-timeout"></span><span class="ctoken-line"><span class="ctoken class-name">timeout</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/timeinterval" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TimeInterval</a></span></span></td>
<td><div class="ctoken comment">
Maximum time to wait for completion (default: 60 seconds).
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
