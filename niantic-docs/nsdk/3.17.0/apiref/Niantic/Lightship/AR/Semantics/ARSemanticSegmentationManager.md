---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Semantics/ARSemanticSegmentationManager/
title: class ARSemanticSegmentationManager
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class ARSemanticSegmentationManager

</div>

(Niantic.Lightship.AR.Semantics.ARSemanticSegmentationManager)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The [ARSemanticSegmentationManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Semantics/ARSemanticSegmentationManager/) controls the XRSemanticsSubsystem and updates the semantics textures on each Update loop. Textures and XRCpuImages are available for confidence maps of individual semantic segmentation channels and a bit array indicating which semantic channels have surpassed the chosen confidence threshold per pixel. For cases where a semantic segmentation texture is overlaid on the screen, utilities are provided to read semantic properties at a given point on the screen.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class ARSemanticSegmentationManager: SubsystemLifecycleManager< XRSemanticsSubsystem, XRSemanticsSubsystemDescriptor, XRSemanticsSubsystem.Provider > {
 public:
   
     struct SemanticsTexture;

       // fields
    
      IReadOnlyList<string> ChannelNames => _readOnlyChannelNames;
        IReadOnlyDictionary<string, int> ChannelIndices => _readOnlyChannelNamesToIndices;

       // properties
    
     uint??? TargetFrameRate;
      bool IsMetadataAvailable;
     Action<ARSemanticSegmentationModelEventArgs> MetadataInitialized;

       // events
    
     event FrameReceived();

       // methods
   
     void Update();
    
     Texture2D GetSemanticChannelTexture(
          string channelName,
           out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams = null
      );
    
     Texture2D GetPackedSemanticsChannelsTexture(
          out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams = null
      );
    
     Texture2D GetSuppressionMaskTexture(
          out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams = null
      );
    
     bool TryAcquireSemanticChannelCpuImage(
         string channel,
           out XRCpuImage cpuImage,
          out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams = null
      );
    
     bool TryAcquirePackedSemanticChannelsCpuImage(
          out XRCpuImage cpuImage,
          out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams = null
      );
    
     bool TryAcquireSuppressionMaskCpuImage(
         out XRCpuImage cpuImage,
          out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams = null
      );
    
     int GetChannelIndex(string channelName);
 
     uint GetSemantics(
          int viewportX,
            int viewportY,
            XRCameraParams? cameraParams = null
      );
    
     List<int> GetChannelIndicesAt(
          int viewportX,
            int viewportY,
            XRCameraParams? cameraParams = null
      );
    
     List<string> GetChannelNamesAt(
         int viewportX,
            int viewportY,
            XRCameraParams? cameraParams = null
      );
    
     bool DoesChannelExistAt(
            int viewportX,
            int viewportY,
            string channelName,
           XRCameraParams? cameraParams = null
      );
    
     bool DoesChannelExistAt(
            int viewportX,
            int viewportY,
            int channelIndex,
         XRCameraParams? cameraParams = null
      );
    
     bool TrySetChannelConfidenceThresholds(Dictionary<string, float> channelConfidenceThresholds);
     bool TryResetChannelConfidenceThresholds();

   protected:
        // methods
   
     override void OnBeforeStart();
      override void OnDisable();
  };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The [ARSemanticSegmentationManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Semantics/ARSemanticSegmentationManager/) controls the XRSemanticsSubsystem and updates the semantics textures on each Update loop. Textures and XRCpuImages are available for confidence maps of individual semantic segmentation channels and a bit array indicating which semantic channels have surpassed the chosen confidence threshold per pixel. For cases where a semantic segmentation texture is overlaid on the screen, utilities are provided to read semantic properties at a given point on the screen.

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### ChannelNames<a href="#ChannelNames" class="hash-link" aria-label="Direct link to ChannelNames" title="Direct link to ChannelNames">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
IReadOnlyList<string> ChannelNames => _readOnlyChannelNames
```

</div>

</div>

The names of the semantic channels that the current model is able to detect.

#### ChannelIndices<a href="#ChannelIndices" class="hash-link" aria-label="Direct link to ChannelIndices" title="Direct link to ChannelIndices">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
IReadOnlyDictionary<string, int> ChannelIndices => _readOnlyChannelNamesToIndices
```

</div>

</div>

The indices of the semantic channels that the current model is able to detect.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### TargetFrameRate<a href="#TargetFrameRate" class="hash-link" aria-label="Direct link to TargetFrameRate" title="Direct link to TargetFrameRate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
uint??? TargetFrameRate
```

</div>

</div>

Frame rate that semantic segmentation inference will aim to run at.

#### IsMetadataAvailable<a href="#IsMetadataAvailable" class="hash-link" aria-label="Direct link to IsMetadataAvailable" title="Direct link to IsMetadataAvailable">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool IsMetadataAvailable
```

</div>

</div>

True if the underlying subsystem has finished initialization.

#### MetadataInitialized<a href="#MetadataInitialized" class="hash-link" aria-label="Direct link to MetadataInitialized" title="Direct link to MetadataInitialized">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Action<ARSemanticSegmentationModelEventArgs> MetadataInitialized
```

</div>

</div>

An event which fires when the underlying subsystem has finished initializing.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

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

#### Update<a href="#Update" class="hash-link" aria-label="Direct link to Update" title="Direct link to Update">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void Update()
```

</div>

</div>

Callback as the manager is being updated.

#### GetSemanticChannelTexture<a href="#GetSemanticChannelTexture" class="hash-link" aria-label="Direct link to GetSemanticChannelTexture" title="Direct link to GetSemanticChannelTexture">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Texture2D GetSemanticChannelTexture(
      string channelName,
       out Matrix4x4 samplerMatrix,
      XRCameraParams? cameraParams = null
  )
```

</div>

</div>

Returns semantic segmentation texture for the specified semantic channel.

    **Parameters**:

    `channelName` - The semantic channel to acquire.

    `samplerMatrix` - A matrix that converts from viewport to image coordinates according to the latest pose.

    `cameraParams` - Params of the viewport to sample with. Defaults to current screen dimensions if null.

    **Returns:**

    The texture for the specified semantic channel, if any. Otherwise, null.

#### GetPackedSemanticsChannelsTexture<a href="#GetPackedSemanticsChannelsTexture" class="hash-link" aria-label="Direct link to GetPackedSemanticsChannelsTexture" title="Direct link to GetPackedSemanticsChannelsTexture">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Texture2D GetPackedSemanticsChannelsTexture(
      out Matrix4x4 samplerMatrix,
      XRCameraParams? cameraParams = null
  )
```

</div>

</div>

Retrieves the texture of semantic data where each pixel can be interpreted as a uint with bits corresponding to different classifications.

    **Parameters**:

    `samplerMatrix` - A matrix that converts from viewport to image coordinates according to the latest pose.

    `cameraParams` - Params of the viewport to sample with. Defaults to current screen dimensions if null.

    **Returns:**

    The packed semantics texture, owned by the manager, if any. Otherwise, null.

#### GetSuppressionMaskTexture<a href="#GetSuppressionMaskTexture" class="hash-link" aria-label="Direct link to GetSuppressionMaskTexture" title="Direct link to GetSuppressionMaskTexture">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Texture2D GetSuppressionMaskTexture(
      out Matrix4x4 samplerMatrix,
      XRCameraParams? cameraParams = null
  )
```

</div>

</div>

Retrieves the suppression mask texture, where each pixel contains a uint which can be used to interpolate between the predicted depth and the far field depth of the scene. This is useful for enabling smooth occlusion suppression.

    **Parameters**:

    `samplerMatrix` - A matrix that converts from viewport to image coordinates according to the latest pose.

    `cameraParams` - Params of the viewport to sample with. Defaults to current screen dimensions if null.

    **Returns:**

    The suppression mask texture, owned by the manager, if any. Otherwise, null.

#### TryAcquireSemanticChannelCpuImage<a href="#TryAcquireSemanticChannelCpuImage" class="hash-link" aria-label="Direct link to TryAcquireSemanticChannelCpuImage" title="Direct link to TryAcquireSemanticChannelCpuImage">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryAcquireSemanticChannelCpuImage(
     string channel,
       out XRCpuImage cpuImage,
      out Matrix4x4 samplerMatrix,
      XRCameraParams? cameraParams = null
  )
```

</div>

</div>

Attempt to acquire the latest semantic segmentation XRCpuImage for the specified semantic class. This provides direct access to the raw pixel data.

The XRCpuImage must be disposed to avoid resource leaks.

    **Parameters**:

    `channel` - The semantic channel to acquire.

    `cpuImage` - If this method returns `true`, an acquired XRCpuImage. The XRCpuImage must be disposed by the caller.

    `samplerMatrix` - A matrix that converts from viewport to image coordinates according to the latest pose.

    `cameraParams` - Params of the viewport to sample with. Defaults to current screen dimensions if null.

    **Returns:**

    True if the CPU image was acquired. Otherwise, false

#### TryAcquirePackedSemanticChannelsCpuImage<a href="#TryAcquirePackedSemanticChannelsCpuImage" class="hash-link" aria-label="Direct link to TryAcquirePackedSemanticChannelsCpuImage" title="Direct link to TryAcquirePackedSemanticChannelsCpuImage">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryAcquirePackedSemanticChannelsCpuImage(
      out XRCpuImage cpuImage,
      out Matrix4x4 samplerMatrix,
      XRCameraParams? cameraParams = null
  )
```

</div>

</div>

Tries to acquire the latest packed semantic channels XRCpuImage. Each element of the XRCpuImage is a bit field indicating which semantic channels have surpassed their respective detection confidence thresholds for that pixel. (See GetChannelIndex)

The utility GetChannelNamesAt can be used for reading semantic channel names at a viewport location.

    **Parameters**:

    `cpuImage` - If this method returns `true`, an acquired XRCpuImage. The CPU image must be disposed by the caller.

    `samplerMatrix` - A matrix that converts from viewport to image coordinates according to the latest pose.

    `cameraParams` - Params of the viewport to sample with. Defaults to current screen dimensions if null.

    **Returns:**

    True if the CPU image was acquired. Otherwise, false

#### TryAcquireSuppressionMaskCpuImage<a href="#TryAcquireSuppressionMaskCpuImage" class="hash-link" aria-label="Direct link to TryAcquireSuppressionMaskCpuImage" title="Direct link to TryAcquireSuppressionMaskCpuImage">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryAcquireSuppressionMaskCpuImage(
     out XRCpuImage cpuImage,
      out Matrix4x4 samplerMatrix,
      XRCameraParams? cameraParams = null
  )
```

</div>

</div>

Tries to acquire the latest suppression mask XRCpuImage. Each element of the XRCpuImage is a uint32 value which can be used to interpolate between instantaneous depth and far field depth.

    **Parameters**:

    `cpuImage` - If this method returns `true`, an acquired XRCpuImage. The CPU image must be disposed by the caller.

    `samplerMatrix` - A matrix that converts from viewport to image coordinates according to the latest pose.

    `cameraParams` - Params of the viewport to sample with. Defaults to current screen dimensions if null.

    **Returns:**

    True if the CPU image was acquired. Otherwise, false

#### GetChannelIndex<a href="#GetChannelIndex" class="hash-link" aria-label="Direct link to GetChannelIndex" title="Direct link to GetChannelIndex">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
int GetChannelIndex(string channelName)
```

</div>

</div>

Get the channel index of a specified semantic class. This corresponds to a bit position in the packed semantics buffer, with index 0 being the most-significant bit.

    **Parameters**:

    `channelName` - The name of the semantic class.

    **Returns:**

    The index of the specified semantic class, or -1 if the channel does not exist.

#### GetSemantics<a href="#GetSemantics" class="hash-link" aria-label="Direct link to GetSemantics" title="Direct link to GetSemantics">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
uint GetSemantics(
      int viewportX,
        int viewportY,
        XRCameraParams? cameraParams = null
  )
```

</div>

</div>

Returns the semantics at the specified pixel on screen.

    **Parameters**:

    `viewportX` - Horizontal coordinate in viewport space.

    `viewportY` - Vertical coordinate in viewport space.

    `cameraParams` - Params of the viewport to sample with. Defaults to current screen dimensions if null.

    **Returns:**

    A 32-bit packed unsigned integer where each bit is a binary indicator for a class, and the most-significant bit corresponds to the channel that is the 0th element of the ChannelNames list.

#### GetChannelIndicesAt<a href="#GetChannelIndicesAt" class="hash-link" aria-label="Direct link to GetChannelIndicesAt" title="Direct link to GetChannelIndicesAt">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
List<int> GetChannelIndicesAt(
      int viewportX,
        int viewportY,
        XRCameraParams? cameraParams = null
  )
```

</div>

</div>

Returns an array of channel indices that are present at the specified pixel onscreen.

This query allocates garbage.

    **Parameters**:

    `viewportX` - Horizontal coordinate in viewport space.

    `viewportY` - Vertical coordinate in viewport space.

    `cameraParams` - Params of the viewport to sample with. Defaults to current screen dimensions if null.

    **Returns:**

    An array of channel indices present for the pixel.

#### GetChannelNamesAt<a href="#GetChannelNamesAt" class="hash-link" aria-label="Direct link to GetChannelNamesAt" title="Direct link to GetChannelNamesAt">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
List<string> GetChannelNamesAt(
     int viewportX,
        int viewportY,
        XRCameraParams? cameraParams = null
  )
```

</div>

</div>

Returns an array of channel names that are present for the specified pixel onscreen.

This query allocates garbage.

    **Parameters**:

    `viewportX` - Horizontal coordinate in viewport space.

    `viewportY` - Vertical coordinate in viewport space.

    `cameraParams` - Params of the viewport to sample with. Defaults to current screen dimensions if null.

    **Returns:**

    An array of channel names present for the pixel.

#### DoesChannelExistAt<a href="#DoesChannelExistAt" class="hash-link" aria-label="Direct link to DoesChannelExistAt" title="Direct link to DoesChannelExistAt">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool DoesChannelExistAt(
        int viewportX,
        int viewportY,
        string channelName,
       XRCameraParams? cameraParams = null
  )
```

</div>

</div>

Check if a semantic class is detected at the specified location in screen space, based on the confidence threshold set for this channel. (See TrySetChannelConfidenceThresholds)

    **Parameters**:

    `viewportX` - Horizontal coordinate in viewport space.

    `viewportY` - Vertical coordinate in viewport space.

    `channelName` - Name of the semantic class to look for.

    `cameraParams` - Params of the viewport to sample with. Defaults to current screen dimensions if null.

    **Returns:**

    True if the semantic class exists at the given coordinates.

#### DoesChannelExistAt<a href="#DoesChannelExistAt" class="hash-link" aria-label="Direct link to DoesChannelExistAt" title="Direct link to DoesChannelExistAt">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool DoesChannelExistAt(
        int viewportX,
        int viewportY,
        int channelIndex,
     XRCameraParams? cameraParams = null
  )
```

</div>

</div>

Check if a semantic class is detected at the specified location in screen space, based on the confidence threshold set for this channel. (See TrySetChannelConfidenceThresholds)

    **Parameters**:

    `viewportX` - Horizontal coordinate in viewport space.

    `viewportY` - Vertical coordinate in viewport space.

    `channelIndex` - Index of the semantic class to look for in the ChannelNames list.

    `cameraParams` - Params of the viewport to sample with. Defaults to current screen dimensions if null.

    **Returns:**

    True if the semantic class exists at the given coordinates.

#### TrySetChannelConfidenceThresholds<a href="#TrySetChannelConfidenceThresholds" class="hash-link" aria-label="Direct link to TrySetChannelConfidenceThresholds" title="Direct link to TrySetChannelConfidenceThresholds">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TrySetChannelConfidenceThresholds(Dictionary<string, float> channelConfidenceThresholds)
```

</div>

</div>

Sets the confidence threshold for including the specified semantic channel in the packed semantic channel buffer.

Each semantic channel will use its default threshold value chosen by the model until a new value is set by this function during the [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) session. Changes to the semantic segmentation thresholds are undone by either restarting the subsystem or by calling [TryResetChannelConfidenceThresholds](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Semantics/ARSemanticSegmentationManager/#TryResetChannelConfidenceThresholds).

    **Parameters**:

    `channelConfidenceThresholds` - A dictionary consisting of keys specifying the name of the semantics channel that is needed and values between 0 and 1, inclusive, that set the threshold above which the platform will include the specified channel in the packed semantics buffer. The key must be a semantic channel name present in the list returned by TryGetChannelNames.

    `System.NotSupportedException` - Thrown when setting confidence thresholds is not supported by the implementation.

    **Returns:**

    True if the thresholds were set. Otherwise, false.

#### TryResetChannelConfidenceThresholds<a href="#TryResetChannelConfidenceThresholds" class="hash-link" aria-label="Direct link to TryResetChannelConfidenceThresholds" title="Direct link to TryResetChannelConfidenceThresholds">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryResetChannelConfidenceThresholds()
```

</div>

</div>

Resets the confidence thresholds for all semantic channels to the default values from the current model.

This reverts any changes made with [TrySetChannelConfidenceThresholds](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Semantics/ARSemanticSegmentationManager/#TrySetChannelConfidenceThresholds).

    **Parameters**:

    `System.NotSupportedException` - Thrown when resetting confidence thresholds is not supported by the implementation.

    **Returns:**

    True if the thresholds were reset. Otherwise, false.

</div>

</div>
