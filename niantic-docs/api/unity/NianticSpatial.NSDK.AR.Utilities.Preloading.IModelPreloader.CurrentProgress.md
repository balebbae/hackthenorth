---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Preloading.IModelPreloader.CurrentProgress/
title: CurrentProgress
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Utilities.Preloading](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Preloading/ "NianticSpatial.NSDK.AR.Utilities.Preloading") <span class="api-breadcrumbs-nav">←</span>[IModelPreloader](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Preloading.IModelPreloader/ "NianticSpatial.NSDK.AR.Utilities.Preloading.IModelPreloader") 

</div>

<div class="api-title">

#  CurrentProgress

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name">[PreloaderStatusCode](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Preloading.PreloaderStatusCode/ "Return status codes for the model preloader")</span><span class="ctoken plain"> </span><span class="ctoken class-name">CurrentProgress</span><span class="ctoken punctuation">(</span><span class="ctoken class-name">[DepthMode](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Preloading.DepthMode/ "The NSDK depth model to use.")</span><span class="ctoken plain"> </span><span class="ctoken class-name">depthMode</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">float</span><span class="ctoken plain"> </span><span class="ctoken class-name">progress</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Read the current status of a mode file request, if a request was previously made. The result of\
DownloadModel is asynchronous, so the caller must poll CurrentProgress\
for the status of the request to ensure that the HTTP request completed successfully.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

Returns a PreloaderStatusCode indicating the status of the request.

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
<td><span id="external parameter-depthmode"></span><span class="ctoken-line"><span class="ctoken class-name">depthMode</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Preloading.DepthMode/" title="The NSDK depth model to use.">DepthMode</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-progress"></span><span class="ctoken-line"><span class="ctoken class-name">progress</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
A value in the range of [0.0, 1.0] representing how much progress has been made downloading the model<br />
file of the specified feature mode. A progress of 1.0 means the file is present in the cache. The download<br />
progress value is server dependent and may not always support incremental progress updates.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Overload 1<a href="#overload-1" class="hash-link" aria-label="Direct link to Overload 1" title="Direct link to Overload 1">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name">[PreloaderStatusCode](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Preloading.PreloaderStatusCode/ "Return status codes for the model preloader")</span><span class="ctoken plain"> </span><span class="ctoken class-name">CurrentProgress</span><span class="ctoken punctuation">(</span><span class="ctoken class-name">[SceneSegmentationMode](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Preloading.SceneSegmentationMode/ "The NSDK semantic segmentation model to use.")</span><span class="ctoken plain"> </span><span class="ctoken class-name">sceneSegmentationMode</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">float</span><span class="ctoken plain"> </span><span class="ctoken class-name">progress</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary-1" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Read the current status of a mode file request, if a request was previously made. The result of\
DownloadModel is asynchronous, so the caller must poll CurrentProgress\
for the status of the request to ensure that the HTTP request completed successfully.

</div>

#### Returns<a href="#returns-1" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

Returns a PreloaderStatusCode indicating the status of the request.

</div>

### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

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
<td><span id="external parameter-depthmode"></span><span class="ctoken-line"><span class="ctoken class-name">depthMode</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Preloading.DepthMode/" title="The NSDK depth model to use.">DepthMode</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-progress"></span><span class="ctoken-line"><span class="ctoken class-name">progress</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
A value in the range of [0.0, 1.0] representing how much progress has been made downloading the model<br />
file of the specified feature mode. A progress of 1.0 means the file is present in the cache. The download<br />
progress value is server dependent and may not always support incremental progress updates.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Overload 2<a href="#overload-2" class="hash-link" aria-label="Direct link to Overload 2" title="Direct link to Overload 2">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name">[PreloaderStatusCode](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Preloading.PreloaderStatusCode/ "Return status codes for the model preloader")</span><span class="ctoken plain"> </span><span class="ctoken class-name">CurrentProgress</span><span class="ctoken punctuation">(</span><span class="ctoken class-name">[ScanningSQCMode](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Preloading.ScanningSQCMode/ "The NSDK Scanning SQC model to use.")</span><span class="ctoken plain"> </span><span class="ctoken class-name">scanningSQCMode</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">float</span><span class="ctoken plain"> </span><span class="ctoken class-name">progress</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary-2" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Read the current status of a mode file request, if a request was previously made. The result of\
DownloadModel is asynchronous, so the caller must poll CurrentProgress\
for the status of the request to ensure that the HTTP request completed successfully.

</div>

#### Returns<a href="#returns-2" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

Returns a PreloaderStatusCode indicating the status of the request.

</div>

### Parameters<a href="#parameters-2" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

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
<td><span id="external parameter-depthmode"></span><span class="ctoken-line"><span class="ctoken class-name">depthMode</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Preloading.DepthMode/" title="The NSDK depth model to use.">DepthMode</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-progress"></span><span class="ctoken-line"><span class="ctoken class-name">progress</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
A value in the range of [0.0, 1.0] representing how much progress has been made downloading the model<br />
file of the specified feature mode. A progress of 1.0 means the file is present in the cache. The download<br />
progress value is server dependent and may not always support incremental progress updates.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
