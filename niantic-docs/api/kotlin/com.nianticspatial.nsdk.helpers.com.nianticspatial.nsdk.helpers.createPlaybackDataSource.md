---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers.com.nianticspatial.nsdk.helpers.createPlaybackDataSource/
title: createPlaybackDataSource
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.helpers](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers/ "com.nianticspatial.nsdk.helpers") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.helpers](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.helpers/#property-com.nianticspatial.nsdk.helpers "com.nianticspatial.nsdk.helpers.com.nianticspatial.nsdk.helpers") 

</div>

<div class="api-title">

#  createPlaybackDataSource

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">createPlaybackDataSource</span><span class="ctoken punctuation">(</span><span class="ctoken plain"> </span><span class="ctoken plain">frameProvider</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span><span class="ctoken plain"> </span><span class="ctoken plain">-\></span><span class="ctoken plain"> </span><span class="ctoken class-name">[PlaybackFrame](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackFrame/ "One frame of playback: metadata, camera representation, optional image and depth....")</span><span class="ctoken plain">?</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken plain">orientationProvider</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span><span class="ctoken plain"> </span><span class="ctoken plain">-\></span><span class="ctoken plain"> </span><span class="ctoken class-name">[Orientation](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Orientation/ "Device orientation when capturing camera frames....")</span><span class="ctoken plain"> </span><span class="ctoken plain">=</span><span class="ctoken plain"> </span><span class="ctoken punctuation">{</span><span class="ctoken plain"> </span><span class="ctoken class-name">[Orientation](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Orientation/ "Device orientation when capturing camera frames....")</span><span class="ctoken punctuation">.</span><span class="ctoken class-name">PORTRAIT</span><span class="ctoken plain"> </span><span class="ctoken punctuation">}</span><span class="ctoken plain"> </span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[NsdkSessionDataSource](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkSessionDataSource/ "Provides synchronous, pull-based access to the latest available sensor data...")</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Creates a playback data source that converts dataset bitmaps to YUV on a background thread.

\

The returned object implements `DefaultLifecycleObserver` — add it to your lifecycle\
for cleanup on destroy.

</div>

------------------------------------------------------------------------

</div>

</div>
