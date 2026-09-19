---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AnchorTrackingState/
title: AnchorTrackingState
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

#  AnchorTrackingState

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">enum</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">AnchorTrackingState</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Represents the current tracking state of a VPS anchor. The tracking state indicates how well the system is able to track an anchor's position and orientation in the current environment. This information is crucial for determining the reliability of anchor pose data.

### Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Tracking states progress from not tracked to fully tracked, with limited tracking representing an intermediate state where tracking is possible but may be less reliable.

### Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val update = vpsSession.getAnchorUpdate(anchorId)
when (update.trackingState) {
AnchorTrackingState.NOT_TRACKED ->
println("Anchor is not currently being tracked")
AnchorTrackingState.LIMITED ->
println("Anchor tracking is limited - pose may be unreliable")
AnchorTrackingState.TRACKED ->
println("Anchor is fully tracked - pose is reliable")
}
```

</div>

</div>

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
<td><span id="property-value"></span><span class="ctoken-line"><span class="ctoken class-name keyword">value</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

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
<td><span id="case-limited"></span><span class="ctoken-line"><span class="ctoken class-name">LIMITED</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">LIMITED</span></span></td>
<td><div class="ctoken comment">
The anchor is being tracked with limited accuracy.<br />
In this state, the system can provide pose estimates but they may be less<br />
reliable than fully tracked anchors. This often occurs during initialization<br />
or when visual conditions are challenging.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-not_tracked"></span><span class="ctoken-line"><span class="ctoken class-name">NOT_TRACKED</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">NOT_TRACKED</span></span></td>
<td><div class="ctoken comment">
The anchor is not currently being tracked.<br />
This state indicates that the system cannot determine the anchor's position<br />
and orientation. This may occur when the device is not in the mapped area<br />
or when visual features are insufficient for tracking.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-tracked"></span><span class="ctoken-line"><span class="ctoken class-name">TRACKED</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">TRACKED</span></span></td>
<td><div class="ctoken comment">
The anchor is being tracked with full accuracy.<br />
This is the optimal tracking state where the system can provide reliable<br />
pose estimates for the anchor. The anchor's position and orientation<br />
should be considered accurate for AR applications.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
