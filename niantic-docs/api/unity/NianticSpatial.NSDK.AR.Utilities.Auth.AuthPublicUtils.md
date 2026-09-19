---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Auth.AuthPublicUtils/
title: AuthPublicUtils
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Utilities.Auth](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Auth/ "NianticSpatial.NSDK.AR.Utilities.Auth") 

</div>

<div class="api-title">

#  AuthPublicUtils

<div class="api-package">

Static class for auth-related utility functions that are shared as part of the public API

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">AuthPublicUtils</span></span>

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
<td><span id="method-expiresat"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Auth.AuthPublicUtils.ExpiresAt/" title="Get the expiry time of a JWT token in seconds.">ExpiresAt</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
Get the expiry time of a JWT token in seconds.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-isemptyorexpiring"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Auth.AuthPublicUtils.IsEmptyOrExpiring/" title="Is the token expired, about to expire, or not set?">IsEmptyOrExpiring</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Is the token expired, about to expire, or not set?
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-logtoken"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Auth.AuthPublicUtils.LogToken/" title="Log details for a single Jwt token....">LogToken</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment">
Log details for a single Jwt token.<br />
Shows the context, token tail (truncated to the last four elements), and time left in seconds.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
