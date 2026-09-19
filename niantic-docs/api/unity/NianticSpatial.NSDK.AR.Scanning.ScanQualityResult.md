---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanQualityResult/
title: ScanQualityResult
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Scanning](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning/ "NianticSpatial.NSDK.AR.Scanning") 

</div>

<div class="api-title">

#  ScanQualityResult

<div class="api-package">

Scan Quality Result.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">ScanQualityResult</span></span>

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
<td><span id="property-rejectionreasons"></span><span class="ctoken-line"><span class="ctoken class-name">RejectionReasons</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">List</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanningSqcScores/" title="This struct is used by publicly and internally....">ScanningSqcScores</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Returns a list of problems with the scan that may contribute to it receiving a lower<br />
scan quality score. This list will be empty for high-quality scans.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-scanqualityscore"></span><span class="ctoken-line"><span class="ctoken class-name">ScanQualityScore</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
An overall score of the scan's quality. Range is 0-1, higher is better.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
