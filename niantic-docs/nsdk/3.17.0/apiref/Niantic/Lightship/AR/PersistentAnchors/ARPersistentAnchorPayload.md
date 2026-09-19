---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/PersistentAnchors/ARPersistentAnchorPayload/
title: class ARPersistentAnchorPayload
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class ARPersistentAnchorPayload

</div>

(Niantic.Lightship.AR.PersistentAnchors.ARPersistentAnchorPayload)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The [ARPersistentAnchorPayload](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/PersistentAnchors/ARPersistentAnchorPayload/) is data used to save and restore persistent anchors.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class ARPersistentAnchorPayload {
 public:
       // fields
    
      byte[] Data;

     // methods
   
     ARPersistentAnchorPayload(byte[] data);
       ARPersistentAnchorPayload(string data);
       string ToBase64();
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The [ARPersistentAnchorPayload](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/PersistentAnchors/ARPersistentAnchorPayload/) is data used to save and restore persistent anchors.

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### Data<a href="#Data" class="hash-link" aria-label="Direct link to Data" title="Direct link to Data">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
byte[] Data
```

</div>

</div>

The data associated with the payload

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### ARPersistentAnchorPayload<a href="#ARPersistentAnchorPayload" class="hash-link" aria-label="Direct link to ARPersistentAnchorPayload" title="Direct link to ARPersistentAnchorPayload">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ARPersistentAnchorPayload(byte[] data)
```

</div>

</div>

Creates a new [ARPersistentAnchorPayload](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/PersistentAnchors/ARPersistentAnchorPayload/)

    **Parameters**:

    `data` - The data associated with the payload

#### ARPersistentAnchorPayload<a href="#ARPersistentAnchorPayload" class="hash-link" aria-label="Direct link to ARPersistentAnchorPayload" title="Direct link to ARPersistentAnchorPayload">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ARPersistentAnchorPayload(string data)
```

</div>

</div>

Creates a new [ARPersistentAnchorPayload](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/PersistentAnchors/ARPersistentAnchorPayload/)

    **Parameters**:

    `data` - The base 64 string to create the payload from

#### ToBase64<a href="#ToBase64" class="hash-link" aria-label="Direct link to ToBase64" title="Direct link to ToBase64">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
string ToBase64()
```

</div>

</div>

Converts a payload to a base 64 string.

    **Returns:**

    The string representation of the payload. Returns null if no data exists in the payload.

</div>

</div>
