---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/playback/setting_up_playback/
title: How to Set Up Playback
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Set Up Playback

</div>

## Description<a href="#description" class="hash-link" aria-label="Direct link to Description" title="Direct link to Description">​</a>

This How-To details how to set up our Playback system so that you can iterate in the Unity editor rather than building to device. Playback will run our algorithms in the editor using a pre-recorded ARSession dataset. This can be used to play through your project on desktop as if you were running it optimally on a mobile device.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/playback_howto_editor-3cbcd1c6964e71bc7973ab8c03608af2.gif" width="1000" alt="Playback Recording Running In Editor" />

</div>

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Unity project with Lightship AR enabled and an AR scene configured. For more information, see [Installing ARDK 3](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/).

## Steps<a href="#steps" class="hash-link" aria-label="Direct link to Steps" title="Direct link to Steps">​</a>

### 1. Download or create a recording to use for Playback<a href="#1--download-or-create-a-recording-to-use-for-playback" class="hash-link" aria-label="Direct link to 1.  Download or create a recording to use for Playback" title="Direct link to 1.  Download or create a recording to use for Playback">​</a>

- Sample recordings are available for download <a href="https://storage.googleapis.com/nianticweb-epos-web-staging/gandhi_statue.tgz" target="_blank" rel="noopener noreferrer">here</a> and/or <a href="https://storage.googleapis.com/nianticweb-epos-web-staging/gandhi_statue_peer_2.tgz" target="_blank" rel="noopener noreferrer">here</a>
- To make your own Playback dataset, see [How to Create Datasets for Playback](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/playback/create_playback_dataset/).
  - ARDK produces two formats of scan recordings, [Raw Scan format and Playback format](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/playback/create_playback_dataset/#recording-formats).
  - Ensure that your scan recording is exported to **Playback format** (extracted from a .tgz archive, and metadata is contained in capture.json). The Playback feature will not accept Raw Scan recordings (where metadata is contained in \*.pb files).

### 2. Verify that Lightship SDK is selected on the PC platform<a href="#2-verify-that-lightship-sdk-is-selected-on-the-pc-platform" class="hash-link" aria-label="Direct link to 2. Verify that Lightship SDK is selected on the PC platform" title="Direct link to 2. Verify that Lightship SDK is selected on the PC platform">​</a>

- In Unity, open the **Edit** top menu, then select **Project Settings**.
- Select XR Plug-in Management from the left-hand menu
- In the XR Plugin Management window, select the Desktop tab
- Enable the `Niantic Lightship SDK for Unity Editor` checkbox

<img src="https://www.nianticspatial.com/docs/assets/images/playback_howto_plugin_management-a47ef329eecca15d6a3a2ef4edd3d49b.png" width="900" alt="XR Plug In Management" />

### 3. Enable Playback<a href="#3-enable-playback" class="hash-link" aria-label="Direct link to 3. Enable Playback" title="Direct link to 3. Enable Playback">​</a>

- Open the **Lightship** top menu, then select Settings to open the Lightship SDK Settings menu.
- Under the **Playback** header, with the **Editor** tab selected, check the **Enabled** box.
- Click the button to the right of the Dataset Path field to browse to the location of your Playback dataset. This can be located anywhere in your file system when using Playback in the Unity Editor. However, if you want to run Playback in a build, the files must be located inside your project’s StreamingAssets folder.

<img src="https://www.nianticspatial.com/docs/assets/images/playback_howto_settings-a74c8a5d67ec5a4fa892e9806a786f14.png" width="900" alt="Lightship SDK Settings" />

### 4. Playback is now configured<a href="#4-playback-is-now-configured" class="hash-link" aria-label="Direct link to 4. Playback is now configured" title="Direct link to 4. Playback is now configured">​</a>

Press play and the footage you selected should start playing in editor. This can be seen from the `Game` or `Simulator` window in Unity. If it is not working, double check the steps above and make sure to have added the `ARSession` and `XROrigin` from the XR menu to your scene.

### 5. Play through frames manually<a href="#5-play-through-frames-manually" class="hash-link" aria-label="Direct link to 5. Play through frames manually" title="Direct link to 5. Play through frames manually">​</a>

If you find your recording moves through the environment too quickly (maybe you want to keep a point of interest on screen for longer), you can click the “Run Manually” checkbox to enable controls the next time you start Playback. Note that this does not stop Unity from running and updating `MonoBehaviours`.

Run Manually mode controls:

- **Spacebar**: step forward one frame
- **Tap left arrow key:** rewind one frame
- **Hold left arrow key:** scroll backward
- **Tap right arrow key:** advance one frame
- **Hold right arrow key:** scroll forward

## Collecting your datasets for testing<a href="#collecting-your-datasets-for-testing" class="hash-link" aria-label="Direct link to Collecting your datasets for testing" title="Direct link to Collecting your datasets for testing">​</a>

Different recordings can be used to test different scenarios for your project, so we recommend having a variety of recordings at your disposal. See [How to Create Datasets for Playback](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/playback/create_playback_dataset/) for more information. Consider recording the following:

- Outdoors
- Indoors
- Large open space
- [Activated VPS Wayspot](https://www.nianticspatial.com/docs/nsdk/3.17.0/features/lightship_vps/)
- Different sequences of the same location to help debug multiplayer

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/playback_howto_statue1-0d718ab613a83b41ede95c510ed7e13b.gif" width="300" alt="Playback Recording Of Statue Angle 1" /><img src="https://www.nianticspatial.com/docs/assets/images/playback_howto_statue2-323e9ee1385c3945b179c0ec29d26359.gif" width="300" alt="Playback Recording Of Statue Angle 2" />

</div>

## Using Location Services with Playback<a href="#using-location-services-with-playback" class="hash-link" aria-label="Direct link to Using Location Services with Playback" title="Direct link to Using Location Services with Playback">​</a>

Wherever you would use the `UnityEngine.Input` API normally, instead use Lightship’s implementation by adding `using Input = Niantic.Lightship.AR.Input;` to the top of your C# file. Lightship’s implementation has the exact same API as Unity’s; and when not running in Playback mode, it is a simple passthrough to Unity’s APIs. When in Playback mode, it’ll supply the location data from the active dataset.

</div>

</div>
