---
source: https://www.nianticspatial.com/docs/nsdk/how-to/vps/mesh_download/
title: How to Download a Mesh Using the API
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Download a Mesh Using the API

</div>

With the Mesh Download API, you can download and create a mesh of any Site at runtime, allowing you to dynamically create mesh overlays in AR scenes. This feature makes it easier to test AR experiences by allowing you to check that your mesh lines up with the real world without having to leave the test environment. For example, you can download a stored mesh after localizing to see how far offset your localization is and figure out how it needs to change. Mesh downloading also allows developers to place content in scenes and explore environmental interactions without needing to stop testing and set up each mesh they want to try.

Its optional parameters provide ways to customize how it works, some of which are explored in this How-To.

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need:

- a Unity project with NSDK installed and configured
- an NSDK access token configured for the app; see [Authorization](https://www.nianticspatial.com/docs/nsdk/auth_getting_started/)
- a Site anchor payload copied from Scaniverse or obtained through the [Sites API](https://www.nianticspatial.com/docs/nsdk/features/sites/)

For project and scene setup, see [Set up the Niantic SDK for Unity](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-the-niantic-sdk-for-unity).

## Download a Site mesh<a href="#download-a-site-mesh" class="hash-link" aria-label="Direct link to Download a Site mesh" title="Direct link to Download a Site mesh">​</a>

[`LocationMeshManager`](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.LocationMeshManager/) is a component included with NSDK. Add **Location Mesh Manager** to a `GameObject`, then reference that component from the script that downloads the mesh:

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using NianticSpatial.NSDK.AR.Subsystems;

[SerializeField]
private LocationMeshManager locationMeshManager;
```

</div>

</div>

In the Inspector, drag the `GameObject` containing **Location Mesh Manager** into this field. Then call `GetLocationMeshForPayloadAsync` with the Site anchor payload. The method downloads the mesh asynchronously and creates a `GameObject` containing the generated mesh. The following code assumes that `anchorPayload` contains the payload for the selected Site.

View the Unity mesh download code

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
GameObject mesh = await locationMeshManager.GetLocationMeshForPayloadAsync(
    anchorPayload,
    getTexture: true
);

// A null result means that the request did not produce a mesh.
if (mesh == null)
{
    return;
}
```

</div>

</div>

</div>

</div>

The returned `GameObject` contains the downloaded geometry and, when requested, its texture. You can render it directly, inspect its child mesh objects, add collision geometry through the download options, or attach it to a tracked Site anchor.

### Position the mesh at its Site<a href="#position-the-mesh-at-its-site" class="hash-link" aria-label="Direct link to Position the mesh at its Site" title="Direct link to Position the mesh at its Site">​</a>

Downloading a mesh does not localize the device or position the mesh in the AR scene. To align it with the physical Site, track an anchor with the same payload and parent the downloaded mesh to that anchor:

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
if (!arVps2Manager.TryTrackAnchor(anchorPayload, out ARVps2Anchor siteAnchor))
{
    return;
}

// Passing false preserves the mesh transform relative to the Site anchor.
mesh.transform.SetParent(siteAnchor.transform, false);

// Update visibility as tracking changes in your app.
mesh.SetActive(siteAnchor.trackingState == TrackingState.Tracking);
```

</div>

</div>

Unity scene requirements and sample files

<div>

<div class="collapsibleContent_i85q">

A project that downloads and renders a mesh needs authorization, a `Location Mesh Manager`, a compatible mesh material, and a source for the Site anchor payload. Placing the mesh at its physical Site also requires an `AR Session`, an `XR Origin` with an AR camera and `AR VPS2 Manager`, and camera and location permissions.

The <a href="https://github.com/nianticspatial/nsdk-samples-csharp" target="_blank" rel="noopener noreferrer">NSDK Unity sample project</a> shows how these pieces are connected:

- `Assets/Samples/VPS2/Scenes/VPS2Localization.unity` contains the scene components.
- `Assets/Samples/VPS2/Scripts/VPS2LocalizeDemo.cs` contains the anchor tracking and mesh download flow.
- `Assets/Samples/VPS2/Scripts/SitesTargetListManager.cs` obtains the Site anchor payload.

The sample's device UI does not expose mesh download as an action; use these files as implementation references.

</div>

</div>

## Customize the mesh download<a href="#customize-the-mesh-download" class="hash-link" aria-label="Direct link to Customize the mesh download" title="Direct link to Customize the mesh download">​</a>

`GetLocationMeshForPayloadAsync` also accepts options for download size, collision geometry, textures, and cancellation:

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
var mesh = await _meshManager.GetLocationMeshForPayloadAsync(
    _anchorPayload,
    maxDownloadSizeKb: 10240,
    addCollider: true,
    getTexture: true,
    cancelOnDisable: true
);
```

</div>

</div>

- `maxDownloadSizeKb` limits the download size.
- `addCollider` adds collision geometry to the generated mesh object.
- `getTexture` requests texture data. When it is `false`, the API requests vertex-colored geometry instead.
- `cancelOnDisable` cancels the request if `LocationMeshManager` is disabled.

The mesh must use a material compatible with the project's render pipeline. Refer to the `Location Mesh Manager` in the sample scene for the setup used by the installed NSDK version. Textured meshes contain more download data; vertex-colored meshes are smaller and require a material that renders vertex colors.

## Known Issues<a href="#known-issues" class="hash-link" aria-label="Direct link to Known Issues" title="Direct link to Known Issues">​</a>

- If no mesh is available for the supplied Site anchor payload, the API returns `null` or an empty result, depending on the platform.
- Some meshes can be quite large. If download size or runtime performance is a concern, consider setting a maximum download size.

## More Information<a href="#more-information" class="hash-link" aria-label="Direct link to More Information" title="Direct link to More Information">​</a>

See [`LocationMeshManager`](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Subsystems.LocationMeshManager/) in the Unity API reference.

</div>

</div>
