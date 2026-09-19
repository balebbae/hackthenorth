---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.DepthConfig/
title: DepthConfig
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk/ "com.nianticspatial.nsdk") 

</div>

<div class="api-title">

#  DepthConfig

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">DepthConfig</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Configuration parameters for ARDK's Depth System.

## Basic Usage<a href="#basic-usage" class="hash-link" aria-label="Direct link to Basic Usage" title="Direct link to Basic Usage">​</a>

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val config = DepthConfig(
framerate = 120
featureMode = AwarenessFeatureMode.SMOOTH,
)
ARDK.ConfigureDepth(handle, config)
```

</div>

</div>

## See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

- ARDK.ConfigureDepth
- ARDK.CreateDepth

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
<td><span id="property-featuremode"></span><span class="ctoken-line"><span class="ctoken class-name">featureMode</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessFeatureMode/" title="Browse to AwarenessFeatureMode">AwarenessFeatureMode</a></span></span></td>
<td><div class="ctoken comment">
Specify mode to internally select model for depth estimation. Each model<br />
selects a model that has different performance and quality characteristics.<br />
<strong>Default:</strong> <code>Unspecified</code>
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-framerate"></span><span class="ctoken-line"><span class="ctoken class-name">framerate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
Framerate which the Depth system takes in input. Depth is an expensive<br />
system so keeping framerate lower is recommended,<br />
<strong>Default:</strong> <code>10</code>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
