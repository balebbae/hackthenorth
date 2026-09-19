---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/data_privacy/
title: NSDK Data Privacy
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# NSDK Data Privacy

</div>

Niantic collects a variety of data via ARDK - for example, geospatial data from device cameras to operate VPS, as well as telemetry to improve user experiences.

Some of this data may be considered personal information under privacy laws, as further explained in the <a href="https://www.nianticspatial.com/legal/data-privacy/niantic-spatial-platform-sdk" target="_blank" rel="noopener noreferrer">Niantic Spatial Platform SDK Data Privacy FAQs</a>. Niantic therefore provides developers with the ability to make a request to retrieve and/or delete this data on behalf of an end user (an **“End User Data Management Request”** or “request” for short).

In order to process End User Data Management Requests, you must provide Niantic with certain identifying fields:

**ApplicationId** - this is the Bundle ID/applicationId of your app on the Apple App Store/ Google Play Store.

**UserId** - this is a unique identifier that you **MUST** provide for each player to track their individual usage in AR.

**ClientId** - this is a device identifier for where the app is installed. It is a fallback in case a UserId is not provided.

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>caution

</div>

<div class="admonitionContent_BuS1">

If you do not provide the fields described above, Niantic may be unable to identify your end user, and therefore unable to process your request.

</div>

</div>

## Setting the UserId<a href="#setting-the-userid" class="hash-link" aria-label="Direct link to Setting the UserId" title="Direct link to Setting the UserId">​</a>

The [UserId](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Settings/PrivacyData/#UserId) is the identifier that you use to identify a user. When the app launches, the user's identifier needs to be provided to ARDK using the [Niantic.Lightship.AR.Settings](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Settings/) namespace.

You need to call the [PrivacyData.SetUserId(string userId)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Settings/PrivacyData/#SetUserId) API every time the app launches with the user's identifier. This allows Niantic to map all the usage information about that player by this UserId.

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>caution

</div>

<div class="admonitionContent_BuS1">

Please provide the `UserId` before triggering any call in the `ARSession` class.

- When initializing XR manually, call `SetUserId(string userId);` after initializing the loaders and before calling any API in the `ARSession` class.

If a UserId is not set, a warning will appear in your logs noting this. If you do not provide a UserId, Niantic may not be able to process your request.

</div>

</div>

## Making an End User Data Management Request<a href="#making-an-end-user-data-management-request" class="hash-link" aria-label="Direct link to Making an End User Data Management Request" title="Direct link to Making an End User Data Management Request">​</a>

You can make an End User Data Management Requests via the <a href="https://lightship.dev/account/settings?tab=users" target="_blank" rel="noopener noreferrer">Niantic Spatial Platform SDK data privacy page in your user settings</a>. You can make the following types of request via this page:

- Data retrieval request
- Data deletion request
- Both data retrieval and deletion.

You will need to provide the following information in order to make a request:

- The ApplicationID for the application your end user is making a request for.
- The [UserId](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Settings/PrivacyData/#UserId).

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

If you do not have a [UserId](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Settings/PrivacyData/#UserId), it is possible to make a request using the ClientID (see the [Getting the ClientID](#getting-the-clientid) section below for more information). Niantic does not recommend relying on [ClientIds](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Settings/PrivacyData/#ClientId) for these requests for the reasons outlined below.

</div>

</div>

### Process<a href="#process" class="hash-link" aria-label="Direct link to Process" title="Direct link to Process">​</a>

1.  Navigate to <a href="https://lightship.dev/account/settings?tab=users" target="_blank" rel="noopener noreferrer">https://lightship.dev/account/settings?tab=users</a>
2.  Enter the [UserId](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Settings/PrivacyData/#UserId) OR the [ClientId](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Settings/PrivacyData/#ClientId) - only one of these is required. In case you provide both, we will default to using the UserId.
3.  Enter the `applicationId` in the **App Bundle Id** field.
4.  The project name for the project whose Api Key you have used for that app.
5.  Select the type of request you might want.
6.  Click on the **Request** button.
7.  Once the request is complete, you will be notified via the email registered with your Niantic Spatial Platform account.
8.  If Niantic is unable to process your request, a member of our support team may reach out to you with further information.

## Getting the Application ID<a href="#getting-the-application-id" class="hash-link" aria-label="Direct link to Getting the Application ID" title="Direct link to Getting the Application ID">​</a>

The Application ID is the Bundle ID for your app on the iOS App Store/Google Play Store. You can get this in Unity through the **Player Settings**:

In iOS:

1.  Launch your game in Unity.
2.  Go to **File** \> **Build Settings** \> **iOS** \> **Player Settings** \> **Player** \> **Build Identifier**.
3.  This is the Bundle ID for the Apple App Store.

In Android:

1.  Launch your game in Unity.
2.  Go to **File** \> **Build Settings** \> **Android** \> **Player Settings** \> **Player** \> **Package Name**.
3.  This is the `applicationId` for the Android Play Store.

## Getting the UserId<a href="#getting-the-userid" class="hash-link" aria-label="Direct link to Getting the UserId" title="Direct link to Getting the UserId">​</a>

To get the user's [UserId](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Settings/PrivacyData/#UserId) from the Ardk while the app is running, you can call the [PrivacyData.SetUserId](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Settings/PrivacyData/#SetUserId) API.

## Getting the ClientId<a href="#getting-the-clientid" class="hash-link" aria-label="Direct link to Getting the ClientId" title="Direct link to Getting the ClientId">​</a>

The [ClientId](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Settings/PrivacyData/#ClientId) is an identifier for the device in case a [UserId](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Settings/PrivacyData/#UserId) is missing. You can get this from the [Niantic.Lightship.AR.Settings](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Settings/) namespace.

ARDK creates this identifier when the app runs for the first time and persists through app upgrades.

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

If the app has been uninstalled and reinstalled, the ClientId will change. We do not recommend relying on ClientIDs to perform End User Data Management Requests, only use them as a last resort.

</div>

</div>

If you have forgotten to set a UserID, it is your responsibility to ensure that you are recording all ClientID's generated by your end user through subsequent installs/uninstalls - without this information, Niantic may be unable to process your End User Data Management Request in full.

</div>

</div>
