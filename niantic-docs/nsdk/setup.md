---
source: https://www.nianticspatial.com/docs/nsdk/setup/
title: Set up the Niantic SDK
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Set up the Niantic SDK for Unity

</div>

The Niantic Spatial SDK (NSDK) for Unity extends AR Foundation with Niantic Spatial features for VPS localization, depth, occlusion, meshing, semantics, and developer tools such as playback and project validation, so you can build Unity AR experiences with real-world localization, contextual awareness, and NSDK development workflows.

### Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

Before you begin, decide whether you are building for Android, iOS, or Meta Quest 3. If you are building for iOS, you will also need Apple Developer account setup for signing.

## AI set up<a href="#ai-set-up" class="hash-link" aria-label="Direct link to AI set up" title="Direct link to AI set up">​</a>

Niantic Spatial provides a **Unity Setup Skill** containing the NSDK setup workflow. AI assistants can use the Skill to guide or automate NSDK installation and configuration, helping you complete the steps on this page more quickly.

To use an **AI coding assistant** to set up the Niantic SDK for you, do the following:

1.  Download the <a href="https://www.nianticspatial.com/docs/skills/niantic-nsdk-unity-setup.zip" download="">Unity setup Skill</a>.
2.  Extract and place the folder into your AI assistant's skills directory. For example:
    - Claude Code: `.claude/skills/`
    - Codex: `.agents/skills/`
3.  Create or open an existing Unity project. If you're creating a new project, use the 3D (Built-In Render Pipeline) or Universal 3D (Core) template.
4.  Ask your AI assistant to set up NSDK in your project. It will guide you through the required steps and help configure your project.

## Manual set up<a href="#manual-set-up" class="hash-link" aria-label="Direct link to Manual set up" title="Direct link to Manual set up">​</a>

To **manually** set up the Niantic SDK for Unity, you will need to:

1.  [Create an account](#create-an-account).
2.  [Download and install](#download-and-install-unity) the Unity Hub and the Unity Engine.
3.  [Install the Niantic SDK Unity packages](#install-the-niantic-sdk-packages).
4.  [Authenticate Niantic SDK in Unity](#authenticate-niantic-sdk-in-unity).
5.  [Activate the XR Loader](#activate-the-xr-loader) for your mobile platform.
6.  [Configure the build platform](#configure-the-build-platform) in Unity for your target device.
7.  [Set up a basic AR scene](#set-up-a-basic-ar-scene) to test your configuration.

Steps to manually set up the NSDK are shown in the following sections.

------------------------------------------------------------------------

### Create an account<a href="#create-an-account" class="hash-link" aria-label="Direct link to Create an account" title="Direct link to Create an account">​</a>

Before getting started with the NSDK setup, follow the steps to [create a Scaniverse account](https://www.nianticspatial.com/docs/nsdk/create_account/#create-a-scaniverse-account). You will use this account either to sign in through **NSDK \> Settings** in the Unity Editor or to create a developer token, depending on the authorization path you choose.

For authorization options, see [Authorization](https://www.nianticspatial.com/docs/nsdk/auth_getting_started/).

### Download and install Unity<a href="#download-and-install-unity" class="hash-link" aria-label="Direct link to Download and install Unity" title="Direct link to Download and install Unity">​</a>

In order to install the Unity 3D Engine you must first install the <a href="https://unity.com/download" target="_blank" rel="noopener noreferrer">Unity Hub</a> which gives you access to the latest versions of the currently supported engines.

NSDK only supports **Unity LTS** and **Unity 6000.0.74f1**. If you no longer see this engine version in the Unity Hub downloads window, go to the <a href="https://unity.com/releases/editor/archive" target="_blank" rel="noopener noreferrer">Unity download archive</a> to locate it. Using any other version of 6000.0.x can introduce conflicts with NSDK and is not recommended.

### Install the Niantic SDK Packages<a href="#install-the-niantic-sdk-packages" class="hash-link" aria-label="Direct link to Install the Niantic SDK Packages" title="Direct link to Install the Niantic SDK Packages">​</a>

Use the following platform-specific instructions to create your Unity project and add the NSDK packages through Unity Package Manager. Select the tab for your target platform before you begin.

<div class="tabs-container tabList__CuJ">

- Android
- iOS
- Meta Quest 3

<div class="margin-top--md">

<div class="tabItem_Ymn6 ardkTab" role="tabpanel">

1.  Create a new Unity project with the **3D (Built-In Render Pipeline)** template. Alternatively, if planning to use Unity's Universal Render Pipeline select the **Universal 3D (Core)** template.

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

If you are using or plan to use the Universal Render Pipeline (URP), refer to [How to Set Up NRDK with the Universal Render Pipeline](https://www.nianticspatial.com/docs/nsdk/how-to/ar/urp/) for additional setup instructions.

</div>

</div>

2.  In your Unity project, open the **Window** top menu, then select **Package Manager**.

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

If you are using Unity **6000.0.X**, you must update the **AR Foundation** package to a minimum of **6.3.0**, but we recommend **6.4.1**.

</div>

</div>

1.  From the plus menu on the Package Manager tab, select **Add package from git URL...**.

    <img src="https://www.nianticspatial.com/docs/assets/images/add_package_from_git-7bda3be7f261a0e08271e7fb2f5e879d.jpg" style="width:25.0%" alt="Package Manager menu" />

2.  Enter `https://github.com/nianticspatial/nsdk-library-upm.git`.
    1.  If prompted, select **Yes** to activate the new Input System Package. This may require a restart of the Unity Editor.

To install a specific NSDK version, use **Add package from git URL...** and append the Git tag, branch, or commit after a `#`. For example: `https://github.com/nianticspatial/nsdk-library-upm.git#vX.Y.Z`.

The official installation path is **Add package from git URL...**. If you want to install NSDK locally instead:

1.  Download and unzip the **Source code (zip)** from the Unity package <a href="https://github.com/nianticspatial/nsdk-library-upm/releases" target="_blank" rel="noopener noreferrer">release</a> repository.
2.  In Unity, open **Window \> Package Management \> Package Manager**.
3.  Open the drop-down menu next to the **+** in the top-left main window.
4.  Select **Install Package From Disk** in Unity Package Manager
5.  Select the root `package.json` file.

Do not use GitHub source archives from **Download ZIP / tar.gz** or **Add package from tarball** for this workflow.

</div>

<div class="tabItem_Ymn6 ardkTab" role="tabpanel" hidden="">

1.  Create a new Unity project with the **3D (Built-In Render Pipeline)** template. Alternatively, if planning to use Unity's Universal Render Pipeline select the **Universal 3D (Core)** template.

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

If you are using or plan to use the Universal Render Pipeline (URP), refer to [How to Set Up NRDK with the Universal Render Pipeline](https://www.nianticspatial.com/docs/nsdk/how-to/ar/urp/) for additional setup instructions.

</div>

</div>

2.  In your Unity project, open the **Window** top menu, then select **Package Manager**.

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

If you are using Unity **6000.0.X**, you must update the **AR Foundation** package to a minimum of **6.3.0**, but we recommend **6.4.1**.

</div>

</div>

1.  From the plus menu on the Package Manager tab, select **Add package from git URL...**.

    <img src="https://www.nianticspatial.com/docs/assets/images/add_package_from_git-7bda3be7f261a0e08271e7fb2f5e879d.jpg" style="width:25.0%" alt="Package Manager menu" />

2.  Enter `https://github.com/nianticspatial/nsdk-library-upm.git`.
    1.  If prompted, select **Yes** to activate the new Input System Package. This may require a restart of the Unity Editor.

To install a specific NSDK version, use **Add package from git URL...** and append the Git tag, branch, or commit after a `#`. For example: `https://github.com/nianticspatial/nsdk-library-upm.git#vX.Y.Z`.

The official installation path is **Add package from git URL...**. If you want to install NSDK locally instead:

1.  Download and unzip the **Source code (zip)** from the Unity package <a href="https://github.com/nianticspatial/nsdk-library-upm/releases" target="_blank" rel="noopener noreferrer">release</a> repository.
2.  In Unity, open **Window \> Package Management \> Package Manager**.
3.  Open the drop-down menu next to the **+** in the top-left main window.
4.  Select **Install Package From Disk** in Unity Package Manager
5.  Select the root `package.json` file.

Do not use GitHub source archives from **Download ZIP / tar.gz** or **Add package from tarball** for this workflow.

</div>

<div class="tabItem_Ymn6 ardkTab" role="tabpanel" hidden="">

The Niantic SDK leverages **Meta XR Core SDK** and **Unity's XR Core Plugin** to support the **Meta Quest 3**.

Follow Meta's <a href="https://developers.meta.com/horizon/documentation/unity/unity-project-setup/" target="_blank" rel="noopener noreferrer">official tutorial</a> to begin developing for the Meta Quest 3 in Unity 6.

#### Notes & Caveats<a href="#notes--caveats" class="hash-link" aria-label="Direct link to Notes &amp; Caveats" title="Direct link to Notes &amp; Caveats">​</a>

- Ensure you're using a supported version of Unity 6 (such as **6000.0.74f1**) and the **OpenXR** plugin (`com.unity.xr.openxr`) version **1.15.1**. Version 1.16.1 is known to cause issues, so force the package to **1.15.1** in the Package Manager.
- The **Meta XR Core SDK** must be acquired from the <a href="https://assetstore.unity.com/packages/tools/integration/meta-xr-core-sdk-269169" target="_blank" rel="noopener noreferrer">Unity Asset Store</a>, as explained in the Meta docs. Select **Enable Feature Set** if prompted.
- If prompted to restart the Unity Editor, do so with **Restart Editor**.
- Verify the Quest's OS version is \>=v74

1.  Go to Meta → Tools → Project Setup Tools and resolve all issues.

2.  In your Unity project, open the **Window** top menu, then select **Package Manager**.

3.  From the plus menu on the Package Manager tab, select **Add package from git URL...**.

    <img src="https://www.nianticspatial.com/docs/assets/images/add_package_from_git-7bda3be7f261a0e08271e7fb2f5e879d.jpg" style="width:25.0%" alt="Package Manager menu" />

4.  Enter `https://github.com/nianticspatial/nsdk-library-upm.git`.
    1.  If prompted, select **Yes** to activate the new Input System Package. This may require a restart of the Unity Editor.

5.  Install the **NSDK Quest Package** by repeating these steps using the following URL instead: `https://github.com/nianticspatial/nsdk-library-upm-quest3.git`.

To install a specific NSDK version, use **Add package from git URL...** and append the same Git tag, branch, or commit to both package URLs. For example:

- `https://github.com/nianticspatial/nsdk-library-upm.git#vX.Y.Z`
- `https://github.com/nianticspatial/nsdk-library-upm-quest3.git#vX.Y.Z`

</div>

</div>

</div>

### Authenticate Niantic SDK in Unity<a href="#authenticate-niantic-sdk-in-unity" class="hash-link" aria-label="Direct link to Authenticate Niantic SDK in Unity" title="Direct link to Authenticate Niantic SDK in Unity">​</a>

Authenticate NSDK in Unity before you build and run your project. You can do this in one of two ways:

1.  Sign in through the Unity Editor:

    1.  In Unity's top menu bar, select **NSDK**.
    2.  Select **Settings**.
    3.  Sign in to your Scaniverse account.

2.  Provide an access token directly to NSDK: For development and internal testing, create a developer token in <a href="https://scaniverse.nianticspatial.com/signin" target="_blank" rel="noopener noreferrer">Scaniverse Web</a>. For production apps, use an access token from your backend.

    Then choose **one** of the following ways to provide that token to NSDK:

    - In Project Settings, paste it into **Edit \> Project Settings \> XR Plug-in Management \> Niantic Spatial Development Kit \> Credentials \> Niantic Spatial Access Token**.
    - In code, set `NsdkSettingsHelper.ActiveSettings.AccessToken`.

For more information, see [Authorization](https://www.nianticspatial.com/docs/nsdk/auth_getting_started/), [Generate developer tokens](https://www.nianticspatial.com/docs/nsdk/auth_developer_token/), and [Generate access tokens](https://www.nianticspatial.com/docs/nsdk/auth_backend/).

Before you continue, confirm that one of these authentication paths is set up. Importing NSDK adds an `AuthBuildSettings` asset, and that asset can be empty, so a successful build does not confirm that authentication is configured.

### Activate the XR loader<a href="#activate-the-xr-loader" class="hash-link" aria-label="Direct link to Activate the XR loader" title="Direct link to Activate the XR loader">​</a>

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

In Unity versions **6000.0.74f1** or newer, you might see a [benign error](https://www.nianticspatial.com/docs/nsdk/release_notes/#known-issues) in the console after following these steps.

</div>

</div>

<div class="tabs-container tabList__CuJ">

- Android
- iOS

<div class="margin-top--md">

<div class="tabItem_Ymn6 ardkTab" role="tabpanel">

1.  Open the **NSDK** top menu, then select **XR Plug-in Management**.
2.  In the **XR Plug-in Management** menu, select the Android tab, then check the box labeled **Niantic Spatial Development Kit + Google ARCore**.

</div>

<div class="tabItem_Ymn6 ardkTab" role="tabpanel" hidden="">

1.  Open the **NSDK** top menu, then select **XR Plug-in Management**.
2.  In the **XR Plug-in Management** menu, select the iOS tab, then check the box labeled **Niantic Spatial Development Kit + Apple ARKit**.

</div>

</div>

</div>

### Configure the build platform<a href="#configure-the-build-platform" class="hash-link" aria-label="Direct link to Configure the build platform" title="Direct link to Configure the build platform">​</a>

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

In Unity, NSDK is configured through components and project settings. Once enabled, the SDK automatically receives AR frame and sensor data and updates each frame at runtime.

### Set up a basic AR scene<a href="#set-up-a-basic-ar-scene" class="hash-link" aria-label="Direct link to Set up a basic AR scene" title="Direct link to Set up a basic AR scene">​</a>

<div class="tabs-container tabList__CuJ">

- Android
- iOS

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

</div>

</div>

## Next steps<a href="#next-steps" class="hash-link" aria-label="Direct link to Next steps" title="Direct link to Next steps">​</a>

After your project is set up, continue to [Unity sample projects](https://www.nianticspatial.com/docs/nsdk/sample_projects/) to explore working examples of NSDK features.

</div>

</div>
