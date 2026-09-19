---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.depth.DepthSession/
title: DepthSession
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.depth](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.depth/ "com.nianticspatial.nsdk.depth") 

</div>

<div class="api-title">

#  DepthSession

<div class="api-extends">

↳ extends [SessionBase](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.SessionBase/ "SessionBase") 

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">DepthSession</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Creates a Depth session. Depth enables your app to get estimated depth information from passed in camera data. This must be called before using any other Depth functionality.

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
<td><span id="property-depthupdates"></span><span class="ctoken-line"><span class="ctoken class-name">depthUpdates</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/kotlinx.coroutines.flow.-flow" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Flow</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKResult/" title="ResultDeprecated wrapper for NSDK operations that can succeed or fail....">NSDKResult</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.DepthBuffer/" title="Depth result from ARDK&#39;s Depth System after computing disparity.">DepthBuffer</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessStatus/" title="Browse to AwarenessStatus">AwarenessStatus</a></span><span class="ctoken punctuation">&gt;</span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Flow of depth updates. This is the primary way to receive depth updates in Kotlin.
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
<td><span id="function-configure"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.depth.DepthSession.configure/" title="Configures depth settings and parameters....">configure</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Configures depth settings and parameters.<br />
This sets up depth configuration including frame rate,<br />
and model the feature is using.<br />
Must be called after [create] but before [start].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-latestdepth"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.depth.DepthSession.latestDepth/" title="Get the latest output from the depth feature...">latestDepth</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKResult/" title="ResultDeprecated wrapper for NSDK operations that can succeed or fail....">NSDKResult</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.DepthBuffer/" title="Depth result from ARDK&#39;s Depth System after computing disparity.">DepthBuffer</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessStatus/" title="Browse to AwarenessStatus">AwarenessStatus</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Get the latest output from the depth feature<br />
This retrieves the latest depth buffer represented as an image, along side other<br />
relevant information such as the camera pose, intrinsics, and min max disparity.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-latestdepthimageparams"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.depth.DepthSession.latestDepthImageParams/" title="Get the latest image params from the depth feature...">latestDepthImageParams</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKResult/" title="ResultDeprecated wrapper for NSDK operations that can succeed or fail....">NSDKResult</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessImageParams/" title="Describes inferred image results.">AwarenessImageParams</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AwarenessStatus/" title="Browse to AwarenessStatus">AwarenessStatus</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Get the latest image params from the depth feature<br />
This retrieves the latest camera parameters used in the depth calculations.<br />
Includes the camera extrinsics, intrinsics, and image width and height.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-ondestroy"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.depth.DepthSession.onDestroy/" title="Browse to onDestroy">onDestroy</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-oninit"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.depth.DepthSession.onInit/" title="Browse to onInit">onInit</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-start"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.depth.DepthSession.start/" title="Starts the depth process....">start</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Starts the depth process.<br />
This begins generating depth information from passed in camera data.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-stop"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.depth.DepthSession.stop/" title="Stops the depth process....">stop</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Stops the depth process.<br />
This halts depth processing.<br />
You can restart depth later with [start].
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
