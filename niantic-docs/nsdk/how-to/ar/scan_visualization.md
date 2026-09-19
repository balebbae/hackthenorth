---
source: https://www.nianticspatial.com/docs/nsdk/how-to/ar/scan_visualization/
title: How to enable scan visualization
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to enable scan visualization in AR

</div>

Scan visualization gives users real-time feedback while they scan. Areas that have been sufficiently captured appear in full color, while incomplete areas remain striped. This makes it easier to understand scan coverage while recording.

This guide is for developers who are building custom scan capture flows in Unity, Swift, or Kotlin and want to add that feedback to their app. It shows how to enable raycast visualization, connect it to the scanning session, and render the striped overlay during capture so users can spot gaps before saving a scan.

**Raycast visualization** is the scan visualization mode that draws this striped overlay from the scanning session's raycast data. It is useful during development because it helps you confirm that scan coverage is complete, spot gaps before saving a scan, and verify that your capture UI is showing the visualization at the right time.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/scanning_stripes_example-730867349edf10322898e3bed014f11c.gif" style="width:40.0%" alt="Example of raycast visualization in an AR scene" />

</div>

**Figure:** Raycast visualization overlays stripes on incomplete areas of a scan.

In Unity, scan visualization is enabled by turning on **raycast visualization** in [AR Scanning Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager/) and rendering the result with the `Unlit/NsdkScanningStripes` shader. At a high level, a Unity implementation needs to:

- enable raycast visualization on `AR Scanning Manager`
- provide depth data for scanning
- render the raycast visualization textures with a material
- show that overlay only while scan visualization is active

The rest of this Unity walkthrough shows one runnable implementation of that flow using the Recording scene from <a href="https://github.com/nianticspatial/nsdk-samples-csharp" target="_blank" rel="noopener noreferrer">nsdk-samples-csharp</a>. In that sample-based implementation:

- the Recording scene already provides the capture lifecycle and UI
- `RecordingDemo.StartScanning()` and `RecordingDemo.StopScanning()` continue to control when scanning starts and stops
- the only new Unity-specific logic added in this guide is the visualization renderer

To enable scan visualization in Unity:

1.  [Prepare your Unity project](#unity-prepare-your-project)
2.  [Enable raycast visualization in AR Scanning Manager](#unity-enable-raycast-visualization-in-ar-scanning-manager)
3.  [Add a visualization renderer to your AR screen](#unity-add-a-visualization-renderer-to-your-ar-screen)
4.  [Start and stop the visualization with capture](#unity-start-and-stop-the-visualization-with-capture)
5.  [Update the visualization while AR frames arrive](#unity-update-the-visualization-while-ar-frames-arrive)

------------------------------------------------------------------------

### Prepare your Unity project<a href="#unity-prepare-your-project" class="hash-link" aria-label="Direct link to Prepare your Unity project" title="Direct link to Prepare your Unity project">​</a>

This section shows how to start from the existing Unity Recording sample so you can build a runnable scan-visualization example on top of a working AR scene rather than setting up the full flow from scratch.

1.  Clone <a href="https://github.com/nianticspatial/nsdk-samples-csharp" target="_blank" rel="noopener noreferrer">nsdk-samples-csharp</a>:

    <div class="language-bash codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` bash
    git clone https://github.com/nianticspatial/nsdk-samples-csharp.git
    ```

    </div>

    </div>

2.  Open the Unity project: in Unity Hub, **Add project from disk** and select the **`NsdkSamples`** folder inside your clone (same layout as Kotlin/Swift samples).

3.  Open `NsdkSamples/Assets/Samples/Scanning/Scenes/Recording.unity`.

4.  Build and run the sample on your device.

This walkthrough assumes:

- the Recording sample builds and runs on your device
- the scene already includes a basic AR setup
- you are working in the current URP-configured sample project
- `RecordingDemo` continues to own scan start and stop in the following runnable example

For general setup steps, see [Set up the Niantic SDK for Unity](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-the-niantic-sdk-for-unity) and [Set up a basic AR scene](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-a-basic-ar-scene).

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

This runnable example uses a URP-compatible render pass, so you do not need to change the sample project's render pipeline settings.

</div>

</div>

------------------------------------------------------------------------

### Enable raycast visualization in AR Scanning Manager<a href="#unity-enable-raycast-visualization-in-ar-scanning-manager" class="hash-link" aria-label="Direct link to Enable raycast visualization in AR Scanning Manager" title="Direct link to Enable raycast visualization in AR Scanning Manager">​</a>

This section shows how to configure the scanning component so it produces the raycast visualization data needed for the striped overlay. In your own Unity app, enable raycast visualization on [AR Scanning Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager/) and make sure scanning has access to depth data.

In a Unity app that uses NSDK scanning:

1.  Select a GameObject that has `AR Scanning Manager`, or add [AR Scanning Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager/) to the GameObject that owns your scan flow. In the following runnable code, see step ⅰ for one implementation.
2.  Enable **Enable Raycast Visualization** so the scanning system generates the raycast visualization textures. In the following runnable code, see step ⅱ for one implementation.
3.  Enable **Record Estimated Depth** if your app needs NSDK-generated depth. In the following runnable code, see step ⅲ for one implementation.
4.  If your device has LiDAR, you can leave **Record Estimated Depth** disabled and instead provide depth through an **AR Occlusion Manager** on your camera setup. In the following runnable code, see step ⅲ for one implementation.
5.  Keep the component's enabled state aligned with your app's scan lifecycle so visualization is only active while scanning is active. In the following runnable code, see step ⅳ for one implementation.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

If your device has LiDAR, you can leave **Record Estimated Depth** disabled. Ensure that **Prefer LiDAR if Available** is enabled in Niantic SDK settings under **XR Plug-in Management**, and add an **AR Occlusion Manager** to the camera object used by your XR Origin so LiDAR depth is available to scanning.

</div>

</div>

Expand to reveal a minimal Unity example for scan-visualization setup

<div>

<div class="collapsibleContent_i85q">

This example keeps the Unity sample changes to the minimum required for this step. It gives you a runnable Recording-scene baseline that is configured to produce raycast visualization data before any rendering code is added.

Use `NsdkSamples/Assets/Samples/Scanning/Scenes/Recording.unity` from <a href="https://github.com/nianticspatial/nsdk-samples-csharp" target="_blank" rel="noopener noreferrer">nsdk-samples-csharp</a> as the runnable baseline for this example.

- ⅰ. In the Recording scene, select the top-level **AR Session** GameObject, which already has [AR Scanning Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager/) attached.
- ⅱ. Enable **Enable Raycast Visualization**.
- ⅲ. Enable **Record Estimated Depth**, or leave it disabled if your device has LiDAR and you have added an **AR Occlusion Manager** to the camera object used by your XR Origin.
- ⅳ. Leave `AR Scanning Manager` disabled in the scene so `RecordingDemo.StartScanning()` still controls when scanning begins.

At this stage, the sample is configured to produce raycast visualization data, but nothing is drawing that data on screen yet. The next section adds the material and camera component used to render it.

</div>

</div>

------------------------------------------------------------------------

### Add a visualization renderer to your AR screen<a href="#unity-add-a-visualization-renderer-to-your-ar-screen" class="hash-link" aria-label="Direct link to Add a visualization renderer to your AR screen" title="Direct link to Add a visualization renderer to your AR screen">​</a>

This section shows how to add the material and camera-side component that render scan visualization over the live AR view.

Follow this workflow to add the visualization renderer:

1.  Create a new Unity `Material` asset for the scan overlay, then select that new asset in the **Inspector** and set its shader to `Unlit > NsdkScanningStripes`. This shader is provided by the NSDK package and composites the striped overlay from the textures produced by [AR Scanning Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager/). In the following runnable code, see step ⅱ for one implementation.

2.  Add scan-visualization renderer logic to a camera-side component. You can create a new script for scan visualization, or extend an existing camera or overlay script that already owns your AR rendering flow. The component should store the visualization material and [AR Scanning Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager/) references, get `ARCameraManager` from the same `GameObject`, and prepare the camera-side state that later sections use to render the overlay over the live AR view. In the following runnable example, see steps ⅲ and ⅳ for one implementation.

    The following code example shows the camera-side component shape used for this setup:

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    using NianticSpatial.NSDK.AR.Scanning;
    using UnityEngine;
    using UnityEngine.XR.ARFoundation;

    public class ScanVisualization : MonoBehaviour
    {
        // The material that composites the scan visualization over the camera image.
        [SerializeField] private Material _raycastVisualizationMaterial;
        // The scanning manager that provides the raycast visualization textures.
        [SerializeField] private ARScanningManager _arScanningManager;

        // The camera manager on this same camera object.
        private ARCameraManager _arCameraManager;

        private void Start()
        {
            _arCameraManager = GetComponent<ARCameraManager>();

            if (_arCameraManager == null || _arScanningManager == null || _raycastVisualizationMaterial == null)
            {
                Debug.LogError("Assign all required components and serialized fields.");
                return;
            }
        }
    }
    ```

    </div>

    </div>

    Expand the previous example to include the script file, camera attachment, material creation, and Inspector assignments if you want a runnable Unity version of this setup. In the following runnable example, see step ⅴ for one implementation.

3.  Prepare the camera-side component for rendering. Confirm that its required references are assigned, get `ARCameraManager` from the same `GameObject`, and initialize any state needed for the later rendering steps. In the following runnable example, see step ⅳ for one implementation.

4.  Add the camera-side component to the camera object that already owns `ARCameraManager`. In the Recording sample, that camera object is `XR Origin > Camera Offset > Main Camera`. In the following runnable example, see step ⅴ for one implementation.

5.  In the **Inspector**, assign the material you created to **Raycast Visualization Material**, then assign the `ARScanningManager` reference from the object that owns scanning. In the Recording sample, drag the top-level **AR Session** GameObject into **Ar Scanning Manager**, or use the object picker and choose `AR Session (ARScanningManager)`. In the following runnable example, see steps ⅵ and ⅶ for one implementation.

    Keep the sample's existing scan lifecycle unchanged. At this stage, the material and camera-side component are wired together, but the overlay does not appear until the later sections connect rendering to scan state and AR frame updates.

Expand to reveal a minimal Unity example for renderer setup

<div>

<div class="collapsibleContent_i85q">

This example builds on the previous step and adds only the material plus a minimal `ScanVisualization` component. The script validates its references and attaches to `XR Origin > Camera Offset > Main Camera`, but it does not render the overlay yet.

- ⅰ. In the **Project** window, create a new `Material` asset named `ScanningStripesMaterial`, select it, and set its shader to `Unlit > NsdkScanningStripes`.
- ⅱ. In the **Project** window, create a new C# script named `ScanVisualization`.
- ⅲ. Replace the contents of `ScanVisualization.cs` with the following code:

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using NianticSpatial.NSDK.AR.Scanning;
using UnityEngine;
using UnityEngine.XR.ARFoundation;

public class ScanVisualization : MonoBehaviour
{
    // The material that composites the scan visualization over the camera image.
    [SerializeField] private Material _raycastVisualizationMaterial;
    // The scanning manager that provides the raycast visualization textures.
    [SerializeField] private ARScanningManager _arScanningManager;

    // The camera manager on this same camera object.
    private ARCameraManager _arCameraManager;
    private void Start()
    {
        _arCameraManager = GetComponent<ARCameraManager>();

        if (_arCameraManager == null || _arScanningManager == null || _raycastVisualizationMaterial == null)
        {
            Debug.LogError("Assign all required components and serialized fields.");
            return;
        }
    }
}
```

</div>

</div>

- ⅳ. Add `ScanVisualization` to `XR Origin > Camera Offset > Main Camera`.
- ⅴ. In the **Inspector**, assign `ScanningStripesMaterial` to **Raycast Visualization Material**.
- ⅵ. In the **Inspector**, drag the top-level **AR Session** GameObject into **Ar Scanning Manager**, or use the object picker and choose `AR Session (ARScanningManager)`.

When you test this step:

- Enter Play mode in Unity or run the sample on your device.
- Confirm that the scene still opens normally and that the existing scan UI is still visible.
- Confirm that no striped overlay appears yet, because the later rendering steps have not been added.
- Optionally, verify that `Assign all required components and serialized fields.` does not appear in the Unity Console or device logs.

</div>

</div>

------------------------------------------------------------------------

### Start and stop the visualization with capture<a href="#unity-start-and-stop-the-visualization-with-capture" class="hash-link" aria-label="Direct link to Start and stop the visualization with capture" title="Direct link to Start and stop the visualization with capture">​</a>

This section shows how scan visualization fits into the existing capture flow so the overlay appears when scanning starts and disappears when scanning stops. In the Recording sample, `RecordingDemo` already owns that lifecycle, so the visualization component added in this guide does not define new start or stop handlers.

Keep your existing capture flow responsible for turning scanning on and off. In `nsdk-samples-csharp`, that code lives in `NsdkSamples/Assets/Samples/Scanning/Scripts/RecordingDemo.cs`. The following code example shows the portion of the sample that starts and stops scanning:

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
private void HandleCameraPermissionGranted()
{
    _arScanningManager.ScanRecordingFramerate = (int)_framerateSlider.value;
    _arScanningManager.enabled = true;
}

public void StartScanning()
{
    _sharePlaybackButton.gameObject.SetActive(false);
    _maxTimePerChunkSlider.interactable = false;
    _framerateSlider.interactable = false;
    _saveScanPanel.SetActive(false);
    CheckCameraPermission();
}

public async void StopScanning()
{
    await _arScanningManager.SaveScan();
    _arScanningManager.enabled = false;

    _maxTimePerChunkSlider.interactable = true;
    _framerateSlider.interactable = true;
    _saveScanPanel.SetActive(true);
}
```

</div>

</div>

In the previous code example:

- `HandleCameraPermissionGranted()` sets the scan framerate, then enables `ARScanningManager`, which is the state the visualization renderer later checks before drawing.
- `StartScanning()` leaves the sample's existing UI flow in place and does not need any visualization-specific branching.
- `StopScanning()` saves the scan, disables `ARScanningManager`, and returns control to the sample's save UI.
- The Unity renderer added in this guide follows that existing lifecycle by rendering only while `ARScanningManager.enabled` and `EnableRaycastVisualization` are both true.

This means the next section only needs to observe scan state and update the overlay while capture is active.

Validate this step with the following workflow:

1.  Run the Recording scene on your device or in the Unity Editor with [Playback](https://www.nianticspatial.com/docs/nsdk/features/playback/) enabled.
2.  Tap **Start Scan** to begin scanning.
3.  Confirm that the sample's existing scan UI responds normally and that scanning begins without any new visualization-specific buttons or errors.
4.  Tap **Stop Scan** to end scanning.
5.  Confirm that the sample returns to its existing save or export UI flow.
6.  Optionally, verify in the Unity Console or in device logs that no scan-save error appears while `RecordingDemo.StopScanning()` runs.

------------------------------------------------------------------------

### Update the visualization while AR frames arrive<a href="#unity-update-the-visualization-while-ar-frames-arrive" class="hash-link" aria-label="Direct link to Update the visualization while AR frames arrive" title="Direct link to Update the visualization while AR frames arrive">​</a>

This section shows how the visualization updates continuously as camera frames arrive so the overlay reflects the latest scan coverage in real time. It also explains how the `ScanVisualization` component keeps the raycast data aligned with the camera image before compositing it in a URP render pass.

This section builds on the camera-side renderer setup from the previous steps and assumes:

- the project uses the current URP-configured sample project
- the visualization material uses the `Unlit/NsdkScanningStripes` shader

1.  Update the camera-side renderer so it subscribes to `ARCameraManager.frameReceived`, copies camera images into a short queue, and enqueues a URP render pass that composites the latest raycast texture. The following code example shows one implementation. In the following runnable example, see step ⅰ for one implementation:

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
    private void Start()
    {
        // Reuse the camera and ARCameraManager already attached to this object.
        _camera = GetComponent<Camera>();
        _arCameraManager = GetComponent<ARCameraManager>();

        if (_camera == null || _arCameraManager == null || _arScanningManager == null || _raycastVisualizationMaterial == null)
        {
            Debug.LogError("Assign all required components and serialized fields.");
            return;
        }

        // Prepare the render-pass state, then listen for new camera frames.
        _cameraTexturesQueue = new Queue<Texture2D>();
        _renderPass = new ScanVisualizationRenderPass();
        _fullScreenMesh = CreateFullScreenMesh();
        _arCameraManager.frameReceived += OnARCameraFrameReceived;
        RenderPipelineManager.beginCameraRendering += EnqueueUniversalRenderPass;
    }

    private void OnARCameraFrameReceived(ARCameraFrameEventArgs args)
    {
        // Only queue frames while scan visualization is active.
        if (!(_arScanningManager.enabled && _arScanningManager.EnableRaycastVisualization))
        {
            return;
        }

        // Copy the latest camera image into a Texture2D, then enqueue it.
        var newTexture = CopyLatestCameraFrame(args);
        if (newTexture == null)
        {
            return;
        }

        EnqueueCameraTexture(newTexture);
    }

    private void EnqueueUniversalRenderPass(ScriptableRenderContext context, Camera currentCamera)
    {
        // Enqueue the URP pass only for this camera while visualization is active.
        if (currentCamera != _camera ||
            !(_arScanningManager.enabled && _arScanningManager.EnableRaycastVisualization) ||
            _cameraTexturesQueue.Count <= Delay)
        {
            return;
        }

        UpdateVisualizationMaterial();
        _renderPass.Material = _raycastVisualizationMaterial;
        _renderPass.Mesh = _fullScreenMesh;
        currentCamera.GetUniversalAdditionalCameraData().scriptableRenderer.EnqueuePass(_renderPass);
    }

    private void OnDestroy()
    {
        if (_arCameraManager != null)
        {
            _arCameraManager.frameReceived -= OnARCameraFrameReceived;
        }

        RenderPipelineManager.beginCameraRendering -= EnqueueUniversalRenderPass;

        while (_cameraTexturesQueue != null && _cameraTexturesQueue.Count > 0)
        {
            Destroy(_cameraTexturesQueue.Dequeue());
        }
    }
}
```

</div>

</div>

In the previous code example:

- `OnARCameraFrameReceived()` captures camera images into a short queue only while scanning is active and raycast visualization is enabled
- [GetRaycastColorTexture()](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager.GetRaycastColorTexture/) provides the visualization texture used by the shader
- `EnqueueUniversalRenderPass()` updates the material and schedules the URP pass that draws the striped overlay for the active camera
- `CopyLatestCameraFrame()`, `EnqueueCameraTexture()`, `UpdateVisualizationMaterial()`, `CreateFullScreenMesh()`, and `ScanVisualizationRenderPass` are helper members that the runnable example defines so the main workflow can stay focused on the rendering flow
- the two-frame delay helps keep the raycast data aligned with the camera image

2.  Validate this step with the following workflow. In the following runnable example, see step ⅱ for one implementation:
    1.  Run the scene on your device or in the Unity Editor with [Playback](https://www.nianticspatial.com/docs/nsdk/features/playback/) enabled.
    2.  Tap **Start Scan** to begin scanning.
    3.  Confirm that diagonal stripes appear over the camera feed.
    4.  Scan more of the scene, then confirm that covered areas transition from striped to full color.
    5.  Tap **Stop Scan**, then confirm that the visualization disappears when scanning ends.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

If you also want to save the recorded scan data, call [SaveScan()](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager.SaveScan/) on `AR Scanning Manager` before disabling it. For more information, see [How to create playback datasets](https://www.nianticspatial.com/docs/nsdk/how-to/playback/create_playback_dataset/).

</div>

</div>

Runnable example: Update Unity scan visualization each frame

<div>

<div class="collapsibleContent_i85q">

This example builds on the previous sections and replaces the placeholder `ScanVisualization.cs` file with a runnable version that renders the striped overlay while the Recording sample is scanning.

Use `NsdkSamples/Assets/Samples/Scanning/Scenes/Recording.unity` as the runnable baseline for this example.

- ⅰ. Replace the contents of `ScanVisualization.cs` with the following code:

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System;
using System.Collections.Generic;
using NianticSpatial.NSDK.AR.Scanning;
using NianticSpatial.NSDK.AR.Utilities;
using Unity.Collections;
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Rendering.RenderGraphModule;
using UnityEngine.Rendering.Universal;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;

public class ScanVisualization : MonoBehaviour
{
    // The material that composites the striped visualization overlay.
    [SerializeField] private Material _raycastVisualizationMaterial;
    // The scanning manager that provides the raycast visualization texture.
    [SerializeField] private ARScanningManager _arScanningManager;

    // The camera this component renders for.
    private Camera _camera;
    // The AR camera manager already attached to the same camera object.
    private ARCameraManager _arCameraManager;
    // The delayed camera frame currently bound to the visualization material.
    private Texture2D _currentCameraTexture;
    // A short queue used to keep the camera image aligned with the raycast texture.
    private Queue<Texture2D> _cameraTexturesQueue;
    // A full-screen mesh used by the URP render pass.
    private Mesh _fullScreenMesh;
    // The URP render pass that draws the visualization overlay.
    private ScanVisualizationRenderPass _renderPass;
    private const int Delay = 2;

    private void Start()
    {
        // Reuse the camera and ARCameraManager already attached to this object.
        _camera = GetComponent<Camera>();
        _arCameraManager = GetComponent<ARCameraManager>();

        if (_camera == null || _arCameraManager == null || _arScanningManager == null || _raycastVisualizationMaterial == null)
        {
            Debug.LogError("Assign all required components and serialized fields.");
            return;
        }

        // Prepare the render-pass state, then listen for new camera frames.
        _cameraTexturesQueue = new Queue<Texture2D>();
        _fullScreenMesh = CreateFullScreenMesh();
        _renderPass = new ScanVisualizationRenderPass();
        _arCameraManager.frameReceived += OnARCameraFrameReceived;
        RenderPipelineManager.beginCameraRendering += EnqueueUniversalRenderPass;
        Debug.Log("ScanVisualization: renderer setup validated.");
    }

    private void OnARCameraFrameReceived(ARCameraFrameEventArgs args)
    {
        // Only queue frames while scan visualization is active.
        if (!(_arScanningManager.enabled && _arScanningManager.EnableRaycastVisualization))
        {
            return;
        }

#if UNITY_EDITOR
        // In the Editor, copy the simulated camera texture directly.
        if (args.textures.Count == 0)
        {
            return;
        }

        var sourceTexture = args.textures[0];
        var newTexture = new Texture2D(
            sourceTexture.width,
            sourceTexture.height,
            sourceTexture.format,
            sourceTexture.mipmapCount > 1);
        Graphics.CopyTexture(sourceTexture, 0, 0, newTexture, 0, 0);
#else
        // On device, convert the latest CPU camera image into an RGBA texture.
        if (!_arCameraManager.TryAcquireLatestCpuImage(out XRCpuImage image))
        {
            return;
        }

        var newTexture = new Texture2D(image.width, image.height, TextureFormat.RGBA32, false);
        var conversionParams = new XRCpuImage.ConversionParams(
            image,
            TextureFormat.RGBA32,
            XRCpuImage.Transformation.None);

        var rawTextureData = newTexture.GetRawTextureData<byte>();
        try
        {
            image.Convert(conversionParams, new NativeSlice<byte>(rawTextureData));
            newTexture.Apply();
        }
        finally
        {
            image.Dispose();
        }
#endif

        while (_cameraTexturesQueue.Count > Delay + 1)
        {
            Destroy(_cameraTexturesQueue.Dequeue());
        }

        _cameraTexturesQueue.Enqueue(newTexture);
    }

    private void EnqueueUniversalRenderPass(ScriptableRenderContext context, Camera currentCamera)
    {
        // Enqueue the URP pass only for this camera while visualization is active.
        if (currentCamera != _camera ||
            !(_arScanningManager.enabled && _arScanningManager.EnableRaycastVisualization) ||
            _cameraTexturesQueue.Count <= Delay)
        {
            return;
        }

        UpdateVisualizationMaterial();
        _renderPass.Material = _raycastVisualizationMaterial;
        _renderPass.Mesh = _fullScreenMesh;
        currentCamera.GetUniversalAdditionalCameraData().scriptableRenderer.EnqueuePass(_renderPass);
    }

    private void UpdateVisualizationMaterial()
    {
        // Advance to the delayed camera frame that should match the latest raycast texture.
        if (_currentCameraTexture != null)
        {
            Destroy(_currentCameraTexture);
        }

        _currentCameraTexture = _cameraTexturesQueue.Dequeue();
        _raycastVisualizationMaterial.SetTexture("_MainTex", _currentCameraTexture);
        _raycastVisualizationMaterial.SetTexture("_ColorTex", _arScanningManager.GetRaycastColorTexture());
        _raycastVisualizationMaterial.SetInt("_ScreenOrientation", (int)XRDisplayContext.GetScreenOrientation());
        _raycastVisualizationMaterial.SetTexture("_ArCameraTex", _currentCameraTexture);
    }

    private void EnqueueCameraTexture(Texture2D newTexture)
    {
        // Keep the queue short so old camera textures do not accumulate.
        while (_cameraTexturesQueue.Count > Delay + 1)
        {
            Destroy(_cameraTexturesQueue.Dequeue());
        }

        _cameraTexturesQueue.Enqueue(newTexture);
    }

    private static Mesh CreateFullScreenMesh()
    {
        // Create a full-screen quad for the URP render pass to draw.
        var mesh = new Mesh
        {
            vertices = new[]
            {
                new Vector3(0f, 0f, -1f),
                new Vector3(0f, 1f, -1f),
                new Vector3(1f, 1f, -1f),
                new Vector3(1f, 0f, -1f),
            },
            uv = new[]
            {
                new Vector2(0f, 0f),
                new Vector2(0f, 1f),
                new Vector2(1f, 1f),
                new Vector2(1f, 0f),
            },
            triangles = new[] {0, 1, 2, 0, 2, 3}
        };

        mesh.UploadMeshData(false);
        return mesh;
    }

    private void OnDestroy()
    {
        if (_arCameraManager != null)
        {
            _arCameraManager.frameReceived -= OnARCameraFrameReceived;
        }

        RenderPipelineManager.beginCameraRendering -= EnqueueUniversalRenderPass;

        if (_currentCameraTexture != null)
        {
            Destroy(_currentCameraTexture);
        }

        if (_fullScreenMesh != null)
        {
            Destroy(_fullScreenMesh);
        }

        while (_cameraTexturesQueue != null && _cameraTexturesQueue.Count > 0)
        {
            Destroy(_cameraTexturesQueue.Dequeue());
        }
    }

    private sealed class ScanVisualizationRenderPass : ScriptableRenderPass
    {
        public Material Material { get; set; }
        public Mesh Mesh { get; set; }

        private static readonly Matrix4x4 s_projection = Matrix4x4.Ortho(0f, 1f, 0f, 1f, 0f, 1f);

        private class PassData
        {
            public UniversalCameraData CameraData;
            public UniversalResourceData ResourceData;
            public Material Material;
            public Mesh Mesh;
        }

        public ScanVisualizationRenderPass()
        {
            // Draw after the camera background and scene geometry are already visible.
            profilingSampler = new ProfilingSampler("Scan Visualization");
            renderPassEvent = RenderPassEvent.AfterRenderingTransparents;
        }

        public override void RecordRenderGraph(RenderGraph renderGraph, ContextContainer frameData)
        {
            // Unity 6 uses Render Graph by default, so record the full-screen overlay here.
            using var builder =
                renderGraph.AddRasterRenderPass<PassData>("Scan Visualization", out var passData, profilingSampler);

            passData.CameraData = frameData.Get<UniversalCameraData>();
            passData.ResourceData = frameData.Get<UniversalResourceData>();
            passData.Material = Material;
            passData.Mesh = Mesh;

            builder.SetRenderAttachment(passData.ResourceData.activeColorTexture, 0);
            builder.SetRenderFunc((PassData data, RasterGraphContext renderContext) =>
            {
                var cmd = renderContext.cmd;
                cmd.SetViewProjectionMatrices(Matrix4x4.identity, s_projection);
                cmd.DrawMesh(data.Mesh, Matrix4x4.identity, data.Material);
                cmd.SetViewProjectionMatrices(
                    data.CameraData.camera.worldToCameraMatrix,
                    data.CameraData.camera.projectionMatrix);
            });
        }

        [Obsolete("This rendering path is for compatibility mode only (when Render Graph is disabled). Use Render Graph API instead.", false)]
        public override void Execute(ScriptableRenderContext context, ref RenderingData renderingData)
        {
            // Keep a compatibility path for projects where Render Graph is disabled.
            var cmd = CommandBufferPool.Get("Scan Visualization");
            using (new ProfilingScope(cmd, profilingSampler))
            {
                cmd.SetViewProjectionMatrices(Matrix4x4.identity, s_projection);
                cmd.DrawMesh(Mesh, Matrix4x4.identity, Material);
                cmd.SetViewProjectionMatrices(
                    renderingData.cameraData.camera.worldToCameraMatrix,
                    renderingData.cameraData.camera.projectionMatrix);
            }

            context.ExecuteCommandBuffer(cmd);
            CommandBufferPool.Release(cmd);
        }
    }
}
```

</div>

</div>

- ⅱ. Validate the runnable example:

  1.  Run the Recording scene on your device or in the Unity Editor with [Playback](https://www.nianticspatial.com/docs/nsdk/features/playback/) enabled.
  2.  Confirm that `ScanVisualization: renderer setup validated.` appears in the Unity Console or in `adb logcat -s Unity | grep "ScanVisualization"`.
  3.  Tap **Start Scan** to begin scanning.
  4.  Wait a few seconds for the visualization to begin updating.
  5.  Confirm that diagonal stripes appear over the camera feed.
  6.  Move the device to scan more of the scene, then confirm that covered areas transition from striped to full color.
  7.  Tap **Stop Scan**, then confirm that the visualization disappears when scanning ends.

</div>

</div>

------------------------------------------------------------------------

## Troubleshooting<a href="#troubleshooting" class="hash-link" aria-label="Direct link to Troubleshooting" title="Direct link to Troubleshooting">​</a>

### Visualization doesn't appear<a href="#visualization-doesnt-appear" class="hash-link" aria-label="Direct link to Visualization doesn&#39;t appear" title="Direct link to Visualization doesn&#39;t appear">​</a>

- Confirm that scanning is active in the Recording sample.
- Ensure that **Enable Raycast Visualization** is enabled on the `AR Scanning Manager` component on **AR Session**.
- Verify that the `ScanVisualization` script is attached to the camera object used by your XR Origin and that all serialized fields are assigned.
- Check that `ScanningStripesMaterial` uses the `Unlit > NsdkScanningStripes` shader.
- Confirm that `ScanVisualization: renderer setup validated.` appears before you tap **Start**.
- If your project uses a different Unity or URP version than the sample, verify that the render-pass APIs used in `ScanVisualization.cs` are available and compatible.
- Verify that depth is available. If LiDAR is unavailable, enable **Record Estimated Depth**. If LiDAR is available, add **AR Occlusion Manager** to the camera object used by your XR Origin.

### Overlay doesn't update<a href="#overlay-doesnt-update" class="hash-link" aria-label="Direct link to Overlay doesn&#39;t update" title="Direct link to Overlay doesn&#39;t update">​</a>

- If the sample's **Start Scan Button** responds but the overlay stays blank, verify that `RecordingDemo.StartScanning()` is enabling the `AR Scanning Manager` referenced from **AR Session** and that **Enable Raycast Visualization** is still turned on in that component.
- Check that `OnARCameraFrameReceived()` is receiving frames while scanning is active and that `_cameraTexturesQueue` grows beyond the two-frame delay before `EnqueueUniversalRenderPass()` tries to schedule the URP pass.
- If the overlay appears misaligned, confirm that `UpdateVisualizationMaterial()` is still assigning the queued camera texture to both `_MainTex` and `_ArCameraTex` before the render pass is enqueued.
- If the overlay flashes briefly and disappears, make sure `RecordingDemo.StopScanning()` is not being called from another UI path and that the queue is not being emptied while capture is still active.

### Performance issues<a href="#performance-issues" class="hash-link" aria-label="Direct link to Performance issues" title="Direct link to Performance issues">​</a>

- Scan visualization processes each recorded camera frame, so lower-end devices may show reduced performance while scanning.
- Lower the recording framerate on `AR Scanning Manager` if needed.
- Avoid running other expensive AR features such as meshing or device mapping at the same time unless necessary.
- Using a shallower depth range reduces compute cost.

</div>

</div>
