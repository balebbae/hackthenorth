---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMapStorage.method-extractMapMetadata/
title: extractMapMetadata
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKMapStorage](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKMapStorage/ "NSDKMapStorage") 

</div>

<div class="api-title">

#  extractMapMetadata

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">extractMapMetadata</span><span class="ctoken plain">(</span><span class="ctoken plain">anchorPayload</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">, </span><span class="ctoken plain">map</span><span class="ctoken plain">: </span><span class="ctoken class-name">[NSDKBuffer](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKBuffer/ "A buffer containing binary data for NSDK operations....")</span><span class="ctoken plain">) </span><span class="ctoken keyword">throws</span><span class="ctoken plain"> -\> </span><span class="ctoken class-name">[MapMetadata](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-MapMetadata/ "Structure representing the metadata of a device map for visualization and processing.")</span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Extracts metadata from a map relative to a specified anchor.\
Render the feature points in the metadata relative to the specified anchor to visualize the map.\
This is only possible when the anchor is linked directly to the map's node(s), or if\
the anchor's nodes are reachable to the map's nodes from the currently active\
transform graph.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The metadata of the map if successful, `nil` if otherwise.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `NSDKError.invalidArgument`or `NSDKError.nullArgument` indicating a problem with either argument. Check NSDK's C logs for more information.

### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

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
<td><span id="external parameter-anchorpayload"></span><span class="ctoken-line"><span class="ctoken class-name">anchorPayload</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span></span></td>
<td><div class="ctoken comment">
The base64-encoded payload of the anchor that the<br />
returned points will be relative to.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-map"></span><span class="ctoken-line"><span class="ctoken class-name">map</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKBuffer/" title="A buffer containing binary data for NSDK operations....">NSDKBuffer</a></span></span></td>
<td><div class="ctoken comment">
The map buffer to extract metadata from.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
