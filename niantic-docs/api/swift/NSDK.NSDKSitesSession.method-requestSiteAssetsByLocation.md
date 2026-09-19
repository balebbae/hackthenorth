---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSitesSession.method-requestSiteAssetsByLocation/
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

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKSitesSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKSitesSession/ "NSDKSitesSession") 

</div>

<div class="api-title">

#  requestSiteAssetsByLocation

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">requestSiteAssetsByLocation</span><span class="ctoken plain">(</span><span class="ctoken plain">lat</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/double" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Double</a></span><span class="ctoken plain">, </span><span class="ctoken plain">lng</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/double" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Double</a></span><span class="ctoken plain">, </span><span class="ctoken plain">radiusMeters</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/double" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Double</a></span><span class="ctoken plain">, </span><span class="ctoken plain">assetType</span><span class="ctoken plain">: </span><span class="ctoken class-name">[AssetType](https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AssetType/ "Asset type - determines which typed asset data is present....")</span><span class="ctoken plain"> = .vpsInfo, </span><span class="ctoken plain">pollingInterval</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/timeinterval" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TimeInterval</a></span><span class="ctoken plain"> = 0.5, </span><span class="ctoken plain">timeout</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/timeinterval" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TimeInterval</a></span><span class="ctoken plain"> = 60.0) </span><span class="ctoken keyword">async</span><span class="ctoken plain"> </span><span class="ctoken keyword">throws</span><span class="ctoken plain"> -\> </span><span class="ctoken class-name">[SiteAssetsResult](https://www.nianticspatial.com/docs/api/swift/NSDK.class-SiteAssetsResult/ "Contains the ``SiteAssetsInfo`` objects returned by a location-based sites query.")</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Requests sites and their assets near a GPS coordinate and waits for the result.\
Results are ordered by distance from the query coordinate.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A `SiteAssetsResult` containing site-assets entries ordered by distance.

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
<td><span id="external parameter-lat"></span><span class="ctoken-line"><span class="ctoken class-name">lat</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/double" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Double</a></span></span></td>
<td><div class="ctoken comment">
Latitude of the query coordinate.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-lng"></span><span class="ctoken-line"><span class="ctoken class-name">lng</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/double" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Double</a></span></span></td>
<td><div class="ctoken comment">
Longitude of the query coordinate.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-radiusmeters"></span><span class="ctoken-line"><span class="ctoken class-name">radiusMeters</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/double" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Double</a></span></span></td>
<td><div class="ctoken comment">
Search radius in meters.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-assettype"></span><span class="ctoken-line"><span class="ctoken class-name">assetType</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AssetType/" title="Asset type - determines which typed asset data is present....">AssetType</a></span></span></td>
<td><div class="ctoken comment">
The type of assets to fetch (default: <code>.vpsInfo</code>).
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
