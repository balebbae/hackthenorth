---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClientManager.GetSiteAssetsByLocationAsync/
title: GetSiteAssetsByLocationAsync
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Sites](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites/ "NianticSpatial.NSDK.AR.Sites") <span class="api-breadcrumbs-nav">←</span>[SitesClientManager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClientManager/ "NianticSpatial.NSDK.AR.Sites.SitesClientManager") 

</div>

<div class="api-title">

#  GetSiteAssetsByLocationAsync

<div class="api-package">

Gets sites and their assets near a GPS coordinate.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Task</a></span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">[SiteAssetsResult](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SiteAssetsResult/ "Result of a site-assets location query.")</span><span class="ctoken punctuation">\></span><span class="ctoken plain"> </span><span class="ctoken class-name">GetSiteAssetsByLocationAsync</span><span class="ctoken punctuation">(</span><span class="ctoken class-name keyword">double</span><span class="ctoken plain"> </span><span class="ctoken class-name">latitude</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">double</span><span class="ctoken plain"> </span><span class="ctoken class-name">longitude</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">double</span><span class="ctoken plain"> </span><span class="ctoken class-name">radiusMeters</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">[AssetType](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetType/ "Asset type - determines which typed asset data is present....")</span><span class="ctoken plain"> </span><span class="ctoken class-name">assetType</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CancellationToken</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">cancellationToken</span><span class="ctoken plain"> </span><span class="ctoken punctuation">=</span><span class="ctoken plain"> </span><span class="ctoken plain">default</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Gets sites and their assets near a GPS coordinate.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The site-assets result ordered by distance.

</div>

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
<td><span id="external parameter-latitude"></span><span class="ctoken-line"><span class="ctoken class-name">latitude</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">double</span></span></td>
<td><div class="ctoken comment">
Latitude of the query coordinate, in degrees.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-longitude"></span><span class="ctoken-line"><span class="ctoken class-name">longitude</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">double</span></span></td>
<td><div class="ctoken comment">
Longitude of the query coordinate, in degrees.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-radiusmeters"></span><span class="ctoken-line"><span class="ctoken class-name">radiusMeters</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">double</span></span></td>
<td><div class="ctoken comment">
Search radius around the coordinate, in meters.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-assettype"></span><span class="ctoken-line"><span class="ctoken class-name">assetType</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetType/" title="Asset type - determines which typed asset data is present....">AssetType</a></span></span></td>
<td><div class="ctoken comment">
The type of assets to filter results by.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-cancellationtoken"></span><span class="ctoken-line"><span class="ctoken class-name">cancellationToken</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">CancellationToken</a></span></span></td>
<td><div class="ctoken comment">
Token to cancel the operation.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
