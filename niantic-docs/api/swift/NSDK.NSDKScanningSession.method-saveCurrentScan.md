---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKScanningSession.method-saveCurrentScan/
title: saveCurrentScan
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

#  saveCurrentScan

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">saveCurrentScan</span><span class="ctoken plain">(</span><span class="ctoken plain">timeout</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/double" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Double</a></span><span class="ctoken plain"> = 10.0, </span><span class="ctoken plain">pollingInterval</span><span class="ctoken plain">: </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/timeinterval" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TimeInterval</a></span><span class="ctoken plain"> = 0.1) </span><span class="ctoken keyword">async</span><span class="ctoken plain"> </span><span class="ctoken keyword">throws</span><span class="ctoken plain"> -\> </span><span class="ctoken class-name">[NSDKScanningSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKScanningSession/ "A session for 3D scanning and visualization with Combine publisher support....")</span><span class="ctoken plain">.</span><span class="ctoken class-name">[SaveInfo](https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKScanningSession.struct-SaveInfo/ "Information about a save operation for a scan.")</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Stops recording and asynchronously saves the recording to the configured path.\
Calling this function will stop the active recording, but `stop` must still be called\
afterward to completely shut down this session.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

Information about the saved scan, including it's id and file location.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- \- `CancellationError` if the Task running this function was cancelled. - `TimeoutError` if the function timed out before it could complete execution. - `NSDKScanningSession.SaveError` if there was an error specific to the save operation. - SeeAlso: - `stop` - `configure(with:)`

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
<td><span id="external parameter-timeout"></span><span class="ctoken-line"><span class="ctoken class-name">timeout</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/double" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Double</a></span></span></td>
<td><div class="ctoken comment">
The maximum duration in seconds to wait for the save operation<br />
(default is 10 seconds).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-pollinginterval"></span><span class="ctoken-line"><span class="ctoken class-name">pollingInterval</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//foundation/timeinterval" target="_blank" rel="noopener noreferrer" title="Opens an external reference">TimeInterval</a></span></span></td>
<td><div class="ctoken comment">
The interval in seconds to wait between progress checks<br />
(default is 0.1 seconds)
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
