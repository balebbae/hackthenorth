---
source: https://www.nianticspatial.com/docs/nsdk/sample_projects/
title: Sample Projects
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Sample Projects

</div>

|  |  |
|----|----|
| ![](https://www.nianticspatial.com/docs/assets/images/samples_menu-5308e47343377af0a5787450f2542d4d.png) | These samples are designed to demonstrate the uses of each feature in our SDK. The sample project launches multiple small samples that you can try out and look though the code to learn how to get started with any feature. Step by step how-to guides are available to teach you how to to leverage each feature. |

## Installing the Samples<a href="#installing-the-samples" class="hash-link" aria-label="Direct link to Installing the Samples" title="Direct link to Installing the Samples">​</a>

<div class="tabs-container tabList__CuJ">

- Android
- iOS
- Meta Quest 3

<div class="margin-top--md">

<div class="tabItem_Ymn6 ardkTab" role="tabpanel">

The samples are available on our GitHub: <a href="https://github.com/nianticspatial/nsdk-samples-csharp" target="_blank" rel="noopener noreferrer">https://github.com/nianticspatial/nsdk-samples-csharp</a> — after cloning, open the **`NsdkSamples`** folder in Unity Hub (Unity project root).

**How to clone/download the samples:**

`git clone https://github.com/nianticspatial/nsdk-samples-csharp.git`

or

Download the repo from <a href="https://github.com/nianticspatial/nsdk-samples-csharp" target="_blank" rel="noopener noreferrer">https://github.com/nianticspatial/nsdk-samples-csharp</a> using the **code/download** button on **github**.

Open the samples project in Unity by pressing **Add** in **Unity Hub** and browsing to the **`NsdkSamples`** folder inside the clone.

</div>

<div class="tabItem_Ymn6 ardkTab" role="tabpanel" hidden="">

The samples are available on our GitHub: <a href="https://github.com/nianticspatial/nsdk-samples-csharp" target="_blank" rel="noopener noreferrer">https://github.com/nianticspatial/nsdk-samples-csharp</a> — after cloning, open the **`NsdkSamples`** folder in Unity Hub (Unity project root).

**How to clone/download the samples:**

`git clone https://github.com/nianticspatial/nsdk-samples-csharp.git`

or

Download the repo from <a href="https://github.com/nianticspatial/nsdk-samples-csharp" target="_blank" rel="noopener noreferrer">https://github.com/nianticspatial/nsdk-samples-csharp</a> using the **code/download** button on **github**.

Open the samples project in Unity by pressing **Add** in **Unity Hub** and browsing to the **`NsdkSamples`** folder inside the clone.

</div>

<div class="tabItem_Ymn6 ardkTab" role="tabpanel" hidden="">

The **Niantic Spatial Meta Plugin** includes sample scenes designed for use with Meta Quest 3 in AR. While the UI will appear different, the functionality of these sample scenes are very similar to the sample scenes for iOS/Android mobile devices described below.

<div class="theme-admonition theme-admonition-info admonition_xJq3 alert alert--info">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)</span>Authentication

</div>

<div class="admonitionContent_BuS1">

Meta Quest samples require a Niantic Spatial access token. For most development and internal testing, use a Developer Token. For more information, see the [Authorization guide](https://www.nianticspatial.com/docs/nsdk/auth_getting_started/).

</div>

</div>

1.  Follow the steps in [Set up the Niantic SDK for Unity](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-the-niantic-sdk-for-unity).
2.  In Unity, open the **Window** top menu, then select **Package Manager**.
3.  With **Packages: Unity Registry** selected, browse to and install the **XR Interaction Toolkit** (com.unity.xr.interaction.toolkit).
4.  With **Packages: In Project** selected, select the **Niantic Spatial Meta Plugin**, and from there select the **Samples** tab.
5.  Click **Import** to import the samples into your current project.
6.  Find the sample scenes under `Assets/Samples/Niantic Spatial SDK Meta Plugin/`.
7.  In the **File** top menu, select **Build Settings**.
8.  Drag the sample scenes that you wish to test into **Scenes in Build**. Ensure that the **Home** scene is at the top of the list. <img src="https://www.nianticspatial.com/docs/assets/images/samples_quest3-49e4cc4b84e2c082c1ec34cfa3dd6611.png" style="width:50.0%" alt="Selecting scenes in the Build Settings menu" />
9.  In Unity, open the **File** top menu, then select **Build Settings** and click **Build and Run** when the Meta Quest 3 device is connected and awake to test out the samples.

</div>

</div>

</div>

## Samples<a href="#samples" class="hash-link" aria-label="Direct link to Samples" title="Direct link to Samples">​</a>

### Depth Display<a href="#depth-display" class="hash-link" aria-label="Direct link to Depth Display" title="Direct link to Depth Display">​</a>

|  |  |
|----|----|
| ![](https://www.nianticspatial.com/docs/assets/images/samples_depth-3f5ba3a4fb29492462d46d609270a3a2.gif) | The depth scene demonstrates how to get the depth buffer and display it as an overlay in the scene. Open **DepthDisplay.unity** in the **Depth** folder to try it out. |

### Occlusion<a href="#occlusion" class="hash-link" aria-label="Direct link to Occlusion" title="Direct link to Occlusion">​</a>

|  |  |
|----|----|
| ![](https://www.nianticspatial.com/docs/assets/images/samples_occlusion-3b91c874c10d0c703410bd530a0cca84.gif) | This sample demonstrates occlusion by moving a static cube in front of the camera. Because the cube does not move, you can walk around and inspect the occlusion quality directly. To open it, see **Occlusion.unity** in the **Depth** folder. This sample also demonstrates two advanced occlusion options available in NSDK, **Occlusion Suppression** and **Occlusion Stabilization**. These options reduce flicker and improve the visual quality of occlusions using input from either scene segmentation or meshing. For more information on how these capabilities work, see the How-To sections for [Occlusion Suppression](https://www.nianticspatial.com/docs/nsdk/how-to/ar/setup_real_world_occlusion/#setting-up-occlusion-suppression) and [Occlusion Stabilization](https://www.nianticspatial.com/docs/nsdk/how-to/ar/setup_real_world_occlusion/#setting-up-occlusion-stabilization). |

### Scene Segmentation<a href="#scene-segmentation" class="hash-link" aria-label="Direct link to Scene Segmentation" title="Direct link to Scene Segmentation">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td width="20%"><img src="https://www.nianticspatial.com/docs/assets/images/samples_semantics-4f5c6c8d2e70dd6ec3640c2e792fa4de.gif" /></td>
<td><p>This sample demonstrates scene segmentation by applying a shader that colors anything recognized on-screen as part of a semantic channel. To open this sample, see <strong>SemanticsDisplay.unity</strong> in the <strong>Semantics</strong> folder.</p>
<p>To use this sample:</p>
<ol>
<li>Select a semantic channel from the drop down list.</li>
<li>Look for the corresponding object(s) on your phone camera.</li>
</ol></td>
</tr>
</tbody>
</table>

### Meshing<a href="#meshing" class="hash-link" aria-label="Direct link to Meshing" title="Direct link to Meshing">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td width="20%"><img src="https://www.nianticspatial.com/docs/assets/images/samples_meshing-2deb65f8a6ce22d62c66c069dbf25328.gif" /></td>
<td><p>This sample demonstrates how to use meshing to generate a physics mesh in your scene. It shows the mesh using a Normal shader, the colors represent Up, Right and Forward.</p>
<p>To open this sample, see <strong>NormalMeshes.unity</strong> in the <strong>Meshing</strong> folder.</p></td>
</tr>
</tbody>
</table>

### Triplanar Mesh<a href="#triplanar-mesh" class="hash-link" aria-label="Direct link to Triplanar Mesh" title="Direct link to Triplanar Mesh">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td width="20%"><img src="https://www.nianticspatial.com/docs/assets/images/samples_textured_meshing-72223b58e88aed6899cef79a8f79f865.gif" /></td>
<td><p>This sample demonstrates how to texture an NSDK mesh. It works like the Meshing sample but uses an example triplanar shader that demonstrates one way to do world space UV projection. The sample tiles three textures in the scene; one for the ground, the walls, and the ceiling.</p>
<p>To open this sample, see <strong>TriplanarMesh.unity</strong> in the <strong>Meshing</strong> folder.</p></td>
</tr>
</tbody>
</table>

### VPS2 Localization<a href="#vps2-localization" class="hash-link" aria-label="Direct link to VPS2 Localization" title="Direct link to VPS2 Localization">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td width="20%"><img src="https://www.nianticspatial.com/docs/assets/images/unity_samples_vps2-eb74b570b5995af2be75a616b001385f.png" /></td>
<td><div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">
<div class="admonitionHeading_Gvgb">
<span class="admonitionIcon_Rf37"></span>Attention
</div>
<div class="admonitionContent_BuS1">
<p>This sample requires <a href="https://www.nianticspatial.com/docs/nsdk/auth_getting_started/">Auth Login</a>).</p>
</div>
</div>
<p>This sample shows a list of sites in the selected Organization and allows you to choose a VPS Asset from the Sites API as a localization target, then interfaces with your phone's position to guide you to it. To open this sample, see <strong>VPS2Localization.unity</strong> in the <strong>PersistentAR</strong> folder.</p>
<p>To use this sample:</p>
<ol>
<li>Build to your device and open the app. Make sure to allow location and camera permissions.</li>
<li>Choose an Organization where the site you're looking for is.</li>
<li>Choose the site you'll want to localize to and tap the <em>Localize</em> button.</li>
<li>Physically visit the location and point the camera at the scaned location. A red arrow will appear pointing you in the general direction.</li>
<li>Wait for the status to change to <strong>Tracking</strong> and a 3d mesh of the scan should appear on top of the real world location.</li>
</ol></td>
</tr>
</tbody>
</table>

### Recording<a href="#recording" class="hash-link" aria-label="Direct link to Recording" title="Direct link to Recording">​</a>

|  |  |
|----|----|
| ![](https://www.nianticspatial.com/docs/assets/images/samples_playback_recording-773d07705e546663075de8c965684a04.gif) | This sample allows you to scan a real-world location for playback in your editor. To open this sample, see **Recording.unity** in the **Scanning** folder. To learn how to use this sample, see [How to Create Datasets for Playback](https://www.nianticspatial.com/docs/nsdk/how-to/playback/create_playback_dataset/). |

### Sites<a href="#sites" class="hash-link" aria-label="Direct link to Sites" title="Direct link to Sites">​</a>

|  |  |
|----|----|
| ![](https://www.nianticspatial.com/docs/assets/images/sites_visualization-20b6569c0fc533a863be0492405a2639.gif) | The Sites feature provides access to organized entity data in the Niantic Spatial platform, enabling your application to discover and navigate the relationships between a user, organization, site, and spatial data asset. This feature allows you to query what spatial content is available to users and how it's structured within your organization. |

### Auth<a href="#auth-1" class="hash-link" aria-label="Direct link to Auth" title="Direct link to Auth">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td width="20%"><img src="https://www.nianticspatial.com/docs/assets/images/samples_auth_unity-278988beeb48f1f387238a1a2e41b74a.gif" /></td>
<td><p>This sample demonstrates different methods of authentication and authorization when working with NSDK.</p>
<p>There is a toggle, leading to two options:</p>
<ol>
<li>A developer login that provides full access to all features.</li>
<li>Connection to a sample Enterprise backend where the user is anonymized.</li>
</ol></td>
</tr>
</tbody>
</table>

</div>

</div>
