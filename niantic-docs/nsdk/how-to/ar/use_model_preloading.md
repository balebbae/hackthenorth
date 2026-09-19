---
source: https://www.nianticspatial.com/docs/nsdk/how-to/ar/use_model_preloading/
title: How to Use Neural Network Model Preloading
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Use Neural Network Model Preloading

</div>

Meshing, depth & occlusion, and scene segmentation use neural network models to process the camera frames. To improve runtime performance, [Model Preloading](https://www.nianticspatial.com/docs/nsdk/features/model_preloading/) allows you to download model files ahead of time, frontloading the installation process and avoiding just-in-time loading delays that can negatively impact the user experience.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/howto_model_preload-ea735fa95e28e89bd98422d4230241ba.gif" width="400" alt="Preloading Sample Graphic" />

</div>

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

- You will need a Unity project with Niantic Spatial SDK AR enabled. For more information, see [Set up the Niantic SDK for Unity](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-the-niantic-sdk-for-unity).

## Neural Network Performance Modes<a href="#neural-network-performance-modes" class="hash-link" aria-label="Direct link to Neural Network Performance Modes" title="Direct link to Neural Network Performance Modes">​</a>

NSDK awareness features support a range of performance modes, allowing developers to select for performance, quality, or a balanced mix. These modes are analogous to the <a href="https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.0/api/UnityEngine.XR.ARSubsystems.EnvironmentDepthMode.html" target="_blank" rel="noopener noreferrer">Unity EnvironmentDepthMode values</a> used in the `XROcclusionSubsystem`.

For example, `Fast` optimizes for faster processing time at the expense of quality, while `Smooth` takes more time to deliver the best graphics. Each mode has its own neural network model file that can be preloaded before using AR features. For developers who want to supply their own neural network model file, `RegisterModel` allows for overriding the predefined NSDK models.

To request a feature mode, specify the feature and mode before starting the awareness feature:

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
DownloadModel(DepthMode.Medium);
DownloadModel(SemanticsMode.Smooth);
```

</div>

</div>

See `Runtime/Utilities/Preloading/Feature.cs` for the definitive list of feature modes.

## Preloading a Niantic Spatial Neural Network Model<a href="#preloading-a-niantic-spatial-neural-network-model" class="hash-link" aria-label="Direct link to Preloading a Niantic Spatial Neural Network Model" title="Direct link to Preloading a Niantic Spatial Neural Network Model">​</a>

To preload a neural network model file before starting an awareness feature:

1.  Determine which model you would like to preload based on your application's performance and quality needs.
2.  Decide when preloading will occur. Preloading can happen any time after AR Foundation has initialized the NSDK loader (when `XRGeneralSettings.Instance.Manager.isInitializationComplete` is true) and before awareness features have started. For example, if your AR script is a `MonoBehaviour`, preloading can happen during `Start()`.

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

Make sure there are no active AR Managers in the scene where you use preloading APIs. If an AR Manager is present, any associated models will download automatically.

</div>

</div>

<div class="theme-admonition theme-admonition-tip admonition_xJq3 alert alert--success">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)</span>Important!

</div>

<div class="admonitionContent_BuS1">

Model preloading APIs are only available during runtime after a Niantic Spatial AR session has started. If a model is not preloaded, awareness features will automatically choose one when starting.

</div>

</div>

1.  Set up a `Canvas` with UI Objects:

    1.  In the **Hierarchy**, right-click in the main scene, then open the **UI** menu and select **Canvas**.
    2.  Repeat this process four more times to add two `Button` and two `Text` objects. Customize their look in any way you want.

2.  Create an empty `GameObject` in the scene where preloading should occur:

    1.  In the **Hierarchy**, right-click the scene, then select **Create Empty**. Name the new `GameObject` **ModelPreloader**.

3.  Add a new script component to the empty:

    1.  Select **ModelPreloader** in the **Hierarchy**, then, in the **Inspector**, click **Add Component** and add a new script to it.

4.  At the top of the script, add serialized fields for the UI Objects:

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    [SerializeField]
    private Button _downloadButton;

    [SerializeField]
    private Button _clearButton;

    [SerializeField]
    private Text _progressPercentText;

    [SerializeField]
    private Text _statusText;
    ```

    </div>

    </div>

5.  Attach the GameObjects to the script in the **Inspector**:

    <img src="https://www.nianticspatial.com/docs/assets/images/howto_model_preloader_editor-9ba9e3495ee1843e3b2af53973a27de1.png" width="500" alt="Objects attached to the script" />

6.  Create a private preloader field, set a model feature to download, and add a bool to keep track of the state:

    1.  Instantiate the object with `ModelPreloaderFactory` in the `Start` method:

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    private IModelPreloader preloader;

    private DepthMode _depthMode = DepthMode.Medium;
    private bool _isDownloading = false;

    private void Start()
    {
        preloader = ModelPreloaderFactory.Create();

        if (null == preloader)
        {
            // Need to wait for XR to initialize before we can preload.
            // Defer preloader instantiation to a later function.
            return;
        }
    ```

    </div>

    </div>

7.  Call `ExistsInCache()` to check if the model already resides in the cache, then set the state of the scene.

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
        if (!preloader.ExistsInCache(_depthMode))
        {
            _statusText.text = $"{_depthMode} model not found in cache";
            _progressPercentText.text = "0%";
            _clearButton.interactable = false;
            _downloadButton.interactable = true;
        }
        else
        {
            // The model is already in the cache. No download is required.
            _statusText.text = $"{_depthMode} model found in cache";
            _progressPercentText.text = "100%";
            _clearButton.interactable = true;
            _downloadButton.interactable = false;
        }
    ```

    </div>

    </div>

8.  Create a `Download` method to have the preloader download the model:

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    private void DownloadModel()
    {
        preloader.DownloadModel(_depthMode);
        _isDownloading = true;
        _statusText.text = "Downloading model...";
        _progressPercentText.text = "0%";
        _clearButton.interactable = false;
        _downloadButton.interactable = false;
    }
    ```

    </div>

    </div>

9.  Add a `ClearCache` method to delete the downloaded model:

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    private void ClearCache()
    {
        preloader.ClearFromCache(_depthMode);
        _statusText.text = $"{_depthMode} model cleared from cache";
        _progressPercentText.text = "0%";
        _clearButton.interactable = false;
        _downloadButton.interactable = true;
    }
    ```

    </div>

    </div>

10. Attach `onClick` listeners to the buttons to call their corresponding methods:

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    private void OnEnable()
    {
        _downloadButton.onClick.AddListener(DownloadModel);
        _clearButton.onClick.AddListener(ClearCache);
    }

    private void OnDisable()
    {
        _downloadButton.onClick.RemoveListener(DownloadModel);
        _clearButton.onClick.RemoveListener(ClearCache);
    }
    ```

    </div>

    </div>

11. If you want to display download progress to the user, periodically call `CurrentProgress()`. When `progress` is `1.0`, model preloading is complete. For example:

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    private void Update()
    {
        if (!_isDownloading)
        {
            return;
        }
        
        var statusCode = preloader.CurrentProgress(_depthMode, out float progress);
        if (Mathf.Approximately(progress, 1.0f))
        {
            // The download has completed successfully, or the model was already in the cache
            _statusText.text = $"{_depthMode} model downloaded successfully";
            _progressPercentText.text = "100%";
            _clearButton.interactable = true;
            _downloadButton.interactable = false;
            _isDownloading = false;
            return;
        }
        
        if (statusCode != PreloaderStatusCode.RequestInProgress)
        {
            // The download is not in progress
            _statusText.text = $"Current status: {statusCode}";
            _isDownloading = false;
            return;
        }
        
        _progressPercentText.text = $"{progress * 100.0f}%";
    }
    ```

    </div>

    </div>

12. Test the scene in the Unity Editor and double-check the steps above if something doesn't work.

### Full Example Model Preloading Script<a href="#full-example-model-preloading-script" class="hash-link" aria-label="Direct link to Full Example Model Preloading Script" title="Direct link to Full Example Model Preloading Script">​</a>

Click here to expand the example script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using NianticSpatial.NSDK.AR.Utilities.Preloading;
using UnityEngine;
using UnityEngine.UI;

public class ModelPreloader : MonoBehaviour
{
    [SerializeField]
    private Button _downloadButton;
    
    [SerializeField]
    private Button _clearButton;
    
    [SerializeField]
    private Text _progressPercentText;
    
    [SerializeField]
    private Text _statusText;
    
    private IModelPreloader preloader;
    
    private DepthMode _depthMode = DepthMode.Medium;
    private bool _isDownloading = false;
    
    private void Start()
    {
        preloader = ModelPreloaderFactory.Create();
        if (null == preloader)
        {
            // Need to wait for XR to initialize before we can preload.
            // Defer preloader instantiation to a later function.
            return;
        }
        
        if (!preloader.ExistsInCache(_depthMode))
        {
            _statusText.text = $"{_depthMode} model not found in cache";
            _progressPercentText.text = "0%";
            _clearButton.interactable = false;
            _downloadButton.interactable = true;
        }
        else
        {
            // The model is already in the cache. No download is required.
            _statusText.text = $"{_depthMode} model found in cache";
            _progressPercentText.text = "100%";
            _clearButton.interactable = true;
            _downloadButton.interactable = false;
        }
    }

    private void Update()
    {
        if (!_isDownloading)
        {
            return;
        }
        
        var statusCode = preloader.CurrentProgress(_depthMode, out float progress);
        if (Mathf.Approximately(progress, 1.0f))
        {
            // The download has completed successfully, or the model was already in the cache
            _statusText.text = $"{_depthMode} model downloaded successfully";
            _progressPercentText.text = "100%";
            _clearButton.interactable = true;
            _downloadButton.interactable = false;
            _isDownloading = false;
            return;
        }
        
        if (statusCode != PreloaderStatusCode.RequestInProgress)
        {
            // The download is not in progress
            _statusText.text = $"Current status: {statusCode}";
            _isDownloading = false;
            return;
        }
        
        _progressPercentText.text = $"{progress * 100.0f}%";
    }
    
    private void OnEnable()
    {
        _downloadButton.onClick.AddListener(DownloadModel);
        _clearButton.onClick.AddListener(ClearCache);
    }
    
    private void OnDisable()
    {
        _downloadButton.onClick.RemoveListener(DownloadModel);
        _clearButton.onClick.RemoveListener(ClearCache);
    }
    
    private void DownloadModel()
    {
        preloader.DownloadModel(_depthMode);
        _isDownloading = true;
        _statusText.text = "Downloading model...";
        _progressPercentText.text = "0%";
        _clearButton.interactable = false;
        _downloadButton.interactable = false;
    }
    
    private void ClearCache()
    {
        preloader.ClearFromCache(_depthMode);
        _statusText.text = $"{_depthMode} model cleared from cache";
        _progressPercentText.text = "0%";
        _clearButton.interactable = false;
        _downloadButton.interactable = true;
    }
}
```

</div>

</div>

</div>

</div>

## Registering a Local Model File<a href="#registering-a-local-model-file" class="hash-link" aria-label="Direct link to Registering a Local Model File" title="Direct link to Registering a Local Model File">​</a>

To avoid performing the expensive download process when starting an AR session, you may want to download the model files beforehand. To support this, ModelPreloader allows you to register local model files for any feature mode.

To register a local model file with NSDK:

1.  Ensure that the model file is in a location that your application can access.
2.  Create an empty `GameObject` in the scene where preloading should occur:
    1.  In the **Hierarchy**, right-click the scene, then select **Create Empty**. Name the new `GameObject` **ModelRegister**.
3.  Add a new script component to the empty:
    1.  Select the empty `GameObject` in the **Hierarchy**, then, in the **Inspector**, click **Add Component**, then add a new script.
4.  Determine which model you would like to preload based on your application's performance and quality needs.
5.  Decide when preloading will occur. Preloading can happen any time after AR Foundation has initialized the NSDK loader (when `XRGeneralSettings.Instance.Manager.isInitializationComplete` is true) and before awareness features have started. For example, if your AR script is a `MonoBehaviour`, preloading can happen during `Start()`.
6.  If an ARManager is present, any required models will automatically start to download when `OnEnable` is called.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

Registering a model for a feature mode will override that model for the rest of the AR session. The feature mode will be reset to default after the AR session ends.

</div>

</div>

1.  Instantiate a `ModelPreloader` object with `ModelPreloaderFactory`:

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    private bool TryInitializePreloader()
    {
        IModelPreloader preloader = ModelPreloaderFactory.Create();
        if (null == preloader)
        {
            // Need to wait for XR to initialize before we can preload.
            return false;
        }
    }
    ```

    </div>

    </div>

2.  Call `RegisterModel(Feature, FeatureMode, filepath)` to register the model with NSDK. This file must be accessible by the application and must remain in place for the duration of the AR session.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
var statusCode = preloader.RegisterModel(DepthMode.Medium, "/example/path/to/model_file");
if (statusCode is PreloaderStatusCode.Success or
                              PreloaderStatusCode.RequestInProgress or
                              PreloaderStatusCode.FileExistsInCache)
{
    // The model is now registered to the cache, or the model was already in the cache.
    // This will be the model used for NSDK's EnvironmentDepthMode.Medium moving forward.
}
```

</div>

</div>

## More Information<a href="#more-information" class="hash-link" aria-label="Direct link to More Information" title="Direct link to More Information">​</a>

Expanded Preloading sample with Multiple Model Downloads and Progress Bars:

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System;
using System.Collections.Generic;
using System.Linq;
using NianticSpatial.NSDK.AR.Utilities.Preloading;

using UnityEngine;
using UnityEngine.Serialization;
using UnityEngine.UI;
using UnityEngine.XR.Management;

public class PreloaderTestManager : MonoBehaviour
{
    [SerializeField]
    private Button _depthButton;

    [SerializeField]
    private Dropdown _depthDropdown;

    [SerializeField]
    private Button _semanticsButton;

    [SerializeField]
    private Dropdown _semanticsDropdown;

    [SerializeField]
    private Text _depthStatusText;

    [SerializeField]
    private Text _semanticsStatusText;

    [SerializeField]
    private Button _clearCacheButton;

    [SerializeField]
    private Text _preloadStatusText;

    [SerializeField]
    private Slider _percentageSlider;

    [SerializeField]
    private Text _percentageText;

    [SerializeField]
    private Text _cacheStatusText;

    [SerializeField]
    private string _localModelPath;

    private IModelPreloader _preloader;

    private DepthMode _depthMode;
    private SemanticsMode _semanticsMode;

    private void Start()
    {
        TryInitializePreloader();
        InitializeDropdownNames<DepthMode>(_depthDropdown);
        InitializeDropdownNames<SemanticsMode>(_semanticsDropdown);
    }

    private void OnDisable()
    {
        _preloader?.Dispose();
        _preloader = null;
    }

    private void InitializeDropdownNames<T>(Dropdown dropdown)
    {
        // Initialize the feature mode names in the dropdown menu.
        SetFeatureModeNames<T>(dropdown);
        dropdown.value = dropdown.options.Select(option => option.text).ToList().IndexOf("Medium");
    }

    private void SetFeatureModeNames<T>(Dropdown dropdown)
    {
        List<string> modeNames = new();
        foreach (var i in Enum.GetValues(typeof(T)))
        {
            var modeName = Enum.GetName(typeof(T), i);
            if (modeName != "Unspecified" && modeName != "Custom")
                modeNames.Add(modeName);
        }
        dropdown.AddOptions(modeNames);
    }

    private void Update()
    {
        if (_preloader == null && !TryInitializePreloader())
            return;

        UpdateDownloadProgress();
        UpdateCacheStatusText();
    }

    private bool TryInitializePreloader()
    {
        if (!XRGeneralSettings.Instance.Manager.isInitializationComplete)
        {
            // Need to wait for XR to initialize before we can preload
            return false;
        }

        _depthMode = DepthMode.Medium;
        _semanticsMode = SemanticsMode.Medium;

        _preloader = ModelPreloaderFactory.Create();

        if (null == _preloader)
        {
            // Need to wait for XR to initialize before we can preload
            return false;
        }

        _depthButton.onClick.AddListener
        (
            () =>
            {
                _depthMode = ParseFeatureMode<DepthMode>(_depthDropdown);
                PreloaderStatusCode result;

                if (_localModelPath.Length > 0)
                {
                    result =  _preloader.RegisterModel(_depthMode, _localModelPath);
                    _preloadStatusText.text = "Depth file registration: " +
                                              (IsError(result) ? "failed" : "success");
                }
                else
                {
                    result = _preloader.DownloadModel(_depthMode);
                    _preloadStatusText.text = IsError(result) ?
                                              "Depth download failed to start" :
                                              "Depth download starting";
                }
            }
        );

        _semanticsButton.onClick.AddListener
        (
            () =>
            {
                _semanticsMode = ParseFeatureMode<SemanticsMode>(_semanticsDropdown);
                PreloaderStatusCode result;

                if (_localModelPath.Length > 0)
                {
                    result =  _preloader.RegisterModel(_semanticsMode, _localModelPath);
                    _preloadStatusText.text = "Semantics file registration: " +
                                              (IsError(result) ? "failed" : "success");
                }
                else
                {
                    result = _preloader.DownloadModel(_semanticsMode);
                    _preloadStatusText.text = IsError(result) ?
                                              "Semantic segmentation download failed to start" :
                                              "Semantic segmentation download starting";
                }
            }
        );

        _clearCacheButton.onClick.AddListener
        (
            () =>
            {
                int successes = 0;
                if (_preloader.ClearFromCache(_depthMode))
                    successes++;

                if (_preloader.ClearFromCache(_semanticsMode))
                    successes++;

                _preloadStatusText.text = "Clear cache: " + successes + " successes";
            }
        );

        _depthDropdown.onValueChanged.AddListener
        (
            (int val) =>
            {
                var mode = val + (int) DepthMode.Fast; // We skip the 'unspecified' and 'custom' modes
                _depthMode = (DepthMode) mode;
            }
        );

        _semanticsDropdown.onValueChanged.AddListener
        (
            (int val) =>
            {
                var mode = val + (int) SemanticsMode.Fast; // We skip the 'unspecified' and 'custom' modes
                _semanticsMode = (SemanticsMode) mode;
            }
        );

        return true;
    }

    private static T ParseFeatureMode<T>(Dropdown dropdown)
    {
        var modeName = dropdown.options[dropdown.value].text;

        T mode = (T) Enum.Parse(typeof(T), modeName);
        return mode;
    }

    private void UpdateDownloadProgress()
    {
        // Display the progress of the feature modes that are selected with the dropdown menus
        var depthStatus = _preloader.CurrentProgress(_depthMode, out var selectedDepthProgress);
        if (IsError(depthStatus))
        {
            if (depthStatus == PreloaderStatusCode.RequestNotFound)
            {
                _depthStatusText.text = "0%";
            }
            else
            {
                _depthStatusText.text = "Failure: " + depthStatus;
                _preloadStatusText.text = "Download failure";
            }
        }
        else
        {
            _depthStatusText.text = (selectedDepthProgress * 100).ToString("0") + "%";
        }

        var semanticsStatus = _preloader.CurrentProgress(_semanticsMode, out var selectedSemanticsProgress);
        if (IsError(semanticsStatus))
        {
            if (semanticsStatus == PreloaderStatusCode.RequestNotFound)
            {
                _semanticsStatusText.text = "0%";
            }
            else
            {
                _semanticsStatusText.text = "Failure: " + semanticsStatus;
                _preloadStatusText.text = "Download failure";
            }
        }
        else
        {
            _semanticsStatusText.text = (selectedSemanticsProgress * 100).ToString("0") + "%";
        }

        // Summarize their download progress
        float combinedProgress = 0, activeDownloads = 0;
        if (selectedDepthProgress > 0 && selectedDepthProgress < 1)
        {
            combinedProgress += selectedDepthProgress;
            activeDownloads++;
        }

        if (selectedSemanticsProgress > 0 && selectedSemanticsProgress < 1)
        {
            combinedProgress += selectedSemanticsProgress;
            activeDownloads++;
        }

        float totalProgress = activeDownloads > 0 ? combinedProgress / activeDownloads : 0;
        _percentageText.text = (totalProgress * 100).ToString("0") + "%";
        _percentageSlider.value = totalProgress;
    }

    private void UpdateCacheStatusText()
    {
        // Cache status
        List<string> modeNames = new();
        DepthMode depthMode = new DepthMode();
        SemanticsMode semanticsMode = new SemanticsMode();
        string cacheStatusText = "Model files preloaded in cache: " + System.Environment.NewLine;

        // Update the cache status for all depth modes
        foreach (DepthMode i in Enum.GetValues(typeof(DepthMode)))
        {
            if (i == DepthMode.Unspecified || i == DepthMode.Custom)
                continue;

            depthMode = i;
            var present = _preloader.ExistsInCache(depthMode);

            if (present)
                modeNames.Add(Enum.GetName(typeof(DepthMode), i) + " Depth");
        }

        // Update the cache status for all semantics modes
        foreach (SemanticsMode i in Enum.GetValues(typeof(SemanticsMode)))
        {
            if (i == SemanticsMode.Unspecified || i == SemanticsMode.Custom)
                continue;

            semanticsMode = i;
            var present = _preloader.ExistsInCache(semanticsMode);

            if (present)
                modeNames.Add(Enum.GetName(typeof(SemanticsMode), i) + " Semantics");
        }

        // Summarize cache status
        for (int i = 0; i < modeNames.Count; i++)
        {
            cacheStatusText += modeNames[i] + (i < modeNames.Count - 1 ? ", " : "");
        }

        _cacheStatusText.text = cacheStatusText;
    }

    private static bool IsError(PreloaderStatusCode statusCode)
    {
        if (statusCode is PreloaderStatusCode.Success or
                            PreloaderStatusCode.RequestInProgress or
                            PreloaderStatusCode.FileExistsInCache)
            return false;

        return true;
    }
}
```

</div>

</div>

</div>

</div>

- [Neural Network Model Preloading feature page](https://www.nianticspatial.com/docs/nsdk/features/model_preloading/)

</div>

</div>
