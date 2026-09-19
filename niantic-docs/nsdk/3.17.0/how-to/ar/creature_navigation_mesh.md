---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/creature_navigation_mesh/
title: How To Add Navigation Mesh
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How To Add Navigation Mesh

</div>

Navigation Mesh allows characters (known as **Agents**) to navigate the AR scene using point-and-click touch inputs.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/navmesh_with_doty-9addad2e0b3ffb1606150926adfd8719.gif" width="400" alt="Lightship NavMesh with Doty" />

</div>

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Unity project with Niantic Spatial SDK installed and Niantic Spatial Meshing enabled. For more information, see [Setting Up the Niantic Spatial SDK for Unity](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/) and [How to Add Physics to a Meshed Scene](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/meshing/meshing_physics_real_world/).

You will also need a Unity `GameObject` with the **AR Mesh Manager** and **Lightship Meshing Extension** Components. For more information, follow the Section 1 steps under [Creating the Mesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/meshing/meshing_physics_real_world/#creating-the-mesh).

Before starting this tutorial, verify that your scene is generating a mesh like this image. Then you can change the <a href="https://github.com/niantic-lightship/ardk-samples/blob/main/Assets/Samples/NavigationMesh/Shaders/InvisibleMeshWithShadows.shader" target="_blank" rel="noopener noreferrer">shader</a> on your prefab to make the mesh invisible and start following this guide to add navigation.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/blue_meshing_how_to-8e99418b4b101269a934bae1975fa2a4.gif" width="400" alt="Lightship Mesh Visual" />

</div>

## Adding the Navigation Mesh Manager<a href="#adding-the-navigation-mesh-manager" class="hash-link" aria-label="Direct link to Adding the Navigation Mesh Manager" title="Direct link to Adding the Navigation Mesh Manager">​</a>

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Important!

</div>

<div class="admonitionContent_BuS1">

This guide assumes that the `Everything` Layer Mask is selected. Should you want to change the Layer Mask, be sure to set the Layer for your [agent's prefab](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/creature_navigation_mesh/#adding-an-agent-to-the-lightshipnavmesh) to what is set in `LightshipNavMeshManager`! For more information on creating layers, please visit the Unity documentation <a href="https://docs.unity3d.com/6000.2/Documentation/Manual/create-layers.html" target="_blank" rel="noopener noreferrer">here</a> to learn more.

</div>

</div>

To add a `LightshipNavMeshManager`:

1.  Create an empty `GameObject`.
    1.  In the **Hierarchy**, select the root of the scene.
    2.  From the main menu, select **GameObject**, then **Create Empty**.
    3.  Name it **NavMeshManager**.
2.  Add a `LightshipNavMeshManager` component to the **NavMeshManager** object.
    1.  In the **Inspector** window, click **Add Component**.
    2.  Type "LightshipNavMeshManager" in the search window, then select it.
    3.  Add the **Main Camera** to the Component. This is the center of where the manager scans for valid paths on the mesh.
3.  If you want to see the LightshipNavMesh, add a `LightshipNavMeshRenderer` component to **NavMeshManager** as well. This will render the **LightshipNavMesh** on-screen when the camera moves.
    1.  In the **Inspector** window, click **Add Component** again.
    2.  This time, search for "LightshipNavMeshRenderer" instead, then select it.
    3.  Add the `LightshipNavMeshManager` to the Component.
    4.  Create a material to be used for rendering the Navigation Mesh, and add it to the Component.

<img src="https://www.nianticspatial.com/docs/assets/images/navmesh_renderer_component-2c53b136da2affa22d03d9dc31b59349.png" width="600" alt="Lightship NavMesh Manager" />

You can also add the `LightshipNavMeshManager` prefab from the NavMesh sample project. For more information, see [Sample Projects](https://www.nianticspatial.com/docs/nsdk/3.17.0/sample_projects/).

Now, if you press play in the editor, you should be able to see a grid of tiles being generated. Next, you will add an Agent that can move around on the Navigation Mesh.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/navmesh_renderer-8168ab524d2849a76d53de926891bd0f.gif" width="400" alt="Lightship NavMesh Visual" />

</div>

<div class="theme-admonition theme-admonition-important admonition_xJq3 alert alert--info">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)</span>important

</div>

<div class="admonitionContent_BuS1">

You can increase the `Scan Range` in the `LightshipNavMeshManager` to create a larger grid of tiles around the camera.

</div>

</div>

## Adding an Agent to the LightshipNavMesh<a href="#adding-an-agent-to-the-lightshipnavmesh" class="hash-link" aria-label="Direct link to Adding an Agent to the LightshipNavMesh" title="Direct link to Adding an Agent to the LightshipNavMesh">​</a>

To test out the **LightshipNavMesh**, we need to add an **Agent** to the scene to move around on it. The [Gameboard sample project](https://www.nianticspatial.com/docs/nsdk/3.17.0/sample_projects/#navigation-mesh) contains an **Agent** prefab that you can use for testing, but you may want to create your own instead.

To create an **Agent** prefab:

1.  Add an object to the scene to act as an **Agent**:
    1.  In the **Hierarchy**, select the root of the scene.
    2.  Right-click, then select **Create Empty**. Name the new Empty `TestAgent`.
2.  Add a `LightshipNavMeshAgent` component to the new **Agent**.
    1.  In the **Hierarchy**, select `TestAgent`.
    2.  In the **Inspector** window, click **Add Component**. Search for "LightshipNavMeshAgent", then select it to add the component.
3.  Add a `LightshipNavMeshAgentPathRenderer` component to show the path the **Agent** can take in the scene.
    1.  In the **Inspector** window, click **Add Component**, then search for "LightshipNavMeshAgentPathRenderer" and select it to add the component.
    2.  Set the `LightshipNavMeshAgent` and the **Material** properties.
4.  Add a cube to represent the **Agent**:
    1.  In the **Hierarchy**, right-click on `TestAgent`, then hover over **3D Object**. For this example, choose **Cube** to add a basic cube as the testing **Agent**.
    2.  In the **Inspector**, under the **Transform** window, shrink the cube by setting its Scale to (0.2, 0.2, 0.2).
    3.  Change its Position to (0, 0.1, 0), so the bottom of the cube is sitting on (0, 0, 0).
    4.  Uncheck the box next to **Box Collider** to disable it. This will prevent the Cube Agent from colliding with the generated mesh.

<img src="https://www.nianticspatial.com/docs/assets/images/cube_agent_properties-de0521a7f02e3e08e0bcd9d8aee5c875.png" width="500" alt="3D Cube Editor Properties" />

1.  Drag the **Agent** to the **Assets** window to make a prefab, then remove it from the scene.

<img src="https://www.nianticspatial.com/docs/assets/images/navmesh_agent_component-ed1366994e23557cc4446dea33bf7596.png" width="600" alt="LightshipNavMesh Agent" />

### Create a Script to Control the Agent<a href="#create-a-script-to-control-the-agent" class="hash-link" aria-label="Direct link to Create a Script to Control the Agent" title="Direct link to Create a Script to Control the Agent">​</a>

To add a control script to the **Agent**:

1.  Create a script **Asset** to manage user input to control the agent.

    1.  In the **Assets** window, right-click in empty space, then hover over **Create** and select **C# Script**.
    2.  Name the new script `NavMeshHowTo`.

2.  Open the script in your code editor.

3.  Set up code to Handle Touch Inputs:

    1.  Create a private Method named "HandleTouch".
    2.  In editor, we'll use "Input.MouseDown" to detect mouse clicks.
    3.  For phone, the "Input.GetTouch"

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    private void HandleTouch()
    {
        // in the editor we want to use mouse clicks, on phones we want touches.
        #if UNITY_EDITOR
            if (Input.GetMouseButtonDown(0) || Input.GetMouseButtonDown(1) || Input.GetMouseButtonDown(2))
        #else
            //if there is no touch or touch selects UI element
            if (Input.touchCount <= 0)
                return;
            var touch = Input.GetTouch(0);

            // only count touches that just began
            if (touch.phase == UnityEngine.TouchPhase.Began)
        #endif
            {
                // do something with touches
            }
    }
    ```

    </div>

    </div>

4.  Convert touch points from the screen to 3D Coordinates

    1.  Add a Camera field to the top of script:

        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        [SerializeField]
        private Camera _camera;
        ```

        </div>

        </div>

        <div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

        <div class="admonitionHeading_Gvgb">

        <span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

        </div>

        <div class="admonitionContent_BuS1">

        `[SerializeField]` allows private properties to be available in the Inspector window.

        </div>

        </div>

    2.  This will use Unity's <a href="https://docs.unity3d.com/ScriptReference/Camera.ScreenToWorldPoint.html" target="_blank" rel="noopener noreferrer"><code>Camera.ScreenPointToRay</code></a> function. Call the method in "HandleTouch" to create a ray pointing from the camera.

        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        #if UNITY_EDITOR
            Ray ray = _camera.ScreenPointToRay(Input.mousePosition);
        #else
            Ray ray = _camera.ScreenPointToRay(touch.position);
        #endif
        ```

        </div>

        </div>

    3.  Check if the Ray can hit the mesh using "Physics.Raycast" and get the resulting point.

        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        {
            // do something with touches
            RaycastHit hit;
            if (Physics.Raycast(ray, out hit))
            {
                // use the 3D point to guide the Agent
            }
        }
        ```

        </div>

        </div>

5.  Guide your Agent using the 3D points from touches

    1.  We'll need to instantiate an Agent from the prefab created earlier.
    2.  Add a `LightshipNavMeshAgent` field to the top of class for the agent prefab:
        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        [SerializeField]
        private LightshipNavMeshAgent _agentPrefab;
        ```

        </div>

        </div>
    3.  Add a private `LightshipNavMeshAgent` field under the Agent Prefab to be used as the instance of the Agent:
        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        private LightshipNavMeshAgent _agentInstance;
        ```

        </div>

        </div>
    4.  The Agent Instance will be a specific occurrence of the Agent Prefab in the scene. The Prefab is merely used as a blueprint to create an Instance.
    5.  If the Agent does not exist yet, it will be created at the hit point. Otherwise, make its new destination on the `NavMesh` the hit point.
        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        // do something with touches
        RaycastHit hit;
        if (Physics.Raycast(ray, out hit))
        {
            // use the 3D point to guide the Agent
            if (_agentInstance == null )
            {
                _agentInstance = Instantiate(_agentPrefab);
                _agentInstance.transform.position = hit.point;
            }
            else
            {
                _agentInstance.SetDestination(hit.point);
            }
        }
        ```

        </div>

        </div>

6.  Add the "HandleTouch" method to the Update method, so the script checks for touches every frame.

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    void Update()
    {
        HandleTouch();
    }
    ```

    </div>

    </div>

7.  Attach the script to the **NavMeshManager**.

    1.  Select your **NavMeshManager** GameObject in the Hierarchy, then click "Add Component" in the **Inspector** window.
    2.  Search for "NavMeshHowTo", then select it to add the controller script to the prefab.
    3.  Make sure to set the properties for **Camera** and **Agent Prefab**

    <img src="https://www.nianticspatial.com/docs/assets/images/navmesh_howto_editor-f584042b0e9b6d36e1b75dcae2be0c68.png" width="600" alt="Lightship NavMesh Script in Editor" />

8.  Now you should be able to spawn and direct the cube to any tile on the **Navigation Mesh**.

    <div style="text-align:center">

    <img src="https://www.nianticspatial.com/docs/assets/images/visualize_navmesh_agent-23c86454588f8c5d76c75b231d5afffd.gif" width="400" alt="Lightship NavMesh with Agent Visualizer" />

    </div>

9.  Let's make the **NavMesh** visuals optional to get a cleaner view. In the `NavMeshHowTo` script:

    1.  Add a field to the `LightshipNavMeshManager` to get a reference to its renderer component.
        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        [SerializeField]
        private LightshipNavMeshManager _navmeshManager;
        ```

        </div>

        </div>
    2.  Create a new method named "SetVisualization" that gets the **NavMeshRenderer** Components and sets their state.
        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        public void SetVisualisation(bool isVisualizationOn)
        {
            //turn off the rendering for the navmesh
            _navmeshManager.GetComponent<LightshipNavMeshRenderer>().enabled = isVisualizationOn;

            if (_agentInstance != null)
            {
                //turn off the path rendering on any agent
                _agentInstance.GetComponent<LightshipNavMeshAgentPathRenderer>().enabled = isVisualizationOn;
            }
        }
        ```

        </div>

        </div>
    3.  Call this method through a UI Button or in a script.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/navmesh_with_agent-129182891cd476eb534d35666ba0b4d3.gif" width="400" alt="Lightship NavMesh with Agent" />

</div>

Click here to show the final NavMeshHowTo script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using UnityEngine;
using Niantic.Lightship.AR.NavigationMesh;

/// SUMMARY:
/// LightshipNavMeshSample
/// This sample shows how to use LightshipNavMesh to add user driven point and click navigation.
/// When you first touch the screen, it will place your agent prefab.
/// Tapping a location moves the agent to that location.
/// The toggle button shows/hides the navigation mesh and path.
/// It assumes the _agentPrefab has LightshipNavMeshAgent on it.
/// If you have written your own agent type, either swap yours in or inherit from it.
///
public class NavMeshHowTo : MonoBehaviour
{
    [SerializeField]
    private Camera _camera;

    [SerializeField]
    private LightshipNavMeshManager _navmeshManager;

    [SerializeField]
    private LightshipNavMeshAgent _agentPrefab;

    private LightshipNavMeshAgent _agentInstance;

    void Update()
    {
        HandleTouch();
    }

    public void SetVisualization(bool isVisualizationOn)
    {
        //turn off the rendering for the navmesh
        _navmeshManager.GetComponent<LightshipNavMeshRenderer>().enabled = isVisualizationOn;

        if (_agentInstance != null)
        {
            //turn off the path rendering on the active agent
            _agentInstance.GetComponent<LightshipNavMeshAgentPathRenderer>().enabled = isVisualizationOn;
        }
    }

    private void HandleTouch()
    {
        //in the editor we want to use mouse clicks, on phones we want touches.
    #if UNITY_EDITOR
        if (Input.GetMouseButtonDown(0) || Input.GetMouseButtonDown(1) || Input.GetMouseButtonDown(2))
    #else
        var touch = Input.GetTouch(0);

        //if there is no touch or touch selects UI element
        if (Input.touchCount <= 0)
            return;
        if (touch.phase == UnityEngine.TouchPhase.Began)
    #endif
        {
        #if UNITY_EDITOR
            Ray ray = _camera.ScreenPointToRay(Input.mousePosition);
        #else
            Ray ray = _camera.ScreenPointToRay(touch.position);
        #endif
            //project the touch point from screen space into 3d and pass that to your agent as a destination
            RaycastHit hit;
            if (Physics.Raycast(ray, out hit))
            {
                if (_agentInstance == null )
                {
                    _agentInstance = Instantiate(_agentPrefab);
                    _agentInstance.transform.position = hit.point;
                }
                else
                {
                    _agentInstance.SetDestination(hit.point);
                }
            }
        }
    }
}
```

</div>

</div>

</div>

</div>

</div>

</div>
