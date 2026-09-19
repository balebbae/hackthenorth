---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKView.method-getCamera/
title: getCamera
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKView](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKView/ "NSDKView") 

</div>

<div class="api-title">

#  getCamera

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">getCamera</span><span class="ctoken plain">() -\> </span><span class="ctoken class-name">[NSDKCamera](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKCamera/ "Single camera API for both modes. Holds either **ARCamera** (live) or **PlaybackCamera** (playback)...")</span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Returns a unified camera (NSDKCamera) for the current frame when one is available.\
In live mode uses the current ARFrame's camera; in playback uses the current playback frame's camera.\
Returns nil if no frame is ready. Use this so callers do not need to branch on session mode for view/projection/viewport.

</div>

------------------------------------------------------------------------

</div>

</div>
