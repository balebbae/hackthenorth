---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/release_notes/
title: Release Notes v3.17
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Release Notes v3.17

</div>

## Highlights<a href="#highlights" class="hash-link" aria-label="Direct link to Highlights" title="Direct link to Highlights">​</a>

- Beta version of Kotlin and Swift SDKs
- Revamp of the documentation website

## Features/Fixes<a href="#featuresfixes" class="hash-link" aria-label="Direct link to Features/Fixes" title="Direct link to Features/Fixes">​</a>

- Swift SDK
- Kotlin SDK
- Scanning
  - The FPS for recording high-resolution frames is now customizable
  - Bug fixes for recording high-resolution frames under certain scenarios
  - v2 sequences with video now use higher-quality encoding
- URP is now the default for the Unity Samples

## Breaking Changes<a href="#breaking-changes" class="hash-link" aria-label="Direct link to Breaking Changes" title="Direct link to Breaking Changes">​</a>

- None

## Notes<a href="#notes" class="hash-link" aria-label="Direct link to Notes" title="Direct link to Notes">​</a>

- We have removed support for Magic Leap 2
- Documentation for previously released versions is now archived and available from our Github repository.

## Known Issues<a href="#known-issues" class="hash-link" aria-label="Direct link to Known Issues" title="Direct link to Known Issues">​</a>

- \[LocationMeshManager\] Requesting a size limit when downloading a VPS mesh currently has no effect.
- \[LocationMeshManager\] Mesh decoding on iOS devices may fail with an error “Failed to download all meshes”. This issue can be resolved by removing and reimporting the Draco for Unity 5.1.4 package in the Unity Package Manager, then rebuilding your application.
- In SharedAR with VPS example, if the device loses tracking (e.g. camera covered or moving too fast) right before attempting to join second time or after, the device will not localize with VPS. This issue can be avoided by restarting the ARLocationManager’s subsystem before StartSharedSpace() is called by calling ARLocationManager.RestartSubsystemAsyncCoroutine() in a coroutine.
- In the VPS Localization example, if the device loses tracking after successfully localizing, the device will not localize with VPS in an attempt to recover. A workaround for this issue is to enable continuous localization from ARLocationManager
- On some older Android phones, the frame-rate will drop for several seconds at the beginning of a VPS session when VPS diagnostics are enabled. This happens while the machine learning models used by VPS diagnostics are being loaded. Once the ML models finish loading, the frame rate recovers (usually about 5-10 seconds). This slow-down does not show up on newer phones (most phones released since 2020 should be OK). The slowdown can be prevented by disabling VPS Diagnostics on the ARLocationManager (this will prevent diagnostics feedback events).
- Updating to 3.17.0 from an older version of ARDK when updating multiple packages (like ARDK and Shared) may cause corruption in the Library folder, leading to the error “Instance of Niantic.Lightship.AR.Loader.LightshipSettings couldn't be created because there is no script with that name.” Closing Unity, deleting the Library folder, and reopening the project resolves the issue. This is an issue with Unity, and they are investigating a fix for it.
- When activating Lightship SDK for Android or iOS in Unity 2022.3.10f1 and above, you may see the following error message in the Unity console: XR Plug-in Management error. Failure reason: Unable to assign com.nianticlabs.lightship for build target \[Android/iOS\]. This error message is benign and the SDK still works as expected for those platforms. After restarting the editor in this state, you may also see warnings in the Project Validation and Lightship Settings windows that can safely be ignored.
- Importing the ARDK UPM in a project started from Universal 3D template might cause a few build errors reported in the console. Restarting the editor should fix this.
- In the On Device Persistent sample, if the user cancels mapping and restarts mapping quickly, the user will see an error message mapping failed unexpectedly. The user can safely start mapping scans again and make sure to scan properly until it stops by itself.
- \[Quest 3 SDK\] Is currently in beta. There are known infrequent instances of instability. Please restart the app when those occur.

</div>

</div>
