---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.recording.RecordingExporter/
title: RecordingExporter
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.recording](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.recording/ "com.nianticspatial.nsdk.recording") 

</div>

<div class="api-title">

#  RecordingExporter

<div class="api-extends">

↳ extends [SessionBase](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.SessionBase/ "SessionBase") 

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">RecordingExporter</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Creates a Recording Exporter instance for exporting saved scans. The Recording Exporter feature allows you to export previously saved scans in various formats with custom metadata and user data.

------------------------------------------------------------------------

## Functions<a href="#functions" class="hash-link" aria-label="Direct link to Functions" title="Direct link to Functions">​</a>

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
<td><span id="function-export"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.recording.RecordingExporter.export/" title="Asynchronously exports a scan recording....">export</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AsyncResult/" title="Represents the final result of a completed asynchronous operation, which can either be...">AsyncResult</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-nothing" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nothing</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Asynchronously exports a scan recording.<br />
This function suspends execution until the export operation is complete,<br />
has failed, or has timed out.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-exportsplitarchives"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.recording.RecordingExporter.exportSplitArchives/" title="Asynchronously exports a scan recording as multiple archive files....">exportSplitArchives</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AsyncResult/" title="Represents the final result of a completed asynchronous operation, which can either be...">AsyncResult</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Array</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken punctuation">&gt;</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-nothing" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nothing</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Asynchronously exports a scan recording as multiple archive files.<br />
This function suspends execution until the export operation is complete,<br />
has failed, or has timed out.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-ondestroy"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.recording.RecordingExporter.onDestroy/" title="Browse to onDestroy">onDestroy</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-oninit"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.recording.RecordingExporter.onInit/" title="Browse to onInit">onInit</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
