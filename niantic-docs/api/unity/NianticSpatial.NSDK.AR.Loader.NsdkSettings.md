---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Loader.NsdkSettings/
title: NsdkSettings
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Loader](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Loader/ "NianticSpatial.NSDK.AR.Loader") 

</div>

<div class="api-title">

#  NsdkSettings

<div class="api-extends">

↳ extends UnityEngine.ScriptableObject

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">partial</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">NsdkSettings</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">ScriptableObject</a></span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Build time settings for NSDK AR. These are serialized to an asset file and can only be altered via the Unity Inspector window.

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
<td><span id="property-accessexpiresat"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">AccessExpiresAt</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
Time when the current runtime access token expires
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-accesstoken"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">AccessToken</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
The effective access token. Returns the access token override if set,<br />
otherwise the developer auth access token.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-accesstokenoverride"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">AccessTokenOverride</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
An access token that takes priority over developer authentication when set.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-authenvironment"></span><span class="ctoken-line"><span class="ctoken class-name">AuthEnvironment</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Auth.AuthEnvironmentType/" title="The type of environment to use for authentication (selects which portal and identity server to use)">AuthEnvironmentType</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-deviceplaybacksettings"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">DevicePlaybackSettings</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Loader.INsdkPlaybackSettings/" title="Browse to INsdkPlaybackSettings">INsdkPlaybackSettings</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-editorplaybacksettings"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">EditorPlaybackSettings</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Loader.INsdkPlaybackSettings/" title="Browse to INsdkPlaybackSettings">INsdkPlaybackSettings</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-filensdkloglevel"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">FileNsdkLogLevel</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Logging.LogLevel/" title="Browse to LogLevel">LogLevel</a></span></span></td>
<td><div class="ctoken comment">
The highest log level to print for a file logger
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-instance"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">Instance</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">NsdkSettings</span></span></td>
<td><div class="ctoken comment">
Accessor to NSDK settings asset instance.<br />
THIS SHOULD ONLY BE USED IN SPECIFIC SITUATIONS:<br />
1) Editor classes that need to read/write values to the asset<br />
2) By NsdkLoaderHelper to initialize the runtime settings on application load<br />
All other code should use NsdkLoaderHelper.ActiveSettings to get the settings,<br />
otherwise it will get the asset instance's values instead of the runtime instance's, which<br />
may be different in tests or if the dev has modified settings at runtime.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-locationandcompassdatasource"></span><span class="ctoken-line"><span class="ctoken class-name">LocationAndCompassDataSource</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.LocationDataSource/" title="Browse to LocationDataSource">LocationDataSource</a></span></span></td>
<td><div class="ctoken comment">
Source of location and compass data fetched from the NianticSpatial.NSDK.AR.Input APIs
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-loopinfinitely"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">LoopInfinitely</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-nsdksimulationparams"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">NsdkSimulationParams</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Loader.NsdkSimulationParams/" title="Browse to NsdkSimulationParams">NsdkSimulationParams</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-playbackdatasetpath"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">PlaybackDatasetPath</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-preferlidarifavailable"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">PreferLidarIfAvailable</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
When enabled, LiDAR depth will be used instead of NSDK depth on devices where LiDAR is available.<br />
Features unique to the NsdkOcclusionExtension cannot be used.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-refreshexpiresat"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">RefreshExpiresAt</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
Time when the current runtime refresh token expires
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-refreshtoken"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">RefreshToken</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
The current runtime refresh token
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-runmanually"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">RunManually</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-spoofcompassinfo"></span><span class="ctoken-line"><span class="ctoken class-name">SpoofCompassInfo</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SpoofCompassInfo/" title="Browse to SpoofCompassInfo">SpoofCompassInfo</a></span></span></td>
<td><div class="ctoken comment">
Values returned by compass service when in Spoof mode
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-spooflocationinfo"></span><span class="ctoken-line"><span class="ctoken class-name">SpoofLocationInfo</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.SpoofLocationInfo/" title="Browse to SpoofLocationInfo">SpoofLocationInfo</a></span></span></td>
<td><div class="ctoken comment">
Values returned by location service when in Spoof mode
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-stdoutnsdkloglevel"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">StdOutNsdkLogLevel</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Logging.LogLevel/" title="Browse to LogLevel">LogLevel</a></span></span></td>
<td><div class="ctoken comment">
The highest log level to print for the stdout logger - typically for internal testing. Keep this off unless<br />
you know what you are looking for
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-unitynsdkloglevel"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">UnityNsdkLogLevel</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Utilities.Logging.LogLevel/" title="Browse to LogLevel">LogLevel</a></span></span></td>
<td><div class="ctoken comment">
The highest log level to print for Unity logger
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-usedeveloperauthentication"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">UseDeveloperAuthentication</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-usensdkdepth"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">UseNsdkDepth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
When enabled, NSDK's depth and occlusion features can be used via ARFoundation. Additional occlusion<br />
features unique to NSDK can be configured in the NsdkOcclusionExtension component.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-usensdkdevicemapping"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">UseNsdkDeviceMapping</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
When enabled, NSDK's device mapping features can be used.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-usensdkmeshing"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">UseNsdkMeshing</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
When enabled, NSDK's meshing features can be used via ARFoundation. Additional mesh features unique<br />
to NSDK can be configured in the LightshipMeshingExtension component.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-usensdkscanning"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">UseNsdkScanning</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
When enabled, NSDK's scanning features can be used.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-usensdkscenesegmentation"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">UseNsdkSceneSegmentation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
When enabled, NSDK's scene segmentation features can be used.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-usensdkvps2"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">UseNsdkVps2</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
When enabled, NSDK's VPS2 feature can be used.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-useplayback"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">UsePlayback</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

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
<td><span id="field-buildsettingskey"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">BuildSettingsKey</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="field-settingskey"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">SettingsKey</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment deemphasize">
-
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
<td><span id="method-updateaccess"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Loader.NsdkSettings.UpdateAccess/" title="Browse to UpdateAccess">UpdateAccess</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
