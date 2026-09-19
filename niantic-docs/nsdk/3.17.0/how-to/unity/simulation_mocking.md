---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/unity/simulation_mocking/
title: How to Set Up and Run Lightship Simulation
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Set Up and Run Lightship Simulation

</div>

Lightship Simulation allows you to test your AR content in-editor without having to use Unity's playback mode. Our simulation mode allows you to move freely around a virtual 3D space while testing out your AR features in real time.

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Unity project with ARDK 3.17 or higher installed and a basic AR scene. For more information, see [Installing ARDK 3](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/) and [Setting up a Basic AR Scene](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/#setting-up-a-basic-ar-scene).

## Enabling Lightship Simulation<a href="#enabling-lightship-simulation" class="hash-link" aria-label="Direct link to Enabling Lightship Simulation" title="Direct link to Enabling Lightship Simulation">​</a>

To enable Lightship Simulation in your Unity project:

1.  In the **Lightship** top menu, select **XR Plug-in Management**, then check the box labeled **Niantic Lightship Simulation**. This will enable Unity's XR Simulation as well.

<img src="https://www.nianticspatial.com/docs/assets/images/xr_settings_simulation-026cf148a571b2b2dff83c2565c701a4.png" width="450" alt="Selecting Niantic Lightship Simulation in XR Plugin Management" />

## Creating and Setting a SimulationEnvironment<a href="#creating-and-setting-a-simulationenvironment" class="hash-link" aria-label="Direct link to Creating and Setting a SimulationEnvironment" title="Direct link to Creating and Setting a SimulationEnvironment">​</a>

Before running your simulation, you will need to turn a prefab into a `SimulationEnvironment` that the system can navigate by making one from scratch or using the default environment as a template.

- To create an environment from scratch:
  1.  Open or create the prefab you would like to use as your `SimulationEnvironment`.
  2.  In the **Inspector**, click **Add Component** and add a **Simulation Environment** component to the prefab.
  3.  In the **Simulation Environment** Component, set the **Camera Starting Pose (Position)** to `0, 0, 0` and the **Camera Movement Bounds (Extents)** to a value large enough to encompass the entire simulation, such as `1000, 1000, 1000`.
- To use the default environment as a template:
  1.  Open the **Window** top menu, then select **XR** \> **AR Foundation** \> **XR Environment**. The **XR Environment** window will open.
  2.  In the **XR Environment** overlay, click the icon with a pencil and a plus sign, then select **Create environment**.
  3.  Choose a name and location in your project assets to save the prefab and click **Save**.
  4.  In the **Hierarchy**, select the root object with your chosen environment name.
  5.  In the **Inspector**, open the **Simulation Environment** Component, then set the **Camera Starting Pose (Position)** to `0, 0, 0` and the **Camera Movement Bounds (Extents)** to a value large enough to encompass the entire simulation, such as `1000, 1000, 1000`.

To set the environment:

1.  Open the **Window** top menu, then select **XR** \> **AR Foundation** \> **XR Environment**. The **XR Environment** window will open.
2.  Click the drop-down menu in the **XR Environment** overlay, then select your environment prefab from the list to assign it in Unity.

<img src="https://www.nianticspatial.com/docs/assets/images/unity_choose_env-3bd8d459e0a6e322ba8dcc1897641d4d.png" width="450" alt="Selecting an environment in Unity" />

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

Without a simulation environment set, Unity will default to a basic environment. If you load your simulation and find yourself in the default, make sure the camera values are properly set and that there is no type mismatch.

</div>

</div>

## Lightship Simulation Settings<a href="#lightship-simulation-settings" class="hash-link" aria-label="Direct link to Lightship Simulation Settings" title="Direct link to Lightship Simulation Settings">​</a>

To change the Lightship simulation settings, open the **Lightship** top menu, then select **Settings**. The simulation settings are at the bottom of the Lightship Settings menu.

The simulation settings are as follows:

- **Environment Prefab** - This option provides a place to set the environment prefab.
- **Use Z-Buffer Depth** - Enabling this option will use the exact depth from the simulation. Disabling this option will use computed depth from the Niantic Spatial Platform depth algorithm.
- **Use Lightship Persistent Anchors** - Disable this option to use Simulation VPS. Enabling this option will run real VPS on simulated environments. Disabling it will enable additional options for configuring Simulation VPS:
  - **Minimum/Maximum Anchor Discovery Time Seconds** - Sets the minimum and maximum time (in seconds) that must pass before the anchor is surfaced.
  - **Apply Translational Offset** - Enabling this offsets the position of the anchor when it is surfaced by a random amount between 0 and the Offset Severity.
  - **Translational Offset Severity Meters** - Specifies the maximum distance (in meters) that the anchor can be offset.
  - **Apply Rotational Offset** - Enabling this offsets the rotation of the anchor when it is surfaced by a random amount between 0 and the Offset Severity.
  - **Rotational Offset Severity Degrees** - Specifies the maximum rotation (in degrees) of the anchor offset.
  - **Surface Anchor Failure** - Enabling this allows you to test a failed anchor instead of a successful one.
  - **Tracking State Reason** - Specifies which kind of failed anchor to test.

<img src="https://www.nianticspatial.com/docs/assets/images/anchors_checkbox-d20c1cbd6a796d930ada622d7cfcf25a.png" width="450" alt="The Simulated Environment Scene appearing in the Hierarchy" />

## Running and Using the Simulation<a href="#running-and-using-the-simulation" class="hash-link" aria-label="Direct link to Running and Using the Simulation" title="Direct link to Running and Using the Simulation">​</a>

Once you have loaded the simulation environment, press Play. Lightship will load the environment into a new scene called `Simulated Environment Scene` on Layer 30, then start the simulation.

<img src="https://www.nianticspatial.com/docs/assets/images/sim_env_scene-add26a39ca24e04e7f0a056edaec612c.png" width="450" alt="The Simulated Environment Scene appearing in the Hierarchy" />

To unlock movement in the simulation, hold down the right mouse button (or tap and hold with two fingers on trackpad) in the game view, then use these controls to move around:

- WASD keys to move forward/backward and strafe;
- Move the mouse to rotate the view;
- Q and E keys to move up and down;
- Shift to go faster.

</div>

</div>
