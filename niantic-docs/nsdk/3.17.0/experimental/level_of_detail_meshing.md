---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/experimental/level_of_detail_meshing/
title: Level of Detail Meshing
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Level of Detail Meshing (Experimental)

</div>

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Niantic Spatial Meshing reconstructs the visible geometry of the scene, allowing AR characters and objects to interact physically with their environment. By default, the spatial resolution used for this reconstruction is constant. Level of Detail Meshing is a new experimental feature that changes the local resolution of the reconstruction based on how far the player is from specific points in space. While they are far away, world details are rendered coarsely, but as they approach, the resolution becomes finer, showing a more precise version of the geometry.

## Enabling Levels of Detail<a href="#enabling-levels-of-detail" class="hash-link" aria-label="Direct link to Enabling Levels of Detail" title="Direct link to Enabling Levels of Detail">​</a>

To enable Level of Detail Meshing, expand the `XROrigin` in the **Hierarchy** and select the object that contains your Lightship Meshing Extension. Then, in the **Inspector** under "Experimental Meshing Options," check the box for "Enable Levels of Detail". Choose a value from 2 to 5, with 5 providing the most detail and 2 the least. (Setting this to 1 or 0 will result in the default behavior: no additional levels of detail.)

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>caution

</div>

<div class="admonitionContent_BuS1">

Enabling levels of detail in conjunction with **Distance-based Volumetric Cleanup** is not recommended.

</div>

</div>

## How is Level of Detail Defined?<a href="#how-is-level-of-detail-defined" class="hash-link" aria-label="Direct link to How is Level of Detail Defined?" title="Direct link to How is Level of Detail Defined?">​</a>

When a new Mesh Block is surfaced to Unity, it creates a new GameObject in the `Trackables` section of the Hierarchy. The names for these GameObjects follow the format `Mesh-<32 digit number>-<32 zeroes>`, where the first digit of the 32-digit number is the level of detail used to reconstruct the triangles in the mesh. Each level doubles the voxel size and block size for that mesh region. For example, a Level 3 mesh block covers a cubic region with sides 8 times longer than a Level 1 mesh block and contains voxels that are 8 times larger.

## Level of Detail Setup Examples<a href="#level-of-detail-setup-examples" class="hash-link" aria-label="Direct link to Level of Detail Setup Examples" title="Direct link to Level of Detail Setup Examples">​</a>

We provide two examples for how to set up meshing level of detail in your project. The first example, taken at a distance of 30 meters, is suitable for indoor use, while the second, taken at 100 meters, is better for outdoor experiences.

Example indoor configuration:

<img src="https://www.nianticspatial.com/docs/assets/images/30m_lod_example-e924a5e0c661dd9b8eb7037c164d522f.gif" width="600" alt="Example Indoor Configuration." />

Example outdoor configuration:

<img src="https://www.nianticspatial.com/docs/assets/images/100m_lod_example-572831d1161fa61e7175219426e450ee.gif" width="600" alt="Example Outdoor Configuration." />

</div>

</div>
