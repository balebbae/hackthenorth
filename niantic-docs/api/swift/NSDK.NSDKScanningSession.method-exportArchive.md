---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKScanningSession.method-exportArchive/
title: exportArchive
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKScanningSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKScanningSession/ "NSDKScanningSession") 

</div>

<div class="api-title">

#  exportArchive

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">exportArchive</span><span class="ctoken plain">(</span><span class="ctoken plain">metadata</span><span class="ctoken plain">: \[</span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain"> : </span><span class="ctoken keyword">Any</span><span class="ctoken plain">\]? = nil, </span><span class="ctoken plain">exportAsVideo</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain"> = true, </span><span class="ctoken plain">exportResolution</span><span class="ctoken plain">: </span><span class="ctoken class-name">[ExportResolution](https://www.nianticspatial.com/docs/api/swift/NSDK.enum-ExportResolution/ "Resolution option for exported scan images....")</span><span class="ctoken plain"> = .high) </span><span class="ctoken keyword">throws</span><span class="ctoken plain"> -\> </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Exports the scan data as an archive file.\
This method processes the saved scan data and exports it to a standard archive format\
that can be used with external 3D processing tools or Niantic's VPS map.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The path of the archive file, if the export was successful, `nil` if otherwise.\
Export failure indicates something was wrong with the saved scan.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- \- `NSDKError.invalidOperation` if the scanning session did not have a saved scan to export.

<div class="theme-admonition theme-admonition-info admonition_xJq3 alert alert--info">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)</span>Notice

</div>

<div class="admonitionContent_BuS1">

Note: This function is blocking and may take a while to execute. See

</div>

</div>

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
<td><span id="external parameter-metadata"></span><span class="ctoken-line"><span class="ctoken class-name">metadata</span></span></td>
<td><span class="ctoken-line"><span class="ctoken plain"> [</span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain"> : </span><span class="ctoken plain">]?</span></span></td>
<td><div class="ctoken comment">
Metadata dictionary to include with the export. Can be left empty.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-exportasvideo"></span><span class="ctoken-line"><span class="ctoken class-name">exportAsVideo</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
If true, the RGB frames in the scan will be exported as an<br />
.mp4 video. If false, they will be individual image files.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-exportresolution"></span><span class="ctoken-line"><span class="ctoken class-name">exportResolution</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-ExportResolution/" title="Resolution option for exported scan images....">ExportResolution</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
