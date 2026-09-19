---
source: https://www.nianticspatial.com/docs/nsdk/how-to/ar/gaussian_splat/
title: How to Create a Gaussian Splat
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Create a Gaussian Splat of an Area or Object

</div>

The Niantic Spatial Platform SDK offers a Gaussian splat feature that can produce a Gaussian cloud from a recorded sequence.

For this demo, we will create a Gaussian splat from a recorded sequence and export it to a file.

<img src="https://www.nianticspatial.com/docs/assets/images/splat_example-cd815e6343bcc42cb3de062cafd986cd.png" width="800" alt="An example of a rendered Gaussian splat from Niantic Spatial SDK" />

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Unity project with the Niantic Spatial Platform SDK installed. For more information, see [Set up the Niantic SDK for Unity](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-the-niantic-sdk-for-unity).

Additionally, you will need to install the Niantic Spatial SDK **Scan Reconstruction** UPM. Install this package via Unity Package Manager using the same method as the main Niantic Spatial SDK package in the [setup guide](https://www.nianticspatial.com/docs/nsdk/setup/). Scan Reconstruction is not currently supported on Windows.

Finally, you will need a recorded Raw Scan sequence to use as the input for the Gaussian splat processor. See [How to Create Datasets for Playback](https://www.nianticspatial.com/docs/nsdk/how-to/playback/create_playback_dataset/) for instructions to record a Raw Scan sequence.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

**Using Playback sequences with Scan Reconstruction**

Turning an existing Playback sequence into a Gaussian splat is possible with an extra conversion step.

AR Scanning Manager can produce two versions of a scan recording:

1.  **Raw Scan format:** By default, AR Scanning Manager will write frames directly to disk.

- This is the format that Scan Reconstruction accepts.
- The files are saved to the directory at `ScanStore.SavedScan.ScanPath`. Metadata is stored in .pb files.

2.  **Playback format:** Optionally, the recorded frames can be exported to a compressed .tgz archive.

- This is the format that [Playback](https://www.nianticspatial.com/docs/nsdk/features/playback/) and [VPS](https://www.nianticspatial.com/docs/nsdk/features/lightship_vps/) accept.
- The sequence is archived under `ScanStore.SavedScan.ScanPath` in a .tgz. Metadata is stored in a capture.json file.

If you have a Playback recording (a .tgz archive, or an extracted sequence that contains a capture.json) that you wish to use with Scan Reconstruction, the sequence must be converted back into Raw Scan format.

The easiest way to do this is to either use the <a href="https://github.com/nianticspatial/nsdk-samples-csharp/tree/main/NsdkSamples/Assets/Samples/Scanning/Scenes" target="_blank" rel="noopener noreferrer">sample Recording scene</a> or to add on the [How to Create Datasets for Playback](https://www.nianticspatial.com/docs/nsdk/how-to/playback/create_playback_dataset/) components to the below scene. Then, run the scene in [Playback mode](https://www.nianticspatial.com/docs/nsdk/features/playback/) with your Playback sequence set as the **Playback Dataset Path** in XR Plug-in Management → Niantic Lightship SDK settings → Playback. The AR Scanning Manager will read the Playback sequence and record it back into a Raw Scan recording in the process of running the scene.

After the recording is completed (`_arScanningManager.enabled = false`), reconstruction of the `SavedScan` can begin with `ProcessSplat()`.

</div>

</div>

## Add AR Scanning Manager to a Unity Project<a href="#add-ar-scanning-manager-to-a-unity-project" class="hash-link" aria-label="Direct link to Add AR Scanning Manager to a Unity Project" title="Direct link to Add AR Scanning Manager to a Unity Project">​</a>

To produce a Gaussian splat, create an AR Scanning Manager to read the [scan sequence](https://www.nianticspatial.com/docs/nsdk/how-to/playback/create_playback_dataset/) from disk.

1.  Create an empty Game Object in the root of your scene. Name it **Splat Processing**.
2.  Add an **AR Scanning Manager** component to the Splat Processing object.
3.  Enable **Full Resolution**.
4.  Set Recording Framerate to **15 FPS**.
5.  Set Near Depth to **0.02 m** and Far Depth to **10.0 m** (or the maximum distance allowed).
6.  **Disable** the manager component so that it does not start recording when the scene starts.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

**Achieving Scaniverse-level Reconstruction Quality**

The first element in producing a splat with Scaniverse-level quality is to use AR Scanning Manager with the recommended settings. The settings used in this document are important for achieving good quality.

1.  Keep Recording Framerate at 15 FPS.
2.  Always enable Full Resolution.
3.  Set the quality level according to the number of training iterations that you want to run. For example, `Low` quality will only run one training iteration. `Medium` is the equivalent of tapping **Enhance** in Scaniverse once to run a second training iteration. `High` and `VeryHigh` add a third and fourth training iteration.
4.  Set Near Depth to 0.02 m and Far Depth to the maximum distance.

The second element is to follow best practices while taking the scan recording.

1.  Move the camera **slowly and smoothly**, and capture surfaces from **multiple angles**.
2.  If scanning an object, take time to capture the object from all sides.
3.  Set up [scan visualization](https://www.nianticspatial.com/docs/nsdk/how-to/ar/scan_visualization/) in the recording scene to make it easier to keep track of what has been captured.
4.  <a href="https://www.youtube.com/watch?v=ELXLFMjLOx8" target="_blank" rel="noopener noreferrer">Watch this video</a> for advice on how to capture a quality scan.

</div>

</div>

## Create and Run a GaussianSplatProcessor<a href="#create-and-run-a-gaussiansplatprocessor" class="hash-link" aria-label="Direct link to Create and Run a GaussianSplatProcessor" title="Direct link to Create and Run a GaussianSplatProcessor">​</a>

Next, create a script to handle the splat processing.

1.  Add a **New script** component to the Splat Processing game object. Name it **SplatProcessing.cs**.
2.  Add the following code to find the first recorded sequence and reconstruct it into a Gaussian cloud.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System;
using NianticSpatial.NSDK.AR.Scanning;
using NianticSpatial.NSDK.Scanning;
using NianticSpatial.NSDK.ScanReconstruction;
using UnityEngine;
using UnityEngine.UI;

public class SplatProcessing : MonoBehaviour
{
    [SerializeField]
    private ARScanningManager _arScanningManager;

    [SerializeField]
    private Button _startButton;

    [SerializeField]
    private Slider _progressSlider;

    private void Start()
    {
        _startButton.onClick.AddListener(ProcessSplat);
    }

    private async void ProcessSplat()
    {
        // Find the first scan saved at the default recording path
        // (To select a specific scan instead, search for its ScanId in the list)
        ScanStore scanStore = _arScanningManager.GetScanStore();
        ScanStore.SavedScan savedScan = scanStore.GetSavedScans()[0];

        // Select the processing quality for the pipeline
        Quality quality = Quality.Medium;
        GaussianSplatProcessor processor = new GaussianSplatProcessor(savedScan);

        try
        {
            Debug.Log("Processing splat...");
            GaussianSplat result = await processor.ProcessSplat(
                (resp) => { _progressSlider.value = resp.Progress; },
                default, quality, Format.SPZ
                //, "/path/to/export/"  // Uncomment this line to provide a custom export path
                );
            Debug.Log("Splat processing complete! " +
                "Num points: " + result.NumPoints +
                ", spherical harmonics degree: " + result.ShDegree +
                ", Positions: " + result.Positions.Length +
                ", Normals: " + result.Alphas.Length +
                ", Colors: " + result.Colors.Length);
        }
        catch (Exception e)
        {
            Debug.LogError("Splat processing failed: " + e.Message);
        }
    }
}
```

</div>

</div>

To process a specific recorded sequence instead of the first one, search the list returned by `GetSavedScans` for the desired ScanId.

<img src="https://www.nianticspatial.com/docs/assets/images/splat_processing_initial-15a9ec707af225f6eaf864ca95557fee.png" width="460" alt="The Splat Processing inspector with the disabled AR Scanning Manager and the new script" />

## Add the UI<a href="#add-the-ui" class="hash-link" aria-label="Direct link to Add the UI" title="Direct link to Add the UI">​</a>

Add a start button and a progress bar to the scene.

1.  Find your **Canvas** game object under the root object in the Inspector, or create one if it does not exist (Right-click → UI → Canvas).
2.  Under the Canvas, add a Slider (Right-click → UI → Slider) named **Progress Slider** and a Legacy Button (Right-click → UI → Legacy → Button) named **Start Button**.
3.  Adjust the position and size of the two UI elements to be visible in the scene.

<div>

<img src="https://www.nianticspatial.com/docs/assets/images/splat_hierarchy-9cdd9974b2f355b2fdd26d50333f2a1b.png" width="300" alt="The project hierarchy with Start Button and Progress Slider child elements under the Canvas element" />

</div>

<div>

<img src="https://www.nianticspatial.com/docs/assets/images/ui_layout-5388374ee4b408707ec644b9adfea1fc.png" width="450" alt="A start button and progress bar in a Unity game preview window" />

</div>

## Complete the Scene<a href="#complete-the-scene" class="hash-link" aria-label="Direct link to Complete the Scene" title="Direct link to Complete the Scene">​</a>

Assign the serialized fields in the **Splat Processing** component with the AR Scanning Manager, button and slider.

<img src="https://www.nianticspatial.com/docs/assets/images/splat_processing-47cbff46024ee0403f2eec556b17a467.png" width="460" alt="The Splat Processing inspector with the serialized fields assigned to the UI elements that we created and the disabled AR Scanning Manager" />

## Export to a File<a href="#export-to-a-file" class="hash-link" aria-label="Direct link to Export to a File" title="Direct link to Export to a File">​</a>

Splats can export to Niantic Spatial's open source, highly-optimized <a href="https://scaniverse.com/spz" target="_blank" rel="noopener noreferrer">SPZ format</a> and to a splat-augmented PLY format, similar to Scaniverse.

To export the Gaussian splat to a file, provide the desired format and output path to `ProcessSplat`. Calling `ProcessSplat` without an export format will return the raw data arrays without exporting to disk.

If `exportFormat` is provided without an `exportPath`, the file is saved to the `SavedScan.ScanPath` directory. [See this document for the default scan recording paths](https://www.nianticspatial.com/docs/nsdk/how-to/playback/create_playback_dataset/#file-locations). For example, running this in the Unity Editor on a Mac will save the file under `/Users/{Username}/Library/Application Support/{Company Name}/{Project Name}/scankit/{Scan ID}/`. Setting the **Scan Path** field of the AR Scanning Manager component will override the default scan recording location.

## Try It Out<a href="#try-it-out" class="hash-link" aria-label="Direct link to Try It Out" title="Direct link to Try It Out">​</a>

Run the scene and tap the start button to start the splat processing. Watch the progress bar increase, and check the console logs for information about the result. Look for your SPZ file at the [default recording path](https://www.nianticspatial.com/docs/nsdk/how-to/playback/create_playback_dataset/#file-locations) for your platform, and try <a href="https://scaniverse.8thwall.app/model-viewer/" target="_blank" rel="noopener noreferrer">viewing it on the web</a>.

<img src="https://www.nianticspatial.com/docs/assets/images/successful_console_logs-b00f619af7816661c4196f9ca7135bd3.png" width="650" alt="Unity console showing successful splat processing complete logs" />

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

Using smooth camera motion and capturing an area or object from many angles will result in a better Gaussian splat result.

</div>

</div>

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

The higher the **quality** setting, the longer the Gaussian splat will take to process.

</div>

</div>

## Rendering a splat<a href="#rendering-a-splat" class="hash-link" aria-label="Direct link to Rendering a splat" title="Direct link to Rendering a splat">​</a>

While Niantic Spatial SDK does not provide a rendering solution for Gaussian splats in Unity, an open source solution is available. Aras Pranckevičius's <a href="https://github.com/aras-p/UnityGaussianSplatting" target="_blank" rel="noopener noreferrer">Unity Gaussian Splatting</a> project is a Unity plug-in that renders SPZ and PLY files.

Alternatively, to view your splat in a web browser, <a href="https://scaniverse.8thwall.app/model-viewer/" target="_blank" rel="noopener noreferrer">drop your SPZ or PLY file onto this webpage</a>. Or, <a href="https://www.youtube.com/watch?v=xE1xi9zcOwo" target="_blank" rel="noopener noreferrer">upload your SPZ file to a Niantic Studio project</a>, and then drag it into the scene view.

Happy splatting!

## Troubleshooting<a href="#troubleshooting" class="hash-link" aria-label="Direct link to Troubleshooting" title="Direct link to Troubleshooting">​</a>

### The splat fails to export to a file<a href="#the-splat-fails-to-export-to-a-file" class="hash-link" aria-label="Direct link to The splat fails to export to a file" title="Direct link to The splat fails to export to a file">​</a>

Splats can fail to export if the scan recording directory name has changed. `SavedScan` directories are stored by their ID and created with 12-character alphanumeric names. Renaming the directory before running reconstruction can cause the export task to fail.

To resolve this issue, avoid renaming the directory.

</div>

</div>
