---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback/
title: com.nianticspatial.nsdk.playback
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") 

</div>

<div class="api-title">

#  playback

</div>

------------------------------------------------------------------------

## Classes<a href="#classes" class="hash-link" aria-label="Direct link to Classes" title="Direct link to Classes">​</a>

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
<td><span id="class-assetplaybackdatasetloader"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.AssetPlaybackDatasetLoader/" title="Loads playback dataset data from the app&#39;s [Context.getAssets] directory....">AssetPlaybackDatasetLoader</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.AssetPlaybackDatasetLoader/" title="Loads playback dataset data from the app&#39;s [Context.getAssets] directory....">AssetPlaybackDatasetLoader</a></span></span></td>
<td><div class="ctoken comment">
Loads playback dataset data from the app's [Context.getAssets] directory.<br />
Use a subdirectory that contains a capture JSON file and the frame images (and optional depth files).<br />
Example: place a dataset in <code>src/main/assets/playback/my_capture/</code> with<br />
<code>capture.json</code>, <code>frame_00000000.jpg</code>, etc. Then use<br />
<code>AssetPlaybackDatasetLoader(context, "playback/my_capture")</code>.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-playbackbackgroundview"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackBackgroundView/" title="A view that displays the current playback frame image as the background....">PlaybackBackgroundView</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackBackgroundView/" title="A view that displays the current playback frame image as the background....">PlaybackBackgroundView</a></span></span></td>
<td><div class="ctoken comment">
A view that displays the current playback frame image as the background.<br />
Place this view behind your 3D/GL surface when in playback mode and call [setPlaybackFrame]<br />
whenever a new [PlaybackFrame] is delivered so the recorded camera image is shown.<br />
Orientation is corrected so that the image (which may be stored in sensor/landscape layout)<br />
is rotated to match the current device orientation using [ImageMath.displayTransform].<br />
Use with [PlaybackSession] and a frame listener: when the session delivers a frame,<br />
build [FrameData] for NSDK and call [setPlaybackFrame] to update this view.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-playbackcamera"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackCamera/" title="Camera representation for playback, built from frame [metadata]. Exposes transform, intrinsics, resolution,...">PlaybackCamera</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackCamera/" title="Camera representation for playback, built from frame [metadata]. Exposes transform, intrinsics, resolution,...">PlaybackCamera</a></span></span></td>
<td><div class="ctoken comment">
Camera representation for playback, built from frame [metadata]. Exposes transform, intrinsics, resolution,<br />
tracking state, and orientation. Use [toArCorePose] to build a [Pose] for [FrameData.cameraPose].<br />
Use [getViewMatrix] and [getProjectionMatrix] to drive a virtual camera for playback rendering.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-playbackdataset"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDataset/" title="A playback dataset loaded from a capture JSON file....">PlaybackDataset</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDataset/" title="A playback dataset loaded from a capture JSON file....">PlaybackDataset</a></span></span></td>
<td><div class="ctoken comment">
A playback dataset loaded from a capture JSON file.<br />
Uses on-demand loading for frame images and depth: only the requested frame is loaded and cached (1-frame cache).<br />
Create via [PlaybackDataset.loadFrom] with a [PlaybackDatasetSource] (e.g. [AssetPlaybackDatasetLoader]).<br />
Use [loadFrom][PlaybackDataset.loadFrom] with a custom [imageDecoder] in unit tests to avoid [BitmapFactory] (not mocked on JVM).<br />
<strong>Thread safety:</strong> This class is NOT thread-safe. All methods must be called from a single thread.<br />
The 1-frame cache ([cachedFrameIndex], [cachedImageBytes], [cachedDepthData], [cachedConfidenceData])<br />
is not protected by a lock; concurrent reads and writes will produce inconsistent results.<br />
[PlaybackSession] satisfies this constraint by funneling all frame loads through a single coroutine dispatcher.<br />
If you introduce additional callers, ensure they are serialized.<br />
Cache fields are marked [@Volatile][Volatile] so that a value written on a background thread is<br />
immediately visible to any thread that subsequently reads it (e.g. the main thread checking<br />
[cachedFrameIndex] before deciding to reload). This is a visibility guarantee only — it does<br />
not make compound check-then-act sequences atomic.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-playbackdataseterror"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDatasetError/" title="Errors that can occur when loading or accessing playback dataset data.">PlaybackDatasetError</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDatasetError/" title="Errors that can occur when loading or accessing playback dataset data.">PlaybackDatasetError</a></span></span></td>
<td><div class="ctoken comment">
Errors that can occur when loading or accessing playback dataset data.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-playbackdatasetloader"></span><span class="ctoken-line"><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDatasetLoader/" title="Base class for loading playback dataset data from various sources....">PlaybackDatasetLoader</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDatasetLoader/" title="Base class for loading playback dataset data from various sources....">PlaybackDatasetLoader</a></span></span></td>
<td><div class="ctoken comment">
Base class for loading playback dataset data from various sources.<br />
Subclasses override [loadCaptureJson], [loadImage], [loadDepthData], [loadDepthConfidence] to provide concrete implementations.<br />
Use [loadDataset] to parse the capture JSON and create a [PlaybackDataset] that uses this loader for on-demand frame loading.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-playbacksession"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackSession/" title="Runs a timed loop over a [PlaybackDataset], loading one frame per tick and notifying a listener....">PlaybackSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackSession/" title="Runs a timed loop over a [PlaybackDataset], loading one frame per tick and notifying a listener....">PlaybackSession</a></span></span></td>
<td><div class="ctoken comment">
Runs a timed loop over a [PlaybackDataset], loading one frame per tick and notifying a listener.<br />
Use [play] to begin playback and [pause] to stop; the loop wraps to frame 0 at end.<br />
Call [setOnFrameListener] before [play] to receive each [PlaybackFrame]; the listener may be<br />
invoked from a background thread (post to main in the sample if needed).
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Interfaces<a href="#interfaces" class="hash-link" aria-label="Direct link to Interfaces" title="Direct link to Interfaces">​</a>

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
<td><span id="interface-playbackdatasetsource"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDatasetSource/" title="Abstraction for loading playback dataset data from a source (assets, file, etc.)....">PlaybackDatasetSource</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackDatasetSource/" title="Abstraction for loading playback dataset data from a source (assets, file, etc.)....">PlaybackDatasetSource</a></span></span></td>
<td><div class="ctoken comment">
Abstraction for loading playback dataset data from a source (assets, file, etc.).<br />
Used for on-demand frame loading: [PlaybackDataset] calls these methods when frames are requested.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Data Classes<a href="#data-classes" class="hash-link" aria-label="Direct link to Data Classes" title="Direct link to Data Classes">​</a>

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
<td><span id="data class-capturemetadata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.CaptureMetadata/" title="Optional capture-level metadata.">CaptureMetadata</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.CaptureMetadata/" title="Optional capture-level metadata.">CaptureMetadata</a></span></span></td>
<td><div class="ctoken comment">
Optional capture-level metadata.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-captureroot"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.CaptureRoot/" title="Root structure for the capture JSON file. Required fields per spec; optional may be null.">CaptureRoot</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.CaptureRoot/" title="Root structure for the capture JSON file. Required fields per spec; optional may be null.">CaptureRoot</a></span></span></td>
<td><div class="ctoken comment">
Root structure for the capture JSON file. Required fields per spec; optional may be null.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-framemetadata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.FrameMetadata/" title="Per-frame metadata from the capture JSON. Required fields per spec; optional may be null.">FrameMetadata</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.FrameMetadata/" title="Per-frame metadata from the capture JSON. Required fields per spec; optional may be null.">FrameMetadata</a></span></span></td>
<td><div class="ctoken comment">
Per-frame metadata from the capture JSON. Required fields per spec; optional may be null.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-locationmetadata"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.LocationMetadata/" title="Location metadata for a frame. All fields optional for varying capture formats.">LocationMetadata</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.LocationMetadata/" title="Location metadata for a frame. All fields optional for varying capture formats.">LocationMetadata</a></span></span></td>
<td><div class="ctoken comment">
Location metadata for a frame. All fields optional for varying capture formats.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-playbackframe"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackFrame/" title="One frame of playback: metadata, camera representation, optional image and depth....">PlaybackFrame</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackFrame/" title="One frame of playback: metadata, camera representation, optional image and depth....">PlaybackFrame</a></span></span></td>
<td><div class="ctoken comment">
One frame of playback: metadata, camera representation, optional image and depth.<br />
Created when a frame is loaded (e.g. by [PlaybackSession]). Use [camera] for pose/intrinsics<br />
and [metadata] for building [FrameData].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="data class-playbackgpslocation"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackGpsLocation/" title="GPS location from playback metadata (no Android dependency). Use [toLocation] to obtain...">PlaybackGpsLocation</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackGpsLocation/" title="GPS location from playback metadata (no Android dependency). Use [toLocation] to obtain...">PlaybackGpsLocation</a></span></span></td>
<td><div class="ctoken comment">
GPS location from playback metadata (no Android dependency). Use [toLocation] to obtain<br />
[android.location.Location] for [FrameData.location]. Testable without mocking Android.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
