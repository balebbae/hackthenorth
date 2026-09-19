---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/real_world_location_ar/
title: Place Content in Real-World Locations Using Location AR
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Place Content in Real-World Locations Using Location AR

</div>

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

The AR Location is the highest-level abstraction that allows us to "anchor" virtual objects to the real world.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/placing_cube-bfdd95b512d7f9612a0e95763d4561dc.gif" width="1200" alt="Placing Cube in Unity" />

</div>

This how-to covers:

- Importing a real-world location from the Geospatial Browser (GSB) into Unity;
- Placing content in a real-world location;
- Testing placed content, either using a mockup or on location.

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

1.  You will need a Unity project with ARDK installed and a set-up basic AR scene. For more information, see [Setup ARDK 3](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/) and [Setting up an AR Scene](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/#setting-up-a-basic-ar-scene).
2.  You will need a valid [API Key](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/#create-a-lightship-account-and-add-api-key).

## Adding a Real-World Location to Unity<a href="#adding-a-real-world-location-to-unity" class="hash-link" aria-label="Direct link to Adding a Real-World Location to Unity" title="Direct link to Adding a Real-World Location to Unity">​</a>

To add an AR location to Unity:

1.  Go to the <a href="https://lightship.dev/account/geospatial-browser/" target="_blank" rel="noopener noreferrer">Geospatial Browser</a> and find the location you want to build content for. The data will download as a .zip file; **do not unzip it**. For more information on downloading location data, see [Downloading Meshes](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/tooling/manage_test_scans/#downloading-meshes).
2.  Drag and drop the downloaded zip file into the **Assets** directory in the **Project** window. Once the import process completes, it will create two assets, a **Mesh** `.prefab` file and a **Manifest** `.asset` file.
3.  Turn on **Persistent Anchors** in **Lightship Settings**:
    1.  Click the **Lightship** top menu, then select **Settings**.
    2.  In the **Inspector** window, check the **Enabled** box next to **Persistent Anchors**.

    <img src="https://www.nianticspatial.com/docs/assets/images/persistent_anchors-9aae8d70ca754c5e98909fbc71171065.png" width="600" alt="Unity menu with &#39;Enable Persistent Anchors&#39; checked" />
4.  Add an **AR Location Manager** component to the `XROrigin`:
    1.  Select the `XROrigin` in the **Hierarchy**, then, in the **Inspector** window, click **Add Component** and search for **ARLocationManager**.
    2.  In the **ARLocationManager** Component, click **Add AR Location** to create a new `ARLocation`.
5.  In the **Hierarchy**, select the `ARLocation` to show its Component in the **Inspector**. Drag and drop the **Manifest** from the **Assets** directory to the **AR Location Manifest** field in the Component.
    1.  This will update the name of the `ARLocation` GameObject to match the manifest and set up its fields for tracking.

## Adding Real-World AR Content<a href="#adding-real-world-ar-content" class="hash-link" aria-label="Direct link to Adding Real-World AR Content" title="Direct link to Adding Real-World AR Content">​</a>

When adding your AR content, remember the following:

1.  Add your AR content as a child of the manifest (`ARLocation`). For example, to add a **Cube** to a location:
    1.  In the **Hierarchy**, right-click the `ARLocation`, then mouse over **3D Object** and select **Cube**.
    2.  In the **Inspector**, set the cube's **Scale** to `0.5`. Set its position so that you can see it in your test location.
2.  Enable auto-tracking:
    1.  In the **Hierarchy**, select the **XROrigin**, then, in the **Inspector** window, check the **Auto-Track** box in the **ARLocationManager** Component.
    2.  When auto-tracking is enabled, the `ARLocationManager` will start tracking on the currently active `ARLocation` when the component is enabled. See [How to Use Location AR with Code](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/location_ar_code/) for more options and information.

<img src="https://www.nianticspatial.com/docs/assets/images/remote_authoring-24c6dc7bdabe3107a96f8c2bfc262cfc.png" width="600" alt="Remote authoring content" />

When an `ARLocation` is tracked during runtime, it is placed in the `ARTrackable` field of the `ARPersistentAnchor` it is associated with. This maintains the relative position of all children of the `ARLocation` in the scene. When placing or updating child content of the `ARLocation`, make your changes in local transform space to make sure the scene stays consistent.

## Testing Real-World AR Content<a href="#testing-real-world-ar-content" class="hash-link" aria-label="Direct link to Testing Real-World AR Content" title="Direct link to Testing Real-World AR Content">​</a>

The most accurate way to test real-world AR content is by building your Unity app to a device and physically visiting the location to test it out. Because this is not always possible, Lightship also provides a Simulation subsystem for Location AR. To enable Simulation, see the [Simulation documentation](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/unity/simulation_mocking/)

Simulated persistent anchors will have a consistent **trackableId**, but these **trackableIds** are not consistent with resolving real anchors (Playback or Live VPS).

<div class="theme-admonition theme-admonition-tip admonition_xJq3 alert alert--success">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)</span>tip

</div>

<div class="admonitionContent_BuS1">

You can also test localizations using Playback. See [How to Setup Playback](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/playback/setting_up_playback/).

</div>

</div>

## More Information<a href="#more-information" class="hash-link" aria-label="Direct link to More Information" title="Direct link to More Information">​</a>

- [Creating Location AR Experiences with VPS](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/lightship_vps/)
- [Using ARLocationManager in Code](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/location_ar_code/)
- [Querying VPS Locations with the VPS Coverage API](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/location_ar_vps_coverage/)

</div>

</div>
