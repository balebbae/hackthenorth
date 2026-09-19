---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/urp/
title: How to Set Up ARDK with the Universal Render Pipeline
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Set Up ARDK with the Universal Render Pipeline

</div>

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

- Completion of [Setting Up the Niantic SDK in Unity](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/)
- Completion of <a href="https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/manual/project-setup/universal-render-pipeline.html" target="_blank" rel="noopener noreferrer">Configure URP for AR Foundation</a>

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

**Meta Quest 3** has platform-specific requirements for developing with the **Universal Render Pipeline (URP)**. More information and instructions can be found <a href="https://docs.unity3d.com/Packages/com.unity.xr.meta-openxr@2.2/manual/get-started/graphics-settings.html#universal-render-pipeline" target="_blank" rel="noopener noreferrer">here</a>.

</div>

</div>

## Setting up URP with Lightship Occlusion<a href="#setting-up-urp-with-lightship-occlusion" class="hash-link" aria-label="Direct link to Setting up URP with Lightship Occlusion" title="Direct link to Setting up URP with Lightship Occlusion">​</a>

Occlusions made using the ARFoundation `AROcclusionManager` will work out-of-the-box with just the `ARBackgroundRendererFeature` added, as in the ARFoundation instructions. However, when using the `LightshipOcclusionExtension` to enhance occlusions, you must also add a `LightshipOcclusionExtensionFeature` to your URP renderer. For more information, see [How to Set Up Real-World Occlusion](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/setup_real_world_occlusion/).

</div>

</div>
