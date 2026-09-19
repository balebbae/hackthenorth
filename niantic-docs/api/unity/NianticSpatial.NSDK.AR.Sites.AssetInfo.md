---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetInfo/
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

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Sites](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites/ "NianticSpatial.NSDK.AR.Sites") 

</div>

<div class="api-title">

#  AssetInfo

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken keyword">struct</span><span class="ctoken plain"> </span><span class="ctoken class-name">AssetInfo</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Information about an asset. Maps to proto messages AssetRecord, AssetData, and AssetComputedValues.

------------------------------------------------------------------------

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name">AssetInfo</span><span class="ctoken punctuation">(</span><span class="ctoken class-name keyword">string</span><span class="ctoken plain"> </span><span class="ctoken class-name">id</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">string</span><span class="ctoken plain"> </span><span class="ctoken class-name">siteId</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">string</span><span class="ctoken plain"> </span><span class="ctoken class-name">name</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">string</span><span class="ctoken plain"> </span><span class="ctoken class-name">description</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">[AssetType](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetType/ "Asset type - determines which typed asset data is present....")</span><span class="ctoken plain"> </span><span class="ctoken class-name">assetType</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">[AssetStatusType](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetStatusType/ "Asset status....")</span><span class="ctoken plain"> </span><span class="ctoken class-name">assetStatus</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">[AssetDeploymentType](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetDeploymentType/ "Asset deployment type....")</span><span class="ctoken plain"> </span><span class="ctoken class-name">deployment</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">[AssetMeshData](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetMeshData/ "Mesh-specific asset data....")</span><span class="ctoken punctuation">\></span><span class="ctoken plain"> </span><span class="ctoken class-name">meshData</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">[AssetSplatData](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetSplatData/ "Splat-specific asset data....")</span><span class="ctoken punctuation">\></span><span class="ctoken plain"> </span><span class="ctoken class-name">splatData</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">[AssetVpsData](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetVpsData/ "VPS-specific asset data....")</span><span class="ctoken punctuation">\></span><span class="ctoken plain"> </span><span class="ctoken class-name">vpsData</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">string</span><span class="ctoken plain"> </span><span class="ctoken class-name">pipelineJobId</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">[AssetPipelineJobStatus](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetPipelineJobStatus/ "Asset pipeline job status....")</span><span class="ctoken plain"> </span><span class="ctoken class-name">pipelineJobStatus</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ireadonlylist-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">IReadOnlyList</a></span><span class="ctoken punctuation">\<</span><span class="ctoken class-name keyword">string</span><span class="ctoken punctuation">\></span><span class="ctoken plain"> </span><span class="ctoken class-name">sourceScanIds</span><span class="ctoken punctuation">)</span></span>

</div>

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
<td><span id="property-assetstatus"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">AssetStatus</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetStatusType/" title="Asset status....">AssetStatusType</a></span></span></td>
<td><div class="ctoken comment">
The asset status.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-assettype"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">AssetType</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetType/" title="Asset type - determines which typed asset data is present....">AssetType</a></span></span></td>
<td><div class="ctoken comment">
The asset type - determines which typed asset data is present.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-deployment"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Deployment</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetDeploymentType/" title="Asset deployment type....">AssetDeploymentType</a></span></span></td>
<td><div class="ctoken comment">
The asset deployment type.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-description"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Description</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
The asset's description, or null if not set.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-id"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Id</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
The unique identifier for the asset.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-meshdata"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">MeshData</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetMeshData/" title="Mesh-specific asset data....">AssetMeshData</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Mesh-specific data. Only valid when AssetType is Mesh.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-name"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Name</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
The asset's display name.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-pipelinejobid"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">PipelineJobId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
The pipeline job ID associated with this asset, or null if not applicable.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-pipelinejobstatus"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">PipelineJobStatus</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetPipelineJobStatus/" title="Asset pipeline job status....">AssetPipelineJobStatus</a></span></span></td>
<td><div class="ctoken comment">
The pipeline job status.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-siteid"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">SiteId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
The site ID this asset belongs to.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-sourcescanids"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">SourceScanIds</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ireadonlylist-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">IReadOnlyList</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name keyword">string</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
The source scan IDs used to create this asset.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-splatdata"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">SplatData</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetSplatData/" title="Splat-specific asset data....">AssetSplatData</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Splat-specific data. Only valid when AssetType is Splat.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-vpsdata"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">VpsData</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetVpsData/" title="VPS-specific asset data....">AssetVpsData</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
VPS-specific data. Only valid when AssetType is VpsInfo.
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
<td><span id="method-tostring"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.AssetInfo.ToString/" title="Browse to ToString">ToString</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
