---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKAsyncState/
title: NSDKAsyncState
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") 

</div>

<div class="api-title">

#  NSDKAsyncState

<div class="api-package">

Reports the state of an asynchronous NSDK operation.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">enum</span><span class="ctoken plain"> </span><span class="ctoken class-name">NSDKAsyncState</span><span class="ctoken plain">\<</span><span class="ctoken plain">Value</span><span class="ctoken plain">, </span><span class="ctoken plain">Error</span><span class="ctoken plain">\> </span><span class="ctoken keyword">where</span><span class="ctoken plain"> </span><span class="ctoken class-name">Error</span><span class="ctoken plain"> : </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/error" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Error</a></span></span>

------------------------------------------------------------------------

## Cases<a href="#cases" class="hash-link" aria-label="Direct link to Cases" title="Direct link to Cases">​</a>

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
<td><span id="case-failure"></span><span class="ctoken-line"><span class="ctoken keyword">case</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKAsyncState/#case-failure" title="The asynchronous operation has failed with an error.">failure</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/error" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Error</a></span><span class="ctoken plain">)</span></span></td>
<td><div class="ctoken comment">
The asynchronous operation has failed with an error.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-inprogress"></span><span class="ctoken-line"><span class="ctoken keyword">case</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKAsyncState/#case-inprogress" title="The asynchronous operation is currently in progress....">inProgress</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Value</span><span class="ctoken plain">?)</span></span></td>
<td><div class="ctoken comment">
The asynchronous operation is currently in progress.<br />
The associated value may contain a partial result if available.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-notready"></span><span class="ctoken-line"><span class="ctoken keyword">case</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKAsyncState/#case-notready" title="Deprecated – use `inProgress` instead.">notReady</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKAsyncState/#case-notready" title="Deprecated – use `inProgress` instead.">notReady</a></span></span></td>
<td><div class="ctoken comment">
Deprecated – use <code>inProgress</code> instead.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-success"></span><span class="ctoken-line"><span class="ctoken keyword">case</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKAsyncState/#case-success" title="The asynchronous operation has completed successfully with a result.">success</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Value</span><span class="ctoken plain">)</span></span></td>
<td><div class="ctoken comment">
The asynchronous operation has completed successfully with a result.
</div></td>
</tr>
</tbody>
</table>

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
<td><span id="property-isfinished"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">isFinished</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
Indicates whether the asynchronous operation has finished
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
