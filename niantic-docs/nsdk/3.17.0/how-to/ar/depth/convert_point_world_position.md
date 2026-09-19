---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/depth/convert_point_world_position/
title: How to Convert a Screen Point to Real-World Position Using Depth
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Convert a Screen Point to Real-World Position Using Depth

</div>

Niantic Spatial SDK's depth map output allows for dynamically placing objects in an AR scene without the use of planes or a mesh. This guide covers the process of choosing a point on the screen and placing an object in 3D space by using the depth output.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/depth_pick_howto-a63b5272dc3b2af545815c4c2c030000.gif" width="400" alt="Placing Cubes with Depth" />

</div>

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Unity project with Niantic Spatial AR enabled. For more information, see [Setting Up the Niantic SDK for Unity](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/).

<div class="theme-admonition theme-admonition-tip admonition_xJq3 alert alert--success">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)</span>tip

</div>

<div class="admonitionContent_BuS1">

If this is your first time using depth, [Accessing and Displaying Depth Information](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/depth/display_depth/) provides a simpler use case for depth and is easier to start with.

</div>

</div>

## Steps<a href="#steps" class="hash-link" aria-label="Direct link to Steps" title="Direct link to Steps">​</a>

If the main scene is not AR-ready, set it up:

1.  Remove the **Main Camera**.

2.  Add an **ARSession** and **XROrigin** to the Hierarchy, then add an **AR Occlusion Manager** Component to **XROrigin**. If you want higher quality occlusions, see [How to Set Up Real-World Occlusion](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/setup_real_world_occlusion/) to learn how to use the `LightshipOcclusionExtension`.

    <img src="https://www.nianticspatial.com/docs/assets/images/ARSessionXROrigin-8f4541a01d5131996058b444d27a31ec.png" width="450" alt="AR Session and XR Origin" /> <img src="https://www.nianticspatial.com/docs/assets/images/AROcclusionManager-7ecd781b12884ffb15d6668e79308db9.png" width="600" alt="AR Occlusion Manager" />

3.  Create a `MonoBehaviour` script that will handle depth picking and placing prefabs. Name it `Depth_ScreenToWorldPosition`.

4.  Add required namespaces to your script

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    using Niantic.Lightship.AR.Utilities;
    using UnityEngine;
    using UnityEngine.XR.ARFoundation;
    using UnityEngine.XR.ARSubsystems;
    ```

    </div>

    </div>

5.  Collect Depth Images on Update

    1.  Add a serialized `AROcclusionManager` and a private `XRCpuImage` field.

        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        [SerializeField]
        private AROcclusionManager _occlusionManager;

        private XRCpuImage? _depthImage;
        ```

        </div>

        </div>

    2.  Create a new method called `UpdateImage`:

        1.  Check that the `XROcclusionSubsystem` is valid and running.
        2.  Call `_occlusionManager.TryAcquireEnvironmentDepthCpuImage` to retrieve the latest depth image form the `AROcclusionManager`.
        3.  Dispose the old depth image and cache the new value.

        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        private void UpdateImage()
        {
            if (!_occlusionManager.subsystem.running)
            {
                return;
            }

            if (_occlusionManager.TryAcquireEnvironmentDepthCpuImage(out var image))
            {
                // Dispose the old image
                _depthImage?.Dispose();

                // Cache the new image
                _depthImage = image;
            }
        }
        ```

        </div>

        </div>

    3.  Invoke the `UpdateImage` method within the `Update` callback:

        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        private void Update()
        {
            UpdateImage();
        }
        ```

        </div>

        </div>

6.  Calculate the display matrix: Because depth images are oriented towards the sensor when surfaced from the Machine Learning model, they need to be sampled with respect to the current screen orientation. The display transform provides a mapping to convert from screen space to the image coordinate system. We use `XRCpuImage` instead of a GPU Texture so that the `Sample(Vector2 uv, Matrix4x4 transform)` method can be used on the CPU.

    1.  Add a private `Matrix4x4` and a `ScreenOrientation` field.
        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        private Matrix4x4 _displayMatrix;
        private ScreenOrientation? _latestScreenOrientation;
        ```

        </div>

        </div>
    2.  Create a new method called `UpdateDisplayMatrix`.
    3.  Check that the script has a valid `XRCpuImage` cached.
    4.  Check if the matrix needs to be recalculated by testing whether the screen orientation has changed.
    5.  Call `CameraMath.CalculateDisplayMatrix` to calculate a matrix that transforms the screen coordinates to image coordinates.

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    private void UpdateDisplayMatrix()
    {
        // Make sure we have a valid depth image
        if (_depthImage is {valid: true})
        {
            // The display matrix only needs to be recalculated if the screen orientation changes
            if (!_latestScreenOrientation.HasValue ||
                _latestScreenOrientation.Value != XRDisplayContext.GetScreenOrientation())
            {
                _latestScreenOrientation = XRDisplayContext.GetScreenOrientation();
                _displayMatrix = CameraMath.CalculateDisplayMatrix(
                    _depthImage.Value.width,
                    _depthImage.Value.height,
                    Screen.width,
                    Screen.height,
                    _latestScreenOrientation.Value,
                    invertVertically: true);
            }
        }
    }
    ```

    </div>

    </div>

    1.  Invoke the `UpdateDisplayMatrix` method within the `Update` callback:

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    private void Update()
    {
        ...
        UpdateDisplayMatrix();
    }
    ```

    </div>

    </div>

7.  Set up code to Handle Touch Inputs:

    1.  Create a private Method named "HandleTouch".
    2.  In editor, we'll use "Input.MouseDown" to detect mouse clicks.
    3.  For phone, the "Input.GetTouch"
    4.  Then, get the 2D screenPosition Coordinates from the device.

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    private void HandleTouch()
    {
        // in the editor we want to use mouse clicks, on phones we want touches.
    #if UNITY_EDITOR
            if (Input.GetMouseButtonDown(0) || Input.GetMouseButtonDown(1) || Input.GetMouseButtonDown(2))
            {
                var screenPosition = new Vector2(Input.mousePosition.x, Input.mousePosition.y);
    #else
            //if there is no touch or touch selects UI element
            if (Input.touchCount <= 0)
                return;
            var touch = Input.GetTouch(0);

            // only count touches that just began
            if (touch.phase == UnityEngine.TouchPhase.Began)
            {
                var screenPosition = touch.position;
    #endif
                // do something with touches
            }
        }
    }
    ```

    </div>

    </div>

8.  Convert touch points from the screen to 3D Coordinates using Depth

    1.  In the HandleTouch method, check for a valid depth image when a touch is detected.

        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
            // do something with touches
            if (_depthImage.HasValue)
            {
                // 1. Sample eye depth

                // 2. Get world position

                // 3. Spawn a thing on the depth map
            }
        ```

        </div>

        </div>

    2.  Sample the depth image at the screenPosition to get the z-value

        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        // 1. Sample eye depth
        var uv = new Vector2(screenPosition.x / Screen.width, screenPosition.y / Screen.height);
        var eyeDepth = _depthImage.Value.Sample<float>(uv, _displayMatrix);
        ```

        </div>

        </div>

    3.  Add a `Camera` field to the top of script:

        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        [SerializeField]
        private Camera _camera;
        ```

        </div>

        </div>

    4.  This will use Unity's <a href="https://docs.unity3d.com/ScriptReference/Camera.ScreenToWorldPoint.html" target="_blank" rel="noopener noreferrer"><code>Camera.ScreenToWorldPoint</code></a> function. Call the method in "HandleTouch" to convert screenPosition and eyeDepth to worldPositions.

        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        // 2. Get world position
        var worldPosition =
            _camera.ScreenToWorldPoint(new Vector3(screenPosition.x, screenPosition.y, eyeDepth));
        ```

        </div>

        </div>

    5.  Spawn a GameObject at this location in world space:

    6.  Add a `GameObject` field to the top of the script:

        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        [SerializeField]
        private GameObject _prefabToSpawn;
        ```

        </div>

        </div>

    7.  Instantiate a copy of this prefab at this position:

        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        // 3. Spawn a thing on the depth map
        Instantiate(_prefabToSpawn, worldPosition, Quaternion.identity);
        ```

        </div>

        </div>

9.  Add `HandleTouch` to the end of the `Update` method.

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
        private void HandleTouch()
        {
            // in the editor we want to use mouse clicks, on phones we want touches.
    #if UNITY_EDITOR
            if (Input.GetMouseButtonDown(0) || Input.GetMouseButtonDown(1) || Input.GetMouseButtonDown(2))
            {
                var screenPosition = new Vector2(Input.mousePosition.x, Input.mousePosition.y);
    #else
            //if there is no touch or touch selects UI element
            if (Input.touchCount <= 0)
                return;
            var touch = Input.GetTouch(0);

            // only count touches that just began
            if (touch.phase == UnityEngine.TouchPhase.Began)
            {
                var screenPosition = touch.position;
    #endif
                // do something with touches
                if (_depthImage.HasValue)
                {
                    // Sample eye depth
                    var uv = new Vector2(screenPosition.x / Screen.width, screenPosition.y / Screen.height);
                    var eyeDepth = _depthImage.Value.Sample<float>(uv, _displayMatrix);
                    
                    // Get world position
                    var worldPosition =
                        _camera.ScreenToWorldPoint(new Vector3(screenPosition.x, screenPosition.y, eyeDepth));
                    
                    //spawn a thing on the depth map
                    Instantiate(_prefabToSpawn, worldPosition, Quaternion.identity);
                }
            }
        }
    ```

    </div>

    </div>

10. Add the `Depth_ScreenToWorldPosition` script as a Component of the `XROrigin` in the **Hierarchy**:

    1.  In the **Hierarchy** window, select the `XROrigin`, then click **Add Component** in the **Inspector**.
    2.  Search for the `Depth_ScreenToWorldPosition` script, then select it.

11. Create a **Cube** to use as the object that will spawn into the scene:

    1.  In the **Hierarchy**, right-click, then, in the **Create** menu, mouse over **3D Object** and select **Cube**.
    2.  In the **Inspector**, scale the **Cube** object down from (1, 1, 1) to (0.75, 0.75, 0.75).
    3.  Drag the new **Cube** object from the **Hierarchy** to the **Assets** window to create a prefab of it, then delete it from the **Hierarchy**. (The **Cube** in the **Assets** window should remain.)

12. Assign the fields in the `Depth_ScreenToWorldPosition` script:

    1.  In the **Hierarchy** window, select the `XROrigin`, then expand the `Depth_ScreenToWorldPosition` Component in the **Inspector** window.
    2.  Assign the `XROrigin` to the **AROcclusionManager** field.
    3.  Assign the **Main Camera** to the **Camera** field.
    4.  Assign your new **Cube** prefab to the **Prefab to Spawn** field.

    <img src="https://www.nianticspatial.com/docs/assets/images/depth_picker_script_editor-dadea3b7604113ee33ec3c7ce515adf8.png" width="600" alt="Depth_ScreenToWorldPosition editor properties" />

13. Try running the scene in-editor using [Playback](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/playback/setting_up_playback/) or open **Build Settings**, then click **Build and Run** to build to device.

    <div style="text-align:center">

    <img src="https://www.nianticspatial.com/docs/assets/images/depth_picker_playback-5b0a7b430c25c662eef2bc8a67c465fd.gif" width="400" alt="Placing Cubes with Depth" />

    </div>

14. If something did not work, double check the steps above and compare your script to the one below.

Click to show the Depth_ScreenToWorldPosition script

<div>

<div class="collapsibleContent_i85q">

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
using Niantic.Lightship.AR.Utilities;
using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;

public class Depth_ScreenToWorldPosition : MonoBehaviour
{
    [SerializeField]
    private AROcclusionManager _occlusionManager;

    [SerializeField]
    private Camera _camera;

    [SerializeField]
    private GameObject _prefabToSpawn;

    private Matrix4x4 _displayMatrix;
    private XRCpuImage? _depthImage;
    private ScreenOrientation? _latestScreenOrientation;

    private void Update()
    {
        UpdateImage();
        UpdateDisplayMatrix();
        HandleTouch();
    }

    private void OnDestroy()
    {
        // Dispose the cached depth image
        _depthImage?.Dispose();
    }

    private void UpdateImage()
    {
        if (!_occlusionManager.subsystem.running)
        {
            return;
        }

        if (_occlusionManager.TryAcquireEnvironmentDepthCpuImage(out var image))
        {
            // Dispose the old image
            _depthImage?.Dispose();

            // Cache the new image
            _depthImage = image;
        }
    }

    private void UpdateDisplayMatrix()
    {
        // Make sure we have a valid depth image
        if (_depthImage is {valid: true})
        {
            // The display matrix only needs to be recalculated if the screen orientation changes
            if (!_latestScreenOrientation.HasValue ||
                _latestScreenOrientation.Value != XRDisplayContext.GetScreenOrientation())
            {
                _latestScreenOrientation = XRDisplayContext.GetScreenOrientation();
                _displayMatrix = CameraMath.CalculateDisplayMatrix(
                    _depthImage.Value.width,
                    _depthImage.Value.height,
                    Screen.width,
                    Screen.height,
                    _latestScreenOrientation.Value,
                    invertVertically: true);
            }
        }
    }

    private void HandleTouch()
    {
        // In the editor we want to use mouse clicks, on phones we want touches.
#if UNITY_EDITOR
        if (Input.GetMouseButtonDown(0) || Input.GetMouseButtonDown(1) || Input.GetMouseButtonDown(2))
        {
            var screenPosition = new Vector2(Input.mousePosition.x, Input.mousePosition.y);
#else
        // If there is no touch or touch selects UI element
        if (Input.touchCount <= 0)
            return;
        var touch = Input.GetTouch(0);

        // Only count touches that just began
        if (touch.phase == UnityEngine.TouchPhase.Began)
        {
            var screenPosition = touch.position;
#endif
            // Do something with touches
            if (_depthImage is {valid: true})
            {
                // Sample eye depth
                var uv = new Vector2(screenPosition.x / Screen.width, screenPosition.y / Screen.height);
                var eyeDepth = _depthImage.Value.Sample<float>(uv, _displayMatrix);

                // Get world position
                var worldPosition =
                    _camera.ScreenToWorldPoint(new Vector3(screenPosition.x, screenPosition.y, eyeDepth));

                // Spawn a thing on the depth map
                Instantiate(_prefabToSpawn, worldPosition, Quaternion.identity);
            }
        }
    }
}
```

</div>

</div>

</div>

</div>

## More Information<a href="#more-information" class="hash-link" aria-label="Direct link to More Information" title="Direct link to More Information">​</a>

- [Depth Feature page](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/depth/)
- [Occlusion Feature page](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/occlusion/)

You can also try combining this guide with [Object Detection](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/object_detection/) or [Scene Segmentation](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/semantics/) to know where things are in 3D space.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/depth_picker_object_detection-0d08ec0223cfeed8f945c8a2a4c04bd4.png" width="500" alt="Placing Cubes with Depth and Object Detection" />

</div>

</div>

</div>
