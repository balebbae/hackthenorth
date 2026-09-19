---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorSubsystemDescriptor/
title: class XRPersistentAnchorSubsystemDescriptor
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class XRPersistentAnchorSubsystemDescriptor

</div>

(Niantic.Lightship.AR.XRSubsystems.XRPersistentAnchorSubsystemDescriptor)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Descriptor for the [XRPersistentAnchorSubsystem](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorSubsystem/).

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class XRPersistentAnchorSubsystemDescriptor: SubsystemDescriptorWithProvider< XRPersistentAnchorSubsystem, XRPersistentAnchorSubsystem.Provider > {
   public:
   
     struct Cinfo;

      // properties
    
     bool supportsTrackableAttachments;

        // methods
   
     static void Create(Cinfo cinfo);
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Descriptor for the [XRPersistentAnchorSubsystem](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRPersistentAnchorSubsystem/).

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### supportsTrackableAttachments<a href="#supportsTrackableAttachments" class="hash-link" aria-label="Direct link to supportsTrackableAttachments" title="Direct link to supportsTrackableAttachments">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool supportsTrackableAttachments
```

</div>

</div>

true if the subsystem supports attachments (that is, the ability to attach an anchor to a trackable).

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
