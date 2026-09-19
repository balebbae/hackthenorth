---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/sample_projects/
title: Sample Projects
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="theme-admonition theme-admonition-warning admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>warning

</div>

<div class="admonitionContent_BuS1">

The Geospatial Browser (GSB), previously used to search and activate VPS locations, has been retired.

Existing applications that already use GSB-based POIs will continue to function. However, it is no longer possible to create new experiences using public POIs from the GSB.

To build new VPS 2.0 experiences, you must scan your own locations using Scaniverse and upgrade to NSDK 4.0.

</div>

</div>

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

The samples are available on our github <a href="https://github.com/niantic-lightship/ardk-samples" target="_blank" rel="noopener noreferrer">https://github.com/niantic-lightship/ardk-samples</a>

How to clone/download the samples:

<div>

<div class="collapsibleContent_i85q">

`git clone https://github.com/niantic-lightship/ardk-samples.git`

or

Download the repo from <a href="https://github.com/niantic-lightship/ardk-samples" target="_blank" rel="noopener noreferrer">https://github.com/niantic-lightship/ardk-samples</a> using the **code/download** button on **github**.

</div>

</div>

Open the samples project in Unity by pressing **Add** in **Unity Hub** and browsing to the project.

You will also need to [add an API key](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/#adding-your-api-key-to-your-unity-project) to have all samples work correctly.

### Running the Samples in Unity 2022

By default, our sample projects run on Unity **6000.0.58f2**, but you can downgrade them to version **2022.3.62f2** if you would prefer to use Unity 2022.

To downgrade the samples to Unity 2022:

1.  In **Unity Hub**, under **Installs**, install **2022.3.62f2** if you do not have it already.
2.  Under **Projects**, find the ARDK sample project. Click on the **Editor Version** and change it to **2022.3.62f2**. Then click the **Open with 2022.3.62f2** button.
3.  When the **Change Editor version?** dialog comes up, click **Change Version**.
4.  When the **Opening Project in Non-Matching Editor Installation** dialog comes up, click **Continue**.
5.  Disable the custom base Gradle template:
    1.  In the Unity top menu, click **Edit**, then **Project Settings**.
    2.  In the left-hand **Project Settings** menu, select **Player**, then click the Android tab.
    3.  Scroll down to **Publishing Settings**, then un-check the box labeled **Custom Base Gradle Template**.
6.  In the **Window** top menu, open the **Package Manager**. Select **Visual Scripting** from the package list, then, if you are using version 1.9.0 or earlier, click the **Update** button.
7.  If there are any errors, the **Enter Safe Mode?** dialog will pop up. Click **Enter Safe Mode** to fix the errors.

</div>

<div class="tabItem_Ymn6 ardkTab" role="tabpanel" hidden="">

The samples are available on our github <a href="https://github.com/niantic-lightship/ardk-samples" target="_blank" rel="noopener noreferrer">https://github.com/niantic-lightship/ardk-samples</a>

How to clone/download the samples:

<div>

<div class="collapsibleContent_i85q">

`git clone https://github.com/niantic-lightship/ardk-samples.git`

or

Download the repo from <a href="https://github.com/niantic-lightship/ardk-samples" target="_blank" rel="noopener noreferrer">https://github.com/niantic-lightship/ardk-samples</a> using the **code/download** button on **github**.

</div>

</div>

Open the samples project in Unity by pressing **Add** in **Unity Hub** and browsing to the project.

You will also need to [add an API key](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/#adding-your-api-key-to-your-unity-project) to have all samples work correctly.

### Running the Samples in Unity 2022

By default, our sample projects run on Unity **6000.0.58f2**, but you can downgrade them to version **2022.3.62f2** if you would prefer to use Unity 2022.

To downgrade the samples to Unity 2022:

1.  In **Unity Hub**, under **Installs**, install **2022.3.62f2** if you do not have it already.
2.  Under **Projects**, find the ARDK sample project. Click on the **Editor Version** and change it to **2022.3.62f2**. Then click the **Open with 2022.3.62f2** button.
3.  When the **Change Editor version?** dialog comes up, click **Change Version**.
4.  When the **Opening Project in Non-Matching Editor Installation** dialog comes up, click **Continue**.
5.  Disable the custom base Gradle template:
    1.  In the Unity top menu, click **Edit**, then **Project Settings**.
    2.  In the left-hand **Project Settings** menu, select **Player**, then click the Android tab.
    3.  Scroll down to **Publishing Settings**, then un-check the box labeled **Custom Base Gradle Template**.
6.  In the **Window** top menu, open the **Package Manager**. Select **Visual Scripting** from the package list, then, if you are using version 1.9.0 or earlier, click the **Update** button.
7.  If there are any errors, the **Enter Safe Mode?** dialog will pop up. Click **Enter Safe Mode** to fix the errors.

</div>

<div class="tabItem_Ymn6 ardkTab" role="tabpanel" hidden="">

The **Lightship Meta Plugin** includes sample scenes designed for use with Meta Quest 3 in AR. While the UI will appear different, the functionality of these sample scenes are very similar to the sample scenes for iOS/Android mobile devices described below.

1.  Follow the steps to [install Lightship for Meta Quest 3](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/).
2.  In Unity, open the **Window** top menu, then select **Package Manager**.
3.  With **Packages: Unity Registry** selected, browse to and install the **XR Interaction Toolkit** (com.unity.xr.interaction.toolkit).
4.  With **Packages: In Project** selected, select the **Niantic Lightship Meta Plugin**, and from there select the **Samples** tab.
5.  Click **Import** to import the samples into your current project.
6.  Find the sample scenes under `Assets/Samples/Niantic Lightship Meta Plugin/`.
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
| ![](https://www.nianticspatial.com/docs/assets/images/samples_occlusion-3b91c874c10d0c703410bd530a0cca84.gif) | This scene demonstrates occlusion by moving a static cube in front of the camera. Because the cube does not move, you can walk around and inspect the occlusion quality directly. To open it, see **Occlusion.unity** in the **Depth** folder. This sample also demonstrates two advanced occlusion options available in Lightship, **Occlusion Suppression** and **Occlusion Stabilization**. These options reduce flicker and improve the visual quality of occlusions using input from either scene segmentation or meshing. For more information on how these capabilities work, see the How-To sections for [Occlusion Suppression](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/setup_real_world_occlusion/#setting-up-occlusion-suppression) and [Occlusion Stabilization](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/setup_real_world_occlusion/#setting-up-occlusion-stabilization). |

### Scene Segmentation<a href="#scene-segmentation" class="hash-link" aria-label="Direct link to Scene Segmentation" title="Direct link to Scene Segmentation">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td width="20%"><img src="https://www.nianticspatial.com/docs/assets/images/samples_semantics-4f5c6c8d2e70dd6ec3640c2e792fa4de.gif" /></td>
<td><p>This scene demonstrates scene segmentation by applying a shader that colors anything recognized on-screen as part of a semantic channel. To open this sample, see <strong>SemanticsDisplay.unity</strong> in the <strong>Semantics</strong> folder.</p>
<p>To use this sample:</p>
<ol>
<li>Select a semantic channel from the drop down list.</li>
<li>Look for the corresponding object(s) on your phone camera.</li>
</ol></td>
</tr>
</tbody>
</table>

### Object Detection<a href="#object-detection" class="hash-link" aria-label="Direct link to Object Detection" title="Direct link to Object Detection">​</a>

|  |  |
|----|----|
| ![](https://www.nianticspatial.com/docs/assets/images/samples_object_detection-1514c1dd33716c1163412f9172eaf259.gif) | This scene demonstrates object detection by drawing a 2d bounding box around any detections it finds. In the settings menu you can toggle showing all detected classes vs only showing a selected class from the provided drop down. To open this sample, see **ObjectDetection.unity** in the **ObjectDetection** folder. |

### Meshing<a href="#meshing" class="hash-link" aria-label="Direct link to Meshing" title="Direct link to Meshing">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td width="20%"><img src="https://www.nianticspatial.com/docs/assets/images/samples_meshing-2deb65f8a6ce22d62c66c069dbf25328.gif" /></td>
<td><p>This scene demonstrates how to use meshing to generate a physics mesh in your scene. It shows the mesh using a Normal shader, the colors represent Up, Right and Forward.</p>
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
<td><p>This scene demonstrates how to texture a Lightship mesh. It works like the Meshing sample but uses an example triplanar shader that demonstrates one way to do world space UV projection. The sample tiles three textures in the scene; one for the ground, the walls, and the ceiling.</p>
<p>To open this sample, see <strong>TriplanarMesh.unity</strong> in the <strong>Meshing</strong> folder.</p></td>
</tr>
</tbody>
</table>

### Navigation Mesh<a href="#navigation-mesh" class="hash-link" aria-label="Direct link to Navigation Mesh" title="Direct link to Navigation Mesh">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td width="20%"><img src="https://www.nianticspatial.com/docs/assets/images/samples_navigation-6fd335aaeef1722b9bf301b904b860b8.gif" /></td>
<td><p>This scene demonstrates using meshing to create a <strong>Navigation Mesh</strong>. As you move around we create and grow a navigation mesh that you can click on to tell an AI agent to move to that position. The agent can walk around corners and jump up on objects. To open the sample, see <strong>NavigationMesh.unity</strong> in the <strong>NavigationMesh</strong> folder.</p>
<p>To view this demonstration:</p>
<ol>
<li>Build the scene to your device, then point your phone at your surroundings and move around. The game pieces should show after a moment.</li>
<li>Tap on a game piece to set a destination.</li>
<li>The <strong>Player Cube</strong> will find a path along the navigation mesh to reach the selected destination.</li>
</ol></td>
</tr>
</tbody>
</table>

### Remote Authoring<a href="#remote-authoring" class="hash-link" aria-label="Direct link to Remote Authoring" title="Direct link to Remote Authoring">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td width="20%"><img src="https://www.nianticspatial.com/docs/assets/images/samples_remote_auth-1bdc7696ad68a24a536333859b91654f.gif" /></td>
<td><div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">
<div class="admonitionHeading_Gvgb">
<span class="admonitionIcon_Rf37"></span>note
</div>
<div class="admonitionContent_BuS1">
<p>This sample only works in portrait orientation.</p>
</div>
</div>
<p>This scene demonstrates target localization by targeting a VPS Anchor. To open this sample, see <strong>RemoteAuthoring.unity</strong> in the <strong>PersistentAR</strong> folder.</p>
<p>To use this sample:</p>
<ol>
<li><p>Go to the <a href="https://lightship.dev/account/geospatial-browser" target="_blank" rel="noopener noreferrer">Geospatial Browser</a>.</p></li>
<li><p>Copy the <strong>Blob</strong> for a <strong>Default Anchor</strong> of your choice.</p></li>
<li><p>In the scene <strong>Hierarchy</strong>, navigate to <strong>XR Origin</strong>. In the <strong>Inspector</strong> window, add the Blob to the list of <strong>Default Anchor Payloads To Localize</strong>.</p>
<p><img src="https://www.nianticspatial.com/docs/assets/images/payloads_to_localize-44b818f783617147059cb6a415278126.png" style="width:50.0%" alt="Default Anchor Payloads To Localize" /></p></li>
<li><p>Build the sample to your device.</p></li>
<li><p>Physically visit the location you’ve chosen in GSB and localize to it.</p></li>
<li><p>A green cube will appear at the mesh origin indicated in the Geospatial Browser by the <strong>Coordinate Axis Marker</strong>.</p></li>
</ol>
<h4 id="changing-the-blob-at-runtime" class="anchor anchorWithStickyNavbar_LWe7">Changing the Blob at Runtime<a href="#changing-the-blob-at-runtime" class="hash-link" aria-label="Direct link to Changing the Blob at Runtime" title="Direct link to Changing the Blob at Runtime">​</a></h4>
<p>You can open the <a href="https://lightship.dev/account/geospatial-browser" target="_blank" rel="noopener noreferrer">Geospatial Browser</a> on your test device, copy the <strong>Blob</strong> of a different anchor, and paste it into the <strong>Payload</strong> text box when the app is running.</p></td>
</tr>
</tbody>
</table>

### VPS Localization<a href="#vps-localization" class="hash-link" aria-label="Direct link to VPS Localization" title="Direct link to VPS Localization">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td width="20%"><img src="https://www.nianticspatial.com/docs/assets/images/samples_vps-296687368f33bcf5eea2c11e21d90563.gif" /></td>
<td><div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">
<div class="admonitionHeading_Gvgb">
<span class="admonitionIcon_Rf37"></span>Attention
</div>
<div class="admonitionContent_BuS1">
<p>This sample requires a <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/create_account/">Lightship API Key</a>).</p>
</div>
</div>
<p>This scene shows a list of VPS locations in a radius, allows you to choose a Waypoint from the Coverage API as a localization target, then interfaces with your phone's map to guide you to it. To open this sample, see <strong>VPSLocalization.unity</strong> in the <strong>PersistentAR</strong> folder.</p>
<p>To use this sample:</p>
<ol>
<li>Build to device and open the app. Make sure to allow location permissions.</li>
<li>To search from your current location, set a radius and tap <strong>Request Areas</strong>. To search from another location, fill in its latitude and longitude coordinates instead.</li>
<li>Physically visit the location and tap the <strong>Localize</strong> button.</li>
<li>Wait for the status to change to <strong>Tracking</strong> and a cube will appear at the mesh's origin.</li>
</ol></td>
</tr>
</tbody>
</table>

### Shared AR VPS<a href="#shared-ar-vps" class="hash-link" aria-label="Direct link to Shared AR VPS" title="Direct link to Shared AR VPS">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td width="20%"><img src="https://www.nianticspatial.com/docs/assets/images/samples_shared_vps-fb3d2d1fec151ab7c97c01d5d263d3c5.gif" /></td>
<td><div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">
<div class="admonitionHeading_Gvgb">
<span class="admonitionIcon_Rf37"></span>Attention
</div>
<div class="admonitionContent_BuS1">
<p>This sample requires a <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/create_account/">Lightship API Key</a>.</p>
</div>
</div>
<p>This scene allows you to choose a Waypoint from the Coverage API and create a shared AR experience around it. To open this sample, see <strong>SharedARVPS.unity</strong> in the <strong>SharedAR</strong> folder.</p>
<p>To use this sample on mobile devices:</p>
<ol>
<li>Follow instructions for <strong>VPSLocalization</strong> to localize to an available location.</li>
<li>Physically visit the location and tap the <strong>Localize</strong> button with 2-10 other phones. This process will localize everyone to the same location and automatically join everyone into the same room.</li>
<li>Wait for the status to change to <strong>Tracking</strong> and every player in the session will see a name tag. The name tag will turn red to indicate that player has lost tracking. The stats UI can be hidden by tapping on it, but it will not return for that session.</li>
</ol>
<p>To use this sample with Playback in the Unity editor:</p>
<ol>
<li>Set up playback of the scene at a location. See <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/playback/setting_up_playback/">How to Set Up Playback</a>.</li>
<li>Provide a default anchor payload string from the Geospatial Browser to use with playback. See <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/tooling/use_geospatial_browser/">How to Use the Geospatial Browser</a>.</li>
<li>Copy the default anchor payload string into the <strong>In Editor Payload</strong> field in the <strong>Vps Colocalization Demo</strong> component.</li>
<li>Start the VPS Colocalization scene. It should use the payload string to automatically start tracking.</li>
<li>When the network UI comes up, choose whether to join as Host or Client.</li>
</ol></td>
</tr>
</tbody>
</table>

### Shared AR Image Tracking Colocalization<a href="#shared-ar-image-tracking-colocalization" class="hash-link" aria-label="Direct link to Shared AR Image Tracking Colocalization" title="Direct link to Shared AR Image Tracking Colocalization">​</a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td width="20%"><img src="https://www.nianticspatial.com/docs/assets/images/samples_shared_image_target-8cca2ba5de67d3c19de13d084a35ce73.gif" /></td>
<td><div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">
<div class="admonitionHeading_Gvgb">
<span class="admonitionIcon_Rf37"></span>Attention
</div>
<div class="admonitionContent_BuS1">
<p>This sample requires a <a href="https://www.nianticspatial.com/docs/nsdk/3.17.0/create_account/">Lightship API Key</a>.</p>
</div>
</div>
<p>This scene allows multiple users to join a shared room without a VPS location, using a static image as the origin point. To open this sample, see <strong>ImageTrackingColocalization.unity</strong> in the <strong>SharedAR</strong> folder.</p>
<p>To use this sample:</p>
<ol>
<li>Print the image in <code>Assets/Samples/SharedAR/IMG-2689.png</code> so that it is 9cm wide.</li>
<li>Place the image on a surface.</li>
<li>Point the device camera at the image. Select <strong>Create New Room</strong>.</li>
</ol></td>
</tr>
</tbody>
</table>

### World Pose<a href="#world-pose" class="hash-link" aria-label="Direct link to World Pose" title="Direct link to World Pose">​</a>

|  |  |
|----|----|
| ![](https://www.nianticspatial.com/docs/assets/images/samples_world_pose-854c15c767e3fc59132744e332624e36.gif) | This sample demonstrates how the World Positioning System improves the camera's accuracy by showing a comparison between the device's GPS compass and the World Pose compass. As you walk around, the World Pose compass should stabilize and become more accurate over time. |

### On Device Persistence<a href="#on-device-persistence" class="hash-link" aria-label="Direct link to On Device Persistence" title="Direct link to On Device Persistence">​</a>

|  |  |
|----|----|
| ![](https://www.nianticspatial.com/docs/assets/images/local_persistence-361adbe1992ddbae62cd955c22ceff22.png) | This sample demonstrates how to create a VPS map locally. This is created and stored on the device and can be used to align and persist content. The sample stores the map and positions of cubes to the device's file system. |

### Cloud Persistence<a href="#cloud-persistence" class="hash-link" aria-label="Direct link to Cloud Persistence" title="Direct link to Cloud Persistence">​</a>

|  |  |
|----|----|
| ![](https://www.nianticspatial.com/docs/assets/images/cloud_persistence-81cb89f53b848d536bccea974c891b2d.png) | This sample is a variation of the On-Device Persistence sample, designed to save map data to the cloud using our datastore. This allows other users to download the map and align to the same space, enabling seamless ad-hoc multiplayer experiences. Multiple players can place cubes, which are automatically synchronized across all participants in the room and persist in their locations. |

### Recording<a href="#recording" class="hash-link" aria-label="Direct link to Recording" title="Direct link to Recording">​</a>

|  |  |
|----|----|
| ![](https://www.nianticspatial.com/docs/assets/images/samples_playback_recording-773d07705e546663075de8c965684a04.gif) | This scene allows you to scan a real-world location for playback in your editor. To open this sample, see **Recording.unity** in the **Scanning** folder. To learn how to use this sample, see [How to Create Datasets for Playback](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/playback/create_playback_dataset/). |

</div>

</div>
