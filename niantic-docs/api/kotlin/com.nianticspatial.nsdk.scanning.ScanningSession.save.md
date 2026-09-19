---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession.save/
title: save
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.scanning](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning/ "com.nianticspatial.nsdk.scanning") <span class="api-breadcrumbs-nav">←</span>[ScanningSession](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession/ "com.nianticspatial.nsdk.scanning.ScanningSession") 

</div>

<div class="api-title">

#  save

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">suspend</span><span class="ctoken plain"> </span><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">save</span><span class="ctoken punctuation">(</span><span class="ctoken plain"> </span><span class="ctoken plain">timeoutMillis</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Long</a></span><span class="ctoken plain"> </span><span class="ctoken plain">=</span><span class="ctoken plain"> </span><span class="ctoken class-name">TIMEOUT_MS</span><span class="ctoken plain"> </span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[AsyncResult](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AsyncResult/ "Represents the final result of a completed asynchronous operation, which can either be...")</span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">[ScanSaveInfo](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ScanSaveInfo/ "Information about a saved scan....")</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">[ScanSaveError](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ScanSaveError/ "Error codes that can be returned when a scan fails to save.")</span><span class="ctoken punctuation">\></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Asynchronously saves the current scan and polls until the operation is complete.

\

This function initiates the save operation and then suspends until the save\
process finishes, either with a success, a failure, or a timeout.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

An `AsyncResult` which will be either `AsyncResult.Success` containing the final `ScanSaveInfo` on success, `AsyncResult.Error` detailing the failure reason, or `AsyncResult.Timeout` indicating a timeout in the scanning process

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `ArdkInvalidOperationStatusException` — if there were no frames to save. Call `getRecordingInfo` to check there are frames before calling this function.

------------------------------------------------------------------------

</div>

</div>
