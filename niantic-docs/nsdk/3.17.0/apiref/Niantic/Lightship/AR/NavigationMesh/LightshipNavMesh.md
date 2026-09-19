---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/
title: class LightshipNavMesh
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class LightshipNavMesh

</div>

(Niantic.Lightship.AR.NavigationMesh.LightshipNavMesh)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

This class manages the data structures associated with a navigation mesh ("LightshipNavMesh"). It dynamically builds a 2d grid on the meshes detected in the environment for running navigation algorithms on. You are able to retrieve a number of properties of the "LightshipNavMesh" from it. There are also a number of methods to help you place and move [LightshipNavMeshAgent](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMeshAgent/) s on the board.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class LightshipNavMesh {
  public:
       // properties
    
     ModelSettings Settings;
     float Area;
       List<Surface> Surfaces;

     // methods
   
     void Destroy();
       LightshipNavMesh(ModelSettings settings, bool visualise);
        bool IsOnNavMesh(Vector3 position, float delta);
    
     bool FindNearestFreePosition(
           Vector3 sourcePosition,
         float range,
          out Vector3 nearestPosition
     );
    
     bool FindRandomPosition(out Vector3 randomPosition);
 
     bool FindNearestFreePosition(
           Vector3 sourcePosition,
         out Vector3 nearestPosition
     );
    
     bool FindRandomPosition(
            Vector3 sourcePosition,
         float range,
          out Vector3 randomPosition
      );
    
     bool CheckFit(Vector3 center, float size);
      bool RayCast(Ray ray, out Vector3 hitPoint);
    
     bool CalculatePath(
         Vector3 fromPosition,
           Vector3 toPosition,
         AgentConfiguration agent,
           out Path path
       );
    
     void Scan(Vector3 origin, float range);
     void Clear();
     void Prune(Vector3 keepNodesOrigin, float range);
   };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

This class manages the data structures associated with a navigation mesh ("LightshipNavMesh"). It dynamically builds a 2d grid on the meshes detected in the environment for running navigation algorithms on. You are able to retrieve a number of properties of the "LightshipNavMesh" from it. There are also a number of methods to help you place and move [LightshipNavMeshAgent](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMeshAgent/) s on the board.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### Settings<a href="#Settings" class="hash-link" aria-label="Direct link to Settings" title="Direct link to Settings">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ModelSettings Settings
```

</div>

</div>

The configuration of the NavMeshModel.

#### Area<a href="#Area" class="hash-link" aria-label="Direct link to Area" title="Direct link to Area">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float Area
```

</div>

</div>

The discovered free area in square meters.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### LightshipNavMesh<a href="#LightshipNavMesh" class="hash-link" aria-label="Direct link to LightshipNavMesh" title="Direct link to LightshipNavMesh">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
LightshipNavMesh(ModelSettings settings, bool visualise)
```

</div>

</div>

Constructs a new [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/) using the parameters given.

    **Parameters**:

    `settings` - [Settings](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Settings/) to calibrate unoccupied area detection.

    `visualise` - Visualize the [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/) in the scene.

    **Returns:**

    Returns the newly created [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/).

#### IsOnNavMesh<a href="#IsOnNavMesh" class="hash-link" aria-label="Direct link to IsOnNavMesh" title="Direct link to IsOnNavMesh">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool IsOnNavMesh(Vector3 position, float delta)
```

</div>

</div>

Checks if a particular 3d position is on the [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/) (within a certain threshold).

    **Parameters**:

    `position` - The 3d position to check for.

    `delta` - The threshold distance from the [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/) to check against.

    **Returns:**

    true if the position provided is within delta meters of the [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/) grid plane.

#### Clear<a href="#Clear" class="hash-link" aria-label="Direct link to Clear" title="Direct link to Clear">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void Clear()
```

</div>

</div>

Removes all surfaces from the [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/).

</div>

</div>
