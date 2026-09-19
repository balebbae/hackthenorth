---
source: https://www.nianticspatial.com/docs/nsdk/how-to/vps/location_manager/
title: Location Drift Mitigation
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Location Drift Mitigation

</div>

The `ARLocationManager` class provides experimental features for drift mitigation.

To access these features:

1.  Open the **Player Settings** menu:
    1.  In the **File** top menu, choose **Build Settings**.
    2.  Click the button labeled **Player Settings** in the bottom-left corner of the **Build Settings** window.
2.  Add the experimental feature flag:
    1.  Scroll down to **Script Compilation** in the **Player Settings** menu.
    2.  Under **Scripting Define Symbols**, click the **+ button** to add another line, then add `NIANTICSPATIAL_NSDK_EXPERIMENTAL_FEATURES` to enable them.

## Feature Overview<a href="#feature-overview" class="hash-link" aria-label="Direct link to Feature Overview" title="Direct link to Feature Overview">​</a>

The experimental drift mitigation features are:

- **Temporal Fusion**
  - By default, averages the last five good localization results to provide a more stable localization. Continuous Localization must be enabled for Temporal Fusion to work.
- **TransformUpdateSmoothingEnabled:**
  - Smoothens anchor updates for cleaner transforms. Continuous Localization must be enabled for update smoothing.
- **InitialServiceRequestIntervalSeconds:**
  - Defines the time between network requests when initially attempting tracking. Longer intervals between requests will reduce network bandwidth consumption, but may take longer to gain tracking. By default, this is set to one request per second.
- **ContinuousServiceRequestIntervalSeconds:**
  - Defines the time between network requests when continuously localizing. Continuous Localization must be enabled to use this feature. Longer intervals between requests will reduce network bandwidth consumption, but may take longer to refine tracking. By default, this is set to one request every five seconds.
- **CloudLocalizationTemporalFusionWindowSize:**
  - Defines the number of anchor update entries that are considered in temporal fusion. By default, this is set to five entries, so it will fuse 25 seconds of entries (five entries multiplied by the default five seconds per localization). It is recommended to set this to a value that will fuse 5 to 25 seconds worth of localizations. Larger window sizes will cause refining to happen more slowly, but be more stable. Requires **Continuous Localization** and **Temporal Fusion** enabled.
- **DiagnosticsEnabled:**
  - Enabling diagnostics will enable an additional `frameDiagnosticsArray` entry in the **XRPersistentAnchorSubsystem's** `debugInfoProvided` event. These diagnostics provide guidance for the localizability of the user's camera feed (too dark, blurry, etc). This feature runs a neural network under the hood, so it is rather expensive.

</div>

</div>
