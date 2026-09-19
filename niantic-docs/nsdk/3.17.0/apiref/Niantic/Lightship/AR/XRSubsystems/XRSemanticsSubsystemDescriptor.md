---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRSemanticsSubsystemDescriptor/
title: class XRSemanticsSubsystemDescriptor
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class XRSemanticsSubsystemDescriptor

</div>

(Niantic.Lightship.AR.XRSubsystems.XRSemanticsSubsystemDescriptor)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Descriptor for the [XRSemanticsSubsystem](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRSemanticsSubsystem/).

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class XRSemanticsSubsystemDescriptor: SubsystemDescriptorWithProvider< XRSemanticsSubsystem, XRSemanticsSubsystem.Provider > {
    public:
       // properties
    
     Supported semanticSegmentationImageSupported;
   };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Descriptor for the [XRSemanticsSubsystem](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRSemanticsSubsystem/).

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### semanticSegmentationImageSupported<a href="#semanticSegmentationImageSupported" class="hash-link" aria-label="Direct link to semanticSegmentationImageSupported" title="Direct link to semanticSegmentationImageSupported">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Supported semanticSegmentationImageSupported
```

</div>

</div>

(Read Only) Whether the subsystem supports semantic segmentation image.

The supported status might take time to determine. If support is still being determined, the value will be Supported.Unknown.

</div>

</div>
