---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/CoverageClientManager/
title: class CoverageClientManager
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class CoverageClientManager

</div>

(Niantic.Lightship.AR.VpsCoverage.CoverageClientManager)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The [CoverageClientManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/CoverageClientManager/) component provides the ability to query VPS coverage area and localization target information within a specified radius from either a device's current location or a specified location. Additionally, private VPS-scans can also be provided to this manager to have them be included in the query result for testing purposes (as private VPS-scans are not currently included in the query response).

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class CoverageClientManager: MonoBehaviour {
    public:
       // properties
    
     bool UseCurrentLocation;
      int QueryRadius;
      float QueryLatitude;
      float QueryLongitude;
     LocalizationTarget[] PrivateARLocalizationTargets;

      // methods
   
     void TryGetCoverage(Action<AreaTargetsResult> onTryGetCoverage);
       Task<Texture> TryGetImageFromUrl(string imageUrl);
     void TryGetImageFromUrl(string imageUrl, Action<Texture> onImageDownloaded);
        Task<Texture> TryGetImageFromUrl(string imageUrl, int width, int height);
    
     void TryGetImageFromUrl(
            string imageUrl,
          int width,
            int height,
           Action<Texture> onImageDownloaded
     );
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The [CoverageClientManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/CoverageClientManager/) component provides the ability to query VPS coverage area and localization target information within a specified radius from either a device's current location or a specified location. Additionally, private VPS-scans can also be provided to this manager to have them be included in the query result for testing purposes (as private VPS-scans are not currently included in the query response).

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### UseCurrentLocation<a href="#UseCurrentLocation" class="hash-link" aria-label="Direct link to UseCurrentLocation" title="Direct link to UseCurrentLocation">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool UseCurrentLocation
```

</div>

</div>

Whether or not to use current location in the query

#### QueryRadius<a href="#QueryRadius" class="hash-link" aria-label="Direct link to QueryRadius" title="Direct link to QueryRadius">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
int QueryRadius
```

</div>

</div>

The radius of the query in meters

#### QueryLatitude<a href="#QueryLatitude" class="hash-link" aria-label="Direct link to QueryLatitude" title="Direct link to QueryLatitude">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float QueryLatitude
```

</div>

</div>

The latitude of the query

#### QueryLongitude<a href="#QueryLongitude" class="hash-link" aria-label="Direct link to QueryLongitude" title="Direct link to QueryLongitude">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float QueryLongitude
```

</div>

</div>

The longitude of the query

#### PrivateARLocalizationTargets<a href="#PrivateARLocalizationTargets" class="hash-link" aria-label="Direct link to PrivateARLocalizationTargets" title="Direct link to PrivateARLocalizationTargets">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
LocalizationTarget[] PrivateARLocalizationTargets
```

</div>

</div>

The localization targets for the private scans

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### TryGetCoverage<a href="#TryGetCoverage" class="hash-link" aria-label="Direct link to TryGetCoverage" title="Direct link to TryGetCoverage">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void TryGetCoverage(Action<AreaTargetsResult> onTryGetCoverage)
```

</div>

</div>

Queries for coverage

    **Parameters**:

    `onTryGetCoverage` - Callback after query completes

#### TryGetImageFromUrl<a href="#TryGetImageFromUrl" class="hash-link" aria-label="Direct link to TryGetImageFromUrl" title="Direct link to TryGetImageFromUrl">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Task<Texture> TryGetImageFromUrl(string imageUrl)
```

</div>

</div>

Tries to get a hint image from the URL

    **Parameters**:

    `imageUrl` - The URL used to get the hint image

    **Returns:**

    The texture with the hint image fetched from the URL

#### TryGetImageFromUrl<a href="#TryGetImageFromUrl" class="hash-link" aria-label="Direct link to TryGetImageFromUrl" title="Direct link to TryGetImageFromUrl">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void TryGetImageFromUrl(string imageUrl, Action<Texture> onImageDownloaded)
```

</div>

</div>

Tries to get a hint image from the URL

    **Parameters**:

    `imageUrl` - The URL used to get the hint image

    `onImageDownloaded` - Callback after the hint image is downloaded

#### TryGetImageFromUrl<a href="#TryGetImageFromUrl" class="hash-link" aria-label="Direct link to TryGetImageFromUrl" title="Direct link to TryGetImageFromUrl">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Task<Texture> TryGetImageFromUrl(string imageUrl, int width, int height)
```

</div>

</div>

Tries to get a hint image from the URL

    **Parameters**:

    `imageUrl` - The URL used to get the hint image

    `width` - The requested width of the hint image

    `height` - The requested height of the hint image

    **Returns:**

    The texture with the hint image

#### TryGetImageFromUrl<a href="#TryGetImageFromUrl" class="hash-link" aria-label="Direct link to TryGetImageFromUrl" title="Direct link to TryGetImageFromUrl">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void TryGetImageFromUrl(
        string imageUrl,
      int width,
        int height,
       Action<Texture> onImageDownloaded
 )
```

</div>

</div>

Tries to get a hint image from the URL

    **Parameters**:

    `imageUrl` - The URL used to get the hint image

    `width` - The requested width of the hint image

    `height` - The requested height of the hint image

    `onImageDownloaded` - Callback when the hint image has been downloaded

</div>

</div>
