---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/features/location_ar_vps_coverage/
title: VPS Coverage API
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Querying VPS Coverage for AR Locations at Runtime

</div>

The VPS Coverage API provides functionality for discovering AR Locations at runtime to display them on maps and use them as localization targets for an **ARLocationManager**.

## Configuring the CoverageClientManager<a href="#configuring-the-coverageclientmanager" class="hash-link" aria-label="Direct link to Configuring the CoverageClientManager" title="Direct link to Configuring the CoverageClientManager">​</a>

<img src="https://www.nianticspatial.com/docs/assets/images/coverage_client_manager-b98e80920c3c0c32e59adb27303fb341.png" width="500" alt="Coverage Client Manager" />

**CoverageClientManager** can either be added to your scene in the Unity Editor or at runtime through `AddComponent`. It can either query for `ARLocations` around the user's current GPS location or one they specify (for example, remotely viewing a city on a map). **CoverageClientManager** also provides configuration for a `QueryRadius` which defines the radius (in meters) to query around the GPS location.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

Your Unity project will need location usage permissions set up for the build target. For iOS, a **Location Usage Description** is required in **Project Settings**. For Android, the user will need to grant the `ACCESS_FINE_LOCATION` permission, which the **CoverageClientManager** will request upon use.

</div>

</div>

The following code snippet demonstrates setting up and configuring the **CoverageClientManager** to query for `ARLocations` within 1km of the user's current location.

Click to reveal CoverageClientManagerExample.cs

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using Niantic.Lightship.AR.VpsCoverage;
using UnityEngine;

public class CoverageClientManagerExample : MonoBehaviour
{
    [SerializeField]
    private CoverageClientManager CoverageClientManager;

    public void QueryAroundUser()
    {
        // If not provided, create one on the current gameobject
        if (!CoverageClientManager)
        {
            CoverageClientManager = gameObject.AddComponent<CoverageClientManager>();
        }

        // Use the current location of the device to query coverage. The query radius is set to 1000 meters.
        CoverageClientManager.UseCurrentLocation = true;
        CoverageClientManager.QueryRadius = 1000;
        
        CoverageClientManager.TryGetCoverage(OnCoverageResult);
    }

    private void OnCoverageResult(AreaTargetsResult result)
    {
        // Currently does nothing
    }
}
```

</div>

</div>

</div>

</div>

## Using Coverage Results<a href="#using-coverage-results" class="hash-link" aria-label="Direct link to Using Coverage Results" title="Direct link to Using Coverage Results">​</a>

The [AreaTargetsResult](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/AreaTargetsResult/) class returns information from the VPS Coverage API query. Check that the [Status](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/AreaTargetsResult/) is **Success** or handle failure cases as needed. Most of the relevant data from the VPS Coverage API query will be contained in the `AreaTargets` list.

### Area Targets and Their Contents<a href="#area-targets-and-their-contents" class="hash-link" aria-label="Direct link to Area Targets and Their Contents" title="Direct link to Area Targets and Their Contents">​</a>

Each [AreaTarget](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/AreaTarget/) contains two fields, the [CoverageArea](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/CoverageArea/) and [LocalizationTarget](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/LocalizationTarget/).

A **CoverageArea** defines a 2-dimensional polygon in real-world space where Location AR is supported. For example, the `Shape` property can be used to draw an overlay on a map using `LatLng` points, while the `LocalizabilityQuality` property reports the overall quality of tracking in the area.

A **LocalizationTarget** defines a point in real-world space where VPS localization is supported. The `Name` and `ImageURL` properties can be used to create a information card about a specific location, while the `DefaultAnchor` property can be passed into the **ARLocationManager** to start tracking.

For more information on these fields and their properties, see the [API documentation](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/AreaTarget/).

This snippet combines **CoverageArea** and **LocalizationTarget** data to sort and filter `AreaTargetsResults` into a usable list:

Click to reveal the Area Targets example script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using Niantic.Lightship.AR.VpsCoverage;
using UnityEngine;

public class CoverageClientManagerExample : MonoBehaviour
{
    [SerializeField]
    private CoverageClientManager CoverageClientManager;

    public void QueryAroundUser()
    {
        CoverageClientManager.TryGetCoverage(OnCoverageResult);
    }

    private void OnCoverageResult(AreaTargetsResult areaTargetsResult)
    {
        if (areaTargetsResult.Status == ResponseStatus.Success)
        {
            // Sort the area targets by distance from the query location
            areaTargetsResult.AreaTargets.Sort((a, b) =>
                a.Area.Centroid.Distance(areaTargetsResult.QueryLocation).CompareTo(
                    b.Area.Centroid.Distance(areaTargetsResult.QueryLocation)));

            // Only consider the 5 nearest production quality areas
            var maxCount = 5;
            foreach (var result in areaTargetsResult.AreaTargets)
            {
                if (result.Area.LocalizabilityQuality != CoverageArea.Localizability.PRODUCTION)
                {
                    continue;
                }
                
                Debug.Log($"Got a localization target: {result.Target.Name}, anchor payload: {result.Target.DefaultAnchor}");
                maxCount--;
                if (maxCount == 0)
                {
                    break;
                }
            }
        }
        else
        {
            Debug.LogError($"Coverage query failed with status: {areaTargetsResult.Status}");
        }
    }
}
```

</div>

</div>

</div>

</div>

### Downloading Hint Images<a href="#downloading-hint-images" class="hash-link" aria-label="Direct link to Downloading Hint Images" title="Direct link to Downloading Hint Images">​</a>

Each **LocalizationTarget** contains an [ImageURL](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/LocalizationTarget/#ImageURL) which points to a hosted hint image corresponding to the **LocalizationTarget**. This information can be used to guide users to the real-world location to localize against. The **CoverageClientManager** contains a few utility methods to download and create a `Texture` with the hint image, as in the following code snippet:

Click to reveal the hint image code snippet

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using Niantic.Lightship.AR.VpsCoverage;
using UnityEngine;

public class CoverageClientManagerExample : MonoBehaviour
{
    [SerializeField]
    private CoverageClientManager CoverageClientManager;

    public void QueryAroundUser()
    {
        CoverageClientManager.TryGetCoverage(OnCoverageResult);
    }

    private async void OnCoverageResult(AreaTargetsResult areaTargetsResult)
    {
        if (areaTargetsResult.Status == ResponseStatus.Success)
        {
            foreach (var result in areaTargetsResult.AreaTargets)
            {
                if (string.IsNullOrEmpty(result.Target.ImageURL))
                {
                    continue;
                }

                var hintTexture = await CoverageClientManager.TryGetImageFromUrl(result.Target.ImageURL);
                
                // Do something with the texture
            }
        }
        else
        {
            Debug.LogError($"Coverage query failed with status: {areaTargetsResult.Status}");
        }
    }
}
```

</div>

</div>

</div>

</div>

Due to the performance impact of blocking on downloads and texture generation, it is recommended to call this API asynchronously. We also recommend limiting the number of images downloaded at a time rather than handling every image in the response.

## Using CoverageClientManager Output in ARLocationManager<a href="#using-coverageclientmanager-output-in-arlocationmanager" class="hash-link" aria-label="Direct link to Using CoverageClientManager Output in ARLocationManager" title="Direct link to Using CoverageClientManager Output in ARLocationManager">​</a>

After getting a list of nearby **AreaTargets**, the user or application can select a specific **LocalizationTarget** to use as an **ARLocation** to track. The following example chooses the first result in the response list as the **ARLocation** to track.

Click to reveal the example script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using Niantic.Lightship.AR.LocationAR;
using Niantic.Lightship.AR.PersistentAnchors;
using Niantic.Lightship.AR.VpsCoverage;
using UnityEngine;

public class CoverageClientManagerExample : MonoBehaviour
{
    [SerializeField]
    private CoverageClientManager CoverageClientManager;

    [SerializeField]
    private ARLocationManager ArLocationManager;

    public void QueryAroundUser()
    {
        CoverageClientManager.TryGetCoverage(OnCoverageResult);
    }

    private void OnCoverageResult(AreaTargetsResult areaTargetsResult)
    {
        if (areaTargetsResult.Status == ResponseStatus.Success)
        {
            var firstResult = areaTargetsResult.AreaTargets[0];
            var anchorPayloadString = firstResult.Target.DefaultAnchor;

            if (string.IsNullOrEmpty(anchorPayloadString))
            {
                // If this area has no anchor payload, don't do anything
                // Select a different area target in a real application
                Debug.LogError($"No anchor found for {firstResult.Target.Name}");
                return;
            }

            var anchorPayload = new ARPersistentAnchorPayload(anchorPayloadString);

            var locationGameObject = new GameObject();
            var arLocation = locationGameObject.AddComponent<ARLocation>();
            arLocation.Payload = anchorPayload;
                
            ArLocationManager.SetARLocations(arLocation);
            ArLocationManager.StartTracking();
        }
        else
        {
            Debug.LogError($"Coverage query failed with status: {areaTargetsResult.Status}");
        }
    }
}
```

</div>

</div>

</div>

</div>

## Surfacing Test Scans Using CoverageClientManager<a href="#surfacing-test-scans-using-coverageclientmanager" class="hash-link" aria-label="Direct link to Surfacing Test Scans Using CoverageClientManager" title="Direct link to Surfacing Test Scans Using CoverageClientManager">​</a>

<img src="https://www.nianticspatial.com/docs/assets/images/private_locations-d4b9faa56ae35f8d4723bfec5bf867c1.png" width="500" alt="Adding Test Scans" />

**CoverageClientManager** will only surface public VPS locations around the query location. However, test scans can be manually added to **CoverageClientManager** to be surfaced in the **AreaTargetsResult** response, regardless of location. Adding the **ARLocationManifest** of a test scan using the **CoverageClientManager** `PrivateARLocations` array will append them to the **AreaTargetsResult** response as if they were queried at runtime. This allows you to use the same flow for discovering public VPS locations and private test scans.

For more information about creating and important test scans, see [Managing Test Scans](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/tooling/manage_test_scans/).

## More Information<a href="#more-information" class="hash-link" aria-label="Direct link to More Information" title="Direct link to More Information">​</a>

- [Creating Location AR Experiences with VPS](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/lightship_vps/)

</div>

</div>
