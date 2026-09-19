---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDataset.getFrameImageAtIndex/
title: getFrameImageAtIndex
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.playback](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback/ "com.nianticspatial.nsdk.playback") <span class="api-breadcrumbs-nav">←</span>[PlaybackDataset](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDataset/ "com.nianticspatial.nsdk.playback.PlaybackDataset") 

</div>

<div class="api-title">

#  getFrameImageAtIndex

<div class="api-package">

Loads the frame image at \[index\] on-demand (and caches it). Returns decoded bitmap, or null if no image.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">getFrameImageAtIndex</span><span class="ctoken punctuation">(</span><span class="ctoken plain">index</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">android</span><span class="ctoken punctuation">.</span><span class="ctoken class-name">graphics</span><span class="ctoken punctuation">.</span><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Bitmap" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bitmap</a></span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Loads the frame image at `index` on-demand (and caches it). Returns decoded bitmap, or null if no image.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `PlaybackDatasetError.IndexOutOfBounds` — if index is invalid.
- `PlaybackDatasetError.ImageLoadFailed` — if the image file cannot be loaded.

------------------------------------------------------------------------

</div>

</div>
