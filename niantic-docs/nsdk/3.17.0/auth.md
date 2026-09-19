---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/auth/
title: Authentication
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Authentication

</div>

## Introduction<a href="#introduction" class="hash-link" aria-label="Direct link to Introduction" title="Direct link to Introduction">​</a>

NSDK is now providing a token-based authentication system as an alternative to the API-key based system. All existing endpoints are still supported, but the API-key is no longer required. Some new features will only be available under the new authentication system.

## Enabling The Login Flow<a href="#login-enable" class="hash-link" aria-label="Direct link to Enabling The Login Flow" title="Direct link to Enabling The Login Flow">​</a>

Token-based authentication is currently hidden behind a script compilation flag `NIANTIC_ARDK_AUTH_LOGIN`. Add `NIANTIC_ARDK_AUTH_LOGIN` under `Scripting Define Symbols` in **Project Settings → Player**.

1.  Open the **Project Settings** window
2.  Select **Player** and then **Other Settings**
3.  In **Player**, select target platform
4.  Under the platform settings, select **Scripting Define Symbols**
5.  Enter `NIANTIC_ARDK_AUTH_LOGIN`
6.  Hit **Apply**

![Update Scripting Define Symbols to include NIANTIC_ARDK_AUTH_LOGIN and NIANTIC_ARDK_AUTH_DEBUG](https://www.nianticspatial.com/docs/assets/images/unity_scripting_symbols-146951b475eb300361c7d1f1ad2487b6.png)

**Note**: This should be repeated for each platform you are targeting.

## Login<a href="#login" class="hash-link" aria-label="Direct link to Login" title="Direct link to Login">​</a>

The login button is part of **Lightship SDK Settings**.

Steps:

1.  Enter **Project Settings** → **Niantic Lightship SDK Page** (see screenshot)
2.  Select **Login** (this will open "Sign In" page in the browser)
3.  Sign in with Google SSO. Success will show: i. "Login Successful" in the browser. ii. "Logout" replaces the "Login" button in Unity's **Project Settings**

![Lightship SDK Settings](https://www.nianticspatial.com/docs/assets/images/unity_sdk_settings-26c4ec6a1891f8e10d44eddfe5de6c08.png)![Login Successful!](https://www.nianticspatial.com/docs/assets/images/web_login_success-483e3439e90df7b7424821602effc6f0.png)

**Note**: API key is no longer required. If you're using token-base authentication, it should not be set.

## Advanced Knowledge/Troubleshooting<a href="#advanced-knowledgetroubleshooting" class="hash-link" aria-label="Direct link to Advanced Knowledge/Troubleshooting" title="Direct link to Advanced Knowledge/Troubleshooting">​</a>

**Working Files**

In Unity, the files that track the auth tokens are located outside of the project folder.

On MacOs, they are located at: `/Users/<username>/.ardkSettings/<project ID>`

On Windows, they are located at: `C:\ProgramData\<project ID>`

The project ID is a unique hash representing the project. There are two files: `authEditorSettings.json` and `authEditorBuildSettings.json`. These contain the current auth tokens. If you encounter problems that can’t be resolved by other means, it may help to delete these.

There is also an asset file generated (in the assets folder): `XR/Settings/AuthBuildSettings.asset`. This contains the auth tokens that are used at runtime (it should normally be empty of tokens, outside of play-mode or building for-device).

**Additional scripting symbols**

`NIANTIC_ARDK_AUTH_DEBUG` can also be set. It provides additional logging and a more verbose settings page.

## The Enterprise Auth Sample<a href="#the-enterprise-auth-sample" class="hash-link" aria-label="Direct link to The Enterprise Auth Sample" title="Direct link to The Enterprise Auth Sample">​</a>

This sample demonstrates how to use the new authentication system in an enterprise environment. It is a Unity project that connects to a sample backend server that handles authentication. There is a separate authentication flow that handles login via a web frontend, which is then redirected to the client so that the client can run a sample user session. This user session requests a Niantic Spatial access token from the backend server, and this access token can then be used to authenticate with any Spatial API endpoint.

## Running the sample project via the Enterprise Auth Flow<a href="#running-the-sample-project-via-the-enterprise-auth-flow" class="hash-link" aria-label="Direct link to Running the sample project via the Enterprise Auth Flow" title="Direct link to Running the sample project via the Enterprise Auth Flow">​</a>

**1. Install and setup the sample project**

See [Sample Projects](https://www.nianticspatial.com/docs/nsdk/3.17.0/sample_projects/) for installation and setup of the sample project in Unity.

**2. Configure the sample project to enable the Enterprise Auth Flow**

1.  Set the scripting symbol `NIANTIC_ARDK_AUTH_LOGIN` in the Unity project settings. See [Enable the Login Flow](#login-enable) for details.
2.  In the **Lightship Settings**, set 'Use developer authentication' to false (do not login or set an API key):

![Lightship SDK Settings](https://www.nianticspatial.com/docs/assets/images/unity_sdk_dev_auth_disabled-0d30cc8769d47216f48cfbc8123784bf.png)

**3. Build and run the sample project on iOS or Android**

1.  Build the sample project in Unity for iOS or Android.

![Build Sample Project](https://www.nianticspatial.com/docs/assets/images/unity_sdk_build-2b41656af2670c59e1286ec89d5f6915.png)

2.  Install and run the sample project on-device.

**4. Login to the sample project via the Enterprise Auth Flow**

1.  Open the sample project on-device.
2.  Scroll down to 'Login/Authentication' (bottom of the list) and tap to enter:

<img src="https://www.nianticspatial.com/docs/assets/images/unity_sample_home_scroll-df2116001ad4178220ca1dfdf1b6975b.png" width="400" alt="Sample Home Scroll" />

3.  Tap the 'Login' button to begin the login flow.

<img src="https://www.nianticspatial.com/docs/assets/images/unity_sample_login-bd368df433380069b5d803b3dd7b22c2.png" width="400" alt="Sample Login" />

This will open a browser window to a frontend login page. Sign-in with Google SSO.

<img src="https://www.nianticspatial.com/docs/assets/images/unity_sample_web_login-d197399c7fafcd80428cf1551aa7dab9.png" width="400" alt="Sample Web Login" />

4.  After successful login, return to the sample project app

You should now be able to run any of the samples that depend on Spatial API endpoints. Any errors will show up in the log window on the 'Login/Authentication' page.

</div>

</div>
