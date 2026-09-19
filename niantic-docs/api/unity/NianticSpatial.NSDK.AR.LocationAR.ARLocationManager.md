---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.LocationAR.ARLocationManager/
title: ARLocationManager
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.LocationAR](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.LocationAR/ "NianticSpatial.NSDK.AR.LocationAR") 

</div>

<div class="api-title">

#  ARLocationManager

<div class="api-extends">

↳ extends [ARVps2Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager/ "ARVps2Manager") 

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">ARLocationManager</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[ARVps2Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager/ "Browse to ARVps2Manager")</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

The ARLocationManager is used to track ARLocations. ARLocations tie digital content to the physical world. When you start tracking an ARLocation, and aim your phone's camera at the physical location, the digital content that you child to the ARLocation will appear in the physical world.

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
<td><span id="property-anchortoarlocationmap"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">AnchorToARLocationMap</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Dictionary</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Anchor/" title="Represents a Persistent Anchor tracked by an XR device.">ARVps2Anchor</a></span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.LocationAR.ARLocation/" title="The ARLocation is the digital twin of the physical location">ARLocation</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Get all the active ARVps2Anchors created by ARLocationManager
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-arlocations"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">ARLocations</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.LocationAR.ARLocation/" title="The ARLocation is the digital twin of the physical location">ARLocation</a></span><span class="ctoken punctuation">[</span><span class="ctoken punctuation">]</span></span></td>
<td><div class="ctoken comment">
Gets all of the ARLocations childed to the ARLocationManager.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-autotrack"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">AutoTrack</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Whether or not to automatically start tracking the selected ARLocation.<br />
If true, the location that is currently enabled will be automatically tracked on Start.
</div></td>
</tr>
</tbody>
</table>

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
<td><span id="method-setarlocations"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.LocationAR.ARLocationManager.SetARLocations/" title="Selects the AR Locations to try to track when StartARLocationTracking() is called.">SetARLocations</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment">
Selects the AR Locations to try to track when StartARLocationTracking() is called.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-startarlocationtracking"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.LocationAR.ARLocationManager.StartARLocationTracking/" title="Starts tracking locations specified by SetARLocations() or set in Unity Editor...">StartARLocationTracking</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment">
Starts tracking locations specified by SetARLocations() or set in Unity Editor<br />
Content authored as children of the ARLocation will be enabled once the ARLocation becomes tracked.<br />
This will create digital content in the physical world.<br />
If no locations were specified in SetARLocations(), requests will be made to attempt to track nearby<br />
locations. In this case, multiple nearby locations may be targeted and the first one to successfully<br />
track will be used.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-stoparlocationtracking"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.LocationAR.ARLocationManager.StopARLocationTracking/" title="Stops tracking all currently tracked locations.">StopARLocationTracking</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment">
Stops tracking all currently tracked locations.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
