---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/tooling/manage_test_scans/
title: How to Manage Test Scans
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Manage Test Scans

</div>

A test scan is a location that contains a single mesh for developing and testing VPS experiences. Any test scans you create are only available to your developer account. Test scans are useful for developing and testing VPS experiences while a Public Location is not yet activated. Due to performance issues, they are not supported for use in published projects.

Test scans are created using the Niantic Scaniverse app. Ensure you’re logged in using your Lightship credentials. For more information about using the app, see [Scaniverse for Lightship](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/tooling/lightship_scaniverse/).

## Scanning a Mesh<a href="#scanning-a-mesh" class="hash-link" aria-label="Direct link to Scanning a Mesh" title="Direct link to Scanning a Mesh">​</a>

1.  After you have followed the instructions to connect Scaniverse to your lightship account [Scaniverse for Lightship](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/tooling/lightship_scaniverse/).

2.  Tap on the map icon to open the Geospatial Browser tab in Scaniverse.

3.  Press the + icon to add a new location

4.  Select Test

5.  Scan the location

6.  Press Upload

7.  Once processed, you can preview the mesh and add it to your project from the Geospatial Browser **Test Scans** tab (located in the **Locations** section at the bottom).

    ![List of test scans](https://www.nianticspatial.com/docs/assets/images/gsb_test_scans-b41d335bfd7332942609a2909b2f01d9.png)

8.  If your test scan fails processing, you may need to rescan. Reach out to `support@lightship.dev` for more information.

## Downloading Meshes<a href="#downloading-meshes" class="hash-link" aria-label="Direct link to Downloading Meshes" title="Direct link to Downloading Meshes">​</a>

You can download a mesh for your Private or Test VPS Location that you can use for development purposes in your Unity project.

Meshes are only available for successfully **Processed** VPS Locations. To download a mesh, select the location and click the **Download Mesh** button.

![Mesh download button](https://www.nianticspatial.com/docs/assets/images/gsb_download_mesh_3.0-ef7684c9cf5c0bc9275669beb543fa55.png)

When you download a mesh, you will receive a zip file that contains mesh data in <a href="https://www.autodesk.com/products/fbx/overview" target="_blank" rel="noopener noreferrer">FBX format</a> and a `.json` file that contains the origin anchor for the mesh. You can use this file for previewing anchored content in Unity and it can be used with the VPS Authoring Assistant. See [Adding a Real-World Location to Unity](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/real_world_location_ar/#adding-a-real-world-location-to-unity) for more information.

<div class="theme-admonition theme-admonition-tip admonition_xJq3 alert alert--success">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)</span>tip

</div>

<div class="admonitionContent_BuS1">

Instead of unzipping the file, use the VPS Authoring Assistant in Unity and drag the file directly into your Unity project.

</div>

</div>

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

The origin anchor is generated each time you download the private mesh zipfile, however previously downloaded anchors for the same mesh are still valid and can still be used as long as the test scan is still valid.

</div>

</div>

When placing your virtual content in Unity, you can import the zip file to help you position it relative to the mesh. When running on your device, localize to your Private VPS Location, restore the origin anchor, then position your virtual content relative to the origin anchor.

</div>

</div>
