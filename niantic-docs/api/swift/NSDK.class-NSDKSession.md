---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKSession/
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

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") 

</div>

<div class="api-title">

#  NSDKSession

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">NSDKSession</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

The main entry point for the NSDK (Native SDK) framework. `NSDKSession` provides the core functionality for AR applications, managing the lifecycle of NSDK features and serving as a factory for specialized sessions like VPS2, scanning, and mapping. This class handles frame data processing, configuration management, and resource cleanup.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Use `NSDKSession` to:

- Initialize the NSDK with auth tokens or a configuration file
- Send camera frame data for processing
- Create specialized feature sessions (VPS2, Scanning, Mapping)
- Query required input data formats
- Manage the lifecycle of NSDK resources

## Example Usage<a href="#example-usage" class="hash-link" aria-label="Direct link to Example Usage" title="Direct link to Example Usage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
// Initialize with tokens
let session = NSDKSession(accessToken: "access-token", refreshToken: "refresh-token")
// Create a VPS2 session for localization
let vps2Session = session.createVps2Session()
// Send frame data during AR session
let status = session.sendFrame(frameData)
```

</div>

</div>

------------------------------------------------------------------------

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

### Constructor<a href="#constructor" class="hash-link" aria-label="Direct link to Constructor" title="Direct link to Constructor">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken keyword">convenience</span><span class="ctoken plain"> </span><span class="ctoken keyword">init</span><span class="ctoken plain">?(</span><span class="ctoken plain">withConfig</span><span class="ctoken plain"> </span><span class="ctoken plain">config</span><span class="ctoken plain">: </span><span class="ctoken class-name">[Configuration](https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.struct-Configuration/ "Configuration settings for initializing an NSDK session....")</span><span class="ctoken plain">)</span></span>

</div>

#### Summary<a href="#summary-1" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Creates a new NSDK session with a Configuration object.\
Use this initializer for fine-grained control over NSDK configuration

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A new NSDK session, or `nil` if configuration is invalid

</div>

#### Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let config = Configuration()
// Configure settings...
if let session = NSDKSession(withConfig: config) {
    // Session created successfully
}
```

</div>

</div>

------------------------------------------------------------------------

### Overload 1<a href="#overload-1" class="hash-link" aria-label="Direct link to Overload 1" title="Direct link to Overload 1">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken keyword">convenience</span><span class="ctoken plain"> </span><span class="ctoken keyword">init</span><span class="ctoken plain">?(</span><span class="ctoken plain">withJson</span><span class="ctoken plain"> </span><span class="ctoken plain">configFilePath</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">, </span><span class="ctoken plain">logCallback</span><span class="ctoken plain">: </span><span class="ctoken class-name">[NSDKLogCallback](https://www.nianticspatial.com/docs/api/swift/NSDK.interface-NSDKLogCallback/ "Protocol for receiving log messages from NSDK....")</span><span class="ctoken plain">? = nil)</span></span>

</div>

#### Summary<a href="#summary-2" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Creates a new NSDK session from a JSON configuration file.\
Use this initializer for fine-grained control over NSDK configuration\
or when loading settings from a configuration file.

</div>

#### Returns<a href="#returns-1" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

A new NSDK session, or `nil` if configuration loading fails

</div>

#### Example<a href="#example-1" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
if let session = NSDKSession(withJson: "/path/to/config.json") {
    // Session created successfully
} else {
    // Failed to load configuration
}
```

</div>

</div>

------------------------------------------------------------------------

### Overload 2<a href="#overload-2" class="hash-link" aria-label="Direct link to Overload 2" title="Direct link to Overload 2">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken keyword">convenience</span><span class="ctoken plain"> </span><span class="ctoken keyword">init</span><span class="ctoken plain">(</span><span class="ctoken plain">accessToken</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">, </span><span class="ctoken plain">useLidar</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain"> = true, </span><span class="ctoken plain">pathConfig</span><span class="ctoken plain">: </span><span class="ctoken class-name">[NSDKPathConfig](https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKPathConfig/ "Browse to NSDKPathConfig")</span><span class="ctoken plain">? = nil, </span><span class="ctoken plain">logCallback</span><span class="ctoken plain">: </span><span class="ctoken class-name">[NSDKLogCallback](https://www.nianticspatial.com/docs/api/swift/NSDK.interface-NSDKLogCallback/ "Protocol for receiving log messages from NSDK....")</span><span class="ctoken plain">? = nil)</span></span>

</div>

#### Summary<a href="#summary-3" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Convenience initializer that accepts an access token.\
The token is sanitized and passed to native AuthManagerApi immediately via creation call.

</div>

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
<td><span id="property-currentframe"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">currentFrame</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKFrameData/" title="A complete frame of data captured from an AR session....">NSDKFrameData</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-datasource"></span><span class="ctoken-line"><span class="ctoken keyword">weak</span><span class="ctoken plain"> </span><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">dataSource</span></span></td>
<td><span class="ctoken-line"><span class="ctoken plain"> (</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.interface-NSDKSessionDataSource/" title="Provides synchronous, pull-based access to the latest available sensor data...">NSDKSessionDataSource</a></span><span class="ctoken plain">)?</span></span></td>
<td><div class="ctoken comment">
The component supplying the session with sensory data.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-isauthorized"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">isAuthorized</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
Returns true if a valid, non-expired access token is available.<br />
Use this to check if features requiring authentication can be used.<br />
If a feature returns an auth error, poll this property until it returns true<br />
before retrying.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-nativehandle"></span><span class="ctoken-line"><span class="ctoken keyword">let</span><span class="ctoken plain"> </span><span class="ctoken class-name">nativeHandle</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">NSDKHandle</span></span></td>
<td><div class="ctoken comment">
The native handle to the underlying NSDK C API instance.<br />
This handle is used internally to communicate with the native NSDK library<br />
and should not be modified directly by application code.
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
<td><span id="method-acquiredepthsession"></span><span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-acquireDepthSession/" title="Returns the shared depth session, creating it on first call....">acquireDepthSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKDepthSession/" title="Depth feature session for NSDK with Combine publisher support....">NSDKDepthSession</a></span></span></td>
<td><div class="ctoken comment">
Returns the shared depth session, creating it on first call.<br />
Subsequent calls return the same instance. The session is inactive until <code>start()</code> is<br />
called. <code>NSDKSession.update()</code> will call <code>update()</code> on it automatically each frame once<br />
it is started.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-acquiredevicemappingsession"></span><span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-acquireDeviceMappingSession/" title="Returns the shared device mapping session, creating it on first call....">acquireDeviceMappingSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKDeviceMappingSession/" title="A session for creating VPS maps from AR data on the local device, with Combine publisher support....">NSDKDeviceMappingSession</a></span></span></td>
<td><div class="ctoken comment">
Returns the shared device mapping session, creating it on first call.<br />
Subsequent calls return the same instance. The session is inactive until <code>start()</code> is<br />
called. <code>NSDKSession.update()</code> will call <code>update()</code> on it automatically each frame once<br />
it is started.<br />
The session holds a reference to the shared <code>NSDKMapStorage</code>, which is also<br />
created on first call and reused on subsequent calls.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-acquiremapstorage"></span><span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-acquireMapStorage/" title="Browse to acquireMapStorage">acquireMapStorage</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKMapStorage/" title="A storage system for managing device-generated maps....">NSDKMapStorage</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-acquiremeshdownloader"></span><span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-acquireMeshDownloader/" title="Creates a new Mesh Downloader instance.">acquireMeshDownloader</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKMeshDownloader/" title="A session-scoped utility for downloading mesh geometry associated with VPS locations.">NSDKMeshDownloader</a></span></span></td>
<td><div class="ctoken comment">
Creates a new Mesh Downloader instance.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-acquiremeshingsession"></span><span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-acquireMeshingSession/" title="Returns the shared meshing session, creating it on first call....">acquireMeshingSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKMeshingSession/" title="A session for real-time 3D mesh generation from AR camera frames, with Combine publisher support....">NSDKMeshingSession</a></span></span></td>
<td><div class="ctoken comment">
Returns the shared meshing session, creating it on first call.<br />
Subsequent calls return the same instance. The session is inactive until <code>start()</code> is<br />
called. <code>NSDKSession.update()</code> will call <code>update()</code> on it automatically each frame once<br />
it is started.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-acquirerecordingexporter"></span><span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-acquireRecordingExporter/" title="Creates a new Recording Exporter session....">acquireRecordingExporter</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKRecordingExporter/" title="A session for exporting scan recordings to various formats....">NSDKRecordingExporter</a></span></span></td>
<td><div class="ctoken comment">
Creates a new Recording Exporter session.<br />
Recording Export enables the conversion and export of saved scan recordings<br />
to various formats for external processing or sharing. This session manages<br />
the export workflow from scan selection through format conversion and output.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-acquirescanningsession"></span><span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-acquireScanningSession/" title="Returns the shared Scanning session, creating it on first call....">acquireScanningSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKScanningSession/" title="A session for 3D scanning and visualization with Combine publisher support....">NSDKScanningSession</a></span></span></td>
<td><div class="ctoken comment">
Returns the shared Scanning session, creating it on first call.<br />
Subsequent calls return the same instance. The session is inactive until <code>start()</code> is<br />
called. <code>NSDKSession.update()</code> will call <code>update()</code> on it automatically each frame once<br />
it is started.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-acquirescenesegmentationsession"></span><span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-acquireSceneSegmentationSession/" title="Returns the shared scene segmentation session, creating it on first call....">acquireSceneSegmentationSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKSceneSegmentationSession/" title="A session for semantic segmentation and environmental understanding with Combine publisher support....">NSDKSceneSegmentationSession</a></span></span></td>
<td><div class="ctoken comment">
Returns the shared scene segmentation session, creating it on first call.<br />
Subsequent calls return the same instance. The session is inactive until <code>start()</code> is<br />
called. <code>NSDKSession.update()</code> will call <code>update()</code> on it automatically each frame once<br />
it is started.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-acquiresitessession"></span><span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-acquireSitesSession/" title="Browse to acquireSitesSession">acquireSitesSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKSitesSession/" title="Browse to NSDKSitesSession">NSDKSitesSession</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-acquirevps2session"></span><span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-acquireVps2Session/" title="Returns the shared VPS2 session, creating it on first call....">acquireVps2Session</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKVps2Session/" title="A session for VPS2 (Visual Positioning System) localization with Combine publisher support....">NSDKVps2Session</a></span></span></td>
<td><div class="ctoken comment">
Returns the shared VPS2 session, creating it on first call.<br />
Subsequent calls return the same instance. The session is inactive until <code>start()</code> is<br />
called. <code>NSDKSession.update()</code> will call <code>update()</code> on it automatically each frame once<br />
it is started.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-destroy"></span><span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-destroy/" title="Destroys a specific session, stopping it and releasing its native resources....">destroy</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Destroys a specific session, stopping it and releasing its native resources.<br />
After this call the session is removed from <code>disposables</code> and must not be used again.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-destroyall"></span><span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-destroyAll/" title="Destroys all sessions at once, releasing all native resources....">destroyAll</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Destroys all sessions at once, releasing all native resources.<br />
Use this on reset or when the <code>NSDKSession</code> is no longer needed.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getaccessauthinfo"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-getAccessAuthInfo/" title="Gets access token authentication information....">getAccessAuthInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AuthInfo/" title="Authentication information containing token claims....">AuthInfo</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Gets access token authentication information.<br />
Returns authentication information containing information about the current access token.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getrefreshauthinfo"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-getRefreshAuthInfo/" title="Gets refresh token authentication information....">getRefreshAuthInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AuthInfo/" title="Authentication information containing token claims....">AuthInfo</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Gets refresh token authentication information.<br />
Returns authentication information containing information about the current refresh token.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-logout"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-logout/" title="Clears cached auth tokens from persistent storage without requiring an NSDK session....">logout</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Clears cached auth tokens from persistent storage without requiring an NSDK session.<br />
This is the preferred logout path. It can be called before NSDK is initialized or after<br />
it has been destroyed. Any running session will pick up the cleared tokens on its next<br />
reconciliation cycle.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-setaccesstoken"></span><span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-setAccessToken/" title="Sets the access token on native (routed through AuthManagerApi via C-ABI)....">setAccessToken</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Sets the access token on native (routed through AuthManagerApi via C-ABI).<br />
Empty or whitespace-only tokens are ignored by native.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-setagelevel"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-setAgeLevel/" title="Sets the age level for the NSDK session....">setAgeLevel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Sets the age level for the NSDK session.<br />
This method sets the age classification for the user
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-setcallbackloglevel"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-setCallbackLogLevel/" title="Sets the log level for callback logging.">setCallbackLogLevel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Sets the log level for callback logging.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-setfileloglevel"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-setFileLogLevel/" title="Sets the log level for file logging.">setFileLogLevel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Sets the log level for file logging.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-setstdoutloglevel"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-setStdoutLogLevel/" title="Sets the log level for standard output logging.">setStdoutLogLevel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Sets the log level for standard output logging.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-update"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-update/" title="Collects the latest requested sensor inputs from the assigned...">update</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Collects the latest requested sensor inputs from the assigned<br />
<code>NsdkSessionDataSource</code> and submits a single frame for processing.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-version"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-version/" title="Retrieves the NSDK version string.">version</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span></span></td>
<td><div class="ctoken comment">
Retrieves the NSDK version string.
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
<td><span id="struct-cloudenvconfig"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.struct-CloudEnvConfig/" title="Browse to CloudEnvConfig">CloudEnvConfig</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.struct-CloudEnvConfig/" title="Browse to CloudEnvConfig">CloudEnvConfig</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-configuration"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.struct-Configuration/" title="Configuration settings for initializing an NSDK session....">Configuration</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.struct-Configuration/" title="Configuration settings for initializing an NSDK session....">Configuration</a></span></span></td>
<td><div class="ctoken comment">
Configuration settings for initializing an NSDK session.<br />
This struct encapsulates various configuration options<br />
including device info, cloud environment settings, user credentials,<br />
and logging preferences.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-deviceinfo"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.struct-DeviceInfo/" title="Browse to DeviceInfo">DeviceInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.struct-DeviceInfo/" title="Browse to DeviceInfo">DeviceInfo</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-userconfig"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.struct-UserConfig/" title="Browse to UserConfig">UserConfig</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.struct-UserConfig/" title="Browse to UserConfig">UserConfig</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
