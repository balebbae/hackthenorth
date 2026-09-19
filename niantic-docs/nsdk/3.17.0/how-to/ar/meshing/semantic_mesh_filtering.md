---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/meshing/semantic_mesh_filtering/
title: How to Exclude Semantic Channels with Mesh Filtering
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Exclude Semantic Channels with Mesh Filtering

</div>

Semantic Mesh Filtering allows you to set an allow list or block list of semantic channels. These follow standard allow/block list behavior. Using an allow list will exclude all channels not in the list, while the block list excludes all channels in the list.

For a list of usable semantic channels, see [Scene Segmentation](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/semantics/#available-semantic-channels).

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/mesh_filter-6428356470a83127d8e419c4815eb60b.gif" width="300" alt="Example of Mesh Filtering being turned on and off" />

</div>

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Unity project with NSDK installed and a basic AR scene. For more information, see [Setting Up the Niantic SDK for Unity](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/) and [Setting up a Basic AR Scene](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/#setting-up-a-basic-ar-scene).

Your project must also have the Lightship Meshing subsystem. To add Meshing to your project, follow the steps under [Creating the Mesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/meshing/adding_meshing/).

## Setting Up Semantic Mesh Filtering<a href="#setting-up-semantic-mesh-filtering" class="hash-link" aria-label="Direct link to Setting Up Semantic Mesh Filtering" title="Direct link to Setting Up Semantic Mesh Filtering">​</a>

To set up semantic mesh filtering:

1.  In the **Hierarchy**, expand the **XROrigin** and **Camera Offset**, then select the **Main Camera**.
2.  In the **Inspector**, click **Add Component**, then add an `ARSegmentationManager` to the **Main Camera**.
3.  In the **Hierarchy**, select the **MeshManager** `GameObject` that you created during the Meshing setup.
4.  Next, find the **Lightship Meshing Extension**, then check the box next to **Mesh Filtering** to enable it.
5.  Two options will appear: **Enable Allow List** and **Enable Block List**. Choose which lists you would like to use, then click the `+` below each list to add slots to it. Once you have added slots, enter the names of the semantic channels you would like to allow/exclude, one per line. In the following example, the `ground` channel is in an allowlist, so meshing will only capture the ground.

<img src="https://www.nianticspatial.com/docs/assets/images/semantic_filter_allow-d8aabaeaace026ee56beb8a1630684f7.png" width="600" alt="Example usage of a semantic filtering allowlist" />

The allow/block lists will remember your settings and channel lists, even if you disable and re-enable them.

## Recommended Usage<a href="#recommended-usage" class="hash-link" aria-label="Direct link to Recommended Usage" title="Direct link to Recommended Usage">​</a>

Semantic channels apply to a variety of common objects and structures, and there are some that you will usually not want included when creating a mesh. At minimum, we recommend excluding `sky` and `person` using a block list to keep those elements out of your mesh.

<img src="https://www.nianticspatial.com/docs/assets/images/semantic_filter_block-7ad9aa7a65dbf5395c31ea9cd5e22734.png" width="600" alt="Example usage of a semantic filtering blocklist" />

You can also combine allow lists and block lists to capture specific parts of a scene as a mesh. As an example, if you wanted to capture a mesh of a path through a grassy field, you could allow `ground` while blocking `sky` and `grass` to only capture ground areas with no grass on them, resulting in a mesh of the path. For another example, if you wanted to capture a mesh of an interesting building, you could allow `building` while blocking `person`, `ground`, and `sky` to make sure the building is all that is captured.

<img src="https://www.nianticspatial.com/docs/assets/images/semantic_filter_both-b4e56c67d0ae03f278edb742f7b26e71.png" width="600" alt="Example usage of both semantic filtering lists" />

## Script Example<a href="#script-example" class="hash-link" aria-label="Direct link to Script Example" title="Direct link to Script Example">​</a>

This script demonstrates a basic example of how to use mesh filtering in code. It defines an allowlist and makes sure the list is active, then provides a method for turning mesh filtering on and off.

Click to reveal ToggleMeshFiltering.cs

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Niantic.Lightship.AR.Meshing

public class ToggleMeshFiltering : MonoBehaviour
{
    [SerializeField] private LightshipMeshingExtension _meshingExtension;

    // Start is called before the first frame update
    void Start()
    {
      // Define the Allow List
      _meshingExtension.AllowList = new List<string>() {"ground"};
      _meshingExtension.IsFilteringAllowListEnabled = true;
    }

    void ToggleMeshFiltering()
    {
      _meshingExtension.IsMeshFilteringEnabled = !_meshingExtension.IsMeshFilteringEnabled;
    }
}
```

</div>

</div>

</div>

</div>

</div>

</div>
