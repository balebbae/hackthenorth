---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/adding_device_mapping/
title: How to Create a Device Map
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Create a Device Map

</div>

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

This feature is experimental and may not work as expected. For more information about it, see the [Device Mapping Feature page](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/device_mapping/).

</div>

</div>

Before you can use a device map in your AR application, you will need to create and save it. In this tutorial, we will go over how to create and save a device map in your Unity project, as well as some tips for how to get the most out of device mapping.

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Unity project with NSDK installed and a basic AR scene. For more information, see [Setting Up Lightship ARDK](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/) and [Setting up a Basic AR Scene](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/#setting-up-a-basic-ar-scene).

## Creating a Device Map<a href="#creating-a-device-map" class="hash-link" aria-label="Direct link to Creating a Device Map" title="Direct link to Creating a Device Map">​</a>

To create and store a device map:

1.  In the **Hierarchy**, select the **XROrigin**, then, in the **Inspector**, click **Add Component** and add an `ARDeviceMappingManager`.
2.  In the **Hierarchy**, right-click the root of your AR scene, then select **Create Empty**. Name the new object `DeviceMappingDemo`.
3.  Select `DeviceMappingDemo` from the **Hierarchy**, then, in the **Inspector**, click **Add Component**. Search for and add a **New Script** to it, then name it `Mapper.cs`.
4.  Open `Mapper.cs` and replace its contents with the following snippet:

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System;
using System.Collections;
using System.IO;
using Niantic.Lightship.AR.Mapping;
using UnityEngine;
using UnityEngine.UI;

public class Mapper : MonoBehaviour
  {

  }
```

</div>

</div>

4.  Add UI elements for the mapper:

    1.  Right-click in the **Hierarchy**, then open the **Create** menu and select **Button** from the **UI** sub-menu. This will create a **Canvas** element and add the button to it.

5.  Add this snippet to the `Mapper` class to map for ten seconds when the button is pressed:

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    [SerializeField]
    private ARDeviceMappingManager _deviceMappingManager;

    [SerializeField]
    private Button _startMappingButton;

    private void Start()
    {
        _startMappingButton.onClick.AddListener(OnStartMappingClicked);
    }

    // Set this function to be called when button is clicked
    public void OnStartMappingClicked()
    {
        StartCoroutine(RunMapping());
    }

    private IEnumerator RunMapping()
    {
        // disable the button after clicking so that only one map is made at a time
        _startMappingButton.gameObject.SetActive(false);
        _deviceMappingManager.SetDeviceMap(new ARDeviceMap());
        _deviceMappingManager.StartMapping();
        // change this value to map for more or less time
        yield return new WaitForSeconds(10.0f);
        _deviceMappingManager.StopMapping();
        _startMappingButton.gameObject.SetActive(true);
    }
    ```

    </div>

    </div>

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

Ten seconds is enough time to map a small area, such as a desk or couch. If you are mapping a larger area, increase the mapping time to compensate.

</div>

</div>

6.  After the UI code, add an event listener for `ARDeviceMappingManager.DeviceMapFinalized` so that we know when to save the map:

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    private const string MapFileName = "SerializedDeviceMapData";

    private void Start()
    {
        // Add this below the previous section's code in Start()
        _deviceMappingManager.DeviceMapFinalized += OnDeviceMapFinalized;
    }

    private void OnDeviceMapFinalized(ARDeviceMap map)
    {
        if (map.HasValidMap())
        {
            // final map generated. save to the file system
            var serializedDeviceMap = map.Serialize();
            var path = Path.Combine(Application.persistentDataPath, MapFileName);
            File.WriteAllBytes(path, serializedDeviceMap);
            Debug.Log($"Map saved");
        }
        else
        {
            Debug.LogError("Map was empty");
        }
    }
    ```

    </div>

    </div>

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

A final device map will be generated after `StopMapping()` is called, but it will not be available until the `DeviceMapFinalized` event is invoked. Make sure to **wait for the finalized event** after the button is pressed!

</div>

</div>

## Optional: Show the Mesh While Mapping<a href="#optional-show-the-mesh-while-mapping" class="hash-link" aria-label="Direct link to Optional: Show the Mesh While Mapping" title="Direct link to Optional: Show the Mesh While Mapping">​</a>

By default, `ARDeviceMappingManager` does not provide any visual feedback while mapping an area. By adding meshing to your project, you can visualize your map's coverage and get a sense of where you still need to cover. The mesh cannot exactly show where the device map was generated or its localizability, but it can provide a general idea of the map's area. To learn about how to add meshing to your Lightship project, see <a href="https://lightship.dev/docs/ardk/how-to/ar/meshing_physics_real_world/#creating-the-mesh" target="_blank" rel="noopener noreferrer">Creating a Mesh</a>.

## Device Mapping Tips<a href="#device-mapping-tips" class="hash-link" aria-label="Direct link to Device Mapping Tips" title="Direct link to Device Mapping Tips">​</a>

- Because device mapping relies on a single scan, localization and tracking accuracy depend heavily on how well you scan the area. If you remember one tip, let it be this: **if you are having localization issues, don't be afraid to re-scan!**
- Lighting matters a lot when scanning an area. If the lighting during localization doesn't match the scan, you will need to re-scan. (This includes both outdoor and indoor lighting!)
- For best results, follow these guidelines when scanning:
  - Focus on distinctive objects in the area that are unlikely to move between scanning and localization, such as furniture, household fixtures, or statues.
  - Avoid looking primarily at flat surfaces without color variation, such as the ground, grass, walls, and floors.
  - Move around while scanning! The more viewpoints you see an object from, the better the map of it will be.

## Complete Device Mapping Script<a href="#complete-device-mapping-script" class="hash-link" aria-label="Direct link to Complete Device Mapping Script" title="Direct link to Complete Device Mapping Script">​</a>

If you are having trouble with your mapping script, compare it to the finished product here!

Click here to reveal the final Mapper.cs script

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System;
using System.Collections;
using System.IO;
using Niantic.Lightship.AR.Mapping;
using UnityEngine;
using UnityEngine.UI;

public class Mapper : MonoBehaviour
{
  public const string MapFileName = "SerializedDeviceMapData";

  [SerializeField]
  private ARDeviceMappingManager _deviceMappingManager;

  [SerializeField]
  private Button _startMappingButton;

  private void Start()
  {
      _deviceMappingManager.DeviceMapFinalized += OnDeviceMapFinalized;
      _startMappingButton.onClick.AddListener(OnStartMappingClicked);
  }

  private void OnDeviceMapFinalized(ARDeviceMap map)
  {
      if (map.HasValidMap())
      {
          // final map generated. save to the file system
          var serializedDeviceMap = map.Serialize();
          var path = Path.Combine(Application.persistentDataPath, MapFileName);
          File.WriteAllBytes(path, serializedDeviceMap);
          Debug.Log($"Map saved");
      }
      else
      {
          Debug.LogError("Map was empty");
      }
  }

  // Set this function to be called when button is clicked
  public void OnStartMappingClicked()
  {
      StartCoroutine(RunMapping());
  }

  private IEnumerator RunMapping()
  {
      _startMappingButton.gameObject.SetActive(false);
      _deviceMappingManager.SetDeviceMap(new ARDeviceMap());
      _deviceMappingManager.StartMapping();
      yield return new WaitForSeconds(10.0f);
      _deviceMappingManager.StopMapping();
      _startMappingButton.gameObject.SetActive(true);
  }

}
```

</div>

</div>

</div>

</div>

</div>

</div>
