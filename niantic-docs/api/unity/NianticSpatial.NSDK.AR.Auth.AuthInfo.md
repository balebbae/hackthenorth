---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Auth.AuthInfo/
title: AuthInfo
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

#  AuthInfo

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken keyword">struct</span><span class="ctoken plain"> </span><span class="ctoken class-name">AuthInfo</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Authentication information containing token claims. Contains parsed JWT claims including token string, expiration, user information, and other standard JWT fields.

------------------------------------------------------------------------

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

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
<td><span id="property-audience"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Audience</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
Audience claim.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-email"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Email</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
Email claim.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-expirationtime"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">ExpirationTime</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
Expiration time (seconds since epoch).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-issuedattime"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">IssuedAtTime</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
Issued at time (seconds since epoch).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-issuer"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Issuer</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
Issuer claim.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-name"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Name</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
Name claim.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-subject"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Subject</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
Subject claim.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-token"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Token</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
Raw JWT token string; may be empty.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-userid"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">UserId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
User ID claim.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
