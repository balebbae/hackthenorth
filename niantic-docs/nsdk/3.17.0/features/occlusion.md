---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/features/occlusion/
title: Occlusion
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Niantic Spatial Occlusion

</div>

## Understanding Occlusion in Augmented Reality<a href="#understanding-occlusion-in-augmented-reality" class="hash-link" aria-label="Direct link to Understanding Occlusion in Augmented Reality" title="Direct link to Understanding Occlusion in Augmented Reality">​</a>

If a virtual object appears in front of a real-world object that it should actually be behind, the AR illusion is broken. AR should seamlessly blend virtual objects into the real world and impart a sense of presence. Occlusion gives depth to virtual objects, allowing them to appear behind or in front of real-world objects. With proper occlusion, virtual content will appear to be physically present in the scene, blocking view of objects dynamically as the user moves their device through the space.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/occlusion_off-347bdfc452e31d914d19be588955601f.png" width="430" alt="An example of AR without occlusion" /><img src="https://www.nianticspatial.com/docs/assets/images/occlusion_on-fbb873aa84345fd7f44f01d4b05a1e4c.png" width="430" alt="An example of AR with occlusion" />

</div>

<div style="text-align:center">

***Left:** AR without occlusion. **Right:** AR with real-world occlusion from NSDK.*

</div>

## Occlusion in NSDK<a href="#occlusion-in-nsdk" class="hash-link" aria-label="Direct link to Occlusion in NSDK" title="Direct link to Occlusion in NSDK">​</a>

Occlusion is powered by depth sensing, and applications can choose which type of occlusion to use. Niantic Spatial SDK (NSDK) provides features that allow for swapping between dynamic and mesh-based occlusion depending on the needs of your application. This implementation works on any NSDK device or platform, regardless of lidar capability.

*An example of occlusion as characters walk behind a tree*

### Types of Occlusion in NSDK<a href="#types-of-occlusion-in-nsdk" class="hash-link" aria-label="Direct link to Types of Occlusion in NSDK" title="Direct link to Types of Occlusion in NSDK">​</a>

**Instant Dynamic Occlusion (Fast, Noisy)**

Dynamic occlusion directly refers to a [depth buffer](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/depth/) to perform occlusions. Depth buffers are either lidar frames or generated depth from NSDK using RGB camera frames. Since depth data is generated quickly, this type of occlusion is good at capturing fast-moving objects, like people or pets. However, just-in-time occlusion will not always line up with meshing and may over/under-occlude meshed objects.

**Mesh Occlusion (Stable, Slow Occlusion)**

Mesh-based occlusion uses a [3D mesh built from many depth frames and device poses by NSDK](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/meshing/) to determine occlusion surfaces. This technique averages a range of depth measurements, making it more accurate for static regions of the environment. This approach is more stable than instant dynamic occlusion and produces cleaner results, but updates are less frequent. Dynamic agents (like people and pets) may occlude less reliably.

**Instant Depth + Mesh-Blended Occlusion** (Unity SDK only)

**Occlusion Stabilization** has the advantages of both modes. It combines the fast response time of instant occlusion with the stable averaging effect of meshing. A depth map is produced from the NSDK mesh, rendered to a texture and combined with the latest depth buffer in a way that avoids flickering and Z-fighting.

## More Information<a href="#more-information" class="hash-link" aria-label="Direct link to More Information" title="Direct link to More Information">​</a>

For details on how to use this feature, see [How to Setup Real-World Occlusion](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/setup_real_world_occlusion/).

</div>

</div>
