---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClientManager/
title: SitesClientManager
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Sites](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites/ "NianticSpatial.NSDK.AR.Sites") 

</div>

<div class="api-title">

#  SitesClientManager

<div class="api-extends">

↳ extends UnityEngine.MonoBehaviour

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">SitesClientManager</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">MonoBehaviour</a></span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

A MonoBehaviour component that provides access to the Sites API. Use this to query organizational hierarchy data including users, organizations, sites, and assets.

## Remarks<a href="#remarks" class="hash-link" aria-label="Direct link to Remarks" title="Direct link to Remarks">​</a>

The SitesClientManager handles the lifecycle of the underlying SitesClient automatically. It creates the client on Awake and disposes it on OnDestroy.

------------------------------------------------------------------------

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

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
<td><span id="property-client"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Client</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClient/" title="Client for interacting with the Sites Manager service....">SitesClient</a></span></span></td>
<td><div class="ctoken comment">
The underlying SitesClient instance.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-requesttimeoutseconds"></span><span class="ctoken-line"><span class="ctoken class-name">RequestTimeoutSeconds</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The timeout for API requests in seconds.
</div></td>
</tr>
</tbody>
</table>

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
<td><span id="method-getassetinfoasync"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClientManager.GetAssetInfoAsync/" title="Gets asset information by asset ID.">GetAssetInfoAsync</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Task</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetResult/" title="Result of an asset information request.">AssetResult</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Gets asset information by asset ID.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getassetsforsiteasync"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClientManager.GetAssetsForSiteAsync/" title="Gets all assets for a site.">GetAssetsForSiteAsync</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Task</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetResult/" title="Result of an asset information request.">AssetResult</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Gets all assets for a site.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getorganizationinfoasync"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClientManager.GetOrganizationInfoAsync/" title="Gets organization information by organization ID.">GetOrganizationInfoAsync</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Task</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.OrganizationResult/" title="Result of an organization information request.">OrganizationResult</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Gets organization information by organization ID.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getorganizationsforuserasync"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClientManager.GetOrganizationsForUserAsync/" title="Gets all organizations for a user....">GetOrganizationsForUserAsync</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Task</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.OrganizationResult/" title="Result of an organization information request.">OrganizationResult</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Gets all organizations for a user.<br />
Consider using GetSelfOrganizationInfoAsync instead.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getselforganizationinfoasync"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClientManager.GetSelfOrganizationInfoAsync/" title="Gets organizations for the current authenticated session.">GetSelfOrganizationInfoAsync</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Task</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.OrganizationResult/" title="Result of an organization information request.">OrganizationResult</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Gets organizations for the current authenticated session.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getselfuserinfoasync"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClientManager.GetSelfUserInfoAsync/" title="Gets information for the currently authenticated user....">GetSelfUserInfoAsync</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Task</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.UserResult/" title="Result of a user information request.">UserResult</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Gets information for the currently authenticated user.<br />
To fetch organizations, consider using GetSelfOrganizationInfoAsync instead.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getsiteassetsbylocationasync"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClientManager.GetSiteAssetsByLocationAsync/" title="Gets sites and their assets near a GPS coordinate.">GetSiteAssetsByLocationAsync</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Task</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SiteAssetsResult/" title="Result of a site-assets location query.">SiteAssetsResult</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Gets sites and their assets near a GPS coordinate.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getsiteinfoasync"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClientManager.GetSiteInfoAsync/" title="Gets site information by site ID.">GetSiteInfoAsync</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Task</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SiteResult/" title="Result of a site information request.">SiteResult</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Gets site information by site ID.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getsitesfororganizationasync"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClientManager.GetSitesForOrganizationAsync/" title="Gets all sites for an organization.">GetSitesForOrganizationAsync</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Task</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SiteResult/" title="Result of a site information request.">SiteResult</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Gets all sites for an organization.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getuserinfoasync"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClientManager.GetUserInfoAsync/" title="Gets user information by user ID.">GetUserInfoAsync</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Task</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.UserResult/" title="Result of a user information request.">UserResult</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Gets user information by user ID.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
