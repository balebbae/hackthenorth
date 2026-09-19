---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKCamera.enum-Backing/
title: Backing
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKCamera](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKCamera/ "NSDKCamera") 

</div>

<div class="api-title">

#  Backing

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">enum</span><span class="ctoken plain"> </span><span class="ctoken class-name">Backing</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

The underlying camera: either a live ARCamera or a playback PlaybackCamera. Switch on this when you need to call APIs that are specific to one type (e.g. `recordedOrientation` on PlaybackCamera). Example:

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
switch camera.backing {
case .ar(let arCamera):
    // ARCamera-specific APIs
case .playback(let playbackCamera):
    let orientation = playbackCamera.recordedOrientation
}
```

</div>

</div>

------------------------------------------------------------------------

## Cases<a href="#cases" class="hash-link" aria-label="Direct link to Cases" title="Direct link to Cases">​</a>

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
<td><span id="case-ar"></span><span class="ctoken-line"><span class="ctoken keyword">case</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKCamera.enum-Backing/#case-ar" title="Browse to ar">ar</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">ARCamera</span><span class="ctoken plain">)</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-playback"></span><span class="ctoken-line"><span class="ctoken keyword">case</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKCamera.enum-Backing/#case-playback" title="Browse to playback">playback</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackCamera/" title="Camera representation built from frame **metadata** (pose4x4, intrinsics, resolution). Exposes the same...">PlaybackCamera</a></span><span class="ctoken plain">)</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
