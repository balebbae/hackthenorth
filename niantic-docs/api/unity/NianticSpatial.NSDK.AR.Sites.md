---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites/
title: NianticSpatial.NSDK.AR.Sites
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") 

</div>

<div class="api-title">

#  Sites

</div>

------------------------------------------------------------------------

## Classes<a href="#classes" class="hash-link" aria-label="Direct link to Classes" title="Direct link to Classes">​</a>

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
<td><span id="class-sitesclient"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClient/" title="Client for interacting with the Sites Manager service....">SitesClient</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.idisposable?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">IDisposable</a></span></span></td>
<td><div class="ctoken comment">
Client for interacting with the Sites Manager service.<br />
Provides methods to query organizational hierarchy data including users,<br />
organizations, sites, and assets.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-sitesclientmanager"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClientManager/" title="A MonoBehaviour component that provides access to the Sites API....">SitesClientManager</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">MonoBehaviour</a></span></span></td>
<td><div class="ctoken comment">
A MonoBehaviour component that provides access to the Sites API.<br />
Use this to query organizational hierarchy data including users, organizations, sites, and assets.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Structs<a href="#structs" class="hash-link" aria-label="Direct link to Structs" title="Direct link to Structs">​</a>

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
<td><span id="struct-assetinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetInfo/" title="Information about an asset....">AssetInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment">
Information about an asset.<br />
Maps to proto messages AssetRecord, AssetData, and AssetComputedValues.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-assetmeshdata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetMeshData/" title="Mesh-specific asset data....">AssetMeshData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment">
Mesh-specific asset data.<br />
Maps to proto message AssetMeshData.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-assetresult"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetResult/" title="Result of an asset information request.">AssetResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment">
Result of an asset information request.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-assetsplatdata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetSplatData/" title="Splat-specific asset data....">AssetSplatData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment">
Splat-specific asset data.<br />
Maps to proto message AssetSplatData.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-assetvpsdata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetVpsData/" title="VPS-specific asset data....">AssetVpsData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment">
VPS-specific asset data.<br />
Maps to proto message AssetVpsData.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-organizationinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.OrganizationInfo/" title="Information about an organization.">OrganizationInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment">
Information about an organization.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-organizationresult"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.OrganizationResult/" title="Result of an organization information request.">OrganizationResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment">
Result of an organization information request.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-siteassetsinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SiteAssetsInfo/" title="A single entry in a site-assets location query result.">SiteAssetsInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment">
A single entry in a site-assets location query result.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-siteassetsresult"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SiteAssetsResult/" title="Result of a site-assets location query.">SiteAssetsResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment">
Result of a site-assets location query.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-siteinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SiteInfo/" title="Information about a site.">SiteInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment">
Information about a site.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-siteresult"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SiteResult/" title="Result of a site information request.">SiteResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment">
Result of a site information request.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-userinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.UserInfo/" title="Information about a user.">UserInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment">
Information about a user.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-userresult"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.UserResult/" title="Result of a user information request.">UserResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span></td>
<td><div class="ctoken comment">
Result of a user information request.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Enums<a href="#enums" class="hash-link" aria-label="Direct link to Enums" title="Direct link to Enums">​</a>

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
<td><span id="enum-assetdeploymenttype"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetDeploymentType/" title="Asset deployment type....">AssetDeploymentType</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetDeploymentType/" title="Asset deployment type....">AssetDeploymentType</a></span></span></td>
<td><div class="ctoken comment">
Asset deployment type.<br />
Maps to proto enum AssetDeploymentType.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-assetpipelinejobstatus"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetPipelineJobStatus/" title="Asset pipeline job status....">AssetPipelineJobStatus</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetPipelineJobStatus/" title="Asset pipeline job status....">AssetPipelineJobStatus</a></span></span></td>
<td><div class="ctoken comment">
Asset pipeline job status.<br />
Maps to proto enum AssetPipelineJobStatus.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-assetstatustype"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetStatusType/" title="Asset status....">AssetStatusType</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetStatusType/" title="Asset status....">AssetStatusType</a></span></span></td>
<td><div class="ctoken comment">
Asset status.<br />
Maps to proto enum AssetStatusType.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-assettype"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetType/" title="Asset type - determines which typed asset data is present....">AssetType</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetType/" title="Asset type - determines which typed asset data is present....">AssetType</a></span></span></td>
<td><div class="ctoken comment">
Asset type - determines which typed asset data is present.<br />
Maps to proto enum AssetType.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-siteserror"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesError/" title="Error codes for Sites API operations.">SitesError</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesError/" title="Error codes for Sites API operations.">SitesError</a></span></span></td>
<td><div class="ctoken comment">
Error codes for Sites API operations.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-sitesrequeststatus"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesRequestStatus/" title="Status of a Sites API request.">SitesRequestStatus</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesRequestStatus/" title="Status of a Sites API request.">SitesRequestStatus</a></span></span></td>
<td><div class="ctoken comment">
Status of a Sites API request.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
