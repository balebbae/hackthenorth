---
source: https://www.nianticspatial.com/docs/nsdk/features/meshing/
title: Meshing
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Niantic Spatial Meshing

</div>

## Understanding Meshing in Augmented Reality<a href="#understanding-meshing-in-augmented-reality" class="hash-link" aria-label="Direct link to Understanding Meshing in Augmented Reality" title="Direct link to Understanding Meshing in Augmented Reality">​</a>

The nature of augmented reality requires physical space to be perceived and understood so that graphics and contextual information are correct from the user's point of view. Some coarse augmentation is possible knowing only the user's location and heading. However, augmenting nearby physical space at a high granularity involves modeling the physical surfaces around the user. The most efficient model for rendering physical surfaces with standard compute hardware is the polygon mesh, the same model that GPUs were originally developed to accelerate. By assembling a sufficient number of 3D triangles (each defined by three vertices, or points, and a normal vector, or direction), it is possible to model physical surfaces and shapes.

Meshing is most valuable when accurate, continuous geometry of the environment is needed—such as **physics-based interactions, realistic object anchoring, obstacle-aware navigation, and spatial UI**. It is especially useful in complex indoor spaces, delivering consistent world awareness and rich environment interaction wherever users are. Achieving this in **real time** on performance-constrained mobile devices and across **many phone and head-mounted platforms** is a challenge. This is where Niantic Spatial SDK comes in.

## Meshing in NSDK<a href="#meshing-in-nsdk" class="hash-link" aria-label="Direct link to Meshing in NSDK" title="Direct link to Meshing in NSDK">​</a>

Using depth data and device tracking, the Niantic Spatial SDK (NSDK) reconstructs the surroundings into a dynamic mesh of triangular geometry, organized into mesh blocks that update as the user moves. The meshing feature is **highly configurable** for operation at different levels of performance and detail according to the needs of the AR application. Meshes produced by the SDK can be used for visualization, collision detection, occlusion and more.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/falling_objects_mesh-5f2585acbdb11eb9713a53bb4d7a9b9b.gif" style="width:300px;height:645px;object-fit:cover" alt="Falling Objects on the Gandhi Statue" />

</div>

*An example of collision detection in an AR scene with Niantic Spatial meshing.*

The mesh is represented by arrays of vertices, indices and normals. The **indices** array defines the triangle faces of the mesh by listing groups of three indices. Each index refers to an entry in the **vertex** array, and each group of three indices defines a triangle. Each vertex has a **normal** vector that indicates which direction the surface is facing. The coordinates of the vertices are with respect to the coordinate system of the pose and depth data provided by the AR platform.

## Mesh Chunks<a href="#mesh-chunks" class="hash-link" aria-label="Direct link to Mesh Chunks" title="Direct link to Mesh Chunks">​</a>

When an AR user explores a large area with the meshing feature, the size of the mesh can grow to become inconvenient to update during each frame. To lighten the application's compute workload as the mesh grows, NSDK breaks the mesh up into chunks. The meshing feature divides the three-dimensional world into a regular grid of blocks, and the mesh that it builds is segmented into **chunks**, with each mesh chunk contained within a block of space. Mesh chunks are continually updated as new depth data is ingested by the feature.

When the app requests new mesh data, it first receives an array of chunks IDs and update flags. The **update** flag for a chunk will only be true if that chunk has been updated since the last time that the application read its mesh data. For each chunk with a high update flag, the app can request that chunk's arrays of vertices, faces and normals. This allows the application to optimize its workload and only update mesh chunks that actually require an update.

## Mesh Filtering<a href="#mesh-filtering" class="hash-link" aria-label="Direct link to Mesh Filtering" title="Direct link to Mesh Filtering">​</a>

**Mesh Filtering** uses [Scene Segmentation](https://www.nianticspatial.com/docs/nsdk/features/semantics/) to identify sections of a mesh as common parts of the world, such as `ground` or `sky` and then determine what should be included in the final mesh with a user-defined allowlist and blocklist. For example, a blocklist containing `sky` would remove the sky from the final mesh, while an allowlist containing `ground` would exclude everything but the ground. See [How to Exclude Semantic Channels with Mesh Filtering](https://www.nianticspatial.com/docs/nsdk/how-to/ar/meshing/semantic_mesh_filtering/) for more information.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/mesh_filtering-4268c7ddda927f499d121d460d1ec42d.gif" width="300" alt="Example of Mesh Filtering being turned on and off" />

</div>

*Changing the mesh filter to only include the ground.*

## Levels of Detail<a href="#levels-of-detail" class="hash-link" aria-label="Direct link to Levels of Detail" title="Direct link to Levels of Detail">​</a>

NSDK provides an experimental option to use **levels of detail** in the mesh. Turning this option on reduces the detail in far-away mesh surfaces, leading to more efficient compute. Instead of a simple three-dimensional grid, levels of detail adds a user-defined number of sub-levels for each spatial block. When the user is far away from a block, only the coarsest level of detail is used to build the mesh there. If the user approaches it, the mesh data in that block becomes more detailed and precise. For more information, see [Level of Detail Meshing](https://www.nianticspatial.com/docs/nsdk/experimental/level_of_detail_meshing/).

</div>

</div>
