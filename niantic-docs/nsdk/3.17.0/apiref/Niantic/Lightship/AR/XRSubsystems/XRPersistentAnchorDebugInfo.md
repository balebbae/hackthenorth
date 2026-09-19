---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorDebugInfo/
title: struct XRPersistentAnchorDebugInfo
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct XRPersistentAnchorDebugInfo

</div>

(Niantic.Lightship.AR.XRSubsystems.XRPersistentAnchorDebugInfo)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Contains debug information of [XRPersistentAnchorSubsystem](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorSubsystem/)

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
struct XRPersistentAnchorDebugInfo {
      // properties
    
     XRPersistentAnchorNetworkRequestStatus[] networkStatusArray;
        XRPersistentAnchorLocalizationStatus[] localizationStatusArray;
     XRPersistentAnchorFrameDiagnostics[] frameDiagnosticsArray;

     // methods
   
     XRPersistentAnchorDebugInfo(
         XRPersistentAnchorNetworkRequestStatus[] networkStatusArray,
            XRPersistentAnchorLocalizationStatus[] localizationStatusArray,
         XRPersistentAnchorFrameDiagnostics[] frameDiagnosticsArray
        );
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Contains debug information of [XRPersistentAnchorSubsystem](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorSubsystem/)

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### networkStatusArray<a href="#networkStatusArray" class="hash-link" aria-label="Direct link to networkStatusArray" title="Direct link to networkStatusArray">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
XRPersistentAnchorNetworkRequestStatus[] networkStatusArray
```

</div>

</div>

Array of [XRPersistentAnchorNetworkRequestStatus](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorNetworkRequestStatus/)

#### localizationStatusArray<a href="#localizationStatusArray" class="hash-link" aria-label="Direct link to localizationStatusArray" title="Direct link to localizationStatusArray">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
XRPersistentAnchorLocalizationStatus[] localizationStatusArray
```

</div>

</div>

Array of [XRPersistentAnchorLocalizationStatus](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorLocalizationStatus/)

#### frameDiagnosticsArray<a href="#frameDiagnosticsArray" class="hash-link" aria-label="Direct link to frameDiagnosticsArray" title="Direct link to frameDiagnosticsArray">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
XRPersistentAnchorFrameDiagnostics[] frameDiagnosticsArray
```

</div>

</div>

Array of XRPersistentAnchorFrameDiagnostics

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### XRPersistentAnchorDebugInfo<a href="#XRPersistentAnchorDebugInfo" class="hash-link" aria-label="Direct link to XRPersistentAnchorDebugInfo" title="Direct link to XRPersistentAnchorDebugInfo">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
XRPersistentAnchorDebugInfo(
     XRPersistentAnchorNetworkRequestStatus[] networkStatusArray,
        XRPersistentAnchorLocalizationStatus[] localizationStatusArray,
     XRPersistentAnchorFrameDiagnostics[] frameDiagnosticsArray
    )
```

</div>

</div>

[XRPersistentAnchorDebugInfo](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorDebugInfo/) Contructor

    **Parameters**:

    `[XRPersistentAnchorDebugInfo](./index.mdx)` - The [XRPersistentAnchorDebugInfo](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorDebugInfo/) with the debug data arrays

</div>

</div>
