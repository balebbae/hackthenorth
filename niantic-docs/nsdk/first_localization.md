---
source: https://www.nianticspatial.com/docs/nsdk/first_localization/
title: First localization with NSDK
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# First localization with NSDK

</div>

Localization determines a device’s position and orientation in the real world. VPS2 localization provides precise alignment when the device is within a scanned Site that has a Production Asset Version. Outside those areas, localization may be limited or unavailable.

This guide walks through the complete workflow—from installing the Scaniverse app to testing localization at your first scanned location using the NSDK Kotlin or Swift sample apps. You will build Niantic’s NsdkSamples application and use the Sites scene to verify localization on your device.

By the end of this guide, you will:

- Capture a location.
- Generate an Asset Version and set it to **Production**.
- Deploy the sample app.
- Successfully localize at that physical location.

This guide covers the following steps:

1.  [Capture a scan](#capture-a-scan) - Install and use the Scaniverse mobile app to record visual features as you move through a space.
2.  [Upload and process scans](#upload-and-process-scans) - Upload and process scans to convert them into 3D spatial representations of a place, such as meshes or splats.
3.  [Configure assets](#configure-assets) - Set generated assets to production and test localization.
4.  [Build and run](#build-and-run) - Install, configure, build and deploy Niantic's sample application on your desktop and run it on a mobile device.

------------------------------------------------------------------------

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

Before you begin, ensure that you have the following:

- A desktop computer to build and run a mobile app.
- A working <a href="https://git-scm.com/" target="_blank" rel="noopener noreferrer">Git</a> installation.
- A <a href="https://scaniverse.nianticspatial.com/signin" target="_blank" rel="noopener noreferrer">Scaniverse business or enterprise account</a>. If you don't have an account, follow the steps in [Create Account](https://www.nianticspatial.com/docs/nsdk/create_account/) to sign up for one.
- A USB cable to connect your desktop to your mobile device.
- <a href="https://unity.com/download" target="_blank" rel="noopener noreferrer">Unity Hub</a> and *Unity Engine* installed.
- A mobile device compatible with the NSDK
  - An Android device running **Android 7.0 or later** with USB debugging enabled.
  - An iOS device that supports <a href="https://developer.apple.com/augmented-reality/arkit/" target="_blank" rel="noopener noreferrer">ARKit</a>.

------------------------------------------------------------------------

## Capture a scan<a href="#capture-a-scan" class="hash-link" aria-label="Direct link to Capture a scan" title="Direct link to Capture a scan">​</a>

The Scaniverse mobile app uses your device camera to capture live images as you move through a space. Niantic backend services process these scans using the NSDK to create spatial assets for localization. Assets must be set to **Production** before they are available for localization in the sample app or your own applications. After installing the app, you must sign in with a Niantic business or enterprise account.

### Install the Scaniverse app<a href="#install-the-scaniverse-app" class="hash-link" aria-label="Direct link to Install the Scaniverse app" title="Direct link to Install the Scaniverse app">​</a>

1.  Install the latest <a href="https://apps.apple.com/us/app/scaniverse-3d-scanner/id1541433223" target="_blank" rel="noopener noreferrer">Scaniverse app</a> from the Apple App Store on your mobile device.
2.  Open the Scaniverse app on your mobile device.
3.  Select the profile icon, shown as a person, in the top right corner of the app.
    - If you're already logged into Scaniverse as a consumer, sign out.
4.  At the bottom of the login screen, tap **Sign in with Business Account** and sign in using your Niantic business or enterprise account.

<div class="theme-admonition theme-admonition-tip admonition_xJq3 alert alert--success">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)</span>Multiple Organizations

</div>

<div class="admonitionContent_BuS1">

If you are in multiple organizations, you can select your organization by going to **Profile** → **select Organization** dropdown.

</div>

</div>

### Create a private Site<a href="#create-a-private-site" class="hash-link" aria-label="Direct link to Create a private Site" title="Direct link to Create a private Site">​</a>

When you create a Site as a business or enterprise customer, the Sites you create are **private** by default. This means that only you or your organization can access it. You can use a private Site for testing, internal tools, or unreleased locations. You can create a Site either from the Scaniverse app as follows:

1.  Select the **+** button on the top right corner of the app. The **Add private site** window opens.
2.  Under **Site Name**, enter a clear, descriptive, and unique name.
3.  Select **Confirm**.

### Add scans to your Site<a href="#add-scans-to-your-site" class="hash-link" aria-label="Direct link to Add scans to your Site" title="Direct link to Add scans to your Site">​</a>

A scan is a collection of camera images that capture visual features as you move through a space. Each individual scan supports up to five minutes of recording time and can cover up to 500 square meters. For larger environments, capture multiple overlapping Scans within the same Site.

Niantic's backend services use these scans to build a three-dimensional representation of the space. You can use this representation to localize a device by aligning it to the physical environment. You can group multiple scans together in a Site, but they must overlap so that Niantic can connect some of the same visual features into a single, consistent representation. In the following steps, you will create a Site and record scans.

For more reliable localization:

- Capture distinct visual features such as walls, furniture, and decorations.
- Move slowly and steadily to reduce motion blur.
- Include multiple angles and viewpoints.
- Cover the full area that you want to localize to.

For more detailed guidance, see [Scan techniques](https://www.nianticspatial.com/docs/scaniverse/techniques/).

Use a mobile device camera to capture scans as follows:

1.  **Start a scan**

    1.  On your mobile device, select the Site you created in the previous step.
    2.  Select **+ Capture** at the bottom of the screen.
    3.  Select the red button at the bottom of the screen to begin scanning the space.

2.  **Move and capture**

    1.  Point your device camera at the area you want to scan.
    2.  Move slowly and steadily to reduce motion blur.

3.  **Finish and review**

    1.  Select the red button again to stop scanning. A preview of the scan begins to play.
    2.  Select **Localize** at the bottom of the app to quickly check the quality of your scan. The app will use the camera to compare live images against the visual features in the scan to see if it can recognize the location and determine the device position and orientation. If localization fails, you can immediately rescan the environment instead of uploading the scan and discovering problems later.
    3.  Select the pen tool next to the default name to change the name of the scan to a clear, descriptive name.
    4.  Select the trash icon at the bottom left of the screen to discard, or **Save** to keep your scan.

------------------------------------------------------------------------

## Upload and process scans<a href="#upload-and-process-scans" class="hash-link" aria-label="Direct link to Upload and process scans" title="Direct link to Upload and process scans">​</a>

After you capture scans, you upload them so Niantic's backend services can generate spatial assets used for localization and reconstruction. These assets represent the scanned space and can include the following:

- **Mesh** - a 3D surface model for accurate geometry, occlusion and interaction.
- **Splat** - a lightweight 3D representation for efficient visualization and localization.
- **VPS Map** - a nonvisual map that enables localization at a scanned location.

To generate assets, [upload](#upload-scans) your scans and [process](#process-scans) them. To use them in an app, [configure](#configure) the assets by setting them to production. After generation, you can [test localization](#test-localization) to confirm that the scan was processed successfully.

### Upload scans<a href="#upload-scans" class="hash-link" aria-label="Direct link to Upload scans" title="Direct link to Upload scans">​</a>

During upload, your scans are transferred to Niantic’s cloud and prepared for processing. You can upload all scans at once or select them individually. Uploading selectively is useful when working with large scans, testing quality, or reducing processing time and cost.

The Scaniverse app lists all scans for your Site under the **Scans** tab.

Select the scan from the previous step to upload it individually, or select **Upload All** to upload all scans in the Site. After upload, your scans are also available to your team in the Scaniverse Web.

### Process scans<a href="#process-scans" class="hash-link" aria-label="Direct link to Process scans" title="Direct link to Process scans">​</a>

During processing, Niantic's backend services analyze the uploaded scans, extract visual features, and generate spatial assets used to recognize and align a device in the environment. This step generates the assets required for localization and reconstruction. Depending on the size of the scan, this step can take several minutes to over an hour.

Start processing in the Scaniverse app as follows:

1.  Navigate to the **Scans** tab for your Site.
2.  Select the checkbox next to the uploaded scans that you want to process.
3.  Select **Generate Assets** at the top right corner of the main window.
4.  (Optional) Enter a meaningful name under **Version name** to help track changes in the scan.
5.  Select **Confirm**.

Processing typically can take several minutes to over an hour depending on scan complexity. Once processing is complete, newly generated assets will be available in either the Scaniverse Web or the Scaniverse app under **Assets -\> History**.

## Configure assets<a href="#configure-assets" class="hash-link" aria-label="Direct link to Configure assets" title="Direct link to Configure assets">​</a>

After your scans finish processing, Niantic's backend services add the generated assets to your Site. By default, these assets are in a preview state and are not available to live applications.

<div class="theme-admonition theme-admonition-important admonition_xJq3 alert alert--info">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)</span>Production Asset

</div>

<div class="admonitionContent_BuS1">

To make them accessible to users and applications, you must set the asset to production.

</div>

</div>

Once the asset is in production, it becomes available to authenticated applications in your organization.

Set the assets to production state in the Scaniverse app as follows:

1.  Navigate to the **Assets** tab for your Site.
2.  Select the three horizontal dots next to the name of your scan at the bottom of your screen.
3.  Select **Set as Production** from the drop-down list.

Once localization works in Scaniverse, you’re ready to verify it in the NSDK sample app.

### Test localization<a href="#test-localization" class="hash-link" aria-label="Direct link to Test localization" title="Direct link to Test localization">​</a>

Asset generation only creates the underlying spatial data. It does not guarantee that localization will work reliably in a real space. Before using the assets in an app, test localization to confirm the following:

- Devices can reliably localize in the scanned physical space.
- Tracking remains stable and content stays accurately aligned.
- Performance is acceptable across supported devices.
- Changes in lighting, occlusion, or the environment don't prevent successful localization.

Testing localization to ensure your device can match live camera input to your generated asset, and validate the user experience as follows:

1.  Go to the physical place you scanned.
2.  In the Scaniverse app, select the Site that you want to test.
3.  Select the **Assets** tab.
4.  Select **Localize**.
5.  If prompted, select **Allow** to give Scaniverse permission to access your device camera.

The app attempts to match your current camera view to the generated assets. If localization is **successful**, the asset will appear correctly aligned in your environment.

If localization fails, see the following:

Details

<div>

<div class="collapsibleContent_i85q">

Rescan the space using guidelines in the [Capture a scan](#capture-a-scan) section. Once you've completed rescanning the environment, do the following:

1.  Go back to the [Upload and process scans](#upload-and-process-scans) step.
2.  Unselect the scan(s) you are replacing, and select the new scan(s).
3.  Generate assets again.

</div>

</div>

The new asset appears in the **Assets** tab after processing. Previous versions remain available under the **History** tab. Scroll to view different versions of your assets. To test localization, select the three horizontal dots next to its name and select **Test localization**. When you decide which version to use in your app, select the three horizontal dots next to its name and select **Set as Production**.

------------------------------------------------------------------------

## Build and run<a href="#build-and-run" class="hash-link" aria-label="Direct link to Build and run" title="Direct link to Build and run">​</a>

After generating assets, configure and deploy the Niantic sample app to verify localization against your production asset. To do this, [set up the sample app](#set-up-the-sample-app), then [build and deploy](#build-and-deploy) the sample app from your desktop as follows:

### Set up the sample app<a href="#set-up-the-sample-app" class="hash-link" aria-label="Direct link to Set up the sample app" title="Direct link to Set up the sample app">​</a>

In Niantic's sample app, you will run the **Sites** example, which shows how to localize a device and place AR content in a real world environment. The Sites scene retrieves your organization’s Sites and production assets and localizes dynamically without hardcoding anchor payloads.

Do the following:

1.  Clone the Unity Samples repository:
    <div class="language-bash codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

    <div class="codeBlockContent_QJqH">

    ``` bash
    git clone https://github.com/nianticspatial/nsdk-samples-csharp.git
    ```

    </div>

    </div>
2.  Open the Unity samples project in Unity *6000.0.74f1*:
    1.  Launch Unity Hub.
    2.  Select **Add** → **Add project from disk**.
    3.  Navigate into the cloned repo and select the **`NsdkSamples`** folder (the Unity project root, not the repository root).

------------------------------------------------------------------------

### Build and deploy<a href="#build-and-deploy" class="hash-link" aria-label="Direct link to Build and deploy" title="Direct link to Build and deploy">​</a>

1.  Open the **Build Profiles** window by selecting **File** \> **Build Profiles**.
2.  Select iOS or Android, then click **Switch Platform**. After the progress bar finishes, click **Player Settings**. Select your platform from the tabs, scroll down to **Other Settings**, and change the following settings:

<div class="tabs-container tabList__CuJ">

- Android
- iOS

<div class="margin-top--md">

<div class="tabItem_Ymn6 ardkTab" role="tabpanel">

- **Rendering** - Uncheck **Auto Graphics API**. If **Vulkan** appears in the Graphics API list, remove it.
- **Identification** - Set the **Minimum API Level** to **Android 7.0 'Nougat' (API Level 24)** or higher.
- **Configuration** - Set the **Scripting Backend** to **IL2CPP**, then enable both **ARMv7** and **ARM64**.

</div>

<div class="tabItem_Ymn6 ardkTab" role="tabpanel" hidden="">

- **Identification** \> **Signing Team ID** - Enter your iOS app developer key from [developer.apple.com](https://developer.apple.com).
- **Camera Use Description** - Write a description for how you're using AR, such as "NSDK".
- **Target Minimum iOS Version** - Set to **14.0** or higher.
- **Architecture** - Select **ARM64**.

</div>

</div>

</div>

------------------------------------------------------------------------

### Localize in sample app<a href="#localize-in-sample-app" class="hash-link" aria-label="Direct link to Localize in sample app" title="Direct link to Localize in sample app">​</a>

After building the **NsdkSamples** app on your desktop and deploying it to your mobile device, you can run any of Niantic’s sample modules to explore different features.

This guide focuses on the **Sites** sample, which demonstrates how to:

- Browse organizations and Sites associated with your account.
- Select a Site that has a Production Asset Version available.
- Test localization directly at that physical location.

When you select a production asset, the app prepares the Site for localization on your device.

Localization works best in locations that have already been scanned and processed. For best results, return to the same physical space where the scan was captured.

<div class="theme-admonition theme-admonition-info admonition_xJq3 alert alert--info">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)</span>Authentication

</div>

<div class="admonitionContent_BuS1">

Before browsing Sites and assets, you must sign in. The sample app uses authenticated sessions to access your organization’s data from Niantic’s backend services. For more information, see the [Auth guide](https://www.nianticspatial.com/docs/nsdk/auth_getting_started/).

</div>

</div>

Launch the sample app and authenticate as follows:

1.  Ensure you are located at the physical location you scanned.
2.  Open the **NsdkSamples** app on your device.
3.  Sign in using the same account you used to upload and process scans.

<!-- -->

4.  Select **VPS2 Localization** from the main menu.

<!-- -->

5.  Choose your organization.
6.  Select **Start Tracking**.
7.  Point your device camera at the scanned area.
    - Move slowly to help the system match visual features
    - Ensure good lighting matches the scan conditions
8.  Use the following **Localization Tracking State** indicators to adjust how you attempt to localize:
    - Red = not localized
    - Yellow = limited localization
    - Green = precise localization (success)

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/Unity_Sites_Localize_ScreenShot_Annotated-0f55251c35b1685a393452e7ab582d78.png" width="300" alt="NSDK VPS2 Localization scene deployed on iOS device shows visual indicators of localization quality." />

</div>

**View detailed tracking state behavior:**

Details

<div>

<div class="collapsibleContent_i85q">

**Anchor Tracking State** (bottom center)

Each tracked anchor displays visual feedback based on its `AnchorUpdateType`:

- **`NOT_TRACKING`**:

  - Info label: "No anchors tracked".
  - Markers disabled and hidden.
  - No visual indicator.

- **`LIMITED`**:

  - Info label: "coarse".
  - A Large **Cube marker** appears at the anchor location.
  - The mesh marker is disabled and hidden.
  - The device has an approximate location with lower precision.
  - A red arrow appears in front of the camera pointing toward the place of interest.

- **`TRACKING`**:

  - Info label: "precise"
  - A **Mesh marker** with textures overlays the location.
  - The cube marker is disabled and hidden.
  - The device has a precise location with high accuracy.
  - The mesh represents the actual scanned environment geometry.

</div>

</div>

------------------------------------------------------------------------

</div>

</div>
