---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackRenderer.method-renderFrame/
title: renderFrame
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[PlaybackRenderer](https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackRenderer/ "PlaybackRenderer") 

</div>

<div class="api-title">

#  renderFrame

<div class="api-package">

Called on the main queue for each new playback frame. Updates the background image and the virtual camera pose/FOV to match the frame.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">renderFrame</span><span class="ctoken plain">(</span><span class="ctoken plain">\_</span><span class="ctoken plain"> </span><span class="ctoken plain">frame</span><span class="ctoken plain">: </span><span class="ctoken class-name">[PlaybackFrame](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-PlaybackFrame/ "One "frame" of playback: metadata (pose, intrinsics, orientation, etc.), optional camera image, optional depth....")</span><span class="ctoken plain">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Called on the main queue for each new playback frame. Updates the background image and the virtual camera pose/FOV to match the frame.

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
<td><span id="external parameter-frame"></span><span class="ctoken-line"><span class="ctoken class-name">frame</span></span></td>
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
