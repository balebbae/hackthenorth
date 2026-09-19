---
source: https://www.nianticspatial.com/docs/nsdk/how-to/ar/urp/
title: How to Set Up ARDK with the Universal Render Pipeline
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Set Up ARDK with the Universal Render Pipeline

</div>

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

- Completion of [Set up the Niantic SDK for Unity](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-the-niantic-sdk-for-unity)
- Completion of <a href="https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/manual/project-setup/universal-render-pipeline.html" target="_blank" rel="noopener noreferrer">Configure URP for AR Foundation</a>

## Setting up URP with Nsdk Occlusion<a href="#setting-up-urp-with-nsdk-occlusion" class="hash-link" aria-label="Direct link to Setting up URP with Nsdk Occlusion" title="Direct link to Setting up URP with Nsdk Occlusion">​</a>

Occlusions made using the ARFoundation `AROcclusionManager` will work out-of-the-box with just the `ARBackgroundRendererFeature` added, as in the ARFoundation instructions. However, when using the `NsdkOcclusionExtension` to enhance occlusions, you must also add a `NsdkOcclusionExtensionFeature` to your URP renderer. For more information, see [How to Set Up Real-World Occlusion](https://www.nianticspatial.com/docs/nsdk/how-to/ar/setup_real_world_occlusion/).

</div>

</div>
