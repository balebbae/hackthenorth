---
source: https://www.nianticspatial.com/docs/nsdk/how-to/vps/tooling/manage_test_scans/
title: How to Manage Site Scans and Meshes
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Manage Site Scans and Meshes

</div>

Use the Scaniverse app to capture and upload scans for a Site. Use Scaniverse Web to manage the Site and its generated assets.

## Create and manage Site scans<a href="#create-and-manage-site-scans" class="hash-link" aria-label="Direct link to Create and manage Site scans" title="Direct link to Create and manage Site scans">​</a>

1.  In the Scaniverse app, create or open a Site.
2.  Record scans that cover the physical space. Scans in the same Site must overlap so they can be connected into one representation.
3.  Upload the scans for processing.
4.  Open the Site in <a href="https://scaniverse.nianticspatial.com/" target="_blank" rel="noopener noreferrer">Scaniverse Web</a> to review its scans and generated assets.
5.  Generate a production VPS asset when the Site is ready for localization.

For the complete capture, upload, and asset-generation workflow, see [Create your first Site](https://www.nianticspatial.com/docs/nsdk/first_localization/#create-your-first-site).

## Download a Site mesh<a href="#download-a-site-mesh" class="hash-link" aria-label="Direct link to Download a Site mesh" title="Direct link to Download a Site mesh">​</a>

To download a Site mesh at runtime, use the NSDK Mesh Download API:

1.  Get the anchor payload from the Site's production VPS asset in Scaniverse Web, or retrieve it through the [Sites API](https://www.nianticspatial.com/docs/nsdk/features/sites/).
2.  Pass that payload to the mesh-download method for your platform.
3.  If the mesh must align with the physical Site, track an anchor with the same payload and place the downloaded mesh relative to that tracked anchor.

See [How to Download a Mesh Using the API](https://www.nianticspatial.com/docs/nsdk/how-to/vps/mesh_download/) for Unity, Swift, and Kotlin examples.

To download a mesh file for offline authoring:

1.  Open the Site in Scaniverse Web.
2.  Open **Assets \> History** and select the generated asset version.
3.  Download the available mesh as an FBX or GLB file from the asset details.

Use the FBX or GLB in the 3D authoring tool or engine workflow appropriate for your project.

</div>

</div>
