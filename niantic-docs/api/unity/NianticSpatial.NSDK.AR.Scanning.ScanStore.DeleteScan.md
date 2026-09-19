---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanStore.DeleteScan/
title: DeleteScan
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Scanning](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning/ "NianticSpatial.NSDK.AR.Scanning") <span class="api-breadcrumbs-nav">←</span>[ScanStore](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanStore/ "NianticSpatial.NSDK.AR.Scanning.ScanStore") 

</div>

<div class="api-title">

#  DeleteScan

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">void</span><span class="ctoken plain"> </span><span class="ctoken class-name">DeleteScan</span><span class="ctoken punctuation">(</span><span class="ctoken class-name">[SavedScan](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanStore.SavedScan/ "Browse to SavedScan")</span><span class="ctoken plain"> </span><span class="ctoken class-name">scan</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Delete the given saved scan from disk.\
This must not be a scan that is currently in progress. Deleting a scan in progress is undefined behavior.\
The scan is invalid after deletion.

</div>

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
<td><span id="external parameter-scan"></span><span class="ctoken-line"><span class="ctoken class-name">scan</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanStore.SavedScan/" title="Browse to SavedScan">SavedScan</a></span></span></td>
<td><div class="ctoken comment">
The scan to delete.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
