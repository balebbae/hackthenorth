---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/playback/create_playback_dataset/
title: How to Create Datasets for Playback
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Create Datasets for Playback

</div>

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/playback_howto_statue1-0d718ab613a83b41ede95c510ed7e13b.gif" width="300" alt="Playback Recording Of Statue Angle 1" /><img src="https://www.nianticspatial.com/docs/assets/images/playback_howto_statue2-323e9ee1385c3945b179c0ec29d26359.gif" width="300" alt="Playback Recording Of Statue Angle 2" />

</div>

With Lightship's Recording feature, you can record the real-world location of your AR application for playback and testing in the Unity editor. You can create a playback dataset by using the Recording sample project or by recording through the API.

## Recording data<a href="#recording-data" class="hash-link" aria-label="Direct link to Recording data" title="Direct link to Recording data">​</a>

### Recording formats<a href="#recording-formats" class="hash-link" aria-label="Direct link to Recording formats" title="Direct link to Recording formats">​</a>

ARDK can produce two versions of a scan recording:

1.  **Raw Scan format:** By default, AR Scanning Manager will write frames directly to disk.

- This is the format that Scan Reconstruction accepts.
- The files are saved to the directory at `ScanStore.SavedScan.ScanPath`. Metadata is stored in .pb files.

2.  **Playback format:** Optionally, the recorded frames can be exported to a compressed .tgz archive.

- This is the format that [Playback](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/playback/) and [VPS](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/lightship_vps/) accept.
- The sequence is archived to `ScanStore.SavedScan.ScanPath` in a .tgz. Metadata is stored in a capture.json file.

This walkthrough demonstrates how to produce the second format for use with Playback.

### File locations<a href="#file-locations" class="hash-link" aria-label="Direct link to File locations" title="Direct link to File locations">​</a>

By default, scan recordings will be saved to these paths. Setting AR Scanning Manager's **Scan Path** field to a custom location will override this. In Unity apps, the saved location is available in the [`ScanStore.SavedScan.ScanPath` property](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/ARDK/AR/Scanning/ScanStore/SavedScan/).

| Platform | Unity SDK | Native SDK |
|----|----|----|
| iOS | {App Files}/scankit/ | {App Files}/scankit/ |
| Android | /sdcard/Android/data/{app.package.name}/files/scankit/ | /sdcard/Android/data/{app.package.name}/files/scankit/ |
| macOS | /Users/{Username}/Library/Application Support/{CompanyName}/{ApplicationName}/scankit/ | {Application path}/data/scankit/ |
| Windows | C:\Users\\Username}\AppData\LocalLow\\CompanyName}\\ApplicationName}\scankit\\ | C:\Users\\Username}\AppData\Local\ardk_data\scankit\\ |

To retrieve the files from an iOS app in Finder, add <a href="https://developer.apple.com/documentation/bundleresources/information-property-list/uifilesharingenabled" target="_blank" rel="noopener noreferrer">UIFileSharingEnabled</a> and <a href="https://developer.apple.com/documentation/bundleresources/information-property-list/lssupportsopeningdocumentsinplace" target="_blank" rel="noopener noreferrer">LSSupportsOpeningDocumentsInPlace</a> to the app's info.plist. To retrieve the files from an Android app, use <a href="https://developer.android.com/tools/adb" target="_blank" rel="noopener noreferrer"><code>adb pull</code></a> with the appropriate path.

## Using the Scanning Sample to Record<a href="#using-the-scanning-sample-to-record" class="hash-link" aria-label="Direct link to Using the Scanning Sample to Record" title="Direct link to Using the Scanning Sample to Record">​</a>

### Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

To scan using the Recording sample project, you will need to download it and build it to your device. For more information, see [the Recording sample project](https://www.nianticspatial.com/docs/nsdk/3.17.0/sample_projects/#recording).

### Steps<a href="#steps" class="hash-link" aria-label="Direct link to Steps" title="Direct link to Steps">​</a>

To record a playback dataset using the sample:

1.  Open the recording sample on your device. When you are ready to record the dataset, tap **Start**.
2.  Record the environment using your device's camera. Keep in mind the following:

- Keep your device in **Portrait Mode**.
- Hold your device as steadily as possible to reduce errors in the dataset.
- The sample saves dataset recordings **every minute**. If you continue recording after one minute, the app will start a new recording. (For example, if you record for 3.5 minutes, the sample creates four separate datasets.)

3.  Tap **Stop** to finish recording. At this point, you have a recording in Raw Scan format.
4.  When you are ready, tap **Export** to convert your most recent Raw Scan recording to a Playback format dataset.
5.  After the export is complete, the sample will display a path to the archived dataset. Remember this path and proceed to [Accessing Your Recorded Data on the Device](#accessing-recorded-data-on-the-device).

<img src="https://www.nianticspatial.com/docs/assets/images/record_sample-8c63939a71855f3fd1badd196183fe19.gif" width="200" alt="Using the recording sample to create a dataset" />

## Using the API to Record Datasets<a href="#using-the-api-to-record-datasets" class="hash-link" aria-label="Direct link to Using the API to Record Datasets" title="Direct link to Using the API to Record Datasets">​</a>

If the Recording sample is too limited for your project, you can create your own recording app instead.

### Prerequisites<a href="#prerequisites-1" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Unity project with NSDK installed and a set-up basic AR scene. For more information, see [Setting Up the Niantic SDK for Unity](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/) and [Setting up a Basic AR Scene](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/#setting-up-a-basic-ar-scene).

### Steps<a href="#steps-1" class="hash-link" aria-label="Direct link to Steps" title="Direct link to Steps">​</a>

1.  Enable Scanning in **Lightship Settings**:
    1.  In the **Lightship** top menu, select **Settings**.
    2.  In the **Inspector** window, check the box labeled **Scanning**.

<img src="https://www.nianticspatial.com/docs/assets/images/lightship_settings_scanning-de869c31add0c06f47f9345435ca034a.png" width="500" alt="Enable scanning in settings" />

1.  In your **AR Scene**, add an **AR Scanning Manager** to the scene, then disable it:
    1.  Select the **ARSession** `GameObject`.
    2.  In the **Inspector** window, click **Add Component**, then add an **AR Scanning Manager** to it.
    3.  Un-check the box next to `AR Scanning Manager (Script)` to disable it.

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>caution

</div>

<div class="admonitionContent_BuS1">

Enabling **Record Estimated Depth** to record NSDK depth buffers on non-lidar devices will limit the AR Scanning Manager's recording FPS to the update rate of the depth feature, regardless of AR Scanning Manager's **Recording Framerate** selection.

To change the update rate of the depth feature from its default rate of **10 FPS**, add a `Lightship Occlusion Extension` component on the same Game Object as an `AR Occlusion Manager` and set the **Target Frame Rate**.

</div>

</div>

<img src="https://www.nianticspatial.com/docs/assets/images/ar_scanning_manager-6414ac7ff66ad29078ee36d6a8c56b0d.png" width="500" alt="AR Scanning manager" />

1.  Create two buttons in your scene; one to start the recording, the other to stop it.
    1.  Right-click in the **Hierarchy**, then, in the **UI** menu, select **Button**. Rename the Button "Record".
    2.  Repeat the previous step, naming the new button "Stop".
    3.  For each button, expand its `GameObject` and select the `Text` sub-object, then change the `Text` field to "Record" or "Stop", as appropriate.
    4.  Move the buttons in the scene view to where you would like them.
2.  Create scripts to drive the recording, then connect them to the buttons:
    1.  In the **Project** window, right-click in the **Assets** folder, then select **C# Script** from the **Create** menu. Name the new script `StartScript`. Create another script and name it `RecorderInput`. Populate the scripts with the following code:

Click to reveal StartScript.cs

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
  using System.Collections;
  using System.Collections.Generic;
  using UnityEngine;

  public class StartScript : MonoBehaviour
  {
      public void Start() {
          // get permission to use location data if on Android
          // then enable location and compass services
  #if UNITY_ANDROID
          if (!Permission.HasUserAuthorizedPermission(Permission.FineLocation))
          {
              var androidPermissionCallbacks = new PermissionCallbacks();
              androidPermissionCallbacks.PermissionGranted += permissionName =>
              {
                  if (permissionName == "android.permission.ACCESS_FINE_LOCATION")
                  {
                      Start();
                  }
              };

              Permission.RequestUserPermission(Permission.FineLocation, androidPermissionCallbacks);
              return;
          }
  #endif
          Input.compass.enabled = true;
          Input.location.Start();
      }
  }
```

</div>

</div>

</div>

</div>

Click to reveal RecorderInput.cs

<div>

<div class="collapsibleContent_i85q">

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
using System.Collections;
using System.Collections.Generic;
using Niantic.ARDK.AR.Scanning;
using Niantic.Lightship.AR.Scanning;
using UnityEngine;

public class RecorderInput : MonoBehaviour
{
    [SerializeField] private ARScanningManager _arScanningManager;

    public async void StopRecordingAndExport() {

        // save the recording with SaveScan()
        // use ScanStore() to get a reference to it, then ScanArchiveBuilder() to export it
        // output the path to the playback recording as a debug message
        string scanId = _arScanningManager.GetCurrentScanId();
        await _arScanningManager.SaveScan();
        var savedScan = _arScanningManager.GetScanStore().GetSavedScans().Find(scan => scan.ScanId == scanId);
        ScanArchiveBuilder builder = new ScanArchiveBuilder(savedScan, new UploadUserInfo());
        while (builder.HasMoreChunks())
        {
            var task = builder.CreateTaskToGetNextChunk();
            task.Start();
            await task;
            Debug.Log(task.Result);   // <- this is the path to the playback recording.
        }
        _arScanningManager.enabled = false;
    }
    
    public void StartRecording() {
        _arScanningManager.enabled = true;
    }

}
```

</div>

</div>

</div>

</div>

1.  In the **Hierarchy**, right-click, then select **Create Empty**. Name the new `GameObject` "RecordScripts". With `RecordScripts` selected, in the **Inspector** window, click **Add Component** and add `StartScript`. Also add `RecorderInput`, making sure to pass the AR Scanning Manager from the Hierarchy.

<img src="https://www.nianticspatial.com/docs/assets/images/record_scripts_gameobject-75464a16b04ae30e806fb9359bd6ae59.png" width="500" alt="RecordScripts gameobject" />

1.  Select the `Record` button in the **Hierarchy**, then add a script to the `OnClick` field in the **Inspector** by dragging the `RecordScripts` `GameObject` into the field and selecting `RecorderInput.StartRecording`. Do the same for the `Stop` button, selecting `RecorderInput.StopRecordingAndExport` at the end.

<img src="https://www.nianticspatial.com/docs/assets/images/record_script-8b3c4d6f8d4f772889ca003c416ba99e.png" width="400" alt="Record Script" /><img src="https://www.nianticspatial.com/docs/assets/images/stop_recording_script-6425b628c7117dde8a1d41a8d63912ca.png" width="400" alt="Stop Recording Script" />

1.  Build to your device and test it out!

## Accessing Recorded Data on the Device<a href="#accessing-recorded-data-on-the-device" class="hash-link" aria-label="Direct link to Accessing Recorded Data on the Device" title="Direct link to Accessing Recorded Data on the Device">​</a>

Follow the instructions for your device's operating system:

### Exporting from iOS<a href="#exporting-from-ios" class="hash-link" aria-label="Direct link to Exporting from iOS" title="Direct link to Exporting from iOS">​</a>

1.  Enable developer mode on your device:
    1.  Open the **Settings** app, then open the **Privacy and Security** menu and enable **Developer Mode**.
2.  Connect your device to Xcode.
3.  Open the **Window** top menu, then select **Device and Simulators** and find the sample app.
4.  With the app highlighted, click the three dot menu and click **Download Container**.

<img src="https://www.nianticspatial.com/docs/assets/images/xcode_container_menu-d9a35568fa02dfb5eae8e90645640c40.png" width="300" alt="XCode container menu" />

1.  Once the container downloads to your machine, right-click on the package, then click **Show Package Contents**.
2.  Navigate to the path from the recording output (for example: `AppData/Documents/scankit/(ID of your scan)/chunk_0.tgz`).
3.  Copy the archive to your machine, then unzip it.

### Exporting from Android<a href="#exporting-from-android" class="hash-link" aria-label="Direct link to Exporting from Android" title="Direct link to Exporting from Android">​</a>

1.  Connect your device to your development machine.
2.  Get the files from your device:
    1.  MacOS: Open **Android File Transfer**, then navigate to the path from the recording output. You may also choose to use Android Studio's Device Explorer, or another tool of your preference.
    2.  Windows: When the dialog pops up asking what you want to do, select **File Transfer**, then navigate to the path from the recording.
3.  Copy the archive to your machine, then unzip it.

## Using the Playback Data in Unity<a href="#using-the-playback-data-in-unity" class="hash-link" aria-label="Direct link to Using the Playback Data in Unity" title="Direct link to Using the Playback Data in Unity">​</a>

To add a playback dataset to Unity:

1.  Open **Project Settings** from the **Edit** menu, then scroll down to **XR Plugin Management** and select **Niantic Lightship SDK**.
2.  Enable **Editor Playback**, then input the absolute path to your dataset in the **Dataset Path** field.
3.  If using on-device playback, make sure the dataset is copied into the `Assets/StreamingAssets` directory of your Unity project before building.

</div>

</div>
