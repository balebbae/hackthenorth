---
source: https://www.nianticspatial.com/docs/nsdk/how-to/playback/setting_up_playback/
title: How to set up playback
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to set up playback

</div>

## Description<a href="#description" class="hash-link" aria-label="Direct link to Description" title="Direct link to Description">​</a>

This guide explains how to set up Playback so you can iterate in the Unity Editor instead of building to a device. Playback runs NSDK algorithms in the editor using a prerecorded `ARSession` dataset so you can play through your project on desktop as if it were running on a mobile device.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/playback_howto_editor-3cbcd1c6964e71bc7973ab8c03608af2.gif" width="1000" alt="Playback recording running in Unity Editor" />

</div>

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

You will need a Unity project with NSDK AR enabled and an AR scene configured. For more information, see [Set up the Niantic SDK for Unity](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-the-niantic-sdk-for-unity).

## Steps<a href="#steps" class="hash-link" aria-label="Direct link to Steps" title="Direct link to Steps">​</a>

To set up Playback in the Unity Editor, complete the following steps:

1.  [Download or create a Playback dataset](#download-or-create-a-recording-to-use-for-playback) — Obtain a dataset to simulate AR sessions in the editor.
2.  [Verify that Niantic SDK is selected on the PC platform](#verify-that-niantic-sdk-is-selected-on-the-pc-platform) — Enable the correct XR plugin for editor playback.
3.  [Enable Playback](#enable-playback) — Configure the dataset and playback settings in NSDK.
4.  [Run Playback in the editor](#playback-is-now-configured) — Start playback and verify it works in the Game or Simulator view.
5.  [Control playback manually](#control-playback-manually) — Step through frames to inspect behavior.

### Download or create a Playback dataset<a href="#download-or-create-a-playback-dataset" class="hash-link" aria-label="Direct link to Download or create a Playback dataset" title="Direct link to Download or create a Playback dataset">​</a>

You can either download a sample Playback dataset or record your own using the [NSDK recording pipeline](https://www.nianticspatial.com/docs/nsdk/how-to/playback/create_playback_dataset/). Playback datasets must be created this way because they bundle AR session tracking data together with images. Externally captured videos don’t contain this tracking information and can’t be converted into supported Playback datasets.

- Download a sample Playback recording of the Gandhi statue shown at the top of the page, where a single user walks around the statue from one side: <a href="https://storage.googleapis.com/nianticweb-epos-web-staging/gandhi_statue.tgz" target="_blank" rel="noopener noreferrer">gandhi_statue.tgz</a>. You can also download a second recording of the same statue captured from a different trajectory: <a href="https://storage.googleapis.com/nianticweb-epos-web-staging/gandhi_statue_peer_2.tgz" target="_blank" rel="noopener noreferrer">gandhi_statue_peer_2.tgz</a>. Use the second recording to simulate a second user or test alignment consistency across sessions.

- To make your own Playback dataset, see [How to Create Datasets for Playback](https://www.nianticspatial.com/docs/nsdk/how-to/playback/create_playback_dataset/).

  - NSDK produces two formats of scan recordings, [Raw Scan format and Playback format](https://www.nianticspatial.com/docs/nsdk/how-to/playback/create_playback_dataset/#recording-formats).
  - Ensure that your scan recording is exported to **Playback format** (extracted from a .tgz archive, and metadata is contained in capture.json). Playback feature does not accept Raw Scan recordings, where metadata is contained in `*.pb` files.

### Verify that Niantic SDK is selected on the PC platform<a href="#verify-that-niantic-sdk-is-selected-on-the-pc-platform" class="hash-link" aria-label="Direct link to Verify that Niantic SDK is selected on the PC platform" title="Direct link to Verify that Niantic SDK is selected on the PC platform">​</a>

- In Unity, open the **Edit** top menu, then select **Project Settings**.
- Select XR Plug-in Management from the left-hand menu.
- In the XR Plug-in Management window, select the **Desktop** tab.
- Enable the `Niantic Spatial Development Kit for Unity Editor` checkbox.

<img src="https://www.nianticspatial.com/docs/assets/images/playback_howto_plugin_management-a47ef329eecca15d6a3a2ef4edd3d49b.png" width="900" alt="XR Plug In Management" />

### Enable Playback<a href="#enable-playback" class="hash-link" aria-label="Direct link to Enable Playback" title="Direct link to Enable Playback">​</a>

- Open the **NSDK** top menu, then select Settings to open the Niantic SDK Settings menu.
- Under the **Playback** header, with the **Editor** tab selected, check the **Enabled** box.
- Click the button to the right of the Dataset Path field to browse to the location of your Playback dataset. This can be located anywhere in your file system when using Playback in the Unity Editor. However, if you want to run Playback in a build, the files must be located inside your project’s StreamingAssets folder.
- You can optionally choose to play just a subset of the entire Playback by dragging the ends of the timeline scrubber. This will use only the selected portion of the overall Playback, with the chosen start and end frames highlighted.

<img src="https://www.nianticspatial.com/docs/assets/images/playback_howto_settings-a74c8a5d67ec5a4fa892e9806a786f14.png" width="900" alt="Niantic SDK Settings" />

### Run Playback in the editor<a href="#run-playback-in-the-editor" class="hash-link" aria-label="Direct link to Run Playback in the editor" title="Direct link to Run Playback in the editor">​</a>

Press **Play**, and the footage you selected should start playing in the editor. This can be seen from the `Game` or `Simulator` window in Unity. If it is not working, double-check the steps above and make sure to have added the `ARSession` and `XROrigin` from the XR menu to your scene.

### Control Playback manually<a href="#control-playback-manually" class="hash-link" aria-label="Direct link to Control Playback manually" title="Direct link to Control Playback manually">​</a>

If your recording moves through the environment too quickly (maybe you want to keep a point of interest on screen for longer), select the checkbox next to **Run Manually** to enable controls the next time you start Playback. Note that this does not stop Unity from running and updating `MonoBehaviours`.

Run Manually mode controls:

- **Spacebar**: step forward one frame
- **Tap left arrow key:** rewind one frame
- **Hold left arrow key:** scroll backward
- **Tap right arrow key:** advance one frame
- **Hold right arrow key:** scroll forward

## Collect datasets for testing<a href="#collect-datasets-for-testing" class="hash-link" aria-label="Direct link to Collect datasets for testing" title="Direct link to Collect datasets for testing">​</a>

Different recordings can be used to test different scenarios for your project, so you should maintain a variety of recordings at your disposal. See [How to Create Datasets for Playback](https://www.nianticspatial.com/docs/nsdk/how-to/playback/create_playback_dataset/) for more information.

Consider recording the following:

- Outdoors
- Indoors
- Large open space
- [Activated VPS Wayspot](https://www.nianticspatial.com/docs/nsdk/features/lightship_vps/)
- Different sequences of the same location to help debug multiplayer

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/playback_howto_statue1-0d718ab613a83b41ede95c510ed7e13b.gif" width="300" alt="Playback Recording Of Statue Angle 1" /><img src="https://www.nianticspatial.com/docs/assets/images/playback_howto_statue2-323e9ee1385c3945b179c0ec29d26359.gif" width="300" alt="Playback Recording Of Statue Angle 2" />

</div>

## Using location services with Playback<a href="#using-location-services-with-playback" class="hash-link" aria-label="Direct link to Using location services with Playback" title="Direct link to Using location services with Playback">​</a>

Wherever you would use the `UnityEngine.Input` API normally, instead use NSDK's implementation by adding `using Input = NianticSpatial.NSDK.AR.Input;` to the top of your C# file. NSDK’s implementation uses the same API as Unity’s. When not running in Playback mode, it passes through to Unity’s APIs. When in Playback mode, it’ll supply the location data from the active dataset.

</div>

</div>
