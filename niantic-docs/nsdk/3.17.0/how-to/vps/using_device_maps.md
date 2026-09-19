---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/using_device_maps/
title: How to Place Virtual Content Using a Device Map
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Place Virtual Content Using a Device Map

</div>

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

This feature is experimental and may not work as expected. For more information about it, see the [Device Mapping Feature page](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/device_mapping/).

</div>

</div>

Now that we have created a device map and saved it to a file, we can read it to place virtual objects in the AR scene. In this how-to, we will cover reading a device map file into your Unity project and how to use it to place content.

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

Before you start, complete [How to Create a Device Map](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/adding_device_mapping/). You will need the Unity project from that tutorial for this one. You will also need one prefab asset to place as virtual content, such as a basic cube.

## Placing Content on the Map<a href="#placing-content-on-the-map" class="hash-link" aria-label="Direct link to Placing Content on the Map" title="Direct link to Placing Content on the Map">​</a>

1.  Select `DeviceMappingDemo` from the **Hierarchy**, then, in the **Inspector**, click **Add Component**. Search for and add a **New Script** to it, then name it `Tracker.cs`.

2.  Open `Tracker.cs` and replace its contents with the following snippet:

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    using System.Collections;
    using System.IO;
    using Niantic.Lightship.AR.Mapping;
    using Niantic.Lightship.AR.PersistentAnchors;
    using UnityEngine;
    using UnityEngine.UI;
    using UnityEngine.XR.ARSubsystems;

    public class Tracker : MonoBehaviour
    {

    }
    ```

    </div>

    </div>

3.  In the **Hierarchy**, select the **XROrigin**, then, in the **Inspector**, click **Add Component** and add an `ARPersistentAnchorManager` to it.

4.  Now that we have a persistent anchor manager, we can tell it what kind of mapping we want to use. Add the following snippet to the `Tracker` class:

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    // initialize the manager
    [SerializeField]
    private ARPersistentAnchorManager _persistentAnchorManager;

    private void Start()
    {
        // tell it we want device mapping (aka "slick" mapping)
        _persistentAnchorManager.DeviceMappingLocalizationEnabled = true;
        _persistentAnchorManager.CloudLocalizationEnabled = false;
        // enable continuous localization to mitigate tracking drift
        _persistentAnchorManager.ContinuousLocalizationEnabled = true;
        _persistentAnchorManager.TemporalFusionEnabled = true;
        _persistentAnchorManager.TransformUpdateSmoothingEnabled = true;
        _persistentAnchorManager.DeviceMappingLocalizationRequestIntervalSeconds = 0.1f;

        // start the manager with our options
        StartCoroutine(_persistentAnchorManager.RestartSubsystemAsyncCoroutine());
    }
    ```

    </div>

    </div>

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
        // Add this below the previous section's code in Start()
        // Listen for button click event
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
    private ARPersistentAnchor _anchor;
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
                _persistentAnchorManager.DestroyAnchor(_anchor);
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

    1.  Add a serialized field for the `ARDeviceMappingManager`.
    2.  We need to clean up some elements before restarting tracking:
        1.  If there is already an anchor, destroy it. Wait a moment before continuing because the anchor can take an extra frame to be destroyed in some situations.
        2.  Disable and re-enable `ARPersistentAnchorManager` to restart tracking. We wait a moment between stopping and starting so that the location data and location manager data are cleaned up asynchronously.
    3.  Once cleanup is done, we can create an `ARDeviceMap` by reading the saved serialized map data from the file we saved it into earlier.
        1.  Read the serialized map data into memory, then create a new `ARDeviceMap` and pass it to `ARDeviceMappingManager.SetDeviceMap()` so that it will be tracked.
    4.  Call `ARPersistentAnchorManager.TryTrackAnchor()` to start tracking again using a new anchor.

8.  After adding this snippet to `Tracker.cs`, open the **Hierarchy** and select **DeviceMappingDemo**. Then, in the **Inspector**, find `Tracker.cs` and assign **ARDeviceMappingManager** from the **XROrigin** to the field in the script.

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    [SerializeField]
    private ARDeviceMappingManager _deviceMappingManager;

    private IEnumerator RestartTracking()
    {
        if (_anchor)
        {
            _persistentAnchorManager.DestroyAnchor(_anchor);
            _anchor = null;
            _anchorVisualObject = null;
        }
        // wait a moment after destroying anchor
        yield return null;

        _persistentAnchorManager.enabled = false;

        // wait a moment before toggling tracking
        yield return null;

        _persistentAnchorManager.enabled = true;

        // Read a new device map from file
        var path = Path.Combine(Application.persistentDataPath, Mapper.MapFileName);
        var serializedDeviceMap = File.ReadAllBytes(path);
        var deviceMap = ARDeviceMap.CreateFromSerializedData(serializedDeviceMap);

        // Assign the device map to the mapping manager
        _deviceMappingManager.SetDeviceMap(deviceMap);

        // Set up tracking with a new anchor
        _persistentAnchorManager.TryTrackAnchor(
            new ARPersistentAnchorPayload(deviceMap.GetAnchorPayload()),
            out _anchor);
    }
    ```

    </div>

    </div>

9.  When the anchor enters the "tracking" state, place virtual objects according to the device map:

    1.  Create variables to hold the virtual content:
        1.  Add a serialized field variable for the prefab, then assign it to yours.
    2.  In `Start()`, subscribe an event listener to changes to the anchor state.
    3.  Create a function to handle event updates:
        1.  If the anchor is in the tracking state, instantiate an object from the prefab with the tracked anchor as its parent.

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    [SerializeField]
    private GameObject _locationAnchorPrefab;

    private void Start()
    {
        // Add this below the previous section's code in Start()
        // Listen for anchor updates and catch them
        _persistentAnchorManager.arPersistentAnchorStateChanged += OnArPersistentAnchorStateChanged;
    }

    // Event listener for anchor updates
    private void OnArPersistentAnchorStateChanged(ARPersistentAnchorStateChangedEventArgs args)
    {
        if (args.arPersistentAnchor.trackingState == TrackingState.Tracking)
        {
            if (!_anchorVisualObject)
            {
                _anchorVisualObject = Instantiate(_locationAnchorPrefab, _anchor.transform);
                Debug.Log("Tracking");
            }
        }
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
using Niantic.Lightship.AR.Mapping;
using Niantic.Lightship.AR.PersistentAnchors;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.XR.ARSubsystems;

public class Tracker : MonoBehaviour
{
    // initialize the managers, prefab, menu, and map file I/O
    [SerializeField]
    private ARPersistentAnchorManager _persistentAnchorManager;

    [SerializeField]
    private ARDeviceMappingManager _deviceMappingManager;

    [SerializeField]
    private GameObject _locationAnchorPrefab;

    [SerializeField]
    private Button _startTrackingButton;

    private GameObject _anchorVisualObject;
    private ARPersistentAnchor _anchor;
    private bool _isTrackingRunning;

    private void Start()
    {
        // Event listeners for anchor and drop-down menu
        _persistentAnchorManager.arPersistentAnchorStateChanged += OnArPersistentAnchorStateChanged;
        _startTrackingButton.onClick.AddListener(OnStartTrackingClicked);

        // tell it we want device mapping (aka "slick" mapping)
        _persistentAnchorManager.DeviceMappingLocalizationEnabled = true;
        _persistentAnchorManager.CloudLocalizationEnabled = false;
        // enable continuous localization to mitigate tracking drift
        _persistentAnchorManager.ContinuousLocalizationEnabled = true;
        _persistentAnchorManager.TemporalFusionEnabled = true;
        _persistentAnchorManager.TransformUpdateSmoothingEnabled = true;
        _persistentAnchorManager.DeviceMappingLocalizationRequestIntervalSeconds = 0.1f;

        // restart the manager with our options
        StartCoroutine(_persistentAnchorManager.RestartSubsystemAsyncCoroutine());
    }

    // When tracking button is clicked
    private void OnStartTrackingClicked()
    {
        var buttonText = _startTrackingButton.GetComponentInChildren<Text>();
        if (_isTrackingRunning)
        {
            // Stop tracking if running
            if (_anchor)
            {
                _persistentAnchorManager.DestroyAnchor(_anchor);
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
            _persistentAnchorManager.DestroyAnchor(_anchor);
            _anchor = null;
            _anchorVisualObject = null;
        }
        yield return null;

        _persistentAnchorManager.enabled = false;

        // start tracking after stop tracking needs "some" time in between...
        yield return null;

        _persistentAnchorManager.enabled = true;

        // Read a new device map from file
        var path = Path.Combine(Application.persistentDataPath, Mapper.MapFileName);
        var serializedDeviceMap = File.ReadAllBytes(path);
        var deviceMap = ARDeviceMap.CreateFromSerializedData(serializedDeviceMap);

        // Assign the device map to the mapping manager
        _deviceMappingManager.SetDeviceMap(deviceMap);

        // Set up tracking with a new anchor
        _persistentAnchorManager.TryTrackAnchor(
            new ARPersistentAnchorPayload(deviceMap.GetAnchorPayload()),
            out _anchor);
    }

    // Event listener for anchor updates
    private void OnArPersistentAnchorStateChanged(ARPersistentAnchorStateChangedEventArgs args)
    {
        if (args.arPersistentAnchor.trackingState == TrackingState.Tracking)
        {
            if (!_anchorVisualObject)
            {
                _anchorVisualObject = Instantiate(_locationAnchorPrefab, _anchor.transform);
                Debug.Log("Tracking");
            }
        }
    }
}
```

</div>

</div>

</div>

</div>

</div>

</div>
