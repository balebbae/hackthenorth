---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackImageUtility.bitmapToYuvImage/
title: bitmapToYuvImage
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.playback](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback/ "com.nianticspatial.nsdk.playback") <span class="api-breadcrumbs-nav">←</span>[PlaybackImageUtility](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackImageUtility/ "com.nianticspatial.nsdk.playback.PlaybackImageUtility") 

</div>

<div class="api-title">

#  bitmapToYuvImage

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken class-name"><a href="https://developer.android.com/reference/androidx/annotation/RequiresApi" target="_blank" rel="noopener noreferrer" title="Opens an external reference">RequiresApi</a></span><span class="ctoken punctuation">(</span><span class="ctoken class-name">Build</span><span class="ctoken punctuation">.</span><span class="ctoken class-name">VERSION_CODES</span><span class="ctoken punctuation">.</span><span class="ctoken class-name">M</span><span class="ctoken punctuation">)</span><span class="ctoken plain"> </span><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">bitmapToYuvImage</span><span class="ctoken punctuation">(</span><span class="ctoken plain">bitmap</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Bitmap" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bitmap</a></span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">YuvImageHandler</span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Converts `bitmap` to a YUV_420_888 `Image`. Returns null if conversion fails.\
Caller must call `YuvImageHandler.close` after use (e.g. after sendFrame returns).

</div>

------------------------------------------------------------------------

</div>

</div>
