---
source: https://www.nianticspatial.com/docs/nsdk/how-to/ar/depth/adding_depth/
title: Adding Depth to Your Project
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Adding Depth to Your Project

</div>

When using Unity, the Niantic Spatial SDK (NSDK) integrates seamlessly with **Unity’s AR Foundation.** This means your application can access depth data through Unity’s standard **AR Occlusion Manager** component.

<img src="https://www.nianticspatial.com/docs/assets/images/ar_occlusion_manager-1f6826f8f0342da5ba5d88697288cae8.jpg" width="433" alt="AROcclusionManager" />

To enable depth in your scene, simply add an AROcclusionManager to your AR camera object. NSDK automatically provides depth data through this component when configured correctly.

While the AROcclusionManager interface mirrors that of AR Foundation, its configuration options behave slightly differently under NSDK:

- **Environment Depth Mode** — This parameter controls which NSDK neural network architecture is used for depth estimation:
  - **Medium:** Uses Niantic’s in-house *MultiDepth* architecture for balanced accuracy and performance.
  - **Best:** Uses a modified *MultiDepth Anti-Flicker* model that takes into account the previous frame’s depth map to improve temporal stability.
  - **Fastest:** Uses a smaller, lightweight model optimized for speed, with potential trade-offs in accuracy.
- **Temporal Smoothing** — *Not supported* in NSDK. Temporal consistency is instead managed internally through the anti-flicker depth model when the **Best** mode is selected.
- **Human Segmentation** — This section is unused in NSDK. For segmentation features such as detecting humans or other object classes, refer to the **Scene Segmentation** feature in the Niantic SDK, which provides broader category support.
- **Occlusion Preference Mode** — In standard AR Foundation, this setting toggles between environment and human occlusion. In NSDK, it is simplified: use **No Occlusion** to disable depth-based occlusion entirely.

## More Information<a href="#more-information" class="hash-link" aria-label="Direct link to More Information" title="Direct link to More Information">​</a>

The [NSDK sample project](https://www.nianticspatial.com/docs/nsdk/sample_projects/) includes an example of running depth.

Also, see [How to Convert a Screen Point to Real-World Position Using Depth](https://www.nianticspatial.com/docs/nsdk/how-to/ar/depth/convert_point_world_position/) for a guide of how to set up a project with depth.

</div>

</div>
