---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/PersistentAnchors/ARPersistentAnchorStateChangedEventArgs/
title: struct ARPersistentAnchorStateChangedEventArgs
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct ARPersistentAnchorStateChangedEventArgs

</div>

(Niantic.Lightship.AR.PersistentAnchors.ARPersistentAnchorStateChangedEventArgs)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Contains information about an [ARPersistentAnchor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/PersistentAnchors/ARPersistentAnchor/) that has changed state.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
struct ARPersistentAnchorStateChangedEventArgs {
      // properties
    
     ARPersistentAnchor arPersistentAnchor;

      // methods
   
     ARPersistentAnchorStateChangedEventArgs(ARPersistentAnchor arPersistentAnchor);
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Contains information about an [ARPersistentAnchor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/PersistentAnchors/ARPersistentAnchor/) that has changed state.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### arPersistentAnchor<a href="#arPersistentAnchor" class="hash-link" aria-label="Direct link to arPersistentAnchor" title="Direct link to arPersistentAnchor">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ARPersistentAnchor arPersistentAnchor
```

</div>

</div>

The [ARPersistentAnchor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/PersistentAnchors/ARPersistentAnchor/) that has changed state

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### ARPersistentAnchorStateChangedEventArgs<a href="#ARPersistentAnchorStateChangedEventArgs" class="hash-link" aria-label="Direct link to ARPersistentAnchorStateChangedEventArgs" title="Direct link to ARPersistentAnchorStateChangedEventArgs">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ARPersistentAnchorStateChangedEventArgs(ARPersistentAnchor arPersistentAnchor)
```

</div>

</div>

Creates the args for state changes on [ARPersistentAnchor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/PersistentAnchors/ARPersistentAnchor/)

    **Parameters**:

    `arPersistentAnchor` - The [ARPersistentAnchor](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/PersistentAnchors/ARPersistentAnchor/) with the state change

</div>

</div>
