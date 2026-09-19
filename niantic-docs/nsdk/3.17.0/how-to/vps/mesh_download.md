---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/mesh_download/
title: How to Download a Mesh Using the API
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Download a Mesh Using the API

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

With the Mesh Downloading API, you can download and create a mesh of any Public Location at runtime. Its optional parameters provide ways to customize how it works, some of which are explored in this How-To.

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Unity project with ARDK installed and an AR scene with Location AR. For more information, see [Installing ARDK 3](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/) and [How to Place Content in Real-World Locations Using Location AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/real_world_location_ar/). Your project must have an `ARLocation` for this How-To.

## Getting Ready in Unity<a href="#getting-ready-in-unity" class="hash-link" aria-label="Direct link to Getting Ready in Unity" title="Direct link to Getting Ready in Unity">​</a>

Before using the Mesh Downloading API, you will need to add a **Location Mesh Manager** Component and an associated script that will download the mesh.

To create the **Location Mesh Manager** and mesh downloading script:

1.  Add `GameObjects` to hold the manager and script:

    1.  In the **Hierarchy**, right-click in your AR scene, then select **Create Empty** and name the new `GameObject` `LocationMeshManager`. Repeat these steps, but name the second object `MeshDownloadHowTo`.

2.  Select `LocationMeshManager`, then, in the **Inspector**, click **Add Component** and add a **Location Mesh Manager**.

    <img src="https://www.nianticspatial.com/docs/assets/images/add_manager-0cae30778e5aa3c386356f1a279e128e.png" width="400" alt="Adding a Location Mesh Manager" />

3.  Select `MeshDownloadHowTo`, then, in the **Inspector**, click **Add Component** and add a **New Script**. Name it `MeshDownloadHowTo`.

    <img src="https://www.nianticspatial.com/docs/assets/images/add_script-93690b6b98f550c820e8699d9c04b8bb.png" width="400" alt="Adding the Mesh Download How To script" />

## Downloading a Mesh Using an AR Location Payload<a href="#downloading-a-mesh-using-an-ar-location-payload" class="hash-link" aria-label="Direct link to Downloading a Mesh Using an AR Location Payload" title="Direct link to Downloading a Mesh Using an AR Location Payload">​</a>

With the Location Mesh Manager ready, you can use the API to download a mesh and set its position at runtime. In this example, you will do this using an `ARLocation` payload to place the mesh on top of the real world in that location. This will generate a `GameObject` with the mesh populated that you can use or modify like any other. For example, you might have the mesh download and appear when the user pushes a button or pass it to some other function for collision detection.

To get started, open `MeshDownloadHowTo.cs`, then replace the code with the following code:

Click to reveal the Mesh Download function

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System.Threading.Tasks;

using Niantic.Lightship.AR.LocationAR;
using Niantic.Lightship.AR.PersistentAnchors;
using Niantic.Lightship.AR.Subsystems;

using UnityEngine;

public class MeshDownloadHowTo : MonoBehaviour
{
  [SerializeField]
  private LocationMeshManager _meshManager;

  [SerializeField]
  private ARLocationManager _arLocationManager;

  private GameObject _downloadedMesh;
  private bool _startedDownload;

  private void Start()
  {
    _arLocationManager.locationTrackingStateChanged += OnLocationTrackingStateChanged;
  }

  private void OnLocationTrackingStateChanged(ARLocationTrackedEventArgs args)
  {
    if (args.Tracking && !_startedDownload)
    {
      _startedDownload = true;
      _ = DownloadAndPositionMeshAsync(location: args.ARLocation);
    }
  }

  private async Task DownloadAndPositionMeshAsync(ARLocation location)
  {
    var payload = location.Payload;

    // wait async for the mesh to download so it doesn't block the main thread
    var go = await _meshManager.GetLocationMeshForPayloadAsync(payload.ToBase64());

    // set the mesh as a child of the ARLocation's position and place it in the scene
    go.transform.SetParent(location.transform, false);
    _downloadedMesh = go;
  }

  private void OnDestroy()
  {
    if (_downloadedMesh)
    {
      Destroy(_downloadedMesh);
    }
  }
}
```

</div>

</div>

</div>

</div>

## Adjusting the Mesh at Runtime<a href="#adjusting-the-mesh-at-runtime" class="hash-link" aria-label="Direct link to Adjusting the Mesh at Runtime" title="Direct link to Adjusting the Mesh at Runtime">​</a>

Once your mesh is downloaded, you can adjust it using the API options. In this example, you will use the API to get a textured mesh and lighten its transparency. By placing it using an `ARLocation` payload, you can create a transparent mesh overlay of any existing Public Location at runtime.

Before updating the script, create a Material that supports transparency and add it to `LocationMeshManager`:

1.  In the **Project** window, right-click in the **Assets** directory, then open the **Create** menu and select **Material**. Name the new material `trans_light`.

2.  Select `trans_light`, then, in the **Inspector**, set the **Rendering Mode** to **Transparent**.

    <img src="https://www.nianticspatial.com/docs/assets/images/make_trans_light-c03957f4f6ec848a438c088c763f5ab9.png" width="500" alt="Making the light transparent material" />

3.  In the **Hierarchy**, select `LocationMeshManager`, then add `trans_light` to the **Textures Mesh Material** field. Then, in the **Project** folder, navigate to **Packages-\>Niantic Lightship AR Plugin-\>Assets-\>Materials** and drag the `vertex_color` material on the **Vertex Color Material** field.

    <img src="https://www.nianticspatial.com/docs/assets/images/add_trans_light-bce6dd9cfbad0ff1d66c8d57d4da82f4.png" width="500" alt="Adding the light transparent material" />

Open `MeshDownloadHowTo.cs`, then update the `DownloadAndPositionMeshAsync` function with the following code:

Click to reveal the updated Mesh Download function

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
private async Task DownloadAndPositionMeshAsync(ARLocation location)
{
    var payload = location.Payload;
    // Use a textured option for the mesh download
    var go = await _meshManager.GetLocationMeshForPayloadAsync(payload.ToBase64(), meshFormat: MeshDownloadRequestResponse.MeshAlgorithm.TEXTURED);
    go.transform.SetParent(location.transform, false);

    // Get the mesh renderers and set the transparency of the material to 0.5
    foreach (var meshRenderer in go.GetComponentsInChildren<MeshRenderer>())
    {
        var mat = meshRenderer.material;
        if (mat != null)
        {
            var color = mat.color;
            color.a = 0.5f;
            meshRenderer.material.color = color;
        }
    }
    _downloadedMesh = go;
}
```

</div>

</div>

</div>

</div>

## Using Materials to Change a Mesh<a href="#using-materials-to-change-a-mesh" class="hash-link" aria-label="Direct link to Using Materials to Change a Mesh" title="Direct link to Using Materials to Change a Mesh">​</a>

By supplying different materials in the Unity Editor to the manager that controls the mesh, you can modify the mesh's traits using code instead of in the editor. By default, the API exposes two different types of mesh: `VERTEX_COLOR` and `TEXTURED`. Vertex-colored meshes are faster to download, but require a material that handles colored vertices to render properly. (We provide a shader and material that can do this. Look for `VertexColor.shader` and `vertex_color.mat` in Unity!) Textured meshes can be rendered with the standard Unity material (or any other that handles textures), but including texture information increases download size.

In particular, we recommend using this feature to create a transparent mesh for debugging so that you can see if it overlays properly in real time.

## Known Issues<a href="#known-issues" class="hash-link" aria-label="Direct link to Known Issues" title="Direct link to Known Issues">​</a>

- Not all mesh types are available at each location. Specifically, coverage meshes are not available at private locations. If the requested mesh type is not available, the API will return `null` or an empty result for the mesh.
- Some meshes can be quite large. If download size or runtime performance is a concern, consider setting a maximum download size.

## More Information<a href="#more-information" class="hash-link" aria-label="Direct link to More Information" title="Direct link to More Information">​</a>

- For general information, see the [Mesh Download section](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/lightship_vps/#downloading-the-3d-mesh-asset-of-a-vps-location) in the [VPS feature page](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/lightship_vps/).
- For details and more optional parameters, see the Mesh Download API Reference.
- To see Mesh Downloading in action, try out the VPS Coverage API sample.

</div>

</div>
