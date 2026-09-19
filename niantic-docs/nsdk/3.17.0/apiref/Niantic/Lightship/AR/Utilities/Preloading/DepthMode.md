---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/DepthMode/
title: enum DepthMode
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# enum DepthMode

</div>

(Niantic.Lightship.AR.Utilities.Preloading.DepthMode)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The Lightship depth model to use.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs

enum DepthMode: byte {
      Unspecified = 0,
        Custom      = 1,
        Fast        = 2,
        Medium      = 3,
        Smooth      = 4,
};
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The Lightship depth model to use.

This is analogous to Unity's UnityEngine.XR.ARSubsystems.EnvironmentDepthMode.

### Enum Values<a href="#enum-values" class="hash-link" aria-label="Direct link to Enum Values" title="Direct link to Enum Values">​</a>

**Unspecified** - The default model will be used, if applicable.

**Fast** - Depth will be generated at the fastest resolution.

**Medium** - Depth will be generated at a medium resolution.

**Smooth** - Depth will be generated at the best resolution.

</div>

</div>
