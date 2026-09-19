---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/features/playback/
title: Recording and Playback
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Recording and Playback

</div>

The Playback feature allows you to import pre-recorded AR sessions and re-run them during a new AR runtime session. Using Playback supplies the application with frames to replay the captured video along with other relevant data such as GPS coordinates and device pose. With this feature, developers can create recordings of locations where they expect their users to experience, then develop applications using real-world data entirely from the editor.

## Integration<a href="#integration" class="hash-link" aria-label="Direct link to Integration" title="Direct link to Integration">​</a>

Lightship Playback functionality integrates seamlessly into ARFoundation’s subsystems, allowing developers to use it without writing any new code. All features such as **Depth**, **Scene Segmentation**, and **Object Detection** should work the same as if the session was occurring in real time on a device.

After selecting Lightship as the active loader in XRSettings, you can use Playback-supported Unity subsystems during Play Mode in the Unity Editor. If the dataset includes location data, that is also available via the Unity <a href="https://docs.unity3d.com/ScriptReference/LocationService.html" target="_blank" rel="noopener noreferrer">LocationService API</a>.

## Recording and Using Playback Datasets<a href="#recording-and-using-playback-datasets" class="hash-link" aria-label="Direct link to Recording and Using Playback Datasets" title="Direct link to Recording and Using Playback Datasets">​</a>

ARDK 3.0 supports the creation of datasets from real-world environments for playback in the Unity Editor. For more information, see [How to Create Datasets for Playback](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/playback/create_playback_dataset/).

To get started developing with a playback dataset, see [How to Set Up Playback](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/playback/setting_up_playback/).

## Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<img src="https://www.nianticspatial.com/docs/assets/images/playback_in_action-946b8e58309d8d18e176ff32bc256d17.gif" width="400" alt="Playback in Action" />

</div>

</div>
