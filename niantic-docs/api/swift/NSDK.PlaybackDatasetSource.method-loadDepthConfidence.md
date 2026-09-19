---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackDatasetSource.method-loadDepthConfidence/
title: loadDepthConfidence
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[PlaybackDatasetSource](https://www.nianticspatial.com/docs/api/swift/NSDK.interface-PlaybackDatasetSource/ "PlaybackDatasetSource") 

</div>

<div class="api-title">

#  loadDepthConfidence

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">loadDepthConfidence</span><span class="ctoken plain">(</span><span class="ctoken plain">confidenceFileName</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">) -\> </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//foundation/data" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Data</a></span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Loads depth confidence data from the data source.\
This method is called on-demand when confidence data is requested.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The confidence data as `Data`, or `nil` if loading fails or confidence data is not available

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
<td><span id="external parameter-confidencefilename"></span><span class="ctoken-line"><span class="ctoken class-name">confidenceFileName</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span></span></td>
<td><div class="ctoken comment">
The filename of the confidence data file (e.g., "confidence_00000000.bin")
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
