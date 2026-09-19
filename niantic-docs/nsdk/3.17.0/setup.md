---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/
title: Setting Up the Niantic SDK
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Setting Up the Niantic SDK for Unity

</div>

To set up the Niantic SDK for Unity, you will need to:

1.  Create an Account
2.  Download and install the Unity Hub and the Unity Engine
3.  Install the Niantic SDK Unity packages
4.  Authenticate Niantic SDK in Unity
5.  Activate the XR Loader for your platform
6.  Configure Unity for the platform your AR experience will run on
7.  Set up a basic Unity AR scene

## Create an Account<a href="#create-an-account" class="hash-link" aria-label="Direct link to Create an Account" title="Direct link to Create an Account">​</a>

Before getting started with the NSDK setup, it is highly recommended to create an account since a couple of steps will require one.

You can find our guide to walk you through creating an account [here](https://www.nianticspatial.com/docs/nsdk/3.17.0/create_account/).

## Download and Install Unity<a href="#download-and-install-unity" class="hash-link" aria-label="Direct link to Download and Install Unity" title="Direct link to Download and Install Unity">​</a>

In order to install the Unity 3D Engine you must first install the <a href="https://unity.com/download" target="_blank" rel="noopener noreferrer">Unity Hub</a> which gives you access to the latest versions of the currently supported engines.

NSDK only supports **Unity LTS** and, as of the time of writing, officially supports **Unity 6000.0.58f2** and Unity **2022.3.62f2**. If you no longer see those engine versions in the Unity Hub downloads window, you can locate them by going to the download archive.

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

You may notice that you can use any version of 6000.0.x and 2022.3.x and be okay. However, we have noticed in the past that some of these patch updates performed on the engine can introduce conflicts with NSDK. For maximum compatibility it’s recommended to stick to the versions mentioned above.

</div>

</div>

## Create a Project and install the Niantic SDK Packages<a href="#create-a-project-and-install-the-niantic-sdk-packages" class="hash-link" aria-label="Direct link to Create a Project and install the Niantic SDK Packages" title="Direct link to Create a Project and install the Niantic SDK Packages">​</a>

<div class="tabs-container tabList__CuJ">

- Android
- iOS
- Meta Quest 3

<div class="margin-top--md">

<div class="tabItem_Ymn6 ardkTab" role="tabpanel">

## Create a Project and Install NSDK

1.  Create a new Unity project with the **3D (Built-In Render Pipeline)** template. Alternatively, if planning to use Unity's Universal Render Pipeline select the **Universal 3D (Core)** template.

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

If you are using or plan to use the Universal Render Pipeline (URP), refer to [How to Set Up NRDK with the Universal Render Pipeline](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/urp/) for additional setup instructions.

</div>

</div>

2.  In your Unity project, open the **Window** top menu, then select **Package Manager**.

3.  From the plus menu on the Package Manager tab, select **Add package from git URL...**.

    <img src="https://www.nianticspatial.com/docs/assets/images/add_package_from_git-7bda3be7f261a0e08271e7fb2f5e879d.jpg" style="width:25.0%" alt="Package Manager menu" />

4.  Enter `https://github.com/niantic-lightship/ardk-upm.git`.
    1.  If prompted, click **Yes** to activate the new Input System Package for ARFoundation 5.0. This may require a restart of the Unity Editor.

5.  To add the SharedAR package, repeat these steps using the following URL instead: `https://github.com/niantic-lightship/sharedar-upm.git`.

To use a specific ARDK version, download its `.tgz` from our release pages (<a href="https://github.com/niantic-lightship/ardk-upm/releases" target="_blank" rel="noopener noreferrer">ardk-upm</a>, <a href="https://github.com/niantic-lightship/sharedar-upm/releases" target="_blank" rel="noopener noreferrer">sharedar-upm</a>). Then, follow the installation instructions above and select "**Add package from tarball**" instead of the Git URL.

</div>

<div class="tabItem_Ymn6 ardkTab" role="tabpanel" hidden="">

## Create a Project and Install NSDK

1.  Create a new Unity project with the **3D (Built-In Render Pipeline)** template. Alternatively, if planning to use Unity's Universal Render Pipeline select the **Universal 3D (Core)** template.

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

If you are using or plan to use the Universal Render Pipeline (URP), refer to [How to Set Up NRDK with the Universal Render Pipeline](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/ar/urp/) for additional setup instructions.

</div>

</div>

2.  In your Unity project, open the **Window** top menu, then select **Package Manager**.

3.  From the plus menu on the Package Manager tab, select **Add package from git URL...**.

    <img src="https://www.nianticspatial.com/docs/assets/images/add_package_from_git-7bda3be7f261a0e08271e7fb2f5e879d.jpg" style="width:25.0%" alt="Package Manager menu" />

4.  Enter `https://github.com/niantic-lightship/ardk-upm.git`.
    1.  If prompted, click **Yes** to activate the new Input System Package for ARFoundation 5.0. This may require a restart of the Unity Editor.

5.  To add the SharedAR package, repeat these steps using the following URL instead: `https://github.com/niantic-lightship/sharedar-upm.git`.

To use a specific ARDK version, download its `.tgz` from our release pages (<a href="https://github.com/niantic-lightship/ardk-upm/releases" target="_blank" rel="noopener noreferrer">ardk-upm</a>, <a href="https://github.com/niantic-lightship/sharedar-upm/releases" target="_blank" rel="noopener noreferrer">sharedar-upm</a>). Then, follow the installation instructions above and select "**Add package from tarball**" instead of the Git URL.

</div>

<div class="tabItem_Ymn6 ardkTab" role="tabpanel" hidden="">

The Niantic SDK leverages **Meta XR Core SDK** and **Unity's XR Core Plugin** to support the **Meta Quest 3**.

Follow Meta's <a href="https://developers.meta.com/horizon/documentation/unity/unity-project-setup/" target="_blank" rel="noopener noreferrer">official tutorial</a> to begin developing for the Meta Quest 3 in Unity 6.

#### Notes & Caveats<a href="#notes--caveats" class="hash-link" aria-label="Direct link to Notes &amp; Caveats" title="Direct link to Notes &amp; Caveats">​</a>

- Ensure you're using a supported version of Unity 6 (such as **6000.0.58f2**) and the **OpenXR** plugin (com.unity.xr.openxr).
- The **Meta XR Core SDK** must be acquired from the <a href="https://assetstore.unity.com/packages/tools/integration/meta-xr-core-sdk-269169" target="_blank" rel="noopener noreferrer">Unity Asset Store</a>, as explained in the Meta docs. Select **Enable Feature Set** if prompted.
- If prompted to restart the Unity Editor, do so with **Restart Editor**.
- Verify the Quest's OS version is \>=v74

1.  Go to Meta → Tools → Project Setup Tools and resolve all issues.

2.  In your Unity project, open the **Window** top menu, then select **Package Manager**.

3.  From the plus menu on the Package Manager tab, select **Add package from git URL...**.

    <img src="https://www.nianticspatial.com/docs/assets/images/add_package_from_git-7bda3be7f261a0e08271e7fb2f5e879d.jpg" style="width:25.0%" alt="Package Manager menu" />

4.  Enter `https://github.com/niantic-lightship/ardk-upm.git`.
    1.  If prompted, click **Yes** to activate the new Input System Package for ARFoundation 6.1. This may require a restart of the Unity Editor.

5.  Install the **Lightship Quest Package** by repeating these steps using the following URL instead: `https://github.com/niantic-lightship/ardk-quest3-upm.git`.

To use a specific ARDK version, download its `.tgz` from our release pages (<a href="https://github.com/niantic-lightship/ardk-upm/releases" target="_blank" rel="noopener noreferrer">ardk-upm</a>, <a href="https://github.com/niantic-lightship/sharedar-upm/releases" target="_blank" rel="noopener noreferrer">sharedar-upm</a>). Then, follow the installation instructions above and select "**Add package from tarball**" instead of the Git URL.

</div>

</div>

</div>

## Authenticate Niantic SDK in Unity<a href="#authenticate-niantic-sdk-in-unity" class="hash-link" aria-label="Direct link to Authenticate Niantic SDK in Unity" title="Direct link to Authenticate Niantic SDK in Unity">​</a>

1.  Authenticate with API Key
    1.  In Unity, navigate to the top menu bar and select the **Lightship** tab, then select **Settings** to open the Lightship Settings menu.
    2.  Click on **Get API Key** under **Credentials**. This should open the lightship.dev website in a browser window. Note that lightship.dev has migrated to scaniverse.nianticspatial.com. You will be able to get your API keys for your pre-existing 3.17 projects.
    3.  Log into your Niantic Spatial account or [create an account](https://www.nianticspatial.com/docs/nsdk/3.17.0/create_account/) if you haven't done so for new projects.
    4.  Open the **Projects** page, then select an existing project or create a new one by clicking **New Project**.
    5.  In your project's **Overview**, copy the API Key by clicking the copy icon next to it.
    6.  Back in Unity, return to the **Lightship Settings** and paste your API Key into the **API Key** field.

## Activate the XR Loader for Your Mobile Platform<a href="#activate-the-xr-loader-for-your-mobile-platform" class="hash-link" aria-label="Direct link to Activate the XR Loader for Your Mobile Platform" title="Direct link to Activate the XR Loader for Your Mobile Platform">​</a>

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

In Unity versions **2022.3.10f1** or newer, you might see a [benign error](https://www.nianticspatial.com/docs/nsdk/3.17.0/release_notes/#known-issues) in the console after following these steps.

</div>

</div>

<div class="tabs-container tabList__CuJ">

- Android
- iOS
- Meta Quest 3

<div class="margin-top--md">

<div class="tabItem_Ymn6 ardkTab" role="tabpanel">

1.  Open the **Lightship** top menu, then select **XR Plug-in Management**.
2.  In the **XR Plug-in Management** menu, select the Android tab, then check the box labeled **Niantic Lightship SDK + Google ARCore**.

</div>

<div class="tabItem_Ymn6 ardkTab" role="tabpanel" hidden="">

1.  Open the **Lightship** top menu, then select **XR Plug-in Management**.
2.  In the **XR Plug-in Management** menu, select the iOS tab, then check the box labeled **Niantic Lightship SDK + Apple ARKit**.

</div>

<div class="tabItem_Ymn6 ardkTab" role="tabpanel" hidden="">

1.  Open the **Lightship** top menu, then select **XR Plug-in Management**.

2.  In the **XR Plug-in Management** menu, select the Android tab, then check the box labeled **OpenXR** and all of its children.
    <img src="https://www.nianticspatial.com/docs/assets/images/quest3_plugins-73de3fa4a583dc69c212a4b1a6b7af01.png" data-align="center" width="700" alt="Setting the plugins for Meta Quest 3" />

3.  From the **Lightship** menu in the top toolbar, click the **Run Setup for Meta** button. Your enabled **OpenXR** features should look like this:

    <img src="https://www.nianticspatial.com/docs/assets/images/quest3_xrfeatures-90d2949e2cb786c924ec0ce464db7786.png" data-align="center" width="700" alt="OpenXR features for Meta Quest 3" />

    **Take extra caution to ensure the only camera passthrough selected is the Lightship Meta AR Camera (Passthrough) as the Meta Quest: Camera (Passthrough) is not compatible.**

4.  If necessary, resolve any remaining errors from the **Project Validation** window under the **Lightship** top menu. Some warnings messages are to be expected.
    <img src="https://www.nianticspatial.com/docs/assets/images/quest3_projectvalidation-fab2f502e3904e0224df25100c815977.png" data-align="center" width="700" alt="Meta Quest 3 Project Validation Example" />

</div>

</div>

</div>

## Configure the Build Platform<a href="#configure-the-build-platform" class="hash-link" aria-label="Direct link to Configure the Build Platform" title="Direct link to Configure the Build Platform">​</a>

1.  Open the **Build Profiles** window by selecting **File** \> **Build Profiles**.
2.  Select iOS or Android, then click **Switch Platform**. After the progress bar finishes, click **Player Settings**. Select your platform from the tabs, scroll down to **Other Settings**, and change the following settings:

<div class="tabs-container tabList__CuJ">

- Android
- iOS
- Meta Quest 3

<div class="margin-top--md">

<div class="tabItem_Ymn6 ardkTab" role="tabpanel">

- **Rendering** - Uncheck **Auto Graphics API**. If **Vulkan** appears in the Graphics API list, remove it.
- **Identification** - Set the **Minimum API Level** to **Android 7.0 'Nougat' (API Level 24)** or higher.
- **Configuration** - Set the **Scripting Backend** to **IL2CPP**, then enable both **ARMv7** and **ARM64**.

</div>

<div class="tabItem_Ymn6 ardkTab" role="tabpanel" hidden="">

- **Identification** \> **Signing Team ID** - Enter your iOS app developer key from [developer.apple.com](https://developer.apple.com).
- **Camera Use Description** - Write a description for how you're using AR, such as "Lightship NSDK".
- **Target Minimum iOS Version** - Set to **14.0** or higher.
- **Architecture** - Select **ARM64**.

</div>

<div class="tabItem_Ymn6 ardkTab" role="tabpanel" hidden="">

Nothing to do here. All configurations should have been taken care of by the Run Setup for Meta option.

</div>

</div>

</div>

## Next Steps<a href="#next-steps" class="hash-link" aria-label="Direct link to Next Steps" title="Direct link to Next Steps">​</a>

### Setting Up a Basic AR Scene<a href="#setting-up-a-basic-ar-scene" class="hash-link" aria-label="Direct link to Setting Up a Basic AR Scene" title="Direct link to Setting Up a Basic AR Scene">​</a>

<div class="tabs-container tabList__CuJ">

- Android
- iOS
- Meta Quest 3

<div class="margin-top--md">

<div class="tabItem_Ymn6 ardkTab" role="tabpanel">

To get started creating your own AR project, begin by creating an empty AR scene:

1.  Create a new Basic scene:
    1.  From the main menu, choose **File** \> **New Scene**.
    2.  Select **Basic (Built-in)** and click **Create**.
2.  Right-click on the **Main Camera** and select **Delete**.
3.  Add an **ARSession** and **XROrigin** to your new scene
    1.  Select the new scene in the **Hierarchy**.
    2.  From the main menu, select **Game Object** \> **XR** \> **AR Session**.
    3.  Repeat to add an **XR Origin (Mobile AR)**.
4.  Save the scene using **File** \> **Save**.

<div class="theme-admonition theme-admonition-tip admonition_xJq3 alert alert--success">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)</span>tip

</div>

<div class="admonitionContent_BuS1">

If you choose **Save As Scene Template**, you can select this scene in the **New Scene** dialog next time.

</div>

</div>

</div>

<div class="tabItem_Ymn6 ardkTab" role="tabpanel" hidden="">

To get started creating your own AR project, begin by creating an empty AR scene:

1.  Create a new Basic scene:
    1.  From the main menu, choose **File** \> **New Scene**.
    2.  Select **Basic (Built-in)** and click **Create**.
2.  Right-click on the **Main Camera** and select **Delete**.
3.  Add an **ARSession** and **XROrigin** to your new scene
    1.  Select the new scene in the **Hierarchy**.
    2.  From the main menu, select **Game Object** \> **XR** \> **AR Session**.
    3.  Repeat to add an **XR Origin (Mobile AR)**.
4.  Save the scene using **File** \> **Save**.

<div class="theme-admonition theme-admonition-tip admonition_xJq3 alert alert--success">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)</span>tip

</div>

<div class="admonitionContent_BuS1">

If you choose **Save As Scene Template**, you can select this scene in the **New Scene** dialog next time.

</div>

</div>

</div>

<div class="tabItem_Ymn6 ardkTab" role="tabpanel" hidden="">

To get started creating your own AR project, begin by creating an empty AR scene:

1.  Create a new Basic scene:
    1.  From the main menu, choose **File** \> **New Scene**.
    2.  Select **Basic (Built-in)** and click **Create**.
2.  Right-click on the **Main Camera** and select **Delete**.
3.  Add an **ARSession** and **XROrigin** to your new scene
    1.  Select the new scene in the **Hierarchy**.
    2.  From the main menu, select **Game Object** \> **XR** \> **AR Session**.
    3.  Repeat to add an **XR Origin (Mobile AR)**.
4.  Save the scene using **File** \> **Save**.

<div class="theme-admonition theme-admonition-tip admonition_xJq3 alert alert--success">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)</span>tip

</div>

<div class="admonitionContent_BuS1">

If you choose **Save As Scene Template**, you can select this scene in the **New Scene** dialog next time.

</div>

</div>

</div>

</div>

</div>

</div>

</div>
