---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/GridNode/
title: struct GridNode
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct GridNode

</div>

(Niantic.Lightship.AR.NavigationMesh.GridNode)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Encloses data for grid elements used during scanning for walkable areas.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   struct GridNode: IEquatable< GridNode > {
     // fields
    
      readonly Vector2Int Coordinates;
      float Elevation;
      float Deviation;
      float DiffFromNeighbour;

     // methods
   
     GridNode(Vector2Int coordinates);
       bool Equals(GridNode other);
       override int GetHashCode();
     override bool Equals(object obj);
      static bool operator == (GridNode left, GridNode right);
        static bool operator != (GridNode left, GridNode right);
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Encloses data for grid elements used during scanning for walkable areas.

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### Coordinates<a href="#Coordinates" class="hash-link" aria-label="Direct link to Coordinates" title="Direct link to Coordinates">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly Vector2Int Coordinates
```

</div>

</div>

Coordinates of this node on the grid.

#### Elevation<a href="#Elevation" class="hash-link" aria-label="Direct link to Elevation" title="Direct link to Elevation">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float Elevation
```

</div>

</div>

Height of the node.

#### Deviation<a href="#Deviation" class="hash-link" aria-label="Direct link to Deviation" title="Direct link to Deviation">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float Deviation
```

</div>

</div>

Standard deviation in the area around the node.

#### DiffFromNeighbour<a href="#DiffFromNeighbour" class="hash-link" aria-label="Direct link to DiffFromNeighbour" title="Direct link to DiffFromNeighbour">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float DiffFromNeighbour
```

</div>

</div>

The calculated minimum difference in elevation from a neighbouring node.

</div>

</div>
