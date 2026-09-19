---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRObjectDetectionSubsystem/
title: class XRObjectDetectionSubsystem
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class XRObjectDetectionSubsystem

</div>

(Niantic.Lightship.AR.XRSubsystems.XRObjectDetectionSubsystem)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Defines an interface for interacting with object detection functionality.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class XRObjectDetectionSubsystem:
      SubsystemWithProvider< XRObjectDetectionSubsystem, XRObjectDetectionSubsystemDescriptor, XRObjectDetectionSubsystem.Provider >,
      ISubsystemWithModelMetadata {
 public:
   
     class Provider;

        // properties
    
     uint TargetFrameRate;
     bool IsMetadataAvailable;
     uint? LatestFrameId;
      bool IsStabilizationEnabled;

      // methods
   
     bool TryGetCategoryNames(out IReadOnlyList<string> names);
     bool TryGetDetectedObjects(out XRDetectedObject[] results);
      XRObjectDetectionSubsystem();
      static bool Register(XRObjectDetectionSubsystemCinfo cinfo);
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Defines an interface for interacting with object detection functionality.

This is an experimental feature. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### TargetFrameRate<a href="#TargetFrameRate" class="hash-link" aria-label="Direct link to TargetFrameRate" title="Direct link to TargetFrameRate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
uint TargetFrameRate
```

</div>

</div>

Specifies the target frame rate for the platform to target running the object detection algorithm at.

The target frame rate.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

    **Parameters**:

    `System.NotSupportedException` - Thrown if frame rate configuration is not supported.

#### IsMetadataAvailable<a href="#IsMetadataAvailable" class="hash-link" aria-label="Direct link to IsMetadataAvailable" title="Direct link to IsMetadataAvailable">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool IsMetadataAvailable
```

</div>

</div>

Is true if metadata has been downloaded and decrypted on the current device. Only if this value is true can the object detection category names or results be acquired.

If metadata is available.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

    **Parameters**:

    `System.NotSupportedException` - Thrown frame rate configuration is not supported.

#### LatestFrameId<a href="#LatestFrameId" class="hash-link" aria-label="Direct link to LatestFrameId" title="Direct link to LatestFrameId">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
uint? LatestFrameId
```

</div>

</div>

Returns the frame id of the most recent object detection output.

The frame id.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

    **Parameters**:

    `System.NotSupportedException` - Thrown if getting frame id is not supported.

#### IsStabilizationEnabled<a href="#IsStabilizationEnabled" class="hash-link" aria-label="Direct link to IsStabilizationEnabled" title="Direct link to IsStabilizationEnabled">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool IsStabilizationEnabled
```

</div>

</div>

When enabled, the object detection algorithm takes into account how many consecutive frames an object as been seen in, and how many frames a previously detected object has been unseen for, when determining which detections to surface. This has the effect of decreasing the possibility of spurious detections, but may also cause an increase in missed detections if framerate is low and the camera view is moving significantly between each frame.

True if stabilization is enabled.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

    **Parameters**:

    `System.NotSupportedException` - Thrown if configuring stabilization is not supported by the implementation.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### TryGetCategoryNames<a href="#TryGetCategoryNames" class="hash-link" aria-label="Direct link to TryGetCategoryNames" title="Direct link to TryGetCategoryNames">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryGetCategoryNames(out IReadOnlyList<string> names)
```

</div>

</div>

Tries to get a list of the object detection category names for the current model.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

    **Parameters**:

    `names` - A list of category names. It will be empty if the method returns false.

    `System.NotSupportedException` - Thrown when reading the category names is not supported by the implementation.

    **Returns:**

    True if category names are available. False if not.

#### TryGetDetectedObjects<a href="#TryGetDetectedObjects" class="hash-link" aria-label="Direct link to TryGetDetectedObjects" title="Direct link to TryGetDetectedObjects">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryGetDetectedObjects(out XRDetectedObject[] results)
```

</div>

</div>

Tries to acquire the latest object detection results from the camera image.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

    **Parameters**:

    `results` - An array of object detection instances.

    `System.NotSupportedException` - Thrown if the implementation does not support getting object detection results.

    **Returns:**

    Whether any object detection instances could be retrieved.

#### XRObjectDetectionSubsystem<a href="#XRObjectDetectionSubsystem" class="hash-link" aria-label="Direct link to XRObjectDetectionSubsystem" title="Direct link to XRObjectDetectionSubsystem">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
XRObjectDetectionSubsystem()
```

</div>

</div>

Construct the subsystem by creating the functionality provider.

#### Register<a href="#Register" class="hash-link" aria-label="Direct link to Register" title="Direct link to Register">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static bool Register(XRObjectDetectionSubsystemCinfo cinfo)
```

</div>

</div>

Register the descriptor for the object detection subsystem implementation.

    **Parameters**:

    `cinfo` - The object detection subsystem implementation construction information.

    **Returns:**

    true if the descriptor was registered. Otherwise, false.

</div>

</div>
