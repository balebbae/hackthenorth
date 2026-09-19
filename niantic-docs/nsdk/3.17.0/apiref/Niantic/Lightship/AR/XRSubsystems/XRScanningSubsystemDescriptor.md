---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRScanningSubsystemDescriptor/
title: class XRScanningSubsystemDescriptor
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class XRScanningSubsystemDescriptor

</div>

(Niantic.Lightship.AR.XRSubsystems.XRScanningSubsystemDescriptor)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class XRScanningSubsystemDescriptor: SubsystemDescriptorWithProvider< XRScanningSubsystem, XRScanningSubsystem.Provider > {
   public:
   
     struct Cinfo;

      // methods
   
     static void Create(Cinfo cinfo);
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### Create<a href="#Create" class="hash-link" aria-label="Direct link to Create" title="Direct link to Create">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static void Create(Cinfo cinfo)
```

</div>

</div>

Creates a new subsystem descriptor and registers it with the SubsystemManager.

    **Parameters**:

    `cinfo` - Constructor info describing the descriptor to create.

</div>

</div>
