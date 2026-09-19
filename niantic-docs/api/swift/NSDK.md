---
source: https://www.nianticspatial.com/docs/api/swift/NSDK/
title: NSDK
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") 

</div>

<div class="api-title">

#  NSDK

</div>

------------------------------------------------------------------------

## Type Aliases<a href="#type-aliases" class="hash-link" aria-label="Direct link to Type Aliases" title="Direct link to Type Aliases">​</a>

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
<td><span id="type alias-networkrequestid"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name">NetworkRequestId</span><span class="ctoken plain"> = </span><span class="ctoken class-name">ARDK_NetworkRequestId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">ARDK_NetworkRequestId</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="type alias-nsdkcameraextrinsics"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name">NSDKCameraExtrinsics</span><span class="ctoken plain"> = </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float4x4</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//simd/simd_float4x4" target="_blank" rel="noopener noreferrer" title="Opens an external reference">simd_float4x4</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="type alias-nsdkcameraintrinsics"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name">NSDKCameraIntrinsics</span><span class="ctoken plain"> = </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKFrameData/" title="A complete frame of data captured from an AR session....">NSDKFrameData</a></span><span class="ctoken plain">.</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKFrameData.struct-CameraIntrinsics/" title="Camera intrinsic parameters for geometric calibration....">CameraIntrinsics</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKFrameData/" title="A complete frame of data captured from an AR session....">NSDKFrameData</a></span><span class="ctoken plain">.</span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKFrameData.struct-CameraIntrinsics/" title="Camera intrinsic parameters for geometric calibration....">CameraIntrinsics</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="type alias-nsdkhandle"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name">NSDKHandle</span><span class="ctoken plain"> = </span><span class="ctoken class-name">ARDK_Handle</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">ARDK_Handle</span></span></td>
<td><div class="ctoken comment">
A type alias for the native NSDK handle used to interface with the underlying C API.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="type alias-nsdksessiondatasource"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name">NsdkSessionDataSource</span><span class="ctoken plain"> = </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.interface-NSDKSessionDataSource/" title="Provides synchronous, pull-based access to the latest available sensor data...">NSDKSessionDataSource</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.interface-NSDKSessionDataSource/" title="Provides synchronous, pull-based access to the latest available sensor data...">NSDKSessionDataSource</a></span></span></td>
<td><div class="ctoken comment">
Type alias for API compatibility.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="type alias-nsdkvpsanchorid"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name">NSDKVpsAnchorId</span><span class="ctoken plain"> = </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Classes<a href="#classes" class="hash-link" aria-label="Direct link to Classes" title="Direct link to Classes">​</a>

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
<td><span id="class-assetresult"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-AssetResult/" title="Contains all the ``AssetInfo`` objects returned by a query to the Sites Manager service.">AssetResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-AssetResult/" title="Contains all the ``AssetInfo`` objects returned by a query to the Sites Manager service.">AssetResult</a></span></span></td>
<td><div class="ctoken comment">
Contains all the <code>AssetInfo</code> objects returned by a query to the Sites Manager service.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-awarenessimageresult"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-AwarenessImageResult/" title="Image-based awareness result containing an NSDKImage.">AwarenessImageResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-AwarenessImageResult/" title="Image-based awareness result containing an NSDKImage.">AwarenessImageResult</a></span></span></td>
<td><div class="ctoken comment">
Image-based awareness result containing an NSDKImage.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-awarenessresult"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-AwarenessResult/" title="Base class for awarness results such as depth and segmentation....">AwarenessResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-AwarenessResult/" title="Base class for awarness results such as depth and segmentation....">AwarenessResult</a></span></span></td>
<td><div class="ctoken comment">
Base class for awarness results such as depth and segmentation.<br />
Provides common properties like frame ID, timestamp, camera pose, and intrinsics.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-bundleplaybackdatasetloader"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-BundlePlaybackDatasetLoader/" title="A loader that retrieves playback dataset data from the app bundle....">BundlePlaybackDatasetLoader</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-BundlePlaybackDatasetLoader/" title="A loader that retrieves playback dataset data from the app bundle....">BundlePlaybackDatasetLoader</a></span></span></td>
<td><div class="ctoken comment">
A loader that retrieves playback dataset data from the app bundle.<br />
This is the default implementation for loading datasets from <code>Bundle.main</code>.<br />
Frame images and depth data are loaded on-demand when requested.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-dataresourceowner"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-DataResourceOwner/" title="Browse to DataResourceOwner">DataResourceOwner</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-DataResourceOwner/" title="Browse to DataResourceOwner">DataResourceOwner</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-defaultsessiondatasource"></span><span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-DefaultSessionDataSource/" title="Default iOS implementation of `NSDKSessionDataSource` backed by...">DefaultSessionDataSource</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-DefaultSessionDataSource/" title="Default iOS implementation of `NSDKSessionDataSource` backed by...">DefaultSessionDataSource</a></span></span></td>
<td><div class="ctoken comment">
Default iOS implementation of <code>NSDKSessionDataSource</code> backed by<br />
<code>ARSession</code> and <code>CLLocationManager</code>.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-depthresult"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-DepthResult/" title="Contains depth estimation results from the NSDK depth processing system.">DepthResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-DepthResult/" title="Contains depth estimation results from the NSDK depth processing system.">DepthResult</a></span></span></td>
<td><div class="ctoken comment">
Contains depth estimation results from the NSDK depth processing system.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-meshdata"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-MeshData/" title="Contains 3D mesh data for rendering and visualization....">MeshData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-MeshData/" title="Contains 3D mesh data for rendering and visualization....">MeshData</a></span></span></td>
<td><div class="ctoken comment">
Contains 3D mesh data for rendering and visualization.<br />
<code>MeshData</code> provides access to 3D mesh geometry including vertices, indices,<br />
normals, and texture coordinates.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-meshdownloaderresults"></span><span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-MeshDownloaderResults/" title="Contains the downloaded mesh geometry data for a VPS location....">MeshDownloaderResults</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-MeshDownloaderResults/" title="Contains the downloaded mesh geometry data for a VPS location....">MeshDownloaderResults</a></span></span></td>
<td><div class="ctoken comment">
Contains the downloaded mesh geometry data for a VPS location.<br />
This object holds an array of mesh results, where each result includes mesh geometry,<br />
texture data (if requested), and the transform matrix that positions the mesh in world space.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkcamera"></span><span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKCamera/" title="Single camera API for both modes. Holds either **ARCamera** (live) or **PlaybackCamera** (playback)...">NSDKCamera</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKCamera/" title="Single camera API for both modes. Holds either **ARCamera** (live) or **PlaybackCamera** (playback)...">NSDKCamera</a></span></span></td>
<td><div class="ctoken comment">
Single camera API for both modes. Holds either <strong>ARCamera</strong> (live) or <strong>PlaybackCamera</strong> (playback)<br />
and exposes transform, viewMatrix, projectionMatrix, viewportRect, etc.<br />
Relation to Apple AR: <strong>Wraps</strong> Apple's ARCamera in live mode; wraps our PlaybackCamera in playback.<br />
Callers use NSDKCamera and don't branch. Create via <code>NSDKCamera(arCamera:)</code> or <code>NSDKCamera(playbackCamera:)</code>.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkdepthsession"></span><span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKDepthSession/" title="Depth feature session for NSDK with Combine publisher support....">NSDKDepthSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKDepthSession/" title="Depth feature session for NSDK with Combine publisher support....">NSDKDepthSession</a></span></span></td>
<td><div class="ctoken comment">
Depth feature session for NSDK with Combine publisher support.<br />
Upon starting the depth session, NSDK will begin processing AR frames to generate depth data.<br />
The latest depth data can be retrieved using <code>latestDepth()</code>, and <code>latestImageParams()</code><br />
provides information to synchronize the depth image with camera frame.<br />
<code>$result</code> is refreshed automatically each frame by <code>NSDKSession.update()</code> while the session<br />
is active. Subscribe to it with Combine:
</div>
<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">
<div class="codeBlockContent_QJqH">
<pre class="prism-code language-swift codeBlock_bY9V thin-scrollbar" tabindex="0" style="color:#393A34;background-color:#f6f8fa"><code>depthSession.$result
    .compactMap { if case .success(let result) = $0 { return result } else { return nil } }
    .sink { result in ... }
    .store(in: &amp;cancellables)</code></pre>
</div>
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkdevicemappingsession"></span><span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKDeviceMappingSession/" title="A session for creating VPS maps from AR data on the local device, with Combine publisher support....">NSDKDeviceMappingSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKDeviceMappingSession/" title="A session for creating VPS maps from AR data on the local device, with Combine publisher support....">NSDKDeviceMappingSession</a></span></span></td>
<td><div class="ctoken comment">
A session for creating VPS maps from AR data on the local device, with Combine publisher support.<br />
The device mapping feature provides capabilities for locally building persistent maps that<br />
can be used for Visual Positioning System (VPS) localization. These maps capture the visual<br />
features and spatial structure of an environment.<br />
<code>$latestMapUpdate</code> is refreshed automatically each frame by <code>NSDKSession.update()</code> while the<br />
session is active. Subscribe to it with Combine:
</div>
<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">
<div class="codeBlockContent_QJqH">
<pre class="prism-code language-swift codeBlock_bY9V thin-scrollbar" tabindex="0" style="color:#393A34;background-color:#f6f8fa"><code>mappingSession.$latestMapUpdate
    .compactMap { $0 }
    .sink { mapUpdate in ... }
    .store(in: &amp;cancellables)</code></pre>
</div>
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkmapstorage"></span><span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKMapStorage/" title="A storage system for managing device-generated maps....">NSDKMapStorage</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKMapStorage/" title="A storage system for managing device-generated maps....">NSDKMapStorage</a></span></span></td>
<td><div class="ctoken comment">
A storage system for managing device-generated maps.<br />
The map storage feature provides capabilities for capturing, storing, and managing<br />
map data from AR sessions. This data can be persisted and used for Visual Positioning<br />
System (VPS) localization and map updates.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkmeshdownloader"></span><span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKMeshDownloader/" title="A session-scoped utility for downloading mesh geometry associated with VPS locations.">NSDKMeshDownloader</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKMeshDownloader/" title="A session-scoped utility for downloading mesh geometry associated with VPS locations.">NSDKMeshDownloader</a></span></span></td>
<td><div class="ctoken comment">
A session-scoped utility for downloading mesh geometry associated with VPS locations.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkmeshingsession"></span><span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKMeshingSession/" title="A session for real-time 3D mesh generation from AR camera frames, with Combine publisher support....">NSDKMeshingSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKMeshingSession/" title="A session for real-time 3D mesh generation from AR camera frames, with Combine publisher support....">NSDKMeshingSession</a></span></span></td>
<td><div class="ctoken comment">
A session for real-time 3D mesh generation from AR camera frames, with Combine publisher support.<br />
The meshing feature provides capabilities for processing AR session data and generating<br />
a triangle mesh representation of the physical environment in real-time. The mesh is<br />
divided into chunks that are individually tracked as they are inserted, updated, or removed.<br />
<code>meshUpdates</code> emits each frame a non-empty batch of chunk changes is available, driven by<br />
<code>NSDKSession.update()</code> while the session is active. Subscribe to it with Combine:
</div>
<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">
<div class="codeBlockContent_QJqH">
<pre class="prism-code language-swift codeBlock_bY9V thin-scrollbar" tabindex="0" style="color:#393A34;background-color:#f6f8fa"><code>meshingSession.meshUpdates
    .sink { updates in ... }
    .store(in: &amp;cancellables)</code></pre>
</div>
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkrecordingexporter"></span><span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKRecordingExporter/" title="A session for exporting scan recordings to various formats....">NSDKRecordingExporter</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKRecordingExporter/" title="A session for exporting scan recordings to various formats....">NSDKRecordingExporter</a></span></span></td>
<td><div class="ctoken comment">
A session for exporting scan recordings to various formats.<br />
<code>NSDKRecordingExporter</code> provides capabilities for converting saved scan data<br />
into recorderV2 format for use in Unity Playback or activating VPS.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkscanningsession"></span><span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKScanningSession/" title="A session for 3D scanning and visualization with Combine publisher support....">NSDKScanningSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKScanningSession/" title="A session for 3D scanning and visualization with Combine publisher support....">NSDKScanningSession</a></span></span></td>
<td><div class="ctoken comment">
A session for 3D scanning and visualization with Combine publisher support.<br />
The scanning feature provides capabilities for capturing, processing, and exporting<br />
3D scan data from AR sessions. Scans of a location can be processed by the Visual<br />
Positioning System's (VPS's) cloud services to enable VPS localization.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkscenesegmentationsession"></span><span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKSceneSegmentationSession/" title="A session for semantic segmentation and environmental understanding with Combine publisher support....">NSDKSceneSegmentationSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKSceneSegmentationSession/" title="A session for semantic segmentation and environmental understanding with Combine publisher support....">NSDKSceneSegmentationSession</a></span></span></td>
<td><div class="ctoken comment">
A session for semantic segmentation and environmental understanding with Combine publisher support.<br />
<code>NSDKSceneSegmentationSession</code> provides capabilities for understanding the semantic structure<br />
of the environment by classifying pixels into different object categories. This enables<br />
applications to make intelligent decisions based on environmental context.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdksession"></span><span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKSession/" title="The main entry point for the NSDK (Native SDK) framework....">NSDKSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKSession/" title="The main entry point for the NSDK (Native SDK) framework....">NSDKSession</a></span></span></td>
<td><div class="ctoken comment">
The main entry point for the NSDK (Native SDK) framework.<br />
<code>NSDKSession</code> provides the core functionality for AR applications, managing the lifecycle<br />
of NSDK features and serving as a factory for specialized sessions like VPS2, scanning, and mapping.<br />
This class handles frame data processing, configuration management, and resource cleanup.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdksitessession"></span><span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKSitesSession/" title="Browse to NSDKSitesSession">NSDKSitesSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKSitesSession/" title="Browse to NSDKSitesSession">NSDKSitesSession</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkview"></span><span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKView/" title="Single view for both live and playback. Subclasses **ARView**; holds either an **ARSession** (live)...">NSDKView</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKView/" title="Single view for both live and playback. Subclasses **ARView**; holds either an **ARSession** (live)...">NSDKView</a></span></span></td>
<td><div class="ctoken comment">
Single view for both live and playback. Subclasses <strong>ARView</strong>; holds either an <strong>ARSession</strong> (live)<br />
or <strong>PlaybackSession</strong> (playback) and exposes <code>sessionMode</code>, <code>getCamera()</code>, <code>setDelegate()</code>, <code>setup()</code>.<br />
Relation to Apple AR: <strong>Uses</strong> ARView; assigns either Apple's ARSession or our PlaybackSession to<br />
<code>self.session</code> so the view always has a "session." The app talks to NSDKView so it doesn't have to<br />
branch on live vs. playback for view, projection, viewport, or delegate callbacks.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-nsdkvps2session"></span><span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKVps2Session/" title="A session for VPS2 (Visual Positioning System) localization with Combine publisher support....">NSDKVps2Session</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKVps2Session/" title="A session for VPS2 (Visual Positioning System) localization with Combine publisher support....">NSDKVps2Session</a></span></span></td>
<td><div class="ctoken comment">
A session for VPS2 (Visual Positioning System) localization with Combine publisher support.<br />
<code>NSDKVps2Session</code> provides capabilities for localizing the device in the real world using<br />
VPS maps, universal localization, and anchor tracking. Anchors can be created at specific<br />
poses and tracked across sessions using payloads.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-organizationresult"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-OrganizationResult/" title="Contains all the ``OrganizationInfo`` objects returned by a query to the Sites Manager service.">OrganizationResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-OrganizationResult/" title="Contains all the ``OrganizationInfo`` objects returned by a query to the Sites Manager service.">OrganizationResult</a></span></span></td>
<td><div class="ctoken comment">
Contains all the <code>OrganizationInfo</code> objects returned by a query to the Sites Manager service.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-playbackbackgroundrenderer"></span><span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackBackgroundRenderer/" title="Browse to PlaybackBackgroundRenderer">PlaybackBackgroundRenderer</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackBackgroundRenderer/" title="Browse to PlaybackBackgroundRenderer">PlaybackBackgroundRenderer</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-playbackcamera"></span><span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackCamera/" title="Camera representation built from frame **metadata** (pose4x4, intrinsics, resolution). Exposes the same...">PlaybackCamera</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackCamera/" title="Camera representation built from frame **metadata** (pose4x4, intrinsics, resolution). Exposes the same...">PlaybackCamera</a></span></span></td>
<td><div class="ctoken comment">
Camera representation built from frame <strong>metadata</strong> (pose4x4, intrinsics, resolution). Exposes the same<br />
concepts as <strong>ARCamera</strong>: transform, viewMatrix, projectionMatrix, viewportRect, displayOrientedTransform.<br />
Relation to Apple AR: <strong>Stands in for</strong> ARCamera during playback. No Apple camera; we synthesize<br />
view/projection from recorded intrinsics and pose. Use <code>PlaybackFrame.camera</code> to obtain an instance.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-playbackdataset"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackDataset/" title="A dataset loaded from a capture JSON file containing frame metadata....">PlaybackDataset</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackDataset/" title="A dataset loaded from a capture JSON file containing frame metadata....">PlaybackDataset</a></span></span></td>
<td><div class="ctoken comment">
A dataset loaded from a capture JSON file containing frame metadata.<br />
This class uses on-demand loading for frame images and depth data.<br />
Only the currently requested frame is loaded into memory, reducing memory pressure<br />
for large datasets.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-playbackdatasetloader"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackDatasetLoader/" title="Base class for loading playback dataset data from various sources....">PlaybackDatasetLoader</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackDatasetLoader/" title="Base class for loading playback dataset data from various sources....">PlaybackDatasetLoader</a></span></span></td>
<td><div class="ctoken comment">
Base class for loading playback dataset data from various sources.<br />
This class provides a base implementation that must be subclassed. Subclasses must override<br />
<code>loadCaptureJSON()</code>, <code>loadImage(imageName:)</code>, <code>loadDepthData(depthFileName:)</code>, and<br />
<code>loadDepthConfidence(confidenceFileName:)</code> to provide concrete implementations.<br />
The loader uses on-demand loading - only the capture JSON is loaded upfront, and frame<br />
images/depth data are loaded when requested by <code>PlaybackDataset</code>.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-playbackrenderer"></span><span class="ctoken-line"><span class="ctoken plain">@</span><span class="ctoken plain">MainActor</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackRenderer/" title="Renders each playback frame: (1) draws the recorded camera image as the background, (2) **moves the...">PlaybackRenderer</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackRenderer/" title="Renders each playback frame: (1) draws the recorded camera image as the background, (2) **moves the...">PlaybackRenderer</a></span></span></td>
<td><div class="ctoken comment">
Renders each playback frame: (1) draws the recorded camera image as the background, (2) <strong>moves the<br />
RealityKit camera</strong> (pose + FOV) to match the playback frame. <strong>PlaybackSession</strong> holds an optional<br />
reference and calls <code>renderFrame(_:)</code> on the main queue for every new frame.<br />
Relation to Apple AR: <strong>Manipulates</strong> RealityKit—sets <code>arView.environment.background = .color(.clear)</code>,<br />
adds a <strong>PerspectiveCamera</strong> and <strong>AnchorEntity</strong>, and updates their transform and <code>fieldOfViewInDegrees</code><br />
every frame from PlaybackCamera. In playback, ARView's default camera is off; we drive the virtual camera.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-playbacksession"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackSession/" title="Drives playback. **Subclasses ARSession** so it can be assigned to `ARView.session` and the app can use...">PlaybackSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackSession/" title="Drives playback. **Subclasses ARSession** so it can be assigned to `ARView.session` and the app can use...">PlaybackSession</a></span></span></td>
<td><div class="ctoken comment">
Drives playback. <strong>Subclasses ARSession</strong> so it can be assigned to <code>ARView.session</code> and the app can use<br />
the same delegate pattern. Runs a loop on a background queue, builds <strong>PlaybackFrame</strong> per frame from<br />
the PlaybackDataset, dispatches to the main queue, and notifies the delegate and <strong>PlaybackRenderer</strong>.<br />
Relation to Apple AR: <strong>Replaces</strong> the behavior of ARSession (no real device frames); API-compatible so<br />
ARView and delegate code don't need to know it's playback.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-playbacksessiondatasource"></span><span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackSessionDataSource/" title="Browse to PlaybackSessionDataSource">PlaybackSessionDataSource</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-PlaybackSessionDataSource/" title="Browse to PlaybackSessionDataSource">PlaybackSessionDataSource</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-raycastbuffer"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-RaycastBuffer/" title="A read-only container for the raycast buffer information generated during scanning.">RaycastBuffer</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-RaycastBuffer/" title="A read-only container for the raycast buffer information generated during scanning.">RaycastBuffer</a></span></span></td>
<td><div class="ctoken comment">
A read-only container for the raycast buffer information generated during scanning.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-scenesegmentationresult"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-SceneSegmentationResult/" title="Contains semantic segmentation results from the NSDK scene segmentation processing system....">SceneSegmentationResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-SceneSegmentationResult/" title="Contains semantic segmentation results from the NSDK scene segmentation processing system....">SceneSegmentationResult</a></span></span></td>
<td><div class="ctoken comment">
Contains semantic segmentation results from the NSDK scene segmentation processing system.<br />
<code>SceneSegmentationResult</code> provides semantic understanding of the environment by classifying<br />
pixels in camera images into different object categories (e.g., sky, ground, buildings,<br />
people, vehicles). This enables applications to understand the scene structure and<br />
make intelligent decisions based on environmental context.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-siteassetsresult"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-SiteAssetsResult/" title="Contains the ``SiteAssetsInfo`` objects returned by a location-based sites query.">SiteAssetsResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-SiteAssetsResult/" title="Contains the ``SiteAssetsInfo`` objects returned by a location-based sites query.">SiteAssetsResult</a></span></span></td>
<td><div class="ctoken comment">
Contains the <code>SiteAssetsInfo</code> objects returned by a location-based sites query.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-siteresult"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-SiteResult/" title="Contains all the ``SiteInfo`` objects returned by a query to the Sites Manager service.">SiteResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-SiteResult/" title="Contains all the ``SiteInfo`` objects returned by a query to the Sites Manager service.">SiteResult</a></span></span></td>
<td><div class="ctoken comment">
Contains all the <code>SiteInfo</code> objects returned by a query to the Sites Manager service.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-sitesresult"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-SitesResult/" title="Base class for results returned by queries to the Sites Manager service.">SitesResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-SitesResult/" title="Base class for results returned by queries to the Sites Manager service.">SitesResult</a></span></span></td>
<td><div class="ctoken comment">
Base class for results returned by queries to the Sites Manager service.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-userresult"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-UserResult/" title="Contains the user information returned by a query to the Sites Manager service.">UserResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-UserResult/" title="Contains the user information returned by a query to the Sites Manager service.">UserResult</a></span></span></td>
<td><div class="ctoken comment">
Contains the user information returned by a query to the Sites Manager service.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-voxelbuffer"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-VoxelBuffer/" title="A read-only container for the voxel buffer information generated during scanning.">VoxelBuffer</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-VoxelBuffer/" title="A read-only container for the voxel buffer information generated during scanning.">VoxelBuffer</a></span></span></td>
<td><div class="ctoken comment">
A read-only container for the voxel buffer information generated during scanning.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-vps2heading"></span><span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-Vps2Heading/" title="A `CLHeading` subclass representing heading data computed by VPS2....">Vps2Heading</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-Vps2Heading/" title="A `CLHeading` subclass representing heading data computed by VPS2....">Vps2Heading</a></span></span></td>
<td><div class="ctoken comment">
A <code>CLHeading</code> subclass representing heading data computed by VPS2.<br />
VPS2 derives heading from visual-inertial localization rather than a physical magnetometer,<br />
so the raw magnetometer component values (<code>x</code>, <code>y</code>, <code>z</code>) are zero and not meaningful.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="class-vps2location"></span><span class="ctoken-line"><span class="ctoken keyword">final</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-Vps2Location/" title="A `CLLocation` subclass representing a position computed by VPS2....">Vps2Location</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.class-Vps2Location/" title="A `CLLocation` subclass representing a position computed by VPS2....">Vps2Location</a></span></span></td>
<td><div class="ctoken comment">
A <code>CLLocation</code> subclass representing a position computed by VPS2.<br />
MSL altitude is not available from VPS2 without a geoid model conversion, so <code>altitude</code><br />
always returns <code>-1</code>. Use <code>ellipsoidalAltitude</code> for the WGS84 height computed by VPS2, and<br />
<code>verticalAccuracy</code> (≥ 0) for its precision.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Protocols<a href="#protocols" class="hash-link" aria-label="Direct link to Protocols" title="Direct link to Protocols">​</a>

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
<td><span id="protocol-nsdkfeaturesession"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.interface-NSDKFeatureSession/" title="A protocol that defines the common lifecycle and configuration interface for NSDK feature sessions.">NSDKFeatureSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.interface-NSDKFeatureSession/" title="A protocol that defines the common lifecycle and configuration interface for NSDK feature sessions.">NSDKFeatureSession</a></span></span></td>
<td><div class="ctoken comment">
A protocol that defines the common lifecycle and configuration interface for NSDK feature sessions.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="protocol-nsdklogcallback"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.interface-NSDKLogCallback/" title="Protocol for receiving log messages from NSDK....">NSDKLogCallback</a></span><span class="ctoken plain"> : AnyObject</span></span></td>
<td><span class="ctoken-line"><span class="ctoken plain"> AnyObject</span></span></td>
<td><div class="ctoken comment">
Protocol for receiving log messages from NSDK.<br />
Implement this protocol to receive NSDK log messages in your application.<br />
The callback will be invoked on background threads, so ensure your implementation<br />
is thread-safe.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="protocol-nsdksessiondatasource"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.interface-NSDKSessionDataSource/" title="Provides synchronous, pull-based access to the latest available sensor data...">NSDKSessionDataSource</a></span><span class="ctoken plain"> : AnyObject</span></span></td>
<td><span class="ctoken-line"><span class="ctoken plain"> AnyObject</span></span></td>
<td><div class="ctoken comment">
Provides synchronous, pull-based access to the latest available sensor data<br />
required by <code>NSDKSession</code>.<br />
All methods must be non-blocking and thread-safe. Returned values represent<br />
the most recent samples already captured by the underlying services.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="protocol-nsdkviewdelegate"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.interface-NSDKViewDelegate/" title="Browse to NSDKViewDelegate">NSDKViewDelegate</a></span><span class="ctoken plain"> : </span><span class="ctoken class-name">ARSessionDelegate</span><span class="ctoken plain">, </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.interface-PlaybackSessionDelegate/" title="Delegate protocol for receiving frame updates during playback (mirrors ARSessionDelegate-style callbacks).">PlaybackSessionDelegate</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">ARSessionDelegate</span><span class="ctoken plain">, </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.interface-PlaybackSessionDelegate/" title="Delegate protocol for receiving frame updates during playback (mirrors ARSessionDelegate-style callbacks).">PlaybackSessionDelegate</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="protocol-playbackdatasetsource"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.interface-PlaybackDatasetSource/" title="Protocol for loading playback dataset data from various sources....">PlaybackDatasetSource</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.interface-PlaybackDatasetSource/" title="Protocol for loading playback dataset data from various sources....">PlaybackDatasetSource</a></span></span></td>
<td><div class="ctoken comment">
Protocol for loading playback dataset data from various sources.<br />
This protocol abstracts data retrieval, allowing for different implementations<br />
such as bundle loading, file system loading, remote loading, or mock data for testing.<br />
Implementations are used for on-demand frame loading - the loader is passed to<br />
<code>PlaybackDataset</code> which calls these methods when frames are requested.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="protocol-playbacksessiondelegate"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.interface-PlaybackSessionDelegate/" title="Delegate protocol for receiving frame updates during playback (mirrors ARSessionDelegate-style callbacks).">PlaybackSessionDelegate</a></span><span class="ctoken plain"> : AnyObject</span></span></td>
<td><span class="ctoken-line"><span class="ctoken plain"> AnyObject</span></span></td>
<td><div class="ctoken comment">
Delegate protocol for receiving frame updates during playback (mirrors ARSessionDelegate-style callbacks).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="protocol-resourceowner"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.interface-ResourceOwner/" title="Browse to ResourceOwner">ResourceOwner</a></span><span class="ctoken plain"> : AnyObject</span></span></td>
<td><span class="ctoken-line"><span class="ctoken plain"> AnyObject</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="protocol-uiorientationreporter"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.interface-UIOrientationReporter/" title="Browse to UIOrientationReporter">UIOrientationReporter</a></span><span class="ctoken plain"> : AnyObject</span></span></td>
<td><span class="ctoken-line"><span class="ctoken plain"> AnyObject</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Structs<a href="#structs" class="hash-link" aria-label="Direct link to Structs" title="Direct link to Structs">​</a>

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
<td><span id="struct-areatarget"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AreaTarget/" title="Contains a ``CoverageArea`` and its associated ``LocalizationTarget``.">AreaTarget</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AreaTarget/" title="Contains a ``CoverageArea`` and its associated ``LocalizationTarget``.">AreaTarget</a></span></span></td>
<td><div class="ctoken comment">
Contains a <code>CoverageArea</code> and its associated <code>LocalizationTarget</code>.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-areatargetresult"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AreaTargetResult/" title="Browse to AreaTargetResult">AreaTargetResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AreaTargetResult/" title="Browse to AreaTargetResult">AreaTargetResult</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-arutils"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-ARUtils/" title="Utility functions for AR and device capability detection....">ARUtils</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-ARUtils/" title="Utility functions for AR and device capability detection....">ARUtils</a></span></span></td>
<td><div class="ctoken comment">
Utility functions for AR and device capability detection.<br />
<code>ARUtils</code> provides helper methods for detecting device capabilities<br />
and AR features that are relevant to NSDK functionality.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-assetinfo"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AssetInfo/" title="Represents asset information from the Sites Manager service....">AssetInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AssetInfo/" title="Represents asset information from the Sites Manager service....">AssetInfo</a></span></span></td>
<td><div class="ctoken comment">
Represents asset information from the Sites Manager service.<br />
Maps to proto messages AssetRecord, AssetData, and AssetComputedValues.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-assetmeshdata"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AssetMeshData/" title="Mesh-specific asset data....">AssetMeshData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AssetMeshData/" title="Mesh-specific asset data....">AssetMeshData</a></span></span></td>
<td><div class="ctoken comment">
Mesh-specific asset data.<br />
Maps to proto message AssetMeshData.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-assetsplatdata"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AssetSplatData/" title="Splat-specific asset data....">AssetSplatData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AssetSplatData/" title="Splat-specific asset data....">AssetSplatData</a></span></span></td>
<td><div class="ctoken comment">
Splat-specific asset data.<br />
Maps to proto message AssetSplatData.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-assetvpsdata"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AssetVpsData/" title="VPS-specific asset data....">AssetVpsData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AssetVpsData/" title="VPS-specific asset data....">AssetVpsData</a></span></span></td>
<td><div class="ctoken comment">
VPS-specific asset data.<br />
Maps to proto message AssetVpsData.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-authinfo"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AuthInfo/" title="Authentication information containing token claims....">AuthInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AuthInfo/" title="Authentication information containing token claims....">AuthInfo</a></span></span></td>
<td><div class="ctoken comment">
Authentication information containing token claims.<br />
Contains parsed JWT claims including token string, expiration, user information, and other standard JWT fields.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-awarenessimageparams"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AwarenessImageParams/" title="Browse to AwarenessImageParams">AwarenessImageParams</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-AwarenessImageParams/" title="Browse to AwarenessImageParams">AwarenessImageParams</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-coveragearea"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-CoverageArea/" title="Represents a geographic area where VPS localization is possible">CoverageArea</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-CoverageArea/" title="Represents a geographic area where VPS localization is possible">CoverageArea</a></span></span></td>
<td><div class="ctoken comment">
Represents a geographic area where VPS localization is possible
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-coveragearearesult"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-CoverageAreaResult/" title="Contains all the ``CoverageArea`` objects returned by a query to the VPS Coverage service.">CoverageAreaResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-CoverageAreaResult/" title="Contains all the ``CoverageArea`` objects returned by a query to the VPS Coverage service.">CoverageAreaResult</a></span></span></td>
<td><div class="ctoken comment">
Contains all the <code>CoverageArea</code> objects returned by a query to the VPS Coverage service.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-geolocationdata"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-GeolocationData/" title="Struct representing geolocation data including latitude, longitude, altitude,...">GeolocationData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-GeolocationData/" title="Struct representing geolocation data including latitude, longitude, altitude,...">GeolocationData</a></span></span></td>
<td><div class="ctoken comment">
Struct representing geolocation data including latitude, longitude, altitude,<br />
heading, and orientation.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-hintimageresult"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-HintImageResult/" title="Image data returned by a query to a VPS hint image URL.">HintImageResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-HintImageResult/" title="Image data returned by a query to a VPS hint image URL.">HintImageResult</a></span></span></td>
<td><div class="ctoken comment">
Image data returned by a query to a VPS hint image URL.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-imagemath"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-ImageMath/" title="Provides affine transformation utilities for image processing....">ImageMath</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-ImageMath/" title="Provides affine transformation utilities for image processing....">ImageMath</a></span></span></td>
<td><div class="ctoken comment">
Provides affine transformation utilities for image processing.<br />
All affine matrices returned by this class operate in <strong>normalized coordinates</strong>,<br />
where image space is mapped to the [0, 1] range in both axes with origin at top-left.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-localizationtarget"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-LocalizationTarget/" title="Represents a real-world point of interest that is a VPS localization target....">LocalizationTarget</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-LocalizationTarget/" title="Represents a real-world point of interest that is a VPS localization target....">LocalizationTarget</a></span></span></td>
<td><div class="ctoken comment">
Represents a real-world point of interest that is a VPS localization target.<br />
VPS localization is more likely to succeed when a localization target is in camera view.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-localizationtargetresult"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-LocalizationTargetResult/" title="Contains all the ``LocalizationTarget`` objects returned by a query to the VPS Coverage service.">LocalizationTargetResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-LocalizationTargetResult/" title="Contains all the ``LocalizationTarget`` objects returned by a query to the VPS Coverage service.">LocalizationTargetResult</a></span></span></td>
<td><div class="ctoken comment">
Contains all the <code>LocalizationTarget</code> objects returned by a query to the VPS Coverage service.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-mapmetadata"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-MapMetadata/" title="Structure representing the metadata of a device map for visualization and processing.">MapMetadata</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-MapMetadata/" title="Structure representing the metadata of a device map for visualization and processing.">MapMetadata</a></span></span></td>
<td><div class="ctoken comment">
Structure representing the metadata of a device map for visualization and processing.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-meshdownloaderresult"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-MeshDownloaderResult/" title="Represents a single mesh result with geometry, texture, and transform data.">MeshDownloaderResult</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-MeshDownloaderResult/" title="Represents a single mesh result with geometry, texture, and transform data.">MeshDownloaderResult</a></span></span></td>
<td><div class="ctoken comment">
Represents a single mesh result with geometry, texture, and transform data.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-nsdkbuffer"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKBuffer/" title="A buffer containing binary data for NSDK operations....">NSDKBuffer</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKBuffer/" title="A buffer containing binary data for NSDK operations....">NSDKBuffer</a></span></span></td>
<td><div class="ctoken comment">
A buffer containing binary data for NSDK operations.<br />
<code>NSDKBuffer</code> provides a safe wrapper around binary data buffers used by<br />
various NSDK features. It handles memory management and provides convenient<br />
access to buffer data.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-nsdkfeaturestatus"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKFeatureStatus/" title="Status flags for NSDK features indicating their current operational state....">NSDKFeatureStatus</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKFeatureStatus/" title="Status flags for NSDK features indicating their current operational state....">NSDKFeatureStatus</a></span></span></td>
<td><div class="ctoken comment">
Status flags for NSDK features indicating their current operational state.<br />
<code>NSDKFeatureStatus</code> is an option set that represents various status conditions<br />
for NSDK features like VPS2, scanning, and mapping. Multiple status flags<br />
can be active simultaneously to provide detailed status information.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-nsdkframedata"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKFrameData/" title="A complete frame of data captured from an AR session....">NSDKFrameData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKFrameData/" title="A complete frame of data captured from an AR session....">NSDKFrameData</a></span></span></td>
<td><div class="ctoken comment">
A complete frame of data captured from an AR session.<br />
<code>NSDKFrameData</code> encapsulates all the sensor data, images, and tracking information<br />
from a single AR frame. This includes camera images, depth data, device pose,<br />
GPS location, compass heading, and camera intrinsics.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-nsdkimage"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKImage/" title="Provides a view into the data buffer of an image output by the NSDK....">NSDKImage</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKImage/" title="Provides a view into the data buffer of an image output by the NSDK....">NSDKImage</a></span></span></td>
<td><div class="ctoken comment">
Provides a view into the data buffer of an image output by the NSDK.<br />
<code>NSDKImage</code> provides access to image data in various formats (RGB, grayscale,<br />
depth, etc.) used by NSDK features like depth processing, semantic segmentation,<br />
and image analysis.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-nsdkinputdataflags"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKInputDataFlags/" title="Flags indicating which types of input data are required by NSDK....">NSDKInputDataFlags</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKInputDataFlags/" title="Flags indicating which types of input data are required by NSDK....">NSDKInputDataFlags</a></span></span></td>
<td><div class="ctoken comment">
Flags indicating which types of input data are required by NSDK.<br />
<code>NSDKInputDataFlags</code> is an option set that specifies which data types<br />
should be included in frames sent to NSDK. Use <code>getRequestedDataInputs()</code><br />
to determine which data is currently needed, then include only the<br />
requested data types in your frame data for optimal performance.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-nsdkpathconfig"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKPathConfig/" title="Browse to NSDKPathConfig">NSDKPathConfig</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKPathConfig/" title="Browse to NSDKPathConfig">NSDKPathConfig</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-nsdkutils"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKUtils/" title="Utility functions for NSDK string management and memory handling....">NSDKUtils</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-NSDKUtils/" title="Utility functions for NSDK string management and memory handling....">NSDKUtils</a></span></span></td>
<td><div class="ctoken comment">
Utility functions for NSDK string management and memory handling.<br />
<code>NSDKUtils</code> provides helper methods for safely managing C string conversions<br />
and memory allocation when working with the NSDK C API.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-organizationinfo"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-OrganizationInfo/" title="Represents organization information from the Sites Manager service.">OrganizationInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-OrganizationInfo/" title="Represents organization information from the Sites Manager service.">OrganizationInfo</a></span></span></td>
<td><div class="ctoken comment">
Represents organization information from the Sites Manager service.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-playbackframe"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-PlaybackFrame/" title="One &quot;frame&quot; of playback: metadata (pose, intrinsics, orientation, etc.), optional camera image, optional depth....">PlaybackFrame</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-PlaybackFrame/" title="One &quot;frame&quot; of playback: metadata (pose, intrinsics, orientation, etc.), optional camera image, optional depth....">PlaybackFrame</a></span></span></td>
<td><div class="ctoken comment">
One "frame" of playback: metadata (pose, intrinsics, orientation, etc.), optional camera image, optional depth.<br />
Exposes <code>.camera</code> → <strong>PlaybackCamera</strong>. Created by PlaybackSession and delivered to the delegate and PlaybackRenderer.<br />
Relation to Apple AR: Not an Apple type. Delivered <strong>instead of ARFrame</strong> when in playback; the app gets<br />
frame-like data (image, camera, etc.) from the delegate so app code can stay uniform.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-scenesegmentationchannels"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-SceneSegmentationChannels/" title="A set of semantic channels represented as a bitmask, matching the C SDK packed-channel layout....">SceneSegmentationChannels</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-SceneSegmentationChannels/" title="A set of semantic channels represented as a bitmask, matching the C SDK packed-channel layout....">SceneSegmentationChannels</a></span></span></td>
<td><div class="ctoken comment">
A set of semantic channels represented as a bitmask, matching the C SDK packed-channel layout.<br />
Use this type wherever you need one or more semantic channels. It supports clean Swift syntax:
</div>
<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">
<div class="codeBlockContent_QJqH">
<pre class="prism-code language-swift codeBlock_bY9V thin-scrollbar" tabindex="0" style="color:#393A34;background-color:#f6f8fa"><code>let channels: SceneSegmentationChannels = [.ground, .sky]
let single = SceneSegmentationChannels.grass</code></pre>
</div>
</div>
<div class="ctoken comment">
Bit positions 0–4 correspond to the C SDK channels: Sky=0, Ground=1, NaturalGround=2, ArtificialGround=3, Grass=4.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-siteassetsinfo"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-SiteAssetsInfo/" title="A single entry in a site-assets location query result.">SiteAssetsInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-SiteAssetsInfo/" title="A single entry in a site-assets location query result.">SiteAssetsInfo</a></span></span></td>
<td><div class="ctoken comment">
A single entry in a site-assets location query result.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-siteinfo"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-SiteInfo/" title="Represents site information from the Sites Manager service.">SiteInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-SiteInfo/" title="Represents site information from the Sites Manager service.">SiteInfo</a></span></span></td>
<td><div class="ctoken comment">
Represents site information from the Sites Manager service.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-textureutils"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-TextureUtils/" title="Browse to TextureUtils">TextureUtils</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-TextureUtils/" title="Browse to TextureUtils">TextureUtils</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-timeouterror"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-TimeoutError/" title="Browse to TimeoutError">TimeoutError</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-TimeoutError/" title="Browse to TimeoutError">TimeoutError</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-userinfo"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-UserInfo/" title="Represents user information from the Sites Manager service.">UserInfo</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-UserInfo/" title="Represents user information from the Sites Manager service.">UserInfo</a></span></span></td>
<td><div class="ctoken comment">
Represents user information from the Sites Manager service.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-vps2geolocationdata"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2GeolocationData/" title="Location and heading data calculated by VPS2.">Vps2GeolocationData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2GeolocationData/" title="Location and heading data calculated by VPS2.">Vps2GeolocationData</a></span></span></td>
<td><div class="ctoken comment">
Location and heading data calculated by VPS2.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-vps2localization"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2Localization/" title="Spatial mapping between the device&#39;s AR coordinate space and real-world...">Vps2Localization</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2Localization/" title="Spatial mapping between the device&#39;s AR coordinate space and real-world...">Vps2Localization</a></span></span></td>
<td><div class="ctoken comment">
Spatial mapping between the device's AR coordinate space and real-world<br />
geolocation, as determined by VPS2.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-vps2localizationrequestrecord"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2LocalizationRequestRecord/" title="Browse to Vps2LocalizationRequestRecord">Vps2LocalizationRequestRecord</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2LocalizationRequestRecord/" title="Browse to Vps2LocalizationRequestRecord">Vps2LocalizationRequestRecord</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-vps2pose"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2Pose/" title="Pose in AR coordinate space calculated by VPS2 from a geolocation.">Vps2Pose</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-Vps2Pose/" title="Pose in AR coordinate space calculated by VPS2 from a geolocation.">Vps2Pose</a></span></span></td>
<td><div class="ctoken comment">
Pose in AR coordinate space calculated by VPS2 from a geolocation.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="struct-vpsanchorupdate"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-VpsAnchorUpdate/" title="Contains the latest tracking information for a VPS anchor....">VpsAnchorUpdate</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.struct-VpsAnchorUpdate/" title="Contains the latest tracking information for a VPS anchor....">VpsAnchorUpdate</a></span></span></td>
<td><div class="ctoken comment">
Contains the latest tracking information for a VPS anchor.<br />
Anchor updates are retrieved via <code>anchorUpdate(anchorId:)</code> and provide the<br />
most current information about an anchor's position, orientation, and tracking status. This<br />
is a snapshot of the anchor, and the latest anchor update should be used every frame.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Enums<a href="#enums" class="hash-link" aria-label="Direct link to Enums" title="Direct link to Enums">​</a>

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
<td><span id="enum-agelevel"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AgeLevel/" title="Codes describing the age level of the user....">AgeLevel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AgeLevel/" title="Codes describing the age level of the user....">AgeLevel</a></span></span></td>
<td><div class="ctoken comment">
Codes describing the age level of the user.<br />
This enum represents the age classification for users of the NSDK
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-assetdeploymenttype"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AssetDeploymentType/" title="Asset deployment type....">AssetDeploymentType</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AssetDeploymentType/" title="Asset deployment type....">AssetDeploymentType</a></span></span></td>
<td><div class="ctoken comment">
Asset deployment type.<br />
Maps to proto enum AssetDeploymentType.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-assetpipelinejobstatus"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AssetPipelineJobStatus/" title="Asset pipeline job status....">AssetPipelineJobStatus</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AssetPipelineJobStatus/" title="Asset pipeline job status....">AssetPipelineJobStatus</a></span></span></td>
<td><div class="ctoken comment">
Asset pipeline job status.<br />
Maps to proto enum AssetPipelineJobStatus.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-assetstatustype"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AssetStatusType/" title="Asset status....">AssetStatusType</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AssetStatusType/" title="Asset status....">AssetStatusType</a></span></span></td>
<td><div class="ctoken comment">
Asset status.<br />
Maps to proto enum AssetStatusType.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-assettype"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AssetType/" title="Asset type - determines which typed asset data is present....">AssetType</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AssetType/" title="Asset type - determines which typed asset data is present....">AssetType</a></span></span></td>
<td><div class="ctoken comment">
Asset type - determines which typed asset data is present.<br />
Maps to proto enum AssetType.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-awarenesserror"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AwarenessError/" title="Browse to AwarenessError">AwarenessError</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AwarenessError/" title="Browse to AwarenessError">AwarenessError</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-exportresolution"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-ExportResolution/" title="Resolution option for exported scan images....">ExportResolution</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-ExportResolution/" title="Resolution option for exported scan images....">ExportResolution</a></span></span></td>
<td><div class="ctoken comment">
Resolution option for exported scan images.<br />
When exporting a recording, this controls which image resolutions are included in the payload.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-headingmode"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-HeadingMode/" title="Controls how the heading is computed from the device&#39;s orientation.">HeadingMode</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-HeadingMode/" title="Controls how the heading is computed from the device&#39;s orientation.">HeadingMode</a></span></span></td>
<td><div class="ctoken comment">
Controls how the heading is computed from the device's orientation.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-nsdkasyncstate"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKAsyncState/" title="Reports the state of an asynchronous NSDK operation.">NSDKAsyncState</a></span><span class="ctoken plain">&lt;</span><span class="ctoken plain">Value</span><span class="ctoken plain">, </span><span class="ctoken plain">Error</span><span class="ctoken plain">&gt; </span><span class="ctoken keyword">where</span><span class="ctoken plain"> </span><span class="ctoken class-name">Error</span><span class="ctoken plain"> : </span><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/error" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Error</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://developer.apple.com/documentation//swift/error" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Error</a></span></span></td>
<td><div class="ctoken comment">
Reports the state of an asynchronous NSDK operation.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-nsdkerror"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKError/" title="Errors thrown by the NSDK API....">NSDKError</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKError/" title="Errors thrown by the NSDK API....">NSDKError</a></span></span></td>
<td><div class="ctoken comment">
Errors thrown by the NSDK API.<br />
<code>NSDKError</code> a subset of all the <code>ARDK_Status</code>codes returned by the C API,<br />
containing just those that can occur in the Swift environment.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-nsdkloglevel"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKLogLevel/" title="Defines the available logging levels for NSDK....">NSDKLogLevel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKLogLevel/" title="Defines the available logging levels for NSDK....">NSDKLogLevel</a></span></span></td>
<td><div class="ctoken comment">
Defines the available logging levels for NSDK.<br />
<code>NSDKLogLevel</code> controls the verbosity of logging output from the NSDK system.<br />
Logging can be configured separately for stdout, files, and callback functions.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-nsdkscreenorientation"></span><span class="ctoken-line"><span class="ctoken plain">@frozen</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKScreenOrientation/" title="Represents the screen orientation in the NSDK layer.">NSDKScreenOrientation</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKScreenOrientation/" title="Represents the screen orientation in the NSDK layer.">NSDKScreenOrientation</a></span></span></td>
<td><div class="ctoken comment">
Represents the screen orientation in the NSDK layer.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-nsdktelemetry"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKTelemetry/" title="Namespace for NSDK telemetry controls.">NSDKTelemetry</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKTelemetry/" title="Namespace for NSDK telemetry controls.">NSDKTelemetry</a></span></span></td>
<td><div class="ctoken comment">
Namespace for NSDK telemetry controls.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-nsdktelemetryenvironment"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKTelemetryEnvironment/" title="Telemetry backend environment passed to native on session start....">NSDKTelemetryEnvironment</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NSDKTelemetryEnvironment/" title="Telemetry backend environment passed to native on session start....">NSDKTelemetryEnvironment</a></span></span></td>
<td><div class="ctoken comment">
Telemetry backend environment passed to native on session start.<br />
Use this type instead of a free <code>String</code> so only supported values (<code>dev</code>, <code>stg</code>, <code>prod</code>) compile.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-nsdktrackingstate"></span><span class="ctoken-line"><span class="ctoken plain">@frozen</span><span class="ctoken plain"> </span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NsdkTrackingState/" title="The general quality of position tracking available when the camera captured a frame.">NsdkTrackingState</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-NsdkTrackingState/" title="The general quality of position tracking available when the camera captured a frame.">NsdkTrackingState</a></span></span></td>
<td><div class="ctoken comment">
The general quality of position tracking available when the camera captured a frame.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-playbackdatasetconstants"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-PlaybackDatasetConstants/" title="Constants for playback dataset file names and extensions.">PlaybackDatasetConstants</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-PlaybackDatasetConstants/" title="Constants for playback dataset file names and extensions.">PlaybackDatasetConstants</a></span></span></td>
<td><div class="ctoken comment">
Constants for playback dataset file names and extensions.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-typedassetdata"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-TypedAssetData/" title="Discriminated union for typed asset data....">TypedAssetData</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-TypedAssetData/" title="Discriminated union for typed asset data....">TypedAssetData</a></span></span></td>
<td><div class="ctoken comment">
Discriminated union for typed asset data.<br />
One of mesh, splat, or vps will be set based on the asset type.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-vps2localizationerror"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-Vps2LocalizationError/" title="Possible errors from VPS localization operations.">Vps2LocalizationError</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-Vps2LocalizationError/" title="Possible errors from VPS localization operations.">Vps2LocalizationError</a></span></span></td>
<td><div class="ctoken comment">
Possible errors from VPS localization operations.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-vps2localizationrequeststatus"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-Vps2LocalizationRequestStatus/" title="Status of a network request.">Vps2LocalizationRequestStatus</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-Vps2LocalizationRequestStatus/" title="Status of a network request.">Vps2LocalizationRequestStatus</a></span></span></td>
<td><div class="ctoken comment">
Status of a network request.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-vps2localizationrequesttype"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-Vps2LocalizationRequestType/" title="Browse to Vps2LocalizationRequestType">Vps2LocalizationRequestType</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-Vps2LocalizationRequestType/" title="Browse to Vps2LocalizationRequestType">Vps2LocalizationRequestType</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-vps2trackingstate"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-Vps2TrackingState/" title="Browse to Vps2TrackingState">Vps2TrackingState</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-Vps2TrackingState/" title="Browse to Vps2TrackingState">Vps2TrackingState</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="enum-vpsgraphoperationerror"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-VpsGraphOperationError/" title="Browse to VpsGraphOperationError">VpsGraphOperationError</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-VpsGraphOperationError/" title="Browse to VpsGraphOperationError">VpsGraphOperationError</a></span></span></td>
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
<td><span id="method-playbacksession"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.method-playbackSession/" title="Called on the main queue when the tracking state changes (e.g. at start of playback). For playback, state is typically .normal.">playbackSession</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Called on the main queue when the tracking state changes (e.g. at start of playback). For playback, state is typically .normal.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
