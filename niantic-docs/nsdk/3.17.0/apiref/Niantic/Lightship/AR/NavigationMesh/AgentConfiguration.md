---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/AgentConfiguration/
title: struct AgentConfiguration
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct AgentConfiguration

</div>

(Niantic.Lightship.AR.NavigationMesh.AgentConfiguration)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
struct AgentConfiguration {
       // fields
    
      readonly float JumpDistance;
        readonly int JumpPenalty;
       readonly PathFindingBehaviour Behaviour;

     // methods
   
     AgentConfiguration(
          int jumpPenalty,
          float jumpDistance,
           PathFindingBehaviour behaviour
        );
    
     static AgentConfiguration CreateSimpleAgent();
        static AgentConfiguration CreateJumpingAgent(PathFindingBehaviour pathFindingBehaviour = PathFindingBehaviour.InterSurfacePreferResults);
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

### Fields<a href="#fields" class="hash-link" aria-label="Direct link to Fields" title="Direct link to Fields">​</a>

#### JumpDistance<a href="#JumpDistance" class="hash-link" aria-label="Direct link to JumpDistance" title="Direct link to JumpDistance">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly float JumpDistance
```

</div>

</div>

The maximum distance an agent can jump in meters.

#### JumpPenalty<a href="#JumpPenalty" class="hash-link" aria-label="Direct link to JumpPenalty" title="Direct link to JumpPenalty">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly int JumpPenalty
```

</div>

</div>

Determines the cost of jumping.

.. note::

This is an added cost for steps taken 'off-surface'. @discussion Being off-surface includes steps taken at the jumping off point and steps taken mid-jump. If there is a 1 cell block between the start and the destination, assuming going around takes ~3 points, then jumping over with no penalty will cost 2 points, jumping over with 1 penalty will cost 3 points, and so on... If there is a gap between the two surfaces, the cost of jumping will aggregate with each step until the agent lands on a surface.

#### Behaviour<a href="#Behaviour" class="hash-link" aria-label="Direct link to Behaviour" title="Direct link to Behaviour">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
readonly PathFindingBehaviour Behaviour
```

</div>

</div>

Determines how the agent should behave when its destination is on a foreign surface.

</div>

</div>
