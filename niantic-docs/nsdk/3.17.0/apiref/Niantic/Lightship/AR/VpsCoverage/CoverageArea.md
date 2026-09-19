---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/CoverageArea/
title: struct CoverageArea
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct CoverageArea

</div>

(Niantic.Lightship.AR.VpsCoverage.CoverageArea)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The [CoverageArea](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/CoverageArea/) struct represents an area where localization with VPS is possible. Precisely, it is a calculated area representing a cluster of localization targets within a certain proximity of each other to help determine reliability of VPS tracking.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
struct CoverageArea {
 
     enumLocalizability;

        // fields
    
      readonly string[] LocalizationTargetIdentifiers => _localizationTargetIdentifiers;
        readonly LatLng[] Shape => _shape;
      readonly Localizability LocalizabilityQuality => _localizabilityQuality;

       // properties
    
     LatLng Centroid;
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The [CoverageArea](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/CoverageArea/) struct represents an area where localization with VPS is possible. Precisely, it is a calculated area representing a cluster of localization targets within a certain proximity of each other to help determine reliability of VPS tracking.

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### LocalizationTargetIdentifiers<a href="#LocalizationTargetIdentifiers" class="hash-link" aria-label="Direct link to LocalizationTargetIdentifiers" title="Direct link to LocalizationTargetIdentifiers">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly string[] LocalizationTargetIdentifiers => _localizationTargetIdentifiers
```

</div>

</div>

Identifiers of all LocalizationTargets within the [CoverageArea](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/CoverageArea/).

#### Shape<a href="#Shape" class="hash-link" aria-label="Direct link to Shape" title="Direct link to Shape">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly LatLng[] Shape => _shape
```

</div>

</div>

Polygon outlining the [CoverageArea](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/CoverageArea/).

#### LocalizabilityQuality<a href="#LocalizabilityQuality" class="hash-link" aria-label="Direct link to LocalizabilityQuality" title="Direct link to LocalizabilityQuality">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly Localizability LocalizabilityQuality => _localizabilityQuality
```

</div>

</div>

The localizability quality gives information about the chances of a successful localization in this [CoverageArea](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/CoverageArea/).

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### Centroid<a href="#Centroid" class="hash-link" aria-label="Direct link to Centroid" title="Direct link to Centroid">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
LatLng Centroid
```

</div>

</div>

Centroid of the Shape polygon.

</div>

</div>
