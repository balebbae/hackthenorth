---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRVps2Subsystem.Provider.GetPose/
title: GetPose
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.XRSubsystems](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems/ "NianticSpatial.NSDK.AR.XRSubsystems") <span class="api-breadcrumbs-nav">←</span>[XRVps2Subsystem](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRVps2Subsystem/ "NianticSpatial.NSDK.AR.XRSubsystems.XRVps2Subsystem") <span class="api-breadcrumbs-nav">←</span>[Provider](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRVps2Subsystem.Provider/ "NianticSpatial.NSDK.AR.XRSubsystems.XRVps2Subsystem.Provider") 

</div>

<div class="api-title">

#  GetPose

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">virtual</span><span class="ctoken plain"> </span><span class="ctoken class-name">[XRVps2Pose](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRVps2Pose/ "Structure describing device location in local AR coordinate space as...")</span><span class="ctoken plain"> </span><span class="ctoken class-name">GetPose</span><span class="ctoken punctuation">(</span><span class="ctoken class-name">[XRVps2Localization](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRVps2Localization/ "Spatial mapping between the device’s AR coordinate space and real-world geolocation,...")</span><span class="ctoken plain"> </span><span class="ctoken class-name">localization</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LocationInfo.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">LocationInfo</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">location</span><span class="ctoken punctuation">)</span></span>

</div>

### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

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
<td><span id="external parameter-localization"></span><span class="ctoken-line"><span class="ctoken class-name">localization</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRVps2Localization/" title="Spatial mapping between the device’s AR coordinate space and real-world geolocation,...">XRVps2Localization</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-latitude"></span><span class="ctoken-line"><span class="ctoken class-name">latitude</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">double</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-longitude"></span><span class="ctoken-line"><span class="ctoken class-name">longitude</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">double</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-altitude"></span><span class="ctoken-line"><span class="ctoken class-name">altitude</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">double</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-orientationedn"></span><span class="ctoken-line"><span class="ctoken class-name">orientationEdn</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Quaternion</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Overload<a href="#overload" class="hash-link" aria-label="Direct link to Overload" title="Direct link to Overload">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">virtual</span><span class="ctoken plain"> </span><span class="ctoken class-name">[XRVps2Pose](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRVps2Pose/ "Structure describing device location in local AR coordinate space as...")</span><span class="ctoken plain"> </span><span class="ctoken class-name">GetPose</span><span class="ctoken punctuation">(</span><span class="ctoken class-name">[XRVps2Localization](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRVps2Localization/ "Spatial mapping between the device’s AR coordinate space and real-world geolocation,...")</span><span class="ctoken plain"> </span><span class="ctoken class-name">localization</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">double</span><span class="ctoken plain"> </span><span class="ctoken class-name">latitude</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">double</span><span class="ctoken plain"> </span><span class="ctoken class-name">longitude</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">double</span><span class="ctoken plain"> </span><span class="ctoken class-name">altitude</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Quaternion</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">orientationEdn</span><span class="ctoken punctuation">)</span></span>

</div>

### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

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
<td><span id="external parameter-localization"></span><span class="ctoken-line"><span class="ctoken class-name">localization</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRVps2Localization/" title="Spatial mapping between the device’s AR coordinate space and real-world geolocation,...">XRVps2Localization</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-latitude"></span><span class="ctoken-line"><span class="ctoken class-name">latitude</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">double</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-longitude"></span><span class="ctoken-line"><span class="ctoken class-name">longitude</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">double</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-altitude"></span><span class="ctoken-line"><span class="ctoken class-name">altitude</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">double</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="external parameter-orientationedn"></span><span class="ctoken-line"><span class="ctoken class-name">orientationEdn</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Quaternion</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
