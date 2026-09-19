---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKScanningSession.method-recordingInfo/
title: recordingInfo
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

#  recordingInfo

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">recordingInfo</span><span class="ctoken plain">() -\> </span><span class="ctoken class-name">[NSDKScanningSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKScanningSession/ "A session for 3D scanning and visualization with Combine publisher support....")</span><span class="ctoken plain">.</span><span class="ctoken class-name">[RecordingInfo](https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKScanningSession.struct-RecordingInfo/ "Information about the recording generated during scanning.")</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns information about the current recording.\
Call this method **before** `saveCurrentScan()` to ensure that the recording\
contains frames to save. Otherwise, the save operation may fail.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A `RecordingInfo` object containing details about the current recording.

</div>

<div class="theme-admonition theme-admonition-info admonition_xJq3 alert alert--info">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)</span>Notice

</div>

<div class="admonitionContent_BuS1">

Note: Make sure to call this method before `saveCurrentScan()` if you plan to

</div>

</div>

------------------------------------------------------------------------

</div>

</div>
