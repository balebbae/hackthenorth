---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRSemanticsSubsystem/
title: class XRSemanticsSubsystem
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class XRSemanticsSubsystem

</div>

(Niantic.Lightship.AR.XRSubsystems.XRSemanticsSubsystem)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Defines an interface for interacting with semantic segmentation functionality.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class XRSemanticsSubsystem:
        SubsystemWithProvider< XRSemanticsSubsystem, XRSemanticsSubsystemDescriptor, XRSemanticsSubsystem.Provider >,
        ISubsystemWithModelMetadata {
 public:
   
     class Provider;

        // properties
    
     uint TargetFrameRate;
     HashSet<string> SuppressionMaskChannels;
      uint? LatestFrameId;
      bool IsMetadataAvailable;

     // methods
   
     XRSemanticsSubsystem();
    
     bool TryGetSemanticChannel(
         string channelName,
           out XRTextureDescriptor semanticsChannelDescriptor,
           out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams = null
      );
    
     bool TryAcquireSemanticChannelCpuImage(
         string channelName,
           out XRCpuImage cpuImage,
          out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams = null
      );
    
     bool TryGetPackedSemanticChannels(
          out XRTextureDescriptor packedSemanticsDescriptor,
            out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams = null
      );
    
     bool TryAcquirePackedSemanticChannelsCpuImage(
          out XRCpuImage cpuImage,
          out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams = null
      );
    
     bool TryGetSuppressionMaskTexture(
          out XRTextureDescriptor suppressionMaskDescriptor,
            out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams = null
      );
    
     bool TryAcquireSuppressionMaskCpuImage(
         out XRCpuImage cpuImage,
          out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams = null
      );
    
     bool TryAcquireSuppressionMaskCpuImage(
         out XRCpuImage cpuImage,
          out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams,
           Matrix4x4? targetPose
     );
    
     bool TryGetChannelNames(out IReadOnlyList<string> names);
      bool TrySetChannelConfidenceThresholds(Dictionary<string, float> channelConfidenceThresholds);
     bool TryResetChannelConfidenceThresholds();
       static bool Register(XRSemanticsSubsystemCinfo semanticsSubsystemCinfo);

 protected:
        // methods
   
     override void OnStop();
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Defines an interface for interacting with semantic segmentation functionality.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### TargetFrameRate<a href="#TargetFrameRate" class="hash-link" aria-label="Direct link to TargetFrameRate" title="Direct link to TargetFrameRate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
uint TargetFrameRate
```

</div>

</div>

Specifies the target frame rate for the platform to target running semantic segmentation inference at.

The target frame rate.

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

Returns the frame id of the most recent semantic segmentation prediction.

The frame id.

    **Parameters**:

    `System.NotSupportedException` - Thrown if getting frame id is not supported.

#### IsMetadataAvailable<a href="#IsMetadataAvailable" class="hash-link" aria-label="Direct link to IsMetadataAvailable" title="Direct link to IsMetadataAvailable">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool IsMetadataAvailable
```

</div>

</div>

Is true if metadata has been downloaded and decrypted on the current device. Only if this value is true can the semantic segmentation label names or inference results be acquired.

If metadata is available.

    **Parameters**:

    `System.NotSupportedException` - Thrown frame rate configuration is not supported.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### XRSemanticsSubsystem<a href="#XRSemanticsSubsystem" class="hash-link" aria-label="Direct link to XRSemanticsSubsystem" title="Direct link to XRSemanticsSubsystem">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
XRSemanticsSubsystem()
```

</div>

</div>

Construct the subsystem by creating the functionality provider.

#### TryGetSemanticChannel<a href="#TryGetSemanticChannel" class="hash-link" aria-label="Direct link to TryGetSemanticChannel" title="Direct link to TryGetSemanticChannel">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryGetSemanticChannel(
     string channelName,
       out XRTextureDescriptor semanticsChannelDescriptor,
       out Matrix4x4 samplerMatrix,
      XRCameraParams? cameraParams = null
  )
```

</div>

</div>

Get the XRTextureDescriptor for the specified semantic channel.

    **Parameters**:

    `channelName` - The string description of the semantics channel to acquire.

    `semanticsChannelDescriptor` - The resulting semantic channel texture descriptor, if available.

    `samplerMatrix` - The matrix that transforms from normalized viewport coordinates to normalized texture coordinates.

    `cameraParams` - Describes the viewport the texture is to be displayed on.

    `System.NotSupportedException` - Thrown if the implementation does not support semantics channel texture.

    **Returns:**

    true if the semantic channel texture descriptor is available and is returned. Otherwise, false.

#### TryAcquireSemanticChannelCpuImage<a href="#TryAcquireSemanticChannelCpuImage" class="hash-link" aria-label="Direct link to TryAcquireSemanticChannelCpuImage" title="Direct link to TryAcquireSemanticChannelCpuImage">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryAcquireSemanticChannelCpuImage(
     string channelName,
       out XRCpuImage cpuImage,
      out Matrix4x4 samplerMatrix,
      XRCameraParams? cameraParams = null
  )
```

</div>

</div>

Acquire the latest semantic channel CPU image.

    **Parameters**:

    `channelName` - The string description of the semantics channel to acquire.

    `cpuImage` - The resulting XRCpuImage. The XRCpuImage must be disposed by the caller.

    `samplerMatrix` - The matrix that transforms from normalized viewport coordinates to normalized image coordinates.

    `cameraParams` - Describes the viewport the image is to be displayed on.

    `System.NotSupportedException` - Thrown if the implementation does not support semantic channels CPU images.

    **Returns:**

    Returns `true` if an XRCpuImage was successfully acquired. Returns `false` otherwise.

#### TryGetPackedSemanticChannels<a href="#TryGetPackedSemanticChannels" class="hash-link" aria-label="Direct link to TryGetPackedSemanticChannels" title="Direct link to TryGetPackedSemanticChannels">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryGetPackedSemanticChannels(
      out XRTextureDescriptor packedSemanticsDescriptor,
        out Matrix4x4 samplerMatrix,
      XRCameraParams? cameraParams = null
  )
```

</div>

</div>

Get the packed semantics texture descriptor.

    **Parameters**:

    `packedSemanticsDescriptor` - The resulting semantic channel texture descriptor, if available.

    `samplerMatrix` - The matrix that transforms from normalized viewport coordinates to normalized texture coordinates.

    `cameraParams` - Describes the viewport the texture is to be displayed on.

    `System.NotSupportedException` - Thrown if the implementation does not support packed semantics texture.

    **Returns:**

    true if the packed semantics texture descriptor is available and is returned. Otherwise, false.

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

Acquire the latest packed semantic channels XRCpuImage.

    **Parameters**:

    `cpuImage` - The resulting XRCpuImage. The XRCpuImage must be disposed by the caller.

    `samplerMatrix` - The matrix that transforms from normalized viewport coordinates to normalized image coordinates.

    `cameraParams` - Describes the viewport the image is to be displayed on.

    **Returns:**

    Returns `true` if an XRCpuImage was successfully acquired. Returns `false` otherwise.

#### TryGetSuppressionMaskTexture<a href="#TryGetSuppressionMaskTexture" class="hash-link" aria-label="Direct link to TryGetSuppressionMaskTexture" title="Direct link to TryGetSuppressionMaskTexture">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryGetSuppressionMaskTexture(
      out XRTextureDescriptor suppressionMaskDescriptor,
        out Matrix4x4 samplerMatrix,
      XRCameraParams? cameraParams = null
  )
```

</div>

</div>

Get a semantic suppression texture descriptor.

    **Parameters**:

    `suppressionMaskDescriptor` - The resulting semantic suppression mask texture descriptor, if available.

    `samplerMatrix` - The matrix that transforms from normalized viewport coordinates to normalized texture coordinates.

    `cameraParams` - Describes the viewport the texture is to be displayed on.

    `System.NotSupportedException` - Thrown if the implementation does not support suppression mask texture.

    **Returns:**

    true if the suppression mask texture descriptor is available and is returned. Otherwise, false.

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

Acquire the latest suppression mask XRCpuImage.

    **Parameters**:

    `cpuImage` - The resulting XRCpuImage. The XRCpuImage must be disposed by the caller.

    `samplerMatrix` - The matrix that transforms from normalized viewport coordinates to normalized image coordinates.

    `cameraParams` - Describes the viewport the image is to be displayed on.

    **Returns:**

    Returns `true` if an XRCpuImage was successfully acquired. Returns `false` otherwise.

#### TryAcquireSuppressionMaskCpuImage<a href="#TryAcquireSuppressionMaskCpuImage" class="hash-link" aria-label="Direct link to TryAcquireSuppressionMaskCpuImage" title="Direct link to TryAcquireSuppressionMaskCpuImage">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryAcquireSuppressionMaskCpuImage(
     out XRCpuImage cpuImage,
      out Matrix4x4 samplerMatrix,
      XRCameraParams? cameraParams,
       Matrix4x4? targetPose
 )
```

</div>

</div>

Acquire the latest suppression mask XRCpuImage.

    **Parameters**:

    `cpuImage` - The resulting XRCpuImage. The XRCpuImage must be disposed by the caller.

    `samplerMatrix` - The matrix that transforms from normalized viewport coordinates to normalized image coordinates.

    `cameraParams` - Describes the viewport the image is to be displayed on.

    `targetPose` - Any image acquired has been captured in the past. The target pose argument defines the pose the image needs to synchronize with. If the image can be synchronized, the samplerMatrix will be calibrated to warp the image as if it was taken from the target pose. If this argument is null, the image will not be warped.

    **Returns:**

    Returns `true` if an XRCpuImage was successfully acquired. Returns `false` otherwise.

#### TryGetChannelNames<a href="#TryGetChannelNames" class="hash-link" aria-label="Direct link to TryGetChannelNames" title="Direct link to TryGetChannelNames">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryGetChannelNames(out IReadOnlyList<string> names)
```

</div>

</div>

Get a list of the semantic channel names for the current semantic model.

    **Parameters**:

    `System.NotSupportedException` - Thrown when reading the channel names is not supported by the implementation.

    **Returns:**

    A list of semantic category labels. The list will be empty if metadata has not yet become available.

#### TrySetChannelConfidenceThresholds<a href="#TrySetChannelConfidenceThresholds" class="hash-link" aria-label="Direct link to TrySetChannelConfidenceThresholds" title="Direct link to TrySetChannelConfidenceThresholds">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TrySetChannelConfidenceThresholds(Dictionary<string, float> channelConfidenceThresholds)
```

</div>

</div>

Sets the confidence thresholds used for including the specified semantic channels in the packed semantic channel buffer.

Each semantic channel will use its default threshold value chosen by the model until a new value is set by this function during the [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) session.

    **Parameters**:

    `channelConfidenceThresholds` - A dictionary consisting of keys specifying the name of the semantics channel that is needed and values between 0 and 1, inclusive, that set the threshold above which the platform will include the specified channel in the packed semantics buffer. The key must be a semantic channel name present in the list returned by TryGetChannelNames.

    `System.NotSupportedException` - Thrown when setting confidence thresholds is not supported by the implementation.

    **Returns:**

    True if the threshold was set. Otherwise, false.

#### TryResetChannelConfidenceThresholds<a href="#TryResetChannelConfidenceThresholds" class="hash-link" aria-label="Direct link to TryResetChannelConfidenceThresholds" title="Direct link to TryResetChannelConfidenceThresholds">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryResetChannelConfidenceThresholds()
```

</div>

</div>

Resets the confidence thresholds for all semantic channels to the default values from the current model.

This reverts any changes made with [TrySetChannelConfidenceThresholds](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRSemanticsSubsystem/#TrySetChannelConfidenceThresholds).

    **Parameters**:

    `System.NotSupportedException` - Thrown when resetting confidence thresholds is not supported by the implementation.

    **Returns:**

    True if the thresholds were reset. Otherwise, false.

#### Register<a href="#Register" class="hash-link" aria-label="Direct link to Register" title="Direct link to Register">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static bool Register(XRSemanticsSubsystemCinfo semanticsSubsystemCinfo)
```

</div>

</div>

Register the descriptor for the semantics subsystem implementation.

    **Parameters**:

    `semanticsSubsystemCinfo` - The semantics subsystem implementation construction information.

    **Returns:**

    true if the descriptor was registered. Otherwise, false.

#### OnStop<a href="#OnStop" class="hash-link" aria-label="Direct link to OnStop" title="Direct link to OnStop">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override void OnStop()
```

</div>

</div>

Invoked when the subsystem is being stopped.

</div>

</div>
