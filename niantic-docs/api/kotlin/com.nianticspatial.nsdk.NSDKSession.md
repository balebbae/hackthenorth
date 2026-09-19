---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKSession/
title: NSDKSession
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

#  NSDKSession

<div class="api-extends">

↳ extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Closeable.html" target="_blank" rel="noopener noreferrer" title="Closeable">Closeable</a> 

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">NSDKSession</span><span class="ctoken plain"> </span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Creates a new NSDK instance with auth tokens or a configuration file. This is the primary entry point for initializing NSDK functionality. You must call this before using any other NSDK features. Only one \[NSDKSession\] may be active at a time. Creating a second instance while one is active will throw \[IllegalStateException\]. Call \[close\] on the existing session before creating a new one.

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
<td><span id="property-datasource"></span><span class="ctoken-line"><span class="ctoken class-name">dataSource</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NsdkSessionDataSource/" title="Provides synchronous, pull-based access to the latest available sensor data...">NsdkSessionDataSource</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
The data source that supplies sensor samples to [update].<br />
Assign a [NsdkSessionDataSource] before calling [update]. Set to null to release it.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-depthsession"></span><span class="ctoken-line"><span class="ctoken class-name">depthSession</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.depth.DepthSession/" title="Creates a Depth session....">DepthSession</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-isauthorized"></span><span class="ctoken-line"><span class="ctoken class-name">isAuthorized</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Boolean</a></span></span></td>
<td><div class="ctoken comment">
Indicates whether the ARDK session is authorized with valid tokens.<br />
Use this property to check if authentication is complete before making<br />
API calls that require authorization. You can poll this property to wait<br />
for token refresh to complete.<br />
Example usage:
</div>
<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">
<div class="codeBlockContent_QJqH">
<pre class="prism-code language-kotlin codeBlock_bY9V thin-scrollbar" tabindex="0" style="color:#393A34;background-color:#f6f8fa"><code>// Wait for authorization before making API calls
while (!ardkSession.isAuthorized) {
delay(1000)
}
// Now safe to make authorized API calls</code></pre>
</div>
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-mapping"></span><span class="ctoken-line"><span class="ctoken class-name">mapping</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.DeviceMappingSession/" title="A session for locally creating VPS maps from AR data....">DeviceMappingSession</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-mapstore"></span><span class="ctoken-line"><span class="ctoken class-name">mapStore</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mapping.MappingStorageSession/" title="Browse to MappingStorageSession">MappingStorageSession</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-meshdownload"></span><span class="ctoken-line"><span class="ctoken class-name">meshDownload</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mesh.MeshDownloaderSession/" title="Creates a Mesh Downloader instance....">MeshDownloaderSession</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-meshingsession"></span><span class="ctoken-line"><span class="ctoken class-name">meshingSession</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.mesh.MeshingSession/" title="A session for real-time 3D mesh generation from AR data....">MeshingSession</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-recordingexporter"></span><span class="ctoken-line"><span class="ctoken class-name">recordingExporter</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.recording.RecordingExporter/" title="Creates a Recording Exporter instance for exporting saved scans....">RecordingExporter</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-scanning"></span><span class="ctoken-line"><span class="ctoken class-name">scanning</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession/" title="A session for 3D scanning and visualization functionality....">ScanningSession</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-scenesegmentation"></span><span class="ctoken-line"><span class="ctoken class-name">sceneSegmentation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.awareness.scenesegmentation.SceneSegmentationSession/" title="Creates a SceneSegmentation session for semantic understanding....">SceneSegmentationSession</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-sites"></span><span class="ctoken-line"><span class="ctoken class-name">sites</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.sites.SitesSession/" title="A session for interacting with the Sites Manager service....">SitesSession</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-vps2"></span><span class="ctoken-line"><span class="ctoken class-name">vps2</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session/" title="A session for VPS2 localization.">Vps2Session</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
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
<td><span id="function-close"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKSession.close/" title="Destroys an NSDK instance and any remaining opened feature sessions...">close</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Destroys an NSDK instance and any remaining opened feature sessions<br />
and frees associated resources.<br />
Must be called when the session is no longer needed. Failing to call [close] will prevent<br />
a new [NSDKSession] from being created until the garbage collector collects this instance.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-disabletelemetry"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKSession.disableTelemetry/" title="Disables telemetry collection for this process....">disableTelemetry</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Disables telemetry collection for this process.<br />
Clears any buffered telemetry events and stops accepting new ones.<br />
This is a process-wide operation.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getaccessauthinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKSession.getAccessAuthInfo/" title="Gets access token authentication information....">getAccessAuthInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AuthInfo/" title="Authentication information containing token claims....">AuthInfo</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Gets access token authentication information.<br />
Returns authentication information containing information about the current access token.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getrefreshauthinfo"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKSession.getRefreshAuthInfo/" title="Gets refresh token authentication information....">getRefreshAuthInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.AuthInfo/" title="Authentication information containing token claims....">AuthInfo</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Gets refresh token authentication information.<br />
Returns authentication information containing information about the current refresh token.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getrequesteddataformats"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKSession.getRequestedDataFormats/" title="Gets the data formats that NSDK requires for processing....">getRequestedDataFormats</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span></span></td>
<td><div class="ctoken comment">
Gets the data formats that NSDK requires for processing.<br />
This function returns a bitmask indicating which types of input data<br />
(camera frames, depth, IMU, etc.) NSDK needs for optimal performance.<br />
Use this to configure your data capture pipeline accordingly.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-getversion"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKSession.getVersion/" title="Returns the NSDK version string from the native library.">getVersion</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span></span></td>
<td><div class="ctoken comment">
Returns the NSDK version string from the native library.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-sendframe"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKSession.sendFrame/" title="Browse to sendFrame">sendFrame</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-setaccesstoken"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKSession.setAccessToken/" title="Set the access token at runtime. Invalid/empty tokens are ignored by native.">setAccessToken</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Set the access token at runtime. Invalid/empty tokens are ignored by native.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-setagelevel"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKSession.setAgeLevel/" title="Sets the age level for the NSDK session....">setAgeLevel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Sets the age level for the NSDK session.<br />
This method sets the age classification for the user
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-setcallbackloglevel"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKSession.setCallbackLogLevel/" title="Sets the log level for callback logs....">setCallbackLogLevel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Sets the log level for callback logs.<br />
This function filters out logs of less severity than the specified level<br />
for the callback logger.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-setfileloglevel"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKSession.setFileLogLevel/" title="Sets the log level for file logs....">setFileLogLevel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Sets the log level for file logs.<br />
This function filters out logs of less severity than the specified level<br />
for the file logger.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-setstdoutloglevel"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKSession.setStdoutLogLevel/" title="Sets the log level for stdout logs....">setStdoutLogLevel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Sets the log level for stdout logs.<br />
This function filters out logs of less severity than the specified level<br />
for the stdout logger.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-update"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKSession.update/" title="Pulls sensor samples from [dataSource] and submits a frame for native processing....">update</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Pulls sensor samples from [dataSource] and submits a frame for native processing.<br />
No-op if [dataSource] is null or not ready. Call once per camera frame.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
