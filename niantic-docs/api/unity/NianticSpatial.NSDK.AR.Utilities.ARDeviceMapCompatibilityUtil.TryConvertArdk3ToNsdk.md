---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.ARDeviceMapCompatibilityUtil.TryConvertArdk3ToNsdk/
title: TryConvertArdk3ToNsdk
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Utilities](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities/ "NianticSpatial.NSDK.AR.Utilities") <span class="api-breadcrumbs-nav">←</span>[ARDeviceMapCompatibilityUtil](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.ARDeviceMapCompatibilityUtil/ "NianticSpatial.NSDK.AR.Utilities.ARDeviceMapCompatibilityUtil") 

</div>

<div class="api-title">

#  TryConvertArdk3ToNsdk

<div class="api-package">

Try to convert Device Map blob as ARDK 3.x Device Map

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">bool</span><span class="ctoken plain"> </span><span class="ctoken class-name">TryConvertArdk3ToNsdk</span><span class="ctoken punctuation">(</span><span class="ctoken class-name keyword">byte</span><span class="ctoken punctuation">\[</span><span class="ctoken punctuation">\]</span><span class="ctoken plain"> </span><span class="ctoken class-name">ardk3DeviceMap</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">byte</span><span class="ctoken punctuation">\[</span><span class="ctoken punctuation">\]</span><span class="ctoken plain"> </span><span class="ctoken class-name">nsdkDeviceMap</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Try to convert Device Map blob as ARDK 3.x Device Map

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

true if successfully converted into NSDK Device Map. false if failed to convert Device Map

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
<td><span id="external parameter-ardk3devicemap"></span><span class="ctoken-line"><span class="ctoken class-name">ardk3DeviceMap</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">byte</span><span class="ctoken punctuation">[</span><span class="ctoken punctuation">]</span></span></td>
<td><div class="ctoken comment">
Byte array data of serialized ARDK 3.x Device Map
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-nsdkdevicemap"></span><span class="ctoken-line"><span class="ctoken class-name">nsdkDeviceMap</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">byte</span><span class="ctoken punctuation">[</span><span class="ctoken punctuation">]</span></span></td>
<td><div class="ctoken comment">
NSDK Device Map, or null if ardk3DeviceMap is not ARDK 3.x Device Map
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
