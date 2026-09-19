---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMeshAgentPathRenderer/
title: class LightshipNavMeshAgentPathRenderer
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class LightshipNavMeshAgentPathRenderer

</div>

(Niantic.Lightship.AR.NavigationMesh.LightshipNavMeshAgentPathRenderer)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

[LightshipNavMeshAgentPathRenderer](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMeshAgentPathRenderer/) is a debug renderer to show you the path a [LightshipNavMeshAgent](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMeshAgent/) is moving along while navigating the environment. You add it to the [LightshipNavMeshAgent](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMeshAgent/) GameObject in your scene and it will draw that agent's current path.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class LightshipNavMeshAgentPathRenderer: MonoBehaviour {
    public:
       // fields
    
      LightshipNavMeshAgent _agent;
       Material _material;
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

[LightshipNavMeshAgentPathRenderer](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMeshAgentPathRenderer/) is a debug renderer to show you the path a [LightshipNavMeshAgent](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMeshAgent/) is moving along while navigating the environment. You add it to the [LightshipNavMeshAgent](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMeshAgent/) GameObject in your scene and it will draw that agent's current path.

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### \_agent<a href="#_agent" class="hash-link" aria-label="Direct link to _agent" title="Direct link to _agent">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
LightshipNavMeshAgent _agent
```

</div>

</div>

The [LightshipNavMeshAgent](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMeshAgent/) that you want to render the path for.

#### \_material<a href="#_material" class="hash-link" aria-label="Direct link to _material" title="Direct link to _material">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Material _material
```

</div>

</div>

The Material used to render the path. This Material will be applied on a LineRenderer.

</div>

</div>
