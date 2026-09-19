---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Utilities/Preloading/SemanticsMode/
title: enum SemanticsMode
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# enum SemanticsMode

</div>

(Niantic.Lightship.AR.Utilities.Preloading.SemanticsMode)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The Lightship semantic segmentation model to use.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs

enum SemanticsMode: byte {
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

The Lightship semantic segmentation model to use.

### Enum Values<a href="#enum-values" class="hash-link" aria-label="Direct link to Enum Values" title="Direct link to Enum Values">​</a>

**Unspecified** - The default model will be used, if applicable.

**Fast** - Semantic segmentation will be generated at the fastest resolution.

**Medium** - Semantic segmentation will be generated at a medium resolution.

**Smooth** - Semantic segmentation will be generated at the best resolution.

</div>

</div>
