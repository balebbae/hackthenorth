---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager/
title: ARScanningManager
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Scanning](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning/ "NianticSpatial.NSDK.AR.Scanning") 

</div>

<div class="api-title">

#  ARScanningManager

<div class="api-extends">

↳ extends UnityEngine.XR.ARFoundation.SubsystemLifecycleManager

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">ARScanningManager</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.0/api/UnityEngine.XR.ARFoundation.SubsystemLifecycleManager-3.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">SubsystemLifecycleManager</a></span><span class="ctoken punctuation">\<</span><span class="ctoken class-name">[XRScanningSubsystem](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem/ "Defines an interface for interacting with scanning functionality.")</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">[XRScanningSubsystemDescriptor](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystemDescriptor/ "Browse to XRScanningSubsystemDescriptor")</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name">[Provider](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.XRSubsystems.XRScanningSubsystem.Provider/ "An abstract class to be implemented by providers of this subsystem.")</span><span class="ctoken punctuation">\></span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

A manager for recording scans of the AR scene for Playback. The recording will start when the manager is enabled. Use SaveScan() to stop and save the recording into the ScanPath.

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
<td><span id="property-enableraycastvisualization"></span><span class="ctoken-line"><span class="ctoken class-name">EnableRaycastVisualization</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Enable raycast visualization for scanning. Required to access the raycast textures.<br />
The data will be available from the GetRaycastColorTexture,<br />
GetRaycastNormalTexture and GetRaycastPositionTexture methods.<br />
Must be set before scanning starts to take effect.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-enablevoxelvisualization"></span><span class="ctoken-line"><span class="ctoken class-name">EnableVoxelVisualization</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Enable voxel visualization for scanning. Required to compute voxels.<br />
RequestVoxelUpdate must be called to asynchronously compute the voxel buffers.<br />
Then, TryGetVoxelBuffer can be called to get the voxel buffers.<br />
After TryGetVoxelBuffer returns true, the voxel data will be available in the<br />
VoxelPositions, VoxelColors and LatestVoxelSize fields.<br />
Must be set before scanning starts to take effect.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-fardepth"></span><span class="ctoken-line"><span class="ctoken class-name">FarDepth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
The far depth plane for depth range, in meters.<br />
This parameter controls the farthest distance at which depth data<br />
will be integrated. Objects farther than this distance will not be<br />
visible in visualization or reconstruction.<br />
Must be set before scanning starts to take effect.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-fullresolutionenabled"></span><span class="ctoken-line"><span class="ctoken class-name">FullResolutionEnabled</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Record full resolution images for scan reconstruction.<br />
Must be set before scanning starts to take effect.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-fullresolutionframerate"></span><span class="ctoken-line"><span class="ctoken class-name">FullResolutionFramerate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The framerate for full resolution frame recording.<br />
A framerate of zero means the system will use the default framerate of 2 FPS.<br />
Must be set before scanning starts to take effect.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-latestvoxelsize"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">LatestVoxelSize</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
The size of the voxels in VoxelPositions, in meters.<br />
The voxel visualizer attempts to use the voxel size requested by the MinimumVoxelSize parameter.<br />
As the number of voxels grows, the voxel visualizer periodically doubles the voxel size to keep memory use<br />
in check. This value should be used for rendering the voxels with the correct dimensions.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-minimumvoxelsize"></span><span class="ctoken-line"><span class="ctoken class-name">MinimumVoxelSize</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
The minimum size of voxels for voxel visualization, in meters.<br />
This parameter sets the initial resolution of the voxel grid used for voxel visualization (see<br />
EnableVoxelVisualization. Smaller values result in higher resolution but require more memory<br />
and computation. The actual voxel size may be larger due to memory constraints, so this is only a minimum<br />
value. Refer to LatestVoxelSize for the correct dimensions when rendering voxels.<br />
Must be set before scanning starts to take effect.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-neardepth"></span><span class="ctoken-line"><span class="ctoken class-name">NearDepth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
The near depth plane for depth range, in meters.<br />
This parameter controls the closest distance at which depth data<br />
will be integrated. Objects closer than this distance will not be<br />
visible in visualization or reconstruction.<br />
Must be set before scanning starts to take effect.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-scanpath"></span><span class="ctoken-line"><span class="ctoken class-name">ScanPath</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
The scan path to store the scan data.<br />
If an absolute path is provided (starting with '/', '', or a drive name), the directory must be writable,<br />
and the application must have permissions to write to the folder.<br />
Otherwise, the path will be interpreted as relative to Application.persistentDataPath.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-scanrecordingframerate"></span><span class="ctoken-line"><span class="ctoken class-name">ScanRecordingFramerate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
The scan recording framerate.<br />
A framerate of zero means the system will use the default framerate of 15 FPS.<br />
Must be set before scanning starts to take effect.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-scantargetid"></span><span class="ctoken-line"><span class="ctoken class-name">ScanTargetId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
The scan target ID.<br />
Must be set before scanning starts to take effect.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-useestimateddepth"></span><span class="ctoken-line"><span class="ctoken class-name">UseEstimatedDepth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Record Niantic depth data if the device does not support platform depth such as lidar.<br />
If platform depth is present, it will be used instead of Niantic depth.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-voxelcolors"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">VoxelColors</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">NativeArray</span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Color32</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
The color of each voxel.<br />
Each entry in the array corresponds to an entry in VoxelPositions at the same index.<br />
These values can only be updated when EnableVoxelVisualization is true and scanning is<br />
in the Started state. Call RequestVoxelUpdate to update the<br />
underlying map, and then call TryGetVoxelBuffer to populate with the latest values.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-voxelnormals"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">VoxelNormals</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">NativeArray</span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector3</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
The normal vector of each voxel.<br />
Each entry in the array corresponds to an entry in VoxelPositions at the same index.<br />
These values can only be updated when EnableVoxelVisualization is true and scanning is<br />
in the Started state. Call RequestVoxelUpdate to update the<br />
underlying map, and then call TryGetVoxelBuffer to populate with the latest values.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-voxelpositions"></span><span class="ctoken-line"><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">VoxelPositions</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name">NativeArray</span><span class="ctoken punctuation">&lt;</span><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector3</a></span><span class="ctoken punctuation">&gt;</span></span></td>
<td><div class="ctoken comment">
The positions of voxels scanned with the camera.<br />
Each entry in the array corresponds to an entry in VoxelColors at the same index.<br />
These values can only be updated when EnableVoxelVisualization is true and scanning is<br />
in the Started state. Call RequestVoxelUpdate to update the<br />
underlying map, and then call TryGetVoxelBuffer to populate with the latest values.
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
<td><span id="method-getcurrentscanid"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager.GetCurrentScanId/" title="Returns the current scanID. The result is only present when scan is in progress.">GetCurrentScanId</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
Returns the current scanID. The result is only present when scan is in progress.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getframecount"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager.GetFrameCount/" title="Get the number of frames in the current scan. Should be called before calling SaveScan as...">GetFrameCount</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
Get the number of frames in the current scan. Should be called before calling SaveScan as<br />
frames must be greater than zero to save a scan
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getraycastcolortexture"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager.GetRaycastColorTexture/" title="Read the current raycast color texture.">GetRaycastColorTexture</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Texture2D</a></span></span></td>
<td><div class="ctoken comment">
Read the current raycast color texture.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getraycastnormaltexture"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager.GetRaycastNormalTexture/" title="Read the current raycast normal texture.">GetRaycastNormalTexture</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Texture2D</a></span></span></td>
<td><div class="ctoken comment">
Read the current raycast normal texture.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getraycastpositiontexture"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager.GetRaycastPositionTexture/" title="Read the current raycast position texture.">GetRaycastPositionTexture</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Texture2D</a></span></span></td>
<td><div class="ctoken comment">
Read the current raycast position texture.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getscanstore"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager.GetScanStore/" title="Browse to GetScanStore">GetScanStore</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanStore/" title="Browse to ScanStore">ScanStore</a></span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-requestvoxelupdate"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager.RequestVoxelUpdate/" title="Browse to RequestVoxelUpdate">RequestVoxelUpdate</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-savescan"></span><span class="ctoken-line"><span class="ctoken keyword">async</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager.SaveScan/" title="Save the current scan. This stops any further recording immediately, and the coroutine finishes when...">SaveScan</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Task</a></span></span></td>
<td><div class="ctoken comment">
Save the current scan. This stops any further recording immediately, and the coroutine finishes when<br />
the saving is fully complete.<br />
Please call GetFrameCount() to guarantee the scan has frames, as if it doesnt have any, the save will fail<br />
Do not disable the component or exit the app when this is in progress. The scan will not be saved correctly<br />
if this process is interrupted.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-trygetvoxelbuffer"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager.TryGetVoxelBuffer/" title="Browse to TryGetVoxelBuffer">TryGetVoxelBuffer</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment deemphasize">
-
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
