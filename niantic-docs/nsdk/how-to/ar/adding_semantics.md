---
source: https://www.nianticspatial.com/docs/nsdk/how-to/ar/adding_semantics/
title: Adding Scene Segmentation
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Adding Scene Segmentation

</div>

NSDK provides this unique feature through the new **`XRSemanticsSubsystem`** class. The `ARSemanticSegmentationManager` makes this subsystem's data available as a MonoBehaviour and manages the subsystem's lifecycle.

## Unity Scene Integration<a href="#unity-scene-integration" class="hash-link" aria-label="Direct link to Unity Scene Integration" title="Direct link to Unity Scene Integration">​</a>

To run scene segmentation in your scene, add an `ARSemanticSegmentationManager` component. By default, the `ARSemanticSegmentationManager` is simple, with only one exposed parameter for framerate settings in its Inspector window.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/ar_semantic_segmentation_manager-02d7e0a31a4c1e763dc58eba2207ae5c.png" style="width:50.0%" alt="ARSemanticSegmentationManager Inspector" />

</div>

\

## More Information<a href="#more-information" class="hash-link" aria-label="Direct link to More Information" title="Direct link to More Information">​</a>

While `ARSemanticSegmentationManager` itself is uncomplicated, there are features in other NSDK components that require one to be present and active in the scene. These include:

- [Occlusion suppression](https://www.nianticspatial.com/docs/nsdk/how-to/ar/adding_occlusion/) in NsdkOcclusionExtension
- [Mesh filtering](https://www.nianticspatial.com/docs/nsdk/how-to/ar/meshing/semantic_mesh_filtering/) in NsdkMeshingExtension

For a full walkthrough of how to add scene segmentation to your project, see [How to Query Scene Segmentation and Highlight Semantic Channels](https://www.nianticspatial.com/docs/nsdk/how-to/ar/query_semantics_real_objects/).

</div>

</div>
