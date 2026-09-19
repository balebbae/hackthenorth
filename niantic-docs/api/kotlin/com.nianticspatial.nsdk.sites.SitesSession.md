---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession/
title: SitesSession
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.sites](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites/ "com.nianticspatial.nsdk.sites") 

</div>

<div class="api-title">

#  SitesSession

<div class="api-extends">

↳ extends [SessionBase](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.SessionBase/ "SessionBase") 

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">SitesSession</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

A session for interacting with the Sites Manager service. `SitesSession` provides capabilities for querying organizational hierarchy data including users, organizations, sites, and assets.

### Usage<a href="#usage" class="hash-link" aria-label="Direct link to Usage" title="Direct link to Usage">​</a>

**1. Acquire the Sites session:**

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val sitesSession = ardkSession.sites.acquire()
```

</div>

</div>

**2. Query user information:**

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val userResult = sitesSession.requestSelfUserInfo()
if (userResult.status == SitesRequestStatus.SUCCESS) {
val user = userResult.user
println("User: ${user?.firstName} ${user?.lastName}")
}
```

</div>

</div>

**3. Query organizations for a user:**

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val orgsResult = sitesSession.requestOrganizationsForUser(userId)
orgsResult.organizations.forEach { org ->
println("Organization: ${org.name}")
}
```

</div>

</div>

**4. Query sites for an organization:**

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val sitesResult = sitesSession.requestSitesForOrganization(orgId)
sitesResult.sites.forEach { site ->
println("Site: ${site.name}")
}
```

</div>

</div>

**5. Query assets for a site:**

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val assetsResult = sitesSession.requestAssetsForSite(siteId)
assetsResult.assets.forEach { asset ->
println("Asset: ${asset.name} (${asset.type})")
}
```

</div>

</div>

**6. Clean up when done:**

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
sitesSession.close()
```

</div>

</div>

## See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

- requestSelfUserInfo
- requestOrganizationsForUser
- requestSitesForOrganization
- requestAssetsForSite

------------------------------------------------------------------------

## Functions<a href="#functions" class="hash-link" aria-label="Direct link to Functions" title="Direct link to Functions">​</a>

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
<td><span id="function-ondestroy"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession.onDestroy/" title="Browse to onDestroy">onDestroy</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-oninit"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession.onInit/" title="Browse to onInit">onInit</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-requestassetinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession.requestAssetInfo/" title="Requests asset information by asset ID.">requestAssetInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetResult/" title="Result of an asset request from the Sites Manager service.">AssetResult</a></span></span></td>
<td><div class="ctoken comment">
Requests asset information by asset ID.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-requestassetsforsite"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession.requestAssetsForSite/" title="Requests all assets for a site.">requestAssetsForSite</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetResult/" title="Result of an asset request from the Sites Manager service.">AssetResult</a></span></span></td>
<td><div class="ctoken comment">
Requests all assets for a site.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-requestorganizationinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession.requestOrganizationInfo/" title="Requests organization information by organization ID.">requestOrganizationInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.OrganizationResult/" title="Result of an organization request from the Sites Manager service.">OrganizationResult</a></span></span></td>
<td><div class="ctoken comment">
Requests organization information by organization ID.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-requestorganizationsforuser"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession.requestOrganizationsForUser/" title="Requests all organizations for a user....">requestOrganizationsForUser</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.OrganizationResult/" title="Result of an organization request from the Sites Manager service.">OrganizationResult</a></span></span></td>
<td><div class="ctoken comment">
Requests all organizations for a user.<br />
Consider using [requestSelfOrganizationInfo] instead.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-requestselforganizationinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession.requestSelfOrganizationInfo/" title="Requests organizations for the current authenticated session.">requestSelfOrganizationInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.OrganizationResult/" title="Result of an organization request from the Sites Manager service.">OrganizationResult</a></span></span></td>
<td><div class="ctoken comment">
Requests organizations for the current authenticated session.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-requestselfuserinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession.requestSelfUserInfo/" title="Requests information for the currently authenticated user....">requestSelfUserInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.UserResult/" title="Result of a user information request from the Sites Manager service.">UserResult</a></span></span></td>
<td><div class="ctoken comment">
Requests information for the currently authenticated user.<br />
Uses the user ID from the access token to fetch user information.<br />
To fetch organizations, consider using [requestSelfOrganizationInfo] instead.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-requestsiteassetsbylocation"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession.requestSiteAssetsByLocation/" title="Requests sites and assets near a GPS coordinate.">requestSiteAssetsByLocation</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SiteAssetsResult/" title="Result of a site-assets location query from the Sites Manager service.">SiteAssetsResult</a></span></span></td>
<td><div class="ctoken comment">
Requests sites and assets near a GPS coordinate.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-requestsiteinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession.requestSiteInfo/" title="Requests site information by site ID.">requestSiteInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SiteResult/" title="Result of a site request from the Sites Manager service.">SiteResult</a></span></span></td>
<td><div class="ctoken comment">
Requests site information by site ID.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-requestsitesfororganization"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession.requestSitesForOrganization/" title="Requests all sites for an organization.">requestSitesForOrganization</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SiteResult/" title="Result of a site request from the Sites Manager service.">SiteResult</a></span></span></td>
<td><div class="ctoken comment">
Requests all sites for an organization.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-requestuserinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession.requestUserInfo/" title="Requests user information by user ID.">requestUserInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.UserResult/" title="Result of a user information request from the Sites Manager service.">UserResult</a></span></span></td>
<td><div class="ctoken comment">
Requests user information by user ID.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
