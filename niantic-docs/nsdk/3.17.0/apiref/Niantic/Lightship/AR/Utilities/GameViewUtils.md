---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/GameViewUtils/
title: class GameViewUtils
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class GameViewUtils

</div>

(Niantic.Lightship.AR.Utilities.GameViewUtils)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class GameViewUtils {
 public:
       // methods
   
     static ScreenOrientation GetEditorScreenOrientation();
        static ScreenOrientation GetGameViewAspectRatio(XRCameraParams cameraParams);
  };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### GetEditorScreenOrientation<a href="#GetEditorScreenOrientation" class="hash-link" aria-label="Direct link to GetEditorScreenOrientation" title="Direct link to GetEditorScreenOrientation">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static ScreenOrientation GetEditorScreenOrientation()
```

</div>

</div>

Calculates the screen orientation via the game view aspect ratio. Use this method instead of UnityEngine.Screen.orientation in Editor, as the latter only returns Portrait in Editor.

    **Returns:**

    The screen orientation. When this method is called in a platform other than the Unity Editor, it defaults to return ScreenOrientation.Portrait.

</div>

</div>
