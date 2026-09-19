---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/ModelSettings/
title: struct ModelSettings
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct ModelSettings

</div>

(Niantic.Lightship.AR.NavigationMesh.ModelSettings)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The [ModelSettings](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/ModelSettings/) struct provides a configuration for how [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/) scans the real environment and creates a navigable space. An instance of [ModelSettings](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/ModelSettings/) is created by the [LightshipNavMeshManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMeshManager/) using the parameters specified by the user in the Inspector, and that instance is subsequently used to create a [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/) that is configured this way.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
struct ModelSettings {
        // fields
    
      float TileSize;
       float SpatialChunkSize;
       int KernelSize;
       float KernelStdDevTol;
        float MaxSlope;
       float MinElevation;
       float StepHeight;
         LayerMask LayerMask;

       // properties
    
     ModelSettings Default;

      // methods
   
     ModelSettings(
           float tileSize,
           float kernelStdDevTol,
            float maxSlope,
           float stepHeight,
         LayerMask layerMask
       );
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The [ModelSettings](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/ModelSettings/) struct provides a configuration for how [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/) scans the real environment and creates a navigable space. An instance of [ModelSettings](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/ModelSettings/) is created by the [LightshipNavMeshManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMeshManager/) using the parameters specified by the user in the Inspector, and that instance is subsequently used to create a [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/) that is configured this way.

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### TileSize<a href="#TileSize" class="hash-link" aria-label="Direct link to TileSize" title="Direct link to TileSize">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float TileSize
```

</div>

</div>

Size of a grid cell in meters.

#### SpatialChunkSize<a href="#SpatialChunkSize" class="hash-link" aria-label="Direct link to SpatialChunkSize" title="Direct link to SpatialChunkSize">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float SpatialChunkSize
```

</div>

</div>

Size of a spatial partition in square meters. Grid cells within the same chunk will be stored together.

#### KernelSize<a href="#KernelSize" class="hash-link" aria-label="Direct link to KernelSize" title="Direct link to KernelSize">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
int KernelSize
```

</div>

</div>

The size of the kernel used to compute areal properties for each cell.

.. note::

This needs to be an odd integer.

#### KernelStdDevTol<a href="#KernelStdDevTol" class="hash-link" aria-label="Direct link to KernelStdDevTol" title="Direct link to KernelStdDevTol">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float KernelStdDevTol
```

</div>

</div>

The standard deviation tolerance value to use when determining node noise within a cell, outside of which the cell is considered too noisy to be walkable.

#### MaxSlope<a href="#MaxSlope" class="hash-link" aria-label="Direct link to MaxSlope" title="Direct link to MaxSlope">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float MaxSlope
```

</div>

</div>

Maximum slope angle (degrees) of an area to be considered flat.

#### MinElevation<a href="#MinElevation" class="hash-link" aria-label="Direct link to MinElevation" title="Direct link to MinElevation">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float MinElevation
```

</div>

</div>

Minimum elevation (meters) a [GridNode](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/GridNode/) is expected to have in order to be walkable

#### StepHeight<a href="#StepHeight" class="hash-link" aria-label="Direct link to StepHeight" title="Direct link to StepHeight">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float StepHeight
```

</div>

</div>

The maximum amount two cells can differ in elevation to be considered on the same plane.

#### LayerMask<a href="#LayerMask" class="hash-link" aria-label="Direct link to LayerMask" title="Direct link to LayerMask">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
LayerMask LayerMask
```

</div>

</div>

Specifies the layer of the environment to raycast.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### Default<a href="#Default" class="hash-link" aria-label="Direct link to Default" title="Direct link to Default">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ModelSettings Default
```

</div>

</div>

Constructs a configuration with default settings.

</div>

</div>
