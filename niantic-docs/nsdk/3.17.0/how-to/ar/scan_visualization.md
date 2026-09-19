---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/scan_visualization/
title: How to Enable Scan Visualization
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Enable Scan Visualization in AR

</div>

Niantic Spatial SDK's raycast visualization feature provides real-time visual feedback during scanning by overlaying diagonal stripes on the camera feed. Areas that have been successfully scanned appear in full color, while unscanned areas display the stripe pattern. This helps you ensure comprehensive coverage of the scene while recording.

<div style="text-align:center">

![Example of raycast visualization in an AR scene](https://www.nianticspatial.com/docs/assets/images/scanning_stripes_example-730867349edf10322898e3bed014f11c.gif)

</div>

This how-to will walk you through:

- Setting up AR Scanning Manager with raycast visualization
- Creating a material for rendering the visualization
- Building a script to handle scanning and visualization rendering

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Built-in Render Pipeline Unity project with ARDK installed and a basic AR scene. For more information, see [Installing ARDK 3](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/) and [Setting up a Basic AR Scene](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/#setting-up-a-basic-ar-scene).

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

This sample code only works with Unity's **Built-in Render Pipeline**. `OnRenderImage` is not compatible with URP, so a different approach to rendering the scanning stripes will be required for URP projects.

</div>

</div>

## Configure AR Scanning Manager<a href="#configure-ar-scanning-manager" class="hash-link" aria-label="Direct link to Configure AR Scanning Manager" title="Direct link to Configure AR Scanning Manager">​</a>

First, add an AR Scanning Manager component with the correct settings for raycast visualization.

1.  In your scene hierarchy, select the XR Origin → Camera Offset → **Main Camera** GameObject.
2.  In the **Inspector** window, click **Add Component** and add an **AR Scanning Manager** component to Main Camera.
3.  Configure the following settings:
    - Enable **Record Estimated Depth** (or leave unchecked if your device has lidar and add an **AR Occlusion Manager** to Main Camera).
    - Enable **Enable Raycast Visualization**.
4.  **Disable** the manager component so that it does not start recording when the scene starts.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

If your device has a lidar sensor, you can leave **Record Estimated Depth** unchecked. Ensure that **Prefer LiDAR if Available** is enabled in Niantic SDK Settings under XR Plug-in Management. You will also need an **AR Occlusion Manager** component on the Main Camera to enable lidar depth data.

</div>

</div>

## Create the Visualization Material<a href="#create-the-visualization-material" class="hash-link" aria-label="Direct link to Create the Visualization Material" title="Direct link to Create the Visualization Material">​</a>

The raycast visualization requires a material that uses the `LightshipScanningStripes` shader.

1.  In your project's **Assets** folder, right-click and select **Create** → **Material**. Name it **ScanningStripesMaterial**.
2.  With the material selected in the **Inspector**, click the shader dropdown and search for **LightshipScanningStripes**.
3.  Optionally, adjust the **Stripe Color** property to change the color of the scanning stripes (default is red).

## Set Up the UI<a href="#set-up-the-ui" class="hash-link" aria-label="Direct link to Set Up the UI" title="Direct link to Set Up the UI">​</a>

Add buttons to control scanning from the user interface.

1.  Find your **Canvas** GameObject in the hierarchy, or create one if it does not exist (Right-click → **UI** → **Canvas**).
2.  Under the Canvas, add two Legacy Buttons (Right-click → **UI** → **Legacy** → **Button**). Name them **Start Button** and **Stop Button**.
3.  Update each button's text label to match its name:
    - Select the **Start Button** GameObject, expand it in the hierarchy, and select the **Text** child object. In the **Inspector**, change the **Text** field to "Start".
    - Repeat for **Stop Button**, setting the text to "Stop".
4.  In the **Inspector**, **disable** the **Stop Button** so it's hidden until scanning starts.
5.  Position the buttons in the scene view so they are visible and accessible.

## Create the Visualization Script<a href="#create-the-visualization-script" class="hash-link" aria-label="Direct link to Create the Visualization Script" title="Direct link to Create the Visualization Script">​</a>

Now, create a script that handles scanning and renders the raycast visualization.

1.  Ensure that your project uses the Built-in Render Pipeline. If this project uses URP, see the note under Prerequisites.
2.  <a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-allowUnsafeCode.html" target="_blank" rel="noopener noreferrer">Enable unsafe C# code</a> to facilitate interaction with the SDK's native layer. Under **Edit → Project Settings → Player → Other Settings**, enable **Allow 'unsafe' Code**.
3.  In the **Hierarchy**, select the **Main Camera** GameObject.
4.  In the **Inspector**, click **Add Component** and select **New Script**. Name the script **ScanVisualization**.
5.  Double-click the script to open it in your code editor.
6.  Add the necessary using statements and serialized fields:

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System.Collections.Generic;
using Niantic.Lightship.AR.Scanning;
using Niantic.Lightship.AR.Utilities;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;
using Unity.Collections.LowLevel.Unsafe;

public class ScanVisualization : MonoBehaviour
{
    [SerializeField]
    private Material _raycastVisualizationMaterial;

    [SerializeField]
    private Button _startButton;

    [SerializeField]
    private Button _stopButton;

    private ARCameraManager _arCameraManager;
    private ARScanningManager _arScanningManager;
    private Queue<Texture2D> _cameraTexturesQueue;
    private const int Delay = 2; // Delay frames to synchronize visualization with camera image
    private bool _isScanning;
```

</div>

</div>

7.  Initialize the camera manager and button listeners in `Start()`:

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
    private void Start()
    {
        _arCameraManager = GetComponent<ARCameraManager>();
        _arScanningManager = GetComponent<ARScanningManager>();
        if (_arCameraManager == null || _arScanningManager == null
            || _raycastVisualizationMaterial == null
            || _startButton == null || _stopButton == null)
        {
            Debug.LogError("A required component is not present. " +
                           "Please check the serialized fields in the Inspector " +
                           "and place this script on a GameObject with the " +
                           "ARCameraManager and ARScanningManager.");
            return;
        }

        _cameraTexturesQueue = new Queue<Texture2D>();
        _arCameraManager.frameReceived += OnARCameraFrameReceived;

        _startButton.onClick.AddListener(StartScanning);
        _stopButton.onClick.AddListener(StopScanning);
    }
```

</div>

</div>

8.  Add the `StartScanning()` method:

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
    public void StartScanning()
    {
        _isScanning = true;
        _startButton.gameObject.SetActive(false);
        _stopButton.gameObject.SetActive(true);
        _arScanningManager.enabled = true;
    }
```

</div>

</div>

9.  Add the `StopScanning()` method:

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
    public void StopScanning()
    {
        _isScanning = false;
        _startButton.gameObject.SetActive(true);
        _stopButton.gameObject.SetActive(false);
        _arScanningManager.enabled = false;

        // Clear the camera texture queue
        while (_cameraTexturesQueue.Count > 0)
        {
            Destroy(_cameraTexturesQueue.Dequeue());
        }
    }
```

</div>

</div>

10. Implement the camera frame handler to capture camera textures:

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
    private void OnARCameraFrameReceived(ARCameraFrameEventArgs args)
    {
        if (!(_isScanning && _arScanningManager.EnableRaycastVisualization))
        {
            return;
        }

#if UNITY_EDITOR
        if (args.textures.Count == 0)
        {
            Debug.LogWarning("Camera frame received with no textures.");
            return;
        }
        var sourceTexture = args.textures[0];
        Texture2D newTexture = new Texture2D(sourceTexture.width, sourceTexture.height, sourceTexture.format, sourceTexture.mipmapCount > 1);
        Graphics.CopyTexture(sourceTexture, 0, 0, newTexture, 0, 0);
#else
        if (!_arCameraManager.TryAcquireLatestCpuImage(out XRCpuImage image))
        {
            return;
        }

        TextureFormat format = TextureFormat.RGBA32;
        var newTexture = new Texture2D(image.width, image.height, format, false);
        var conversionParams = new XRCpuImage.ConversionParams(image, format, XRCpuImage.Transformation.None);

        var rawTextureData = newTexture.GetRawTextureData<byte>();
        try
        {
            unsafe
            {
                image.Convert(conversionParams, new System.IntPtr(rawTextureData.GetUnsafePtr()), rawTextureData.Length);
                newTexture.Apply();
            }
        }
        finally
        {
            image.Dispose();
        }
#endif
        // Prevent the queue from growing indefinitely
        while (_cameraTexturesQueue.Count > Delay + 1)
        {
            DestroyImmediate(_cameraTexturesQueue.Dequeue());
        }

        _cameraTexturesQueue.Enqueue(newTexture);
    }
```

</div>

</div>

11. Implement `OnRenderImage()` to render the visualization overlay:

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
    private void OnRenderImage(RenderTexture src, RenderTexture dest)
    {
        if (_isScanning && _arScanningManager.EnableRaycastVisualization)
        {
            if (_cameraTexturesQueue.Count <= Delay)
            {
                Graphics.Blit(src, dest);
                return;
            }

            var currentTexture = _cameraTexturesQueue.Dequeue();

            // Set the material properties for the shader
            _raycastVisualizationMaterial.SetTexture("MainTex", currentTexture);
            _raycastVisualizationMaterial.SetTexture("_ColorTex", _arScanningManager.GetRaycastColorTexture());
            _raycastVisualizationMaterial.SetInt("_ScreenOrientation", (int)XRDisplayContext.GetScreenOrientation());
            _raycastVisualizationMaterial.SetTexture("_ArCameraTex", currentTexture);

            // Render with the visualization material
            Graphics.Blit(src, dest, _raycastVisualizationMaterial);

            Destroy(currentTexture);
        }
        else
        {
            Graphics.Blit(src, dest);
        }
    }
```

</div>

</div>

12. Clean up in `OnDestroy()` and complete the class:

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
    private void OnDestroy()
    {
        if (_arCameraManager != null)
        {
            _arCameraManager.frameReceived -= OnARCameraFrameReceived;
        }

        while (_cameraTexturesQueue != null && _cameraTexturesQueue.Count > 0)
        {
            Destroy(_cameraTexturesQueue.Dequeue());
        }
    }
}
```

</div>

</div>

Click to reveal the full script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System.Collections.Generic;
using Niantic.Lightship.AR.Scanning;
using Niantic.Lightship.AR.Utilities;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;
using Unity.Collections.LowLevel.Unsafe;

public class ScanVisualization : MonoBehaviour
{
    [SerializeField]
    private Material _raycastVisualizationMaterial;

    [SerializeField]
    private Button _startButton;

    [SerializeField]
    private Button _stopButton;

    private ARCameraManager _arCameraManager;
    private ARScanningManager _arScanningManager;
    private Queue<Texture2D> _cameraTexturesQueue;
    private const int Delay = 2; // Delay frames to synchronize visualization with camera image
    private bool _isScanning;

    private void Start()
    {
        _arCameraManager = GetComponent<ARCameraManager>();
        _arScanningManager = GetComponent<ARScanningManager>();
        if (_arCameraManager == null || _arScanningManager == null
            || _raycastVisualizationMaterial == null
            || _startButton == null || _stopButton == null)
        {
            Debug.LogError("A required component is not present. " +
                           "Please check the serialized fields in the Inspector " +
                           "and place this script on a GameObject with the " +
                           "ARCameraManager and ARScanningManager.");
            return;
        }

        _cameraTexturesQueue = new Queue<Texture2D>();
        _arCameraManager.frameReceived += OnARCameraFrameReceived;

        _startButton.onClick.AddListener(StartScanning);
        _stopButton.onClick.AddListener(StopScanning);
    }

    public void StartScanning()
    {
        _isScanning = true;
        _startButton.gameObject.SetActive(false);
        _stopButton.gameObject.SetActive(true);
        _arScanningManager.enabled = true;
    }

    public void StopScanning()
    {
        _isScanning = false;
        _startButton.gameObject.SetActive(true);
        _stopButton.gameObject.SetActive(false);
        _arScanningManager.enabled = false;

        // Clear the camera texture queue
        while (_cameraTexturesQueue.Count > 0)
        {
            Destroy(_cameraTexturesQueue.Dequeue());
        }
    }

    private void OnARCameraFrameReceived(ARCameraFrameEventArgs args)
    {
        if (!(_isScanning && _arScanningManager.EnableRaycastVisualization))
        {
            return;
        }

#if UNITY_EDITOR
        if (args.textures.Count == 0)
        {
            Debug.LogWarning("Camera frame received with no textures.");
            return;
        }
        var sourceTexture = args.textures[0];
        Texture2D newTexture = new Texture2D(sourceTexture.width, sourceTexture.height, sourceTexture.format,
                                             sourceTexture.mipmapCount > 1);
        Graphics.CopyTexture(sourceTexture, 0, 0, newTexture, 0, 0);
#else
        if (!_arCameraManager.TryAcquireLatestCpuImage(out XRCpuImage image))
        {
            return;
        }

        TextureFormat format = TextureFormat.RGBA32;
        var newTexture = new Texture2D(image.width, image.height, format, false);
        var conversionParams = new XRCpuImage.ConversionParams(image, format, XRCpuImage.Transformation.None);

        var rawTextureData = newTexture.GetRawTextureData<byte>();
        try
        {
            unsafe
            {
                image.Convert(conversionParams, new System.IntPtr(rawTextureData.GetUnsafePtr()),
                              rawTextureData.Length);
                newTexture.Apply();
            }
        }
        finally
        {
            image.Dispose();
        }
#endif
        // Prevent the queue from growing indefinitely
        while (_cameraTexturesQueue.Count > Delay + 1)
        {
            DestroyImmediate(_cameraTexturesQueue.Dequeue());
        }

        _cameraTexturesQueue.Enqueue(newTexture);
    }

    private void OnRenderImage(RenderTexture src, RenderTexture dest)
    {
        if (_isScanning && _arScanningManager.EnableRaycastVisualization)
        {
            if (_cameraTexturesQueue.Count <= Delay)
            {
                Graphics.Blit(src, dest);
                return;
            }

            var currentTexture = _cameraTexturesQueue.Dequeue();

            // Set the material properties for the shader
            _raycastVisualizationMaterial.SetTexture("MainTex", currentTexture);
            _raycastVisualizationMaterial.SetTexture("_ColorTex", _arScanningManager.GetRaycastColorTexture());
            _raycastVisualizationMaterial.SetInt("_ScreenOrientation", (int)XRDisplayContext.GetScreenOrientation());
            _raycastVisualizationMaterial.SetTexture("_ArCameraTex", currentTexture);

            // Render with the visualization material
            Graphics.Blit(src, dest, _raycastVisualizationMaterial);

            Destroy(currentTexture);
        }
        else
        {
            Graphics.Blit(src, dest);
        }
    }

    private void OnDestroy()
    {
        if (_arCameraManager != null)
        {
            _arCameraManager.frameReceived -= OnARCameraFrameReceived;
        }

        while (_cameraTexturesQueue != null && _cameraTexturesQueue.Count > 0)
        {
            Destroy(_cameraTexturesQueue.Dequeue());
        }
    }
}
```

</div>

</div>

</div>

</div>

## Complete the Setup<a href="#complete-the-setup" class="hash-link" aria-label="Direct link to Complete the Setup" title="Direct link to Complete the Setup">​</a>

Now, assign the serialized fields to the ScanVisualization script component in the Inspector:

- Drag the **ScanningStripesMaterial** material from the Project window to the **Raycast Visualization Material** field.
- Drag the **Start Button** from the Canvas to the **Start Button** field.
- Drag the **Stop Button** from the Canvas to the **Stop Button** field.

![The components in the Inspector with the settings and serialized fields configured](https://www.nianticspatial.com/docs/assets/images/scan_visualization_components-a090d171a0cf1ae9570898827c8715ca.png)

## Try It Out<a href="#try-it-out" class="hash-link" aria-label="Direct link to Try It Out" title="Direct link to Try It Out">​</a>

Run the scene on your device or in the Unity Editor with [Playback](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/playback/) enabled. Tap the **Start** button to begin scanning. You should see diagonal stripes overlay the camera feed. As you scan different areas of the scene, those areas will transition from striped to full color, indicating successful scan coverage.

Tap the **Stop** button to end scanning and the visualization will disappear.

Try playing with the depth range in AR Scanning Manager to see how the visualization is affected.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

The visualization uses a small delay (2 frames) to synchronize with the camera image. This ensures the raycast data aligns properly with what the camera is seeing.

</div>

</div>

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

When using this with actual recording, call `SaveScan()` on the AR Scanning Manager before disabling it if you want to save the recorded data. See [How to Create Datasets for Playback](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/playback/create_playback_dataset/) for more information about saving scan recordings.

</div>

</div>

## Troubleshooting<a href="#troubleshooting" class="hash-link" aria-label="Direct link to Troubleshooting" title="Direct link to Troubleshooting">​</a>

### Visualization doesn't appear<a href="#visualization-doesnt-appear" class="hash-link" aria-label="Direct link to Visualization doesn&#39;t appear" title="Direct link to Visualization doesn&#39;t appear">​</a>

- Confirm the project's render pipeline. This sample only works with Built-in Render Pipeline. `OnRenderImage` is not invoked in URP projects.
- Ensure that **Enable Raycast Visualization** is checked in the AR Scanning Manager component.
- Verify that the `ScanVisualization` script is attached to the **Main Camera** GameObject and that all serialized fields are assigned.
- Check that the **ScanningStripesMaterial** uses the **Unlit/LightshipScanningStripes** shader.

Additionally, verify that depth is working:

- Ensure that depth data is available. If lidar is not available, verify that **Record Estimated Depth** is enabled. If using lidar, ensure that an **AR Occlusion Manager** is added to the Main Camera.
- Check that **Depth** is enabled in Niantic SDK Settings under XR Plug-in Management.

### Performance issues<a href="#performance-issues" class="hash-link" aria-label="Direct link to Performance issues" title="Direct link to Performance issues">​</a>

- The visualization requires processing each camera frame that's recorded. On lower-end devices, you may experience some performance impact during scanning.
- Consider reducing the **Recording Framerate** setting in AR Scanning Manager to reduce the compute load.
- Running other AR features such as meshing or device mapping in parallel can lead to CPU pressure. Consider reducing frame rate and fidelity settings in AR Mesh Manager when running in parallel with scanning.
- Setting a shallower depth range results in less compute.

</div>

</div>
