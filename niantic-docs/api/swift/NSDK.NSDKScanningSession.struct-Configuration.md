---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKScanningSession.struct-Configuration/
title: Configuration
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKScanningSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKScanningSession/ "NSDKScanningSession") 

</div>

<div class="api-title">

#  Configuration

<div class="api-package">

Configuration structure for the scanning session.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">struct</span><span class="ctoken plain"> </span><span class="ctoken class-name">Configuration</span></span>

------------------------------------------------------------------------

## Constructors<a href="#constructors" class="hash-link" aria-label="Direct link to Constructors" title="Direct link to Constructors">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">init</span><span class="ctoken plain">(</span><span class="ctoken plain">framerate</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span><span class="ctoken plain"> = 0, </span><span class="ctoken plain">enableRaycastVisualization</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain"> = false, </span><span class="ctoken plain">enableVoxelVisualization</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain"> = false, </span><span class="ctoken plain">raycastWidth</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span><span class="ctoken plain"> = 0, </span><span class="ctoken plain">raycastHeight</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span><span class="ctoken plain"> = 0, </span><span class="ctoken plain">nearDepth</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain"> = 0.02, </span><span class="ctoken plain">farDepth</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain"> = 0.0, </span><span class="ctoken plain">voxelSize</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span><span class="ctoken plain"> = 0.0, </span><span class="ctoken plain">path</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">? = nil, </span><span class="ctoken plain">scanTargetId</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">? = nil, </span><span class="ctoken plain">generateDepthsIfLidarUnavailable</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain"> = false, </span><span class="ctoken plain">enableFullResolution</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain"> = false, </span><span class="ctoken plain">fullResolutionFramerate</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int</a></span><span class="ctoken plain"> = 0, </span><span class="ctoken plain">recordAllSensors</span><span class="ctoken plain">: </span><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span><span class="ctoken plain"> = false)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Initializes a new scanning session configuration with provided settings.

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
<td><span id="property-enablefullresolution"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">enableFullResolution</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
Controls whether full-resolution camera images are recorded.<br />
When <code>true</code>, the scanning feature will record a JPEG image that is the same resolution<br />
as the raw camera image passed to the NSDK session with the <code>sendFrame</code> function.<br />
When <code>false</code>, the scanning feature records a 720x540 resolution JPEG image<br />
generated by cropping and/or scaling and compressing the raw camera image.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-enableraycastvisualization"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">enableRaycastVisualization</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
Controls whether raycast visualization images are generated.<br />
When <code>true</code>, images for the raycast visualization will be generated each time a new input<br />
frame is available. The scanning feature provides buffers that can be used to generate<br />
a 2D image that visualizes what parts of the scene have been thoroughly scanned.<br />
See the <code>RaycastBuffer</code> class for more information.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-enablevoxelvisualization"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">enableVoxelVisualization</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
Controls whether voxel visualization is enabled.<br />
When <code>true</code>, voxels can be computed, and computed voxels will be updated each time a<br />
new input frame is available. Use <code>computeVoxels</code> to update the voxel grid and<br />
<code>voxelBuffer</code> to read the data.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-fardepth"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">farDepth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Far depth plane for scan depth range, in meters.<br />
This parameter controls the farthest distance at which depth data will be integrated.<br />
Objects farther than this distance will not be visible in visualization or reconstruction.<br />
This does not affect the range of the recorded depth frames. If set to <code>0.0</code>, this is<br />
configured to 5.0 m in the default configuration. Values greater than 5.0 m are not<br />
recommended. Must be greater than <code>nearDepth</code>, or set to <code>0</code> to use the default range.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-framerate"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">framerate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int32</a></span></span></td>
<td><div class="ctoken comment">
Target FPS for recording and visualization processes.<br />
The target framerate is the cap for how often the feature will process new input frames.<br />
The actual framerate may differ. If set to <code>0</code>, this defaults to 30 FPS. The recording<br />
FPS cannot exceed the rate at which frames are delivered to the scanning session.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-fullresolutionframerate"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">fullResolutionFramerate</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int32</a></span></span></td>
<td><div class="ctoken comment">
Target FPS for full resolution frame recording.<br />
The target framerate for recording full resolution frames when <code>enableFullResolution</code><br />
is <code>true</code>. The actual framerate for full-resolution frames may differ from the target<br />
framerate. If set to <code>0</code>, this is configured to 2 FPS in the default configuration.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-generatedepthsiflidarunavailable"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">generateDepthsIfLidarUnavailable</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
Whether to use and record NSDK's estimated depths, if platform depths are unavailable.<br />
Depths are recorded as part of the scan data, and are also required to generate voxels<br />
or raycast visualization images. If NSDK was configured to use platform depths, this<br />
value is ignored, and depths are expected to come through the scanning session.<br />
Otherwise:<br />
- When <code>true</code>, NSDK will generate estimated depths for use by the scanning feature<br />
- When <code>false</code>, the scanning feature will not be able to generate voxels or raycast<br />
visualization images, but will still be able to record other scan data.<br />
- Attention: If NSDK depth is being recorded because <code>generateDepthsIfLidarUnavailable</code><br />
is <code>true</code> and lidar is unavailable, the recording FPS will be limited to the<br />
update rate of the depth feature, which defaults to 10 FPS.<br />
To change the update rate of the depth feature, set<br />
<code>NSDKDepthSession.Configuration.framerate</code> to match<br />
<code>ScanningConfiguration.framerate</code>.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-neardepth"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">nearDepth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Near depth plane for scan depth range, in meters.<br />
This parameter controls the closest distance at which depth data will be integrated.<br />
Objects closer than this distance will not be visible in visualization or reconstruction.<br />
This does not affect the range of the recorded depth frames. If set to <code>-1.0</code>, this is<br />
configured to 0.02 m in the default configuration. Must be greater than or equal to 0<br />
and less than <code>farDepth</code>, or set to <code>-1.0</code> to use the default range.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-path"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">path</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Optional field to set a base path for writing scan data.<br />
If an absolute path (starting with '/', '', or a drive name) is provided, the directory<br />
must be writeable by the application. All other paths will be interpreted as relative to<br />
the public application path configured when the NSDK object was created. If left <code>nil</code>,<br />
NSDK uses the public application path which was configured when creating the NSDK object.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-raycastheight"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">raycastHeight</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int32</a></span></span></td>
<td><div class="ctoken comment">
Height of the raycast visualization's output image in pixel units.<br />
The output quality is bound by both the configured resolution and the quality of the<br />
underlying 3D reconstruction data. On devices without native depth support, the data is<br />
unlikely to be sufficient to support resolutions above 256x144. If set to <code>0</code>, this is<br />
configured to 144 pixels.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-raycastwidth"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">raycastWidth</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/int32" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Int32</a></span></span></td>
<td><div class="ctoken comment">
Width of the raycast visualization's output image in pixel units.<br />
The output quality is bound by both the configured resolution and the quality of the<br />
underlying 3D reconstruction data. On devices without native depth support, the data is<br />
unlikely to be sufficient to support resolutions above 256x144. If set to <code>0</code>, this is<br />
configured to 256 pixels.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-recordallsensors"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">recordAllSensors</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/bool" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Bool</a></span></span></td>
<td><div class="ctoken comment">
Whether to record all sensors.<br />
When <code>true</code>, all sensors will be recorded. When <code>false</code>, only the first sensor will be recorded.<br />
<strong>Default:</strong> <code>false</code>
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-scantargetid"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">scanTargetId</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken plain">?</span></span></td>
<td><div class="ctoken comment">
Optional field to set a scan target identifier for use with Niantic Spatial's mapping<br />
services.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-voxelsize"></span><span class="ctoken-line"><span class="ctoken keyword">var</span><span class="ctoken plain"> </span><span class="ctoken class-name">voxelSize</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword"><a href="https://developer.apple.com/documentation//swift/float" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Float</a></span></span></td>
<td><div class="ctoken comment">
Minimum size of voxels for the voxel visualization, in meters.<br />
This parameter controls the resolution of the voxel grid used for voxel visualization.<br />
Smaller values result in higher resolution but require more memory and computation.<br />
Larger values result in lower resolution but are more efficient. The actual voxel size<br />
may become larger due to memory constraints, so this is only a minimum value. If set to<br />
<code>0.0</code>, this is configured to 0.01 m in the default configuration.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
