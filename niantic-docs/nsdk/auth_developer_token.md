---
source: https://www.nianticspatial.com/docs/nsdk/auth_developer_token/
title: Generate developer tokens
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Generate developer tokens

</div>

Developer tokens are the simplest way to authorize the Niantic Software Development Kit (<a href="https://www.nianticspatial.com/docs/api/unity/" target="_blank" rel="noopener noreferrer">NSDK</a>) and Niantic Spatial REST APIs. When you generate a developer token in <a href="https://scaniverse.nianticspatial.com/signin" target="_blank" rel="noopener noreferrer">Scaniverse web</a>, include it in your application build or server code, and every API call made with that token inherits the access of the organization that issued it.

Developer tokens are a good fit for internal testing, demos, server-side scripts, and continuous integration (CI). For a public, multi-user deployment, use [production-issued access tokens](https://www.nianticspatial.com/docs/nsdk/auth_backend/) instead.

<div class="theme-admonition theme-admonition-warning admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>warning

</div>

<div class="admonitionContent_BuS1">

Developer tokens are secrets. Anyone who holds a token has the same Niantic Spatial API access as the organization that issued it. Never commit a token to source control, paste it into chat, or bundle it into a public release. If a token is exposed, [revoke it](#revoke-a-developer-token) immediately from <a href="https://scaniverse.nianticspatial.com/signin" target="_blank" rel="noopener noreferrer">Scaniverse web</a>.

</div>

</div>

## How developer tokens work<a href="#how-developer-tokens-work" class="hash-link" aria-label="Direct link to How developer tokens work" title="Direct link to How developer tokens work">​</a>

The developer token workflow has four steps:

1.  [Create a developer token](#create-a-developer-token) in <a href="https://scaniverse.nianticspatial.com/signin" target="_blank" rel="noopener noreferrer">Scaniverse web</a>.
2.  Copy the token and store it securely in the location your app or script will use.
3.  [Use the token](#use-the-token) with NSDK or supported REST API requests.
4.  [Revoke the token](#revoke-a-developer-token) when you no longer need it or if it is exposed.

No backend exchange, client ID, or refresh step is required. The token remains valid until it expires or is revoked.

## Create a developer token<a href="#create-a-developer-token" class="hash-link" aria-label="Direct link to Create a developer token" title="Direct link to Create a developer token">​</a>

Create a developer token to use NSDK features and related services without setting up a production backend as follows:

1.  Sign in to <a href="https://scaniverse.nianticspatial.com" target="_blank" rel="noopener noreferrer">Scaniverse Web</a>.
2.  Select **Credentials** \> **Developer Tokens** from the left navigation pane.
3.  Select **New developer token**.
4.  Enter a unique name under **Developer token name**.
5.  Select an **Expiration date** for when the token will automatically expire. You can choose either 7, 14, 30, 60, or 90 days.
6.  Select one or both scopes:
    - `Scaniverse API` if your application needs to use sites that you created and manage in Scaniverse, including site discovery paths in NSDK.
    - `VPS API` for VPS localization and related NSDK features that rely on VPS/VPS2 services, such as localization, VPS-based positioning, or VPS/VPS2 experiences tied to mapped locations.
7.  Select **Create**.
8.  Copy the raw token into your application configuration or secrets store. Scaniverse only shows the developer token once.

Your application must send the developer token in every API call to Niantic Spatial API using the `Authorization: Bearer` header as shown in the following section.

## Use the token<a href="#use-the-token" class="hash-link" aria-label="Direct link to Use the token" title="Direct link to Use the token">​</a>

You can use a developer token with NSDK or with supported Niantic Spatial REST API requests, depending on your workflow.

### Use the token with NSDK<a href="#use-the-token-with-nsdk" class="hash-link" aria-label="Direct link to Use the token with NSDK" title="Direct link to Use the token with NSDK">​</a>

Provide the developer token to NSDK during initialization as follows:

<div class="language-csharp codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` csharp
using NianticSpatial.NSDK.AR.Loader;

NsdkSettingsHelper.ActiveSettings.AccessToken = "<YOUR_DEVELOPER_TOKEN>";
```

</div>

</div>

You can also store the token inside the Unity project settings as follows:

1.  Open **Edit \> Project Settings**.
2.  In the left navigation bar, expand **XR Plug-in Management**.
3.  Select **Niantic Spatial Development Kit**.
4.  Under **Credentials**, paste the developer token into the **Niantic Spatial Access Token** field.

Replace `YOUR_DEVELOPER_TOKEN` with the value you copied from Scaniverse web. Every NSDK API call made by the build uses this token until it expires or is revoked.

### Use the token in REST API requests<a href="#use-the-token-in-rest-api-requests" class="hash-link" aria-label="Direct link to Use the token in REST API requests" title="Direct link to Use the token in REST API requests">​</a>

You can also use a developer token with Niantic Spatial REST APIs by sending it in the `Authorization` header:

<div class="language-bash codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` bash
curl https://api.nianticspatial.com/web/v1/... \
  -H "Authorization: Bearer <YOUR_DEVELOPER_TOKEN>"
```

</div>

</div>

The same header works for any Niantic Spatial endpoint authorized by the token's scopes. No additional token exchange or refresh step is required.

## Revoke a developer token<a href="#revoke-a-developer-token" class="hash-link" aria-label="Direct link to Revoke a developer token" title="Direct link to Revoke a developer token">​</a>

If a token is exposed, or the environment it was issued for is no longer in use, revoke it immediately:

1.  Open **Credentials** \> **Developer Tokens** from the left navigation bar in <a href="https://scaniverse.nianticspatial.com/signin" target="_blank" rel="noopener noreferrer">Scaniverse web</a>.
2.  Select the three vertical dots next to the token you want to revoke in the list of tokens.
3.  Select **Revoke**.

Revoked tokens are marked inactive immediately. API enforcement typically propagates within a few minutes. After the revocation propagates, any application build or script still using the token receives a `401 Unauthorized` response.

Expired tokens remain visible in the list for reference. They no longer grant access and do not count against the active-token limit.

## Errors and limits<a href="#errors-and-limits" class="hash-link" aria-label="Direct link to Errors and limits" title="Direct link to Errors and limits">​</a>

The following table lists common developer token errors and the limits that apply when you use a token:

| HTTP status | When it happens | What to do |
|----|----|----|
| `401` | The token is missing, malformed, expired, or revoked. | Create a new token in the portal and update your build or script. |
| `403` | The token does not include the scope required by the endpoint. | Create a new token with the correct scope. |
| `429` | The token exceeds 10 requests per second. | Wait before trying again, or use separate tokens or a production backend flow if you need to send more requests. |

Each developer token has its own rate limit. Reaching the limit for one token does not affect other tokens or change your organization's other usage limits.

## Security guidelines<a href="#security-guidelines" class="hash-link" aria-label="Direct link to Security guidelines" title="Direct link to Security guidelines">​</a>

Use the following guidelines when storing, sharing, and rotating developer tokens:

- Scope tokens as narrowly as possible.
- Use shorter lifetimes for riskier environments, external testing, or CI.
- Create separate tokens for different environments and tester groups so you can revoke them independently.
- Rotate tokens when team membership changes or when you suspect a token has been shared too broadly.
- Do not bundle developer tokens into public releases. Use the [production authorization flow](https://www.nianticspatial.com/docs/nsdk/auth_backend/) instead.

## FAQ<a href="#faq" class="hash-link" aria-label="Direct link to FAQ" title="Direct link to FAQ">​</a>

**Can I extend a token's expiration?**\
No. To use a different expiration, create a new token, update your app or environment, and then revoke the old token.

**Can I change a token's scope after creation?**\
No. To use a different scope, create a new token with the scope you need.

**Who in my organization can manage developer tokens?**\
Currently, any organization member can create, view, and revoke developer tokens. This behavior may change in a future release.

**Is the token tied to the person who created it?**\
No. A developer token belongs to the organization, not to an individual user. The creator is recorded for audit purposes, but the token continues to work until it expires or is revoked.

</div>

</div>
