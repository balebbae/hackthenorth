---
source: https://www.nianticspatial.com/docs/nsdk/features/semantics/
title: Niantic Spatial Scene Segmentation
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Scene Segmentation

</div>

Scene Segmentation is the process of classifying every pixel in an image into meaningful categories, creating a detailed understanding of the environment. This capability powers mission-critical applications enabling accurate scene interpretation, safer autonomous navigation, precise spatial analytics, and context-aware decision-making at scale.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/SemanticsWithTrees-94f3ab67a28457e1b4d12d80f927bcf9.png" width="625" alt="Image with the tree channel" />

</div>

## What's new?<a href="#whats-new" class="hash-link" aria-label="Direct link to What&#39;s new?" title="Direct link to What&#39;s new?">​</a>

NSDK serves semantic predictions in two forms:

1.  A buffer of unsigned integers for each pixel in the viewport, referred to as "packed semantic channels." The 32 bits of each integer correspond to a semantic channel and are either enabled (value is 1) or disabled (value is 0) depending on whether an object in that channel exists at that pixel. A pixel can have more than one label, e.g. both `ground` and `natural_ground`.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/buffer_diagram-45da1070941337d6be8640c37238290d.png" width="800" alt="Buffer Diagram" />

</div>

2.  For each semantic channel, there is a buffer of normalized (between 0 and 1) float values for each pixel in the viewport. These floats show the probability that their pixel should be classified as the specified semantic channel.

## Available Semantic Channels<a href="#available-semantic-channels" class="hash-link" aria-label="Direct link to Available Semantic Channels" title="Direct link to Available Semantic Channels">​</a>

The following table lists the current set of semantic channels. Because the ordering of channels in this list may change with new versions of NSDK, we recommend that you use names rather than index values in your app. Use the XRSemanticsSubsystem.TryGetChannelNames method or ARSemanticSegmentationManager.ChannelNames property to verify names at runtime.

Because channel names are read from a neural network model, there will be slight delays when the scene segmentation subsystem starts, while the model is initialized, and before channel names are available. This delay can be reduced by downloading the model in advance. See [Neural Network Model Preloading](https://www.nianticspatial.com/docs/nsdk/features/model_preloading/) for more information.

| Index | Channel Name | Notes |
|----|----|----|
| \[0\] | `sky` | Includes clouds. Does not include fog. |
| \[1\] | `ground` | Includes everything in `natural_ground` and `artificial_ground`. `Ground` may be more reliable than the combination of the two where there is ambiguity about natural vs artificial. |
| \[2\] | `natural_ground` | Includes dirt, grass, sand, mud, and other organic / natural ground. Ground with heavy vegetation or foliage may be detected as `foliage` instead. |
| \[3\] | `artificial_ground` | Includes roads, sidewalks, tracks, carpets, rugs, flooring, paths, gravel, and some playing fields. |
| \[4\] | `grass` | Grassy ground, e.g. lawns, rather than tall grass. |

## Learn More<a href="#learn-more" class="hash-link" aria-label="Direct link to Learn More" title="Direct link to Learn More">​</a>

- [How to Query Scene Segmentation and Highlight Semantic Channels](https://www.nianticspatial.com/docs/nsdk/how-to/ar/query_semantics_real_objects/)
- [How to Exclude Semantic Channels with Mesh Filtering](https://www.nianticspatial.com/docs/nsdk/how-to/ar/meshing/semantic_mesh_filtering/)

</div>

</div>
