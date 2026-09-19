---
source: https://www.nianticspatial.com/docs/nsdk/how-to/vps/location_ar_code/
title: How to Use Location AR with Code
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Use Location AR with Code

</div>

This how-to covers:

- Managing and tracking ARLocations through the `ARLocationManager` public API
- Listening for updates to registered ARLocations
- Placing content relative to an ARLocation
- Swapping tracked ARLocations during an AR Session

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

1.  You will need a Unity project with NSDK installed and a set-up basic AR scene. For more information, see [Set up the Niantic SDK for Unity](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-the-niantic-sdk-for-unity) and [Set up a basic AR scene](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-a-basic-ar-scene).
2.  If you have not done so, make sure you have [created a Niantic Spatial account](https://www.nianticspatial.com/docs/nsdk/create_account/) and [authenticated](https://www.nianticspatial.com/docs/nsdk/auth_client/)
3.  Your project must have an `ARLocationManager` in its AR scene to use this How-To. See Step 4 of [Adding a Real-World Location to Unity](https://www.nianticspatial.com/docs/nsdk/how-to/vps/real_world_location_ar/#adding-a-real-world-location-to-unity) to learn how to add an `ARLocationManager` and an `ARLocation` to your project. (For [Swapping ARLocations](#swapping-locations-using-code), you will need more than one `ARLocation`.)

## Registering ARLocations to be Tracked<a href="#registering-arlocations-to-be-tracked" class="hash-link" aria-label="Direct link to Registering ARLocations to be Tracked" title="Direct link to Registering ARLocations to be Tracked">​</a>

To add an `ARLocation` to the `ARLocationManager`, set it by calling SetARLocations on the `ARLocationManager`.

Each time this is called, all previously set locations will be cleared. `SetARLocations()` can only be called before calling `StartTracking()`. After setting the `ARLocations` to be tracked, call StartTracking() on the `ARLocationManager` to start tracking attempts.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

While up to five `ARLocations` can be registered simultaneously, only the first one to successfully track will report updates. Attempting to track multiple locations simultaneously will also increase the network bandwidth usage of tracking. It is recommended to only register a single `ARLocation` to be tracked if you know where the user is located or are targeting a location for tracking. Registering multiple locations is useful if you are unsure exactly what the tracking target will be.

</div>

</div>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using UnityEngine;
using NianticSpatial.NSDK.AR.LocationAR;

public class ARLocationTracking : MonoBehaviour
{
    [SerializeField]
    private ARLocationManager ArLocationManager;

    [SerializeField]
    private ARLocation[] ArLocations;

    public void StartTracking()
    {
        ArLocationManager.SetARLocations(ArLocations);
        ArLocationManager.StartTracking();
    }
}
```

</div>

</div>

## Listening for Updates to Registered ARLocations<a href="#listening-for-updates-to-registered-arlocations" class="hash-link" aria-label="Direct link to Listening for Updates to Registered ARLocations" title="Direct link to Listening for Updates to Registered ARLocations">​</a>

To receive and process updates to registered `ARLocations`, subscribe to locationTrackingStateChanged.

The event arguments contain the updated `ARLocation` and a `bool` called `Tracking` to report their current tracking state. If multiple locations are registered, only the first `ARLocation` to become tracked will fire events. All other `ARLocations` will be automatically removed from the tracking list.

Click to reveal the updated ARLocationTracking script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using UnityEngine;
using NianticSpatial.NSDK.AR.LocationAR;
using NianticSpatial.NSDK.AR.PersistentAnchors;

public class ARLocationTracking : MonoBehaviour
{
    [SerializeField]
    private ARLocationManager ArLocationManager;

    [SerializeField]
    private ARLocation[] ArLocations;

    private bool firstTrackingUpdateReceived = false;

    public void StartTracking()
    {
        ArLocationManager.locationTrackingStateChanged += OnLocationTrackingStateChanged;
        ArLocationManager.SetARLocations(ArLocations);
        ArLocationManager.StartTracking();
    }

    private void OnLocationTrackingStateChanged(ARLocationTrackedEventArgs args)
    {
        var trackedLocation = args.ARLocation;
        var isTracking = args.Tracking;

        if (!firstTrackingUpdateReceived && isTracking){
            Debug.Log("First tracking update received");
            firstTrackingUpdateReceived = true;
        }

        trackedLocation.gameObject.SetActive(isTracking);
    }
}
```

</div>

</div>

</div>

</div>

In this snippet, the `ARLocation` `GameObject` will be enabled and disabled depending on the tracking state. This is useful to handle loss of tracking when the `ARLocation` virtual content is no longer tracking properly and may be offset from the AR camera feed.

### Placing Content Relative to the ARLocation<a href="#placing-content-relative-to-the-arlocation" class="hash-link" aria-label="Direct link to Placing Content Relative to the ARLocation" title="Direct link to Placing Content Relative to the ARLocation">​</a>

Virtual content spawned relative to the `ARLocation` at runtime should be children of the `ARLocation` `GameObject`. This ensures that any tracking updates to the `ARLocation` will update virtual content as well. Also, using local transform methods (`localPosition`, `localRotation`) instead of global transforms (`position`, `rotation`) helps virtual content to stay relative to the `ARLocation`. Local transforms relative to the `ARLocation` can be stored and retrieved in a future session to place virtual content in the same location.

Click to reveal the ARLocationPlacement script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using UnityEngine;
using NianticSpatial.NSDK.AR.LocationAR;

public class ARLocationPlacement : MonoBehaviour
{
    [SerializeField]
    private GameObject GameAsset;
    
    // An ARLocation that is already tracking
    private ARLocation ArLocation;

    // Instantiate an object at some provided pose in world space (ie, the results of a hit test against a plane)
    public GameObject SpawnObjectFromHitTest(Vector3 position, Quaternion rotation)
    {
        var go = Instantiate(GameAsset, position, rotation);
        
        // Retain the previously set pose, but child the asset to the ARLocation
        go.transform.SetParent(ArLocation.transform, true);

        return go;
    }
    
    public void UpdateObjectPosition(Vector3 localPosition, Quaternion localRotation, GameObject go)
    {
        go.transform.localPosition = localPosition;
        go.transform.localRotation = localRotation;
    }
}
```

</div>

</div>

</div>

</div>

### Updating Tracking When Content Is Misaligned<a href="#updating-tracking-when-content-is-misaligned" class="hash-link" aria-label="Direct link to Updating Tracking When Content Is Misaligned" title="Direct link to Updating Tracking When Content Is Misaligned">​</a>

Over time, drift in the ARSession or losing AR tracking can cause `ARLocations` to be misaligned with the real world. In the case of `ARLocation` tracking loss, the `ARLocationManager` will automatically attempt to reconnect with the `ARLocation` upon regaining tracking. However, not all tracking loss events are reported or handled. To manually trigger `ARLocation` tracking, call TryUpdateTracking() on the `ARLocationManager`.

Click to reveal the updated ARLocationTracking script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using UnityEngine;
using NianticSpatial.NSDK.AR.LocationAR;

public class ARLocationTracking : MonoBehaviour
{  
    [SerializeField]
    private ARLocationManager ArLocationManager;

    // This can be attached to a button, or called on a timer
    // Requires that an ARLocation has been previously tracked
    public void UpdateTracking()
    {
        ArLocationManager.TryUpdateTracking();
    }
}
```

</div>

</div>

</div>

</div>

### Stopping Location Tracking<a href="#stopping-location-tracking" class="hash-link" aria-label="Direct link to Stopping Location Tracking" title="Direct link to Stopping Location Tracking">​</a>

`ARLocation` tracking can be stopped by calling StopTracking() on the `ARLocationManager`. This will remove any `ARPersistentAnchors` associated with tracked locations, set all locations to inactive, and return each `ARLocation` to its original parent in the Hierarchy if it still exists. To avoid leaking `GameObjects` between tracking sessions, we recommend despawning and destroying any instantiated `GameObjects` before calling `StopTracking()`.

Click to reveal the StopTracking code snippet

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using UnityEngine;
using NianticSpatial.NSDK.AR.LocationAR;

public class ARLocationTracking : MonoBehaviour
{
  [SerializeField]
  private ARLocationManager ArLocationManager;

  // GameObjects spawned at runtime
  private GameObject[] SpawnedGameObjects;
  
  public void StopTracking()
  {
    foreach (var go in SpawnedGameObjects)
    {
      Destroy(go);
    }
    
    ArLocationManager.StopTracking();
  }
}
```

</div>

</div>

</div>

</div>

### Swapping Locations Using Code<a href="#swapping-locations-using-code" class="hash-link" aria-label="Direct link to Swapping Locations Using Code" title="Direct link to Swapping Locations Using Code">​</a>

`ARLocations` can only be swapped when tracking is stopped. This can be used to update a tracked `ARLocation`, such as when the user moves to a new location. After calling `StopTracking()`, set a new `ARLocation` to be tracked and call `StartTracking()`. If no `SetARLocations` call is made, the previous set of `ARLocations` will be used.

Click to reveal the location swapping code snippet

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using UnityEngine;
using System.Collections;
using NianticSpatial.NSDK.AR.LocationAR;

public class ARLocationTracking : MonoBehaviour
{
    [SerializeField]
    private ARLocationManager ArLocationManager;

    // Already being tracked
    [SerializeField]
    private ARLocation InitialLocation;

    [SerializeField]
    private ARLocation SecondLocation;

    public void UpdateLocationForTracking()
    {
        StartCoroutine(UpdateLocationCoroutine());
    }

    private IEnumerator UpdateLocationCoroutine()
    {
        ArLocationManager.StopTracking();
        ArLocationManager.SetARLocations(SecondLocation);

        // Wait a frame to clear native systems and tracking
        yield return null;
        ArLocationManager.StartTracking();
    }
}
```

</div>

</div>

</div>

</div>

## More Information<a href="#more-information" class="hash-link" aria-label="Direct link to More Information" title="Direct link to More Information">​</a>

- [Creating Location AR Experiences with VPS](https://www.nianticspatial.com/docs/nsdk/features/lightship_vps/)

</div>

</div>
