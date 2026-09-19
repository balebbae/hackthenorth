---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SiteResult/
title: SiteResult
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

#  SiteResult

<div class="api-package">

Result of a site information request.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken keyword">struct</span><span class="ctoken plain"> </span><span class="ctoken class-name">SiteResult</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.valuetype?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ValueType</a></span></span>

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
<td><span id="property-sites"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Sites</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SiteInfo/" title="Information about a site.">SiteInfo</a></span><span class="ctoken punctuation">[</span><span class="ctoken punctuation">]</span></span></td>
<td><div class="ctoken comment">
The sites returned by the request.<br />
Empty array if the request failed or is in progress.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-status"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Status</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesRequestStatus/" title="Status of a Sites API request.">SitesRequestStatus</a></span></span></td>
<td><div class="ctoken comment">
The status of the request.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
