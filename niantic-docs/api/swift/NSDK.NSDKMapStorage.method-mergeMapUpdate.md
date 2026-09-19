---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMapStorage.method-mergeMapUpdate/
title: mergeMapUpdate
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

#  mergeMapUpdate

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">mergeMapUpdate</span><span class="ctoken plain">(</span><span class="ctoken plain">existingMap</span><span class="ctoken plain">: </span><span class="ctoken class-name">[NSDKBuffer](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKBuffer/ "A buffer containing binary data for NSDK operations....")</span><span class="ctoken plain">, </span><span class="ctoken plain">mapUpdate</span><span class="ctoken plain">: </span><span class="ctoken class-name">[NSDKBuffer](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKBuffer/ "A buffer containing binary data for NSDK operations....")</span><span class="ctoken plain">) </span><span class="ctoken keyword">throws</span><span class="ctoken plain"> -\> </span><span class="ctoken class-name">[NSDKBuffer](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKBuffer/ "A buffer containing binary data for NSDK operations....")</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Merges a map update into an existing map.\
This method combines incremental map updates with a base map to produce\
a merged map buffer containing the complete map data.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The merged map buffer

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `NSDKError` of type `NSDKError.invalidArgument`or `NSDKError.nullArgument` indicating a problem with either argument . Check NSDK's C logs for more information.

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
<td><span id="external parameter-existingmap"></span><span class="ctoken-line"><span class="ctoken class-name">existingMap</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKBuffer/" title="A buffer containing binary data for NSDK operations....">NSDKBuffer</a></span></span></td>
<td><div class="ctoken comment">
The existing map to merge the update into.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-mapupdate"></span><span class="ctoken-line"><span class="ctoken class-name">mapUpdate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKBuffer/" title="A buffer containing binary data for NSDK operations....">NSDKBuffer</a></span></span></td>
<td><div class="ctoken comment">
The map update to merge into the existing map.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
