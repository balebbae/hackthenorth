---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Auth.AuthClient.SetAccessToken/
title: SetAccessToken
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Auth](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Auth/ "NianticSpatial.NSDK.AR.Auth") <span class="api-breadcrumbs-nav">←</span>[AuthClient](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Auth.AuthClient/ "NianticSpatial.NSDK.AR.Auth.AuthClient") 

</div>

<div class="api-title">

#  SetAccessToken

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">void</span><span class="ctoken plain"> </span><span class="ctoken class-name">SetAccessToken</span><span class="ctoken punctuation">(</span><span class="ctoken class-name keyword">string</span><span class="ctoken plain"> </span><span class="ctoken class-name">accessToken</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Sets the access token for authentication with NSDK services.\
This token will be used for API Gateway requests instead of the API key.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `InvalidOperationException` — Thrown if the NSDK context is not initialized or the operation fails.

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
<td><span id="external parameter-accesstoken"></span><span class="ctoken-line"><span class="ctoken class-name">accessToken</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
The access token string for authentication.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
