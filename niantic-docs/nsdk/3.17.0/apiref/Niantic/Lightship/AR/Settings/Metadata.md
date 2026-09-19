---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Settings/Metadata/
title: class Metadata
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class Metadata

</div>

(Niantic.Lightship.AR.Settings.Metadata)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Contains metadata and properties regarding the current instance of Ardk

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class Metadata {
  public:
       // properties
    
     string Version;

       // methods
   
     static void SetAccessToken(string accessToken);
        static void SetRefreshToken(string refreshToken);
  };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Contains metadata and properties regarding the current instance of Ardk

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### Version<a href="#Version" class="hash-link" aria-label="Direct link to Version" title="Direct link to Version">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
string Version
```

</div>

</div>

Returns the ardk version that you are using

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### SetAccessToken<a href="#SetAccessToken" class="hash-link" aria-label="Direct link to SetAccessToken" title="Direct link to SetAccessToken">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static void SetAccessToken(string accessToken)
```

</div>

</div>

Sets the access token for authentication with Lightship services. This token will be used for API Gateway requests instead of the API key.

    **Parameters**:

    `accessToken` - The access token string for authentication

#### SetRefreshToken<a href="#SetRefreshToken" class="hash-link" aria-label="Direct link to SetRefreshToken" title="Direct link to SetRefreshToken">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static void SetRefreshToken(string refreshToken)
```

</div>

</div>

Sets the refresh token so native can refresh access tokens as needed.

    **Parameters**:

    `refreshToken` - The refresh token string

</div>

</div>
