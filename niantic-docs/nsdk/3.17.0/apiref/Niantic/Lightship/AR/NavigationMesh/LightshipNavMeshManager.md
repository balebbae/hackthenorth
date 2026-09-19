---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMeshManager/
title: class LightshipNavMeshManager
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class LightshipNavMeshManager

</div>

(Niantic.Lightship.AR.NavigationMesh.LightshipNavMeshManager)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

[LightshipNavMeshManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMeshManager/) is a MonoBehaviour that will create a [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/) configured according to your settings and manage how it gets updated. You can add this component to a GameObject in your scene to use the [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/) features. You can pass this to any GameObject s that may need the [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/) e.g. your agents that handle moving across the board.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class LightshipNavMeshManager: MonoBehaviour {
  public:
       // fields
    
      bool _visualise = true;

      // properties
    
     LightshipNavMesh LightshipNavMesh;
  };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

[LightshipNavMeshManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMeshManager/) is a MonoBehaviour that will create a [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/) configured according to your settings and manage how it gets updated. You can add this component to a GameObject in your scene to use the [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/) features. You can pass this to any GameObject s that may need the [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/) e.g. your agents that handle moving across the board.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### LightshipNavMesh<a href="#LightshipNavMesh" class="hash-link" aria-label="Direct link to LightshipNavMesh" title="Direct link to LightshipNavMesh">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
LightshipNavMesh LightshipNavMesh
```

</div>

</div>

A reference to the [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/) that is being managed by this [LightshipNavMeshManager](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMeshManager/)

</div>

</div>
