---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Auth.AuthPublicUtils.IsEmptyOrExpiring/
title: IsEmptyOrExpiring
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Utilities.Auth](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Auth/ "NianticSpatial.NSDK.AR.Utilities.Auth") <span class="api-breadcrumbs-nav">←</span>[AuthPublicUtils](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Auth.AuthPublicUtils/ "NianticSpatial.NSDK.AR.Utilities.Auth.AuthPublicUtils") 

</div>

<div class="api-title">

#  IsEmptyOrExpiring

<div class="api-package">

Is the token expired, about to expire, or not set?

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">bool</span><span class="ctoken plain"> </span><span class="ctoken class-name">IsEmptyOrExpiring</span><span class="ctoken punctuation">(</span><span class="ctoken class-name keyword">string</span><span class="ctoken plain"> </span><span class="ctoken class-name">token</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">int</span><span class="ctoken plain"> </span><span class="ctoken class-name">minTimeLeftSeconds</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Is the token expired, about to expire, or not set?

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

true if empty, expired, or expiring

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
<td><span id="external parameter-token"></span><span class="ctoken-line"><span class="ctoken class-name">token</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
the token
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-mintimeleftseconds"></span><span class="ctoken-line"><span class="ctoken class-name">minTimeLeftSeconds</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
minimum time left to qualify as not expiring
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
