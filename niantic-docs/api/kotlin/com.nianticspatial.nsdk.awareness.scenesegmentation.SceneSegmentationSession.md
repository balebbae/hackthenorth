---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession/
title: SceneSegmentationSession
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

#  SceneSegmentationSession

<div class="api-extends">

↳ extends [SessionBase](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.SessionBase/ "SessionBase") 

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">SceneSegmentationSession</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Creates a SceneSegmentation session for semantic understanding. The SceneSegmentation feature allows you to understand the semantic content of the environment, identifying objects, surfaces, and other meaningful elements in the scene.

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
<td><span id="property-confidencechannel"></span><span class="ctoken-line"><span class="ctoken class-name">confidenceChannel</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationChannel/" title="Represents the different semantic segmentation channels that can be detected....">SceneSegmentationChannel</a></span></span></td>
<td><div class="ctoken comment">
The channel index for confidence updates. Can be changed at any time.<br />
When changed, the polling will automatically use the new channel index on the next poll.<br />
Default is 0 (Sky channel).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-confidenceupdates"></span><span class="ctoken-line"><span class="ctoken class-name">confidenceUpdates</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/kotlinx.coroutines.flow.-flow" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Flow</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKResult/" title="ResultDeprecated wrapper for NSDK operations that can succeed or fail....">NSDKResult</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationResult/" title="Represents the result of the scene segmentation processor....">SceneSegmentationResult</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessStatus/" title="Browse to AwarenessStatus">AwarenessStatus</a></span><span class="ctoken punctuation">&gt;</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Flow of confidence updates for the currently configured semantic channel.<br />
Confidence values represent the probability that a pixel belongs to the channel.<br />
The channel index can be changed by setting [confidenceChannelIndex].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-imageparamsupdates"></span><span class="ctoken-line"><span class="ctoken class-name">imageParamsUpdates</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/kotlinx.coroutines.flow.-flow" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Flow</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKResult/" title="ResultDeprecated wrapper for NSDK operations that can succeed or fail....">NSDKResult</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessImageParams/" title="Describes inferred image results.">AwarenessImageParams</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessStatus/" title="Browse to AwarenessStatus">AwarenessStatus</a></span><span class="ctoken punctuation">&gt;</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Flow of image parameter updates.<br />
Image parameters include camera intrinsics, extrinsics, and image dimensions.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-packedchannelsupdates"></span><span class="ctoken-line"><span class="ctoken class-name">packedChannelsUpdates</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/kotlinx.coroutines.flow.-flow" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Flow</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKResult/" title="ResultDeprecated wrapper for NSDK operations that can succeed or fail....">NSDKResult</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationResult/" title="Represents the result of the scene segmentation processor....">SceneSegmentationResult</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessStatus/" title="Browse to AwarenessStatus">AwarenessStatus</a></span><span class="ctoken punctuation">&gt;</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Flow of packed channel updates. This is the primary way to receive packed channel scene segmentation updates.<br />
Packed channels contain all semantic channels in a single bitmask per pixel.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-suppressionmaskupdates"></span><span class="ctoken-line"><span class="ctoken class-name">suppressionMaskUpdates</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/kotlinx.coroutines.flow.-flow" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Flow</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKResult/" title="ResultDeprecated wrapper for NSDK operations that can succeed or fail....">NSDKResult</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationResult/" title="Represents the result of the scene segmentation processor....">SceneSegmentationResult</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessStatus/" title="Browse to AwarenessStatus">AwarenessStatus</a></span><span class="ctoken punctuation">&gt;</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Flow of suppression mask updates.<br />
Suppression masks indicate which pixels should be suppressed in semantic processing.
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
<td><span id="function-channelnames"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession.channelNames/" title="Gets the names of available semantic channels....">channelNames</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Array</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationChannel/" title="Represents the different semantic segmentation channels that can be detected....">SceneSegmentationChannel</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Gets the names of available semantic channels.<br />
This retrieves a list of semantic channel names that can be used<br />
for semantic analysis and classification.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-configure"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession.configure/" title="Configures scene segmentation settings and parameters....">configure</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Configures scene segmentation settings and parameters.<br />
This sets up scene segmentation configuration including quality settings,<br />
processing parameters, and output options.<br />
This can only be run while the session is stopped.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-featurestatus"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession.featureStatus/" title="Reports errors that have occurred with processes running inside this session....">featureStatus</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.FeatureStatus/" title="Browse to FeatureStatus">FeatureStatus</a></span></span></td>
<td><div class="ctoken comment">
Reports errors that have occurred with processes running inside this session.<br />
Check this periodically to see if any errors have occurred with<br />
processes running inside this feature. Once an error has been<br />
flagged, it will remain flagged until the culprit process has<br />
been run again and completed successfully.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-latestconfidence"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession.latestConfidence/" title="Gets the latest scene segmentation confidence data....">latestConfidence</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKResult/" title="ResultDeprecated wrapper for NSDK operations that can succeed or fail....">NSDKResult</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationResult/" title="Represents the result of the scene segmentation processor....">SceneSegmentationResult</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessStatus/" title="Browse to AwarenessStatus">AwarenessStatus</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Gets the latest scene segmentation confidence data.<br />
This retrieves the most recent confidence values for semantic<br />
classification of the current frame.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-latestimageparams"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession.latestImageParams/" title="Gets the latest image parameters for scene segmentation processing....">latestImageParams</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKResult/" title="ResultDeprecated wrapper for NSDK operations that can succeed or fail....">NSDKResult</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessImageParams/" title="Describes inferred image results.">AwarenessImageParams</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessStatus/" title="Browse to AwarenessStatus">AwarenessStatus</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Gets the latest image parameters for scene segmentation processing.<br />
This retrieves the most recent image parameters used for<br />
semantic analysis of the current frame.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-latestpackedchannel"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession.latestPackedChannel/" title="Gets the latest packed channel scene segmentation data....">latestPackedChannel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKResult/" title="ResultDeprecated wrapper for NSDK operations that can succeed or fail....">NSDKResult</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationResult/" title="Represents the result of the scene segmentation processor....">SceneSegmentationResult</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessStatus/" title="Browse to AwarenessStatus">AwarenessStatus</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Gets the latest packed channel scene segmentation data.<br />
This retrieves the most recent packed channel data for semantic<br />
classification of the current frame.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-latestsuppressionmask"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession.latestSuppressionMask/" title="Gets the latest suppression mask data....">latestSuppressionMask</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKResult/" title="ResultDeprecated wrapper for NSDK operations that can succeed or fail....">NSDKResult</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationResult/" title="Represents the result of the scene segmentation processor....">SceneSegmentationResult</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessStatus/" title="Browse to AwarenessStatus">AwarenessStatus</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Gets the latest suppression mask data.<br />
This retrieves the most recent suppression mask for semantic<br />
classification of the current frame.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-ondestroy"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession.onDestroy/" title="Browse to onDestroy">onDestroy</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-oninit"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession.onInit/" title="Browse to onInit">onInit</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-start"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession.start/" title="Starts the scene segmentation session....">start</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Starts the scene segmentation session.<br />
This begins actively analyzing the environment for semantic content,<br />
identifying objects and surfaces in real-time.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-stop"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession.stop/" title="Stops the scene segmentation session....">stop</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Stops the scene segmentation session.<br />
This halts scene segmentation processing while keeping the native scene segmentation session loaded.<br />
You can restart scene segmentation later with [start].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-unpackchannelsfrombitmask"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession.unpackChannelsFromBitmask/" title="Unpacks semantic channels from a packed channel bitmask....">unpackChannelsFromBitmask</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EnumSet.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">EnumSet</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationChannel/" title="Represents the different semantic segmentation channels that can be detected....">SceneSegmentationChannel</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Unpacks semantic channels from a packed channel bitmask.<br />
This converts a bitmask value (where each bit represents a semantic channel)<br />
into an EnumSet of SceneSegmentationChannel enum values representing the channels present<br />
in the bitmask.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
