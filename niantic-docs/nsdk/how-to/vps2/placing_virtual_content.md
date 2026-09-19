---
source: https://www.nianticspatial.com/docs/nsdk/how-to/vps2/placing_virtual_content/
title: Place virtual content with VPS2
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Place virtual content with VPS2

</div>

This guide explains how to place virtual content in an AR scene using an [anchor](https://www.nianticspatial.com/docs/nsdk/core_concepts/#anchor-and-place-content).

Virtual content is any digital object rendered in AR, such as a 3D model, label, or visual effect. To appear in the correct location and remain stable as the user moves, it must be attached to an anchor.

An anchor defines a tracked position and orientation in the real world. Attaching virtual content to an anchor allows the AR system to keep that content aligned with the environment over time.

With VPS2, anchors can be positioned relative to real-world locations, allowing you to place content consistently across sessions and devices.

In this guide, you will:

- Track an anchor in the AR scene
- Attach virtual content to the anchor
- Verify that the content remains stable as the AR session updates

Different placement approaches define how content is created, what data is saved, and how that content is restored later. The next section helps you choose the approach that best fits your application.

------------------------------------------------------------------------

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

Before you start, make sure you already have:

- a project with NSDK installed and a basic AR scene set up
- a Site in Scaniverse for workflows that use a Site anchor or Site-derived content

For setup details, see [Set up the Niantic SDK for Unity](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-the-niantic-sdk-for-unity), [Set up a basic AR scene](https://www.nianticspatial.com/docs/nsdk/setup/#set-up-a-basic-ar-scene), and [First Localization with NSDK](https://www.nianticspatial.com/docs/nsdk/first_localization/).

------------------------------------------------------------------------

## Choose how to place virtual content<a href="#choose-how-to-place-virtual-content" class="hash-link" aria-label="Direct link to Choose how to place virtual content" title="Direct link to Choose how to place virtual content">​</a>

There are multiple ways to place virtual content in an AR scene. Each approach defines how **content is positioned**, how it **behaves over time**, and **what data is stored** so it can be reused.

You can use one or more approaches in the same app, depending on your use case. For example, one feature might place persistent content at a real-world location, while another allows users to place temporary content during a session.

**Key considerations**

- **Using multiple approaches** - Different features in your app can use different placement approaches. You do not need to choose only one for the entire application.
- **Persistence** - Each approach defines what data, if any, is stored for reuse, and whether that reuse is limited to the current session or can work across sessions and devices:
  - **VPS-based placement** stores data relative to a real-world location, which can allow content to appear in the same place across sessions and devices.
  - **Local placement** can keep content stable during the current session, including user-driven placement such as hit tests, but it does not necessarily restore to the same real-world position later unless your app persists additional data.

Use the following table to compare the available approaches based on when to use them, what data they save, and how each one restores content later.

| Approach | Best for | Saved data | Restoration |
|----|----|----|----|
| [Place content relative to an anchor](#place-content-relative-to-an-anchor) | You localize to a Site from its Site anchor payload, then want content to stay attached to that tracked anchor across sessions. | The Site anchor payload plus each content item's anchor-local transform. | Re-localizes to the same Site anchor and reapplies the saved anchor-local transform. |
| [Place content using geo coordinates](#place-content-using-geo-coordinates) | Content is authored at a known latitude, longitude, and altitude. | Geolocation data such as latitude, longitude, altitude, and optional heading. | Reconstructs placement from geospatial coordinates and reapplies the resulting pose. |

**Best practices**

- Use **Place content relative to an anchor** for content that should stay attached to a tracked Site anchor and be restored from anchor-local pose data.
- Use **Place content using geo coordinates** for content authored at a known latitude, longitude, and altitude.

------------------------------------------------------------------------

### Place content relative to an anchor<a href="#place-content-relative-to-an-anchor" class="hash-link" aria-label="Direct link to Place content relative to an anchor" title="Direct link to Place content relative to an anchor">​</a>

Use this approach when the user decides where content should appear during a localized session. Save the content's local transform relative to the anchor, then apply that same local transform again the next time the anchor is tracked.

The primary VPS2 flow in NSDK 4.x is to track a Site anchor from its payload with [ARVps2Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager/), keep the returned [ARVps2Anchor](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Anchor/), and place content relative to that anchor.

Follow this workflow to place, save, and later restore content relative to a tracked Site anchor:

1.  [Create a Site](https://www.nianticspatial.com/docs/nsdk/first_localization/#create-a-private-site) in <a href="https://scaniverse.nianticspatial.com/signin" target="_blank" rel="noopener noreferrer">Scaniverse</a>, then get its Site anchor payload. The payload identifies the Site anchor you will track again in later sessions. You can get the anchor payload in either of these ways:

    - Copy the Site's default anchor payload from Scaniverse when you are testing with a known Site.
    - Alternatively, use the Sites API at runtime and let the user choose a Site.

2.  Track the Site anchor with [TryTrackAnchor](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager.TryTrackAnchor/). Keep the returned [ARVps2Anchor](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Anchor/), because your content will be attached relative to it. This code is introduced in step 1 of the following runnable example.

3.  Wait until the anchor reaches `Tracking`. This prevents you from placing content against an unstable anchor pose. This check is introduced in step 1 of the following runnable example.

4.  When the user chooses a placement pose, instantiate the content and parent it under `anchor.transform`. Parenting the content under the tracked anchor keeps it aligned as VPS2 updates the anchor pose. This code is introduced in step 1 of the following runnable example.

5.  Save the Site anchor payload together with the content's `localPosition` and `localRotation`. Those values are what let you restore the same content relative to the same Site anchor later. This code is introduced in step 1 of the following runnable example. Expand the following example if you want a runnable Unity component that implements this workflow end to end, including tracking the Site anchor, placing content under it, and saving the anchor-relative pose for later restoration.

    Runnable example: Place content relative to a tracked Site anchor

    <div>

    <div class="collapsibleContent_i85q">

    The code comments in this example refer to the workflow steps in the previous list. To wire this example into a runnable scene, do the following:

    This example already includes a small set of `Debug.Log` and `Debug.LogError` statements that you can use during testing. Open the Unity Console while the scene is running to confirm that tracking starts, the placement succeeds, and the pose is saved.

    To keep this example runnable without authentication, use a valid Site anchor payload that you already obtained earlier, then paste that string into the `Anchor Payload` field on the `TrackSiteAnchorAndPlaceContent` component in the Unity Inspector.

    1.  Create a new Unity script file named `TrackSiteAnchorAndPlaceContent.cs`, then replace its contents with the following code: The following example defines the component that tracks a Site anchor, places content under that anchor, and saves the anchor-relative pose:

        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        using System;
        using NianticSpatial.NSDK.AR;
        using NianticSpatial.NSDK.AR.PersistentAnchors;
        using UnityEngine;
        using UnityEngine.UI;
        using UnityEngine.XR.ARSubsystems;

        [Serializable]
        public struct SavedTrackedContent
        {
            public string anchorPayload;
            public Vector3 localPosition;
            public Quaternion localRotation;
        }

        public class TrackSiteAnchorAndPlaceContent : MonoBehaviour
        {
            [SerializeField] private ARVps2Manager _arVps2Manager;
            [SerializeField] private string _anchorPayload;
            [SerializeField] private GameObject _contentPrefab;
            [SerializeField] private Button _placeButton;
            [SerializeField] private Camera _arCamera;

            private ARVps2Anchor _trackedAnchor;
            private string _trackedAnchorPayload;

            private void OnEnable()
            {
                _placeButton.onClick.AddListener(OnPlaceButtonClicked);

                if (!string.IsNullOrWhiteSpace(_anchorPayload))
                {
                    TryTrackSiteAnchor(_anchorPayload);
                }
            }

            private void OnDisable()
            {
                _placeButton.onClick.RemoveListener(OnPlaceButtonClicked);
            }

            public bool TryTrackSiteAnchor(string anchorPayload)
            {
                // Workflow step 2: track the Site anchor from its payload.
                if (!_arVps2Manager.TryTrackAnchor(anchorPayload, out _trackedAnchor))
                {
                    Debug.LogError("TrackSiteAnchorAndPlaceContent: TryTrackAnchor failed.");
                    return false;
                }

                // Workflow step 2: keep the payload so you can save it with the content pose.
                _trackedAnchorPayload = anchorPayload;
                 return true;
             }

            private void OnPlaceButtonClicked()
            {
                // Workflow step 3: wait until the tracked anchor is stable before placing content.
                if (_trackedAnchor == null || _trackedAnchor.trackingState != TrackingState.Tracking)
                {
                    return;
                }

                // Workflow step 4: place the content in world space, then parent it under the tracked anchor.
                var worldPosition = _arCamera.transform.position + _arCamera.transform.forward;
                var worldRotation = Quaternion.LookRotation(_arCamera.transform.forward, Vector3.up);
                var content = Instantiate(_contentPrefab, worldPosition, worldRotation);
                content.transform.SetParent(_trackedAnchor.transform, true);

                // Workflow step 5: save the Site anchor payload plus the content's anchor-local pose.
                var savedPose = new SavedTrackedContent
                {
                    anchorPayload = _trackedAnchorPayload,
                    localPosition = content.transform.localPosition,
                    localRotation = content.transform.localRotation
                };

                SavePose(savedPose);
            }

            private void SavePose(SavedTrackedContent savedPose)
            {
                Debug.Log("TrackSiteAnchorAndPlaceContent: content placed and pose saved.");
                // Store the anchor payload plus the local pose in PlayerPrefs, a file, or your backend.
            }
        }
        ```

        </div>

        </div>

    2.  Create a clean test scene for this example. In a fresh Unity scene, add the following objects from the `Hierarchy` menu:

        - in the `Hierarchy` context menu, choose `XR > AR Session`
        - in the `Hierarchy` context menu, choose `XR > XR Origin (Mobile AR)`
        - create an empty `GameObject`, name it `AR Input Manager`, then use `Add Component` to add `AR Input Manager`
        - in the `Hierarchy` context menu, choose `UI > Canvas`
        - under `Canvas`, choose `UI > Button`
        - an empty `GameObject` named `TrackedContentManager` Then:
        - add [ARVps2Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager/) to `XR Origin`
        - add `TrackSiteAnchorAndPlaceContent` to `TrackedContentManager`
        - add your new scene to `Build Profiles > Scenes` and move it ahead of `Home` so the app opens directly into it on device

    3.  Select the `GameObject` that has the `TrackSiteAnchorAndPlaceContent` component, then assign the five serialized fields in the Inspector:

        - Drag the object that has [ARVps2Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager/) into the `ARVps2Manager` field. In the `nsdk-samples-csharp` project, drag `XR Origin` into the `ARVps2Manager` field.
        - Paste a valid Site anchor payload into the `Anchor Payload` field. In the `nsdk-samples-csharp` project, paste it into the same field on `VPS2LocalizeDemoManager`.
        - Drag your AR camera into the camera field. In the `nsdk-samples-csharp` project, drag `Main Camera` from `XR Origin > Camera Offset > Main Camera` into the camera field.
        - Create or choose the UI button that should trigger placement, then drag it into the button field. In the `nsdk-samples-csharp` project, add `TrackSiteAnchorAndPlaceContent` to `VPS2LocalizeDemoManager`, create a `Button` under `Canvas`, and drag that new button into the button field.
        - Drag the prefab asset you want to place into the content field. For a fast visible test object, create `Hierarchy > 3D Object > Cube`, then drag that `Cube` into your project to create a prefab asset.

    4.  Run the scene and wait for the anchor to reach `Tracking`. `OnEnable()` calls `TryTrackSiteAnchor(_anchorPayload)` automatically when the `Anchor Payload` field is not empty:

        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        TryTrackSiteAnchor(_anchorPayload);
        ```

        </div>

        </div>

        View the anchor status in your device logs by logging `_trackedAnchor.trackingState` while testing. Wait until the anchor status reaches `Tracking` before pressing the button you created in step 3. The on-screen validation order for this runnable example is:

        - launch the scene on device
        - wait for the Site anchor to reach `Tracking`
        - press the placement button once Build to iPhone or Android to validate tracked-anchor placement with a real Site payload.

    </div>

    </div>

6.  Restore the content in a later session. Track the same Site anchor again, then reapply the saved local transform so the content returns to the same real-world location. This code is introduced in steps 1 through 6 of the following runnable example. Expand the following example if you want a runnable Unity restore component for the same workflow. Test it in a second run after you already placed content once and captured the saved payload plus local transform values from step 5.

    Runnable example: Restore content relative to a tracked Site anchor

    <div>

    <div class="collapsibleContent_i85q">

    The code in this example implements the restore phase from step 6 of the previous list. To wire it into the same scene and test it, do the following:

    1.  Create a new Unity script file named `ContentRestore.cs`, then replace its contents with the following code: In the `nsdk-samples-csharp` project, place the script in `NsdkSamples/Assets/Samples/PersistentAR/Scripts`. The following example defines the component that tracks the saved Site anchor again and reapplies the saved local pose when tracking is stable. This script reuses the `SavedTrackedContent` struct that you already created in `TrackSiteAnchorAndPlaceContent.cs` in step 5:

        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        using NianticSpatial.NSDK.AR;
        using NianticSpatial.NSDK.AR.PersistentAnchors;
        using UnityEngine;
        using UnityEngine.XR.ARSubsystems;

        public class ContentRestore : MonoBehaviour
        {
            [SerializeField] private ARVps2Manager _arVps2Manager;
            [SerializeField] private GameObject _contentPrefab;
            [SerializeField] private SavedTrackedContent _savedContent;

            private ARVps2Anchor _trackedAnchor;
            private bool _contentRestored;

            public bool BeginRestore()
            {
                var started = _arVps2Manager.TryTrackAnchor(_savedContent.anchorPayload, out _trackedAnchor);
                Debug.Log($"ContentRestore: BeginRestore started = {started}");
                return started;
            }

            private void Update()
            {
                if (_contentRestored || _trackedAnchor == null || _trackedAnchor.trackingState != TrackingState.Tracking)
                {
                    return;
                }

                var content = Instantiate(_contentPrefab, _trackedAnchor.transform);
                content.transform.localPosition = _savedContent.localPosition;
                content.transform.localRotation = _savedContent.localRotation;
                _contentRestored = true;
                Debug.Log("ContentRestore: content restored under tracked anchor.");
            }
        }
        ```

        </div>

        </div>

    2.  Add `ContentRestore` to the same scene object that already stays active while VPS2 localization is running. In a fresh Unity scene, add it to the same `TrackedContentManager` `GameObject` that already holds `TrackSiteAnchorAndPlaceContent`. In the `nsdk-samples-csharp` project, the closest reference point is `VPS2LocalizeDemoManager` in `NsdkSamples/Assets/Samples/PersistentAR/Scenes/VPS2Localization.unity`.

    3.  Select the `GameObject` that has the `ContentRestore` component, then assign the three serialized fields in the Inspector:

        - Drag the object that has [ARVps2Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager/) into the `ARVps2Manager` field. In the `nsdk-samples-csharp` project, drag `XR Origin` into the `ARVps2Manager` field.
        - Drag the same prefab asset you used during placement into the content field. In the `nsdk-samples-csharp` project, use the same prefab you assigned to `TrackSiteAnchorAndPlaceContent`.
        - Enter the saved `anchorPayload`, `localPosition`, and `localRotation` into the `Saved Content` field. For a real restore test, use the values you captured from the successful placement run in step 5.

    4.  Add a small helper script that starts the restore flow when the scene loads. Create a new Unity script file named `RestoreStarter.cs`, then place it on the same `TrackedContentManager` object as `ContentRestore`.

        The following script example starts the restore flow automatically when the scene loads:

        <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

        <div class="codeBlockContent_QJqH">

        ``` cs
        using UnityEngine;

        public class RestoreStarter : MonoBehaviour
        {
            [SerializeField] private ContentRestore _contentRestore;

            private void Start()
            {
                _contentRestore.BeginRestore();
            }
        }
        ```

        </div>

        </div>

    5.  Select the `GameObject` that has the `RestoreStarter` component, then drag the `ContentRestore` component into the `Content Restore` field. For the restore run, disable `TrackSiteAnchorAndPlaceContent` so the scene does not place more content when it starts.

    6.  Build to iPhone or Android and run the scene again at the same Site. Do not press the placement button in this run. Wait for the anchor to reach `Tracking`. The on-screen validation order for this runnable example is:

        - launch the restore scene on device
        - wait for the Site anchor to reach `Tracking`
        - do not press any placement button in this run, because `RestoreStarter` begins restore automatically The expected result is that the content is recreated automatically under the tracked anchor and returns to the same real-world location.

    </div>

    </div>

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

[TryCreateAnchor](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager.TryCreateAnchor/) is not the default flow for this workflow. The usual path is to track a Site anchor from its payload with [TryTrackAnchor](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager.TryTrackAnchor/) and place content relative to that anchor. Creating an additional anchor is a more advanced case, for example if you need a separate anchor far away from the default Site anchor.

</div>

</div>

### Use a Site mesh with anchored content<a href="#place-content-with-imported-site-mesh" class="hash-link" aria-label="Direct link to Use a Site mesh with anchored content" title="Direct link to Use a Site mesh with anchored content">​</a>

A Site mesh is a 3D model of the physical environment reconstructed from a scan. An app can render it, use it for collision or occlusion, or use it as a visual guide for placing content. The mesh itself does not track the Site.

In the current VPS2 workflow, tracking and mesh geometry are requested separately using the same Site anchor payload:

1.  Get the Site's anchor payload from Scaniverse or the Sites API.
2.  Pass the payload to `ARVps2Manager.TryTrackAnchor` and wait for the returned anchor to reach `Tracking`.
3.  Pass the same payload to `LocationMeshManager.GetLocationMeshForPayloadAsync` to download the Site mesh.
4.  Add the downloaded mesh as a child of the tracked anchor without changing its local transform.
5.  Add virtual content as a child of the tracked anchor. Use the mesh as a guide for its local position, rotation, and scale.

The following excerpt shows how the five steps connect. It is intentionally not a complete component: assign the manager and prefab references, and call the asynchronous portion from your app's tracking flow.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
// 1. Get the payload for the Site you want to track.
string anchorPayload = GetSelectedSiteAnchorPayload();

// 2. Start tracking the Site anchor.
if (!_arVps2Manager.TryTrackAnchor(anchorPayload, out ARVps2Anchor siteAnchor))
    return;

// Run the remaining code after siteAnchor.trackingState reaches Tracking.

// 3. Download the Site mesh using the same payload.
GameObject siteMesh = await _locationMeshManager
    .GetLocationMeshForPayloadAsync(anchorPayload);

// 4. Align the downloaded mesh with the tracked Site anchor.
siteMesh.transform.SetParent(siteAnchor.transform, false);

// 5. Place content relative to the same anchor, using the mesh as a visual guide.
GameObject content = Instantiate(_contentPrefab, siteAnchor.transform);
content.transform.localPosition = contentPositionOnMesh;
content.transform.localRotation = contentRotationOnMesh;
```

</div>

</div>

See [Place content relative to an anchor](#place-content-relative-to-an-anchor) for the full tracked-anchor workflow and [Mesh Download API](https://www.nianticspatial.com/docs/nsdk/how-to/vps/mesh_download/) for mesh download options.

### Place content using geo coordinates<a href="#place-content-using-geo-coordinates" class="hash-link" aria-label="Direct link to Place content using geo coordinates" title="Direct link to Place content using geo coordinates">​</a>

Use this approach when content should appear at a fixed latitude, longitude, and altitude. Use the latest VPS2 localization snapshot to relate AR space to the real world, then convert your target geolocation into an AR pose with [TryGetPose()](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager.TryGetPose/).

Follow this workflow to place content from geo coordinates:

1.  Get the known latitude, longitude, and altitude for the real-world location where the content should appear. For example, these values might come from authored content data, a backend, or a fixed test location. For quick testing, use a known nearby coordinate from a maps app.
2.  Get the latest VPS2 localization from [ARVps2Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager/) with [TryGetLatestLocalization](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager.TryGetLatestLocalization/). The localization snapshot represents the current relationship between AR space and the real world. This code is introduced in step 1 of the following runnable example.
3.  Call [TryGetPose](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager.TryGetPose/) with that localization, the target latitude, longitude, and altitude, and an EDN orientation quaternion (often <a href="https://docs.unity3d.com/ScriptReference/Quaternion-identity.html" target="_blank" rel="noopener noreferrer">Quaternion.identity</a> when the target has no specific heading). When localization is available and the pose conversion succeeds, it returns the pose for that real-world location in AR space. This code is introduced in step 1 of the following runnable example.
4.  Apply the returned pose to your `GameObject` and keep updating it as VPS2 improves. Repeating this conversion lets the content stay aligned to the latest VPS2 estimate. This code is introduced in step 1 of the following runnable example.

The following example converts a fixed geolocation into an AR pose and applies that pose to a Unity `GameObject` as VPS2 improves:

Runnable example: Place content from geo coordinates

<div>

<div class="collapsibleContent_i85q">

The code comments in this example refer to the workflow steps in the previous list. To wire this example into a runnable scene and test it, do the following:

1.  Create a new Unity script file named `GeoPositionedObjectHelper.cs`. In the `nsdk-samples-csharp` project, place the script in `NsdkSamples/Assets/Samples/PersistentAR/Scripts`. The following example defines the component that converts a fixed geolocation into a `GameObject` pose. It includes a small `Debug.Log` you can watch on device to confirm that the helper is applying updated poses:

    <div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` cs
    using NianticSpatial.NSDK.AR;
    using UnityEngine;

    public class GeoPositionedObjectHelper : MonoBehaviour
    {
        [SerializeField] private ARVps2Manager _vps2Manager;
        [SerializeField] private double _latitude;
        [SerializeField] private double _longitude;
        [SerializeField] private double _altitude;

        void Update()
        {
            // Workflow step 2: get the latest VPS2 localization snapshot.
            if (!_vps2Manager.TryGetLatestLocalization(out var localization))
            {
                return;
            }

            // Workflow step 3: convert the target geolocation into an AR pose.
            if (_vps2Manager.TryGetPose(
                    localization,
                    _latitude,
                    _longitude,
                    _altitude,
                    Quaternion.identity,
                    out var pose))
            {
                // Workflow step 4: apply the latest pose to the GameObject.
                gameObject.transform.SetPositionAndRotation(
                    pose.Pose.position,
                    pose.Pose.rotation);
                Debug.Log("GeoPositionedObjectHelper: applied latest pose to GameObject.");
            }
        }
    }
    ```

    </div>

    </div>

2.  Create a clean test scene for this example. In a fresh Unity scene, add the following objects from the `Hierarchy` menu:

    - in the `Hierarchy` context menu, choose `XR > AR Session`
    - in the `Hierarchy` context menu, choose `XR > XR Origin (Mobile AR)`
    - create an empty `GameObject`, name it `AR Input Manager`, then use `Add Component` to add `AR Input Manager`
    - in the `Hierarchy` context menu, choose `3D Object > Cube`, then rename it `GeoContent` Then:
    - add [ARVps2Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager/) to `XR Origin`
    - add `GeoPositionedObjectHelper` to `GeoContent` Add your new scene to `Build Profiles > Scenes` and move it ahead of `Home` so the app opens directly into it on device.

3.  Select the `GameObject` that has the `GeoPositionedObjectHelper` component, then assign the serialized fields in the Inspector:

    - Drag the object that has [ARVps2Manager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.VPS2.ARVps2Manager/) into the `ARVps2Manager` field. In the `nsdk-samples-csharp` project, drag `XR Origin` into the `ARVps2Manager` field.
    - Enter the target latitude in the `Latitude` field. In the `nsdk-samples-csharp` project, enter the latitude for the real-world location you want to test.
    - Enter the target longitude in the `Longitude` field. In the `nsdk-samples-csharp` project, enter the longitude for the same real-world location.
    - Enter the target altitude in the `Altitude` field. In the `nsdk-samples-csharp` project, enter the altitude for that same location. If the latitude and longitude are correct but `GeoContent` is not visible, the altitude may be placing it too high or too low. Start with a large visible cube and adjust altitude until it enters view.

4.  Build to iPhone or Android and run the scene while VPS2 is localizing. This helper does not start VPS2 by itself. It only reads the latest localization after `ARVps2Manager` has started. The on-screen validation order for this runnable example is:

    - launch the scene on device

    - let VPS2 localize normally

    - do not press a placement button, because this helper updates automatically during `Update()` Watch the device logs for:

      The following text example shows the log message that confirms the helper applied an updated pose:

      <div class="language-text codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

      <div class="codeBlockContent_QJqH">

      ``` text
      GeoPositionedObjectHelper: applied latest pose to GameObject.
      ```

      </div>

      </div>

    The expected result is that the visible `GeoContent` cube moves automatically into the AR pose for that real-world location and stays aligned as localization improves. Unlike the anchor-relative example, this flow does not use a placement button.

</div>

</div>

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

When trying this out, set the latitude and longitude in the script to a location close to you for live testing or the playback scan for remote testing.

</div>

</div>

## Test Your Placement<a href="#test-your-placement" class="hash-link" aria-label="Direct link to Test Your Placement" title="Direct link to Test Your Placement">​</a>

Use both Playback and on-location testing during development.

- Playback runs NSDK against a prerecorded AR session dataset instead of live camera input.
- Playback is useful when you want to iterate quickly, repeat the same test path, or debug placement behavior without traveling to the Site each time.
- Playback can help you test geo-coordinate placement and the later placement or restore logic if you already have a valid Site anchor payload.
- Playback does not provide a Site anchor or the default anchor payload, so it cannot validate the full tracked-anchor workflow by itself.
- Playback is still a simulation of a recorded session, so it is best for iteration and debugging rather than final validation.
- On-location device testing is still the most accurate way to confirm that content appears in the correct real-world place for the actual Site.

A practical test flow is:

1.  Use Playback to verify geo-coordinate placement or later placement and restore logic that already has a valid Site anchor payload.
2.  Build to a device and test on location to confirm the full tracked-anchor workflow and the final real-world position of the content at the Site.

To set up Playback, see [How to set up Playback](https://www.nianticspatial.com/docs/nsdk/how-to/playback/setting_up_playback/).

</div>

</div>
