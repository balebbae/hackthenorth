---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKFrameData.method-withUnsafeCFrameData/
title: withUnsafeCFrameData
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKFrameData](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKFrameData/ "NSDKFrameData") 

</div>

<div class="api-title">

#  withUnsafeCFrameData

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">withUnsafeCFrameData</span><span class="ctoken plain">\<</span><span class="ctoken plain">T</span><span class="ctoken plain">\>(</span><span class="ctoken plain">\_</span><span class="ctoken plain"> </span><span class="ctoken plain">body</span><span class="ctoken plain">: (</span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/unsafepointer" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UnsafePointer</a></span><span class="ctoken plain">\<</span><span class="ctoken class-name">ARDK_FrameData</span><span class="ctoken plain">\>) </span><span class="ctoken keyword">throws</span><span class="ctoken plain"> -\> </span><span class="ctoken class-name">T</span><span class="ctoken plain">) </span><span class="ctoken keyword">rethrows</span><span class="ctoken plain"> -\> </span><span class="ctoken class-name">T</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Calls the given closure with a pointer to a valid `ARDK_FrameData` whose\
camera and depth frame arrays are backed by storage that remains valid for the\
duration of the call

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
<td><span id="external parameter-body"></span><span class="ctoken-line"><span class="ctoken class-name">body</span></span></td>
<td><span class="ctoken-line"><span class="ctoken plain"> (</span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/unsafepointer" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UnsafePointer</a></span><span class="ctoken plain">&lt;</span><span class="ctoken class-name">ARDK_FrameData</span><span class="ctoken plain">&gt;) </span><span class="ctoken keyword">throws</span><span class="ctoken plain"> -&gt; </span><span class="ctoken class-name">T</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
