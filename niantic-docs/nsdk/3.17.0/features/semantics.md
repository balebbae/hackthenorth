---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/features/semantics/
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

The following table lists the current set of semantic channels. Because the ordering of channels in this list may change with new versions of ARDK, we recommend that you use names rather than index values in your app. Use the XRSemanticsSubsystem.TryGetChannelNames method or ARSemanticSegmentationManager.ChannelNames property to verify names at runtime.

Because channel names are read from a neural network model, there will be slight delays when the scene segmentation subsystem starts, while the model is initialized, and before channel names are available. This delay can be reduced by downloading the model in advance. See [Neural Network Model Preloading](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/model_preloading/) for more information.

Click to expand the table of semantic channels

<div>

<div class="collapsibleContent_i85q">

| Index | Channel Name | Notes |
|----|----|----|
| \[0\] | `sky` | Includes clouds. Does not include fog. |
| \[1\] | `ground` | Includes everything in `natural_ground` and `artificial_ground`. `Ground` may be more reliable than the combination of the two where there is ambiguity about natural vs artificial. |
| \[2\] | `natural_ground` | Includes dirt, grass, sand, mud, and other organic / natural ground. Ground with heavy vegetation or foliage may be detected as `foliage` instead. |
| \[3\] | `artificial_ground` | Includes roads, sidewalks, tracks, carpets, rugs, flooring, paths, gravel, and some playing fields. |
| \[4\] | `water` | Includes rivers, seas, ponds, lakes, pools, waterfalls, some puddles. Does not include drinking water, water in cups, bowls, sinks, baths. Water with strong reflections may be detected as what is in the reflection instead of as water. |
| \[5\] | `person` | Includes body parts, hair, and clothes worn. Does not include accessories or carried objects. Does not distinguish between individuals. Mannequins, toys, statues, paintings, and other artistic expressions of a person are not considered a “person”, though some detections may occur. Photorealistic images of a person are detected as a “person”. Model performance may suffer when a person is partially visible in the image or is in an unusual body posture, such as when crouching or widely spreading their arms. |
| \[6\] | `building` | Includes residential and commercial buildings, both modern and traditional. Should not be considered synonymous with walls. |
| \[7\] | `foliage` | Includes bushes, shrubs, leafy parts and trunks of trees, potted plants, and flowers. |
| \[8\] | `grass` | Grassy ground, e.g. lawns, rather than tall grass. |

</div>

</div>

## Experimental Semantic Channels<a href="#experimental-semantic-channels" class="hash-link" aria-label="Direct link to Experimental Semantic Channels" title="Direct link to Experimental Semantic Channels">​</a>

Niantic VPS also offers a set of experimental semantic channels. Because they are experimental, these channels may need accuracy improvements; if you find an issue with them, please provide feedback in the <a href="https://community.lightship.dev/c/bugs/5" target="_blank" rel="noopener noreferrer">Niantic Spatial Developer Community</a>.

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention

</div>

<div class="admonitionContent_BuS1">

Experimental features are not recommended for use in production-level applications!

</div>

</div>

Click to expand the experimental channels

<div>

<div class="collapsibleContent_i85q">

| Index | Channel Name | Notes |
|----|----|----|
| \[9\] | `flower_experimental` | The part of a plant that has brightly colored petals and provides pollen. Does not include any green parts (stems, leaves). |
| \[10\] | `tree_trunk_experimental` | The part of a tree that connects the leafy crown and branches with its roots. Does not include leaves, branches, flowers, or processed/cut wood (logs). |
| \[11\] | `pet_experimental` | Only dogs and cats. Not designed to work on soft toys of dogs and cats. |
| \[12\] | `sand_experimental` | Finely divided rock and mineral particles. Sand has various compositions but is defined by its small grain size. Includes all types of sandy/gravelly surfaces found on the floor/ground, wet sand, and sandcastles/sand art. Does not include dirt, soil. |
| \[13\] | `tv_experimental` | Screen portion of any digital device. Includes both screens turned on and screens turned off. Excludes the frame (“bezel”) around the screen, and stands. |
| \[14\] | `dirt_experimental` | Includes mud and dust covering the ground. May overlap significantly with sand. Includes dirt roads. |
| \[15\] | `vehicle_experimental` | includes all components of vehicles. Covers all types of cars and trucks. Intended to also work on (but accuracy may vary) motorcycles, bicycles, rickshaws, horse carriages, tuk-tuks, trains/trams, boats/ships, airplanes/helicopters/hovercrafts. |
| \[16\] | `food_experimental` | Anything that can be consumed as “food” and not “drink” by human beings, including salt & pepper, and boxes/packaging likely to contain food or ingredients. Does not include live animals, pet food, or plates/dishes the food is served on. |
| \[17\] | `loungeable_experimental` | All objects intended to be used to sit on. Includes beds (including the legs and bases), and legs and bases for chairs or sofas. Does not include pet beds/blankets, or any empty spaces/gaps in chairs or sofas. |
| \[18\] | `snow_experimental` | Atmospheric water vapor frozen into ice crystals and falling in light white flakes or covering the ground as a white layer. Includes clean and dirty snow. Includes icebergs and icicles, ice/snow sculptures, igloos/snow houses. Does not include ice in drinks, snow in the sky. |

</div>

</div>

## Learn More<a href="#learn-more" class="hash-link" aria-label="Direct link to Learn More" title="Direct link to Learn More">​</a>

- [How to Query Scene Segmentation and Highlight Semantic Channels](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/query_semantics_real_objects/)
- [How to Exclude Semantic Channels with Mesh Filtering](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/meshing/semantic_mesh_filtering/)

</div>

</div>
