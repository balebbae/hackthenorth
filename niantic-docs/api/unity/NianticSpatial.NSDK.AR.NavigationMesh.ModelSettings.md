---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh.ModelSettings/
title: ModelSettings
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.NavigationMesh](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.NavigationMesh/ "NianticSpatial.NSDK.AR.NavigationMesh") 

</div>

<div class="api-title">

#  ModelSettings

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">struct</span><span class="ctoken plain"> </span><span class="ctoken class-name">ModelSettings</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

The ModelSettings struct provides a configuration for how NsdkNavMesh scans the real environment and creates a navigable space. An instance of ModelSettings is created by the NsdkNavMeshManager using the parameters specified by the user in the Inspector, and that instance is subsequently used to create a NsdkNavMesh that is configured this way.

------------------------------------------------------------------------

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name">ModelSettings</span><span class="ctoken punctuation">(</span><span class="ctoken class-name keyword">float</span><span class="ctoken plain"> </span><span class="ctoken class-name">tileSize</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">float</span><span class="ctoken plain"> </span><span class="ctoken class-name">kernelStdDevTol</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">float</span><span class="ctoken plain"> </span><span class="ctoken class-name">maxSlope</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">float</span><span class="ctoken plain"> </span><span class="ctoken class-name">stepHeight</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">LayerMask</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">layerMask</span><span class="ctoken punctuation">)</span></span>

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
<td><span id="property-default"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Default</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">ModelSettings</span></span></td>
<td><div class="ctoken comment">
Constructs a configuration with default settings.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

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
<td><span id="field-kernelsize"></span><span class="ctoken-line"><span class="ctoken class-name">KernelSize</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The size of the kernel used to compute areal properties for each cell.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-kernelstddevtol"></span><span class="ctoken-line"><span class="ctoken class-name">KernelStdDevTol</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
The standard deviation tolerance value to use when determining node noise within a cell,<br />
outside of which the cell is considered too noisy to be walkable.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-layermask"></span><span class="ctoken-line"><span class="ctoken class-name">LayerMask</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">LayerMask</a></span></span></td>
<td><div class="ctoken comment">
Specifies the layer of the environment to raycast.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-maxslope"></span><span class="ctoken-line"><span class="ctoken class-name">MaxSlope</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
Maximum slope angle (degrees) of an area to be considered flat.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-minelevation"></span><span class="ctoken-line"><span class="ctoken class-name">MinElevation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
Minimum elevation (meters) a GridNode is expected to have in order to be walkable
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-spatialchunksize"></span><span class="ctoken-line"><span class="ctoken class-name">SpatialChunkSize</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
Size of a spatial partition in square meters.<br />
Grid cells within the same chunk will be stored together.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-stepheight"></span><span class="ctoken-line"><span class="ctoken class-name">StepHeight</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
The maximum amount two cells can differ in elevation to be considered on the same plane.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-tilesize"></span><span class="ctoken-line"><span class="ctoken class-name">TileSize</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
Size of a grid cell in meters.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
