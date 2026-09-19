---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKMeshDownloader/
title: NSDKMeshDownloader
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") 

</div>

<div class="api-title">

#  NSDKMeshDownloader

<div class="api-package">

A session-scoped utility for downloading mesh geometry associated with VPS locations.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">NSDKMeshDownloader</span></span>

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
<td><span id="method-requestlocationmesh"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMeshDownloader.method-requestLocationMesh/" title="Requests all meshes for a VPS location identified by an anchor payload....">requestLocationMesh</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-MeshDownloaderResults/" title="Contains the downloaded mesh geometry data for a VPS location....">MeshDownloaderResults</a></span></span></td>
<td><div class="ctoken comment">
Requests all meshes for a VPS location identified by an anchor payload.<br />
Initiates a network request to download all meshes associated with the given VPS location.<br />
The call suspends until the operation completes successfully, fails, or times out.<br />
The method automatically polls for completion and returns a <code>MeshDownloaderResults</code> object<br />
containing the downloaded geometry data.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
