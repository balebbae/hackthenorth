---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkFrame/
title: NsdkFrame
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk/ "com.nianticspatial.nsdk") 

</div>

<div class="api-title">

#  NsdkFrame

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">sealed</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">NsdkFrame</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Abstraction over the current frame so callers can use one API for both live AR (ARCore \[Frame\]) and playback (\[PlaybackFrame\]). Use \[camera\] for pose, intrinsics, and tracking. Use \[backing\] when you need Frame- or PlaybackFrame-specific APIs (e.g. acquireCameraImage).

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
<td><span id="property-backing"></span><span class="ctoken-line"><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name">backing</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Backing</span></span></td>
<td><div class="ctoken comment">
The underlying frame (live or playback). Switch on this for type-specific APIs.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-camera"></span><span class="ctoken-line"><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name">camera</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkCamera/" title="Camera view over the current frame (live or playback). Mirrors ARCore [com.google.ar.core.Camera]...">NsdkCamera</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-timestamp"></span><span class="ctoken-line"><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name">timestamp</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Long</a></span></span></td>
<td><div class="ctoken comment">
Timestamp in nanoseconds when this frame was captured. Matches ARCore [Frame.getTimestamp].
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
<td><span id="function-getupdatedanchors"></span><span class="ctoken-line"><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkFrame.getUpdatedAnchors/" title="Anchors updated this frame (live only; playback returns empty). Matches ARCore [Frame.getUpdatedAnchors].">getUpdatedAnchors</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">Collection</span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://developers.google.com/ar/reference/java/com/google/ar/core/Anchor" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Anchor</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Anchors updated this frame (live only; playback returns empty). Matches ARCore [Frame.getUpdatedAnchors].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-hasdisplaygeometrychanged"></span><span class="ctoken-line"><span class="ctoken keyword">abstract</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkFrame.hasDisplayGeometryChanged/" title="True if display rotation or viewport changed since the previous frame. Matches ARCore [Frame.hasDisplayGeometryChanged]. Playback always returns false.">hasDisplayGeometryChanged</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Boolean</a></span></span></td>
<td><div class="ctoken comment">
True if display rotation or viewport changed since the previous frame. Matches ARCore [Frame.hasDisplayGeometryChanged]. Playback always returns false.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
