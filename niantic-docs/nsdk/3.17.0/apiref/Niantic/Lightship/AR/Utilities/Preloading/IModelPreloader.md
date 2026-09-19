---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/IModelPreloader/
title: class IModelPreloader
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class IModelPreloader

</div>

(Niantic.Lightship.AR.Utilities.Preloading.IModelPreloader)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Interface for the [ARDK](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/ARDK/) class that pre-downloads necessary neural network model files for awareness features. If the files are not preloaded, they will take time to download when an [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) session configured to use those features is run.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class IModelPreloader: IDisposable {
    public:
       // methods
   
     virtual abstract PreloaderStatusCode DownloadModel(DepthMode depthMode) = 0;
     virtual abstract PreloaderStatusCode DownloadModel(SemanticsMode semanticsMode) = 0;
     virtual abstract PreloaderStatusCode DownloadModel(ScanningSQCMode scanningSQCMode) = 0;
     virtual abstract PreloaderStatusCode DownloadModel(ObjectDetectionMode objectDetectionMode) = 0;
 
     virtual abstract PreloaderStatusCode RegisterModel(
           DepthMode depthMode,
            string filepath
     ) = 0;
    
     virtual abstract PreloaderStatusCode RegisterModel(
           SemanticsMode semanticsMode,
            string filepath
     ) = 0;
    
     virtual abstract PreloaderStatusCode RegisterModel(
           ScanningSQCMode scanningSQCMode,
            string filepath
     ) = 0;
    
     virtual abstract PreloaderStatusCode RegisterModel(
           ObjectDetectionMode objectDetectionMode,
            string filepath
     ) = 0;
    
     virtual abstract PreloaderStatusCode CurrentProgress(
         DepthMode depthMode,
            out float progress
        ) = 0;
    
     virtual abstract PreloaderStatusCode CurrentProgress(
         SemanticsMode semanticsMode,
            out float progress
        ) = 0;
    
     virtual abstract PreloaderStatusCode CurrentProgress(
         ScanningSQCMode scanningSQCMode,
            out float progress
        ) = 0;
    
     virtual abstract PreloaderStatusCode CurrentProgress(
         ObjectDetectionMode objectDetectionMode,
            out float progress
        ) = 0;
    
     virtual abstract bool ExistsInCache(DepthMode depthMode) = 0;
      virtual abstract bool ExistsInCache(SemanticsMode semanticsMode) = 0;
      virtual abstract bool ExistsInCache(ScanningSQCMode scanningSQCMode) = 0;
      virtual abstract bool ExistsInCache(ObjectDetectionMode objectDetectionMode) = 0;
      virtual abstract bool ClearFromCache(DepthMode depthMode) = 0;
     virtual abstract bool ClearFromCache(SemanticsMode semanticsMode) = 0;
     virtual abstract bool ClearFromCache(ScanningSQCMode scanningSQCMode) = 0;
     virtual abstract bool ClearFromCache(ObjectDetectionMode objectDetectionMode) = 0;
     virtual abstract void Dispose() = 0;
  };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Interface for the [ARDK](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/ARDK/) class that pre-downloads necessary neural network model files for awareness features. If the files are not preloaded, they will take time to download when an [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) session configured to use those features is run.

Each awareness feature has one or more modes on a performance-to-quality curve, and each mode corresponds to a different model file. See Feature in [Niantic.Lightship.AR.Utilities.Preloading](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/).

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### DownloadModel<a href="#DownloadModel" class="hash-link" aria-label="Direct link to DownloadModel" title="Direct link to DownloadModel">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract PreloaderStatusCode DownloadModel(DepthMode depthMode) = 0
```

</div>

</div>

Begins downloading the requested model file to the cache if not already present. The request status can be polled with [CurrentProgress(DepthMode, out float)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/IModelPreloader/#CurrentProgress) or [ExistsInCache(DepthMode)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/IModelPreloader/#ExistsInCache).

    **Returns:**

    Returns a [PreloaderStatusCode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/PreloaderStatusCode/) indicating the initial status of the request. The final result of the request may be deferred due to asynchronous network operations, so if this request returns PreloaderStatusCode.Success or PreloaderStatusCode.RequestInProgress, the user should continue to query [CurrentProgress(DepthMode, out float)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/IModelPreloader/#CurrentProgress) every frame to confirm that the network request completes successfully.

#### DownloadModel<a href="#DownloadModel" class="hash-link" aria-label="Direct link to DownloadModel" title="Direct link to DownloadModel">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract PreloaderStatusCode DownloadModel(SemanticsMode semanticsMode) = 0
```

</div>

</div>

Begins downloading the requested model file to the cache if not already present. The request status can be polled with [CurrentProgress(SemanticsMode, out float)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/IModelPreloader/#CurrentProgress) or [ExistsInCache(SemanticsMode)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/IModelPreloader/#ExistsInCache).

    **Returns:**

    Returns a [PreloaderStatusCode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/PreloaderStatusCode/) indicating the initial status of the request. The final result of the request may be deferred due to asynchronous network operations, so if this request returns PreloaderStatusCode.Success or PreloaderStatusCode.RequestInProgress, the user should continue to query [CurrentProgress(SemanticsMode, out float)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/IModelPreloader/#CurrentProgress) every frame to confirm that the network request completes successfully.

#### DownloadModel<a href="#DownloadModel" class="hash-link" aria-label="Direct link to DownloadModel" title="Direct link to DownloadModel">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract PreloaderStatusCode DownloadModel(ScanningSQCMode scanningSQCMode) = 0
```

</div>

</div>

Begins downloading the requested model file to the cache if not already present. The request status can be polled with [CurrentProgress(ScanningSQCMode, out float)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/IModelPreloader/#CurrentProgress) or [ExistsInCache(ScanningSQCMode)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/IModelPreloader/#ExistsInCache).

    **Returns:**

    Returns a [PreloaderStatusCode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/PreloaderStatusCode/) indicating the initial status of the request. The final result of the request may be deferred due to asynchronous network operations, so if this request returns PreloaderStatusCode.Success or PreloaderStatusCode.RequestInProgress, the user should continue to query [CurrentProgress(ScanningSQCMode, out float)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/IModelPreloader/#CurrentProgress) every frame to confirm that the network request completes successfully.

#### DownloadModel<a href="#DownloadModel" class="hash-link" aria-label="Direct link to DownloadModel" title="Direct link to DownloadModel">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract PreloaderStatusCode DownloadModel(ObjectDetectionMode objectDetectionMode) = 0
```

</div>

</div>

Begins downloading the requested model file to the cache if not already present. The request status can be polled with [CurrentProgress(ObjectDetectionMode, out float)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/IModelPreloader/#CurrentProgress) or [ExistsInCache(ObjectDetectionMode)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/IModelPreloader/#ExistsInCache).

    **Returns:**

    Returns a [PreloaderStatusCode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/PreloaderStatusCode/) indicating the initial status of the request. The final result of the request may be deferred due to asynchronous network operations, so if this request returns PreloaderStatusCode.Success or PreloaderStatusCode.RequestInProgress, the user should continue to query [CurrentProgress(ObjectDetectionMode, out float)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/IModelPreloader/#CurrentProgress) every frame to confirm that the network request completes successfully.

#### RegisterModel<a href="#RegisterModel" class="hash-link" aria-label="Direct link to RegisterModel" title="Direct link to RegisterModel">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract PreloaderStatusCode RegisterModel(
       DepthMode depthMode,
        string filepath
 ) = 0
```

</div>

</div>

Register a local neural network model file for a specific feature. This overrides Lightship's URI for the specified feature mode and remains in effect until Lightship is deinitialized. The file must be in a location accessible by the application and remain in place for the duration of the [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) session.

    **Returns:**

    Returns a [PreloaderStatusCode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/PreloaderStatusCode/) indicating the result of the request.

#### RegisterModel<a href="#RegisterModel" class="hash-link" aria-label="Direct link to RegisterModel" title="Direct link to RegisterModel">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract PreloaderStatusCode RegisterModel(
       SemanticsMode semanticsMode,
        string filepath
 ) = 0
```

</div>

</div>

Register a local neural network model file for a specific feature. This overrides Lightship's URI for the specified feature mode and remains in effect until Lightship is deinitialized. The file must be in a location accessible by the application and remain in place for the duration of the [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) session.

    **Returns:**

    Returns a [PreloaderStatusCode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/PreloaderStatusCode/) indicating the result of the request.

#### RegisterModel<a href="#RegisterModel" class="hash-link" aria-label="Direct link to RegisterModel" title="Direct link to RegisterModel">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract PreloaderStatusCode RegisterModel(
       ScanningSQCMode scanningSQCMode,
        string filepath
 ) = 0
```

</div>

</div>

Register a local neural network model file for a specific feature. This overrides Lightship's URI for the specified feature mode and remains in effect until Lightship is deinitialized. The file must be in a location accessible by the application and remain in place for the duration of the [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) session.

    **Returns:**

    Returns a [PreloaderStatusCode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/PreloaderStatusCode/) indicating the result of the request.

#### RegisterModel<a href="#RegisterModel" class="hash-link" aria-label="Direct link to RegisterModel" title="Direct link to RegisterModel">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract PreloaderStatusCode RegisterModel(
       ObjectDetectionMode objectDetectionMode,
        string filepath
 ) = 0
```

</div>

</div>

Register a local neural network model file for a specific feature. This overrides Lightship's URI for the specified feature mode and remains in effect until Lightship is deinitialized. The file must be in a location accessible by the application and remain in place for the duration of the [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) session.

    **Returns:**

    Returns a [PreloaderStatusCode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/PreloaderStatusCode/) indicating the result of the request.

#### CurrentProgress<a href="#CurrentProgress" class="hash-link" aria-label="Direct link to CurrentProgress" title="Direct link to CurrentProgress">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract PreloaderStatusCode CurrentProgress(
     DepthMode depthMode,
        out float progress
    ) = 0
```

</div>

</div>

Read the current status of a mode file request, if a request was previously made. The result of DownloadModel is asynchronous, so the caller must poll [CurrentProgress(DepthMode, out float)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/IModelPreloader/#CurrentProgress) for the status of the request to ensure that the HTTP request completed successfully.

    **Parameters**:

    `progress` - A value in the range of \[0.0, 1.0\] representing how much progress has been made downloading the model file of the specified feature mode. A progress of 1.0 means the file is present in the cache. The download progress value is server dependent and may not always support incremental progress updates.

    **Returns:**

    Returns a [PreloaderStatusCode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/PreloaderStatusCode/) indicating the status of the request.

#### CurrentProgress<a href="#CurrentProgress" class="hash-link" aria-label="Direct link to CurrentProgress" title="Direct link to CurrentProgress">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract PreloaderStatusCode CurrentProgress(
     SemanticsMode semanticsMode,
        out float progress
    ) = 0
```

</div>

</div>

Read the current status of a mode file request, if a request was previously made. The result of DownloadModel is asynchronous, so the caller must poll [CurrentProgress(SemanticsMode, out float)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/IModelPreloader/#CurrentProgress) for the status of the request to ensure that the HTTP request completed successfully.

    **Parameters**:

    `progress` - A value in the range of \[0.0, 1.0\] representing how much progress has been made downloading the model file of the specified feature mode. A progress of 1.0 means the file is present in the cache. The download progress value is server dependent and may not always support incremental progress updates.

    **Returns:**

    Returns a PreloaderStatusCode indicating the status of the request.

#### CurrentProgress<a href="#CurrentProgress" class="hash-link" aria-label="Direct link to CurrentProgress" title="Direct link to CurrentProgress">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract PreloaderStatusCode CurrentProgress(
     ScanningSQCMode scanningSQCMode,
        out float progress
    ) = 0
```

</div>

</div>

Read the current status of a mode file request, if a request was previously made. The result of DownloadModel is asynchronous, so the caller must poll [CurrentProgress(ScanningSQCMode, out float)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/IModelPreloader/#CurrentProgress) for the status of the request to ensure that the HTTP request completed successfully.

    **Parameters**:

    `progress` - A value in the range of \[0.0, 1.0\] representing how much progress has been made downloading the model file of the specified feature mode. A progress of 1.0 means the file is present in the cache. The download progress value is server dependent and may not always support incremental progress updates.

    **Returns:**

    Returns a [PreloaderStatusCode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/PreloaderStatusCode/) indicating the status of the request.

#### CurrentProgress<a href="#CurrentProgress" class="hash-link" aria-label="Direct link to CurrentProgress" title="Direct link to CurrentProgress">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract PreloaderStatusCode CurrentProgress(
     ObjectDetectionMode objectDetectionMode,
        out float progress
    ) = 0
```

</div>

</div>

Read the current status of a mode file request, if a request was previously made. The result of DownloadModel is asynchronous, so the caller must poll [CurrentProgress(ObjectDetectionMode, out float)](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/IModelPreloader/#CurrentProgress) for the status of the request to ensure that the HTTP request completed successfully.

    **Parameters**:

    `progress` - A value in the range of \[0.0, 1.0\] representing how much progress has been made downloading the model file of the specified feature mode. A progress of 1.0 means the file is present in the cache. The download progress value is server dependent and may not always support incremental progress updates.

    **Returns:**

    Returns a [PreloaderStatusCode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/PreloaderStatusCode/) indicating the status of the request.

#### ExistsInCache<a href="#ExistsInCache" class="hash-link" aria-label="Direct link to ExistsInCache" title="Direct link to ExistsInCache">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract bool ExistsInCache(DepthMode depthMode) = 0
```

</div>

</div>

Checks if a model associated with the specified [DepthMode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/DepthMode/) is present in the cache.

    **Returns:**

    True if the specified model was found in the application's cache.

#### ExistsInCache<a href="#ExistsInCache" class="hash-link" aria-label="Direct link to ExistsInCache" title="Direct link to ExistsInCache">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract bool ExistsInCache(SemanticsMode semanticsMode) = 0
```

</div>

</div>

Checks if a model associated with the specified [SemanticsMode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/SemanticsMode/) is present in the cache.

    **Returns:**

    True if the specified model was found in the application's cache.

#### ExistsInCache<a href="#ExistsInCache" class="hash-link" aria-label="Direct link to ExistsInCache" title="Direct link to ExistsInCache">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract bool ExistsInCache(ScanningSQCMode scanningSQCMode) = 0
```

</div>

</div>

Checks if a model associated with the specified [ScanningSQCMode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/ScanningSQCMode/) is present in the cache.

    **Returns:**

    True if the specified model was found in the application's cache.

#### ExistsInCache<a href="#ExistsInCache" class="hash-link" aria-label="Direct link to ExistsInCache" title="Direct link to ExistsInCache">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract bool ExistsInCache(ObjectDetectionMode objectDetectionMode) = 0
```

</div>

</div>

Checks if a model associated with the specified [ObjectDetectionMode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/ObjectDetectionMode/) is present in the cache.

    **Returns:**

    True if the specified model was found in the application's cache.

#### ClearFromCache<a href="#ClearFromCache" class="hash-link" aria-label="Direct link to ClearFromCache" title="Direct link to ClearFromCache">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract bool ClearFromCache(DepthMode depthMode) = 0
```

</div>

</div>

Clears this model file from the application's cache. This function will fail if the download is currently in progress or if the file is not present in the cache. Calling this while the specified model is currently being loaded into a Lightship [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) session is invalid and will result in undefined behavior.

    **Returns:**

    True if the specified feature was present in the application's cache and was successfully removed.

#### ClearFromCache<a href="#ClearFromCache" class="hash-link" aria-label="Direct link to ClearFromCache" title="Direct link to ClearFromCache">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract bool ClearFromCache(SemanticsMode semanticsMode) = 0
```

</div>

</div>

Clears this model file from the application's cache. This function will fail if the download is currently in progress or if the file is not present in the cache. Calling this while the specified model is currently being loaded into a Lightship [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) session is invalid and will result in undefined behavior.

    **Returns:**

    True if the specified feature was present in the application's cache and was successfully removed.

#### ClearFromCache<a href="#ClearFromCache" class="hash-link" aria-label="Direct link to ClearFromCache" title="Direct link to ClearFromCache">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract bool ClearFromCache(ScanningSQCMode scanningSQCMode) = 0
```

</div>

</div>

Clears this model file from the application's cache. This function will fail if the download is currently in progress or if the file is not present in the cache. Calling this while the specified model is currently being loaded into a Lightship [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) session is invalid and will result in undefined behavior.

    **Returns:**

    True if the specified feature was present in the application's cache and was successfully removed.

#### ClearFromCache<a href="#ClearFromCache" class="hash-link" aria-label="Direct link to ClearFromCache" title="Direct link to ClearFromCache">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract bool ClearFromCache(ObjectDetectionMode objectDetectionMode) = 0
```

</div>

</div>

Clears this model file from the application's cache. This function will fail if the download is currently in progress or if the file is not present in the cache. Calling this while the specified model is currently being loaded into a Lightship [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) session is invalid and will result in undefined behavior.

    **Returns:**

    True if the specified feature was present in the application's cache and was successfully removed.

#### Dispose<a href="#Dispose" class="hash-link" aria-label="Direct link to Dispose" title="Direct link to Dispose">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual abstract void Dispose() = 0
```

</div>

</div>

Dispose the handle to the native model preloader.

</div>

</div>
