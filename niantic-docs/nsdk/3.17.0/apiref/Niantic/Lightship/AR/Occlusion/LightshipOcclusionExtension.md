---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Occlusion/LightshipOcclusionExtension/
title: class LightshipOcclusionExtension
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class LightshipOcclusionExtension

</div>

(Niantic.Lightship.AR.Occlusion.LightshipOcclusionExtension)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

This component allows configuration of the additional functionality available in Lightship's implementation of XROcclusionSubsystem.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class LightshipOcclusionExtension: CompositeRenderer {
  public:
       // fields
    
      bool IsRenderingActive => IsCommandBufferAdded ||(!IsUsingLegacyRenderPipeline&& IsAnyFeatureEnabled);
        bool SupportsTargetFrameRate => IsUsingLightshipOcclusionSubsystem;
         Texture2D DepthTexture => _occlusionComponent?.GPUDepth;
        Matrix4x4 DepthTransform => _occlusionComponent?.DepthTransform ?? Matrix4x4.identity;
         static const string ZBufferOcclusionShaderName = "Lightship/ZBufferOcclusion";
       static const string OcclusionMeshShaderName = "Lightship/OcclusionMesh";

        // properties
    
     uint?? TargetFrameRate;
        Matrix4x4? LatestIntrinsicsMatrix;
      Matrix4x4? LatestExtrinsicsMatrix;
      OptimalOcclusionDistanceMode OcclusionDistanceMode;
     bool BypassOcclusionManagerUpdates;
       bool OverrideOcclusionManagerSettings;
        Material CustomMaterial;
        Material CustomBackgroundMaterial;
      Material BackgroundMaterial;
        bool UseCustomBackgroundMaterial;
     Material FusedDepthMaterial;
        OptimalOcclusionDistanceMode Mode;

      // methods
   
     bool TryGetDepth(int screenX, int screenY, out float depth);
     void TrackOccludee(Renderer occludee);

 protected:
        // fields
    
      override string RendererName => "LightshipOcclusionExtension Pass(LegacyRP)";
       override bool ShouldAddCommandBuffer => IsUsingLegacyRenderPipeline&& IsAnyFeatureEnabled;

        // properties
    
     override string ShaderName;

     // methods
   
     override string[] OnRequestExternalPassDependencies(CameraEvent evt);
        override bool OnAddRenderCommands(CommandBuffer cmd, Material mat);
     override void Awake();
      override void Update();
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

This component allows configuration of the additional functionality available in Lightship's implementation of XROcclusionSubsystem.

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### RendererName<a href="#RendererName" class="hash-link" aria-label="Direct link to RendererName" title="Direct link to RendererName">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override string RendererName => "LightshipOcclusionExtension Pass(LegacyRP)"
```

</div>

</div>

The name of the occlusion extension command buffer.

#### ShouldAddCommandBuffer<a href="#ShouldAddCommandBuffer" class="hash-link" aria-label="Direct link to ShouldAddCommandBuffer" title="Direct link to ShouldAddCommandBuffer">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override bool ShouldAddCommandBuffer => IsUsingLegacyRenderPipeline&& IsAnyFeatureEnabled
```

</div>

</div>

Determines whether the command buffer should be attached to the camera.

#### IsRenderingActive<a href="#IsRenderingActive" class="hash-link" aria-label="Direct link to IsRenderingActive" title="Direct link to IsRenderingActive">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool IsRenderingActive => IsCommandBufferAdded ||(!IsUsingLegacyRenderPipeline&& IsAnyFeatureEnabled)
```

</div>

</div>

Whether the second pass of background rendering is active to satisfy custom occlusion features.

#### SupportsTargetFrameRate<a href="#SupportsTargetFrameRate" class="hash-link" aria-label="Direct link to SupportsTargetFrameRate" title="Direct link to SupportsTargetFrameRate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool SupportsTargetFrameRate => IsUsingLightshipOcclusionSubsystem
```

</div>

</div>

Determines whether the [TargetFrameRate](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Occlusion/LightshipOcclusionExtension/#TargetFrameRate) API is supported with the current configuration.

#### DepthTexture<a href="#DepthTexture" class="hash-link" aria-label="Direct link to DepthTexture" title="Direct link to DepthTexture">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Texture2D DepthTexture => _occlusionComponent?.GPUDepth
```

</div>

</div>

Returns the raw depth texture used in rendering.

#### DepthTransform<a href="#DepthTransform" class="hash-link" aria-label="Direct link to DepthTransform" title="Direct link to DepthTransform">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Matrix4x4 DepthTransform => _occlusionComponent?.DepthTransform ?? Matrix4x4.identity
```

</div>

</div>

Returns a transform for converting between normalized image coordinates and a coordinate space appropriate for rendering [DepthTexture](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Occlusion/LightshipOcclusionExtension/#DepthTexture) on the viewport.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### ShaderName<a href="#ShaderName" class="hash-link" aria-label="Direct link to ShaderName" title="Direct link to ShaderName">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override string ShaderName
```

</div>

</div>

The name of the shader used by the rendering material.

#### TargetFrameRate<a href="#TargetFrameRate" class="hash-link" aria-label="Direct link to TargetFrameRate" title="Direct link to TargetFrameRate">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
uint?? TargetFrameRate
```

</div>

</div>

The framerate that depth inference will aim to run at. Setting the value to 0 will result in using the recommended frame rate. Call [SupportsTargetFrameRate](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Occlusion/LightshipOcclusionExtension/#SupportsTargetFrameRate) to check if the target frame rate is supported.

#### LatestIntrinsicsMatrix<a href="#LatestIntrinsicsMatrix" class="hash-link" aria-label="Direct link to LatestIntrinsicsMatrix" title="Direct link to LatestIntrinsicsMatrix">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Matrix4x4? LatestIntrinsicsMatrix
```

</div>

</div>

Returns the intrinsics matrix for [DepthTexture](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Occlusion/LightshipOcclusionExtension/#DepthTexture). Contains values for the camera's focal length and principal point. Converts between 2D image pixel coordinates and 3D world coordinates relative to the camera.

#### LatestExtrinsicsMatrix<a href="#LatestExtrinsicsMatrix" class="hash-link" aria-label="Direct link to LatestExtrinsicsMatrix" title="Direct link to LatestExtrinsicsMatrix">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Matrix4x4? LatestExtrinsicsMatrix
```

</div>

</div>

Returns the extrinsics matrix for [DepthTexture](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Occlusion/LightshipOcclusionExtension/#DepthTexture).

#### OcclusionDistanceMode<a href="#OcclusionDistanceMode" class="hash-link" aria-label="Direct link to OcclusionDistanceMode" title="Direct link to OcclusionDistanceMode">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
OptimalOcclusionDistanceMode OcclusionDistanceMode
```

</div>

</div>

Get or set the current mode in use for determining the distance at which occlusions will have the best visual quality.

#### BypassOcclusionManagerUpdates<a href="#BypassOcclusionManagerUpdates" class="hash-link" aria-label="Direct link to BypassOcclusionManagerUpdates" title="Direct link to BypassOcclusionManagerUpdates">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool BypassOcclusionManagerUpdates
```

</div>

</div>

Whether to disable automatically updating the depth texture of the occlusion manager. This feature can be used to avoid redundant texture operations since depth is ultimately going to be overriden by the Lightship [Occlusion](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Occlusion/) Extension anyway. Not using this setting may result in undesired synchronization with the rendering thread that impacts performance.

#### OverrideOcclusionManagerSettings<a href="#OverrideOcclusionManagerSettings" class="hash-link" aria-label="Direct link to OverrideOcclusionManagerSettings" title="Direct link to OverrideOcclusionManagerSettings">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool OverrideOcclusionManagerSettings
```

</div>

</div>

Whether to override the occlusion manager's settings to set the most optimal configuration for the occlusion extension. Currently, the following overrides are applied: 1) On iPhone devices with Lidar sensor, the best and medium occlusion mode will cause a significant performance hit as well as a crash. We will override the occlusion mode to fastest to avoid this issue and enable smooth edges for the best results. 2) The occlusion preference mode is set to NoOcclusion when the occlusion extension is active.

#### CustomMaterial<a href="#CustomMaterial" class="hash-link" aria-label="Direct link to CustomMaterial" title="Direct link to CustomMaterial">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Material CustomMaterial
```

</div>

</div>

Get or set the custom material used for processing the [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) background depth buffer. If set to null, the default material will be used.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### OnRequestExternalPassDependencies<a href="#OnRequestExternalPassDependencies" class="hash-link" aria-label="Direct link to OnRequestExternalPassDependencies" title="Direct link to OnRequestExternalPassDependencies">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override string[] OnRequestExternalPassDependencies(CameraEvent evt)
```

</div>

</div>

The occlusion extension command buffer needs to run after the [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) Background command buffer.

#### TryGetDepth<a href="#TryGetDepth" class="hash-link" aria-label="Direct link to TryGetDepth" title="Direct link to TryGetDepth">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool TryGetDepth(int screenX, int screenY, out float depth)
```

</div>

</div>

Returns the metric eye depth at the specified pixel coordinates.

    **Parameters**:

    `screenX` - The x position on the screen.

    `screenY` - The y position on the screen.

    `depth` - The resulting depth value.

    **Returns:**

    Whether retrieving the depth value was successful.

#### TrackOccludee<a href="#TrackOccludee" class="hash-link" aria-label="Direct link to TrackOccludee" title="Direct link to TrackOccludee">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void TrackOccludee(Renderer occludee)
```

</div>

</div>

Sets the principal virtual object being occluded in the SpecifiedGameObject occlusion mode.

This method changes the optimal occlusion distance mode setting.

\>

</div>

</div>
