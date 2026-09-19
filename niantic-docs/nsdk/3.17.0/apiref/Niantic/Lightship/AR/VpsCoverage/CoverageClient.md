---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/CoverageClient/
title: class CoverageClient
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class CoverageClient

</div>

(Niantic.Lightship.AR.VpsCoverage.CoverageClient)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Client to request CoverageAreas and LocalizationTargets.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class CoverageClient {
    public:
       // methods
   
     CoverageClient(LightshipSettings lightshipSettings);
        CoverageClient();
  
     async void TryGetCoverageAreas(
           LatLng queryLocation,
           int queryRadius,
          Action<CoverageAreasResult> onAreasReceived
       );
    
     async void TryGetLocalizationTargets(
         string[] targetIdentifiers,
           Action<LocalizationTargetsResult> onTargetsReceived
       );
    
     async void TryGetCoverage(
            LatLng queryLocation,
           int queryRadius,
          Action<AreaTargetsResult> onLocationsReceived,
          LocalizationTarget[] privateScanLocalizationTargets = null
       );
    
     async Task<Texture> TryGetImageFromUrl(string imageUrl);
 
     async void TryGetImageFromUrl(
            string imageUrl,
          Action<Texture> onImageDownloaded
     );
    
     async Task<Texture> TryGetImageFromUrl(string imageUrl, int width, int height);
    
     async void TryGetImageFromUrl(
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

Client to request CoverageAreas and LocalizationTargets.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### TryGetCoverageAreas<a href="#TryGetCoverageAreas" class="hash-link" aria-label="Direct link to TryGetCoverageAreas" title="Direct link to TryGetCoverageAreas">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
async void TryGetCoverageAreas(
       LatLng queryLocation,
       int queryRadius,
      Action<CoverageAreasResult> onAreasReceived
   )
```

</div>

</div>

Request CoverageAreas at device location within a radius using the callback pattern.

    **Parameters**:

    `queryLocation` - Center of query

    `queryRadius` - Radius for query between 0m and 2000m. A negative radius will default to the maximum radius of 2000m.

    `onAreasReceived` - Callback invoked when the requested CoverageAreas are ready.

#### TryGetLocalizationTargets<a href="#TryGetLocalizationTargets" class="hash-link" aria-label="Direct link to TryGetLocalizationTargets" title="Direct link to TryGetLocalizationTargets">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
async void TryGetLocalizationTargets(
     string[] targetIdentifiers,
       Action<LocalizationTargetsResult> onTargetsReceived
   )
```

</div>

</div>

Request LocalizationTargets for a set of identifiers using the callback pattern.

    **Parameters**:

    `targetIdentifiers` - Set of unique identifiers of the requested targets.

    `onTargetsReceived` - Callback invoked when the requested LocalizationTargets are ready.

#### TryGetCoverage<a href="#TryGetCoverage" class="hash-link" aria-label="Direct link to TryGetCoverage" title="Direct link to TryGetCoverage">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
async void TryGetCoverage(
        LatLng queryLocation,
       int queryRadius,
      Action<AreaTargetsResult> onLocationsReceived,
      LocalizationTarget[] privateScanLocalizationTargets = null
   )
```

</div>

</div>

Request coupled CoverageAreas and LocalizationTargets within a radius, using the callback pattern.

    **Parameters**:

    `queryLocation` - Center of query

    `queryRadius` - Radius for query between 0m and 2000m. A negative radius will default to the maximum radius of 2000m.

    `onLocationsReceived` - Callback invoked when the requested CoverageAreas and LocalizationTargets are ready.

    `privateScanLocalizationTargets` - Optional. For any [LocalizationTarget](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/LocalizationTarget/) included in this array, a corresponding [AreaTarget](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/AreaTarget/) will be added to the AreaTargets returned through the onLocationsReceived callback. Specify your private [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) Locations via the [CoverageClientManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/CoverageClientManager/) in order to utilize this parameter.

#### TryGetImageFromUrl<a href="#TryGetImageFromUrl" class="hash-link" aria-label="Direct link to TryGetImageFromUrl" title="Direct link to TryGetImageFromUrl">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
async Task<Texture> TryGetImageFromUrl(string imageUrl)
```

</div>

</div>

Downloads the image from the provided url as a texture, using the async await pattern.

    **Parameters**:

    `imageUrl` - URL of the localization target's hint image

#### TryGetImageFromUrl<a href="#TryGetImageFromUrl" class="hash-link" aria-label="Direct link to TryGetImageFromUrl" title="Direct link to TryGetImageFromUrl">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
async void TryGetImageFromUrl(
        string imageUrl,
      Action<Texture> onImageDownloaded
 )
```

</div>

</div>

Downloads the image from the provided url as a texture, using the callback pattern.

    **Parameters**:

    `imageUrl` -

    `onImageDownloaded` - Callback for downloaded image as texture. When download fails, texture is returned as null.

#### TryGetImageFromUrl<a href="#TryGetImageFromUrl" class="hash-link" aria-label="Direct link to TryGetImageFromUrl" title="Direct link to TryGetImageFromUrl">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
async Task<Texture> TryGetImageFromUrl(string imageUrl, int width, int height)
```

</div>

</div>

Downloads the image from the provided url as a texture cropped to a fixed size, using the async await pattern. The source image is first resampled so the image is fitting for the limiting dimension, then it gets cropped to the fixed size.

    **Parameters**:

    `imageUrl` - URL of the localization target's hint image

    `width` - Fixed width of cropped image

    `height` - Fixed height of cropped image

#### TryGetImageFromUrl<a href="#TryGetImageFromUrl" class="hash-link" aria-label="Direct link to TryGetImageFromUrl" title="Direct link to TryGetImageFromUrl">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
async void TryGetImageFromUrl(
        string imageUrl,
      int width,
        int height,
       Action<Texture> onImageDownloaded
 )
```

</div>

</div>

Downloads the image from the provided url as a texture cropped to a fixed size, using the callback pattern. The source image is first resampled so the image is fitting for the limiting dimension, then it gets cropped to the fixed size.

    **Parameters**:

    `imageUrl` - URL of the localization target's hint image

    `width` - Fixed width of cropped image

    `height` - Fixed height Fixed height of cropped image

    `onImageDownloaded` - Callback for downloaded image as texture. When download fails texture is returned as null.

</div>

</div>
