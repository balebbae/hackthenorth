---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKDeviceMappingSession.struct-Configuration/
title: Configuration
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKDeviceMappingSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKDeviceMappingSession/ "NSDKDeviceMappingSession") 

</div>

<div class="api-title">

#  Configuration

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">struct</span><span class="ctoken plain"> </span><span class="ctoken class-name">Configuration</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Configuration settings for the mapping process. This structure defines various parameters that control how the mapping algorithm behaves during map creation, including feature detection, tracking edges, and node splitting criteria.

------------------------------------------------------------------------

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">init</span><span class="ctoken plain">()</span></span>

</div>

#### Summary<a href="#summary-1" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Creates a new configuration with default values.\
All parameters are set to their default values, which provide a good starting point\
for most mapping scenarios.

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
<td><span id="property-learnedfeaturesenabled"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">learnedFeaturesEnabled</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
Enables the use of learned features for mapping.<br />
When <code>true</code>, the mapping system uses neural network learned features for improved<br />
mapping quality. When <code>false</code> (default), the legacy feature detection method is used.<br />
Learned features generally provide better results but require more processing power.<br />
- Attention: Maps created with different feature detection methods are not compatible.<br />
For example, a map created with learned features cannot be merged with a map created with<br />
legacy feature detection.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-mapperframerate"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">mapperFrameRate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/uint32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UInt32</a></span></span></td>
<td><div class="ctoken comment">
Target frame rate for the mapping process.<br />
Specifies the desired FPS for map processing. The actual frame rate may be lower<br />
due to device performance limitations. A value of <code>0</code> (default) uses automatic<br />
frame rate selection based on device capabilities.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-splittermaxdistancemeters"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">splitterMaxDistanceMeters</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Maximum distance before creating a new map node (in meters).<br />
When the device travels more than this distance from the current map node,<br />
a new node will be created. A value of <code>0</code> will use native default values.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-splittermaxdurationseconds"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">splitterMaxDurationSeconds</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Maximum duration before creating a new map node (in seconds).<br />
When mapping continues for longer than this duration on a single node,<br />
a new node will be created. A value of <code>0</code> will use native default values.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-trackingedgesdisabled"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">trackingEdgesDisabled</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
Controls whether tracking edges between maps are disabled.<br />
When <code>false</code> (default), the system can form tracking edges between different map nodes,<br />
improving overall map consistency. Set to <code>true</code> to disable this feature if needed<br />
for specific use cases.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
