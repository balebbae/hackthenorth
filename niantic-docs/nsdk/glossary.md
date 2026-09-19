---
source: https://www.nianticspatial.com/docs/nsdk/glossary/
title: Glossary
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Glossary

</div>

**AR Scene** - A Unity Scene that has an **ARSession** and **XROrigin** setup to enable AR. See [Set up a basic AR scene](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-a-basic-ar-scene).

**Augmented Reality (AR)** - Augmented Reality is the result of using real-world locations and adding digital objects and experiences to those places.

**Component** - A Unity <a href="https://docs.unity3d.com/Manual/Components.html" target="_blank" rel="noopener noreferrer">Component</a>.

**Dataset** - A recording of your AR application in a real-world location for playback and testing in the Unity editor. See [How to Create Datasets for Playback](https://www.nianticspatial.com/docs/nsdk/how-to/playback/create_playback_dataset/).

**Depth** - An estimation of how far objects are from the camera. This is used to place AR objects convincingly. See [Depth](https://www.nianticspatial.com/docs/nsdk/features/depth/).

**Depth Occlusion** - Using depth to estimate whether an AR object would be visually blocked by a real-world object. See the Depth Occlusion [sample](https://www.nianticspatial.com/docs/nsdk/sample_projects/#occlusion).

**Localization** - The process of placing a user into an AR experience. See [Creating Location AR Experiences with VPS](https://www.nianticspatial.com/docs/nsdk/features/lightship_vps/).

**Location AR** - Using a real-world location to act as the center of an AR experience. See [Creating Location AR Experiences with VPS](https://www.nianticspatial.com/docs/nsdk/features/lightship_vps/).

**Meshing** - Meshing uses depth and tracking data to generate a mesh representing the estimated geometry of the scanned real world. See [Meshing](https://www.nianticspatial.com/docs/nsdk/features/meshing/).

**Neural Network Model** - Neural Network Models are trained to allow features such as [Depth](#Depth) or [Semantic Segmentation](#Semantic_Segmentation) to know how to draw each pixel in an AR environment. See [Neural Network Model Preloading](https://www.nianticspatial.com/docs/nsdk/features/model_preloading/).

**Occlusion** - Occlusion gives depth to virtual objects, allowing them to appear behind or in front of objects in the real world. See [Occlusion](https://www.nianticspatial.com/docs/nsdk/features/occlusion/).

**ParrelSync** - <a href="https://github.com/VeriorPies/ParrelSync" target="_blank" rel="noopener noreferrer">ParrelSync</a> is a Unity editor extension that allows users to test multiplayer gameplay without building the project by having another Unity editor window opened and mirror the changes from the original project.

**Playback** - A feature that allows you to import pre-recorded video of specific locations (such as a [Dataset](#Dataset)) and run it in the Unity editor. See [Playback](https://www.nianticspatial.com/docs/nsdk/features/playback/).

**Playback Data** - A [Dataset](#Dataset) you created for playback in the Unity editor. See [How to Create Datasets for Playback](https://www.nianticspatial.com/docs/nsdk/how-to/playback/create_playback_dataset/).

**Private VPS Locations** - A [VPS](https://www.nianticspatial.com/docs/nsdk/features/lightship_vps/) location in your surrounding area used to test in the <a href="https://scaniverse.com/" target="_blank" rel="noopener noreferrer">Niantic Scaniverse App</a>.

**Project Validation** - Niantic Spatial offers an upgraded version of the Unity Project Validation System, allowing developers to check their projects for common errors, such as configuration issues in Scenes and Projects. See [Project Validation](https://www.nianticspatial.com/docs/nsdk/features/project_validation/).

**Real-World Occlusion** - [Depth Occlusion](#Depth_Occlusion) as applied to real-world objects. See [Occlusion](https://www.nianticspatial.com/docs/nsdk/features/occlusion/).

**Real-World Objects** - Objects in the real world identified by [Semantic Segmentation](#Semantic_Segmentation). See [How to Query Scene Segmentation to Find Real-World Objects](https://www.nianticspatial.com/docs/nsdk/how-to/ar/query_semantics_real_objects/).

**Real-World Position** - The position in the real world that matches a [screen point](#Screen_Point) on a scene captured by a camera. See [How to Convert a Screen Point to Real-World Position Using Depth](https://www.nianticspatial.com/docs/nsdk/how-to/ar/depth/convert_point_world_position/).

**Raycast Visualization** - A feature that provides real-time visual feedback during scanning by overlaying diagonal stripes on the camera feed. Areas that have been successfully scanned appear in full color, while unscanned areas display the stripe pattern. See [How to Enable Scan Visualization in AR](https://www.nianticspatial.com/docs/nsdk/how-to/ar/scan_visualization/).

**Simulation** - The ability to move the camera in a virtual environment to test AR features. See [How to Set Up and Run Niantic Spatial Simulation](https://www.nianticspatial.com/docs/nsdk/how-to/unity/simulation_mocking/) for details.

**Screen Point** - A 2D position in a camera image. See [How to Convert a Screen Point to Real-World Position Using Depth](https://www.nianticspatial.com/docs/nsdk/how-to/ar/depth/convert_point_world_position/).

**Scene Segmentation** - See [Semantic Segmentation](#Semantic_Segmentation).

**Semantic Depth Suppression** - Enables a user to holdout depth values for specific semantic channels to the far depth plane. See [Niantic Spatial Occlusion Extension](https://www.nianticspatial.com/docs/nsdk/features/occlusion/#lightship-occlusion-extension).

**Semantic Segmentation** - The process of assigning class labels to specific regions in an image. See [Scene Segmentation](https://www.nianticspatial.com/docs/nsdk/features/semantics/).

**Test Scans** - A [Private VPS Location](#Private_VPS_Locations) used for testing.

**Visual Positioning System (VPS)** - Niantic Spatial VPS lets you synchronize your device with real-world locations by locating and understanding real-world [VPS-Activated Locations](#VPS_Activated_Location). See [Creating Location AR Experiences with VPS](https://www.nianticspatial.com/docs/nsdk/features/lightship_vps/) for more information.

**VPS-Activated Location** - A unique or notable, publicly accessible, real-world location that Niantic Spatial VPS apps can engage with. See [Creating Location AR Experiences with VPS](https://www.nianticspatial.com/docs/nsdk/features/lightship_vps/).

**VPS Coverage Areas** - Geographic regions where users can localize with VPS and interact with persistent AR content. See [Creating Location AR Experiences with VPS](https://www.nianticspatial.com/docs/nsdk/features/lightship_vps/).

**World Pose System (WPS)** - Provides a stable geographic position and orientation for the device and support for conversions between geographic and AR tracking coordinates. See [Building an App Using WPS](https://www.nianticspatial.com/docs/nsdk/how-to/ar/world_pose/).

</div>

</div>
