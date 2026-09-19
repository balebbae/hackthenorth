---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRObjectDetectionSubsystem/Provider/
title: class Provider
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class Provider

</div>

(Niantic.Lightship.AR.XRSubsystems.XRObjectDetectionSubsystem.Provider)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The provider which will service the [XRObjectDetectionSubsystem](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRObjectDetectionSubsystem/).

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class Provider: SubsystemProvider< XRObjectDetectionSubsystem > {
 public:
       // fields
    
      ? uint LatestFrameId => throw new NotSupportedException("Getting the latest frame id is not supported by this implementation");
      bool IsMetadataAvailable => throw new NotSupportedException("Getting if metadata is available is not supported by this implementation");

      // properties
    
     uint TargetFrameRate;
     bool IsStabilizationEnabled;

      // methods
   
     virtual bool TryGetCategoryNames(out IReadOnlyList<string> names);
       virtual bool TryGetDetectedObjects(out XRDetectedObject[] results);
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The provider which will service the [XRObjectDetectionSubsystem](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRObjectDetectionSubsystem/).

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### LatestFrameId<a href="#LatestFrameId" class="hash-link" aria-label="Direct link to LatestFrameId" title="Direct link to LatestFrameId">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
? uint LatestFrameId => throw new NotSupportedException("Getting the latest frame id is not supported by this implementation")
```

</div>

</div>

Frame id of the most recent object detection output.

The frame id.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

    **Parameters**:

    `System.NotSupportedException` - Thrown if getting frame id is not supported.

#### IsMetadataAvailable<a href="#IsMetadataAvailable" class="hash-link" aria-label="Direct link to IsMetadataAvailable" title="Direct link to IsMetadataAvailable">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool IsMetadataAvailable => throw new NotSupportedException("Getting if metadata is available is not supported by this implementation")
```

</div>

</div>

Is true if metadata has been downloaded and decrypted on the current device. Only if this value is true can the object detection category names or results be acquired.

If metadata is available.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

    **Parameters**:

    `System.NotSupportedException` - Thrown frame rate configuration is not supported.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### TargetFrameRate<a href="#TargetFrameRate" class="hash-link" aria-label="Direct link to TargetFrameRate" title="Direct link to TargetFrameRate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
uint TargetFrameRate
```

</div>

</div>

Property to be implemented by the provider to get or set the frame rate for the platform's object detection feature.

The requested frame rate in frames per second.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

    **Parameters**:

    `System.NotSupportedException` - Thrown when requesting frame rate is not supported by the implementation.

#### IsStabilizationEnabled<a href="#IsStabilizationEnabled" class="hash-link" aria-label="Direct link to IsStabilizationEnabled" title="Direct link to IsStabilizationEnabled">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool IsStabilizationEnabled
```

</div>

</div>

Property to be implemented by the provider to get or set whether filtering is enabled.

True if filtering is enabled.

    **Parameters**:

    `System.NotSupportedException` - Thrown when configuring filtering is not supported by the implementation.

    `NotSupportedException` -

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### TryGetCategoryNames<a href="#TryGetCategoryNames" class="hash-link" aria-label="Direct link to TryGetCategoryNames" title="Direct link to TryGetCategoryNames">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual bool TryGetCategoryNames(out IReadOnlyList<string> names)
```

</div>

</div>

Method to be implemented by the provider to get a list of the object detection category names for the current model.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

    **Parameters**:

    `names` - A list of category labels. It will be empty if the method returns false.

    `System.NotSupportedException` - Thrown when reading the category names is not supported by the implementation.

    **Returns:**

    True if channel names are available. False if not.

#### TryGetDetectedObjects<a href="#TryGetDetectedObjects" class="hash-link" aria-label="Direct link to TryGetDetectedObjects" title="Direct link to TryGetDetectedObjects">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual bool TryGetDetectedObjects(out XRDetectedObject[] results)
```

</div>

</div>

Tries to acquire the latest object detection results from the camera image.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

    **Parameters**:

    `results` - An array of objects detected in the latest input camera image. If no objects were detected, this array will be empty.

    `System.NotSupportedException` - Thrown if the implementation does not support getting detected objects.

    **Returns:**

    True if the object detection neural network has produced output.

</div>

</div>
