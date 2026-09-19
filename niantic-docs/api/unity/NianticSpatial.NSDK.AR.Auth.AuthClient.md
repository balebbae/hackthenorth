---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Auth.AuthClient/
title: AuthClient
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Auth](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Auth/ "NianticSpatial.NSDK.AR.Auth") 

</div>

<div class="api-title">

#  AuthClient

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">AuthClient</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Static client for interacting with the Auth Manager service. Provides methods to manage authentication tokens and check authorization status.

------------------------------------------------------------------------

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

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
<td><span id="method-getaccessauthinfo"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Auth.AuthClient.GetAccessAuthInfo/" title="Gets access token authentication information....">GetAccessAuthInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Auth.AuthInfo/" title="Authentication information containing token claims....">AuthInfo</a></span></span></td>
<td><div class="ctoken comment">
Gets access token authentication information.<br />
Returns authentication information containing information about the current access token.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getrefreshauthinfo"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Auth.AuthClient.GetRefreshAuthInfo/" title="Gets refresh token authentication information....">GetRefreshAuthInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Auth.AuthInfo/" title="Authentication information containing token claims....">AuthInfo</a></span></span></td>
<td><div class="ctoken comment">
Gets refresh token authentication information.<br />
Returns authentication information containing information about the current refresh token.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-isauthorized"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Auth.AuthClient.IsAuthorized/" title="Checks if auth tokens are valid and ready for use....">IsAuthorized</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Checks if auth tokens are valid and ready for use.<br />
Returns true if a valid, non-expired access token is available.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-setaccesstoken"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Auth.AuthClient.SetAccessToken/" title="Sets the access token for authentication with NSDK services....">SetAccessToken</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment">
Sets the access token for authentication with NSDK services.<br />
This token will be used for API Gateway requests instead of the API key.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-staticlogout"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Auth.AuthClient.StaticLogout/" title="Clears cached auth tokens from persistent storage without requiring an NSDK context....">StaticLogout</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment">
Clears cached auth tokens from persistent storage without requiring an NSDK context.<br />
This is the preferred logout path — safe to call before NSDK is initialized or after<br />
it has been destroyed. Any running session will pick up the cleared tokens on its next<br />
reconciliation cycle.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
