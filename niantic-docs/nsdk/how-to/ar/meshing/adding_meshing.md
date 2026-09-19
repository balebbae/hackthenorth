---
source: https://www.nianticspatial.com/docs/nsdk/how-to/ar/meshing/adding_meshing/
title: Adding Meshing to Your Project
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Adding Meshing to Your Project

</div>

By placing the standard <a href="https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.0/api/UnityEngine.XR.ARFoundation.ARMeshManager.html" target="_blank" rel="noopener noreferrer"><code>ARMeshManager</code></a> in a scene, developers can access a live mesh that allows virtual objects to interact with the real-world environment. For example, a virtual ball thrown into a meshed scene will realistically bounce off of the floor and walls.

When the Niantic Spatial SDK (NSDK) is enabled in Unity, meshing is still provided through Unity's <a href="https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.0/manual/features/meshing.html" target="_blank" rel="noopener noreferrer">AR Foundation Meshing Subsystem</a> and enabled with the standard <a href="https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.0/api/UnityEngine.XR.ARFoundation.ARMeshManager.html" target="_blank" rel="noopener noreferrer"><code>ARMeshManager</code></a>. NSDK overrides the default implementation and provides Niantic Spatial's proprietary meshing technology through the standard interface.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

Niantic Spatial Meshing works on lidar and non-lidar devices running either Android or iOS. For support on lidar devices, ensure that the `Prefer LiDAR if Available` setting is checked in **Niantic Spatial Development Kit Settings** and an <a href="https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.0/api/UnityEngine.XR.ARFoundation.AROcclusionManager.html" target="_blank" rel="noopener noreferrer">AROcclusionManager</a> is present in your scene.

</div>

</div>

## Mesh Chunks<a href="#mesh-chunks" class="hash-link" aria-label="Direct link to Mesh Chunks" title="Direct link to Mesh Chunks">​</a>

To lighten the application's compute workload as the mesh grows, NSDK breaks the mesh up into chunks. The three-dimensional world is divided into a regular grid of "blocks" of a fixed size. When meshing is running, new mesh chunks will be created in the scene Hierarchy underneath `XROrigin` \> `Trackables`. Each block has its own renderer and collider defined by the Mesh Prefab specified in the `ARMeshManager`. Mesh chunks are continually updated as new data is added to the 3D representation.

## Meshing Extensions<a href="#meshing-extensions" class="hash-link" aria-label="Direct link to Meshing Extensions" title="Direct link to Meshing Extensions">​</a>

To offer more configurability than the standard `ARMeshManager`, NSDK provides an optional **`Nsdk Meshing Extension`** component. `Nsdk Meshing Extension` provides extra options to allow you to tweak meshing rules for distance, quality and clean-up.

Add a `Nsdk Meshing Extension` component to the same game object as `ARMeshManager` to gain access to these settings:

<img src="https://www.nianticspatial.com/docs/assets/images/lightship_meshing_extension-6b357739a0c28229c7a0af4dd9b7b61a.png" style="width:33.0%" alt="Nsdk Meshing Extension settings" />

- **Target Frame Rate:** The number of times per second to run the mesh update routine. This should be no higher than the AR Session update rate.
- **Fuse Keyframes Only:** Enabling this improves mesh accuracy at the cost of a lower update frequency.
- **AR Fusion Parameters:**
  - **Maximum Integration Distance:** The far distance threshold from the device sensor for integrating depth samples into the 3D scene, in meters. New mesh blocks will not be generated further than this distance from the camera.
  - **Voxel Size:** The size of individual voxel elements in the scene, in meters. Higher values will save memory but also reduce the precision of the surfaces.
  - **Enable Distance-Based Volumetric Cleanup:** Enable this to save memory and smooth latency by cleaning up already-processed elements in the feature's volumetric representation (once they move outside the region where new meshes are generated). This will not remove previously-generated mesh.
- **AR Meshing Parameters:**
  - **Mesh Block Size:** The size of the mesh blocks used for generating the mesh filter and mesh collider.
  - **Mesh Culling Distance:** The distance from the user where mesh blocks will be removed from the scene. Set to 0 to disable distance-based culling.
  - **Enable Mesh Decimation:** Enable to save memory by removing excess triangles from the mesh.
- **Mesh Filtering:**
  - **Is Mesh Filtering Enabled:** Check this box to enable mesh filtering. See [Mesh Filtering](https://www.nianticspatial.com/docs/nsdk/how-to/ar/meshing/semantic_mesh_filtering/) for more information.
  - **Semantic Segmentation Manager:** When mesh filtering is enabled, an `AR Semantic Segmentation Manager` component is required in the scene.
  - **Allow List:** If populated, only these semantic classes will be allowed in the mesh.
  - **Block List:** If populated, these semantic classes will be excluded from the mesh.
- **Experimental Meshing Options:**
  - **Enable Levels of Detail:** Check this box to enable the experimental level of detail meshing feature which saves memory and reduces latency. For more information, see the [Meshing Level of Detail](https://www.nianticspatial.com/docs/nsdk/experimental/level_of_detail_meshing/) feature page.

## Mesh Filtering<a href="#mesh-filtering" class="hash-link" aria-label="Direct link to Mesh Filtering" title="Direct link to Mesh Filtering">​</a>

Mesh Filtering uses [semantic segmentation](https://www.nianticspatial.com/docs/nsdk/features/semantics/) to identify sections of a mesh as common parts of the world, such as `ground` or `sky`, then uses that information to determine what should be part of the final mesh with a user-defined allowlist and blocklist. For example, a blocklist containing `sky` would remove the sky from the final mesh, while an allowlist containing `ground` would exclude everything but the ground. See [How to Exclude Semantic Channels with Mesh Filtering](https://www.nianticspatial.com/docs/nsdk/how-to/ar/meshing/semantic_mesh_filtering/) for more information.

<img src="https://www.nianticspatial.com/docs/assets/images/semantic_filter_allow-d8aabaeaace026ee56beb8a1630684f7.png" width="600" alt="Example usage of a semantic filtering allowlist" />

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/mesh_filtering-4268c7ddda927f499d121d460d1ec42d.gif" width="300" alt="Example of Mesh Filtering being turned on and off" />

</div>

## Long-Distance Meshing<a href="#long-distance-meshing" class="hash-link" aria-label="Direct link to Long-Distance Meshing" title="Direct link to Long-Distance Meshing">​</a>

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>caution

</div>

<div class="admonitionContent_BuS1">

These settings are only recommended for high-end devices. For information on supported devices, see the <a href="https://developers.google.com/ar/devices" target="_blank" rel="noopener noreferrer">Google ARCore device list</a> and <a href="https://www.apple.com/augmented-reality" target="_blank" rel="noopener noreferrer">Apple ARKit device list</a>.

</div>

</div>

You can configure your application to mesh over much longer distances by increasing the **Voxel Size**, turning on **Enable Distance-Based Volumetric Cleanup** and increasing the **Maximum Integration Distance** and **Mesh Culling Distance** to between 20 and 40 meters. For example, try out the following settings:

- **Target Frame Rate**: 20
- **AR Fusion Parameters**:
  - **Maximum Integration Distance**: 40
  - **Voxel Size**: 0.05
  - **Enable Distance-Based Volumetric Cleanup**: True
- **AR Meshing Parameters**:
  - **Mesh Block Size**: 1.4
  - **Mesh Culling Distance**: 40 (should be \>= Maximum integration distance)
  - **Enable Mesh Decimation**: True

If you use these settings, increase the **Concurrent Queue Size** setting in the `ARMeshManager` component as well to make sure that the manager can keep up with the amount of tiles being surfaced. This will increase CPU and GPU usage, so we recommend testing thoroughly on a variety of devices.

<div style="margin-left:15px">

<img src="https://www.nianticspatial.com/docs/assets/images/meshing_settings-e4e2c0b8a20558661082be7a2ecdb987.jpg" style="width:60.0%" alt="Long Distance Meshing example" /><img src="https://www.nianticspatial.com/docs/assets/images/long_dist_mesh-5bea57676b0db00da3735fef587f5836.gif" style="width:25.0%" alt="Long Distance Meshing example" />

</div>

## Lidar Devices<a href="#lidar-devices" class="hash-link" aria-label="Direct link to Lidar Devices" title="Direct link to Lidar Devices">​</a>

On lidar devices, it is possible to use Niantic Spatial Meshing with either lidar depth or NSDK depth. To use lidar depth, ensure that **Prefer LiDAR if Available** is enabled in the Niantic Spatial Development Kit settings menu (**NSDK** top menu \> **Settings**) and that an <a href="https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.0/api/UnityEngine.XR.ARFoundation.AROcclusionManager.html" target="_blank" rel="noopener noreferrer">AROcclusionManager</a> is present in the scene. (Note that meshing will still be supported even if **No Occlusion** is selected as the **Occlusion Preference Mode**.)

Lidar depth will only support a maximum integration distance of around five meters. If you wish to generate mesh blocks farther away from the user, disable **Prefer LiDAR if Available** to use NSDK depth instead.

## More Information<a href="#more-information" class="hash-link" aria-label="Direct link to More Information" title="Direct link to More Information">​</a>

The [NSDK sample project](https://www.nianticspatial.com/docs/nsdk/sample_projects/) includes an example of running meshing.

See [How to Exclude Semantic Channels with Mesh Filtering](https://www.nianticspatial.com/docs/nsdk/how-to/ar/meshing/semantic_mesh_filtering/) for a guide of how to set up a project with meshing.

See [How to Add Physics to a Meshed Scene](https://www.nianticspatial.com/docs/nsdk/how-to/ar/meshing/adding_meshing/) for how to use meshing to simulate realistic collisions.

</div>

</div>
