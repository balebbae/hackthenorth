---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/XRDisplayContext/
title: class XRDisplayContext
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class XRDisplayContext

</div>

(Niantic.Lightship.AR.Utilities.XRDisplayContext)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Container for data relevant to rendering in relation to the XR camera's display

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class XRDisplayContext {
  public:
       // fields
    
      static float OccludeeEyeDepth = DefaultOccludeeEyeDepth;

        // methods
   
     static ScreenOrientation GetScreenOrientation();
  };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Container for data relevant to rendering in relation to the XR camera's display

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### OccludeeEyeDepth<a href="#OccludeeEyeDepth" class="hash-link" aria-label="Direct link to OccludeeEyeDepth" title="Direct link to OccludeeEyeDepth">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static float OccludeeEyeDepth = DefaultOccludeeEyeDepth
```

</div>

</div>

Linear eye-depth from the camera to the occludee.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### GetScreenOrientation<a href="#GetScreenOrientation" class="hash-link" aria-label="Direct link to GetScreenOrientation" title="Direct link to GetScreenOrientation">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static ScreenOrientation GetScreenOrientation()
```

</div>

</div>

For Lightship, it is important to know the screen orientation in order to know how to rotate the camera input image received from the XRCameraSubsystem. The UnityEngine.Screen.orientation property only returns ScreenOrientation.Portrait when called in Editor, presumably because there is no rotation offset between the camera image and the displayed screen image in Editor. Thus, use this method to get the screen orientation value expected by Lightship's APIs, regardless of the active platform.

    **Returns:**

    The corrected screen orientation. When running XR in Lightship's Playback mode, the returned value will match the screen orientation recorded in the dataset's current frame. Else, will return the UnityEngine.Screen.orientation value.

</div>

</div>
