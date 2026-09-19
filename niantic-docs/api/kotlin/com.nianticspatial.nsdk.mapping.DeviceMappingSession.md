---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.DeviceMappingSession/
title: DeviceMappingSession
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.mapping](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping/ "com.nianticspatial.nsdk.mapping") 

</div>

<div class="api-title">

#  DeviceMappingSession

<div class="api-extends">

↳ extends [SessionBase](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.SessionBase/ "SessionBase") 

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">DeviceMappingSession</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

A session for locally creating VPS maps from AR data. The device mapping feature provides capabilities for locally building persistent maps that can be used for Visual Positioning System (VPS) localization. These maps capture the visual features and spatial structure of an environment.

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
<td><span id="function-configure"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.DeviceMappingSession.configure/" title="Configure the session with the specified settings....">configure</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Configure the session with the specified settings.<br />
&gt; Note: It is only valid to call this when the session is stopped.<br />
&gt; Note: Configuration is asynchronous and can fail later, even if this call<br />
does not throw an error. Use [featureStatus()] to check there are no issues.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-featurestatus"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.DeviceMappingSession.featureStatus/" title="Reports errors that have occurred within processes running inside this feature....">featureStatus</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.FeatureStatus/" title="Browse to FeatureStatus">FeatureStatus</a></span></span></td>
<td><div class="ctoken comment">
Reports errors that have occurred within processes running inside this feature.<br />
Check this periodically to see if any errors have occurred with processes running<br />
inside this feature. Once an error has been flagged, it will remain flagged until the<br />
culprit process has been run again and completed successfully.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-ondestroy"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.DeviceMappingSession.onDestroy/" title="Browse to onDestroy">onDestroy</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-oninit"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.DeviceMappingSession.onInit/" title="Browse to onInit">onInit</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-start"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.DeviceMappingSession.start/" title="Start the mapping session....">start</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Start the mapping session.<br />
This starts some underlying processes that need to be running before actual mapping can begin,<br />
downloading the model containing the mapping algorithm. It does not actually start the map<br />
building process, which needs to be invoked separately with [startCreating].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-startcreating"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.DeviceMappingSession.startCreating/" title="Begin a mapping sequence....">startCreating</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Begin a mapping sequence.<br />
This begins building an on-device map that can be used for VPS.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-stop"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.DeviceMappingSession.stop/" title="Stop all mapping processes....">stop</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Stop all mapping processes.<br />
This halts active mapping while keeping the mapping instance alive.<br />
You can restart mapping later with [start].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-stopcreating"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.DeviceMappingSession.stopCreating/" title="Stop the current mapping sequence....">stopCreating</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Stop the current mapping sequence.<br />
This stops adding new frames to the current on-device VPS Map.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
