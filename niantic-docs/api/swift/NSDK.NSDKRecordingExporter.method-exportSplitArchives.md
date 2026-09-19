---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKRecordingExporter.method-exportSplitArchives/
title: exportSplitArchives
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKRecordingExporter](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKRecordingExporter/ "NSDKRecordingExporter") 

</div>

<div class="api-title">

#  exportSplitArchives

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">exportSplitArchives</span><span class="ctoken plain">(</span><span class="ctoken plain">scanDirPath</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">, </span><span class="ctoken plain">scanId</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">, </span><span class="ctoken plain">maxFramesPerArchive</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int32</a></span><span class="ctoken plain">, </span><span class="ctoken plain">userData</span><span class="ctoken plain">: \[</span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain"> : </span><span class="ctoken keyword">Any</span><span class="ctoken plain">\] = \[:\], </span><span class="ctoken plain">exportAsVideo</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain"> = true, </span><span class="ctoken plain">exportResolution</span><span class="ctoken plain">: </span><span class="ctoken class-name">[ExportResolution](https://www.nianticspatial.com/docs/api/swift/NSDK.enum-ExportResolution/ "Resolution option for exported scan images....")</span><span class="ctoken plain"> = .high, </span><span class="ctoken plain">pollingInterval</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/timeinterval" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TimeInterval</a></span><span class="ctoken plain"> = 0.1, </span><span class="ctoken plain">timeout</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/timeinterval" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TimeInterval</a></span><span class="ctoken plain"> = 300.0, </span><span class="ctoken plain">progressCallback</span><span class="ctoken plain">: ((</span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain">) -\> </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/void" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Void</a></span><span class="ctoken plain">)? = nil) </span><span class="ctoken keyword">async</span><span class="ctoken plain"> </span><span class="ctoken keyword">throws</span><span class="ctoken plain"> -\> \[</span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">\]</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Exports a scan recording as multiple archive files asynchronously.\
Starts the export process for a scan recording and suspends until the export\
completes successfully, fails, or times out.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A list of file paths to the exported recording.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- \- `CancellationError` if the Task running this function was cancelled. - `TimeoutError` if the function timed out before it could complete execution.

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
<td><span id="external parameter-scandirpath"></span><span class="ctoken-line"><span class="ctoken class-name">scanDirPath</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-scanid"></span><span class="ctoken-line"><span class="ctoken class-name">scanId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span></span></td>
<td><div class="ctoken comment">
The unique identifier of the scan to export.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-maxframesperarchive"></span><span class="ctoken-line"><span class="ctoken class-name">maxFramesPerArchive</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int32</a></span></span></td>
<td><div class="ctoken comment">
The maximum number of frames to include in each archive of the<br />
exported recording. Must be greater than 0.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-userdata"></span><span class="ctoken-line"><span class="ctoken class-name">userData</span></span></td>
<td><span class="ctoken-line"><span class="ctoken plain"> [</span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain"> : </span><span class="ctoken plain">]</span></span></td>
<td><div class="ctoken comment">
Dictionary containing custom metadata to include in the export.
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
<td><div class="ctoken comment">
Resolution option for exported images (default: <code>ExportResolution/high</code>).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-pollinginterval"></span><span class="ctoken-line"><span class="ctoken class-name">pollingInterval</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/timeinterval" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TimeInterval</a></span></span></td>
<td><div class="ctoken comment">
Time between progress checks (default: 0.5s).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-timeout"></span><span class="ctoken-line"><span class="ctoken class-name">timeout</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/timeinterval" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TimeInterval</a></span></span></td>
<td><div class="ctoken comment">
Maximum duration to wait before failing (default: 5 minutes).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-progresscallback"></span><span class="ctoken-line"><span class="ctoken class-name">progressCallback</span></span></td>
<td><span class="ctoken-line"><span class="ctoken plain"> ((</span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain">) -&gt; </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/void" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Void</a></span><span class="ctoken plain">)?</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
