---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetInfo/
title: AssetInfo
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

#  AssetInfo

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">data</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">AssetInfo</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Represents asset information from the Sites Manager service. Maps to proto messages AssetRecord, AssetData, and AssetComputedValues.

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
<td><span id="property-assetstatus"></span><span class="ctoken-line"><span class="ctoken class-name">assetStatus</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetStatusType/" title="Asset status....">AssetStatusType</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-assettype"></span><span class="ctoken-line"><span class="ctoken class-name">assetType</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetType/" title="Asset type - determines which typed asset data is present....">AssetType</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-deployment"></span><span class="ctoken-line"><span class="ctoken class-name">deployment</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetDeploymentType/" title="Asset deployment type....">AssetDeploymentType</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-description"></span><span class="ctoken-line"><span class="ctoken class-name">description</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-id"></span><span class="ctoken-line"><span class="ctoken class-name">id</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-meshdata"></span><span class="ctoken-line"><span class="ctoken class-name">meshData</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetMeshData/" title="Mesh-specific asset data....">AssetMeshData</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Mesh data (null if asset type is not mesh).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-name"></span><span class="ctoken-line"><span class="ctoken class-name">name</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-pipelinejobid"></span><span class="ctoken-line"><span class="ctoken class-name">pipelineJobId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-pipelinejobstatus"></span><span class="ctoken-line"><span class="ctoken class-name">pipelineJobStatus</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetPipelineJobStatus/" title="Asset pipeline job status....">AssetPipelineJobStatus</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-siteid"></span><span class="ctoken-line"><span class="ctoken class-name">siteId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-sourcescanids"></span><span class="ctoken-line"><span class="ctoken class-name">sourceScanIds</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-list" target="_blank" rel="noopener noreferrer" title="Opens an external reference">List</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-splatdata"></span><span class="ctoken-line"><span class="ctoken class-name">splatData</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetSplatData/" title="Splat-specific asset data....">AssetSplatData</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Splat data (null if asset type is not splat).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-typeddata"></span><span class="ctoken-line"><span class="ctoken class-name">typedData</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.TypedAssetData/" title="Discriminated union for typed asset data....">TypedAssetData</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-vpsdata"></span><span class="ctoken-line"><span class="ctoken class-name">vpsData</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.AssetVpsData/" title="VPS-specific asset data....">AssetVpsData</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
VPS data (null if asset type is not vps).
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
