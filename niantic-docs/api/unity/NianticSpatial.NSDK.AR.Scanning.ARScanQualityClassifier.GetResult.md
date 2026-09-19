---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanQualityClassifier.GetResult/
title: GetResult
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Scanning](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning/ "NianticSpatial.NSDK.AR.Scanning") <span class="api-breadcrumbs-nav">←</span>[ARScanQualityClassifier](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanQualityClassifier/ "NianticSpatial.NSDK.AR.Scanning.ARScanQualityClassifier") 

</div>

<div class="api-title">

#  GetResult

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name">[ScanQualityResult](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanQualityResult/ "Scan Quality Result.")</span><span class="ctoken plain"> </span><span class="ctoken class-name">GetResult</span><span class="ctoken punctuation">(</span><span class="ctoken class-name keyword">string</span><span class="ctoken plain"> </span><span class="ctoken class-name">scanPath</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns a ScanQualityResult of current quality compute,\
Scores are in range of \[0, 1.0\]. Higher values means high scan quality.\
Categories are within ScanQualityCategory.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A ScanQualityResult with list of Scores and CategoriesFailRequirement.

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
<td><span id="external parameter-scanpath"></span><span class="ctoken-line"><span class="ctoken class-name">scanPath</span></span></td>
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
