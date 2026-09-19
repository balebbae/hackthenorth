---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKLogCallback.method-onLog/
title: onLog
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKLogCallback](https://www.nianticspatial.com/docs/api/swift/NSDK.interface-NSDKLogCallback/ "NSDKLogCallback") 

</div>

<div class="api-title">

#  onLog

<div class="api-package">

Called when NSDK generates a log message.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">onLog</span><span class="ctoken plain">(</span><span class="ctoken plain">level</span><span class="ctoken plain">: </span><span class="ctoken class-name">[NSDKLogLevel](https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKLogLevel/ "Defines the available logging levels for NSDK....")</span><span class="ctoken plain">, </span><span class="ctoken plain">message</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">, </span><span class="ctoken plain">fileName</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">?, </span><span class="ctoken plain">fileLine</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span><span class="ctoken plain">, </span><span class="ctoken plain">funcName</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">?)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Called when NSDK generates a log message.

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
<td><span id="external parameter-level"></span><span class="ctoken-line"><span class="ctoken class-name">level</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKLogLevel/" title="Defines the available logging levels for NSDK....">NSDKLogLevel</a></span></span></td>
<td><div class="ctoken comment">
The severity level of the log message
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-message"></span><span class="ctoken-line"><span class="ctoken class-name">message</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span></span></td>
<td><div class="ctoken comment">
The log message content
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-filename"></span><span class="ctoken-line"><span class="ctoken class-name">fileName</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Optional source file name where the log was generated
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-fileline"></span><span class="ctoken-line"><span class="ctoken class-name">fileLine</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
Line number in the source file
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-funcname"></span><span class="ctoken-line"><span class="ctoken class-name">funcName</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Optional function name where the log was generated
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
