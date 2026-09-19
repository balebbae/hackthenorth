---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/ObjectDetection/ARObjectDetectionManager/
title: class ARObjectDetectionManager
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class ARObjectDetectionManager

</div>

(Niantic.Lightship.AR.ObjectDetection.ARObjectDetectionManager)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The manager for the object detection subsystem.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class ARObjectDetectionManager: SubsystemLifecycleManager< XRObjectDetectionSubsystem, XRObjectDetectionSubsystemDescriptor, XRObjectDetectionSubsystem.Provider > {
    public:
       // fields
    
      bool IsMetadataAvailable => subsystem?.IsMetadataAvailable ?? false;

     // properties
    
     uint??? TargetFrameRate;
      bool??? IsStabilizationEnabled;
       IReadOnlyList<string> CategoryNames;
      Action<ARObjectDetectionModelEventArgs> MetadataInitialized;

        // events
    
     event ObjectDetectionsUpdated();

     // methods
   
     bool TryGetDetectedObjects(out XRDetectedObject[] results);

  protected:
        // methods
   
     override void OnBeforeStart();
      override void OnDisable();
  };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The manager for the object detection subsystem.

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### IsMetadataAvailable<a href="#IsMetadataAvailable" class="hash-link" aria-label="Direct link to IsMetadataAvailable" title="Direct link to IsMetadataAvailable">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool IsMetadataAvailable => subsystem?.IsMetadataAvailable ?? false
```

</div>

</div>

True if the underlying subsystem has finished initialization.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### TargetFrameRate<a href="#TargetFrameRate" class="hash-link" aria-label="Direct link to TargetFrameRate" title="Direct link to TargetFrameRate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
uint??? TargetFrameRate
```

</div>

</div>

Frame rate that the object detection inference will aim to run at.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

#### IsStabilizationEnabled<a href="#IsStabilizationEnabled" class="hash-link" aria-label="Direct link to IsStabilizationEnabled" title="Direct link to IsStabilizationEnabled">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool??? IsStabilizationEnabled
```

</div>

</div>

When enabled, the object detection algorithm takes into account how many consecutive frames an object as been seen in, and how many frames a previously detected object has been unseen for, when determining which detections to surface. This has the effect of decreasing the possibility of spurious detections, but may also cause an increase in missed detections if framerate is low and the camera view is moving significantly between each frame.

True if stabilization is enabled.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

#### CategoryNames<a href="#CategoryNames" class="hash-link" aria-label="Direct link to CategoryNames" title="Direct link to CategoryNames">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
IReadOnlyList<string> CategoryNames
```

</div>

</div>

The names of the object detection categories that the current model is able to detect. Will return an empty list if no metadata is available.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

#### MetadataInitialized<a href="#MetadataInitialized" class="hash-link" aria-label="Direct link to MetadataInitialized" title="Direct link to MetadataInitialized">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Action<ARObjectDetectionModelEventArgs> MetadataInitialized
```

</div>

</div>

An event which fires when the underlying subsystem has finished initializing.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

### Events<a href="#events" class="hash-link" aria-label="Direct link to Events" title="Direct link to Events">​</a>

#### ObjectDetectionsUpdated<a href="#ObjectDetectionsUpdated" class="hash-link" aria-label="Direct link to ObjectDetectionsUpdated" title="Direct link to ObjectDetectionsUpdated">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
event ObjectDetectionsUpdated()
```

</div>

</div>

An event which fires when the underlying subsystem has made the set of detected objects for the latest input camera frame available.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### TryGetDetectedObjects<a href="#TryGetDetectedObjects" class="hash-link" aria-label="Direct link to TryGetDetectedObjects" title="Direct link to TryGetDetectedObjects">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryGetDetectedObjects(out XRDetectedObject[] results)
```

</div>

</div>

Tries to acquire the most recent set of detected objects.

This is an experimental API. Experimental features are subject to breaking changes, not officially supported, and may be deprecated without notice.

    **Parameters**:

    `results` - An array of detected objects.If no objects were detected, this array will be empty.

    **Returns:**

    True if the object detection neural network has produced output.

#### OnBeforeStart<a href="#OnBeforeStart" class="hash-link" aria-label="Direct link to OnBeforeStart" title="Direct link to OnBeforeStart">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override void OnBeforeStart()
```

</div>

</div>

Callback before the subsystem is started (but after it is created).

#### OnDisable<a href="#OnDisable" class="hash-link" aria-label="Direct link to OnDisable" title="Direct link to OnDisable">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override void OnDisable()
```

</div>

</div>

Callback when the manager is being disabled.

</div>

</div>
