---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMeshAgent/
title: class LightshipNavMeshAgent
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class LightshipNavMeshAgent

</div>

(Niantic.Lightship.AR.NavigationMesh.LightshipNavMeshAgent)

[LightshipNavMeshAgent](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMeshAgent/) is an example agent implementation that navigates a [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/) based on logic programmed here. You place this MonoBehaviour on a GameObject to have that GameObject navigate autonomously through your real environment. You can create new versions of this to change how your creatures navigate the [LightshipNavMesh](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/NavigationMesh/LightshipNavMesh/). For example you may want to use physics/forces or add splines rather than straight lines. This is a basic example that uses linear interpolation and coroutines.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class LightshipNavMeshAgent: MonoBehaviour {
    public:
   
     enumAgentNavigationState;

      // properties
    
     AgentNavigationState State;
     Path path;

      // methods
   
     void StopMoving();
        void SetDestination(Vector3 destination);
  };
```

</div>

</div>

</div>

</div>
