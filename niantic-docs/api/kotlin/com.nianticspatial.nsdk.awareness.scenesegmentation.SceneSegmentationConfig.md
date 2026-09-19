---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationConfig/
title: SceneSegmentationConfig
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.awareness.scenesegmentation](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation/ "com.nianticspatial.nsdk.awareness.scenesegmentation") 

</div>

<div class="api-title">

#  SceneSegmentationConfig

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">SceneSegmentationConfig</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Configuration for the scene segmentation feature. This class provides configuration options for the scene segmentation processing system, allowing customization of frame rate, processing mode, and other parameters. Non-boolean fields left at default values will be internally converted to appropriate defaults by the system.

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
<td><span id="property-framerate"></span><span class="ctoken-line"><span class="ctoken class-name">frameRate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
Target FPS for recording and visualization processes.<br />
The target framerate is the cap for how often the feature will<br />
process new input frames. The actual framerate may be lower.<br />
This is set to 30 in the default configuration.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-mode"></span><span class="ctoken-line"><span class="ctoken class-name">mode</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessFeatureMode/" title="Browse to AwarenessFeatureMode">AwarenessFeatureMode</a></span></span></td>
<td><div class="ctoken comment">
Descriptor for the scene segmentation mode.<br />
Controls the processing mode for scene segmentation processing, affecting<br />
the balance between performance and accuracy.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-numthresholds"></span><span class="ctoken-line"><span class="ctoken class-name">numThresholds</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
Number of threshold values.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-suppressionmaskchannels"></span><span class="ctoken-line"><span class="ctoken class-name">suppressionMaskChannels</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
Suppression mask channels configuration.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-thresholds"></span><span class="ctoken-line"><span class="ctoken class-name">thresholds</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">FloatArray</a></span></span></td>
<td><div class="ctoken comment">
Threshold values for semantic processing.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
