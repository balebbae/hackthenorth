---
source: https://www.nianticspatial.com/docs/nsdk/how-to/playback/create_playback_dataset/
title: Create playback datasets
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Create playback datasets

</div>

## Introduction<a href="#unity-introduction" class="hash-link" aria-label="Direct link to Introduction" title="Direct link to Introduction">​</a>

Use NSDK Recording to capture camera, motion, and sensor data from an AR session. Export the recording as a playback dataset for repeatable testing in the Unity Editor.

The Unity sample project is Niantic's working C# reference app. Its Recording scene demonstrates a complete capture and export flow, and it provides a runnable AR scene for the API tutorial.

Start by [getting the sample project](#unity-get-the-sample-project), then choose one of these independent workflows:

- **[Recording sample](#unity-record-with-the-sample):** Use Niantic's existing Recording scene to create a dataset quickly.
- **[Recording API](#unity-record-with-the-api):** Build a separate tutorial component when you need control over the UI, capture state, archive creation, or sharing behavior.

You do not need to complete the Recording sample workflow before using the Recording API workflow.

In the Unity instructions:

- **Sample project** means Niantic's downloaded `nsdk-samples-csharp` project.
- **Recording sample** means the `Recording.unity` scene and its existing `RecordingDemo` component.
- **Tutorial component** means the `PlaybackCaptureController` you create.
- **Your app** means the Unity application where you will integrate the completed recording flow.

<span id="recording-formats"></span>

NSDK first saves a raw scan in the scan store. `ScanArchiveBuilder` then packages that saved scan into one or more `.tgz` playback archives. The raw scan is the source recording; the exported archives are the files you load with Playback.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/playback_howto_statue1-0d718ab613a83b41ede95c510ed7e13b.gif" width="300" alt="The first view of a statue recorded in a playback dataset" /><img src="https://www.nianticspatial.com/docs/assets/images/playback_howto_statue2-323e9ee1385c3945b179c0ec29d26359.gif" width="300" alt="A second view of the same statue recorded in the playback dataset" />

</div>

## Get the sample project<a href="#unity-get-the-sample-project" class="hash-link" aria-label="Direct link to Get the sample project" title="Direct link to Get the sample project">​</a>

Both workflows use the public <a href="https://github.com/nianticspatial/nsdk-samples-csharp" target="_blank" rel="noopener noreferrer"><code>nsdk-samples-csharp</code></a> repository. The published sample project is configured for Unity `6000.0.58f2`; install that Unity version with the Android or iOS build support module for your target device when you want to validate the sample without changing it.

Use the Unity editor version declared by the sample project when you want to run the downloaded sample without upgrading it first. Opening a Unity project with a newer editor can update project metadata, package files, or generated settings. Upgrade the project only when you intend to validate against that newer editor.

Get and open the sample source:

1.  In Terminal, clone the repository:

    <div class="language-bash codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` bash
    git clone https://github.com/nianticspatial/nsdk-samples-csharp.git
    ```

    </div>

    </div>

    Alternatively, select **Code \> Download ZIP** on GitHub, then extract the ZIP.

2.  In Unity Hub, select **Add \> Add project from disk**.

3.  Select `<download-location>/nsdk-samples-csharp/NsdkSamples`. The Unity project is in the `NsdkSamples` subdirectory, not at the repository root.

4.  Open the project with Unity `6000.0.58f2` and wait for package resolution and script compilation to finish.

5.  Authenticate NSDK before building:

    1.  In Unity's menu bar, select **NSDK \> Settings**.
    2.  Sign in to your Scaniverse account, or provide a developer token under **Edit \> Project Settings \> XR Plug-in Management \> Niantic Spatial Development Kit \> Credentials**.

For more information about choosing and configuring an authentication method, see [Authorization](https://www.nianticspatial.com/docs/nsdk/auth_getting_started/).

## Record with the Recording sample<a href="#unity-record-with-the-sample" class="hash-link" aria-label="Direct link to Record with the Recording sample" title="Direct link to Record with the Recording sample">​</a>

The Recording sample is the fastest way to create a playback dataset in Unity without building another recording interface.

### Prepare the Recording sample<a href="#unity-prepare-the-recording-sample" class="hash-link" aria-label="Direct link to Prepare the Recording sample" title="Direct link to Prepare the Recording sample">​</a>

1.  In the Project window, open `Assets/Samples/Scanning/Scenes/Recording.unity`.
2.  Configure the project for Android or iOS by following [Configure the build platform](https://www.nianticspatial.com/docs/nsdk/setup/#configure-the-build-platform).
3.  Select **File \> Build Profiles** and confirm that `Recording` is enabled in the scene list.
4.  Connect a supported physical device and select **Build and Run**.
5.  On the device, grant camera and location access when prompted.

The first iOS recording requires an internet connection while NSDK downloads a resource used to convert altitude data. Wait for initialization to finish before starting capture.

### Record the environment<a href="#unity-record-the-environment" class="hash-link" aria-label="Direct link to Record the environment" title="Direct link to Record the environment">​</a>

1.  Tap **Start**.
2.  Move the device through the environment in portrait orientation. Hold it steadily enough for AR tracking and record the area from several viewpoints.

After tapping **Start**, record the environment for several seconds before tapping **Stop**. The Recording sample does not expose its recorded frame count in the UI. The API workflow adds an explicit frame-count gate before saving.

### Stop and export<a href="#unity-sample-stop-and-export" class="hash-link" aria-label="Direct link to Stop and export" title="Direct link to Stop and export">​</a>

1.  Tap **Stop** after recording the environment.
2.  Wait for the save confirmation to appear, then tap **Save** to export the recording.
3.  Wait for **Exporting Completed**. Keep each `.tgz` path displayed in the export panel; a longer recording can produce more than one archive.
4.  Use [Retrieve and verify the recording](#unity-retrieve-and-verify-the-recording) to copy every archive and inspect its contents.

On iOS, you can also use **Share** to send a single exported archive to Files, AirDrop, or another app.

## Record with the API<a href="#unity-record-with-the-api" class="hash-link" aria-label="Direct link to Record with the API" title="Direct link to Record with the API">​</a>

The Unity API gives you control over the recording UI, capture state, frame-count gate, archive creation, and archive verification and sharing. This workflow uses a copy of Niantic's Recording scene as a runnable development environment. It creates a separate component and UI without replacing `RecordingDemo.cs`.

The API walkthrough contains these sections:

1.  [Capture implementation overview](#unity-capture-implementation-overview)
2.  [Prepare the tutorial scene](#unity-prepare-the-tutorial-scene)
3.  [Create PlaybackCaptureController](#unity-create-playback-capture-controller)
4.  [Add capture controls](#unity-add-capture-controls)
5.  [Start capture](#unity-start-capture)
6.  [Stop and save](#unity-stop-and-save)
7.  [Export the archives](#unity-export-the-archives)
8.  [Verify and share archives](#unity-verify-and-share-archives)
9.  [Retrieve and verify the recording](#unity-retrieve-and-verify-the-recording)
10. [View the complete PlaybackCaptureController](#unity-complete-playback-capture-controller)
11. [Add to your app](#unity-add-to-your-app)

------------------------------------------------------------------------

### Capture implementation overview<a href="#unity-capture-implementation-overview" class="hash-link" aria-label="Direct link to Capture implementation overview" title="Direct link to Capture implementation overview">​</a>

The API walkthrough starts from Niantic's Recording sample scene. These sample assets provide the runtime environment and reference implementation for the tutorial component:

| Sample asset | Responsibility |
|----|----|
| `Assets/Samples/Scanning/Scenes/Recording.unity` | Contains the configured AR Session, XR Origin, camera, NSDK settings, and Recording sample UI. |
| `Assets/Samples/Scanning/Scripts/RecordingDemo.cs` | Owns the sample recording controls, save/export flow, and scan visualization. |
| `ARScanningManager` on **AR Session** | Provides the Recording API entry point used by the tutorial controller. |
| `IOSShare` | Provides the sample iOS share-sheet helper used after export. |

The tutorial creates a separate scene and `PlaybackCaptureController.cs` so the Recording sample remains unchanged. When the finished controller moves into an app, that app must provide an AR Session with `ARScanningManager`, a valid authentication path, camera frames, location data, and app-specific archive handling.

Standalone development or internal-test builds can use a developer token from **Credentials \> Developer Tokens** in <a href="https://scaniverse.nianticspatial.com/signin" target="_blank" rel="noopener noreferrer">Scaniverse web</a>. Developer tokens should stay out of source control and public builds; see [Authorization](https://www.nianticspatial.com/docs/nsdk/auth_getting_started/) for the production flow.

### Prepare the tutorial scene<a href="#unity-prepare-the-tutorial-scene" class="hash-link" aria-label="Direct link to Prepare the tutorial scene" title="Direct link to Prepare the tutorial scene">​</a>

Create a disposable scene beside Niantic's Recording sample so you can validate the API code without changing the reference implementation:

1.  In the Project window, select `Assets/Samples/Scanning/Scenes/Recording.unity`, then select **Edit \> Duplicate**.
2.  Rename the copy `PlaybackCaptureTutorial.unity`, then open it.
3.  In the Hierarchy, select **RecordingDemo**. In the Inspector, clear the checkbox beside the existing `RecordingDemo` component so it cannot control the tutorial recording.
4.  Select the existing **Canvas** GameObject and deactivate it from the Inspector so its controls do not overlap the tutorial UI.
5.  Create the tutorial UI:
    1.  Select **GameObject \> UI \> Canvas** and name it `PlaybackCaptureCanvas`.

    2.  With `PlaybackCaptureCanvas` selected, configure its **Canvas Scaler** component to match the sample Canvas:

        | Canvas Scaler field      | Value                      |
        |--------------------------|----------------------------|
        | **UI Scale Mode**        | **Scale With Screen Size** |
        | **Reference Resolution** | `2500` x `1440`            |
        | **Screen Match Mode**    | **Match Width Or Height**  |
        | **Match**                | `0.5`                      |

    3.  With `PlaybackCaptureCanvas` selected, use **GameObject \> UI \> Button - TextMeshPro** to create a button. In the Hierarchy, rename the new button `StartCaptureButton`.

    4.  In the Hierarchy, expand `StartCaptureButton` and select its **Text (TMP)** child. In the Inspector, find the **TextMeshPro - Text (UI)** component and set **Text Input** to `Start Capture`. Set **Font Size** to `48`, and set **Alignment** to center and middle.

    5.  Repeat the previous two actions to create the remaining buttons: `StopCaptureButton` with **Text Input** set to `Stop Capture`, and `ExportButton` with **Text Input** set to `Export`. Use **Font Size** `48` and center-middle **Alignment** for both button labels.

    6.  With `PlaybackCaptureCanvas` selected, use **GameObject \> UI \> Text - TextMeshPro** to create a text object. In the Hierarchy, rename the new text object `CaptureStatus`.

    7.  Select `CaptureStatus`. In the Inspector, find the **TextMeshPro - Text (UI)** component and set **Text Input** to `Ready to capture`. Set **Font Size** to `56`, and set **Alignment** to center and middle.

    8.  Arrange the controls in the lower center of the screen, based on the disabled Recording sample controls. For each object, select the object in the Hierarchy, find its **Rect Transform** component in the Inspector, and enter the following values:

        `CaptureStatus`

        - Anchor Min: X `0.5`, Y `0`
        - Anchor Max: X `0.5`, Y `0`
        - Pivot: X `0.5`, Y `0.5`
        - Pos: X `0`, Y `720`
        - Width `1000`, Height `100`

        `StartCaptureButton`

        - Anchor Min: X `0.5`, Y `0`
        - Anchor Max: X `0.5`, Y `0`
        - Pivot: X `0.5`, Y `0.5`
        - Pos: X `-360`, Y `550`
        - Width `320`, Height `120`

        `StopCaptureButton`

        - Anchor Min: X `0.5`, Y `0`
        - Anchor Max: X `0.5`, Y `0`
        - Pivot: X `0.5`, Y `0.5`
        - Pos: X `0`, Y `550`
        - Width `320`, Height `120`

        `ExportButton`

        - Anchor Min: X `0.5`, Y `0`
        - Anchor Max: X `0.5`, Y `0`
        - Pivot: X `0.5`, Y `0.5`
        - Pos: X `360`, Y `550`
        - Width `320`, Height `120`
6.  Select **GameObject \> Create Empty** and name the new GameObject `PlaybackCaptureTutorial`.
7.  Select **File \> Build Profiles**, then select **Open Scene List**. The sample project includes several scenes and defaults to the `Home` scene, so configure this tutorial build to include only the tutorial scene:
    1.  Clear the checkbox for each selected scene in the scene list.
    2.  Select **Add Open Scenes** to add `PlaybackCaptureTutorial`.
    3.  Confirm that `PlaybackCaptureTutorial` is the only selected scene in the list.

The copied scene continues to provide the configured AR Session, XR Origin, camera, NSDK settings, and build configuration. The new component owns only the recording flow and its controls.

**Validate this step:**

1.  Select **Build and Run**.
2.  If Unity displays the **Unsupported Input Handling** dialog, select **Yes**. Unity might restart after updating the input handling setting. After Unity reopens the project, select **Build and Run** again.
3.  On the device, confirm that the app opens directly to `PlaybackCaptureTutorial` instead of the sample app's `Home` scene.
4.  Confirm that **Start Capture**, **Stop Capture**, **Export**, and **Ready to capture** are visible on the device.

The next steps add the script that connects the buttons to recording behavior.

### Create PlaybackCaptureController<a href="#unity-create-playback-capture-controller" class="hash-link" aria-label="Direct link to Create PlaybackCaptureController" title="Direct link to Create PlaybackCaptureController">​</a>

Create the component state and compiling placeholders used by the remaining steps:

1.  In the Project window, select `Assets/Samples/Scanning/Scripts`, then select **Assets \> Create \> Scripting \> MonoBehaviour Script**.
2.  Name the file `PlaybackCaptureController.cs`.
3.  Open `Assets/Samples/Scanning/Scripts/PlaybackCaptureController.cs` and replace its contents with the following code.

Expand to create PlaybackCaptureController.cs with its initial state and placeholders

<div>

<div class="collapsibleContent_i85q">

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
using System.Collections;
using System.Collections.Generic;
using System.Threading.Tasks;
using NianticSpatial.NSDK.AR.Scanning;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

public sealed class PlaybackCaptureController : MonoBehaviour
{
    // Connect these fields to the AR Scanning Manager and tutorial controls in
    // the Inspector. In your app, reuse the manager and controls in its AR scene.
    [SerializeField] private ARScanningManager _arScanningManager;
    [SerializeField] private Button _startButton;
    [SerializeField] private Button _stopButton;
    [SerializeField] private Button _exportButton;
    [SerializeField] private TMP_Text _statusText;

    // The exporter creates another archive after this many frames. Adjust the
    // value for your storage or upload limits.
    [SerializeField, Min(1)] private int _maxFramesPerChunk = 900;

    private ScanStore _scanStore;
    private ScanStore.SavedScan _savedScan;
    private readonly List<string> _archivePaths = new();
    private Coroutine _captureStartRoutine;
    private Coroutine _frameMonitorRoutine;
    private bool _isPreparing;
    private bool _isCapturing;
    private bool _canStopCapture;
    private bool _isSaving;
    private bool _isExporting;

    private void Awake()
    {
        if (_arScanningManager == null ||
            _startButton == null ||
            _stopButton == null ||
            _exportButton == null ||
            _statusText == null)
        {
            Debug.LogError(
                "PlaybackCaptureController: assign the manager and all controls."
            );
            enabled = false;
            return;
        }

        // Reuse the manager's scan store for the lifetime of this screen.
        _scanStore = _arScanningManager.GetScanStore();

        // If your UI already owns these actions, call the matching methods from
        // its existing handlers instead of registering another listener.
        _startButton.onClick.AddListener(StartCapture);
        _stopButton.onClick.AddListener(StopAndSaveCapture);
        _exportButton.onClick.AddListener(ExportCapture);
        UpdateControls();
        Debug.Log("PlaybackCaptureController: initialized");
    }

    private void OnDestroy()
    {
        _startButton?.onClick.RemoveListener(StartCapture);
        _stopButton?.onClick.RemoveListener(StopAndSaveCapture);
        _exportButton?.onClick.RemoveListener(ExportCapture);

        StopRoutine(ref _captureStartRoutine);
        StopRoutine(ref _frameMonitorRoutine);

        // Stop an unfinished recording when this tutorial screen is destroyed.
        // Do not unload your production screen while SaveScan() is running.
        if (_isCapturing && _arScanningManager != null)
        {
            _arScanningManager.enabled = false;
        }
    }

    private void UpdateControls()
    {
        // Placeholder: replaced in "Add capture controls."
    }

    public void StartCapture()
    {
        // Placeholder: replaced in "Start capture."
    }

    private IEnumerator StartWhenLocationIsReady()
    {
        // Placeholder: replaced in "Start capture."
        yield break;
    }

    private IEnumerator WaitForFirstFrame()
    {
        // Placeholder: replaced in "Start capture."
        yield break;
    }

    public async void StopAndSaveCapture()
    {
        // Placeholder: replaced in "Stop and save."
        await Task.CompletedTask;
    }

    public async void ExportCapture()
    {
        // Placeholder: replaced in "Export the archives."
        await Task.CompletedTask;
    }

    private void HandleArchives()
    {
        // Placeholder: replaced in "Verify and share archives."
    }

    private void SetStatus(string message)
    {
        _statusText.text = message;
        Debug.Log($"PlaybackCaptureController: {message}");
    }

    private void StopRoutine(ref Coroutine routine)
    {
        if (routine == null)
        {
            return;
        }

        StopCoroutine(routine);
        routine = null;
    }
}
```

</div>

</div>

</div>

</div>

4.  Return to Unity and wait for script compilation to finish.
5.  Select **PlaybackCaptureTutorial** in the Hierarchy, then select **Add Component \> Playback Capture Controller**.
6.  Assign the component fields in the Inspector:
    - Drag **AR Session** to **Ar Scanning Manager**.
    - Drag `StartCaptureButton`, `StopCaptureButton`, and `ExportButton` to their matching button fields.
    - Drag `CaptureStatus` to **Status Text**.
7.  Select **AR Session** and confirm that **AR Scanning Manager** is disabled so the tutorial component controls when recording starts.

**Validate this step:**

1.  Select **Build and Run**.

2.  Confirm `PlaybackCaptureController: initialized` appears in the device log for your platform:

    - For Android, open **View \> Tool Windows \> Logcat** in Android Studio. Select the connected device and app process, then search for `PlaybackCaptureController: initialized`.

      As a Terminal alternative, run:

      <div class="language-bash codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

      <div class="codeBlockContent_QJqH">

      ``` bash
      adb logcat | grep "PlaybackCaptureController: initialized"
      ```

      </div>

      </div>

      Press <span class="kbd">Control</span>+<span class="kbd">C</span> to stop watching the log.

    - For iOS, build the iOS project from Unity, open the generated Xcode project, and run the app on the connected device from Xcode. Select **View \> Debug Area \> Activate Console**, then search the debug console for `PlaybackCaptureController: initialized`.

### Add capture controls<a href="#unity-add-capture-controls" class="hash-link" aria-label="Direct link to Add capture controls" title="Direct link to Add capture controls">​</a>

In `Assets/Samples/Scanning/Scripts/PlaybackCaptureController.cs`, locate the placeholder `UpdateControls()` method and replace the entire method with the following implementation:

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
private void UpdateControls()
{
    // Keep capture actions mutually exclusive. Preserve the frame-count gate
    // if your app displays this state with different controls.
    bool isBusy = _isPreparing || _isSaving || _isExporting;
    _startButton.interactable = !isBusy && !_isCapturing;
    _stopButton.interactable = !isBusy && _isCapturing && _canStopCapture;
    _exportButton.interactable = !isBusy && !_isCapturing && _savedScan != null;
    Debug.Log(
        "PlaybackCaptureController: controls updated; " +
        $"start={_startButton.interactable}, " +
        $"stop={_stopButton.interactable}, " +
        $"export={_exportButton.interactable}"
    );
}
```

</div>

</div>

The component derives every control state from the recording lifecycle. Stop remains disabled until NSDK reports a recorded frame, and Export remains disabled until a saved scan exists.

**Validate this step:**

1.  Build and run the tutorial scene.

2.  Confirm the device log contains the initial control state:

    <div class="language-text codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` text
    PlaybackCaptureController: controls updated; start=True, stop=False, export=False
    ```

    </div>

    </div>

    For Android, use Android Studio Logcat to search for `PlaybackCaptureController: controls updated`, or run:

    <div class="language-bash codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` bash
    adb logcat | grep "PlaybackCaptureController: controls updated"
    ```

    </div>

    </div>

    For iOS, run the app from Xcode and search the debug console for `PlaybackCaptureController: controls updated`.

The next step adds the capture-start behavior.

### Start capture<a href="#unity-start-capture" class="hash-link" aria-label="Direct link to Start capture" title="Direct link to Start capture">​</a>

In `Assets/Samples/Scanning/Scripts/PlaybackCaptureController.cs`, add the Android permission import with the other `using` directives. Keep the import inside the platform check so iOS builds do not depend on Android-only APIs:

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
#if UNITY_ANDROID
using UnityEngine.Android;
#endif
```

</div>

</div>

Then replace the placeholder `StartCapture()`, `StartWhenLocationIsReady()`, and `WaitForFirstFrame()` methods with the following implementations. The Android build requests location permission when necessary. Both Android and iOS builds initialize Unity's location and compass services, enable the scanning manager, and open the stop gate only after NSDK records a frame:

Expand to replace the Unity start-capture methods

<div>

<div class="collapsibleContent_i85q">

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
public void StartCapture()
{
    if (_isPreparing || _isCapturing || _isSaving || _isExporting)
    {
        return;
    }

    // Android requires runtime location permission before Unity can start its
    // location service. Replace this block with your app's existing permission
    // flow if permissions are requested somewhere else.
#if UNITY_ANDROID && !UNITY_EDITOR
    if (!Permission.HasUserAuthorizedPermission(Permission.FineLocation))
    {
        _isPreparing = true;
        UpdateControls();
        SetStatus("waiting for location permission");

        var callbacks = new PermissionCallbacks();
        callbacks.PermissionGranted += permissionName =>
        {
            if (permissionName == Permission.FineLocation)
            {
                // Permission is now available. Enter StartCapture() again so
                // the shared Android/iOS startup path following this block runs.
                _isPreparing = false;
                StartCapture();
            }
        };
        callbacks.PermissionDenied += permissionName =>
        {
            _isPreparing = false;
            SetStatus("location permission is required for capture");
            UpdateControls();
        };
        Permission.RequestUserPermission(Permission.FineLocation, callbacks);
        return;
    }
#endif

    // Shared Android/iOS setup: clear any previous tutorial recording state,
    // update the controls, then wait for location before enabling recording.
    // In your app, keep this reset near the code that owns the capture UI.
    _isPreparing = true;
    _savedScan = null;
    _archivePaths.Clear();
    UpdateControls();
    _captureStartRoutine = StartCoroutine(StartWhenLocationIsReady());
}

private IEnumerator StartWhenLocationIsReady()
{
    // NSDK records location and compass data with the camera frames. Replace
    // this startup block with your app's existing location-readiness signal if
    // your app already owns location and compass initialization.
    Input.compass.enabled = true;
    if (Input.location.status == LocationServiceStatus.Stopped)
    {
        Input.location.Start();
    }

    const float timeoutSeconds = 20f;
    float elapsedSeconds = 0f;
    while (Input.location.status != LocationServiceStatus.Running &&
           Input.location.status != LocationServiceStatus.Failed &&
           elapsedSeconds < timeoutSeconds)
    {
        elapsedSeconds += Time.unscaledDeltaTime;
        yield return null;
    }

    _captureStartRoutine = null;
    if (Input.location.status != LocationServiceStatus.Running)
    {
        _isPreparing = false;
        SetStatus("location initialization failed");
        UpdateControls();
        yield break;
    }

    _canStopCapture = false;
    _isPreparing = false;
    _isCapturing = true;

    // Enabling ARScanningManager requests that recording begin. It is not safe
    // to stop yet, so Stop Capture stays disabled until WaitForFirstFrame()
    // observes GetFrameCount() > 0.
    _arScanningManager.enabled = true;
    SetStatus("capture start requested");
    UpdateControls();
    _frameMonitorRoutine = StartCoroutine(WaitForFirstFrame());
}

private IEnumerator WaitForFirstFrame()
{
    // Recording startup can lag behind the button tap. Poll the NSDK frame
    // count until the recording contains at least one saved frame. If your app
    // already exposes capture-readiness state, use that signal instead.
    var pollingDelay = new WaitForSecondsRealtime(0.2f);
    while (_isCapturing)
    {
        int frameCount = _arScanningManager.GetFrameCount();
        if (frameCount > 0)
        {
            // From this point forward, SaveScan() has frame data to save, so
            // the UI can enable Stop Capture.
            _canStopCapture = true;
            _frameMonitorRoutine = null;
            SetStatus($"capture ready to stop; frameCount={frameCount}");
            UpdateControls();
            yield break;
        }

        yield return pollingDelay;
    }

    _frameMonitorRoutine = null;
}
```

</div>

</div>

</div>

</div>

Enabling `ARScanningManager` requests that recording begin, but a scan cannot be saved until `GetFrameCount()` is greater than zero. The initialization interval can vary. Keep the stop action disabled until the SDK confirms that it has recorded a frame.

**Validate this step:**

1.  Build and run the tutorial scene, then grant camera and location permissions if the device requests them.

2.  Tap **Start Capture** and move the device through the environment.

3.  Confirm the device log contains both messages and that the second frame count is greater than zero:

    <div class="language-text codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` text
    PlaybackCaptureController: capture start requested
    PlaybackCaptureController: capture ready to stop; frameCount=
    ```

    </div>

    </div>

4.  Confirm that **Stop Capture** is enabled after the second message appears.

The next section replaces the placeholder stop method with the save behavior.

### Stop and save<a href="#unity-stop-and-save" class="hash-link" aria-label="Direct link to Stop and save" title="Direct link to Stop and save">​</a>

Add the following imports to `Assets/Samples/Scanning/Scripts/PlaybackCaptureController.cs`:

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
using System;
using System.Linq;
```

</div>

</div>

Replace the placeholder `StopAndSaveCapture()` method with the following code. It rechecks the frame count, reads the scan ID while capture is active, keeps the scanning manager enabled throughout the asynchronous save, and then resolves the saved scan from the scan store:

Expand to replace the Unity stop-and-save method

<div>

<div class="collapsibleContent_i85q">

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
public async void StopAndSaveCapture()
{
    // Save only after recording has started and the frame-count gate has opened.
    // In your app, keep the same guard even if another UI element calls save.
    if (!_isCapturing || !_canStopCapture || _isSaving)
    {
        return;
    }

    // Recheck at the save boundary so callers other than the button cannot
    // ask SaveScan() to save an empty recording.
    int frameCount = _arScanningManager.GetFrameCount();
    if (frameCount <= 0)
    {
        _canStopCapture = false;
        UpdateControls();
        return;
    }

    // Read the ID while scanning is active; GetCurrentScanId() is only
    // guaranteed to return it while a scan is in progress.
    string scanId = _arScanningManager.GetCurrentScanId();
    if (string.IsNullOrEmpty(scanId))
    {
        SetStatus("save failed: scan ID is unavailable");
        return;
    }

    StopRoutine(ref _frameMonitorRoutine);
    // Switch the tutorial UI into a saving state before awaiting SaveScan().
    // Replace these flags with your app's own state model if needed.
    _isCapturing = false;
    _canStopCapture = false;
    _isSaving = true;
    SetStatus($"save started; frameCount={frameCount}");
    UpdateControls();

    try
    {
        // Keep ARScanningManager enabled until this asynchronous save
        // completes. Disabling it earlier can interrupt the recording.
        await _arScanningManager.SaveScan();
        _arScanningManager.enabled = false;

        // The exporter needs the SavedScan object. If your app stores scans in
        // another model, replace this lookup with that source of truth.
        _savedScan = _scanStore.GetSavedScans()
            .FirstOrDefault(scan => scan.ScanId == scanId);
        if (_savedScan == null)
        {
            throw new InvalidOperationException(
                $"Saved scan {scanId} was not found in the scan store."
            );
        }

        SetStatus($"save completed; scanId={scanId}");
    }
    catch (Exception exception)
    {
        _arScanningManager.enabled = false;
        _savedScan = null;
        Debug.LogException(exception);
        // Replace this status text with your app's error surface.
        SetStatus($"save failed: {exception.Message}");
    }
    finally
    {
        // Always leave the UI in a non-saving state after success or failure.
        _isSaving = false;
        UpdateControls();
    }
}
```

</div>

</div>

</div>

</div>

**Validate this step:**

1.  Build and run the tutorial scene.

2.  Start capture and wait for **Stop Capture** to become enabled.

3.  Tap **Stop Capture**.

4.  Confirm that tapping **Stop Capture** caused the device log to contain the following messages in order. The first frame count must be greater than zero, and the second message must contain a scan ID:

    <div class="language-text codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` text
    PlaybackCaptureController: save started; frameCount=
    PlaybackCaptureController: save completed; scanId=
    ```

    </div>

    </div>

5.  Confirm that **Start Capture** and **Export** are enabled after saving.

Do not tap **Export** for this validation. At this point in the walkthrough, `ExportCapture()` is still a placeholder. The next section adds the export code and tells you when to tap **Export**.

### Export the archives<a href="#unity-export-the-archives" class="hash-link" aria-label="Direct link to Export the archives" title="Direct link to Export the archives">​</a>

In `Assets/Samples/Scanning/Scripts/PlaybackCaptureController.cs`, replace the placeholder `ExportCapture()` method with the following implementation. It passes the `SavedScan` directly to `ScanArchiveBuilder`, disposes the builder's native resources, and stores every path returned by the exporter:

Expand to replace the Unity export method

<div>

<div class="collapsibleContent_i85q">

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
public async void ExportCapture()
{
    // Export needs a saved scan. In your app, keep the export action disabled
    // until the save flow has produced the SavedScan you want to package.
    if (_savedScan == null || _isSaving || _isExporting)
    {
        return;
    }

    // Track export state for this tutorial UI. Replace this with your app's
    // progress, loading, or job state if export runs from another layer.
    _isExporting = true;
    _archivePaths.Clear();
    SetStatus($"export started; scanId={_savedScan.ScanId}");
    UpdateControls();

    try
    {
        // ScanArchiveBuilder converts the saved recording into one or more
        // playback archives. It owns native resources, so always dispose it.
        using var builder = new ScanArchiveBuilder(
            _savedScan,
            // Replace UploadUserInfo with your app's upload/user metadata if
            // your backend expects it. Leave it empty for local validation.
            new UploadUserInfo(),
            // Tune this value for your storage, upload, or sharing limits.
            _maxFramesPerChunk
        );
        if (!builder.IsValid())
        {
            throw new InvalidOperationException(
                "The scan archive builder could not be created."
            );
        }

        while (builder.HasMoreChunks())
        {
            // Each chunk task writes one .tgz archive. The returned value is
            // the actual file path; use it instead of constructing a path from
            // the scan ID.
            Task<string> exportTask = builder.CreateTaskToGetNextChunk();
            exportTask.Start();
            string archivePath = await exportTask;
            if (!string.IsNullOrEmpty(archivePath))
            {
                _archivePaths.Add(archivePath);
                Debug.Log(
                    $"PlaybackCaptureController: archive exported: {archivePath}"
                );
            }
        }

        if (_archivePaths.Count == 0)
        {
            throw new InvalidOperationException("No playback archives were exported.");
        }

        SetStatus($"export completed; archiveCount={_archivePaths.Count}");
        // Replace HandleArchives() with your app's upload, storage, or sharing
        // flow when you integrate the exporter outside this tutorial.
        HandleArchives();
    }
    catch (Exception exception)
    {
        Debug.LogException(exception);
        // Replace this status text with your app's error surface.
        SetStatus($"export failed: {exception.Message}");
    }
    finally
    {
        // Always clear the exporting state so the UI does not stay disabled
        // after a successful export or a handled failure.
        _isExporting = false;
        UpdateControls();
    }
}
```

</div>

</div>

</div>

</div>

The `maxFramesPerChunk` value controls the maximum number of frames in each output archive. A recording with more frames produces multiple `.tgz` files. `ScanArchiveBuilder` does not provide a fractional progress callback, so update your UI when each returned chunk finishes.

**Validate this step:**

1.  Build and run the tutorial scene, then start and stop a recording.
2.  Tap **Export**.
3.  Confirm the device log contains `export started; scanId=`, followed by one or more `archive exported:` messages containing `.tgz` paths.
4.  Confirm `export completed; archiveCount=` reports the number of exported paths. Archive verification and sharing are still placeholders and are added in the next section.

### Verify and share archives<a href="#unity-verify-and-share-archives" class="hash-link" aria-label="Direct link to Verify and share archives" title="Direct link to Verify and share archives">​</a>

Add the following import to `Assets/Samples/Scanning/Scripts/PlaybackCaptureController.cs`:

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
using System.IO;
```

</div>

</div>

Replace the placeholder `HandleArchives()` method with the following code. It verifies every returned file and logs its path. On iOS, Niantic's sample project also provides `IOSShare`, which opens the system share sheet when the recording fits in one archive:

Expand to replace the Unity archive verification and sharing method

<div>

<div class="collapsibleContent_i85q">

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
private void HandleArchives()
{
    foreach (string archivePath in _archivePaths)
    {
        if (!File.Exists(archivePath))
        {
            Debug.LogError(
                $"PlaybackCaptureController: archive not found: {archivePath}"
            );
            continue;
        }

        Debug.Log($"PlaybackCaptureController: archive ready: {archivePath}");
    }

#if UNITY_IOS && !UNITY_EDITOR
    // Niantic's sample app includes IOSShare. Replace it with your product's
    // upload or storage flow if the archive should not use the share sheet.
    if (_archivePaths.Count == 1 && File.Exists(_archivePaths[0]))
    {
        IOSShare.ShareFile(
            _archivePaths[0],
            "Sharing playback recording"
        );
        Debug.Log(
            $"PlaybackCaptureController: share sheet opened: {_archivePaths[0]}"
        );
    }
#endif
}
```

</div>

</div>

</div>

</div>

The public Unity sample does not include an Android `FileProvider` sharing flow. On Android, use the logged archive paths for retrieval or replace `HandleArchives()` with your app's upload, storage, or sharing implementation. Do the same on iOS if your product should not use the system share sheet.

**Validate this step:**

1.  Build and run the tutorial scene.
2.  Tap **Start Capture**, move the device through the environment, wait for **Stop Capture** to become enabled, then tap **Stop Capture**.
3.  After the save completes and **Export** is enabled, tap **Export**.
4.  Confirm each `archive exported:` path has a matching `archive ready:` path.
5.  Confirm the device log does not contain `archive not found` or `export failed`.

Expected result by platform:

- Android: no share sheet opens because the public Unity sample does not include an Android sharing implementation.
- iOS: a single-archive recording opens the share sheet, and `share sheet opened:` contains the same path.

### Retrieve and verify the recording<a href="#unity-retrieve-and-verify-the-recording" class="hash-link" aria-label="Direct link to Retrieve and verify the recording" title="Direct link to Retrieve and verify the recording">​</a>

Use the `archive ready:` log from the previous section to identify each `.tgz` file that export created. The `save completed; scanId=` log names the recording folder, but the `archive ready:` log gives the full archive path to retrieve.

<span id="recording-data"></span>

#### File locations<a href="#file-locations" class="hash-link" aria-label="Direct link to File locations" title="Direct link to File locations">​</a>

If **Scan Path** is empty on `ARScanningManager`, Unity recordings use these default locations:

| Platform | Default Unity recording directory |
|----|----|
| iOS | The app's `Documents/scankit/` directory |
| Android | `/sdcard/Android/data/{app.package.name}/files/scankit/` |
| macOS Editor | `/Users/{username}/Library/Application Support/{companyName}/{productName}/scankit/` |
| Windows Editor | `C:\Users\{username}\AppData\LocalLow\{companyName}\{productName}\scankit\` |

The saved location is also available from the [`ScanStore.SavedScan.ScanBasePath`](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanStore/#property-scanbasepath) property. If your app configures **Scan Path**, use that location instead of the defaults.

#### Retrieve from Android<a href="#unity-retrieve-from-android" class="hash-link" aria-label="Direct link to Retrieve from Android" title="Direct link to Retrieve from Android">​</a>

1.  In the device log, copy each full path from `archive ready:`. The path should end in `.tgz`, for example:

    <div class="language-text codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` text
    /sdcard/Android/data/com.nianticspatial.nsdk.nsdksamples/files/scankit/SCAN_ID/chunk_0.tgz
    ```

    </div>

    </div>

2.  Copy the file with either Android Studio Device Explorer or `adb pull`:

    - Android Studio Device Explorer is the most reliable option when the device restricts direct command-line access to app-specific external storage:

      1.  In Android Studio, select **View \> Tool Windows \> Device Explorer**, then select the connected device.
      2.  Navigate to the directory shown in the `archive ready:` path.
      3.  Select each `.tgz` file, then use **Save As** in the Device Explorer toolbar to copy it to the development machine.

    - `adb pull` is the direct command-line option when the path is accessible. Replace the path in this command with the path from your device log:

      <div class="language-bash codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

      <div class="codeBlockContent_QJqH">

      ``` bash
      adb pull /sdcard/Android/data/com.nianticspatial.nsdk.nsdksamples/files/scankit/SCAN_ID/chunk_0.tgz .
      ```

      </div>

      </div>

      The final `.` copies the archive into the terminal's current directory.

3.  Repeat the copy action for each additional `archive ready:` path.

For your own app, replace `com.nianticspatial.nsdk.nsdksamples` with its Android application ID.

#### Retrieve from iOS<a href="#unity-retrieve-from-ios" class="hash-link" aria-label="Direct link to Retrieve from iOS" title="Direct link to Retrieve from iOS">​</a>

On iOS, use the share sheet from the previous section when it opens. Save the archive to Files, send it with AirDrop, or share it with another app.

If you need to retrieve the archive directly from the app container, use Finder. The public sample's `Assets/Editor/PostBuildProcess.cs` adds `UIFileSharingEnabled` and `LSSupportsOpeningDocumentsInPlace` to the generated app. These keys expose the app's Documents directory in Finder.

1.  Keep the iOS device connected and unlocked.
2.  In Finder, select the device in the sidebar, then select **Files**.
3.  Expand **NSDK Unity Samples** and drag the `scankit` folder to the Mac.
4.  Open the scan-ID directory reported by `save completed; scanId=`.
5.  Locate the `.tgz` file named in the `archive ready:` path.

When you integrate recording into your own Unity app, add the same keys in its iOS post-build processor:

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
rootDict.SetBoolean("UIFileSharingEnabled", true);
rootDict.SetBoolean("LSSupportsOpeningDocumentsInPlace", true);
```

</div>

</div>

#### Verify the exported files<a href="#unity-verify-the-exported-files" class="hash-link" aria-label="Direct link to Verify the exported files" title="Direct link to Verify the exported files">​</a>

1.  Extract each `.tgz` archive with the operating system's built-in archive support:
    - On macOS, select the file in Finder, then select **File \> Open**.
    - On Windows 11 version 24H2 or later, select the file in File Explorer, then select **Extract All**.
    - On Linux, select the file in the system file manager, then select its **Extract** action. The action name depends on the desktop environment.
2.  In the extracted files, confirm that `capture.json` and `frame_*.jpg` are present.
3.  Open `capture.json` in a text editor and locate its top-level `frameCount` property. Confirm that the value is greater than zero.
4.  Confirm that frame numbering begins with `frame_00000000.jpg`. Across all chunks, the number of frame images should correspond to the exported frame count.
5.  Open several `frame_*.jpg` files and confirm that they show the environment you recorded.

Depth and confidence files are device- and configuration-dependent, so their absence does not by itself mean the playback dataset is invalid. To validate the recording by replaying it, continue with [Set up Playback](https://www.nianticspatial.com/docs/nsdk/how-to/playback/setting_up_playback/).

### View the complete PlaybackCaptureController<a href="#unity-complete-playback-capture-controller" class="hash-link" aria-label="Direct link to View the complete PlaybackCaptureController" title="Direct link to View the complete PlaybackCaptureController">​</a>

The expandable section contains the complete `PlaybackCaptureController.cs` assembled in the preceding steps. Use it to check your completed component, recover a missed change, or copy the full implementation without repeating the walkthrough. Refer to this code for the tutorial's finished result; Niantic's existing `RecordingDemo.cs` is a separate sample implementation and does not correspond line-for-line with these steps.

Expand to reveal PlaybackCaptureController.cs

<div>

<div class="collapsibleContent_i85q">

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using NianticSpatial.NSDK.AR.Scanning;
using TMPro;
using UnityEngine;
#if UNITY_ANDROID
using UnityEngine.Android;
#endif
using UnityEngine.UI;

public sealed class PlaybackCaptureController : MonoBehaviour
{
    // Connect these fields to the AR Scanning Manager and tutorial controls in
    // the Inspector. In your app, reuse the manager and controls in its AR scene.
    [SerializeField] private ARScanningManager _arScanningManager;
    [SerializeField] private Button _startButton;
    [SerializeField] private Button _stopButton;
    [SerializeField] private Button _exportButton;
    [SerializeField] private TMP_Text _statusText;

    // The exporter creates another archive after this many frames. Adjust the
    // value for your storage or upload limits.
    [SerializeField, Min(1)] private int _maxFramesPerChunk = 900;

    private ScanStore _scanStore;
    private ScanStore.SavedScan _savedScan;
    private readonly List<string> _archivePaths = new();
    private Coroutine _captureStartRoutine;
    private Coroutine _frameMonitorRoutine;
    private bool _isPreparing;
    private bool _isCapturing;
    private bool _canStopCapture;
    private bool _isSaving;
    private bool _isExporting;

    private void Awake()
    {
        if (_arScanningManager == null ||
            _startButton == null ||
            _stopButton == null ||
            _exportButton == null ||
            _statusText == null)
        {
            Debug.LogError(
                "PlaybackCaptureController: assign the manager and all controls."
            );
            enabled = false;
            return;
        }

        // Reuse the manager's scan store for the lifetime of this screen.
        _scanStore = _arScanningManager.GetScanStore();

        // If your UI already owns these actions, call the matching methods from
        // its existing handlers instead of registering another listener.
        _startButton.onClick.AddListener(StartCapture);
        _stopButton.onClick.AddListener(StopAndSaveCapture);
        _exportButton.onClick.AddListener(ExportCapture);
        UpdateControls();
        Debug.Log("PlaybackCaptureController: initialized");
    }

    private void OnDestroy()
    {
        _startButton?.onClick.RemoveListener(StartCapture);
        _stopButton?.onClick.RemoveListener(StopAndSaveCapture);
        _exportButton?.onClick.RemoveListener(ExportCapture);

        StopRoutine(ref _captureStartRoutine);
        StopRoutine(ref _frameMonitorRoutine);

        // Stop an unfinished recording when this tutorial screen is destroyed.
        // Do not unload your production screen while SaveScan() is running.
        if (_isCapturing && _arScanningManager != null)
        {
            _arScanningManager.enabled = false;
        }
    }

    private void UpdateControls()
    {
        // Keep capture actions mutually exclusive. Preserve the frame-count gate
        // if your app displays this state with different controls.
        bool isBusy = _isPreparing || _isSaving || _isExporting;
        _startButton.interactable = !isBusy && !_isCapturing;
        _stopButton.interactable = !isBusy && _isCapturing && _canStopCapture;
        _exportButton.interactable = !isBusy && !_isCapturing && _savedScan != null;
        Debug.Log(
            "PlaybackCaptureController: controls updated; " +
            $"start={_startButton.interactable}, " +
            $"stop={_stopButton.interactable}, " +
            $"export={_exportButton.interactable}"
        );
    }

    public void StartCapture()
    {
        if (_isPreparing || _isCapturing || _isSaving || _isExporting)
        {
            return;
        }

        // Android requires runtime location permission before Unity can start its
        // location service. Replace this block with your app's existing permission
        // flow if permissions are requested somewhere else.
#if UNITY_ANDROID && !UNITY_EDITOR
        if (!Permission.HasUserAuthorizedPermission(Permission.FineLocation))
        {
            _isPreparing = true;
            UpdateControls();
            SetStatus("waiting for location permission");

            var callbacks = new PermissionCallbacks();
            callbacks.PermissionGranted += permissionName =>
            {
                if (permissionName == Permission.FineLocation)
                {
                    // Permission is now available. Enter StartCapture() again so
                    // the shared Android/iOS startup path following this block runs.
                    _isPreparing = false;
                    StartCapture();
                }
            };
            callbacks.PermissionDenied += permissionName =>
            {
                _isPreparing = false;
                SetStatus("location permission is required for capture");
                UpdateControls();
            };
            Permission.RequestUserPermission(Permission.FineLocation, callbacks);
            return;
        }
#endif

        // Shared Android/iOS setup: clear any previous tutorial recording state,
        // update the controls, then wait for location before enabling recording.
        // In your app, keep this reset near the code that owns the capture UI.
        _isPreparing = true;
        _savedScan = null;
        _archivePaths.Clear();
        UpdateControls();
        _captureStartRoutine = StartCoroutine(StartWhenLocationIsReady());
    }

    private IEnumerator StartWhenLocationIsReady()
    {
        // NSDK records location and compass data with the camera frames. Replace
        // this startup block with your app's existing location-readiness signal if
        // your app already owns location and compass initialization.
        Input.compass.enabled = true;
        if (Input.location.status == LocationServiceStatus.Stopped)
        {
            Input.location.Start();
        }

        const float timeoutSeconds = 20f;
        float elapsedSeconds = 0f;
        while (Input.location.status != LocationServiceStatus.Running &&
               Input.location.status != LocationServiceStatus.Failed &&
               elapsedSeconds < timeoutSeconds)
        {
            elapsedSeconds += Time.unscaledDeltaTime;
            yield return null;
        }

        _captureStartRoutine = null;
        if (Input.location.status != LocationServiceStatus.Running)
        {
            _isPreparing = false;
            SetStatus("location initialization failed");
            UpdateControls();
            yield break;
        }

        _canStopCapture = false;
        _isPreparing = false;
        _isCapturing = true;

        // Enabling ARScanningManager requests that recording begin. It is not safe
        // to stop yet, so Stop Capture stays disabled until WaitForFirstFrame()
        // observes GetFrameCount() > 0.
        _arScanningManager.enabled = true;
        SetStatus("capture start requested");
        UpdateControls();
        _frameMonitorRoutine = StartCoroutine(WaitForFirstFrame());
    }

    private IEnumerator WaitForFirstFrame()
    {
        // Recording startup can lag behind the button tap. Poll the NSDK frame
        // count until the recording contains at least one saved frame. If your app
        // already exposes capture-readiness state, use that signal instead.
        var pollingDelay = new WaitForSecondsRealtime(0.2f);
        while (_isCapturing)
        {
            int frameCount = _arScanningManager.GetFrameCount();
            if (frameCount > 0)
            {
                // From this point forward, SaveScan() has frame data to save, so
                // the UI can enable Stop Capture.
                _canStopCapture = true;
                _frameMonitorRoutine = null;
                SetStatus($"capture ready to stop; frameCount={frameCount}");
                UpdateControls();
                yield break;
            }

            yield return pollingDelay;
        }

        _frameMonitorRoutine = null;
    }

    public async void StopAndSaveCapture()
    {
        // Save only after recording has started and the frame-count gate has opened.
        // In your app, keep the same guard even if another UI element calls save.
        if (!_isCapturing || !_canStopCapture || _isSaving)
        {
            return;
        }

        // Recheck at the save boundary so callers other than the button cannot
        // ask SaveScan() to save an empty recording.
        int frameCount = _arScanningManager.GetFrameCount();
        if (frameCount <= 0)
        {
            _canStopCapture = false;
            UpdateControls();
            return;
        }

        // Read the ID while scanning is active; GetCurrentScanId() is only
        // guaranteed to return it while a scan is in progress.
        string scanId = _arScanningManager.GetCurrentScanId();
        if (string.IsNullOrEmpty(scanId))
        {
            SetStatus("save failed: scan ID is unavailable");
            return;
        }

        StopRoutine(ref _frameMonitorRoutine);
        // Switch the tutorial UI into a saving state before awaiting SaveScan().
        // Replace these flags with your app's own state model if needed.
        _isCapturing = false;
        _canStopCapture = false;
        _isSaving = true;
        SetStatus($"save started; frameCount={frameCount}");
        UpdateControls();

        try
        {
            // Keep ARScanningManager enabled until this asynchronous save
            // completes. Disabling it earlier can interrupt the recording.
            await _arScanningManager.SaveScan();
            _arScanningManager.enabled = false;

            // The exporter needs the SavedScan object. If your app stores scans in
            // another model, replace this lookup with that source of truth.
            _savedScan = _scanStore.GetSavedScans()
                .FirstOrDefault(scan => scan.ScanId == scanId);
            if (_savedScan == null)
            {
                throw new InvalidOperationException(
                    $"Saved scan {scanId} was not found in the scan store."
                );
            }

            SetStatus($"save completed; scanId={scanId}");
        }
        catch (Exception exception)
        {
            _arScanningManager.enabled = false;
            _savedScan = null;
            Debug.LogException(exception);
            // Replace this status text with your app's error surface.
            SetStatus($"save failed: {exception.Message}");
        }
        finally
        {
            // Always leave the UI in a non-saving state after success or failure.
            _isSaving = false;
            UpdateControls();
        }
    }

    public async void ExportCapture()
    {
        // Export needs a saved scan. In your app, keep the export action disabled
        // until the save flow has produced the SavedScan you want to package.
        if (_savedScan == null || _isSaving || _isExporting)
        {
            return;
        }

        // Track export state for this tutorial UI. Replace this with your app's
        // progress, loading, or job state if export runs from another layer.
        _isExporting = true;
        _archivePaths.Clear();
        SetStatus($"export started; scanId={_savedScan.ScanId}");
        UpdateControls();

        try
        {
            // ScanArchiveBuilder converts the saved recording into one or more
            // playback archives. It owns native resources, so always dispose it.
            using var builder = new ScanArchiveBuilder(
                _savedScan,
                // Replace UploadUserInfo with your app's upload/user metadata if
                // your backend expects it. Leave it empty for local validation.
                new UploadUserInfo(),
                // Tune this value for your storage, upload, or sharing limits.
                _maxFramesPerChunk
            );
            if (!builder.IsValid())
            {
                throw new InvalidOperationException(
                    "The scan archive builder could not be created."
                );
            }

            while (builder.HasMoreChunks())
            {
                // Each chunk task writes one .tgz archive. The returned value is
                // the actual file path; use it instead of constructing a path from
                // the scan ID.
                Task<string> exportTask = builder.CreateTaskToGetNextChunk();
                exportTask.Start();
                string archivePath = await exportTask;
                if (!string.IsNullOrEmpty(archivePath))
                {
                    _archivePaths.Add(archivePath);
                    Debug.Log(
                        $"PlaybackCaptureController: archive exported: {archivePath}"
                    );
                }
            }

            if (_archivePaths.Count == 0)
            {
                throw new InvalidOperationException("No playback archives were exported.");
            }

            SetStatus($"export completed; archiveCount={_archivePaths.Count}");
            // Replace HandleArchives() with your app's upload, storage, or sharing
            // flow when you integrate the exporter outside this tutorial.
            HandleArchives();
        }
        catch (Exception exception)
        {
            Debug.LogException(exception);
            // Replace this status text with your app's error surface.
            SetStatus($"export failed: {exception.Message}");
        }
        finally
        {
            // Always clear the exporting state so the UI does not stay disabled
            // after a successful export or a handled failure.
            _isExporting = false;
            UpdateControls();
        }
    }

    private void HandleArchives()
    {
        foreach (string archivePath in _archivePaths)
        {
            if (!File.Exists(archivePath))
            {
                Debug.LogError(
                    $"PlaybackCaptureController: archive not found: {archivePath}"
                );
                continue;
            }

            Debug.Log($"PlaybackCaptureController: archive ready: {archivePath}");
        }

#if UNITY_IOS && !UNITY_EDITOR
        // Niantic's sample app includes IOSShare. Replace it with your product's
        // upload or storage flow if the archive should not use the share sheet.
        if (_archivePaths.Count == 1 && File.Exists(_archivePaths[0]))
        {
            IOSShare.ShareFile(
                _archivePaths[0],
                "Sharing playback recording"
            );
            Debug.Log(
                $"PlaybackCaptureController: share sheet opened: {_archivePaths[0]}"
            );
        }
#endif
    }

    private void SetStatus(string message)
    {
        _statusText.text = message;
        Debug.Log($"PlaybackCaptureController: {message}");
    }

    private void StopRoutine(ref Coroutine routine)
    {
        if (routine == null)
        {
            return;
        }

        StopCoroutine(routine);
        routine = null;
    }
}
```

</div>

</div>

</div>

</div>

### Add to your app<a href="#unity-add-to-your-app" class="hash-link" aria-label="Direct link to Add to your app" title="Direct link to Add to your app">​</a>

The tutorial scene supplies several dependencies that your existing AR scene may already own:

| Tutorial dependency | Use in your app |
|----|----|
| `ARScanningManager` on **AR Session** | Reuse the scanning manager in the scene that owns your AR session. |
| Tutorial buttons and status label | Connect your existing controls, or move the state transitions into your UI layer. |
| `Input.location` and `Input.compass` initialization | Keep your app's existing location and compass lifecycle if it already provides one. |
| `IOSShare` | Replace this sample helper with your product's upload, storage, or sharing flow. |

Move the completed recording flow into your Unity app:

1.  Confirm that the app has NSDK installed, an AR Session and XR Origin, a valid authentication path, and **Scanning** enabled under **Edit \> Project Settings \> XR Plug-in Management \> Niantic Spatial Development Kit**.
2.  Copy `PlaybackCaptureController.cs` into the app, or move its state and methods into the component that already owns recording UI.
3.  Add or reuse an `ARScanningManager` on the app's **AR Session** GameObject. Leave the component disabled until `StartCapture()` enables it.
4.  Connect the scanning manager and the app's start, stop, export, and status UI to the serialized fields. If another component already registers the button events, remove the listener registration from `Awake()` and call the corresponding methods from the existing handlers.
5.  Replace the Android permission and Unity location initialization with the app's existing permission flow if it has one. Preserve the requirement that location and compass data are available before recording starts.
6.  Replace `HandleArchives()` with the app's upload, storage, or sharing behavior. If the app does not include Niantic's `IOSShare` helper, remove or replace that iOS-only call before building for iOS.
7.  Prevent scene navigation while `SaveScan()` is running. Keep `ARScanningManager` enabled until the save completes, then stop it during the AR screen's normal cleanup.
8.  Build and run the app on a supported physical device, then validate the complete lifecycle:
    1.  Open the AR screen and its Android or iOS device log.
    2.  Start capture and confirm `capture start requested` appears.
    3.  Confirm `capture ready to stop; frameCount=` reports a value greater than zero before Stop becomes available.
    4.  Stop capture and confirm the save-started and save-completed messages appear in order.
    5.  Export the recording and confirm every `archive exported:` path has a matching `archive ready:` path.
    6.  Retrieve the archives and confirm `capture.json` reports a frame count greater than zero.
    7.  Leave and reopen the AR scene, then complete a second capture and export. Confirm that the first component does not retain a coroutine or active scanning manager.
    8.  Confirm the device log does not report `location initialization failed`, `save failed`, `export failed`, or `archive not found`.

Continue with [Set up Playback](https://www.nianticspatial.com/docs/nsdk/how-to/playback/setting_up_playback/) to load the exported recording in the Unity Editor.

</div>

</div>
