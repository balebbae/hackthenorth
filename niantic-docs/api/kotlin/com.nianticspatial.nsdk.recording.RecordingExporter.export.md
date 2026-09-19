---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.recording.RecordingExporter.export/
title: export
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.recording](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.recording/ "com.nianticspatial.nsdk.recording") <span class="api-breadcrumbs-nav">←</span>[RecordingExporter](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.recording.RecordingExporter/ "com.nianticspatial.nsdk.recording.RecordingExporter") 

</div>

<div class="api-title">

#  export

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">suspend</span><span class="ctoken plain"> </span><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">export</span><span class="ctoken punctuation">(</span><span class="ctoken plain"> </span><span class="ctoken plain">scanDirPath</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">scanId</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">userData</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-map" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Map</a></span><span class="ctoken punctuation">\<</span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Any</a></span><span class="ctoken punctuation">\></span><span class="ctoken plain">?</span><span class="ctoken plain"> </span><span class="ctoken plain">=</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">null</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">exportAsVideo</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Boolean</a></span><span class="ctoken plain"> </span><span class="ctoken plain">=</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">true</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">exportResolution</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[ExportResolution](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.recording.ExportResolution/ "Resolution option for exported scan images....")</span><span class="ctoken plain"> </span><span class="ctoken plain">=</span><span class="ctoken plain"> </span><span class="ctoken class-name">[ExportResolution](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.recording.ExportResolution/ "Resolution option for exported scan images....")</span><span class="ctoken punctuation">.</span><span class="ctoken class-name">HIGH</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">timeoutMillis</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Long</a></span><span class="ctoken plain"> </span><span class="ctoken plain">=</span><span class="ctoken plain"> </span><span class="ctoken class-name">TIMEOUT_MS</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">onProgress</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">(</span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken punctuation">)</span><span class="ctoken plain"> </span><span class="ctoken plain">-\></span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Unit</a></span><span class="ctoken punctuation">)</span><span class="ctoken plain">?</span><span class="ctoken plain"> </span><span class="ctoken plain">=</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">null</span><span class="ctoken plain"> </span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[AsyncResult](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AsyncResult/ "Represents the final result of a completed asynchronous operation, which can either be...")</span><span class="ctoken punctuation">\<</span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-nothing" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nothing</a></span><span class="ctoken punctuation">\></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Asynchronously exports a scan recording.

\

This function suspends execution until the export operation is complete,\
has failed, or has timed out.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

An `AsyncResult` which will be either `AsyncResult.Success` containing the path to the exported file, or `AsyncResult.Timeout`.

</div>

------------------------------------------------------------------------

</div>

</div>
