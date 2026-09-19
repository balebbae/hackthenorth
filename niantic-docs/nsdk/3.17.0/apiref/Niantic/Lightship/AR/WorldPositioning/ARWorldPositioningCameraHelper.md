---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningCameraHelper/
title: class ARWorldPositioningCameraHelper
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class ARWorldPositioningCameraHelper

</div>

(Niantic.Lightship.AR.WorldPositioning.ARWorldPositioningCameraHelper)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

[ARWorldPositioningCameraHelper](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningCameraHelper/) provides information relating to the world position of a camera and implements 'Heads Down Mode' to improve user comfort during extended gameplay.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   class ARWorldPositioningCameraHelper: MonoBehaviour {
   public:
   
     enumCameraControlMode;

     // properties
    
     float TrueHeading;
        double Latitude;
      double Longitude;
     double Altitude;
      Quaternion RotationCameraRUFToWorldEUN;
     Vector3 Forward;
        CameraControlMode CameraMode;

       // methods
   
     void ToggleHeadsDownMode();
       void Awake();
     void OnDisable();
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

[ARWorldPositioningCameraHelper](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningCameraHelper/) provides information relating to the world position of a camera and implements 'Heads Down Mode' to improve user comfort during extended gameplay.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### TrueHeading<a href="#TrueHeading" class="hash-link" aria-label="Direct link to TrueHeading" title="Direct link to TrueHeading">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
float TrueHeading
```

</div>

</div>

The heading of the camera relative to true north, measured in degrees

#### Latitude<a href="#Latitude" class="hash-link" aria-label="Direct link to Latitude" title="Direct link to Latitude">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
double Latitude
```

</div>

</div>

The latitude of the camera, measured in degrees

#### Longitude<a href="#Longitude" class="hash-link" aria-label="Direct link to Longitude" title="Direct link to Longitude">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
double Longitude
```

</div>

</div>

The longitude of the camera, measured in degrees

#### Altitude<a href="#Altitude" class="hash-link" aria-label="Direct link to Altitude" title="Direct link to Altitude">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
double Altitude
```

</div>

</div>

The altitude of the camera, measured in metres above sea level

#### RotationCameraRUFToWorldEUN<a href="#RotationCameraRUFToWorldEUN" class="hash-link" aria-label="Direct link to RotationCameraRUFToWorldEUN" title="Direct link to RotationCameraRUFToWorldEUN">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Quaternion RotationCameraRUFToWorldEUN
```

</div>

</div>

The rotation from camera coordinates (Right-Up-Forwards) to global geographic coordinates (East-Up-North)

#### Forward<a href="#Forward" class="hash-link" aria-label="Direct link to Forward" title="Direct link to Forward">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Vector3 Forward
```

</div>

</div>

The camera forward vector in global geographic coordinates (East-Up-North)

#### CameraMode<a href="#CameraMode" class="hash-link" aria-label="Direct link to CameraMode" title="Direct link to CameraMode">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
CameraControlMode CameraMode
```

</div>

</div>

The CameraMode The selected CameraControlMode for the camera

</div>

</div>
