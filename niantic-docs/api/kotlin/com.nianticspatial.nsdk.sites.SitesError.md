---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesError/
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

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.sites](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites/ "com.nianticspatial.nsdk.sites") 

</div>

<div class="api-title">

#  SitesError

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">enum</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">SitesError</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Error codes that can occur during Sites Manager operations. These errors indicate various failure conditions when communicating with the Sites Manager service.

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
<td><span id="case-http_forbidden"></span><span class="ctoken-line"><span class="ctoken class-name">HTTP_FORBIDDEN</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">HTTP_FORBIDDEN</span></span></td>
<td><div class="ctoken comment">
HTTP 403 Forbidden - authentication or authorization failed.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-http_not_found"></span><span class="ctoken-line"><span class="ctoken class-name">HTTP_NOT_FOUND</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">HTTP_NOT_FOUND</span></span></td>
<td><div class="ctoken comment">
HTTP 404 Not Found - the requested resource was not found.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-http_server_error"></span><span class="ctoken-line"><span class="ctoken class-name">HTTP_SERVER_ERROR</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">HTTP_SERVER_ERROR</span></span></td>
<td><div class="ctoken comment">
HTTP 5xx Server Error - the server encountered an error.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-http_too_many_requests"></span><span class="ctoken-line"><span class="ctoken class-name">HTTP_TOO_MANY_REQUESTS</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">HTTP_TOO_MANY_REQUESTS</span></span></td>
<td><div class="ctoken comment">
HTTP 429 Too Many Requests - rate limit exceeded.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-invalid_request"></span><span class="ctoken-line"><span class="ctoken class-name">INVALID_REQUEST</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">INVALID_REQUEST</span></span></td>
<td><div class="ctoken comment">
The request was invalid.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-network_error"></span><span class="ctoken-line"><span class="ctoken class-name">NETWORK_ERROR</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">NETWORK_ERROR</span></span></td>
<td><div class="ctoken comment">
A network error occurred during the request.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-none"></span><span class="ctoken-line"><span class="ctoken class-name">NONE</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">NONE</span></span></td>
<td><div class="ctoken comment">
No error occurred.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-parse_error"></span><span class="ctoken-line"><span class="ctoken class-name">PARSE_ERROR</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">PARSE_ERROR</span></span></td>
<td><div class="ctoken comment">
Failed to parse the server response.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-unexpected_error"></span><span class="ctoken-line"><span class="ctoken class-name">UNEXPECTED_ERROR</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">UNEXPECTED_ERROR</span></span></td>
<td><div class="ctoken comment">
An unexpected error occurred.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
