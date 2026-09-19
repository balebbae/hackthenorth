---
source: https://www.nianticspatial.com/docs/nsdk/how-to/ar/world_pose/
title: How to Build an App Using the World Pose System (WPS)
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Build an App Using the World Pose System (WPS)

</div>

NSDK offers a World Pose System (WPS) that you can use to get locations and compass heading orientations with better accuracy and stability than standard GPS. In this tutorial, you will learn how to add basic WPS functionality to a Unity project and configure it to localize near you.

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Unity project with ARDK installed, a basic AR scene, and NSDK Occlusion. For more information, see [Set up the Niantic SDK for Unity](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-the-niantic-sdk-for-unity), [Set up a basic AR scene](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-a-basic-ar-scene), and [How to Set Up Real-World Occlusion](https://www.nianticspatial.com/docs/nsdk/how-to/ar/setup_real_world_occlusion/).

You will also need to create a playback scan. For more information, see [How to Create Datasets for Playback](https://www.nianticspatial.com/docs/nsdk/how-to/playback/create_playback_dataset/).

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

When setting up Occlusion for this How-To, skip step 2 (the "add a cube" section) of [Setting Up Occlusion](https://www.nianticspatial.com/docs/nsdk/how-to/ar/setup_real_world_occlusion/#setting-up-occlusion) and follow the steps of [Setting up Occlusion Suppression](https://www.nianticspatial.com/docs/nsdk/how-to/ar/setup_real_world_occlusion/#setting-up-occlusion-suppression) to exclude the sky and ground when testing your WPS occlusion.

</div>

</div>

## Adding WPS to a Unity Project<a href="#adding-wps-to-a-unity-project" class="hash-link" aria-label="Direct link to Adding WPS to a Unity Project" title="Direct link to Adding WPS to a Unity Project">​</a>

To add WPS to a Unity project:

1.  In the **Hierarchy**, select the `XROrigin`, then, in the **Inspector**, click **Add Component** and add an `ARWorldPositioningObjectHelper` to it. This will also create a `ARWorldPositioningManager` Component.
2.  Still in the **Hierarchy**, expand the `XROrigin` and `Camera Offset` to expose the `Main Camera`, then select it. In the **Inspector**, locate **Clipping Planes** under **Camera** and set the **Far** value to 1000.
3.  In the `ARWorldPositioningObjectHelper` Component, set the **Altitude Mode** to **Camera-relative with smart averaging**.
4.  In the **Assets** folder, right-click and mouse over **Create**, then select **C# Script**. Name the new script `AddWPSObjects`.
5.  Back in the **Hierarchy**, right-click, then select **Create Empty** to add a new `GameObject`. Name it `WPSObjects`. Select `WPSObjects`, then click **Add Component** in the **Inspector** and add `AddWPSObjects` as a script component.

<img src="https://www.nianticspatial.com/docs/assets/images/wps_components-7e018e60814e2c5fb3259c67f92a865c.png" width="400" alt="WPS components in Unity with proper configuration" />

## Writing the WPS Script<a href="#writing-the-wps-script" class="hash-link" aria-label="Direct link to Writing the WPS Script" title="Direct link to Writing the WPS Script">​</a>

For the basic use of WPS in a script, initialize it as normal, then call `AddOrUpdateObject` from `ARWorldPositioningObjectHelper` to update objects with WPS data. The example below, **AddWPSObjects.cs**, creates a cube, then uses `ARWorldPositioningObjectHelper` to place it dynamically in the scene.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

When trying this out, set the latitude and longitude in the script to a location close to you (for live testing) or the playback scan (for remote testing).

</div>

</div>

Click to reveal AddWPSObjects.cs

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using NianticSpatial.NSDK.AR.WorldPositioning;

public class AddWPSObjects : MonoBehaviour
{
    [SerializeField] ARWorldPositioningObjectHelper positioningHelper;

    // Start is called before the first frame update
    void Start()
    {
        // replace the coordinates here with your location
        double latitude = 37.79534850764306;
        double longitude = -122.39243231803636;
        double altitude = 0.0; // We're using camera-relative positioning so make the cube appear at the same height as the camera

        // instantiate a cube, scale it up for visibility (make it even bigger if you need), then update its location
        GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
        cube.transform.localScale *= 2.0f;
        positioningHelper.AddOrUpdateObject(cube, latitude, longitude, altitude, Quaternion.identity);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
```

</div>

</div>

</div>

</div>

Add the **AddWPSObjects** component to your `WPSObjects` GameObject, then populate **positioningHelper** field with the `ARWorldPositioningManager` component from the `XROrigin` GameObject.

### Setting a Location<a href="#setting-a-location" class="hash-link" aria-label="Direct link to Setting a Location" title="Direct link to Setting a Location">​</a>

Before you can use WPS in your project, you will need to know the latitude and longitude coordinates of the location where you created your playback scan. To get the coordinates of the location:

1.  Open <a href="https://maps.google.com" target="_blank" rel="noopener noreferrer">Google Maps</a> and find the location where you captured your playback scan.
2.  Click the map to add a marker.
3.  Right-click the marker, then select the coordinates at the top of the menu to copy them to your clipboard.
4.  Paste the latitude and longitude values in **AddWPSObjects.cs**.

Afterwards, build and run the application to test it out. The cube should appear where you placed it!

### Querying live GPS location<a href="#querying-live-gps-location" class="hash-link" aria-label="Direct link to Querying live GPS location" title="Direct link to Querying live GPS location">​</a>

Alternatively, query Unity's **Input.location** API to use the device's live GPS reading:

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

If you're using Android, it might take a moment for tracking to start and the cube to appear

</div>

</div>

Click to reveal modified AddWPSObjects.cs

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using NianticSpatial.NSDK.AR.WorldPositioning;

public class AddWPSObjects : MonoBehaviour
{
    [SerializeField] ARWorldPositioningObjectHelper positioningHelper;

    // Start is called before the first frame update
    IEnumerator Start()
    {
        Input.location.Start();
        
        // Waits until the location service initializes
        int maxWait = 60;
        while (Input.location.status != LocationServiceStatus.Running && maxWait > 0)
        {
            yield return new WaitForSeconds(1);
            maxWait--;
        }
        
        // If the service didn't initialize, this cancels location service use.
        if (maxWait < 1)
        {
            Debug.LogError("GPS timed out with status " +  Input.location.status);
            yield break;
        }

        double latitude = Input.location.lastData.latitude;
        double longitude = Input.location.lastData.longitude;
        double altitude = 0.0; // We're using camera-relative positioning, so make the cube appear at the same height as the camera
        Debug.LogError("GPS started successfully with lat: " + latitude + ", long: " + longitude);

        // Instantiate a cube and scale it up for visibility (make it even bigger if you need to).
        // Initially, the cube is invisible.
        // The cube will appear nearby once WorldPositioningStatus == Available.
        // Its position will be continually refined and updated by WPS.
        GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
        cube.transform.localScale *= 2.0f;
        positioningHelper.AddOrUpdateObject(cube, latitude, longitude, altitude, Quaternion.identity);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
```

</div>

</div>

</div>

</div>

## Comparing WPS and GPS<a href="#comparing-wps-and-gps" class="hash-link" aria-label="Direct link to Comparing WPS and GPS" title="Direct link to Comparing WPS and GPS">​</a>

To show the difference between WPS and GPS, we have also provided an example script that creates a second cube using GPS and displays both at once. Try it out and see the difference for yourself!

Click to reveal the comparison script

<div>

<div class="collapsibleContent_i85q">

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
using UnityEngine;
using NianticSpatial.NSDK.AR.WorldPositioning;
using System;

public class AddWPSObjects : MonoBehaviour
{
    [SerializeField] ARWorldPositioningObjectHelper positioningHelper;
    [SerializeField] Camera trackingCamera;

    // TODO: replace the coordinates here with your location. This defaults to the San Francisco ferry building!
    double latitude = 37.795328;
    double longitude = -122.392394;
    double altitude = 0.0; // We're using camera-relative positioning so make the cube appear at the same height as the camera

    // Start is called before the first frame update
    void Start()
    {
        // instantiate a cube, scale it up for visibility (make it even bigger if you need), then update its location
        GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
        cube.transform.localScale *= 2.0f;
        positioningHelper.AddOrUpdateObject(cube, latitude, longitude, altitude, Quaternion.identity);
    }

    // Create a second cube and move it to the position predicted using the raw GPS + compass
    private GameObject gpsCube = null;
    void Update()
    { 
        // Create a second cube if we don't already have one:
        if(gpsCube == null)
        {
            gpsCube = GameObject.CreatePrimitive(PrimitiveType.Cube);
            gpsCube.GetComponent<Renderer>().material.color = Color.red;
        }

        if (Input.location.isEnabledByUser)
        {
            double deviceLatitude = Input.location.lastData.latitude;
            double deviceLongitude = Input.location.lastData.longitude;
            
            Vector2 eastNorthOffsetMetres = EastNorthOffset(latitude,longitude, deviceLatitude, deviceLongitude);
            Vector3 trackingOffsetMetres = Quaternion.Euler(0, 0, Input.compass.trueHeading)*new Vector3(eastNorthOffsetMetres[0], (float)altitude, eastNorthOffsetMetres[1]);
            Vector3 trackingMetres = trackingCamera.transform.localPosition + trackingOffsetMetres;
            gpsCube.transform.localPosition = trackingMetres;
        }
    }

    public Vector2 EastNorthOffset(double latitudeDegreesA, double longitudeDegreesA, double latitudeDegreesB, double longitudeDegreesB)
    {
        double DEGREES_TO_METRES = 111139.0;
        float lonDifferenceMetres = (float)(Math.Cos((latitudeDegreesA+latitudeDegreesB)*0.5* Math.PI / 180.0) * (longitudeDegreesA - longitudeDegreesB) * DEGREES_TO_METRES);
        float latDifferenceMetres = (float)((latitudeDegreesA - latitudeDegreesB) * DEGREES_TO_METRES);
        return new Vector2(lonDifferenceMetres,latDifferenceMetres);
    }
}
```

</div>

</div>

</div>

</div>

Update the **latitude** and **longitude** fields with the GPS coordinates that you got from the **Setting a Location** section to compare WPS to GPS.

## Example Result<a href="#example-result" class="hash-link" aria-label="Direct link to Example Result" title="Direct link to Example Result">​</a>

<img src="https://www.nianticspatial.com/docs/assets/images/wps_gandhi-cfa2fd674c6cca8193692897713e8dad.png" width="236" alt="Occluding a cube with a statue of Gandhi using WPS" />

</div>

</div>
