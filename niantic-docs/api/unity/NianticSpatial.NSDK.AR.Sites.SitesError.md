---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesError/
title: SitesError
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Sites](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites/ "NianticSpatial.NSDK.AR.Sites") 

</div>

<div class="api-title">

#  SitesError

<div class="api-package">

Error codes for Sites API operations.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">enum</span><span class="ctoken plain"> </span><span class="ctoken class-name">SitesError</span></span>

------------------------------------------------------------------------

## Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

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
<td><span id="field-httpforbidden"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">HttpForbidden</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">SitesError</span></span></td>
<td><div class="ctoken comment">
HTTP 403 Forbidden - authentication failed or insufficient permissions.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-httpnotfound"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">HttpNotFound</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">SitesError</span></span></td>
<td><div class="ctoken comment">
HTTP 404 Not Found - the requested resource was not found.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-httpservererror"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">HttpServerError</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">SitesError</span></span></td>
<td><div class="ctoken comment">
HTTP 5xx Server Error - server-side error occurred.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-httptoomanyrequests"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">HttpTooManyRequests</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">SitesError</span></span></td>
<td><div class="ctoken comment">
HTTP 429 Too Many Requests - rate limit exceeded.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-invalidrequest"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">InvalidRequest</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">SitesError</span></span></td>
<td><div class="ctoken comment">
The request was invalid.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-networkerror"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">NetworkError</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">SitesError</span></span></td>
<td><div class="ctoken comment">
A network error occurred during the request.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-none"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">None</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">SitesError</span></span></td>
<td><div class="ctoken comment">
No error occurred.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-parseerror"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">ParseError</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">SitesError</span></span></td>
<td><div class="ctoken comment">
Failed to parse the response.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-unexpectederror"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">UnexpectedError</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">SitesError</span></span></td>
<td><div class="ctoken comment">
An unexpected error occurred.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
