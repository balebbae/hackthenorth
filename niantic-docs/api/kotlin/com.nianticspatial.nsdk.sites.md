---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites/
title: com.nianticspatial.nsdk.sites
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") 

</div>

<div class="api-title">

#  sites

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
<td><span id="class-sitesexception"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesException/" title="Exception thrown when a Sites Manager operation fails.">SitesException</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesException/" title="Exception thrown when a Sites Manager operation fails.">SitesException</a></span></span></td>
<td><div class="ctoken comment">
Exception thrown when a Sites Manager operation fails.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-sitessession"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession/" title="A session for interacting with the Sites Manager service....">SitesSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession/" title="A session for interacting with the Sites Manager service....">SitesSession</a></span></span></td>
<td><div class="ctoken comment">
A session for interacting with the Sites Manager service.<br />
<code>SitesSession</code> provides capabilities for querying organizational hierarchy data<br />
including users, organizations, sites, and assets.<br />
### Usage<br />
<strong>1. Acquire the Sites session:</strong>
</div>
<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">
<div class="codeBlockContent_QJqH">
<pre class="prism-code language-kotlin codeBlock_bY9V thin-scrollbar" tabindex="0" style="color:#393A34;background-color:#f6f8fa"><code>val sitesSession = ardkSession.sites.acquire()</code></pre>
</div>
</div>
<div class="ctoken comment">
<strong>2. Query user information:</strong>
</div>
<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">
<div class="codeBlockContent_QJqH">
<pre class="prism-code language-kotlin codeBlock_bY9V thin-scrollbar" tabindex="0" style="color:#393A34;background-color:#f6f8fa"><code>val userResult = sitesSession.requestSelfUserInfo()
if (userResult.status == SitesRequestStatus.SUCCESS) {
val user = userResult.user
println(&quot;User: ${user?.firstName} ${user?.lastName}&quot;)
}</code></pre>
</div>
</div>
<div class="ctoken comment">
<strong>3. Query organizations for a user:</strong>
</div>
<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">
<div class="codeBlockContent_QJqH">
<pre class="prism-code language-kotlin codeBlock_bY9V thin-scrollbar" tabindex="0" style="color:#393A34;background-color:#f6f8fa"><code>val orgsResult = sitesSession.requestOrganizationsForUser(userId)
orgsResult.organizations.forEach { org -&gt;
println(&quot;Organization: ${org.name}&quot;)
}</code></pre>
</div>
</div>
<div class="ctoken comment">
<strong>4. Query sites for an organization:</strong>
</div>
<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">
<div class="codeBlockContent_QJqH">
<pre class="prism-code language-kotlin codeBlock_bY9V thin-scrollbar" tabindex="0" style="color:#393A34;background-color:#f6f8fa"><code>val sitesResult = sitesSession.requestSitesForOrganization(orgId)
sitesResult.sites.forEach { site -&gt;
println(&quot;Site: ${site.name}&quot;)
}</code></pre>
</div>
</div>
<div class="ctoken comment">
<strong>5. Query assets for a site:</strong>
</div>
<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">
<div class="codeBlockContent_QJqH">
<pre class="prism-code language-kotlin codeBlock_bY9V thin-scrollbar" tabindex="0" style="color:#393A34;background-color:#f6f8fa"><code>val assetsResult = sitesSession.requestAssetsForSite(siteId)
assetsResult.assets.forEach { asset -&gt;
println(&quot;Asset: ${asset.name} (${asset.type})&quot;)
}</code></pre>
</div>
</div>
<div class="ctoken comment">
<strong>6. Clean up when done:</strong>
</div>
<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">
<div class="codeBlockContent_QJqH">
<pre class="prism-code language-kotlin codeBlock_bY9V thin-scrollbar" tabindex="0" style="color:#393A34;background-color:#f6f8fa"><code>sitesSession.close()</code></pre>
</div>
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-typedassetdata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.TypedAssetData/" title="Discriminated union for typed asset data....">TypedAssetData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.TypedAssetData/" title="Discriminated union for typed asset data....">TypedAssetData</a></span></span></td>
<td><div class="ctoken comment">
Discriminated union for typed asset data.<br />
One of mesh, splat, or vps will be set based on the asset type.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Data Classes<a href="#data-classes" class="hash-link" aria-label="Direct link to Data Classes" title="Direct link to Data Classes">​</a>

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
<td><span id="data class-assetinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetInfo/" title="Represents asset information from the Sites Manager service....">AssetInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetInfo/" title="Represents asset information from the Sites Manager service....">AssetInfo</a></span></span></td>
<td><div class="ctoken comment">
Represents asset information from the Sites Manager service.<br />
Maps to proto messages AssetRecord, AssetData, and AssetComputedValues.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-assetmeshdata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetMeshData/" title="Mesh-specific asset data....">AssetMeshData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetMeshData/" title="Mesh-specific asset data....">AssetMeshData</a></span></span></td>
<td><div class="ctoken comment">
Mesh-specific asset data.<br />
Maps to proto message AssetMeshData.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-assetresult"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetResult/" title="Result of an asset request from the Sites Manager service.">AssetResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetResult/" title="Result of an asset request from the Sites Manager service.">AssetResult</a></span></span></td>
<td><div class="ctoken comment">
Result of an asset request from the Sites Manager service.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-assetsplatdata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetSplatData/" title="Splat-specific asset data....">AssetSplatData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetSplatData/" title="Splat-specific asset data....">AssetSplatData</a></span></span></td>
<td><div class="ctoken comment">
Splat-specific asset data.<br />
Maps to proto message AssetSplatData.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-assetvpsdata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetVpsData/" title="VPS-specific asset data....">AssetVpsData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetVpsData/" title="VPS-specific asset data....">AssetVpsData</a></span></span></td>
<td><div class="ctoken comment">
VPS-specific asset data.<br />
Maps to proto message AssetVpsData.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-organizationinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.OrganizationInfo/" title="Represents organization information from the Sites Manager service.">OrganizationInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.OrganizationInfo/" title="Represents organization information from the Sites Manager service.">OrganizationInfo</a></span></span></td>
<td><div class="ctoken comment">
Represents organization information from the Sites Manager service.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-organizationresult"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.OrganizationResult/" title="Result of an organization request from the Sites Manager service.">OrganizationResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.OrganizationResult/" title="Result of an organization request from the Sites Manager service.">OrganizationResult</a></span></span></td>
<td><div class="ctoken comment">
Result of an organization request from the Sites Manager service.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-siteassetsinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SiteAssetsInfo/" title="A single entry in a site-assets location query result.">SiteAssetsInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SiteAssetsInfo/" title="A single entry in a site-assets location query result.">SiteAssetsInfo</a></span></span></td>
<td><div class="ctoken comment">
A single entry in a site-assets location query result.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-siteassetsresult"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SiteAssetsResult/" title="Result of a site-assets location query from the Sites Manager service.">SiteAssetsResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SiteAssetsResult/" title="Result of a site-assets location query from the Sites Manager service.">SiteAssetsResult</a></span></span></td>
<td><div class="ctoken comment">
Result of a site-assets location query from the Sites Manager service.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-siteinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SiteInfo/" title="Represents site information from the Sites Manager service.">SiteInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SiteInfo/" title="Represents site information from the Sites Manager service.">SiteInfo</a></span></span></td>
<td><div class="ctoken comment">
Represents site information from the Sites Manager service.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-siteresult"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SiteResult/" title="Result of a site request from the Sites Manager service.">SiteResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SiteResult/" title="Result of a site request from the Sites Manager service.">SiteResult</a></span></span></td>
<td><div class="ctoken comment">
Result of a site request from the Sites Manager service.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-userinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.UserInfo/" title="Represents user information from the Sites Manager service.">UserInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.UserInfo/" title="Represents user information from the Sites Manager service.">UserInfo</a></span></span></td>
<td><div class="ctoken comment">
Represents user information from the Sites Manager service.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-userresult"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.UserResult/" title="Result of a user information request from the Sites Manager service.">UserResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.UserResult/" title="Result of a user information request from the Sites Manager service.">UserResult</a></span></span></td>
<td><div class="ctoken comment">
Result of a user information request from the Sites Manager service.
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
<td><span id="enum-assetdeploymenttype"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetDeploymentType/" title="Asset deployment type....">AssetDeploymentType</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetDeploymentType/" title="Asset deployment type....">AssetDeploymentType</a></span></span></td>
<td><div class="ctoken comment">
Asset deployment type.<br />
Maps to proto enum AssetDeploymentType.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-assetpipelinejobstatus"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetPipelineJobStatus/" title="Asset pipeline job status....">AssetPipelineJobStatus</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetPipelineJobStatus/" title="Asset pipeline job status....">AssetPipelineJobStatus</a></span></span></td>
<td><div class="ctoken comment">
Asset pipeline job status.<br />
Maps to proto enum AssetPipelineJobStatus.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-assetstatustype"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetStatusType/" title="Asset status....">AssetStatusType</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetStatusType/" title="Asset status....">AssetStatusType</a></span></span></td>
<td><div class="ctoken comment">
Asset status.<br />
Maps to proto enum AssetStatusType.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-assettype"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetType/" title="Asset type - determines which typed asset data is present....">AssetType</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetType/" title="Asset type - determines which typed asset data is present....">AssetType</a></span></span></td>
<td><div class="ctoken comment">
Asset type - determines which typed asset data is present.<br />
Maps to proto enum AssetType.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-siteserror"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesError/" title="Error codes that can occur during Sites Manager operations....">SitesError</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesError/" title="Error codes that can occur during Sites Manager operations....">SitesError</a></span></span></td>
<td><div class="ctoken comment">
Error codes that can occur during Sites Manager operations.<br />
These errors indicate various failure conditions when communicating<br />
with the Sites Manager service.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-sitesrequeststatus"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesRequestStatus/" title="Status of a Sites Manager network request.">SitesRequestStatus</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesRequestStatus/" title="Status of a Sites Manager network request.">SitesRequestStatus</a></span></span></td>
<td><div class="ctoken comment">
Status of a Sites Manager network request.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
