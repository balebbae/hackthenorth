---
source: https://www.nianticspatial.com/docs/nsdk/how-to/ar/textured_mesh/
title: How to Create a Textured Mesh
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Scan and Display a Textured Mesh of an Area or Object

</div>

The Niantic Spatial SDK offers a textured meshing feature that can produce a mesh and texture from a recorded sequence. While [live meshing](https://www.nianticspatial.com/docs/nsdk/features/meshing/) is useful for capturing real-time information about the surroundings for the application to respond to, the textured meshing feature lets you save a mesh for offline use and display it with accurate color texturing. Unlike live meshing, textured meshes are generated as a post-processing step after a recording is completed. Photogrammetric textured meshing is supported on all Niantic Spatial SDK-compatible iPhone and Android devices, but scanning with lidar will produce the best mesh quality.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/demo_video_30fps-ba63eb1eab108f1017b5b9fd72738ed9.gif" width="400" alt="Processing and viewing a textured mesh created with NSDK" />

</div>

For this demo, we will record an area, process it into a textured mesh, and display it in AR.

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Unity project with the Niantic Spatial SDK installed and a basic AR scene to get started. For more information, see [Set up the Niantic SDK for Unity](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-the-niantic-sdk-for-unity) and [Set up a basic AR scene](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-a-basic-ar-scene).

Additionally, you will need to install the Niantic Spatial SDK **Scan Reconstruction** UPM. Install this package via Unity Package Manager using the same method as the main Niantic Spatial SDK package in the [setup guide](https://www.nianticspatial.com/docs/nsdk/setup/). Scan Reconstruction is not currently supported on Windows.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

**Using Playback sequences with Scan Reconstruction**

Turning an existing Playback sequence into a textured mesh is possible with a slight change in project setup.

AR Scanning Manager can produce two versions of a scan recording:

1.  **Raw Scan format:** By default, AR Scanning Manager will write frames directly to disk.

- This is the format that Scan Reconstruction accepts.
- The files are saved to the directory at `ScanStore.SavedScan.ScanPath`. Metadata is stored in .pb files.

2.  **Playback format:** Optionally, the recorded frames can be exported to a compressed .tgz archive.

- This is the format that [Playback](https://www.nianticspatial.com/docs/nsdk/features/playback/) and [VPS](https://www.nianticspatial.com/docs/nsdk/features/lightship_vps/) accept.
- The sequence is archived under `ScanStore.SavedScan.ScanPath` in a .tgz. Metadata is stored in a capture.json file.

If you have a Playback recording (a .tgz archive, or an extracted sequence that contains a capture.json) that you wish to use with Scan Reconstruction, the sequence must be converted back into Raw Scan format.

The easiest way to do this is to complete this how-to walkthrough in [Playback mode](https://www.nianticspatial.com/docs/nsdk/features/playback/) instead of using live frame data, with your Playback sequence set as the **Playback Dataset Path** in XR Plug-in Management → NSDK settings → Playback. The AR Scanning Manager will read the Playback sequence and record it back into a Raw Scan recording in the process of running the below scene.

</div>

</div>

## Adding AR Scanning Manager and AR Occlusion Manager to a Unity Project<a href="#adding-ar-scanning-manager-and-ar-occlusion-manager-to-a-unity-project" class="hash-link" aria-label="Direct link to Adding AR Scanning Manager and AR Occlusion Manager to a Unity Project" title="Direct link to Adding AR Scanning Manager and AR Occlusion Manager to a Unity Project">​</a>

To produce a textured mesh, you first need to record a dataset. The AR Scanning Manager component will take a recording and produce a new dataset as a `SavedScan` object that you will use in the next step. `SavedScan` points to camera and depth frames [saved to disk in Raw Scan format](https://www.nianticspatial.com/docs/nsdk/how-to/playback/create_playback_dataset/#recording-data), and this is what Scan Reconstruction processes into a textured mesh.

1.  Create an empty GameObject in the root of your scene. Name it **Scanning**.
2.  Add an **AR Scanning Manager** component to the Scanning object.
3.  Enable **Use Estimated Depth**. (If your device has a lidar sensor, this option can be left unchecked.)
4.  Enable **Full Resolution**.
5.  Set Recording Framerate to **15 FPS**.
6.  Set Near Depth to **0.02 m** and Far Depth to **5.0 m** (refer to the below note for suggested ranges for small or medium objects).
7.  **Disable** the manager component so that it does not start recording when the scene starts.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

**Achieving Scaniverse-level Reconstruction Quality**

The first element in producing a reconstruction with Scaniverse-level quality is to use AR Scanning Manager with the recommended settings. The settings used in this document are important for achieving good quality.

1.  Keep Recording Framerate at 15 FPS.
2.  Always enable Full Resolution.
3.  In the reconstruction script, set mesh and texture qualities to `VeryHigh` to perform reconstruction with Scaniverse quality.
4.  An appropriately-constrained depth range focuses processing power and detail where it is most needed. The following is a guide for selecting near & far depth ranges according to the scan area:
    - **Small object:** 0.02 m - 0.8 m
    - **Medium object:** 0.02 m - 2.5 m
    - **Large object or area:** 0.02 m - 5 m

The second element is to follow best practices while taking the scan recording.

1.  Move the camera **slowly and smoothly**, and capture surfaces from **multiple angles**.
2.  If scanning an object, take time to capture the object from all sides.
3.  Set up [scan visualization](https://www.nianticspatial.com/docs/nsdk/how-to/ar/scan_visualization/) in the recording scene to make it easier to keep track of what has been captured.
4.  <a href="https://www.youtube.com/watch?v=ELXLFMjLOx8" target="_blank" rel="noopener noreferrer">Watch this video</a> for advice on how to capture a quality scan.

The third element is depth source. Lidar depth with Area Mode will generally produce the best mesh results. When lidar is not available, Detail Mode is recommended.

</div>

</div>

Then, add an AR Occlusion Manager component to generate depth buffers.

1.  In the hierarchy, navigate to XR Origin → Camera Offset → **Main Camera**.
2.  Add an **AR Occlusion Manager** component to the Main Camera object.
3.  Set Occlusion Preference Mode to **No Occlusion**.
4.  Add a **Nsdk Occlusion Extension** component to **Main Camera** and set its **Target Frame Rate** to 15 FPS to prevent multidepth from capping the recording FPS to its default rate of 10 FPS.

<img src="https://www.nianticspatial.com/docs/assets/images/occlusion_manager-70124fc7172e5484530ac139217e8f0a.png" width="400" alt="Add an AR Occlusion Manager to the Main Camera in the Inspector" />

## Handle Scanning with a Script<a href="#handle-scanning-with-a-script" class="hash-link" aria-label="Direct link to Handle Scanning with a Script" title="Direct link to Handle Scanning with a Script">​</a>

Next, create a script to handle scanning and reconstruction tasks.

1.  Add a new script Component to the **Scanning** GameObject. Name it **ScanDemo.cs**.
2.  Add code to accept references to the AR Scanning Manager and buttons to start and stop the scanning. The script will also hold a reference to the `ScanStore`, a library of our recorded datasets.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
[SerializeField]
private ARScanningManager _arScanningManager;

[SerializeField]
private Button _startScanningButton;

[SerializeField]
private Button _stopScanningButton;

private GameObject _renderedObject;
private ScanStore _scanStore;
private ScanStore.SavedScan _savedScan;

private void Start()
{
    _scanStore = _arScanningManager.GetScanStore();
    _startScanningButton.onClick.AddListener(StartScanning);
    _stopScanningButton.onClick.AddListener(StopScanning);
}

public void StartScanning()
{
    _stopScanningButton.gameObject.SetActive(true);
    _startScanningButton.gameObject.SetActive(false);
    _arScanningManager.enabled = true;
    _renderedObject?.SetActive(false);
}
```

</div>

</div>

## Create a TexturedMeshProcessor<a href="#create-a-texturedmeshprocessor" class="hash-link" aria-label="Direct link to Create a TexturedMeshProcessor" title="Direct link to Create a TexturedMeshProcessor">​</a>

ScanDemo will use a TexturedMeshProcessor to reconstruct the sequence that it just scanned.

1.  In **ScanDemo.cs**, add references to a prefab, a parent GameObject, a slider to show progress, and a text box to display error status.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
[SerializeField]
private GameObject _meshPreviewPrefab;

[SerializeField]
private GameObject _meshPreviewRoot;

[SerializeField]
private Slider _progressSlider;

[SerializeField]
private Text _errorText;
```

</div>

</div>

2.  Add a function to stop scanning, save the scan to disk, and start the mesh reconstruction process with the scan.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
public async void StopScanning()
{
    _stopScanningButton.gameObject.SetActive(false);
    await _arScanningManager.SaveScan();
    _arScanningManager.enabled = false;
    string scanID = _arScanningManager.GetCurrentScanId();
    _savedScan = _scanStore.GetSavedScans().First(s => s.ScanId == scanID);
    StartReconstruction(_savedScan);
}
```

</div>

</div>

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

To process a specific recorded sequence instead of the first one, search the list returned by `GetSavedScans` for the desired ScanId.

</div>

</div>

3.  After recording a `SavedScan` dataset, pass it to a **TexturedMeshProcessor** to start the textured meshing process and wait for it to complete. Optionally export the 3D reconstruction to an OBJ or PLY file.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
private async void StartReconstruction(ScanStore.SavedScan savedScan)
{
    ReconstructionMode mode = ReconstructionMode.Detail;
    Quality meshQuality = Quality.VeryHigh;
    Quality textureQuality = Quality.VeryHigh;
    TexturedMeshProcessor reconstructor = new TexturedMeshProcessor(savedScan);
    try
    {
        TexturedMesh result = await reconstructor.Reconstruct(mode, meshQuality, textureQuality,
            (resp) => { _progressSlider.value = resp.Progress; }, default
                //, Format.OBJ          // Uncomment this line if you wish to export to a file.
                //, "/path/to/export/"  // Uncomment this line to provide a custom export path
                );
```

</div>

</div>

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

If your mobile device supports **lidar** and you plan to capture large areas, you can use `Area` mode instead of `Detail` mode. This will result in better quality than meshing a large area with only RGB camera data. Ensure that **Prefer LiDAR if Available** is enabled in Niantic SDK Settings under XR Plug-in Management. See [Supporting lidar and non-lidar use cases](https://www.nianticspatial.com/docs/nsdk/how-to/ar/textured_mesh/#supporting-lidar-and-non-lidar-use-cases) for more details.

</div>

</div>

4.  Add code to receive the result. Apply the mesh and texture to a prefab for display in the AR view. Delete the recording data from disk to save space, or don't delete yet if you intend to export to a file. If there was a failure, display the error. Finally, reenable the start button to create another scan.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
        if (_renderedObject != null)
        {
            Destroy(_renderedObject.GetComponent<MeshFilter>().sharedMesh);
            Destroy(_renderedObject.GetComponent<Renderer>().material.mainTexture);
            Destroy(_renderedObject);
        }

        _renderedObject = Instantiate(_meshPreviewPrefab, _meshPreviewRoot.transform);
        _renderedObject.transform.localPosition = result.Position;
        _renderedObject.GetComponent<MeshFilter>().sharedMesh = result.Mesh;
        _renderedObject.GetComponent<Renderer>().material.mainTexture = result.Texture;
        _errorText.text = "";
        // _scanStore.DeleteScan(_savedScan);  // Uncomment this line to delete the raw data
    }
    catch (Exception e)
    {
        _errorText.text = e.Message;
    }

    _startScanningButton.gameObject.SetActive(true);
}
```

</div>

</div>

## Create a Mesh Preview Prefab<a href="#create-a-mesh-preview-prefab" class="hash-link" aria-label="Direct link to Create a Mesh Preview Prefab" title="Direct link to Create a Mesh Preview Prefab">​</a>

Next, you will create a prefab with the components necessary to render a generic mesh. The Niantic Spatial SDK already returns Unity-native types for the mesh, texture, and position, so the only thing you need to do is display it with Unity's built-in **Mesh Filter** and **Mesh Renderer** tools.

1.  In your project's Assets folder, create a new material (Right-click → Create → Material). Name it **ScannedObjectUnlit**.
2.  Change its shader to **Particles/Standard Unlit**.

<img src="https://www.nianticspatial.com/docs/assets/images/material-de9922f495d7bfafcf7f1fd9b1c98ebb.png" width="400" alt="Create an unlit material" />

3.  Anywhere under the canvas, create a **Cube** (Right-click → 3D Object → Cube). Optionally remove its Box Collider component if you don't want physics collisions.
4.  Under the cube's Mesh Renderer, set the material to the ScannedObjectUnlit material that you just created. Save the Cube as a <a href="https://docs.unity3d.com/6000.1/Documentation/Manual/CreatingPrefabs.html" target="_blank" rel="noopener noreferrer">prefab</a> in your project's Assets named **Preview**. This is the object that will turn the SDK's arrays of vertices, triangles and texture coordinates into rendered graphics.

<img src="https://www.nianticspatial.com/docs/assets/images/prefab-96a34c4e84e4d1b568a4b3437227b58f.png" width="400" alt="Create a prefab with mesh rendering components" />

5.  Delete the Cube from step 3 from the hierarchy—we only needed it to create the prefab.

## Complete the UI<a href="#complete-the-ui" class="hash-link" aria-label="Direct link to Complete the UI" title="Direct link to Complete the UI">​</a>

To finish off the scene, add several UI objects to your scene.

1.  Find your **Canvas** GameObject under the root object in the Inspector, or create one if it does not exist (Right-click → UI → Canvas).
2.  Under the canvas, add a Legacy Text named **Error String** (Right-click → UI → Legacy → Text).
3.  Add a Slider named **Progress Bar** (Right-click → UI → Slider)
4.  Add two Legacy Buttons named **Start Scan Button** and **Stop Scan Button**, respectively (Right-click → UI → Legacy → Button).
5.  Update the buttons' text labels to match their names.
6.  In the inspector, **disable** Stop Scan Button so that it's hidden until scanning starts.
7.  In the scene editor, position the buttons and sliders so that they are visible in the scene.

Add an empty GameObject under Camera Offset. Name it **MeshRoot** and ensure that it has default (identity) transform values. The mesh prefab will be created as a child of this object.

<img src="https://www.nianticspatial.com/docs/assets/images/hierarchy_final-b860cc5029e917ce61e41568b5095b4e.png" width="400" alt="What the final scene hierarchy should look like" />

Tie it all together by assigning the serialized fields in the **Scanning** object with the UI elements and prefab objects that you created.

<img src="https://www.nianticspatial.com/docs/assets/images/scanning_object_final-689692a079bdfa1d5e35004227dc00a2.png" width="400" alt="The final scanning object should have all serialized fields assigned" />

## Export to a File<a href="#export-to-a-file" class="hash-link" aria-label="Direct link to Export to a File" title="Direct link to Export to a File">​</a>

Textured meshes can export to OBJ and PLY formats. OBJ exports are archived with texture (JPG) and material (MTL) files.

To export the 3D reconstruction to a file, add the desired format and output path to the `Reconstruct` call. For example, to export to an OBJ, `await reconstructor.Reconstruct(mode, meshQuality, textureQuality, (resp) => { _progressSlider.value = resp.Progress; }, default, Format.OBJ, "/your/path/")`.

If `exportFormat` is provided without an `exportPath`, the file is saved to the scan recording directory. [See this document for the default scan recording paths](https://www.nianticspatial.com/docs/nsdk/how-to/playback/create_playback_dataset/#file-locations). For example, running this in the Unity Editor on a Mac will save the file under `/Users/{Username}/Library/Application Support/{Company Name}/{Project Name}/scankit/{Scan ID}/` by default. Setting the **Scan Path** field of the AR Scanning Manager component will override the default scan recording location.

## Try It Out<a href="#try-it-out" class="hash-link" aria-label="Direct link to Try It Out" title="Direct link to Try It Out">​</a>

Run the scene and tap the start button to start recording. Use smooth camera motion to capture the area and walk around to capture from all angles.

When you're done scanning, it's time for the textured mesh to process. Tap the stop button and watch the progress meter fill. Finally, you should see the textured mesh appear in the camera view as an AR overlay of the area you scanned.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

The mesh position is only valid for the current session. If tracking restarts with a different origin, the real-world position of the mesh will be wrong. To consistently place objects across AR sessions and devices, consider using [VPS](https://www.nianticspatial.com/docs/nsdk/features/lightship_vps/) or [Device Mapping](https://www.nianticspatial.com/docs/nsdk/features/device_mapping/).

</div>

</div>

<img src="https://www.nianticspatial.com/docs/assets/images/textured_mesh_example-6ffda98241dc60ecbc76ca2ba335be3c.png" width="400" alt="Example of a textured mesh scanned and rendered in AR" />

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

The higher the **mesh quality**, the longer the mesh will take to process.

</div>

</div>

Click to reveal the full demo script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System;
using System.Linq;
using NianticSpatial.NSDK.AR.Scanning;
using NianticSpatial.NSDK.Scanning;
using NianticSpatial.NSDK.ScanReconstruction;
using UnityEngine;
using UnityEngine.UI;

public class ScanDemo : MonoBehaviour
{
    [SerializeField]
    private ARScanningManager _arScanningManager;

    [SerializeField]
    private Button _startScanningButton;

    [SerializeField]
    private Button _stopScanningButton;

    [SerializeField]
    private GameObject _meshPreviewPrefab;

    [SerializeField]
    private GameObject _meshPreviewRoot;

    [SerializeField]
    private Slider _progressSlider;

    [SerializeField]
    private Text _errorText;

    private GameObject _renderedObject;
    private ScanStore _scanStore;
    private ScanStore.SavedScan _savedScan;

    private void Start()
    {
        _scanStore = _arScanningManager.GetScanStore();
        _startScanningButton.onClick.AddListener(StartScanning);
        _stopScanningButton.onClick.AddListener(StopScanning);
    }

    public void StartScanning()
    {
        _stopScanningButton.gameObject.SetActive(true);
        _startScanningButton.gameObject.SetActive(false);
        _arScanningManager.enabled = true;
        _renderedObject?.SetActive(false);
    }

    public async void StopScanning()
    {
        _stopScanningButton.gameObject.SetActive(false);
        await _arScanningManager.SaveScan();
        _arScanningManager.enabled = false;
        string scanID = _arScanningManager.GetCurrentScanId();
        _savedScan = _scanStore.GetSavedScans().First(s => s.ScanId == scanID);
        StartReconstruction(_savedScan);
    }

    private async void StartReconstruction(ScanStore.SavedScan savedScan)
    {
        ReconstructionMode mode = ReconstructionMode.Detail;
        Quality meshQuality = Quality.VeryHigh;
        Quality textureQuality = Quality.VeryHigh;
        TexturedMeshProcessor reconstructor = new TexturedMeshProcessor(savedScan);
        try
        {
            TexturedMesh result = await reconstructor.Reconstruct(mode, meshQuality, textureQuality,
                (resp) => { _progressSlider.value = resp.Progress; }, default
                //, Format.OBJ          // Uncomment this line if you wish to export to a file.
                //, "/path/to/export/"  // Uncomment this line to provide a custom export path
                );
            if (_renderedObject != null)
            {
                Destroy(_renderedObject.GetComponent<MeshFilter>().sharedMesh);
                Destroy(_renderedObject.GetComponent<Renderer>().material.mainTexture);
                Destroy(_renderedObject);
            }

            _renderedObject = Instantiate(_meshPreviewPrefab, _meshPreviewRoot.transform);
            _renderedObject.transform.localPosition = result.Position;
            _renderedObject.GetComponent<MeshFilter>().sharedMesh = result.Mesh;
            _renderedObject.GetComponent<Renderer>().material.mainTexture = result.Texture;
            _errorText.text = "";
            // _scanStore.DeleteScan(_savedScan);  // Uncomment this line to delete the raw data
        }
        catch (Exception e)
        {
            _errorText.text = e.Message;
        }

        _startScanningButton.gameObject.SetActive(true);
    }
}
```

</div>

</div>

</div>

</div>

## Troubleshooting<a href="#troubleshooting" class="hash-link" aria-label="Direct link to Troubleshooting" title="Direct link to Troubleshooting">​</a>

### Supporting lidar and non-lidar use cases:<a href="#supporting-lidar-and-non-lidar-use-cases" class="hash-link" aria-label="Direct link to Supporting lidar and non-lidar use cases:" title="Direct link to Supporting lidar and non-lidar use cases:">​</a>

Using lidar depth data will result in higher mesh quality, but not all devices have lidar support. Because of this, depending on your deployment scheme, it may be necessary to configure your scene to run on any device.

If the device has a lidar sensor:

1.  Ensure that **Prefer LiDAR if Available** is enabled in Niantic SDK Settings under XR Plug-in Management.
2.  In `StartReconstruction`, assign `ReconstructionMode mode = ReconstructionMode.Area;` if you will scan large areas; otherwise, use `ReconstructionMode.Detail`.
3.  In the AR Scanning Manager component, disable **Record Estimated Depth**.

If the device does not have lidar, or to configure the scene to run on any device without using lidar:

1.  In Niantic SDK Settings under XR Plug-in Management, ensure that **Prefer LiDAR if Available** is disabled and **Depth** is enabled.
2.  In `StartReconstruction`, assign `ReconstructionMode mode = ReconstructionMode.Detail;`.
3.  In the AR Scanning Manager component, enable **Record Estimated Depth**.
4.  Ensure that an **AR Occlusion Manager** is present on the Main Camera.

### The scene crashes when I run it:<a href="#the-scene-crashes-when-i-run-it" class="hash-link" aria-label="Direct link to The scene crashes when I run it:" title="Direct link to The scene crashes when I run it:">​</a>

There may be a lidar configuration mismatch between your device and scene. See [Supporting lidar and non-lidar use cases](https://www.nianticspatial.com/docs/nsdk/how-to/ar/textured_mesh/#supporting-lidar-and-non-lidar-use-cases) to match the scene configuration to your target device.

Ensure that **Scanning** is enabled in Niantic SDK Settings under XR Plug-in Management.

### The scan produces a low-poly or inaccurate mesh:<a href="#the-scan-produces-a-low-poly-or-inaccurate-mesh" class="hash-link" aria-label="Direct link to The scan produces a low-poly or inaccurate mesh:" title="Direct link to The scan produces a low-poly or inaccurate mesh:">​</a>

If possible, perform the scan with a lidar device and configure the scene for lidar capture ([see above](https://www.nianticspatial.com/docs/nsdk/how-to/ar/textured_mesh/#supporting-lidar-and-non-lidar-use-cases)). Scan with as much light on the subject as possible. Use smooth and slow camera motions when scanning. Take time to capture the subject from all angles.

### The mesh fails to export to a file<a href="#the-mesh-fails-to-export-to-a-file" class="hash-link" aria-label="Direct link to The mesh fails to export to a file" title="Direct link to The mesh fails to export to a file">​</a>

Textured meshes can fail to export if the scan recording directory name has changed. `SavedScan` directories are stored by their ID and created with 12-character alphanumeric names. Renaming the directory before running reconstruction can cause the export task to fail.

To resolve this issue, avoid renaming the directory.

### Processing fails with "Not enough points for triangulation"<a href="#processing-fails-with-not-enough-points-for-triangulation" class="hash-link" aria-label="Direct link to Processing fails with &quot;Not enough points for triangulation&quot;" title="Direct link to Processing fails with &quot;Not enough points for triangulation&quot;">​</a>

This error can occur when a scan is either too short (not enough frames covering the captured area from multiple angles) or too long (the frames that are selected for processing do not have enough overlap with each other).

If this happens during a short scan, take enough time to slowly capture the surfaces from multiple angles.

If this happens during a long scan, consider focusing on a smaller area for each scan to allow for more frames per surface.

### Processing fails with "PoseRefiner failed"<a href="#processing-fails-with-poserefiner-failed" class="hash-link" aria-label="Direct link to Processing fails with &quot;PoseRefiner failed&quot;" title="Direct link to Processing fails with &quot;PoseRefiner failed&quot;">​</a>

This error can occur when a scan is too short or too sparse.

To resolve this issue, take time to slowly capture the area from multiple angles, and use the recommended settings from this walkthrough.

</div>

</div>
