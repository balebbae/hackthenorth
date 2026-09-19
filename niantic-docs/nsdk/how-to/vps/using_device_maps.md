---
source: https://www.nianticspatial.com/docs/nsdk/how-to/vps/using_device_maps/
title: Using Device Maps
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

This feature is experimental and may not work as expected. For more information about it, see the [Device Mapping Feature page](https://www.nianticspatial.com/docs/nsdk/features/device_mapping/).

</div>

</div>

<div>

# How to Place Virtual Content Using a Device Map

</div>

Now that we have created a device map and saved it to a file, we can read it to place virtual objects in the AR scene. In this how-to, we will cover reading a device map file into your Unity project and how to use it to place content.

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

Before you start, complete [How to Create a Device Map](https://www.nianticspatial.com/docs/nsdk/how-to/vps/adding_device_mapping/). You will need the Unity project from that tutorial for this one. You will also need one prefab asset to place as virtual content, such as a basic cube.

## Placing Content on the Map<a href="#placing-content-on-the-map" class="hash-link" aria-label="Direct link to Placing Content on the Map" title="Direct link to Placing Content on the Map">​</a>

1.  Select `DeviceMappingDemo` from the **Hierarchy**, then, in the **Inspector**, click **Add Component**. Search for and add a **New Script** to it, then name it `Tracker.cs`.

2.  Open `Tracker.cs` and replace its contents with the following snippet:

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    using System.Collections;
    using System.IO;
    using NianticSpatial.NSDK.AR.Mapping;
    using NianticSpatial.NSDK.AR.PersistentAnchors;
    using NianticSpatial.NSDK.AR.VPS2;
    using UnityEngine;
    using UnityEngine.UI;
    using UnityEngine.XR.ARFoundation;
    using UnityEngine.XR.ARSubsystems;

    public class Tracker : MonoBehaviour
    {

    }
    ```

    </div>

    </div>

3.  In the **Hierarchy**, select the **XROrigin**, then, in the **Inspector**, click **Add Component** and add an **`ARVps2Manager`** to it.

4.  Add a reference to the manager and an `Awake()` method so VPS2 uses **device map localization** (and turns off VPS map and universal localization for this tutorial flow):

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    [SerializeField]
    private ARVps2Manager _vps2Manager;

    private void Awake()
    {
        _vps2Manager.DeviceMapLocalizationEnabled = true;
        _vps2Manager.VpsMapLocalizationEnabled = false;
        _vps2Manager.UniversalLocalizationEnabled = false;
    }
    ```

    </div>

    </div>

    VPS2 reads these settings when the subsystem starts. Set them in `Awake()` or match them on the **ARVps2Manager** component in the Inspector before play.

5.  Add UI elements to the `Tracker` script for choosing a device map:

    1.  Add a button to start and stop tracking:
        1.  Right-click in the **Hierarchy**, then open the **Create** menu and select **Button** from the **UI** sub-menu. This will create a **Canvas** element and add the button to it.
        2.  In the script, add a serialized field for the button.
    2.  Create a private method, `OnStartTrackingClicked()`, and have it listen for button clicks in `Start()`.

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    [SerializeField]
    private Button _startTrackingButton;

    private void Start()
    {
        _startTrackingButton.onClick.AddListener(OnStartTrackingClicked);
    }

    // When tracking button is clicked
    private void OnStartTrackingClicked()
    {
    }
    ```

    </div>

    </div>

6.  Add logic to `Tracker.cs` that toggles the tracking state when the button is clicked:

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    private ARVps2Anchor _anchor;
    // variable for reference to the object on the map
    private GameObject _anchorVisualObject;
    private bool _isTrackingRunning;

    // When tracking button is clicked
    private void OnStartTrackingClicked()
    {
        var buttonText = _startTrackingButton.GetComponentInChildren<Text>();
        if (_isTrackingRunning)
        {
            // Stop tracking if running and clean up anchor
            if (_anchor)
            {
                _vps2Manager.RemoveAnchor(_anchor);
                _anchor = null;
                _anchorVisualObject = null;
            }
            buttonText.text = "Start Tracking";
            _isTrackingRunning = false;
        }
        // otherwise, change the button to "stop" and start tracking
        else
        {
            buttonText.text = "Stop Tracking";
            _isTrackingRunning = true;
            StartCoroutine(RestartTracking());
        }
    }
    ```

    </div>

    </div>

7.  Add the next code snippet to restart tracking using the map from the file:

    1.  We need to clean up some elements before restarting tracking:
        1.  If there is already an anchor, remove it. Wait a moment before continuing because the anchor can take an extra frame to be removed in some situations.
        2.  Disable and re-enable `ARVps2Manager` to restart tracking. We wait a moment between stopping and starting so that subsystem state is cleaned up asynchronously.
    2.  Once cleanup is done, we can set the saved serialized map data from the file we saved it into earlier.
        1.  Read the serialized map data into memory and pass it to `DeviceMapAccessController.AddMap()` so that it will be tracked.
    3.  Call `ARVps2Manager.TryTrackAnchor` with a **base64** payload string (see snippet) to start tracking again using a new anchor.

8.  After adding this snippet to `Tracker.cs`, open the **Hierarchy** and select **DeviceMappingDemo**. Then, in the **Inspector**, find `Tracker.cs` and assign **ARVps2Manager** from the **XROrigin** to the fields in the script.

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    private DeviceMapAccessController _deviceMapAccessController;

    private void Awake()
    {
        _vps2Manager.DeviceMapLocalizationEnabled = true;
        _vps2Manager.VpsMapLocalizationEnabled = false;
        _vps2Manager.UniversalLocalizationEnabled = false;
        _deviceMapAccessController = DeviceMapAccessController.Acquire();
    }

    private IEnumerator RestartTracking()
    {
        if (_anchor)
        {
            _vps2Manager.RemoveAnchor(_anchor);
            _anchor = null;
            _anchorVisualObject = null;
        }
        // wait a moment after removing anchor
        yield return null;

        _vps2Manager.enabled = false;

        // wait a moment before toggling tracking
        yield return null;

        _vps2Manager.enabled = true;

        // Read a new device map from file
        var path = Path.Combine(Application.persistentDataPath, Mapper.MapFileName);
        var serializedDeviceMap = File.ReadAllBytes(path);

        // Assign the device map to the DeviceMapAccessController
        _deviceMapAccessController.AddMap(serializedDeviceMap);

        // Create a root anchor payload and track it
        if (_deviceMapAccessController.CreateRootAnchor(out var anchorPayload))
        {
            _vps2Manager.TryTrackAnchor(anchorPayload, out _anchor);
        }
    }
    ```

    </div>

    </div>

9.  When the anchor enters the **Tracking** state, place virtual objects according to the device map:

    1.  Create variables to hold the virtual content:
        1.  Add a serialized field variable for the prefab, then assign it to yours.
    2.  Replace your earlier `Start()` method so you subscribe once to the button and to **`ARVps2Manager.trackablesChanged`** (VPS2 consolidates anchor add/update/remove into this event).
    3.  Add `OnDestroy()` to unsubscribe, and implement the handler:
        1.  For the `ARVps2Anchor` reference you received from `TryTrackAnchor`, when its `trackingState` is `Tracking`, instantiate an object from the prefab with the tracked anchor as its parent.

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    [SerializeField]
    private GameObject _locationAnchorPrefab;

    private void Start()
    {
        _startTrackingButton.onClick.AddListener(OnStartTrackingClicked);
        _vps2Manager.trackablesChanged += OnVps2TrackablesChanged;
    }

    private void OnDestroy()
    {
        if (_vps2Manager != null)
        {
            _vps2Manager.trackablesChanged -= OnVps2TrackablesChanged;
        }
        _deviceMapAccessController?.Release();
        _deviceMapAccessController = null;
    }

    // Event listener for anchor changes
    private void OnVps2TrackablesChanged(ARTrackablesChangedEventArgs<ARVps2Anchor> args)
    {
        foreach (var u in args.updated)
        {
            // Handle anchor updates
        }
        // `args` contains added anchors and deleted anchors. You can process them as needed
    }
    ```

    </div>

    </div>

Your virtual object should now be visible!

## Completed Tracker Script<a href="#completed-tracker-script" class="hash-link" aria-label="Direct link to Completed Tracker Script" title="Direct link to Completed Tracker Script">​</a>

If you are having trouble with your tracking script, compare it to the finished product here!

Click to reveal the final Tracker.cs script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System.Collections;
using System.IO;
using NianticSpatial.NSDK.AR.Mapping;
using NianticSpatial.NSDK.AR.PersistentAnchors;
using NianticSpatial.NSDK.AR.VPS2;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;

public class Tracker : MonoBehaviour
{
    [SerializeField]
    private ARVps2Manager _vps2Manager;

    [SerializeField]
    private GameObject _locationAnchorPrefab;

    [SerializeField]
    private Button _startTrackingButton;

    private GameObject _anchorVisualObject;
    private ARVps2Anchor _anchor;
    private bool _isTrackingRunning;

    private DeviceMapAccessController _deviceMapAccessController;

    private void Awake()
    {
        _vps2Manager.DeviceMapLocalizationEnabled = true;
        _vps2Manager.VpsMapLocalizationEnabled = false;
        _vps2Manager.UniversalLocalizationEnabled = false;
        _deviceMapAccessController = DeviceMapAccessController.Acquire();
    }

    private void Start()
    {
        _vps2Manager.trackablesChanged += OnVps2TrackablesChanged;
        _startTrackingButton.onClick.AddListener(OnStartTrackingClicked);
    }

    private void OnDestroy()
    {
        if (_vps2Manager != null)
        {
            _vps2Manager.trackablesChanged -= OnVps2TrackablesChanged;
        }
    }

    private void OnStartTrackingClicked()
    {
        var buttonText = _startTrackingButton.GetComponentInChildren<Text>();
        if (_isTrackingRunning)
        {
            if (_anchor)
            {
                _vps2Manager.RemoveAnchor(_anchor);
                _anchor = null;
                _anchorVisualObject = null;
            }
            buttonText.text = "Start Tracking";
            _isTrackingRunning = false;
        }
        else
        {
            buttonText.text = "Stop Tracking";
            _isTrackingRunning = true;
            StartCoroutine(RestartTracking());
        }
    }

    private IEnumerator RestartTracking()
    {
        if (_anchor)
        {
            _vps2Manager.RemoveAnchor(_anchor);
            _anchor = null;
            _anchorVisualObject = null;
        }
        // wait a moment after removing anchor
        yield return null;

        _vps2Manager.enabled = false;

        // wait a moment before toggling tracking
        yield return null;

        _vps2Manager.enabled = true;

        // Read a new device map from file
        var path = Path.Combine(Application.persistentDataPath, Mapper.MapFileName);
        var serializedDeviceMap = File.ReadAllBytes(path);

        // Assign the device map to the DeviceMapAccessController
        _deviceMapAccessController.AddMap(serializedDeviceMap);

        // Create a root anchor payload and track it
        if (_deviceMapAccessController.CreateRootAnchor(out var anchorPayload))
        {
            _vps2Manager.TryTrackAnchor(anchorPayload, out _anchor);
        }
    }

    private void OnVps2TrackablesChanged(ARTrackablesChangedEventArgs<ARVps2Anchor> args)
    {
        if (_anchor == null || _locationAnchorPrefab == null)
            return;

        void ConsiderAnchor(ARVps2Anchor anchor)
        {
            if (anchor != _anchor)
                return;
            if (anchor.trackingState == TrackingState.Tracking && !_anchorVisualObject)
            {
                _anchorVisualObject = Instantiate(_locationAnchorPrefab, _anchor.transform);
                Debug.Log("Tracking");
            }
        }

        foreach (var a in args.added)
            ConsiderAnchor(a);
        foreach (var u in args.updated)
            ConsiderAnchor(u);
    }
}
```

</div>

</div>

</div>

</div>

</div>

</div>
