---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackBackgroundView.setPlaybackFrame/
title: setPlaybackFrame
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.playback](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback/ "com.nianticspatial.nsdk.playback") <span class="api-breadcrumbs-nav">←</span>[PlaybackBackgroundView](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackBackgroundView/ "com.nianticspatial.nsdk.playback.PlaybackBackgroundView") 

</div>

<div class="api-title">

#  setPlaybackFrame

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">setPlaybackFrame</span><span class="ctoken punctuation">(</span><span class="ctoken plain">frame</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[PlaybackFrame](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackFrame/ "One frame of playback: metadata, camera representation, optional image and depth....")</span><span class="ctoken plain">?</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Updates the background image from the given playback frame.\
Call on the main thread when `PlaybackSession` delivers a new frame.\
If `frame` is null or `frame.image` is null, the view is cleared.\
Applies a display transform so the image orientation matches the current device orientation.\
Uses frame metadata `screenOrientation` when present, with fallback to resolution-based inference.

</div>

------------------------------------------------------------------------

</div>

</div>
