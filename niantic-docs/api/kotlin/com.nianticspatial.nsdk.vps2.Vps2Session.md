---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session/
title: Vps2Session
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.vps2](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2/ "com.nianticspatial.nsdk.vps2") 

</div>

<div class="api-title">

#  Vps2Session

<div class="api-extends">

↳ extends [SessionBase](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.SessionBase/ "SessionBase") 

</div>

<div class="api-package">

A session for VPS2 localization.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">Vps2Session</span></span>

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
<td><span id="property-anchorupdates"></span><span class="ctoken-line"><span class="ctoken class-name">anchorUpdates</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/kotlinx.coroutines.flow.-flow" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Flow</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AnchorUpdate/" title="Contains the latest tracking information for a VPS anchor....">AnchorUpdate</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Flow of anchor updates for all tracked anchors.<br />
Anchors are automatically added when created via [trackAnchor] or [createAnchor].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-localizationrequestrecords"></span><span class="ctoken-line"><span class="ctoken class-name">localizationRequestRecords</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/kotlinx.coroutines.flow.-flow" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Flow</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2LocalizationRequestRecord/" title="Diagnostics record describing a VPS2 localization request....">Vps2LocalizationRequestRecord</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Flow of localization request records.<br />
Each emission is a single [Vps2LocalizationRequestRecord] from the latest batch.<br />
Records are emitted only when new ones are available.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-localizationupdates"></span><span class="ctoken-line"><span class="ctoken class-name">localizationUpdates</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/kotlinx.coroutines.flow.-flow" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Flow</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Localization/" title="Spatial mapping between the device&#39;s AR coordinate space and real-world...">Vps2Localization</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Flow of the latest localization snapshot.<br />
This is useful for consumers that want to reactively drive UI or downstream computations<br />
without manually polling [getLatestLocalization].
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
<td><span id="function-anchoridtostring"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.anchorIdToString/" title="Convert a VPS2 anchor id (32-byte ASCII hex) to a printable string.">anchorIdToString</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span></span></td>
<td><div class="ctoken comment">
Convert a VPS2 anchor id (32-byte ASCII hex) to a printable string.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-configure"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.configure/" title="Configure VPS2. Must be called while stopped.">configure</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Configure VPS2. Must be called while stopped.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-createanchor"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.createAnchor/" title="Create and start tracking an anchor at the specified pose.">createAnchor</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UUID</a></span></span></td>
<td><div class="ctoken comment">
Create and start tracking an anchor at the specified pose.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-featurestatus"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.featureStatus/" title="Browse to featureStatus">featureStatus</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.FeatureStatus/" title="Browse to FeatureStatus">FeatureStatus</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getanchorpayload"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.getAnchorPayload/" title="Gets the payload data of a specified anchor....">getAnchorPayload</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Gets the payload data of a specified anchor.<br />
The payload encodes the data needed to localize an anchor across multiple devices or sessions.<br />
It can be shared or stored for later use with [trackAnchor].
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getanchorupdate"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.getAnchorUpdate/" title="Gets the latest tracking update for a specified anchor.">getAnchorUpdate</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AnchorUpdate/" title="Contains the latest tracking information for a VPS anchor....">AnchorUpdate</a></span></span></td>
<td><div class="ctoken comment">
Gets the latest tracking update for a specified anchor.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getdevicegeolocation"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.getDeviceGeolocation/" title="Get the geolocation of the device&#39;s last known camera pose.">getDeviceGeolocation</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2GeolocationData/" title="Geolocation data from VPS2 localization with accuracy information.">Vps2GeolocationData</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Get the geolocation of the device's last known camera pose.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getlatestlocalization"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.getLatestLocalization/" title="Gets the most recent VPS2 localization result....">getLatestLocalization</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Localization/" title="Spatial mapping between the device&#39;s AR coordinate space and real-world...">Vps2Localization</a></span></span></td>
<td><div class="ctoken comment">
Gets the most recent VPS2 localization result.<br />
The returned localization contains the spatial mapping between<br />
the device's AR coordinate space and real-world geolocation.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getlatestlocalizationrequestrecords"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.getLatestLocalizationRequestRecords/" title="Get diagnostic localization request records since the last call.">getLatestLocalizationRequestRecords</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-list" target="_blank" rel="noopener noreferrer" title="Opens an external reference">List</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2LocalizationRequestRecord/" title="Diagnostics record describing a VPS2 localization request....">Vps2LocalizationRequestRecord</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Get diagnostic localization request records since the last call.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getpose"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.getPose/" title="Convert a geolocation to an AR pose using a localization snapshot.">getPose</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developers.google.com/ar/reference/java/com/google/ar/core/Pose" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Pose</a></span></span></td>
<td><div class="ctoken comment">
Convert a geolocation to an AR pose using a localization snapshot.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-gettrackedanchors"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.getTrackedAnchors/" title="Get the set of all tracked anchors.">getTrackedAnchors</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-set" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Set</a></span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UUID</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
Get the set of all tracked anchors.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-ondestroy"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.onDestroy/" title="Browse to onDestroy">onDestroy</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-oninit"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.onInit/" title="Browse to onInit">onInit</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-removeanchor"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.removeAnchor/" title="Stop tracking an anchor.">removeAnchor</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Stop tracking an anchor.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-start"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.start/" title="Browse to start">start</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-stop"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.stop/" title="Browse to stop">stop</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-trackanchor"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.trackAnchor/" title="Start tracking an anchor specified by a base64 payload.">trackAnchor</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UUID</a></span></span></td>
<td><div class="ctoken comment">
Start tracking an anchor specified by a base64 payload.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
