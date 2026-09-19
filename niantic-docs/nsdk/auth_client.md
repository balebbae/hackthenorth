---
source: https://www.nianticspatial.com/docs/nsdk/auth_client/
title: Sample login reference
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Sample login reference

</div>

The NSDK sample apps include a complete login flow that exchanges a Scaniverse login for an NSDK access token through Niantic's sample backend. This page explains how that flow works, from browser login through token exchange to NSDK authorization.

**The sample login code is a reference implementation**, not an SDK you ship to users. When building a production application, replace the Niantic sample backend with your own backend and identity system. The NSDK only needs the final NSDK access token — how you obtain it is up to you.

Use this page if you are working from the NSDK sample login flow. For development and internal testing without the sample login flow, use [developer tokens](https://www.nianticspatial.com/docs/nsdk/auth_developer_token/). For production deployment, use [backend-issued short-lived access tokens](https://www.nianticspatial.com/docs/nsdk/auth_backend/).

This page covers:

- **[How the sample login works](#how-the-sample-login-works)**: The token exchange flow and file structure.
- **[Callback scheme registration](#register-a-callback-scheme)**: How the sample app is configured to receive the authentication result after login.
- **[The sample login flow](#the-sample-login-flow)**: How the sample app starts login, handles the callback, establishes a session, and exchanges session tokens for NSDK access tokens.
- **[Token usage in the sample app](#use-tokens-in-your-app)**: How the sample app sets, checks, refreshes, and clears NSDK access tokens.

NSDK access tokens are JSON Web Tokens (JWTs) used to authorize requests to Niantic Spatial services.

NSDK access tokens expire after a set period. The sample app verifies the token's validity using the expiration timestamp and requests a new one when the token is missing or expired. In a production app, your backend handles token issuance. The client can still monitor token expiration and request a new token from your backend when needed, but tokens should not be refreshed directly with the Identity Service from the client.

This page focuses on the sample app's client-side token usage. For help choosing an authorization path, see [Authorization](https://www.nianticspatial.com/docs/nsdk/auth_getting_started/). For development and internal testing, see [Generate developer tokens](https://www.nianticspatial.com/docs/nsdk/auth_developer_token/). For production backend token issuance, see [Generate access tokens](https://www.nianticspatial.com/docs/nsdk/auth_backend/).

## How the sample login works<a href="#how-the-sample-login-works" class="hash-link" aria-label="Direct link to How the sample login works" title="Direct link to How the sample login works">​</a>

The sample apps log in through Niantic's sample backend, which handles the Scaniverse login and token exchange on behalf of the client. The flow has three stages:

1.  **Browser login:** The user logs in with a Scaniverse account in a browser. The sample backend returns an NS sample session token to the app via a deep-link callback.
2.  **Token exchange:** The app exchanges the NS sample session token for an NSDK access token through a series of backend calls.
3.  **NSDK authorization:** The app passes the NSDK access token to the NSDK session. The NSDK uses this token to authorize API requests.

Only the NSDK access token is passed to the NSDK. All intermediate sample-flow tokens, including NS sample session tokens and NSDK refresh tokens, are managed entirely in client code and never reach the native SDK.

### Token exchange detail<a href="#token-exchange-detail" class="hash-link" aria-label="Direct link to Token exchange detail" title="Direct link to Token exchange detail">​</a>

The sample apps use the Niantic Spatial Identity Service to exchange intermediate sample-flow tokens for an NSDK access token. This is the same service your production backend would call using a service account. In the sample flow, the exchange works as follows:

| Step | Request | Returns |
|----|----|----|
| 1 | `refresh_user_session_access_token` with NS sample session token | Rotated NS sample session token (Set-Cookie) |
| 2 | `exchange_build_refresh_token` with NS sample session token | NSDK refresh token |
| 3 | `refresh_build_access_token` with NSDK refresh token | NSDK access token |

All requests are `POST` calls to the identity endpoint: `https://spatial-identity.nianticspatial.com/oauth/token`

The sample apps run a background refresh loop that checks token expiration every 10 seconds and re-executes the exchange before the token expires.

<div class="theme-admonition theme-admonition-info admonition_xJq3 alert alert--info">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)</span>info

</div>

<div class="admonitionContent_BuS1">

In a production app, your backend replaces steps 1–3. Your backend logs in the user with your own identity system, requests an NSDK access token using a service account (see [Generate access tokens](https://www.nianticspatial.com/docs/nsdk/auth_backend/)), and returns it to the client. The client then passes the NSDK access token to the NSDK using the same APIs shown in this guide.

</div>

</div>

### File structure<a href="#file-structure" class="hash-link" aria-label="Direct link to File structure" title="Direct link to File structure">​</a>

Each sample app organizes its login flow into a small set of files:

| File | Purpose |
|----|----|
| `LoginManager.cs` | Opens browser login and handles the deep-link callback |
| `NSSampleSessionManager.cs` | Manages the NS sample session token lifecycle, refresh loop, and NSDK access token exchange |
| `AuthRequests.cs` | HTTP request helpers for the three token exchange calls |
| `AuthManager.cs` | UI manager for login/logout |
| `AuthEndpoints.cs` | ScriptableObject configuration for endpoint URLs |
| `AuthRetryHelper.cs` | Retry logic for NSDK operations that require authorization |

These files are located in the sample project's Auth directory:

<div class="language-text codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` text
nsdk-samples-csharp/NsdkSamples/Assets/Samples/Auth/Scripts/
```

</div>

</div>

## Register a callback scheme<a href="#register-a-callback-scheme" class="hash-link" aria-label="Direct link to Register a callback scheme" title="Direct link to Register a callback scheme">​</a>

After login, the authentication flow redirects to a URL using the app's callback scheme. The app must be configured to handle this redirect so it can receive the authentication result.

The redirect URL uses the format:

- `<your-app-scheme>://signin/redirect?refreshToken=...`

The registered callback scheme must match the scheme used by the authentication redirect URL. This is the URL that returns to the app after authentication.

Here is how the sample app registers its callback scheme.

In Unity, the URL scheme is configured to receive the login redirect for either iOS or Android as follows:

**iOS:** The sample project configures its URL scheme through Unity's Project Settings:

1.  **Edit → Project Settings → Player** → **iOS** tab.
2.  Under **Other Settings → Supported URL schemes**, the sample adds an entry with its scheme.

Unity stores the URL scheme in `ProjectSettings/ProjectSettings.asset`. When building for iOS, Unity generates an Xcode project and converts these settings into `Info.plist`. After updating the URL scheme, the iOS project must be rebuilt so Xcode sees the change.

**Android:** The sample project registers its callback scheme in `Assets/Plugins/Android/AndroidManifest.xml` with an intent filter. The scheme value matches the one used in the login code.

<div class="language-xml codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` xml
<intent-filter>
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
    <data android:scheme="nsdk-unity-samples" android:host="signin" />
</intent-filter>
```

</div>

</div>

The following example shows the minimum Android manifest content for this intent filter:

<div class="language-xml codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android" xmlns:tools="http://schemas.android.com/tools">
    <application>
        <activity android:name="com.unity3d.player.UnityPlayerActivity" android:theme="@style/UnityThemeSelector" >
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data android:scheme="nsdk-unity-samples" android:host="signin" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

</div>

</div>

## The sample login flow<a href="#the-sample-login-flow" class="hash-link" aria-label="Direct link to The sample login flow" title="Direct link to The sample login flow">​</a>

This section walks through each stage of the sample login flow:

1.  [Start login](#start-login)
2.  [Handle the login callback](#handle-the-login-callback)
3.  [Establish the sample session](#establish-the-sample-session)
4.  [Exchange session tokens for NSDK access tokens](#exchange-session-tokens-for-nsdk-access-tokens)

### Start login<a href="#start-login" class="hash-link" aria-label="Direct link to Start login" title="Direct link to Start login">​</a>

The sample app initiates the login flow from its UI by calling the login manager. The login manager opens a browser page where the user authenticates with a Scaniverse account. After authentication completes, the browser redirects back to the app with an NS sample session token.

Before starting login, the sample app initializes the endpoints used by the login flow. The login manager reads endpoint URLs from an `AuthEndpoints` ScriptableObject at runtime, so it must be set before calling `LoginManager.LoginRequested()`.

The sample project creates the `AuthEndpoints` asset via **Create → Scriptable Objects → AuthEndpoints** in the Unity Project window, then initializes it with a script:

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
using UnityEngine;

public class AuthEndpointsInitializer : MonoBehaviour
{
    [SerializeField] private AuthEndpoints authEndpoints;

    private void Awake()
    {
        authEndpoints.SetAsSettings();
    }
}
```

</div>

</div>

This script is attached to a `GameObject` in the scene with the `AuthEndpoints` asset assigned in the Inspector.

The sample app starts the login flow by calling `LoginManager.LoginRequested()` in response to user input. Here is the login button handler:

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
using UnityEngine;

public class LoginController : MonoBehaviour
{
    public void OnLoginTapped()
    {
        LoginManager.LoginRequested();
    }
}
```

</div>

</div>

This script is added to a `GameObject` in the scene, and `OnLoginTapped()` is connected to a UI Button in the Inspector.

### Handle the login callback<a href="#handle-the-login-callback" class="hash-link" aria-label="Direct link to Handle the login callback" title="Direct link to Handle the login callback">​</a>

After authentication completes, the app receives the authentication result through a callback URL. This URL contains the NS sample session token required to establish a sample session.

Unity delivers the authentication result through a deep link. When the browser finishes authentication, it redirects to the app using the registered callback scheme.

The sample login flow handles this automatically. `LoginManager.LoginRequested()` sets up the deep link listener and processes the returned URL when the app resumes.

No additional callback-handling code is needed in the sample app.

### Establish the sample session<a href="#establish-the-sample-session" class="hash-link" aria-label="Direct link to Establish the sample session" title="Direct link to Establish the sample session">​</a>

After login completes, the login manager extracts the returned NS sample session token from the callback URL and stores it in `NSSampleSessionManager`.

The following code in `LoginManager.cs` completes the login flow:

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
private static void OnDeepLinkActivated(string url)
{
    Application.deepLinkActivated -= OnDeepLinkActivated;
    IsLoginInProgress = false;

    var sessionToken = GetParamValue("refreshToken", url);
    NSSampleSessionManager.SetNSSampleSession(sessionToken);
    LoginComplete?.Invoke();
}
```

</div>

</div>

After login completes, the app returns to the scene and continues running. The sample session is established automatically.

### Exchange session tokens for NSDK access tokens<a href="#exchange-session-tokens-for-nsdk-access-tokens" class="hash-link" aria-label="Direct link to Exchange session tokens for NSDK access tokens" title="Direct link to Exchange session tokens for NSDK access tokens">​</a>

After the NS sample session token is stored, the session manager exchanges it for an NSDK access token through three sequential HTTP requests (see [Token exchange detail](#token-exchange-detail)) and passes the result to the NSDK session.

The access flow is set up before login starts to enable NSDK features.

The sample login flow stores the NS sample session token after login. `NSSampleSessionManager` then exchanges it for an NSDK access token and sets it on the NSDK automatically.

`NSSampleSessionManager` also runs a background refresh loop that periodically checks token expiration and re-exchanges before the token expires, keeping the NSDK authorized for the duration of the app session.

Once logged in, the app uses the NSDK access token as described in the following sections.

## Use tokens in your app<a href="#use-tokens-in-your-app" class="hash-link" aria-label="Direct link to Use tokens in your app" title="Direct link to Use tokens in your app">​</a>

Whether using the sample login flow or a production backend, the NSDK APIs for managing tokens are the same. This section shows how the sample app:

- Sets NSDK access tokens on the NSDK session.
- Periodically checks if a token has expired or is about to expire.
- Clears tokens on logout.

The sample app sets the NSDK access token when initializing the NSDK session:

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
using NianticSpatial.NSDK.AR.Loader;

NsdkSettingsHelper.ActiveSettings.AccessToken = accessToken
```

</div>

</div>

The sample app checks if the NSDK access token has expired or will expire soon using `AuthClient.GetAccessAuthInfo`, which returns an `AuthInfo` object containing the expiration time in seconds since the Unix epoch:

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
using NianticSpatial.NSDK.AR.Auth;

/// <summary>
/// Returns true if the NSDK access token has expired or is about to expire in under a minute.
/// Uses <see cref="AuthClient.GetAccessAuthInfo"/> to read the NSDK access token's expiration.
/// </summary>
/// <returns>true if access is expired or expires in under 60 seconds; false otherwise.</returns>
public static bool IsAccessExpiredOrExpiringSoon()
{
    var authInfo = AuthClient.GetAccessAuthInfo();
    var currentTimeSeconds = (int)DateTimeOffset.UtcNow.ToUnixTimeSeconds();
    var timeLeft = authInfo.ExpirationTime - currentTimeSeconds;
    return timeLeft < ExpiringSoonThresholdSeconds;
}
```

</div>

</div>

On logout, the sample app clears the NSDK access token to prevent further NSDK access until a new token is obtained:

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
AuthClient.StaticLogout();
```

</div>

</div>

## How this sample relates to production<a href="#how-this-sample-relates-to-production" class="hash-link" aria-label="Direct link to How this sample relates to production" title="Direct link to How this sample relates to production">​</a>

In a production app, your backend issues and manages NSDK access tokens for each logged-in user. See [Generate access tokens](https://www.nianticspatial.com/docs/nsdk/auth_backend/) for server-side setup. The sample login flow demonstrates the client-side pattern a production app would follow. The key differences are:

1.  **Login flow.** Replace the login flow. Use your own login UI and identity system instead of the Scaniverse browser login.
2.  **Token exchange.** Your production backend requests NSDK access tokens from the Niantic Spatial Identity Service using a service account (see [Generate access tokens](https://www.nianticspatial.com/docs/nsdk/auth_backend/)). Different users or organizations can be associated with different service accounts for asset and permission separation. The client receives only the final NSDK access token.
3.  **Refresh pattern.** The sample app's approach of monitoring token expiration on the client and requesting new tokens before they expire applies equally to production — only the token source changes.
4.  **Passing the NSDK access token.** This is identical in both cases — call `setAccessToken` with whatever token your backend provides.

The NSDK uses the final access token the same way, regardless of its source. Tokens from the sample backend, your production backend, and developer tokens issued in Scaniverse web are all passed to the same NSDK APIs.

</div>

</div>
