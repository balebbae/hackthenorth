---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackDataset/
title: PlaybackDataset
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") 

</div>

<div class="api-title">

#  PlaybackDataset

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">PlaybackDataset</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

A dataset loaded from a capture JSON file containing frame metadata. This class uses on-demand loading for frame images and depth data. Only the currently requested frame is loaded into memory, reducing memory pressure for large datasets.

------------------------------------------------------------------------

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

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
<td><span id="method-hasdepth"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackDataset.method-hasDepth/" title="Checks if the dataset has depth data from a LiDAR source.">hasDepth</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
Checks if the dataset has depth data from a LiDAR source.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Nested Types<a href="#nested-types" class="hash-link" aria-label="Direct link to Nested Types" title="Direct link to Nested Types">​</a>

### Structs<a href="#structs" class="hash-link" aria-label="Direct link to Structs" title="Direct link to Structs">​</a>

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
<td><span id="struct-capturemetadata"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackDataset.struct-CaptureMetadata/" title="Metadata structure for capture information. All fields optional so varying capture exports decode without keyNotFound.">CaptureMetadata</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackDataset.struct-CaptureMetadata/" title="Metadata structure for capture information. All fields optional so varying capture exports decode without keyNotFound.">CaptureMetadata</a></span></span></td>
<td><div class="ctoken comment">
Metadata structure for capture information. All fields optional so varying capture exports decode without keyNotFound.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-captureroot"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackDataset.struct-CaptureRoot/" title="Root structure for the capture JSON file. Required fields per capture.json spec; optional fields may be omitted.">CaptureRoot</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackDataset.struct-CaptureRoot/" title="Root structure for the capture JSON file. Required fields per capture.json spec; optional fields may be omitted.">CaptureRoot</a></span></span></td>
<td><div class="ctoken comment">
Root structure for the capture JSON file. Required fields per capture.json spec; optional fields may be omitted.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-framemetadata"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackDataset.struct-FrameMetadata/" title="Frame metadata structure matching the JSON format. Required fields per capture.json spec; optional fields may be omitted.">FrameMetadata</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackDataset.struct-FrameMetadata/" title="Frame metadata structure matching the JSON format. Required fields per capture.json spec; optional fields may be omitted.">FrameMetadata</a></span></span></td>
<td><div class="ctoken comment">
Frame metadata structure matching the JSON format. Required fields per capture.json spec; optional fields may be omitted.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-locationmetadata"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackDataset.struct-LocationMetadata/" title="Location metadata structure. All fields are optional so various capture formats (2D-only GPS, no compass, minimal logs) decode without keyNotFound.">LocationMetadata</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackDataset.struct-LocationMetadata/" title="Location metadata structure. All fields are optional so various capture formats (2D-only GPS, no compass, minimal logs) decode without keyNotFound.">LocationMetadata</a></span></span></td>
<td><div class="ctoken comment">
Location metadata structure. All fields are optional so various capture formats (2D-only GPS, no compass, minimal logs) decode without keyNotFound.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

### Enums<a href="#enums" class="hash-link" aria-label="Direct link to Enums" title="Direct link to Enums">​</a>

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
<td><span id="enum-playbackdataseterror"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackDataset.enum-PlaybackDatasetError/" title="Errors that can occur when retrieving frame data.">PlaybackDatasetError</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.PlaybackDataset.enum-PlaybackDatasetError/" title="Errors that can occur when retrieving frame data.">PlaybackDatasetError</a></span></span></td>
<td><div class="ctoken comment">
Errors that can occur when retrieving frame data.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
