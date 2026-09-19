---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDataset/
title: PlaybackDataset
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

#  PlaybackDataset

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">PlaybackDataset</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

A playback dataset loaded from a capture JSON file. Uses on-demand loading for frame images and depth: only the requested frame is loaded and cached (1-frame cache). Create via \[PlaybackDataset.loadFrom\] with a \[PlaybackDatasetSource\] (e.g. \[AssetPlaybackDatasetLoader\]). Use \[loadFrom\]\[PlaybackDataset.loadFrom\] with a custom \[imageDecoder\] in unit tests to avoid \[BitmapFactory\] (not mocked on JVM). **Thread safety:** This class is NOT thread-safe. All methods must be called from a single thread. The 1-frame cache (\[cachedFrameIndex\], \[cachedImageBytes\], \[cachedDepthData\], \[cachedConfidenceData\]) is not protected by a lock; concurrent reads and writes will produce inconsistent results. \[PlaybackSession\] satisfies this constraint by funneling all frame loads through a single coroutine dispatcher. If you introduce additional callers, ensure they are serialized. Cache fields are marked \[@Volatile\]\[Volatile\] so that a value written on a background thread is immediately visible to any thread that subsequently reads it (e.g. the main thread checking \[cachedFrameIndex\] before deciding to reload). This is a visibility guarantee only — it does not make compound check-then-act sequences atomic.

------------------------------------------------------------------------

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

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
<td><span id="property-framecount"></span><span class="ctoken-line"><span class="ctoken class-name">frameCount</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-frameinterval"></span><span class="ctoken-line"><span class="ctoken class-name">frameInterval</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Double</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

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
<td><span id="function-getdepthconfidenceatindex"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDataset.getDepthConfidenceAtIndex/" title="Loads depth confidence (UInt8 binary) at [index] on-demand. Returns null if not available.">getDepthConfidenceAtIndex</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ByteArray</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Loads depth confidence (UInt8 binary) at [index] on-demand. Returns null if not available.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getdepthdataatindex"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDataset.getDepthDataAtIndex/" title="Loads depth data (Float32 binary) at [index] on-demand. Returns null if this frame has no depth.">getDepthDataAtIndex</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ByteArray</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Loads depth data (Float32 binary) at [index] on-demand. Returns null if this frame has no depth.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getframeimageatindex"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDataset.getFrameImageAtIndex/" title="Loads the frame image at [index] on-demand (and caches it). Returns decoded bitmap, or null if no image.">getFrameImageAtIndex</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">android</span><span class="ctoken punctuation">.</span><span class="ctoken class-name">graphics</span><span class="ctoken punctuation">.</span><span class="ctoken class-name"><a href="https://developer.android.com/reference/android/opengl/Bitmap" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bitmap</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Loads the frame image at [index] on-demand (and caches it). Returns decoded bitmap, or null if no image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getframeimagebytesatindex"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDataset.getFrameImageBytesAtIndex/" title="Returns raw image bytes at [index] (on-demand, cached). Use when you need bytes instead of Bitmap.">getFrameImageBytesAtIndex</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ByteArray</a></span></span></td>
<td><div class="ctoken comment">
Returns raw image bytes at [index] (on-demand, cached). Use when you need bytes instead of Bitmap.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getframemetadataatindex"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDataset.getFrameMetadataAtIndex/" title="Returns frame metadata at [index].">getFrameMetadataAtIndex</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.FrameMetadata/" title="Per-frame metadata from the capture JSON. Required fields per spec; optional may be null.">FrameMetadata</a></span></span></td>
<td><div class="ctoken comment">
Returns frame metadata at [index].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getplaybackframeatindex"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDataset.getPlaybackFrameAtIndex/" title="Loads a single frame at [index] as a [PlaybackFrame] (metadata, camera, optional image and depth)....">getPlaybackFrameAtIndex</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackFrame/" title="One frame of playback: metadata, camera representation, optional image and depth....">PlaybackFrame</a></span></span></td>
<td><div class="ctoken comment">
Loads a single frame at [index] as a [PlaybackFrame] (metadata, camera, optional image and depth).<br />
Image load failure yields a frame with [PlaybackFrame.image] null; depth is null when not available.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-hasdepth"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDataset.hasDepth/" title="True if the dataset declares LiDAR depth ([depthSource] == &quot;lidar&quot;).">hasDepth</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Boolean</a></span></span></td>
<td><div class="ctoken comment">
True if the dataset declares LiDAR depth ([depthSource] == "lidar").
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
