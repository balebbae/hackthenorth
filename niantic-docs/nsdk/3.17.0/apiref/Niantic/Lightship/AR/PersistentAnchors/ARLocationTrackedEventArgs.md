---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/PersistentAnchors/ARLocationTrackedEventArgs/
title: struct ARLocationTrackedEventArgs
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct ARLocationTrackedEventArgs

</div>

(Niantic.Lightship.AR.PersistentAnchors.ARLocationTrackedEventArgs)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Event arguments for the ARLocationManager.locationTrackingStateChanged event.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
struct ARLocationTrackedEventArgs {
       // properties
    
     ARLocation ARLocation;
      bool Tracking;
        ARLocationTrackingStateReason TrackingStateReason;
      float TrackingConfidence;

     // methods
   
     ARLocationTrackedEventArgs(
          ARLocation arARLocation,
            bool tracking,
            ARLocationTrackingStateReason reason,
           float trackingConfidence = 0.0f
     );
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Event arguments for the ARLocationManager.locationTrackingStateChanged event.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### ARLocation<a href="#ARLocation" class="hash-link" aria-label="Direct link to ARLocation" title="Direct link to ARLocation">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ARLocation ARLocation
```

</div>

</div>

The ARLocation being tracked

#### Tracking<a href="#Tracking" class="hash-link" aria-label="Direct link to Tracking" title="Direct link to Tracking">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
bool Tracking
```

</div>

</div>

Whether or not the ARLocation is currently tracked

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### ARLocationTrackedEventArgs<a href="#ARLocationTrackedEventArgs" class="hash-link" aria-label="Direct link to ARLocationTrackedEventArgs" title="Direct link to ARLocationTrackedEventArgs">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ARLocationTrackedEventArgs(
      ARLocation arARLocation,
        bool tracking,
        ARLocationTrackingStateReason reason,
       float trackingConfidence = 0.0f
 )
```

</div>

</div>

Creates the args for ARLocation tracking

    **Parameters**:

    `arARLocation` - The ARLocation to track

    `tracking` - Whether or not the ARLocation is being tracked

    `reason` - If tracking is false, more information about why

    `trackingConfidence` - Positive number representing confidence we have in latest tracking update

</div>

</div>
