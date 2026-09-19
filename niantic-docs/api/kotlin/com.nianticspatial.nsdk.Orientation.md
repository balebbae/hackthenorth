---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.Orientation/
title: Orientation
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

#  Orientation

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">enum</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">Orientation</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Device orientation when capturing camera frames. Orientation affects how ARDK interprets camera data and poses. Ensure the correct orientation is set in \[FrameData.screenOrientation\] for accurate tracking and localization.

## See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

- FrameData.screenOrientation

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
<td><span id="case-landscape_left"></span><span class="ctoken-line"><span class="ctoken class-name">LANDSCAPE_LEFT</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">LANDSCAPE_LEFT</span></span></td>
<td><div class="ctoken comment">
Device rotated 90° counter-clockwise from portrait (landscape)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-landscape_right"></span><span class="ctoken-line"><span class="ctoken class-name">LANDSCAPE_RIGHT</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">LANDSCAPE_RIGHT</span></span></td>
<td><div class="ctoken comment">
Device rotated 90° clockwise from portrait (landscape)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-portrait"></span><span class="ctoken-line"><span class="ctoken class-name">PORTRAIT</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">PORTRAIT</span></span></td>
<td><div class="ctoken comment">
Device held upright in portrait mode
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-portrait_upside_down"></span><span class="ctoken-line"><span class="ctoken class-name">PORTRAIT_UPSIDE_DOWN</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">PORTRAIT_UPSIDE_DOWN</span></span></td>
<td><div class="ctoken comment">
Device held upside-down in portrait mode
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-unknown"></span><span class="ctoken-line"><span class="ctoken class-name">UNKNOWN</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">UNKNOWN</span></span></td>
<td><div class="ctoken comment">
Orientation is unknown or not yet determined
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
