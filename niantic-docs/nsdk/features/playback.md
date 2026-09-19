---
source: https://www.nianticspatial.com/docs/nsdk/features/playback/
title: Recording and Playback
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Recording and Playback

</div>

The Playback feature allows you to import pre-recorded AR sessions and re-run them during a new AR runtime session. Using Playback supplies the application with frames from an AR session recording along with other relevant data such as GPS coordinates and device pose. Developers can use this feature to create recordings of locations where they expect their users to interact with their app, then develop and test using real-world data entirely from the editor.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>Playback datasets are not standard video files

</div>

<div class="admonitionContent_BuS1">

Playback requires an AR session recording that contains tracking data, device poses, timestamps, and location information. Standard videos captured from external cameras don’t include this metadata, so they can’t be used as Playback datasets.

</div>

</div>

To test NSDK features against a real-world location, first record a dataset on a supported device using NSDK Recording methods, then use Playback to iterate on your application.

## Integration<a href="#integration" class="hash-link" aria-label="Direct link to Integration" title="Direct link to Integration">​</a>

NSDK Playback functionality integrates seamlessly into ARFoundation’s subsystems, allowing developers to use it without writing any new code. All features such as **Depth**, and **Scene Segmentation** should work the same as if the session was occurring in real time on a device.

After selecting NSDK as the active loader in **XR Plug-in Management**, you can use Playback-supported Unity subsystems during Play Mode in the Unity Editor. If your dataset includes location data, it's exposed through Unity's <a href="https://docs.unity3d.com/ScriptReference/LocationService.html" target="_blank" rel="noopener noreferrer">LocationService API</a>.

## Recording and Using Playback Datasets<a href="#recording-and-using-playback-datasets" class="hash-link" aria-label="Direct link to Recording and Using Playback Datasets" title="Direct link to Recording and Using Playback Datasets">​</a>

NSDK 4.0 supports the creation of datasets from real-world environments for playback in the Unity Editor. For more information, see [How to Create Datasets for Playback](https://www.nianticspatial.com/docs/nsdk/how-to/playback/create_playback_dataset/).

To get started developing with a playback dataset, see [How to Set Up Playback](https://www.nianticspatial.com/docs/nsdk/how-to/playback/setting_up_playback/).

## Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<img src="https://www.nianticspatial.com/docs/assets/images/playback_in_action-946b8e58309d8d18e176ff32bc256d17.gif" width="400" alt="Playback in Action" />

</div>

</div>
