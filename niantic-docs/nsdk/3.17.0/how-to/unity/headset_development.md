---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/unity/headset_development/
title: Developing for NSDK on XR Headsets
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Developing for NSDK on XR Headsets

</div>

Working with NSDK on XR headsets is, in many ways, the same as developing an AR experience for mobile devices. Due to hardware differences between XR headsets and a standard smartphone, some tasks must be done differently. In this How-To, you will learn about the differences and how to address them in your Unity project.

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

1.  You must complete the [setup](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/#create-a-project-and-install-the-niantic-sdk-packages) process for your supported XR headset before using this How-To.
2.  You will need a valid NSDK API key attached to your Unity project for the VPS section of this How-To. See the [Create Account page](https://www.nianticspatial.com/docs/nsdk/3.17.0/create_account/) for more information.
3.  Scripts in this How-To use elements from the `ARLocationManager` and VPS Coverage APIs. If you need a refresher, see [How to Use Location AR with Code](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/location_ar_code/) and [Querying VPS Coverage for AR Locations at Runtime](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/querying_vps_coverage/).

## Playback<a href="#playback" class="hash-link" aria-label="Direct link to Playback" title="Direct link to Playback">​</a>

By playing through pre-recorded footage in the Unity editor, NSDK's Playback system is able to simulate AR applications on a supported XR headset in the same way as it does on mobile devices.

To use playback in the Unity Editor, you must enable **Niantic Lightship SDK for Unity Editor** as a plugin provider in **XR Plug-in Management** for Windows, Mac, Linux settings.

<img src="https://www.nianticspatial.com/docs/assets/images/xr_settings-eaac6737f97cf1fd47cce470ffc68b42.png" width="500" alt="Enable Niantic Lightship SDK for Unity Editor" />

<div class="tabs-container tabList__CuJ">

- Meta Quest 3

<div class="margin-top--md">

<div class="tabItem_Ymn6 ardkTab" role="tabpanel">

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Warning!

</div>

<div class="admonitionContent_BuS1">

In the Unity Editor, the visualization of object detection results may not be in the correct orientation. This is a visual issue as object detection works as expected on-device.

</div>

</div>

1.  Follow the instructions in [Using the API to Record Datasets](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/playback/create_playback_dataset/#using-the-api-to-record-datasets) to record your playback dataset. **Note:** You must record in **landscape** to use the recording on the Meta Quest 3.
2.  In Unity, open the **Lightship** top menu, then select **Lightship Settings**. In the **Playback** section, enter the path to your recording in the **Dataset Path** field.
3.  Set up your XR scene with any necessary scripts and components, then press Play in the Editor to run the Unity scene using your recording.

</div>

</div>

</div>

## Spoofing Locations<a href="#spoofing-locations" class="hash-link" aria-label="Direct link to Spoofing Locations" title="Direct link to Spoofing Locations">​</a>

Because most XR headsets do not have GPS hardware, you will need to spoof a location to use some of NSDK's location-based features such as the Coverage API -- VPS no longer requires GPS coordinates when localizing.

To spoof a location, you have two options:

- Lightship Settings UI; or
- Scripting via `RuntimeLightshipSettings.ActiveSettings`

The UI is handy for quicker iteration while the scripting functionality is useful for situations where you would like to emulate location changes at runtime.

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

You must still accept Location Service permissions on your headset when spoofing a location, even though GPS is not available on the device.

</div>

</div>

### Spoofing via Lightship Settings<a href="#spoofing-via-lightship-settings" class="hash-link" aria-label="Direct link to Spoofing via Lightship Settings" title="Direct link to Spoofing via Lightship Settings">​</a>

<img src="https://www.nianticspatial.com/docs/assets/images/spoof_ui-3a36a98c2445c8d453b3f5336b8b36c1.png" width="500" alt="Spoofing location and compass data in Lightship Settings" />

To get started spoofing locations and compass data, open the **Lightship** top menu in Unity, select **Lightship Settings**, and scroll down to the **Location & Compass** section. If necessary, change the **Data Source** from `Sensors` to `Spoof`. Changes are immediately picked up by `Niantic.Lightship.AR.Input.location`.

#### Spoof Location Info<a href="#spoof-location-info" class="hash-link" aria-label="Direct link to Spoof Location Info" title="Direct link to Spoof Location Info">​</a>

1.  **Latitude**: The simulated north/south coordinate.
2.  **Longitude**: The simulated east/west coordinate.
3.  **Timestamp**: When the location data was captured, in milliseconds since the Unix epoch.
4.  **Altitude**: Simulated height above sea level, in meters.
5.  **Horizontal Accuracy**: Uncertainty of the latitude/longitude, in meters. Lower = more accurate.
6.  **Vertical Accuracy**: Uncertainty of the altitude, in meters. Lower = more accurate.

#### Spoof Compass Info<a href="#spoof-compass-info" class="hash-link" aria-label="Direct link to Spoof Compass Info" title="Direct link to Spoof Compass Info">​</a>

1.  **Magnetic Heading**: Direction to *magnetic north*, in degrees. `0` (or `360`) is north; `90` is east.
2.  **True Heading**: Direction to *true north*, in degrees. Adjusted for magnetic declination (the difference between magnetic and true north).
3.  **Heading Accuracy**: Uncertainty of the **True Heading**, in degrees. Lower = more accurate.
4.  **Raw Vector**: The raw magnetometer data as a 3D vector (x, y, z), useful for computing orientation or tilt.
5.  **Timestamp**: When the compass data was captured, in milliseconds since the Unix epoch. Typically aligns with the location timestamp.

### Spoofing via Script<a href="#spoofing-via-script" class="hash-link" aria-label="Direct link to Spoofing via Script" title="Direct link to Spoofing via Script">​</a>

All of the aforementioned settings under **Lightship Settings** are configurable within a Unity script.

To ensure your changes take effect, you must specify the data source for `LightshipSettingsHelper.ActiveSettings` by setting `LocationAndCompassDataSource` to `LocationDataSource.Spoof`. Alternatively, you can update this via Lightship settings as mentioned above.

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
// Important or you won't see your spoofed data!
LightshipSettingsHelper.ActiveSettings.LocationAndCompassDataSource = LocationDataSource.Spoof;

var locationInfo = LightshipSettingsHelper.ActiveSettings.SpoofLocationInfo;
locationInfo.Latitude = 10.1f;
locationInfo.Longitude = 20.2f;
locationInfo.Altitude = 30.3f;
locationInfo.HorizontalAccuracy = 40.4f;
locationInfo.VerticalAccuracy = 50.5f;
locationInfo.Timestamp = 12345678;

var compassInfo = LightshipSettingsHelper.ActiveSettings.SpoofCompassInfo;
compassInfo.MagneticHeading = 90f;
compassInfo.TrueHeading = 1.43f;
compassInfo.HeadingAccuracy = 1f;
compassInfo.RawVector = new Vector3(0.1f, 0.2f, 0.3f);
compassInfo.Timestamp = 123456;
```

</div>

</div>

</div>

</div>
