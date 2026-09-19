---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/meshing/meshing_physics_real_world/
title: How to Add Physics to a Meshed Scene
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Add Physics to a Meshed Scene

</div>

This how-to covers:

- Adding dynamic meshing to a scene with the default manager;
- How to create a prefab for meshing;
- Interacting with mesh physics;
- Making the mesh invisible.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/frat_pyramid_ball_launch-fa1c059e07e73520077431cebbb2cff7.gif" width="300" alt="Launching Spheres in the Real World" /><img src="https://www.nianticspatial.com/docs/assets/images/falling_objects_mesh-5f2585acbdb11eb9713a53bb4d7a9b9b.gif" style="width:300px;height:645px;object-fit:cover" alt="Falling Objects on the Gandhi Statue" />

</div>

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Unity project with ARDK installed and a set-up basic AR scene. For more information, see [Setting Up the Niantic SDK for Unity](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/) and [Setting up a Basic AR Scene](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/#setting-up-a-basic-ar-scene).

## Creating the Mesh<a href="#creating-the-mesh" class="hash-link" aria-label="Direct link to Creating the Mesh" title="Direct link to Creating the Mesh">​</a>

To create a mesh prefab:

1.  Add an AR Mesh Manager to the XROrigin:

    1.  In the **Hierarchy**, right-click on the `XROrigin`, then select **Create Empty** to add an empty `GameObject` to it. Name the new object **MeshManager**.

    2.  In the **Hierarchy**, select **MeshManager**, then, in the **Inspector** window, click **Add Component** and add an **ARMeshManager** Component to it.

    <div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

    <div class="admonitionHeading_Gvgb">

    <span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>caution

    </div>

    <div class="admonitionContent_BuS1">

    Be cautious when adding the `ARMeshManager` Component to GameObjects that parent a camera. The `ARMeshManager` will automatically increase the scale of the GameObject it's attached to. This can misalign the scale of the real and virtual worlds, breaking occlusions and the perceived distances of objects.

    </div>

    </div>

    1.  Repeat this process, but add a **Lightship Meshing Extension** Component instead.

        <img src="https://www.nianticspatial.com/docs/assets/images/meshmanager_components-55751cfe6012f1d8987ea12deef5dd37.png" width="400" alt="The Unity UI showing the added components" />

2.  Add an AR Occlusion Manager:

    1.  In the **Hierarchy**, expand the `XROrigin` and **Camera Offset**, then select the **Main Camera** object. Then, in the **Inspector**, click **Add Component** and add an `AROcclusionManager`.

    2.  Set the **Occlusion Preference Mode** to **No Occlusion**.

        <img src="https://www.nianticspatial.com/docs/assets/images/no_occlusion-f2183cdfc1a1681c9e2f6b8dd1c53d07.png" width="400" alt="The AR Occlusion Manager with No Occlusion set" />

3.  Prepare the mesh for conversion to prefab:

    1.  In the **Hierarchy**, right click and create an Empty `GameObject` in the main scene. Name it **MeshChunk**.

    2.  In the **Inspector** window, add three Components to **MeshChunk**; a **Mesh Filter** to hold geographic information, a **Mesh Renderer** to display the mesh (if desired), and a **Mesh Collider** to provide physics.

    3.  In the **Mesh Renderer** Component, expand the **Materials** drop-down, then click the circle button to open the **Select Material** window and pick a **Default Material** to add to it.

        <img src="https://www.nianticspatial.com/docs/assets/images/mesh_chunk-eb3df6ce8c355a7d2ac373d57c6f48e4.png" width="800" alt="Create a MeshChunk game object like so" />

    <div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

    <div class="admonitionHeading_Gvgb">

    <span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

    </div>

    <div class="admonitionContent_BuS1">

    **Unity 6** users will need to to upgrade the **Default Material** used in the **MeshChunk** to work with the **Universal Render Pipeline (URP)**.

    This can be done by double-clicking on the **Default Material** after it’s added to the **MeshChunk**’s **Mesh Renderer**, then on the top menu go to **Edit** → **Rendering** → **Materials** and convert the **Material** to **URP**.

    </div>

    </div>

4.  Convert the mesh into a prefab and assign it:

    1.  Drag **MeshChunk** from the **Hierarchy** to the **Assets** window, converting it into a prefab.

    2.  Delete the **MeshChunk** `GameObject` from the scene.

    3.  Select **MeshManager** from the **Hierarchy**, then drag the **MeshChunk** prefab to the **Mesh Prefab** slot in the **Inspector**.

        <img src="https://www.nianticspatial.com/docs/assets/images/mesh_prefab-af5bc424a0e21abbd7c8ea6a8d8d269c.png" width="800" alt="Create a MeshChunk prefab and add it to the ARMeshManager" />

5.  Test it out:

    1.  Build to device or press play in the editor. A mesh overlay should appear on screen.

    <img src="https://www.nianticspatial.com/docs/assets/images/editor_playback_meshing-f71612b9c41f17d5f6bb16e68cfa53d1.png" width="800" alt="Mesh overlay with playback" />

## Testing Mesh Physics<a href="#testing-mesh-physics" class="hash-link" aria-label="Direct link to Testing Mesh Physics" title="Direct link to Testing Mesh Physics">​</a>

Because the mesh has a **Mesh Collider**, the mesh will respond to any object using standard Unity physics collision. For example, the mesh can provide collision for creatures walking on meshed surfaces or inform game entities when they have bumped into walls. This exercise demonstrates this by allowing the player to shoot spheres into the scene and see them bounce off of the mesh.

To add physics to the mesh:

1.  Create a physics prefab and add rigid body collision to it:
    1.  In the **Hierarchy**, right click, then mouse over **3D Object** and select **Sphere**. Name it **LauncherSphere**.
    2.  Select **LauncherSphere** in the **Hierarchy**, then add a **RigidBody** Component to it in the **Inspector**.
    3.  Still in the **Inspector**, make **LauncherSphere** smaller by setting its scale in the **Transform** Component to (0.2, 0.2, 0.2).
    4.  Drag **LauncherSphere** to the **Assets** window to make it into a prefab, then delete it from the scene.
2.  Create a script to launch spheres:
    1.  In the **Assets** window, right-click, then mouse over **Create** and choose **C# Script**. Name the new script **Launcher**.
    2.  Add the **Launcher** code to your script:

Click to expand the Launcher code

<div>

<div class="collapsibleContent_i85q">

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp

using UnityEngine;

public class Launcher : MonoBehaviour
{
    public Rigidbody _prefabWithRigidbody;
    void Update()
    {
#if UNITY_EDITOR
        if(Input.GetMouseButtonDown(0))
#else
        if (Input.touchCount > 0)
#endif
        {
            // spawn in front of at the camera
            var pos = Camera.main.transform.position;
            var forw = Camera.main.transform.forward;
            var thing = Instantiate(_prefabWithRigidbody, pos+(forw*0.4f), Quaternion.identity);

            thing.AddForce(forw * 200.0f);
        }
    }
}
```

</div>

</div>

</div>

</div>

3.  Make a `GameObject` to run the script:
    1.  In the **Hierarchy**, right-click in your Scene, then choose **Create Empty**. Name it **LauncherScript**, then drag and drop the **Launcher** script onto it from the **Assets** directory.
    2.  Select **LauncherScript** from the **Hierarchy**, then, in the **Inspector**, assign **LauncherSphere** as the **Prefab** variable.
4.  Build to device and test! You should be able to tap anywhere on screen and shoot a sphere that bounces off of surfaces.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/frat_pyramid_ball_launch-fa1c059e07e73520077431cebbb2cff7.gif" width="300" alt="Launching Spheres in the Real World" />

</div>

## Making the Mesh Invisible<a href="#making-the-mesh-invisible" class="hash-link" aria-label="Direct link to Making the Mesh Invisible" title="Direct link to Making the Mesh Invisible">​</a>

The simplest way to make the mesh invisible is to tell Unity not to render it. Delete the **Mesh Renderer** from the prefab and Unity will no longer be able to draw it, but this also means the mesh cannot provide occlusion and shadows in the scene.

<div class="tabs-container tabList__CuJ">

- Built-in Render Pipeline
- Universal Render Pipeline

<div class="margin-top--md">

<div class="tabItem_Ymn6 ardkTab" role="tabpanel">

To keep this functionality, Lightship provides a shader called `InvisibleMeshWithShadows` that will receive light and draw shadows without rendering the mesh directly.

To add an invisibility shader to the mesh:

1.  If you don't have a copy of the `InvisibleMeshWithShadows` shader in your project, download it from our GitHub repository <a href="https://github.com/niantic-lightship/ardk-samples/blob/main/Assets/Samples/NavigationMesh/Shaders/InvisibleMeshWithShadows.shader" target="_blank" rel="noopener noreferrer">here</a> and add it to your project.
2.  Right-click in the **Assets** window, then mouse over **Create** and select **Material**. Name it **InvisibleShader**.
3.  Add the `InvisibleMeshWithShadows` shader to **InvisibleShader**:
    1.  In the **Assets** window, select the Material.
    2.  In the **Inspector** window, click the **Shader** dropdown, search for `InvisibleMeshWithShadows`, and select it.
4.  Add **InvisibleShader** to the **Mesh Renderer** in the prefab:
    1.  Select your **MeshChunk** object in the **Hierarchy**.
    2.  In the **Inspector** window, find the **Mesh Renderer** component and click the **Materials** menu to expand it.
    3.  Add **InvisibleShader** as the Material by clicking the circle and searching for **InvisibleShader** or dragging and dropping **Invisible Shader** to the element box.

</div>

<div class="tabItem_Ymn6 ardkTab" role="tabpanel" hidden="">

To keep this functionality, Lightship provides two Shader Graph assets available for download from our GitHub repository <a href="https://github.com/niantic-lightship/ardk-samples/blob/main/Assets/Samples/Common/Shaders/URPGraphShaders" target="_blank" rel="noopener noreferrer">here</a>.

1.  Import <a href="https://github.com/niantic-lightship/ardk-samples/blob/main/Assets/Samples/Common/Shaders/URPGraphShaders/MainLight.shadersubgraph" target="_blank" rel="noopener noreferrer"><code>MainLight.shadersubgraph</code></a>
2.  Import <a href="https://github.com/niantic-lightship/ardk-samples/blob/main/Assets/Samples/Common/Shaders/URPGraphShaders/TransparentWithShadow.shadergraph" target="_blank" rel="noopener noreferrer"><code>TransparentWithShadow.shadergraph</code></a>

</div>

</div>

</div>

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

Here, we've aligned the `Directional Light` in the scene to match the real world. Look into <a href="https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/api/UnityEngine.XR.ARFoundation.ARLightEstimationData.html" target="_blank" rel="noopener noreferrer"><code>ARLightEstimation</code></a> from AR Foundation to set up realistic lighting in your project.

</div>

</div>

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/mesh_with_shadows-cb87f76c68fc1d93787c7e847aaa886d.gif" width="250" alt="Invisible mesh with moving shadows" />

</div>

## Custom Mesh Texturing<a href="#custom-mesh-texturing" class="hash-link" aria-label="Direct link to Custom Mesh Texturing" title="Direct link to Custom Mesh Texturing">​</a>

While this how-to will not cover them, there are other ways to leverage mesh textures for AR development. Two examples follow:

- A custom mesh renderer (as used in the <a href="https://github.com/niantic-lightship/ardk-samples/tree/main/Assets/Samples/Meshing" target="_blank" rel="noopener noreferrer">Meshing sample scenes</a>) could display normals to see triangle facing directions while debugging.
- By default, the mesh renderer does not create a UV surface map, but using tri-planar projection when generating the mesh can create a UV map of the world space. The example shader can for mesh texturing can be found <a href="https://github.com/niantic-lightship/ardk-samples/tree/3.4.0/Assets/Samples/Meshing/Shaders" target="_blank" rel="noopener noreferrer">here</a>

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/blue_meshing_how_to-8e99418b4b101269a934bae1975fa2a4.gif" width="300" alt="Blue Mesh over the Gandhi Statue" /><img src="https://www.nianticspatial.com/docs/assets/images/textured_mesh-dd22c3e052b35f061bd5ce12627a33fb.gif" style="width:300px;height:645px;object-fit:cover" alt="Custom shader to texture meshes at different normals" />

</div>

## More Information<a href="#more-information" class="hash-link" aria-label="Direct link to More Information" title="Direct link to More Information">​</a>

- For more details on how this works, see [Meshing](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/meshing/).

</div>

</div>
