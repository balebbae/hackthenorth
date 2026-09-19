---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AnchorUpdate/
title: AnchorUpdate
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

#  AnchorUpdate

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">data</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">AnchorUpdate</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Contains the latest tracking information for a VPS anchor. `AnchorUpdate` provides comprehensive information about an anchor's current state, including its pose, tracking quality, and status information. This data is updated as VPS refines its localization.

### Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Anchor updates are retrieved via `getAnchorUpdate(uuid)` and provide the most current information about an anchor's position, orientation, and tracking status. The data includes confidence metrics and timestamps for quality assessment.

### Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val update = vpsSession.getAnchorUpdate(anchorId)
println("Anchor ID: ${update.uuid}")
println("Pose: ${update.anchorToLocalTrackingTransform}")
println("Tracking State: ${update.trackingState}")
println("Confidence: ${update.trackingConfidence}")
if (update.trackingState == AnchorTrackingState.TRACKED && update.trackingConfidence > 0.8f) {
// Use anchor pose for AR content placement
placeARContent(update.anchorToLocalTrackingTransform)
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
<td><span id="property-anchortolocaltrackingtransform"></span><span class="ctoken-line"><span class="ctoken class-name">anchorToLocalTrackingTransform</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developers.google.com/ar/reference/java/com/google/ar/core/Pose" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Pose</a></span></span></td>
<td><div class="ctoken comment">
The 4x4 transformation matrix from anchor space to local tracking space.<br />
This matrix represents the anchor's position and orientation relative to the<br />
device's current local coordinate system. Use this for placing AR content<br />
relative to the anchor.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-geolocation"></span><span class="ctoken-line"><span class="ctoken class-name">geolocation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.GeolocationData/" title="Browse to GeolocationData">GeolocationData</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Geolocation data of the anchor, or null if unavailable.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-timestampms"></span><span class="ctoken-line"><span class="ctoken class-name">timestampMs</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Long</a></span></span></td>
<td><div class="ctoken comment">
Timestamp when this update was generated (in milliseconds since epoch).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-trackingconfidence"></span><span class="ctoken-line"><span class="ctoken class-name">trackingConfidence</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Confidence score for the current tracking estimate.<br />
A value between 0.0 and 1.0 indicating the reliability of the pose estimate.<br />
Higher values indicate more reliable tracking. Use this to determine whether<br />
the pose data is suitable for your application.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-trackingstate"></span><span class="ctoken-line"><span class="ctoken class-name">trackingState</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AnchorTrackingState/" title="Represents the current tracking state of a VPS anchor....">AnchorTrackingState</a></span></span></td>
<td><div class="ctoken comment">
The current tracking state of the anchor.<br />
Indicates whether the anchor is being tracked and how reliable the pose data is.<br />
See [AnchorTrackingState] for detailed information about each state.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-trackingstatereason"></span><span class="ctoken-line"><span class="ctoken class-name">trackingStateReason</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AnchorTrackingStateReason/" title="Provides additional context about why an anchor is in a particular tracking state....">AnchorTrackingStateReason</a></span></span></td>
<td><div class="ctoken comment">
Additional context about the tracking state.<br />
Provides specific reasons for tracking issues or state changes, helping<br />
applications understand and respond to tracking problems.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-uuid"></span><span class="ctoken-line"><span class="ctoken class-name">uuid</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UUID</a></span></span></td>
<td><div class="ctoken comment">
The unique identifier of the anchor.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
