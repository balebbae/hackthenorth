---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRSemanticsSubsystem/Provider/
title: class Provider
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class Provider

</div>

(Niantic.Lightship.AR.XRSubsystems.XRSemanticsSubsystem.Provider)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The provider which will service the [XRSemanticsSubsystem](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRSemanticsSubsystem/).

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class Provider: SubsystemProvider< XRSemanticsSubsystem > {
   public:
       // fields
    
      ? uint LatestFrameId => throw new NotSupportedException("Getting the latest frame id is not supported by this implementation");
      bool IsMetadataAvailable => throw new NotSupportedException("Getting if metadata is available is not supported by this implementation");

      // properties
    
     uint TargetFrameRate;
     HashSet<string> SuppressionMaskChannels;

      // methods
   
     virtual bool TryPrepareSubsystem();
 
     virtual bool TryGetSemanticChannel(
           string channelName,
           out XRTextureDescriptor semanticChannelDescriptor,
            out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams = null
      );
    
     virtual bool TryAcquireSemanticChannelCpuImage(
           string channelName,
           out XRCpuImage cpuImage,
          out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams = null
      );
    
     virtual bool TryGetPackedSemanticChannels(
            out XRTextureDescriptor packedSemanticsDescriptor,
            out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams = null
      );
    
     virtual bool TryAcquirePackedSemanticChannelsCpuImage(
            out XRCpuImage cpuImage,
          out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams = null
      );
    
     virtual bool TryGetSuppressionMaskTexture(
            out XRTextureDescriptor suppressionMaskDescriptor,
            out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams = null
      );
    
     virtual bool TryAcquireSuppressionMaskCpuImage(
           out XRCpuImage cpuImage,
          out Matrix4x4 samplerMatrix,
          XRCameraParams? cameraParams = null
      );
    
     virtual bool TryGetChannelNames(out IReadOnlyList<string> names);
        virtual bool TrySetChannelConfidenceThresholds(Dictionary<string, float> channelConfidenceThresholds);
       virtual bool TryResetChannelConfidenceThresholds();
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The provider which will service the [XRSemanticsSubsystem](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRSemanticsSubsystem/).

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### TargetFrameRate<a href="#TargetFrameRate" class="hash-link" aria-label="Direct link to TargetFrameRate" title="Direct link to TargetFrameRate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
uint TargetFrameRate
```

</div>

</div>

Property to be implemented by the provider to get or set the frame rate for the platform's semantic segmentation feature.

The requested frame rate in frames per second.

    **Parameters**:

    `System.NotSupportedException` - Thrown when requesting a frame rate that is not supported by the implementation.

#### SuppressionMaskChannels<a href="#SuppressionMaskChannels" class="hash-link" aria-label="Direct link to SuppressionMaskChannels" title="Direct link to SuppressionMaskChannels">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
HashSet<string> SuppressionMaskChannels
```

</div>

</div>

Property to be implemented by the provider to get or set the list of suppression channels for the platform's semantic segmentation feature.

The requested list of suppression channels

    **Parameters**:

    `System.NotSupportedException` - Thrown if the list of channels is not supported by this implementation.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### TryPrepareSubsystem<a href="#TryPrepareSubsystem" class="hash-link" aria-label="Direct link to TryPrepareSubsystem" title="Direct link to TryPrepareSubsystem">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual bool TryPrepareSubsystem()
```

</div>

</div>

If the semantic segmentation model is ready, prepare the subsystem's data structures.

    **Returns:**

    true if the semantic segmentation model is ready and the subsystem has prepared its data structures. Otherwise, false.

#### TryGetSemanticChannel<a href="#TryGetSemanticChannel" class="hash-link" aria-label="Direct link to TryGetSemanticChannel" title="Direct link to TryGetSemanticChannel">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual bool TryGetSemanticChannel(
       string channelName,
       out XRTextureDescriptor semanticChannelDescriptor,
        out Matrix4x4 samplerMatrix,
      XRCameraParams? cameraParams = null
  )
```

</div>

</div>

Get the XRTextureDescriptor for the specified semantic channel.

    **Parameters**:

    `channelName` - The string description of the semantics channel to acquire.

    `semanticChannelDescriptor` - The resulting semantic channel texture descriptor, if available.

    `samplerMatrix` - The matrix that transforms from normalized viewport coordinates to normalized texture coordinates.

    `cameraParams` - Describes the viewport the texture is to be displayed on.

    `System.NotSupportedException` - Thrown if the implementation does not support semantics channel texture.

    **Returns:**

    true if the semantic channel texture descriptor is available and is returned. Otherwise, false.

#### TryAcquireSemanticChannelCpuImage<a href="#TryAcquireSemanticChannelCpuImage" class="hash-link" aria-label="Direct link to TryAcquireSemanticChannelCpuImage" title="Direct link to TryAcquireSemanticChannelCpuImage">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual bool TryAcquireSemanticChannelCpuImage(
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
virtual bool TryGetPackedSemanticChannels(
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
virtual bool TryAcquirePackedSemanticChannelsCpuImage(
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
virtual bool TryGetSuppressionMaskTexture(
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
virtual bool TryAcquireSuppressionMaskCpuImage(
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

#### TryGetChannelNames<a href="#TryGetChannelNames" class="hash-link" aria-label="Direct link to TryGetChannelNames" title="Direct link to TryGetChannelNames">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual bool TryGetChannelNames(out IReadOnlyList<string> names)
```

</div>

</div>

Method to be implemented by the provider to get a list of the semantic channel names for the current semantic model.

    **Parameters**:

    `names` - A list of semantic category labels. It will be empty if the method returns false.

    `System.NotSupportedException` - Thrown when reading the channel names is not supported by the implementation.

    **Returns:**

    True if channel names are available. False if not.

#### TrySetChannelConfidenceThresholds<a href="#TrySetChannelConfidenceThresholds" class="hash-link" aria-label="Direct link to TrySetChannelConfidenceThresholds" title="Direct link to TrySetChannelConfidenceThresholds">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
virtual bool TrySetChannelConfidenceThresholds(Dictionary<string, float> channelConfidenceThresholds)
```

</div>

</div>

Sets the confidence threshold for including the specified semantic channel in the packed semantic channel buffer.

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
virtual bool TryResetChannelConfidenceThresholds()
```

</div>

</div>

Resets the confidence thresholds for all semantic channels to the default values from the current model.

This reverts any changes made with TrySetChannelConfidenceThresholds.

    **Parameters**:

    `System.NotSupportedException` - Thrown when resetting confidence thresholds is not supported by the implementation.

    **Returns:**

    True if the thresholds were reset. Otherwise, false.

</div>

</div>
