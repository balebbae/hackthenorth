---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/object_detection/
title: How to Enable Object Detection
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Enable Object Detection

</div>

Lightship Object Detection adds over 200 classes to the Lightship contextual awareness system, allowing for semantically-labeled 2D bounding boxes around objects in images. By providing bounding boxes and detection confidence levels, object detection adds a powerful dimension to your AR app by intelligently perceiving the material world around you.

This how-to will get you started with the feature by:

- Adding object detection to your scene
- Logging the objects seen by the camera
- Labeling objects on the screen in real time

For more details on the Object Detection classes, see the [Feature page](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/object_detection/).

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/object_detection_demo-751d5da9362fc5b650fe2b856d6dbe51.gif" width="400" alt="Object detection demonstration graphic" />

</div>

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Unity project with ARDK installed and a basic AR scene. For more information, see [Installing ARDK 3](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/) and [Setting up a Basic AR Scene](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/#setting-up-a-basic-ar-scene).

## Adding the AR Object Detection Manager<a href="#adding-the-ar-object-detection-manager" class="hash-link" aria-label="Direct link to Adding the AR Object Detection Manager" title="Direct link to Adding the AR Object Detection Manager">​</a>

To add the **AR Object Detection Manager**:

1.  Open the **Lightship** top menu, then select **XR Plug-in Management** and open the **Niantic Lightship SDK** menu. Make sure that Object Detection is enabled.

2.  In the **Hierarchy** of your [AR scene](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/#how-to-setup-an-ar-scene), expand the `XROrigin` and **Camera Offset**, then select **Main Camera**.

3.  In the **Inspector**, click **Add Component** and add an `AR Object Detection Manager` to the Main Camera.

    <img src="https://www.nianticspatial.com/docs/assets/images/obj_detection_manager-cea855b30ff25e3a9b981e3eb04a7e8f.png" width="500" alt="An AR Object Detection Manager added as a component of the Main Camera" />

## Printing the Results of Object Detection<a href="#printing-the-results-of-object-detection" class="hash-link" aria-label="Direct link to Printing the Results of Object Detection" title="Direct link to Printing the Results of Object Detection">​</a>

To see the data provided by Object Detection, register the `ObjectDetectionsUpdated` event. This outputs a callback when there are new object detection results. If object detection recognizes anything in the AR Camera image, the event will return a list of results, with each result corresponding to an area of the camera image. Each result may include more than one object category if Object Detection predicts multiple possible classifications for the object. You can filter and sort the results by their confidence values to focus on the most likely classifications.

To monitor the Object Detection output:

1.  In the **Hierarchy**, right click and select **Create Empty** to add a new `GameObject` to the scene. Name it `LogResults`.

    <img src="https://www.nianticspatial.com/docs/assets/images/hierarchy_log_results-429908a0a109fdde47c73c975fa0dea7.png" width="500" alt="LogResults in the scene hierarchy" />

2.  With `LogResults` selected, in the **Inspector**, click **Add Component** and add a **New Script**. Name it `LogResults`.

    <img src="https://www.nianticspatial.com/docs/assets/images/log_results_initial_inspector-27715db05de84d6bb1001e07e34b7772.png" width="500" alt="LogResults with the new script added" />

3.  Double-click `LogResults.cs` to open it.

4.  Add a serialized field for the `AR Object Detection Manager`. The manager takes care of the details about running the feature so that we can focus on the results.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using UnityEngine;
using Niantic.Lightship.AR.ObjectDetection;

public class LogResults : MonoBehaviour
{
    [SerializeField]
    private ARObjectDetectionManager _objectDetectionManager;
```

</div>

</div>

5.  When `Start()` runs, enable the manager and register the `OnMetadataInitialized` event. It will fire when Object Detection has started processing.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
    private void Start()
    {
        _objectDetectionManager.enabled = true;
        _objectDetectionManager.MetadataInitialized += OnMetadataInitialized;
    }
```

</div>

</div>

6.  When the feature is ready, register for the `ObjectDetectionsUpdated` event to automatically receive results.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
    private void OnMetadataInitialized(ARObjectDetectionModelEventArgs args)
    {
        _objectDetectionManager.ObjectDetectionsUpdated += ObjectDetectionsUpdated;
    }
```

</div>

</div>

7.  Create a function called `ObjectDetectionsUpdated()` to collect the results in a string and log them to the console.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
    private void ObjectDetectionsUpdated(ARObjectDetectionsUpdatedEventArgs args)
    {
        // Initialize our output string
        string resultString = "";
        var result = args.Results;

        if (result == null)
        {
            return;
        }

        // Reset our results string
        resultString = "";
```

</div>

</div>

8.  Loop through the results.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
        // Iterate through our results. Each result can contain more than one category.
        for (int i = 0; i < result.Count; i++)
        {
            var detection = result[i];
            var categorizations = detection.GetConfidentCategorizations();
            if (categorizations.Count <= 0)
            {
                break;
            }
```

</div>

</div>

<div class="theme-admonition theme-admonition-info admonition_xJq3 alert alert--info">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)</span>Filtering by Confidence

</div>

<div class="admonitionContent_BuS1">

Lightship Object Detection can produce a lot of results. To exclude lower-confidence categorizations, try passing a probability threshold to `GetConfidentCategorizations`. For example, `GetConfidentCategorizations(0.6)` will only return categorizations with a confidence score of **0.6** or above.

If no probability threshold is specified, the function defaults to filtering for a confidence score of **0.4**.

</div>

</div>

9.  Each result may contain more than one object category, so list them from highest to lowest confidence.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
            // Sort our categorizations by highest confidence
            categorizations.Sort((a, b) => b.Confidence.CompareTo(a.Confidence));

            // List each category that this object could be
            for (int j = 0; j < categorizations.Count; j++)
            {
                var categoryToDisplay = categorizations[j];

                resultString += "Detected " + $"{categoryToDisplay.CategoryName}: " + "with " + $"{categoryToDisplay.Confidence} Confidence \n";
            }
        }
```

</div>

</div>

10. Finally, log all the results and categories that we saw.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
        // Log all results
        Debug.Log(resultString);
    }
```

</div>

</div>

11. Don't forget to clean up at the end!

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
    private void OnDestroy()
    {
        _objectDetectionManager.MetadataInitialized -= OnMetadataInitialized;
        _objectDetectionManager.ObjectDetectionsUpdated -= ObjectDetectionsUpdated;
    }
```

</div>

</div>

Click to reveal the full `LogResults` script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using UnityEngine;
using Niantic.Lightship.AR.ObjectDetection;

public class LogResults : MonoBehaviour
{
    [SerializeField]
    private ARObjectDetectionManager _objectDetectionManager;

    private void Start()
    {
        _objectDetectionManager.enabled = true;
        _objectDetectionManager.MetadataInitialized += OnMetadataInitialized;
    }

    private void OnMetadataInitialized(ARObjectDetectionModelEventArgs args)
    {
        _objectDetectionManager.ObjectDetectionsUpdated += ObjectDetectionsUpdated;
    }

    private void ObjectDetectionsUpdated(ARObjectDetectionsUpdatedEventArgs args)
    {
        // Initialize our output string
        string resultString = "";
        var result = args.Results;

        if (result == null)
        {
            return;
        }

        // Reset our results string
        resultString = "";

        // Iterate through our results. Each result can contain more than one category.
        for (int i = 0; i < result.Count; i++)
        {
            var detection = result[i];
            var categorizations = detection.GetConfidentCategorizations();
            if (categorizations.Count <= 0)
            {
                break;
            }

            // Sort our categorizations by highest confidence
            categorizations.Sort((a, b) => b.Confidence.CompareTo(a.Confidence));

            // List each category that this object could be
            for (int j = 0; j < categorizations.Count; j++)
            {
                var categoryToDisplay = categorizations[j];

                resultString += "Detected " + $"{categoryToDisplay.CategoryName}: " + "with " + $"{categoryToDisplay.Confidence} Confidence \n";
            }
        }

        // Log all results
        Debug.Log(resultString);
    }

    private void OnDestroy()
    {
        _objectDetectionManager.MetadataInitialized -= OnMetadataInitialized;
        _objectDetectionManager.ObjectDetectionsUpdated -= ObjectDetectionsUpdated;
    }
}
```

</div>

</div>

</div>

</div>

## Adding the Finished Script to Your Project<a href="#adding-the-finished-script-to-your-project" class="hash-link" aria-label="Direct link to Adding the Finished Script to Your Project" title="Direct link to Adding the Finished Script to Your Project">​</a>

1.  Select `LogResults` in the **Hierarchy**, then, in the **Inspector**, assign the **Main Camera** to the **Object Detection Manager** field of the `LogResults` Component.

    <img src="https://www.nianticspatial.com/docs/assets/images/log_results_final_inspector-e0fdbcdd4756884d7a282fd9f05cb945.png" width="500" alt="LogResults with the Object Detection Manager field assigned" />

2.  Try running the scene with a [playback dataset](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/playback/setting_up_playback/) in the Unity Editor or on a mobile device with the logging console connected. Object Detection should show you the classes and confidence values it detects in your camera feed.

    <img src="https://www.nianticspatial.com/docs/assets/images/log_results_result-a95bea63a4257a51bbf4b093f0fbc0ce.png" width="500" alt="The console output after running object detection on a dataset in the Editor" />

## Setting Up the Bounding Boxes<a href="#setting-up-the-bounding-boxes" class="hash-link" aria-label="Direct link to Setting Up the Bounding Boxes" title="Direct link to Setting Up the Bounding Boxes">​</a>

By creating an overlay to display bounding boxes, we can show the object detection results live on-screen. Each bounding box is defined by its coordinates, which refer to its top-left corner, and its size, which it gets from the object detection code. We will place this overlay over the AR Camera Background and create a prefab that we can reuse to display multiple bounding boxes at once.

1.  In the **Hierarchy**, right-click in the main scene, then mouse over **UI** and select **Canvas**.

2.  With Canvas selected, in the **Inspector**, find the **Canvas Scalar** Component. Set the **UI Scale Mode** to **Select Scale With Screen Size** and set **Match** to **0.5**.

    <img src="https://www.nianticspatial.com/docs/assets/images/canvas-be12d4d1280df56e7d80e33066f48b48.png" width="500" alt="Canvas with fields configured" />

3.  In the **Hierarchy**, right-click on **Canvas** and select **Create Empty**. Name the new object `BoundingBoxOverlay`.

    <img src="https://www.nianticspatial.com/docs/assets/images/hierarchy_0-15c69899873f17097876108ded07087d.png" width="500" alt="BoundingBoxOverlay in the hierarchy" />

4.  With `BoundingBoxOverlay` selected, in the **Inspector**, set the `Rect Transform` **Anchor Presets** to **Stretch** for both axes while holding **Shift** and **Alt** to also set the pivot and position.

    <img src="https://www.nianticspatial.com/docs/assets/images/bounding_box_overlay_anchors-9a87bcb7a8053573950ac671d9127105.png" width="500" alt="Setting the Anchor Presets of BoundingBoxOverlay to stretch for X and Y" />

    1.  After setting the **Anchor Presets** to **Stretch**, re-zero the `Left`, `Right`, `Top`, and `Bottom` positioning fields in the `Rect Transform` if those have changed.

5.  Create a bounding box prefab:

    1.  In the **Hierarchy**, right-click on `BoundingBoxOverlay` and select **Create Empty**. Name the new object `RectObject`.

        <img src="https://www.nianticspatial.com/docs/assets/images/hierarchy_1a-9854f0e8712bb276af13ceddd7581156.png" width="500" alt="RectObject in the hierarchy" />

    2.  With `RectObject` selected, in the **Inspector**, set the `Rect Transform` **Anchor Presets** to **Bottom-Left**.

    3.  Set the Rect Transform's **Pivot** to X:**0**, Y:**1**.

    4.  Set the positional values as follows:

        - Pos X: **0**
        - Pos Y: **1920**
        - Pos Z: **0**
        - Width: **1080**
        - Height: **1920**

    5.  Click **Add Component** and add an **Image** component to `RectObject`.

    6.  In the **Source Image** field, open the search box to search for an asset. Find and select the `Background` asset (this is a built-in asset under `Resources/unity_builtin_extra/`).

    7.  Uncheck **Fill Center**.

    8.  Click **Add Component** and add a **New script** to `RectObject`. Name the script **UIRectObject**.

        <img src="https://www.nianticspatial.com/docs/assets/images/rect_object-515cb1edbddab9c1cf904a0cfa99becf.png" width="500" alt="RectObject with fields configured" />

    9.  Double-click the `UIRectObject` script to open it. Replace the contents with the following code to make sure the bounding box frames the object:

    Click to reveal the bounding box code

    <div>

    <div class="collapsibleContent_i85q">

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    using System;
    using System.Collections;
    using System.Collections.Generic;
    using UnityEditor;
    using UnityEngine;
    using UnityEngine.UI;

    [RequireComponent(typeof(RectTransform), typeof(Image))]
    public class UIRectObject : MonoBehaviour
    {
        private RectTransform _rectangleRectTransform;
        private Image _rectangleImage;
        private Text _text;

        public void Awake()
        {
            _rectangleRectTransform = GetComponent<RectTransform>();
            _rectangleImage = GetComponent<Image>();
            _text = GetComponentInChildren<Text>();
        }

        public void SetRectTransform(Rect rect)
        {
            _rectangleRectTransform.anchoredPosition = new Vector2(rect.x, rect.y);
            _rectangleRectTransform.sizeDelta = new Vector2(rect.width, rect.height);
        }

        public void SetColor(Color color)
        {
            _rectangleImage.color = color;
        }

        public void SetText(string text)
        {
            _text.text = text;
        }

        public RectTransform getRectTransform(){
            return _rectangleRectTransform;
        }
    }
    ```

    </div>

    </div>

    </div>

    </div>

    10. In the **Hierarchy**, right-click on `RectObject` and select **Create Empty**. Name the new object `Category Text`.

    <img src="https://www.nianticspatial.com/docs/assets/images/hierarchy_1b-50aa797db736dd28269491d8a114999a.png" width="500" alt="Category Text in the hierarchy" />

    11. In the **Inspector**, set the Rect Transform **Anchor Presets** to **Stretch** while holding **Shift** and **Alt** to also set the pivot and position.

    12. Set the **Height** to **400**.

    13. Click **Add Component** to add a **Text** component to `Category Text`.

    14. In the **Text** field, add filler text such as `Label: Prob`.

    15. Set the **Alignment** to horizontally and vertically centered. Check **Best Fit** and set **Max Size** to **100**. Set the **Color** to green.

        <img src="https://www.nianticspatial.com/docs/assets/images/category_text-98857c43219948c8afe8061c11df6154.png" width="500" alt="Category Text with fields configured" />

    16. In the **Project** tab, right-click in the **Assets** directory, then open the **Create** menu and select **Folder**. Name it `Prefabs`.

    17. Drag the `RectObject` game object from the **Inspector** to the **Prefab** directory in the **Project** tab to create a prefab of the bounding box.

        <img src="https://www.nianticspatial.com/docs/assets/images/prefab-7d604c8054c83b60ddf04229d157a651.png" width="500" alt="The final RectObject prefab in the Project tab" />

6.  In the **Hierarchy**, select `BoundingBoxOverlay`, then, in the **Inspector**, click **Add Component** and select **New Script**. Name the script `DrawRect`.

7.  Double-click the `DrawRect` script to open it.

8.  Add a `SerializedField` for the type of prefab that we'll instantiate for each object detected. We'll cache them in a pool to improve performance.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
public class DrawRect : MonoBehaviour
{
    [SerializeField]
    private GameObject _rectanglePrefab;

    private List<UIRectObject> _rectangleObjects = new List<UIRectObject>();
    private List<int> _openIndices = new List<int>();
```

</div>

</div>

9.  Add a function to create a new bounding box and add it to a pool. We keep a pool of prefabs and reuse them to avoid repeated allocations.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
    public void CreateRect(Rect rect, Color color, string text)
    {
        if (_openIndices.Count == 0)
        {
            var newRect = Instantiate(_rectanglePrefab, parent: this.transform).GetComponent<UIRectObject>();

            _rectangleObjects.Add(newRect);
            _openIndices.Add(_rectangleObjects.Count - 1);
        }

        // Treat the first index as a queue
        int index = _openIndices[0];
        _openIndices.RemoveAt(0);

        UIRectObject rectangle = _rectangleObjects[index];
        rectangle.SetRectTransform(rect);
        rectangle.SetColor(color);
        rectangle.SetText(text);
        rectangle.gameObject.SetActive(true);
    }
```

</div>

</div>

10. Add a function to hide all of the bounding boxes and return them to the pool for the next prediction result.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
    public void ClearRects()
    {
        for (var i = 0; i < _rectangleObjects.Count; i++)
        {
            _rectangleObjects[i].gameObject.SetActive(false);
            _openIndices.Add(i);
        }
    }
```

</div>

</div>

Click to reveal the full `DrawRect` script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DrawRect : MonoBehaviour
{
    [SerializeField]
    private GameObject _rectanglePrefab;

    private List<UIRectObject> _rectangleObjects = new List<UIRectObject>();
    private List<int> _openIndices = new List<int>();

    public void CreateRect(Rect rect, Color color, string text)
    {
        if (_openIndices.Count == 0)
        {
            var newRect = Instantiate(_rectanglePrefab, parent: this.transform).GetComponent<UIRectObject>();

            _rectangleObjects.Add(newRect);
            _openIndices.Add(_rectangleObjects.Count - 1);
        }

        // Treat the first index as a queue
        int index = _openIndices[0];
        _openIndices.RemoveAt(0);

        UIRectObject rectangle = _rectangleObjects[index];
        rectangle.SetRectTransform(rect);
        rectangle.SetColor(color);
        rectangle.SetText(text);
        rectangle.gameObject.SetActive(true);
    }

    public void ClearRects()
    {
        for (var i = 0; i < _rectangleObjects.Count; i++)
        {
            _rectangleObjects[i].gameObject.SetActive(false);
            _openIndices.Add(i);
        }
    }
}
```

</div>

</div>

</div>

</div>

11. In the **Hierarchy**, delete `RectObject`. `BoundingBoxOverlay` should now have no child objects. `RectObject`s will be dynamically placed by the script in the next section.

    <img src="https://www.nianticspatial.com/docs/assets/images/hierarchy_1-989dbf6e1ada71cd17082c8e962e9a94.png" width="500" alt="The Hierarchy after deleting the original RectObject" />

12. In the **Inspector**, assign the **RectObject** prefab to the **Rectangle Prefab** field of the `DrawRect` component.

    <img src="https://www.nianticspatial.com/docs/assets/images/bounding_box_overlay_final-0970c4cce6cc325c6f238806b21e3982.png" width="500" alt="The final BoundingBoxOverlay" />

## Adding the Bounding Box Detection Script<a href="#adding-the-bounding-box-detection-script" class="hash-link" aria-label="Direct link to Adding the Bounding Box Detection Script" title="Direct link to Adding the Bounding Box Detection Script">​</a>

The last task is to write a script that passes the results from the Lightship Object Detection feature to the bounding box overlay. This script is similar to the `LogResults` class that we wrote earlier, but to save on display space, this class will only label the most confident categorization for each result.

1.  In the **Hierarchy**, right click and select **Create Empty** to create a new game object in the scene. Name it `Sample`.

    <img src="https://www.nianticspatial.com/docs/assets/images/hierarchy_2-4bae1b2faa65f665be1f4da74b36eb5a.png" width="500" alt="Sample in the scene hierarchy" />

2.  With `Sample` selected, in the **Inspector**, click **Add Component** and add a **New Script**. Name it `ObjectDetectionSample`.

3.  Double-click the `ObjectDetectionSample` script to open it.

4.  Add fields for the detection threshold, the `AR Object Detection Manager` and the classes that display the bounding boxes on the screen:

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
public class ObjectDetectionSample: MonoBehaviour
{
    [SerializeField]
    private float _probabilityThreshold = 0.5f;

    [SerializeField]
    private ARObjectDetectionManager _objectDetectionManager;

    private Color[] _colors = new Color[]
    {
        Color.red,
        Color.blue,
        Color.green,
        Color.yellow,
        Color.magenta,
        Color.cyan,
        Color.white,
        Color.black
    };

    [SerializeField]
    private DrawRect _drawRect;

    private Canvas _canvas;
```

</div>

</div>

5.  Add functions for the initialization and de-initialization lifecycle. When the `AR Object Detection Manager` has new object detection results, the new `ObjectDetectionsUpdated` function will be called with the latest results.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
    private void Awake()
    {
        _canvas = FindObjectOfType<Canvas>();
    }

    public void Start()
    {
        _objectDetectionManager.enabled = true;
        _objectDetectionManager.MetadataInitialized += OnMetadataInitialized;
    }

    private void OnDestroy()
    {
        _objectDetectionManager.MetadataInitialized -= OnMetadataInitialized;
        _objectDetectionManager.ObjectDetectionsUpdated -= ObjectDetectionsUpdated;
    }

    private void OnMetadataInitialized(ARObjectDetectionModelEventArgs args)
    {
        _objectDetectionManager.ObjectDetectionsUpdated += ObjectDetectionsUpdated;
    }
```

</div>

</div>

6.  Next, we add `ObjectDetectionsUpdated` to connect the dots between the object detection results and what the user will see on screen. This function starts with clearing the frame of previous bounding box results.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
    private void ObjectDetectionsUpdated(ARObjectDetectionsUpdatedEventArgs args)
    {
        string resultString = "";
        float _confidence = 0;
        string _name = "";
        var result = args.Results;
        if (result == null)
        {
            return;
        }

        _drawRect.ClearRects();
```

</div>

</div>

7.  Loop over the results. Sometimes, a result will have several classifications at different confidence levels. For now, this function will display the one with the highest confidence value.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
        for (int i = 0; i < result.Count; i++)
        {
            var detection = result[i];
            var categorizations = detection.GetConfidentCategorizations(_probabilityThreshold);
            if (categorizations.Count <= 0)
            {
                break;
            }

            categorizations.Sort((a, b) => b.Confidence.CompareTo(a.Confidence));
            var categoryToDisplay = categorizations[0];
            _confidence = categoryToDisplay.Confidence;
            _name = categoryToDisplay.CategoryName;
```

</div>

</div>

8.  Once you have the most confident prediction for an object, convert its bounding box area to the viewport space with `CalculateRect`. In this example, the results are displayed on the `Canvas` that is aligned with the AR camera's background image. The `DrawRect` class from earlier activates a `RectObject` bounding box with the new location and label.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
            int h = Mathf.FloorToInt(_canvas.GetComponent<RectTransform>().rect.height);
            int w = Mathf.FloorToInt(_canvas.GetComponent<RectTransform>().rect.width);

            // Get the rect around the detected object
            var _rect = result[i].CalculateRect(w,h,Screen.orientation);

            resultString = $"{_name}: {_confidence}\n";
            // Draw the rect
            _drawRect.CreateRect(_rect, _colors[i % _colors.Length], resultString);
        }
```

</div>

</div>

Click to reveal the full `ObjectDetectionSample` script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using Niantic.Lightship.AR.ObjectDetection;
using UnityEngine;

public class ObjectDetectionSample: MonoBehaviour
{
    [SerializeField]
    private float _probabilityThreshold = 0.5f;

    [SerializeField]
    private ARObjectDetectionManager _objectDetectionManager;

    private Color[] _colors = new Color[]
    {
        Color.red,
        Color.blue,
        Color.green,
        Color.yellow,
        Color.magenta,
        Color.cyan,
        Color.white,
        Color.black
    };

    [SerializeField]
    private DrawRect _drawRect;

    private Canvas _canvas;

    private void Awake()
    {
        _canvas = FindObjectOfType<Canvas>();
    }

    public void Start()
    {
        _objectDetectionManager.enabled = true;
        _objectDetectionManager.MetadataInitialized += OnMetadataInitialized;
    }

    private void OnDestroy()
    {
        _objectDetectionManager.MetadataInitialized -= OnMetadataInitialized;
        _objectDetectionManager.ObjectDetectionsUpdated -= ObjectDetectionsUpdated;
    }

    private void OnMetadataInitialized(ARObjectDetectionModelEventArgs args)
    {
        _objectDetectionManager.ObjectDetectionsUpdated += ObjectDetectionsUpdated;
    }

    private void ObjectDetectionsUpdated(ARObjectDetectionsUpdatedEventArgs args)
    {
        string resultString = "";
        float _confidence = 0;
        string _name = "";
        var result = args.Results;
        if (result == null)
        {
            return;
        }

        _drawRect.ClearRects();

        for (int i = 0; i < result.Count; i++)
        {
            var detection = result[i];
            var categorizations = detection.GetConfidentCategorizations(_probabilityThreshold);
            if (categorizations.Count <= 0)
            {
                break;
            }

            categorizations.Sort((a, b) => b.Confidence.CompareTo(a.Confidence));
            var categoryToDisplay = categorizations[0];
            _confidence = categoryToDisplay.Confidence;
            _name = categoryToDisplay.CategoryName;

            int h = Mathf.FloorToInt(_canvas.GetComponent<RectTransform>().rect.height);
            int w = Mathf.FloorToInt(_canvas.GetComponent<RectTransform>().rect.width);

            // Get the rect around the detected object
            var _rect = result[i].CalculateRect(w,h,Screen.orientation);

            resultString = $"{_name}: {_confidence}\n";
            // Draw the rect
            _drawRect.CreateRect(_rect, _colors[i % _colors.Length], resultString);
        }
    }
}
```

</div>

</div>

</div>

</div>

9.  To complete the setup, assign objects to the `ObjectDetectionSample` component:

    1.  Assign the `Main Camera` to the **Object Detection Manager** field.
    2.  Assign `BoundingBoxOverlay` to the **Draw Rect** field.

    <img src="https://www.nianticspatial.com/docs/assets/images/sample_fields-a13aa0d221bec1c89577018b274c1bcd.png" width="500" alt="The Sample object with fields configured" />

## Example Result<a href="#example-result" class="hash-link" aria-label="Direct link to Example Result" title="Direct link to Example Result">​</a>

You should now be able to test Object Detection using [AR Playback](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/playback/setting_up_playback/) or on your mobile device and see bounding boxes overlaid onto suitable classes of objects.

<div class="theme-admonition theme-admonition-info admonition_xJq3 alert alert--info">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)</span>Probability Thresholds

</div>

<div class="admonitionContent_BuS1">

The default probability threshold is 0.5, meaning that the object detection algorithm will create a bounding box if it is at least 50% confident of a match. Try increasing the **Probability Threshold** in the **Object Detection Sample** component and see how the results change.

</div>

</div>

<img src="https://www.nianticspatial.com/docs/assets/images/final_result_example-64b2326a01b5cfabf3b8258ff7a4637e.png" width="500" alt="An example of object detection in action" />

</div>

</div>
