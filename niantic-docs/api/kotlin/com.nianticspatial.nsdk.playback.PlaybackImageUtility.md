---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackImageUtility/
title: PlaybackImageUtility
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

#  PlaybackImageUtility

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">object</span><span class="ctoken plain"> </span><span class="ctoken class-name">PlaybackImageUtility</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Converts a playback \[Bitmap\] to an Android \[Image\] in YUV_420_888 format so it can be passed as \[com.nianticspatial.nsdk.FrameData.cameraImagePlanes\] to \[com.nianticspatial.nsdk.NSDKSession.sendFrame\]. Caller must call \[YuvImageHandler.close\] when done (e.g. after sendFrame returns).

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
<td><span id="function-bitmaptoyuvimage"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.playback.PlaybackImageUtility.bitmapToYuvImage/" title="Converts [bitmap] to a YUV_420_888 [Image]. Returns null if conversion fails....">bitmapToYuvImage</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">YuvImageHandler</span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Converts [bitmap] to a YUV_420_888 [Image]. Returns null if conversion fails.<br />
Caller must call [YuvImageHandler.close] after use (e.g. after sendFrame returns).
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
