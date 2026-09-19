---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKSitesSession/
title: NSDKSitesSession
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") 

</div>

<div class="api-title">

#  NSDKSitesSession

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">NSDKSitesSession</span></span>

------------------------------------------------------------------------

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

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
<td><span id="method-requestassetinfo"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSitesSession.method-requestAssetInfo/" title="Requests asset info and waits for the result.">requestAssetInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-AssetResult/" title="Contains all the ``AssetInfo`` objects returned by a query to the Sites Manager service.">AssetResult</a></span></span></td>
<td><div class="ctoken comment">
Requests asset info and waits for the result.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-requestassetsforsite"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSitesSession.method-requestAssetsForSite/" title="Requests assets for a site and waits for the result.">requestAssetsForSite</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-AssetResult/" title="Contains all the ``AssetInfo`` objects returned by a query to the Sites Manager service.">AssetResult</a></span></span></td>
<td><div class="ctoken comment">
Requests assets for a site and waits for the result.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-requestorganizationinfo"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSitesSession.method-requestOrganizationInfo/" title="Requests organization info and waits for the result.">requestOrganizationInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-OrganizationResult/" title="Contains all the ``OrganizationInfo`` objects returned by a query to the Sites Manager service.">OrganizationResult</a></span></span></td>
<td><div class="ctoken comment">
Requests organization info and waits for the result.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-requestorganizationsforuser"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSitesSession.method-requestOrganizationsForUser/" title="Requests organizations for a user and waits for the result....">requestOrganizationsForUser</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-OrganizationResult/" title="Contains all the ``OrganizationInfo`` objects returned by a query to the Sites Manager service.">OrganizationResult</a></span></span></td>
<td><div class="ctoken comment">
Requests organizations for a user and waits for the result.<br />
This is an async wrapper that combines request initiation and polling.<br />
It automatically handles polling until the request completes or times out.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-requestselforganizationinfo"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSitesSession.method-requestSelfOrganizationInfo/" title="Requests organizations for the current authenticated session and waits for the result.">requestSelfOrganizationInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-OrganizationResult/" title="Contains all the ``OrganizationInfo`` objects returned by a query to the Sites Manager service.">OrganizationResult</a></span></span></td>
<td><div class="ctoken comment">
Requests organizations for the current authenticated session and waits for the result.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-requestselfuserinfo"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSitesSession.method-requestSelfUserInfo/" title="Requests self user info and waits for the result....">requestSelfUserInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-UserResult/" title="Contains the user information returned by a query to the Sites Manager service.">UserResult</a></span></span></td>
<td><div class="ctoken comment">
Requests self user info and waits for the result.<br />
Uses the user ID from the authenticated session's metadata.<br />
To fetch organizations, consider using<br />
<code>requestSelfOrganizationInfo(pollingInterval:timeout:)</code> instead.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-requestsiteassetsbylocation"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSitesSession.method-requestSiteAssetsByLocation/" title="Requests sites and their assets near a GPS coordinate and waits for the result....">requestSiteAssetsByLocation</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-SiteAssetsResult/" title="Contains the ``SiteAssetsInfo`` objects returned by a location-based sites query.">SiteAssetsResult</a></span></span></td>
<td><div class="ctoken comment">
Requests sites and their assets near a GPS coordinate and waits for the result.<br />
Results are ordered by distance from the query coordinate.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-requestsiteinfo"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSitesSession.method-requestSiteInfo/" title="Requests site info and waits for the result.">requestSiteInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-SiteResult/" title="Contains all the ``SiteInfo`` objects returned by a query to the Sites Manager service.">SiteResult</a></span></span></td>
<td><div class="ctoken comment">
Requests site info and waits for the result.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-requestsitesfororganization"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSitesSession.method-requestSitesForOrganization/" title="Requests sites for an organization and waits for the result.">requestSitesForOrganization</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-SiteResult/" title="Contains all the ``SiteInfo`` objects returned by a query to the Sites Manager service.">SiteResult</a></span></span></td>
<td><div class="ctoken comment">
Requests sites for an organization and waits for the result.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-requestuserinfo"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSitesSession.method-requestUserInfo/" title="Requests user info and waits for the result.">requestUserInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-UserResult/" title="Contains the user information returned by a query to the Sites Manager service.">UserResult</a></span></span></td>
<td><div class="ctoken comment">
Requests user info and waits for the result.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
