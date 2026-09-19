---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/migration_guide/
title: Migration Guide
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Migration Guide

</div>

## Migrating an ARDK 2.X Project to 3.0<a href="#migrating-an-ardk-2x-project-to-30" class="hash-link" aria-label="Direct link to Migrating an ARDK 2.X Project to 3.0" title="Direct link to Migrating an ARDK 2.X Project to 3.0">​</a>

To upgrade an existing project:

1.  Follow the instructions at [Installing ARDK 3.0](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/), stopping after step 3.
2.  Clean up redundancies in your code, such as deleting protobuf and telemetry plugins in ARDK 2.X.
3.  Complete the ARDK 3.0 installation steps, starting from [adding your API key](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/#create-a-lightship-account-and-add-api-key).
4.  Replace 2.X managers (such as `ARSession`) with 3.0 managers. See the [Manager Conversion Guide](#manager-conversion-guide) for a list of 2.X managers and their 3.0 counterparts.
5.  Replace references to `Niantic.ARDK` in scripts with the relevant `Niantic.Lightship` references.
6.  Once you have converted everything and your project compiles, delete the old ARDK folder.

## Manager Conversion Guide<a href="#manager-conversion-guide" class="hash-link" aria-label="Direct link to Manager Conversion Guide" title="Direct link to Manager Conversion Guide">​</a>

| ARDK 2.X Component | ARDK 3.0 Component |
|----|----|
| `ARSessionManager` | `ARSession` + `ARCameraManager` |
| `ARRenderingManager` | `ARCameraManager` + `ARCameraBackground` |
| `ARCameraPositionHelper` | `TrackedPoseDriver` |
| `ARDepthManager` | `AROcclusionManager` (+ `LightshipOcclusionExtension`) |
| `ARDepthInterpolationAdapter` | `LightshipOcclusionExtension` |
| `ARMeshManager` | `ARMeshManager` (+ `LightshipMeshingExtension`) |
| `ARPlaneManager` (from ARDK 2.x) | `ARPlaneManager` (from AR Foundation) |
| `ARSemanticSegmentationManager` | `ARSemanticSegmentationManager` (+ `LightshipOcclusionExtension`) |
| `GameboardManager` | `LightshipNavMeshManager` |

## Feature Conversion Guide<a href="#feature-conversion-guide" class="hash-link" aria-label="Direct link to Feature Conversion Guide" title="Direct link to Feature Conversion Guide">​</a>

### 1. Session Management<a href="#1-session-management" class="hash-link" aria-label="Direct link to 1. Session Management" title="Direct link to 1. Session Management">​</a>

In ARDK 2.X, AR session management was handled by an ARDK MonoBehaviour component called `ARSessionManager`.

In ARDK 3.0, AR session management is handled by AR Foundation in a MonoBehaviour component called `ARSession`. For more information on how to set up a basic AR scene using the `ARSession` component, see [Setting Up a Basic AR Scene](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/#setting-up-a-basic-ar-scene). For more information, see <a href="https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.1/manual/features/session.html" target="_blank" rel="noopener noreferrer">Unity’s documentation</a>.

### 2. Rendering<a href="#2-rendering" class="hash-link" aria-label="Direct link to 2. Rendering" title="Direct link to 2. Rendering">​</a>

In ARDK 2.X, rendering was handled by an ARDK MonoBehaviour component called `ARRenderingManager`.

In ARDK 3.0, rendering is handled by AR Foundation. The device camera is handled by a MonoBehaviour component called `ARCameraManager`. The composition of the camera frame and CG content is handled by a MonoBehaviour component called `ARCameraBackground`. For more information, see <a href="https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.1/manual/features/Camera/camera-components.html" target="_blank" rel="noopener noreferrer">Unity Camera Components</a> (opens in new window).

| ARDK 2.X | ARDK 3.0 |
|----|----|
| `[ARSessionManager]` `IsLightEstimationEnabled` | `[ARCameraManager]` `LightEstimation` |
| `[ARSessionManager]` `IsAutoFocusEnabled` | `[ARCameraManager]` `AutoFocus` |
| `[ARRenderingManager]` `RenderTarget` | Always set to Camera |
| `[ARRenderingManager]` `Camera` | Always the camera with the `ARCameraManager` |

### 3. Depth / Occlusion<a href="#3-depth--occlusion" class="hash-link" aria-label="Direct link to 3. Depth / Occlusion" title="Direct link to 3. Depth / Occlusion">​</a>

In AR, depth textures are used to dynamically occlude digital content.

In ARDK 2.X, depth textures were exposed through the `ARDepthManager`. Depth interpolation was done in the `ARDepthInterpolationAdapter` and semantic suppression of depth-based occlusion was set up in the `ARSemanticSegmentationManager`.

In ARDK 3.0, depth-based occlusion is handled by the `AROcclusionManager` provided by AR Foundation. Additional ARDK occlusion settings are now all enabled through the `LightshipOcclusionExtension`, such as interpolation modes, occlusion suppression, and occlusion stabilization.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>ARDK 2.X</th>
<th>ARDK 3.0</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>[ARDepthManager]</code> <code>KeyFrameFrequency</code></td>
<td><code>[LightshipOcclusionExtension]</code> <code>TargetFrameRate</code></td>
</tr>
<tr>
<td><code>[ARDepthManager]</code> <code>OcclusionMode</code></td>
<td>Always using DepthBuffer in <code>ARCameraBackground</code></td>
</tr>
<tr>
<td><code>[ARDepthManager]</code> <code>StabilizeOcclusionExperimental</code></td>
<td><code>[LightshipOcclusionExtension]</code> <code>OcclusionStabilization</code></td>
</tr>
<tr>
<td><code>[ARDepthManager]</code> <code>PreferSmootherEdges</code></td>
<td>Not supported yet</td>
</tr>
<tr>
<td><code>[ARDepthManager]</code> <code>Interpolation</code></td>
<td>Depth buffer always returned interpolated</td>
</tr>
<tr>
<td><code>[ARDepthInterpolationAdapter]</code> <code>Mode</code><br />
- <code>SampleFullScreen</code><br />
- <code>TrackOccludee</code></td>
<td><code>[LightshipOcclusionExtension]</code> <code>Mode</code><br />
- <code>Static</code><br />
- <code>SpecifiedGameObject</code></td>
</tr>
<tr>
<td><code>[ARDepthManager]</code> <code>Occludee</code></td>
<td><code>[LightshipOcclusionExtension]</code> <code>PrincipalOccludee</code></td>
</tr>
</tbody>
</table>

### 4. Meshing<a href="#4-meshing" class="hash-link" aria-label="Direct link to 4. Meshing" title="Direct link to 4. Meshing">​</a>

In ARDK 3.0, Meshing is exposed through a MonoBehaviour component called `ARMeshManager`, now provided by AR Foundation. In addition, ARDK-specific settings can be changed through the `LightshipMeshingExtension` component. The settings from ARDK 2.x are still included, but some are renamed:

| ARDK 2.X | ARDK 3.0 |
|----|----|
| `[ARMeshManager]` `FrameRate` | `[LightshipMeshingExtension]` `TargetFrameRate` |
| `[ARMeshManager]` `FrameRateTargetBlockSize` | `[LightshipMeshingExtension]` `MeshBlockSize` |
| `[ARMeshManager]` `MeshingRangeMax` | `[LightshipMeshingExtension]` `MaximumIntegrationDistance` |
| `[ARMeshManager]` `VoxelSize` | `[ARMeshManager]` `VoxelSize` |
| `[ARMeshManager]` `MeshPrefab` | `[ARMeshManager]` `MeshPrefab` |
| `[ARMeshManager]` `MeshRoot` | Fixed to XROrigin -\> CameraOffset -\> Trackables |
| `[ARMeshManager]` `FrameRateColliderUpdateThrottle` | `[ARMeshManager]` Handled by ConcurrentQueueSize |
| `[ARMeshManager]` `MeshVisibilitySettings` | Set via prefab material directly |

### 5. Planes<a href="#5-planes" class="hash-link" aria-label="Direct link to 5. Planes" title="Direct link to 5. Planes">​</a>

In ARDK 3.x, plane finding and visualization use AR Foundation's implementation of `ARPlaneManager`, a wrapper over ARKit and ARCore. This is similar to what was done in ARDK 2.x, but with differences at runtime. Please take a look at the AR Foundation Samples to better understand how to use `ARPlaneManager` from AR Foundation in your application.

| ARDK 2.X                   | ARDK 3.0                       |
|----------------------------|--------------------------------|
| `IARPlaneAnchor`           | `ARPlane`                      |
| `ARSession.AnchorsAdded`   | `ArPlaneManager.planesChanged` |
| `ARSession.AnchorsUpdated` | `ArPlaneManager.planesChanged` |
| `ARSession.AnchorsMerged`  | `ArPlaneManager.planesChanged` |
| `ARSession.AnchorsRemoved` | `ArPlaneManager.planesChanged` |

### 6. Semantics<a href="#6-semantics" class="hash-link" aria-label="Direct link to 6. Semantics" title="Direct link to 6. Semantics">​</a>

In ARDK 3.0, semantics are still handled by `ARSemanticSegmentationManager`. The new manager offers functions that get packed semantics and confidence values per channel without having to prepare confidence channels. Interpolation can be done with a `SamplerMatrix` that is returned on every semantic frame. Semantic depth suppression settings have been moved to `LightshipOcclusionExtension`.

| ARDK 2.X | ARDK 3.0 |
|----|----|
| `KeyFrameFrequency` | `TargetFrameRate` |
| `DepthSuppressionChannels` | `[LightshipOcclusionExtension]` `SuppressionChannels` |
| `PersistentConfidences` | Now directly accessed through the manager |
| `Interpolation` | Done with `SamplerMatrix` (see samples) |

### 7. Gameboard / LightshipNavMesh<a href="#7-gameboard--lightshipnavmesh" class="hash-link" aria-label="Direct link to 7. Gameboard / LightshipNavMesh" title="Direct link to 7. Gameboard / LightshipNavMesh">​</a>

The Gameboard feature from ARDK 2.X has been renamed to LightshipNavMesh in ARDK 3.0.

The implementation is the same, but visualization is now handled by an additional component called `LightshipNavMeshRenderer`.

### 8. VPS Coverage<a href="#8-vps-coverage" class="hash-link" aria-label="Direct link to 8. VPS Coverage" title="Direct link to 8. VPS Coverage">​</a>

`VpsCoverageExampleManager` has been reworked into the `CoverageClientManager` Component. Private AR locations can now be added through an `ARLocationManifest` instead of a `VpsCoverageResponse` object.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>ARDK 2.X</th>
<th>ARDK 3.0</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>[VpsCoverageExampleManager]</code> <code>CoverageClientRuntime</code></td>
<td>Always calls live service</td>
</tr>
<tr>
<td><code>[VpsCoverageExampleManager]</code><br />
<code>MockResponses (ScriptableObject)</code></td>
<td><code>[CoverageClientManager]</code><br />
<code>PrivateARLocations (ARLocationManifest)</code></td>
</tr>
<tr>
<td><code>[VpsCoverageExampleManager]</code> <code>SpoofLocation</code><br />
- <code>Lat_degrees</code><br />
- <code>Lon_degrees</code></td>
<td><code>[CoverageClientManager]</code> <code>SpoofLocationUseCurrentLocation</code><br />
- <code>QueryLatitude</code><br />
- <code>QueryLongitude</code></td>
</tr>
<tr>
<td><code>[CoverageClientManager]</code> <code>VoxelSizeTargetImage</code></td>
<td>The <code>[CoverageClientManager]</code> is not tied to a sample anymore</td>
</tr>
</tbody>
</table>

</div>

</div>
