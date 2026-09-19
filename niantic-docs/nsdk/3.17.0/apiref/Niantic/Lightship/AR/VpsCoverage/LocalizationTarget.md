---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/LocalizationTarget/
title: struct LocalizationTarget
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct LocalizationTarget

</div>

(Niantic.Lightship.AR.VpsCoverage.LocalizationTarget)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The [LocalizationTarget](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/LocalizationTarget/) struct represents a real world point of interest that used for VPS tracking.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
struct LocalizationTarget {
       // fields
    
      readonly string Identifier => _identifier;
        readonly LatLng Center => _center;
      readonly string Name => _name;
        readonly string ImageURL => _imageURL;
        readonly string DefaultAnchor => _defaultAnchor;
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The [LocalizationTarget](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/LocalizationTarget/) struct represents a real world point of interest that used for VPS tracking.

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### Identifier<a href="#Identifier" class="hash-link" aria-label="Direct link to Identifier" title="Direct link to Identifier">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly string Identifier => _identifier
```

</div>

</div>

Unique identifier of the [LocalizationTarget](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/LocalizationTarget/).

#### Center<a href="#Center" class="hash-link" aria-label="Direct link to Center" title="Direct link to Center">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly LatLng Center => _center
```

</div>

</div>

Geolocation of the [LocalizationTarget](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/LocalizationTarget/).

#### Name<a href="#Name" class="hash-link" aria-label="Direct link to Name" title="Direct link to Name">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly string Name => _name
```

</div>

</div>

Name of the [LocalizationTarget](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/LocalizationTarget/).

#### ImageURL<a href="#ImageURL" class="hash-link" aria-label="Direct link to ImageURL" title="Direct link to ImageURL">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly string ImageURL => _imageURL
```

</div>

</div>

Url where hint image is stored.

#### DefaultAnchor<a href="#DefaultAnchor" class="hash-link" aria-label="Direct link to DefaultAnchor" title="Direct link to DefaultAnchor">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly string DefaultAnchor => _defaultAnchor
```

</div>

</div>

Default anchor.

</div>

</div>
