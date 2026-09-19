---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AnchorTrackingStateReason/
title: AnchorTrackingStateReason
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

#  AnchorTrackingStateReason

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">enum</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">AnchorTrackingStateReason</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Provides additional context about why an anchor is in a particular tracking state. When an anchor is not tracked or has limited tracking, this enum provides specific reasons that can help developers understand and respond to tracking issues.

### Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Tracking state reasons help diagnose why tracking may be failing or limited, enabling applications to provide appropriate user feedback or take corrective actions.

### Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val update = vpsSession.getAnchorUpdate(anchorId)
when (update.trackingStateReason) {
AnchorTrackingStateReason.INITIALIZING ->
println("Anchor is still initializing - tracking will improve")
AnchorTrackingStateReason.PERMISSION_DENIED ->
println("Tracking failed due to permission issues")
AnchorTrackingStateReason.FATAL_NETWORK_ERROR ->
println("Network error preventing tracking")
else ->
println("Other tracking issue: ${update.trackingStateReason}")
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
<td><span id="case-fatal_network_error"></span><span class="ctoken-line"><span class="ctoken class-name">FATAL_NETWORK_ERROR</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">FATAL_NETWORK_ERROR</span></span></td>
<td><div class="ctoken comment">
A fatal network error prevented tracking.<br />
This reason indicates that network connectivity issues are preventing<br />
the VPS system from functioning properly.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-initializing"></span><span class="ctoken-line"><span class="ctoken class-name">INITIALIZING</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">INITIALIZING</span></span></td>
<td><div class="ctoken comment">
The anchor is currently initializing and tracking will improve.<br />
This reason indicates that the system is still processing the anchor's<br />
visual features and tracking quality should improve over time.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-internal_error"></span><span class="ctoken-line"><span class="ctoken class-name">INTERNAL_ERROR</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">INTERNAL_ERROR</span></span></td>
<td><div class="ctoken comment">
An internal error occurred within the tracking system.<br />
This reason indicates a system-level error that prevented normal tracking.<br />
The application should check the VPS feature status for more details.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-none"></span><span class="ctoken-line"><span class="ctoken class-name">NONE</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">NONE</span></span></td>
<td><div class="ctoken comment">
No specific reason for the current tracking state.<br />
This is the default state when tracking is working normally or when<br />
no specific reason has been identified for tracking issues.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-no_visual_localization"></span><span class="ctoken-line"><span class="ctoken class-name">NO_VISUAL_LOCALIZATION</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">NO_VISUAL_LOCALIZATION</span></span></td>
<td><div class="ctoken comment">
The device has not localized to a VPS location.<br />
This reason indicates that the device has not yet successfully localized<br />
to a VPS location, so anchor position accuracy is limited.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-permission_denied"></span><span class="ctoken-line"><span class="ctoken class-name">PERMISSION_DENIED</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">PERMISSION_DENIED</span></span></td>
<td><div class="ctoken comment">
Tracking failed due to insufficient permissions.<br />
This reason indicates that the anchor target requested is not accessible<br />
by the current authenticated user. Check that the API key or authentication token<br />
has the necessary permissions and organization access.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="case-removed"></span><span class="ctoken-line"><span class="ctoken class-name">REMOVED</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">REMOVED</span></span></td>
<td><div class="ctoken comment">
The anchor has been explicitly removed from tracking.<br />
This reason indicates that the anchor was removed via <code>removeAnchor</code><br />
and is no longer being tracked by the system.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
