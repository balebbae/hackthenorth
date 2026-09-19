---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackBackgroundView/
title: PlaybackBackgroundView
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.playback](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback/ "com.nianticspatial.nsdk.playback") 

</div>

<div class="api-title">

#  PlaybackBackgroundView

<div class="api-extends">

↳ extends ImageView

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">PlaybackBackgroundView</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

A view that displays the current playback frame image as the background. Place this view behind your 3D/GL surface when in playback mode and call \[setPlaybackFrame\] whenever a new \[PlaybackFrame\] is delivered so the recorded camera image is shown. Orientation is corrected so that the image (which may be stored in sensor/landscape layout) is rotated to match the current device orientation using \[ImageMath.displayTransform\]. Use with \[PlaybackSession\] and a frame listener: when the session delivers a frame, build \[FrameData\] for NSDK and call \[setPlaybackFrame\] to update this view.

------------------------------------------------------------------------

## Functions<a href="#functions" class="hash-link" aria-label="Direct link to Functions" title="Direct link to Functions">​</a>

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
<td><span id="function-onsizechanged"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackBackgroundView.onSizeChanged/" title="Browse to onSizeChanged">onSizeChanged</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-setplaybackframe"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackBackgroundView.setPlaybackFrame/" title="Updates the background image from the given playback frame....">setPlaybackFrame</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Updates the background image from the given playback frame.<br />
Call on the main thread when [PlaybackSession] delivers a new frame.<br />
If [frame] is null or [frame.image] is null, the view is cleared.<br />
Applies a display transform so the image orientation matches the current device orientation.<br />
Uses frame metadata [screenOrientation] when present, with fallback to resolution-based inference.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
