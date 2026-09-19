---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDatasetLoader.loadDataset/
title: loadDataset
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.playback](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback/ "com.nianticspatial.nsdk.playback") <span class="api-breadcrumbs-nav">←</span>[PlaybackDatasetLoader](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDatasetLoader/ "com.nianticspatial.nsdk.playback.PlaybackDatasetLoader") 

</div>

<div class="api-title">

#  loadDataset

<div class="api-package">

Loads the dataset: reads capture JSON from this source and returns a \[PlaybackDataset\] that uses this loader for on-demand frame loading.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">open</span><span class="ctoken plain"> </span><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">loadDataset</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[PlaybackDataset](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDataset/ "A playback dataset loaded from a capture JSON file....")</span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Loads the dataset: reads capture JSON from this source and returns a `PlaybackDataset` that uses this loader for on-demand frame loading.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The dataset, or null if JSON is missing or invalid.

</div>

------------------------------------------------------------------------

## Overload<a href="#overload" class="hash-link" aria-label="Direct link to Overload" title="Direct link to Overload">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">open</span><span class="ctoken plain"> </span><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">loadDataset</span><span class="ctoken punctuation">(</span><span class="ctoken plain">imageDecoder</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken punctuation">(</span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ByteArray</a></span><span class="ctoken punctuation">)</span><span class="ctoken plain"> </span><span class="ctoken plain">-\></span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Bitmap" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bitmap</a></span><span class="ctoken plain">?</span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[PlaybackDataset](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDataset/ "A playback dataset loaded from a capture JSON file....")</span><span class="ctoken plain">?</span></span>

</div>

#### Summary<a href="#summary-1" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Loads the dataset with a custom image decoder (e.g. `{ null }` in unit tests to avoid `BitmapFactory` not mocked).

</div>

------------------------------------------------------------------------

</div>

</div>
