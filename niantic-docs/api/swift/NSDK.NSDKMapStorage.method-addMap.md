---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMapStorage.method-addMap/
title: addMap
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

#  addMap

<div class="api-package">

Adds previously serialized map data to the map storage.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">addMap</span><span class="ctoken plain">(</span><span class="ctoken plain">map</span><span class="ctoken plain">: </span><span class="ctoken class-name">[NSDKBuffer](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKBuffer/ "A buffer containing binary data for NSDK operations....")</span><span class="ctoken plain">) </span><span class="ctoken keyword">throws</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Adds previously serialized map data to the map storage.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `NSDKError.invalidArgument`or `NSDKError.nullArgument` indicating a problem with the `map` argument . Check NSDK's C logs for more information.

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
<td><span id="external parameter-map"></span><span class="ctoken-line"><span class="ctoken class-name">map</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKBuffer/" title="A buffer containing binary data for NSDK operations....">NSDKBuffer</a></span></span></td>
<td><div class="ctoken comment">
The serialized map data to add. It should be encoded as a<br />
DeviceMap protobuf and can be obtained from <code>mapData()</code>, <code>mapUpdate()</code>,<br />
or <code>mergeMapUpdate(existingMap:mapUpdate:)</code>.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
