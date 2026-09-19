---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Networking/PeerID/
title: struct PeerID
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct PeerID

</div>

(Niantic.Lightship.SharedAR.Networking.PeerID)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Struct that represents the identifiers of other peers in the room. Can be compared with other PeerIDs and used as Keys in Dictionaries.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   struct PeerID: IEquatable< PeerID > {
     // fields
    
      static readonly PeerID InvalidID = new(0);

       // properties
    
     Guid Identifier;

        // methods
   
     PeerID(uint id);
      uint ToUint32();
      bool Equals(PeerID other);
     override int GetHashCode();
     override string ToString();
     override bool Equals(object obj);
      static bool operator == (PeerID left, PeerID right);
        static bool operator != (PeerID left, PeerID right);
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Struct that represents the identifiers of other peers in the room. Can be compared with other PeerIDs and used as Keys in Dictionaries.

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### InvalidID<a href="#InvalidID" class="hash-link" aria-label="Direct link to InvalidID" title="Direct link to InvalidID">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static readonly PeerID InvalidID = new(0)
```

</div>

</div>

The Invalid peer ID returned by functions that have errored. This [PeerID](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Networking/PeerID/) returns 0 from ToUint32.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### Identifier<a href="#Identifier" class="hash-link" aria-label="Direct link to Identifier" title="Direct link to Identifier">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Guid Identifier
```

</div>

</div>

Guid representation of the [PeerID](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Networking/PeerID/).

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### PeerID<a href="#PeerID" class="hash-link" aria-label="Direct link to PeerID" title="Direct link to PeerID">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
PeerID(uint id)
```

</div>

</div>

Constructor for the [PeerID](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Networking/PeerID/). PeerIDs should be received from the [INetworking](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Networking/INetworking/) API, not manually constructed.

#### ToUint32<a href="#ToUint32" class="hash-link" aria-label="Direct link to ToUint32" title="Direct link to ToUint32">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
uint ToUint32()
```

</div>

</div>

UInt32 representation of the [PeerID](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Networking/PeerID/).

#### Equals<a href="#Equals" class="hash-link" aria-label="Direct link to Equals" title="Direct link to Equals">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool Equals(PeerID other)
```

</div>

</div>

Equality implementation for [PeerID](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Networking/PeerID/).

#### GetHashCode<a href="#GetHashCode" class="hash-link" aria-label="Direct link to GetHashCode" title="Direct link to GetHashCode">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override int GetHashCode()
```

</div>

</div>

Get unique hash for this [PeerID](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Networking/PeerID/). Necessary for Dictionary compatibility.

#### ToString<a href="#ToString" class="hash-link" aria-label="Direct link to ToString" title="Direct link to ToString">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
override string ToString()
```

</div>

</div>

String representation of the [PeerID](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Networking/PeerID/).

</div>

</div>
