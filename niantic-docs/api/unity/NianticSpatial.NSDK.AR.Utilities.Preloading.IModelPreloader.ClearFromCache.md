---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Preloading.IModelPreloader.ClearFromCache/
title: ClearFromCache
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

#  ClearFromCache

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">bool</span><span class="ctoken plain"> </span><span class="ctoken class-name">ClearFromCache</span><span class="ctoken punctuation">(</span><span class="ctoken class-name">[DepthMode](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Preloading.DepthMode/ "The NSDK depth model to use.")</span><span class="ctoken plain"> </span><span class="ctoken class-name">depthMode</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Clears this model file from the application's cache.\
This function will fail if the download is currently in progress or if the file is not present in the\
cache.\
Calling this while the specified model is currently being loaded into a NSDK AR session is invalid\
and will result in undefined behavior.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

True if the specified feature was present in the application's cache and was successfully removed.

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
</tbody>
</table>

------------------------------------------------------------------------

## Overload 1<a href="#overload-1" class="hash-link" aria-label="Direct link to Overload 1" title="Direct link to Overload 1">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">bool</span><span class="ctoken plain"> </span><span class="ctoken class-name">ClearFromCache</span><span class="ctoken punctuation">(</span><span class="ctoken class-name">[SceneSegmentationMode](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Preloading.SceneSegmentationMode/ "The NSDK semantic segmentation model to use.")</span><span class="ctoken plain"> </span><span class="ctoken class-name">sceneSegmentationMode</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary-1" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Clears this model file from the application's cache.\
This function will fail if the download is currently in progress or if the file is not present in the\
cache.\
Calling this while the specified model is currently being loaded into a NSDK AR session is invalid\
and will result in undefined behavior.

</div>

#### Returns<a href="#returns-1" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

True if the specified feature was present in the application's cache and was successfully removed.

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
</tbody>
</table>

------------------------------------------------------------------------

## Overload 2<a href="#overload-2" class="hash-link" aria-label="Direct link to Overload 2" title="Direct link to Overload 2">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">bool</span><span class="ctoken plain"> </span><span class="ctoken class-name">ClearFromCache</span><span class="ctoken punctuation">(</span><span class="ctoken class-name">[ScanningSQCMode](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Preloading.ScanningSQCMode/ "The NSDK Scanning SQC model to use.")</span><span class="ctoken plain"> </span><span class="ctoken class-name">scanningSQCMode</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary-2" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Clears this model file from the application's cache.\
This function will fail if the download is currently in progress or if the file is not present in the\
cache.\
Calling this while the specified model is currently being loaded into a NSDK AR session is invalid\
and will result in undefined behavior.

</div>

#### Returns<a href="#returns-2" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

True if the specified feature was present in the application's cache and was successfully removed.

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
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
