---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/ArdkSitesSession/
title: ArdkSitesSession
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `ArdkSitesSession`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public final class ArdkSitesSession: ArdkSession.IDisposable
```

</div>

</div>

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `requestOrganizationsForUser(userId:pollingInterval:timeout:)`<a href="#requestorganizationsforuseruseridpollingintervaltimeout" class="hash-link" aria-label="Direct link to requestorganizationsforuseruseridpollingintervaltimeout" title="Direct link to requestorganizationsforuseruseridpollingintervaltimeout">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func requestOrganizationsForUser(
    userId: String,
    pollingInterval: TimeInterval = 0.5,
    timeout: TimeInterval = 60.0
) async throws -> OrganizationResult
```

</div>

</div>

Requests organizations for a user and waits for the result.

This is an async wrapper that combines request initiation and polling. It automatically handles polling until the request completes or times out.

- Parameters:
  - userId: The user ID to fetch organizations for.
  - pollingInterval: The interval between status checks (default: 0.5 seconds).
  - timeout: Maximum time to wait for completion (default: 60 seconds).
- Returns: An `OrganizationResult` containing the organizations.
- Throws:
  - `CancellationError` if the Task running this function was cancelled.
  - `TimeoutError` if the function timed out before it could complete execution.
  - `SitesResult.Error` if there was an error specific to the network query.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| userId | The user ID to fetch organizations for. |
| pollingInterval | The interval between status checks (default: 0.5 seconds). |
| timeout | Maximum time to wait for completion (default: 60 seconds). |

### `requestSitesForOrganization(orgId:pollingInterval:timeout:)`<a href="#requestsitesfororganizationorgidpollingintervaltimeout" class="hash-link" aria-label="Direct link to requestsitesfororganizationorgidpollingintervaltimeout" title="Direct link to requestsitesfororganizationorgidpollingintervaltimeout">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func requestSitesForOrganization(
    orgId: String,
    pollingInterval: TimeInterval = 0.5,
    timeout: TimeInterval = 60.0
) async throws -> SiteResult
```

</div>

</div>

Requests sites for an organization and waits for the result.

- Parameters:
  - orgId: The organization ID to fetch sites for.
  - pollingInterval: The interval between status checks (default: 0.5 seconds).
  - timeout: Maximum time to wait for completion (default: 60 seconds).
- Returns: A `SiteResult` containing the sites.
- Throws:
  - `CancellationError` if the Task running this function was cancelled.
  - `TimeoutError` if the function timed out before it could complete execution.
  - `SitesResult.Error` if there was an error specific to the network query.

#### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| orgId | The organization ID to fetch sites for. |
| pollingInterval | The interval between status checks (default: 0.5 seconds). |
| timeout | Maximum time to wait for completion (default: 60 seconds). |

### `requestAssetsForSite(siteId:pollingInterval:timeout:)`<a href="#requestassetsforsitesiteidpollingintervaltimeout" class="hash-link" aria-label="Direct link to requestassetsforsitesiteidpollingintervaltimeout" title="Direct link to requestassetsforsitesiteidpollingintervaltimeout">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func requestAssetsForSite(
    siteId: String,
    pollingInterval: TimeInterval = 0.5,
    timeout: TimeInterval = 60.0
) async throws -> AssetResult
```

</div>

</div>

Requests assets for a site and waits for the result.

- Parameters:
  - siteId: The site ID to fetch assets for.
  - pollingInterval: The interval between status checks (default: 0.5 seconds).
  - timeout: Maximum time to wait for completion (default: 60 seconds).
- Returns: An `AssetResult` containing the assets.
- Throws:
  - `CancellationError` if the Task running this function was cancelled.
  - `TimeoutError` if the function timed out before it could complete execution.
  - `SitesResult.Error` if there was an error specific to the network query.

#### Parameters<a href="#parameters-2" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| siteId | The site ID to fetch assets for. |
| pollingInterval | The interval between status checks (default: 0.5 seconds). |
| timeout | Maximum time to wait for completion (default: 60 seconds). |

### `requestOrganizationInfo(orgId:pollingInterval:timeout:)`<a href="#requestorganizationinfoorgidpollingintervaltimeout" class="hash-link" aria-label="Direct link to requestorganizationinfoorgidpollingintervaltimeout" title="Direct link to requestorganizationinfoorgidpollingintervaltimeout">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func requestOrganizationInfo(
    orgId: String,
    pollingInterval: TimeInterval = 0.5,
    timeout: TimeInterval = 60.0
) async throws -> OrganizationResult
```

</div>

</div>

Requests organization info and waits for the result.

- Parameters:
  - orgId: The organization ID to fetch info for.
  - pollingInterval: The interval between status checks (default: 0.5 seconds).
  - timeout: Maximum time to wait for completion (default: 60 seconds).
- Returns: An `OrganizationResult` containing the organization info.
- Throws:
  - `CancellationError` if the Task running this function was cancelled.
  - `TimeoutError` if the function timed out before it could complete execution.
  - `SitesResult.Error` if there was an error specific to the network query.

#### Parameters<a href="#parameters-3" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| orgId | The organization ID to fetch info for. |
| pollingInterval | The interval between status checks (default: 0.5 seconds). |
| timeout | Maximum time to wait for completion (default: 60 seconds). |

### `requestSiteInfo(siteId:pollingInterval:timeout:)`<a href="#requestsiteinfositeidpollingintervaltimeout" class="hash-link" aria-label="Direct link to requestsiteinfositeidpollingintervaltimeout" title="Direct link to requestsiteinfositeidpollingintervaltimeout">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func requestSiteInfo(
    siteId: String,
    pollingInterval: TimeInterval = 0.5,
    timeout: TimeInterval = 60.0
) async throws -> SiteResult
```

</div>

</div>

Requests site info and waits for the result.

- Parameters:
  - siteId: The site ID to fetch info for.
  - pollingInterval: The interval between status checks (default: 0.5 seconds).
  - timeout: Maximum time to wait for completion (default: 60 seconds).
- Returns: A `SiteResult` containing the site info.
- Throws:
  - `CancellationError` if the Task running this function was cancelled.
  - `TimeoutError` if the function timed out before it could complete execution.
  - `SitesResult.Error` if there was an error specific to the network query.

#### Parameters<a href="#parameters-4" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| siteId | The site ID to fetch info for. |
| pollingInterval | The interval between status checks (default: 0.5 seconds). |
| timeout | Maximum time to wait for completion (default: 60 seconds). |

### `requestAssetInfo(assetId:pollingInterval:timeout:)`<a href="#requestassetinfoassetidpollingintervaltimeout" class="hash-link" aria-label="Direct link to requestassetinfoassetidpollingintervaltimeout" title="Direct link to requestassetinfoassetidpollingintervaltimeout">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func requestAssetInfo(
    assetId: String,
    pollingInterval: TimeInterval = 0.5,
    timeout: TimeInterval = 60.0
) async throws -> AssetResult
```

</div>

</div>

Requests asset info and waits for the result.

- Parameters:
  - assetId: The asset ID to fetch info for.
  - pollingInterval: The interval between status checks (default: 0.5 seconds).
  - timeout: Maximum time to wait for completion (default: 60 seconds).
- Returns: An `AssetResult` containing the asset info.
- Throws:
  - `CancellationError` if the Task running this function was cancelled.
  - `TimeoutError` if the function timed out before it could complete execution.
  - `SitesResult.Error` if there was an error specific to the network query.

#### Parameters<a href="#parameters-5" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| assetId | The asset ID to fetch info for. |
| pollingInterval | The interval between status checks (default: 0.5 seconds). |
| timeout | Maximum time to wait for completion (default: 60 seconds). |

### `requestUserInfo(userId:pollingInterval:timeout:)`<a href="#requestuserinfouseridpollingintervaltimeout" class="hash-link" aria-label="Direct link to requestuserinfouseridpollingintervaltimeout" title="Direct link to requestuserinfouseridpollingintervaltimeout">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func requestUserInfo(
    userId: String,
    pollingInterval: TimeInterval = 0.5,
    timeout: TimeInterval = 60.0
) async throws -> UserResult
```

</div>

</div>

Requests user info and waits for the result.

- Parameters:
  - userId: The user ID to fetch info for.
  - pollingInterval: The interval between status checks (default: 0.5 seconds).
  - timeout: Maximum time to wait for completion (default: 60 seconds).
- Returns: A `UserResult` containing the user info.
- Throws:
  - `CancellationError` if the Task running this function was cancelled.
  - `TimeoutError` if the function timed out before it could complete execution.
  - `SitesResult.Error` if there was an error specific to the network query.

#### Parameters<a href="#parameters-6" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| userId | The user ID to fetch info for. |
| pollingInterval | The interval between status checks (default: 0.5 seconds). |
| timeout | Maximum time to wait for completion (default: 60 seconds). |

### `requestSelfUserInfo(pollingInterval:timeout:)`<a href="#requestselfuserinfopollingintervaltimeout" class="hash-link" aria-label="Direct link to requestselfuserinfopollingintervaltimeout" title="Direct link to requestselfuserinfopollingintervaltimeout">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func requestSelfUserInfo(
    pollingInterval: TimeInterval = 0.5,
    timeout: TimeInterval = 60.0
) async throws -> UserResult
```

</div>

</div>

Requests self user info and waits for the result.

Uses the user ID from the authenticated session's metadata.

- Parameters:
  - pollingInterval: The interval between status checks (default: 0.5 seconds).
  - timeout: Maximum time to wait for completion (default: 60 seconds).
- Returns: A `UserResult` containing the user info.
- Throws:
  - `CancellationError` if the Task running this function was cancelled.
  - `TimeoutError` if the function timed out before it could complete execution.
  - `SitesResult.Error` if there was an error specific to the network query.
  - `ArdkError.invalidOperation` if no access token was available.

#### Parameters<a href="#parameters-7" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| pollingInterval | The interval between status checks (default: 0.5 seconds). |
| timeout | Maximum time to wait for completion (default: 60 seconds). |

</div>

</div>
