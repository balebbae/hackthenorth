---
source: https://www.nianticspatial.com/docs/nsdk/how-to/sites/getting_started/
title: Getting Started with Sites
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Getting Started with Sites

</div>

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The Sites feature provides an API for querying hierarchical data in the Niantic Spatial platform. This guide will help you get started using Sites in your application.

The Sites feature organizes data in a hierarchical structure:

**Organization** → **Site** → **Asset**.

Your application starts at the **Organization** level, which is resolved directly from your access token (see below).

## Requirements<a href="#requirements" class="hash-link" aria-label="Direct link to Requirements" title="Direct link to Requirements">​</a>

The Sites feature requires authentication using Niantic Spatial Auth. Your application must be authenticated before using any Sites API methods.

To authenticate:

1.  Ensure you have access the <a href="https://scaniverse.nianticspatial.com" target="_blank" rel="noopener noreferrer">Niantic Spatial Portal</a> where you can manage your organizations, sites, and assets.
2.  Set up auth in your application by following the [Auth guide](https://www.nianticspatial.com/docs/nsdk/auth_getting_started/)

## Your access token and Organization<a href="#your-access-token-and-organization" class="hash-link" aria-label="Direct link to Your access token and Organization" title="Direct link to Your access token and Organization">​</a>

Your access token is scoped to an Organization. That tells the SDK which Organization's data your app can access. Use `requestSelfOrganizationInfo` to get that Organization's information. For a code example, see [Get your organization](#2-get-your-organization).

## Basic Usage<a href="#basic-usage" class="hash-link" aria-label="Direct link to Basic Usage" title="Direct link to Basic Usage">​</a>

The Sites API follows a simple pattern: Make requests and handle results. All requests are asynchronous and return struct data that represents the Sites entity you are requesting.

### 1. Acquire a Sites Session<a href="#1-acquire-a-sites-session" class="hash-link" aria-label="Direct link to 1. Acquire a Sites Session" title="Direct link to 1. Acquire a Sites Session">​</a>

Add the Sites component to your unity scene's gameobject

<img src="https://www.nianticspatial.com/docs/assets/images/sites_manager_unity_component-8cf701976e9185a0df775e48233e9ad1.png" width="400" alt="Sites Client Manager component in Unity Inspector" />

Then add a reference to the Sites component to your monobehaviour:

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
[SerializeField]
private SitesClientManager _sitesClientManager;
```

</div>

</div>

### 2. Get your organization<a href="#2-get-your-organization" class="hash-link" aria-label="Direct link to 2. Get your organization" title="Direct link to 2. Get your organization">​</a>

Resolve your organization directly from the access token with `requestSelfOrganizationInfo`.

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
var orgResult = await _sitesClientManager.GetSelfOrganizationInfoAsync();
if (orgResult.Status == SitesRequestStatus.Success && orgResult.Organizations.Count > 0) {
    var organization = orgResult.Organizations[0];
    Debug.Log($"Organization: {organization.Name}");
    var orgId = organization.Id;
}
```

</div>

</div>

### 3. Query Sites<a href="#3-query-sites" class="hash-link" aria-label="Direct link to 3. Query Sites" title="Direct link to 3. Query Sites">​</a>

Browse sites within an organization, using the `orgId` from the previous step:

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
var sitesResult = await _sitesClientManager.GetSitesForOrganizationAsync(orgId);
if (sitesResult.Status == SitesRequestStatus.Success) {
    foreach (var site in sitesResult.Sites) {
        Debug.Log($"Site: {site.Name}");
    }
}
```

</div>

</div>

### 4. Query Assets<a href="#4-query-assets" class="hash-link" aria-label="Direct link to 4. Query Assets" title="Direct link to 4. Query Assets">​</a>

Discover spatial assets available at a site:

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
var assetsResult = await _sitesClientManager.GetAssetsForSiteAsync(siteId);
if (assetsResult.Status == SitesRequestStatus.Success) {
    foreach (var asset in assetsResult.Assets) {
        Debug.Log($"Asset: {asset.Name} ({asset.AssetType})");
    }
}
```

</div>

</div>

### 5. Get a Site's VPS anchor payload<a href="#5-get-a-sites-vps-anchor-payload" class="hash-link" aria-label="Direct link to 5. Get a Site&#39;s VPS anchor payload" title="Direct link to 5. Get a Site&#39;s VPS anchor payload">​</a>

To precisely localize to a Site — and place content on its anchor — you need the Site's **anchor payload**. It lives on the Site's **production VPS asset**: find the asset whose type is VPS info and whose deployment is *production*, then read its `anchorPayload`.

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
var assetsResult = await _sitesClientManager.GetAssetsForSiteAsync(siteId);
string anchorPayload = null;
if (assetsResult.Status == SitesRequestStatus.Success) {
    foreach (var asset in assetsResult.Assets) {
        if (asset.AssetType == AssetType.VpsInfo &&
            asset.Deployment == AssetDeploymentType.Production &&
            asset.VpsData.HasValue) {
            anchorPayload = asset.VpsData.Value.AnchorPayload;
            // Pass anchorPayload to VPS2 to start map-relative localization for this Site.
            break;
        }
    }
}
```

</div>

</div>

Fetching the anchor payload alone does not start map-relative localization. To start map-relative localization for a Site, pass the payload to `trackAnchor()`. For an example that passes the payload to `trackAnchor()` and places content on the tracked anchor, see [Place virtual content with VPS2](https://www.nianticspatial.com/docs/nsdk/how-to/vps2/placing_virtual_content/). To learn which status to read while waiting for localization, see [Check device status and anchor status](https://www.nianticspatial.com/docs/nsdk/features/vps2/#check-device-status-and-anchor-status).

## Next Steps<a href="#next-steps" class="hash-link" aria-label="Direct link to Next Steps" title="Direct link to Next Steps">​</a>

- Explore the full [API reference](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Sites.SitesClient/)

</div>

</div>
