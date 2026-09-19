---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackSessionDelegate.method-playbackSession/
title: playbackSession
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[PlaybackSessionDelegate](https://www.nianticspatial.com/docs/api/swift/NSDK.interface-PlaybackSessionDelegate/ "PlaybackSessionDelegate") 

</div>

<div class="api-title">

#  playbackSession

<div class="api-package">

Called on the main queue each time a new playback frame is ready. Use the frame's metadata, image, and optional depth for rendering or processing.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">playbackSession</span><span class="ctoken plain">(</span><span class="ctoken plain">\_</span><span class="ctoken plain"> </span><span class="ctoken plain">session</span><span class="ctoken plain">: </span><span class="ctoken class-name">[PlaybackSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackSession/ "Drives playback. **Subclasses ARSession** so it can be assigned to `ARView.session` and the app can use...")</span><span class="ctoken plain">, </span><span class="ctoken plain">didUpdate</span><span class="ctoken plain"> </span><span class="ctoken plain">frame</span><span class="ctoken plain">: </span><span class="ctoken class-name">[PlaybackFrame](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-PlaybackFrame/ "One "frame" of playback: metadata (pose, intrinsics, orientation, etc.), optional camera image, optional depth....")</span><span class="ctoken plain">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Called on the main queue each time a new playback frame is ready. Use the frame's metadata, image, and optional depth for rendering or processing.

</div>

### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

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
<td><span id="external parameter-session"></span><span class="ctoken-line"><span class="ctoken class-name">session</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackSession/" title="Drives playback. **Subclasses ARSession** so it can be assigned to `ARView.session` and the app can use...">PlaybackSession</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-didupdate"></span><span class="ctoken-line"><span class="ctoken class-name">frame</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-PlaybackFrame/" title="One &quot;frame&quot; of playback: metadata (pose, intrinsics, orientation, etc.), optional camera image, optional depth....">PlaybackFrame</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Overload<a href="#overload" class="hash-link" aria-label="Direct link to Overload" title="Direct link to Overload">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">playbackSession</span><span class="ctoken plain">(</span><span class="ctoken plain">\_</span><span class="ctoken plain"> </span><span class="ctoken plain">session</span><span class="ctoken plain">: </span><span class="ctoken class-name">[PlaybackSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackSession/ "Drives playback. **Subclasses ARSession** so it can be assigned to `ARView.session` and the app can use...")</span><span class="ctoken plain">, </span><span class="ctoken plain">cameraDidChangeTrackingState</span><span class="ctoken plain"> </span><span class="ctoken plain">camera</span><span class="ctoken plain">: </span><span class="ctoken class-name">[PlaybackCamera](https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackCamera/ "Camera representation built from frame **metadata** (pose4x4, intrinsics, resolution). Exposes the same...")</span><span class="ctoken plain">)</span></span>

</div>

#### Summary<a href="#summary-1" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Called on the main queue when the tracking state changes (e.g. at start of playback). For playback, state is typically .normal.

</div>

### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

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
<td><span id="external parameter-session"></span><span class="ctoken-line"><span class="ctoken class-name">session</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackSession/" title="Drives playback. **Subclasses ARSession** so it can be assigned to `ARView.session` and the app can use...">PlaybackSession</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-didupdate"></span><span class="ctoken-line"><span class="ctoken class-name">frame</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-PlaybackFrame/" title="One &quot;frame&quot; of playback: metadata (pose, intrinsics, orientation, etc.), optional camera image, optional depth....">PlaybackFrame</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
