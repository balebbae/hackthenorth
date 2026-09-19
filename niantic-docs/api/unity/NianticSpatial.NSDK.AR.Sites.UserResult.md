---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.UserResult/
title: UserResult
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

#  UserResult

<div class="api-package">

Result of a user information request.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken keyword">struct</span><span class="ctoken plain"> </span><span class="ctoken class-name">UserResult</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span>

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
<td><span id="property-error"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Error</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesError/" title="Error codes for Sites API operations.">SitesError</a></span></span></td>
<td><div class="ctoken comment">
The error code if the request failed.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-status"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Status</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesRequestStatus/" title="Status of a Sites API request.">SitesRequestStatus</a></span></span></td>
<td><div class="ctoken comment">
The status of the request.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-user"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">User</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.nullable-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Nullable</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.UserInfo/" title="Information about a user.">UserInfo</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
The user information if the request succeeded, or null if failed.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
