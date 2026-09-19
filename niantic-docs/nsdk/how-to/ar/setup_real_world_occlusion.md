---
source: https://www.nianticspatial.com/docs/nsdk/how-to/ar/setup_real_world_occlusion/
title: How to Set Up Real-World Occlusion
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Set Up Real-World Occlusion

</div>

Niantic Spatial Occlusion creates depth in AR applications, rendering game objects in front of or behind objects in the real world. Niantic Spatial SDK for Unity (NSDK) integrates seamlessly with the AR Foundation Occlusion Manager, enabling occlusion options not available in ARKit and ARCore.

<img src="https://www.nianticspatial.com/docs/assets/images/plush_occlusion-89cc7051d417c90467d5d830d544d043.png" width="300" alt="Occlusion in action" />

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Unity project with NSDK installed and a set-up basic AR scene. For more information, see [Set up the Niantic SDK for Unity](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-the-niantic-sdk-for-unity) and [Set up a basic AR scene](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-a-basic-ar-scene).

## Setting Up Occlusion<a href="#setting-up-occlusion" class="hash-link" aria-label="Direct link to Setting Up Occlusion" title="Direct link to Setting Up Occlusion">​</a>

To set up Niantic Spatial occlusion:

1.  Add an `AROcclusionManager` to your **Main Camera** `GameObject`:
    1.  In the **Hierarchy**, expand the `XROrigin` and **Camera Offset**, then select the **Main Camera** object. Then, in the **Inspector**, click **Add Component** and add an `AROcclusionManager`.
2.  Add a cube as a child of your Camera, then set its position, rotation, and scale:
    1.  In the **Hierarchy**, right-click the **Main Camera**, then mouse over **3D Object** and select **Cube**.
    2.  In the **Inspector**, under the **Transform** heading, set the cube's position to (0, 0, 2), its rotation to (0, 45, 45), and its scale to (0.2, 0.2, 0.2).
3.  When you build to device or use playback, your cube will be occluded by physical objects that are less than 2 meters away from your phone.

<img src="https://www.nianticspatial.com/docs/assets/images/snorlax_occlusion-9427356a34a70145dd2621b3fdfd3c9a.png" width="236" alt="More occlusion in action" />

## Improving Occlusion Quality with the NSDK Occlusion Extension<a href="#improving-occlusion-quality-with-the-nsdk-occlusion-extension" class="hash-link" aria-label="Direct link to Improving Occlusion Quality with the NSDK Occlusion Extension" title="Direct link to Improving Occlusion Quality with the NSDK Occlusion Extension">​</a>

By adding the NSDK Occlusion Extension, you can improve the visual quality of occlusions by adding functionality to the standard `AROcclusionManager`.

To add the extension and test one of its features:

1.  Add a `NsdkOcclusionExtension` to the Main Camera `GameObject`.

    1.  In the **Hierarchy**, expand the `XROrigin` and select the **Main Camera**. Then, in the **Inspector**, click **Add Component** and add a `Nsdk Occlusion Extension`.

2.  If you are using the Universal Render Pipeline, add a `Nsdk Occlusion Extension Feature` to the URP renderer:

    1.  In the **Project** window, find the URP renderer you are using under the **Assets** directory.
    2.  In the **Inspector**, click the **Add Renderer Feature** button, then select `Nsdk Occlusion Extension Feature`. Make sure it comes after the `AR Background Renderer Feature`.
    3.  Enable Unity's **Compatibility Mode (RenderGraph disabled)** under Edit → Project Settings → Graphics → URP

3.  In the extension options menu, set the **Optimal Occlusion Distance Mode** to **Specified Game Object**.

4.  Set the **Cube** you created earlier as the **Principal Occludee**.

5.  When you build to device or run in playback, the edges of objects in the image should now line up more precisely with the occlusion boundaries of the cube.

    <img src="https://www.nianticspatial.com/docs/assets/images/extension_0-34bea46afc7ec615c237cd8b1ccc8b33.png" width="500" alt="NSDK Occlusion Extension" />

For more information on the NSDK Occlusion Extension and its features, see [Adding Occlusion to Your Project](https://www.nianticspatial.com/docs/nsdk/how-to/ar/adding_occlusion/#nsdk-occlusion-extension).

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

URP users using the `NSDK Occlusion Extension Feature` will need to enable **Compatibility Mode (RenderGraph disabled)** (Edit \> Project Settings \> Graphics \> URP). Otherwise, the extension will have no effect.

</div>

</div>

## Setting up Occlusion Suppression<a href="#setting-up-occlusion-suppression" class="hash-link" aria-label="Direct link to Setting up Occlusion Suppression" title="Direct link to Setting up Occlusion Suppression">​</a>

**Occlusion Suppression** prevents pixels containing specified semantic information from occluding AR assets. Depth-based occlusion can be noisy and lead to inconsistencies with particular semantic channels. Enabling Occlusion Suppression can improve the visual quality of occlusions, particularly when AR characters appear to clip into the floor or disappear into the sky.

1.  Follow the steps in [**Improving Occlusion Quality with the NSDK Occlusion Extension**](#improving-occlusion-quality-with-the-nsdk-occlusion-extension).

2.  Add an `ARSemanticSegmentationManager` to the **Main Camera** `GameObject`.

    1.  In the **Hierarchy**, expand the 'XROrigin' and select the **Main Camera**. Then, in the **Inspector**, click **Add Component** and add an `AR Semantic Segmentation Manager` to it.

3.  In the **Inspector**, open the **Nsdk Occlusion Extension** options menu, then check the box labeled **Enable Occlusion Suppression**. This will make new options appear.

4.  Drag the **Main Camera** `GameObject` from the **Hierarchy** to the **Semantic Segmentation Manager** field in the **Inspector**.

5.  In the **Suppression Channels** list, add `sky` for Element 0 and `ground` for Element 1.

6.  Done! When you test your application, pixels corresponding to the ground or sky should not occlude your virtual objects. Try using other semantic channels from the [Scene Segmentation](https://www.nianticspatial.com/docs/nsdk/features/semantics/) page and see what happens!

    <img src="https://www.nianticspatial.com/docs/assets/images/extension_1-aadd8e66e4fd09905a5db722d2caf93c.png" width="500" alt="NSDK Occlusion Extension with AR Semantic Segmentation Manager" />

## Setting up Occlusion Stabilization<a href="#setting-up-occlusion-stabilization" class="hash-link" aria-label="Direct link to Setting up Occlusion Stabilization" title="Direct link to Setting up Occlusion Stabilization">​</a>

**Occlusion Stabilization** combines information from the instantaneous depth buffer and a depth field rendered from the world mesh to stabilize occlusions between frames. This leads to higher-quality, more consistent occlusions in static parts of the scene.

1.  Follow the steps in [**Improving Occlusion Quality with the NSDK Occlusion Extension**](#improving-occlusion-quality-with-the-nsdk-occlusion-extension).

2.  Set up Meshing in your scene:

    1.  In the **Hierarchy**, select the `XROrigin` and add an empty `GameObject` to it. Name it **Meshing**.

    2.  Select **Meshing**, then, in the **Inspector**, click **Add Component** and add an **ARMeshManager** Component to it.

    3.  In the **ARMeshManager** Component, set the **MeshPrefab** to **FusedMesh** (located in `Packages/Niantic Spatial Development Kit AR Plugin/Assets/Prefabs`).

        1.  This prefab has a layer set to "Mesh". In your next project, if you add a different prefab here, make sure it is on a new layer. To create a new layer, in the **Inspector**, select the **Layer** drop-down, then create a layer and give it a unique name. (The name can be anything as long as it is not already in use.)
        2.  \[URP Only\] If you are using the universal render pipeline, you will need to add the prefab directly to your Unity project before assigning it to **ARMeshManager**. In the **Project** window, scroll down to **Packages**, then open **NSDK AR Plugin**. In the **Assets** subfolder, select **Prefabs**, then drag and drop the **FusedMesh** prefab to your project's **Assets** folder. Once you have done so, set the **MeshPrefab** to **FusedMesh**.

    4.  \[Optional\] To configure advanced settings for meshing, add a **NsdkMeshingExtension** Component to the **Meshing** `GameObject`.

    5.  Change the Shader for the **FusedMesh** Material to `Nsdk/FusedDepthChunkURP`.

        <img src="https://www.nianticspatial.com/docs/assets/images/armeshmanager-3cf1b35dfa5ca826ef1b4670a98c5163.png" width="500" alt="The Meshing object with AR Mesh Manager" />

3.  Enable Occlusion Stabilization:

    1.  In the **Inspector**, open the **Nsdk Occlusion Extension** options menu, then check the box labeled **Enable Occlusion Stabilization**. This will make new options appear.

    2.  Drag the **Meshing** `GameObject` from the **Hierarchy** to the **Meshing Manager** field in the **Inspector**.

        <img src="https://www.nianticspatial.com/docs/assets/images/extension_2-3201857ec8f36e7336d43d7c0d438eaf.png" width="500" alt="Nsdk Occlusion Extension" />

## More Information<a href="#more-information" class="hash-link" aria-label="Direct link to More Information" title="Direct link to More Information">​</a>

For more information, see the [Occlusion Feature page](https://www.nianticspatial.com/docs/nsdk/features/occlusion/) and [Adding Occlusion to Your Project](https://www.nianticspatial.com/docs/nsdk/how-to/ar/adding_occlusion/).

</div>

</div>
