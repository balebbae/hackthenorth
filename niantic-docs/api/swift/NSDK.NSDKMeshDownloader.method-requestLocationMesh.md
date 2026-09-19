---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKMeshDownloader.method-requestLocationMesh/
title: requestLocationMesh
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKMeshDownloader](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKMeshDownloader/ "NSDKMeshDownloader") 

</div>

<div class="api-title">

#  requestLocationMesh

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">requestLocationMesh</span><span class="ctoken plain">(</span><span class="ctoken plain">payload</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">, </span><span class="ctoken plain">getTexture</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain">, </span><span class="ctoken plain">maxDownloadSize</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/uint32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UInt32</a></span><span class="ctoken plain">? = nil, </span><span class="ctoken plain">timeout</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/timeinterval" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TimeInterval</a></span><span class="ctoken plain"> = 300.0, </span><span class="ctoken plain">pollingInterval</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/timeinterval" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TimeInterval</a></span><span class="ctoken plain"> = 0.5) </span><span class="ctoken keyword">async</span><span class="ctoken plain"> </span><span class="ctoken keyword">throws</span><span class="ctoken plain"> -\> </span><span class="ctoken class-name">[MeshDownloaderResults](https://www.nianticspatial.com/docs/api/swift/NSDK.class-MeshDownloaderResults/ "Contains the downloaded mesh geometry data for a VPS location....")</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Requests all meshes for a VPS location identified by an anchor payload.\
Initiates a network request to download all meshes associated with the given VPS location.\
The call suspends until the operation completes successfully, fails, or times out.\
The method automatically polls for completion and returns a `MeshDownloaderResults` object\
containing the downloaded geometry data.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A `MeshDownloaderResults` object containing the downloaded mesh data.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- \- `CancellationError` if the Task running this function was cancelled. - `TimeoutError` if the function timed out before it could complete execution. - `NSDKError` if there was an error with one or more of the arguments. Check NSDK's C logs for more information.

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
<td><span id="external parameter-payload"></span><span class="ctoken-line"><span class="ctoken class-name">payload</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span></span></td>
<td><div class="ctoken comment">
The VPS anchor payload string identifying the target location. This can be<br />
obtained from the <code>blob</code> field in Geospatial Browser, or the <code>default_anchor</code> field of<br />
the VPS Coverage API’s <code>LocalizationTarget</code>.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-gettexture"></span><span class="ctoken-line"><span class="ctoken class-name">getTexture</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
If <code>true</code>, the response includes mesh texture data; if <code>false</code>, the image and<br />
UV buffers are empty. Instead, a color field (rgb) will be provided for each vertex.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-maxdownloadsize"></span><span class="ctoken-line"><span class="ctoken class-name">maxDownloadSize</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/uint32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UInt32</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
The optional maximum size (in kilobytes) for meshes to be downloaded.<br />
Meshes larger than this limit are skipped. A value of <code>nil</code> means no size limit.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-timeout"></span><span class="ctoken-line"><span class="ctoken class-name">timeout</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/timeinterval" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TimeInterval</a></span></span></td>
<td><div class="ctoken comment">
The maximum duration to wait for completion (default: 300 seconds).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-pollinginterval"></span><span class="ctoken-line"><span class="ctoken class-name">pollingInterval</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/timeinterval" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TimeInterval</a></span></span></td>
<td><div class="ctoken comment">
The interval between status checks (default: 0.5 seconds).
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
