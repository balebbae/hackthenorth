---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningTangentialTransform/
title: class ARWorldPositioningTangentialTransform
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class ARWorldPositioningTangentialTransform

</div>

(Niantic.Lightship.AR.WorldPositioning.ARWorldPositioningTangentialTransform)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The [ARWorldPositioningTangentialTransform](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningTangentialTransform/) class represents a transform from a Euclidean tangential coordinate system to geographic coordinates and provides methods to convert between the two.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class ARWorldPositioningTangentialTransform {
 public:
       // fields
    
      Matrix4x4 TangentialToEUN;
      double OriginLatitude;
        double OriginLongitude;
       double OriginAltitude;
        static double DEGREES_TO_METRES = 111139.0;
      static double METRES_TO_DEGREES = 1.0 / DEGREES_TO_METRES;

      // methods
   
     ARWorldPositioningTangentialTransform();
   
     ARWorldPositioningTangentialTransform(
           Matrix4x4 tangentialToEUN,
          double originLatitude,
            double originLongitude,
           double originAltitude
       );
    
     void WorldToTangential(
         double latitudeDegrees,
           double longitudeDegrees,
          double altitudeMetres,
            Quaternion worldRotationEUN,
            out Vector3 tangentialTranslationRUF,
         out Quaternion tangentialRotationRUF
        );
    
     void WorldToTangential(
         double latitudeDegrees,
           double longitudeDegrees,
          double altitudeMetres,
            out Vector3 tangentialTranslationRUF
        );
    
     void TangentialToWorld(
         Vector3 tangentialTranslationRUF,
           Quaternion tangentialRotationRUF,
           out double latitudeDegrees,
         out double longitudeDegrees,
            out double altitudeMetres,
          out Quaternion worldRotationEUN
     );
    
     void TangentialToWorld(
         Transform tangentialPose,
           out double latitudeDegrees,
         out double longitudeDegrees,
            out double altitudeMetres,
          out Quaternion worldRotationEUN
     );
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The [ARWorldPositioningTangentialTransform](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningTangentialTransform/) class represents a transform from a Euclidean tangential coordinate system to geographic coordinates and provides methods to convert between the two.

It is common to approximate world geographic coordinates within a small region using a tangential Euclidean coordinate system. WPS uses this class to represent the transform between the [AR](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/) tracking tangential coordinates and world geographic coordinates. [ARWorldPositioningTangentialTransform](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningTangentialTransform/) can also be used to convert any map data which is provided in a tangential coordinate system. The representation is similar to that used by GeoPose but with a left-handed East-Up-North coordinate system to align with Unity rather than the East-North-Up coordinate system defined in the GeoPose standard.

TangentialToEUN the matrix transform from local tangential coordinates to tangential EUN (East-Up-North) coordinates

originLatitude the latitude of the origin for the tangential world coordinate system

originLongitude the longitude of the origin for the tangential world coordinate system

originAltitude the altitude of the origin for the tangential world coordinate system

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### ARWorldPositioningTangentialTransform<a href="#ARWorldPositioningTangentialTransform" class="hash-link" aria-label="Direct link to ARWorldPositioningTangentialTransform" title="Direct link to ARWorldPositioningTangentialTransform">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ARWorldPositioningTangentialTransform(
       Matrix4x4 tangentialToEUN,
      double originLatitude,
        double originLongitude,
       double originAltitude
   )
```

</div>

</div>

Creates a new [ARWorldPositioningTangentialTransform](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/WorldPositioning/ARWorldPositioningTangentialTransform/)

    **Parameters**:

    `tangentialToEUN` - the matrix transform from local tangential coordinates to tangential EUN (East-Up-North) coordinates

    `originLatitude` - the latitude of the origin for the tangential world coordinate system

    `originLongitude` - the longitude of the origin for the tangential world coordinate system

    `originAltitude` - the altitude of the origin for the tangential world coordinate system

#### WorldToTangential<a href="#WorldToTangential" class="hash-link" aria-label="Direct link to WorldToTangential" title="Direct link to WorldToTangential">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void WorldToTangential(
     double latitudeDegrees,
       double longitudeDegrees,
      double altitudeMetres,
        Quaternion worldRotationEUN,
        out Vector3 tangentialTranslationRUF,
     out Quaternion tangentialRotationRUF
    )
```

</div>

</div>

Converts a pose in world geographic coordinates to a pose in the tangential Euclidean coordinate system

    **Parameters**:

    `latitudeDegrees` - The latitude of the object measured in degrees

    `longitudeDegrees` - The longitude of the object measured in degrees

    `altitudeMetres` - The altitude of the object measured in metres above sea level

    `worldRotationEUN` - The rotation of the object relative to East-Up-North axes

    `tangentialTranslationRUF` - The corresponding translation in the tangential Euclidean coordinate system

    `tangentialRotationRUF` - The corresponding rotation in the tangential Euclidean coordinate system

#### WorldToTangential<a href="#WorldToTangential" class="hash-link" aria-label="Direct link to WorldToTangential" title="Direct link to WorldToTangential">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void WorldToTangential(
     double latitudeDegrees,
       double longitudeDegrees,
      double altitudeMetres,
        out Vector3 tangentialTranslationRUF
    )
```

</div>

</div>

Converts a position in world geographic coordinates to a position in the tangential Euclidean coordinate system

    **Parameters**:

    `latitudeDegrees` - The latitude of the object measured in degrees

    `longitudeDegrees` - The longitude of the object measured in degrees

    `altitudeMetres` - The altitude of the object measured in metres above sea level

    `tangentialTranslationRUF` - The corresponding rotation in the tangential Euclidean coordinate system

#### TangentialToWorld<a href="#TangentialToWorld" class="hash-link" aria-label="Direct link to TangentialToWorld" title="Direct link to TangentialToWorld">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void TangentialToWorld(
     Vector3 tangentialTranslationRUF,
       Quaternion tangentialRotationRUF,
       out double latitudeDegrees,
     out double longitudeDegrees,
        out double altitudeMetres,
      out Quaternion worldRotationEUN
 )
```

</div>

</div>

Converts a position in the tangential Euclidean coordinate system to a position in world geographic coordinates

    **Parameters**:

    `tangentialTranslationRUF` - The translation in the tangential Euclidean coordinate system

    `tangentialRotationRUF` - The rotation in the tangential Euclidean coordinate system

    `latitudeDegrees` - The corresponding latitude of the object measured in degrees

    `longitudeDegrees` - The corresponding longitude of the object measured in degrees

    `altitudeMetres` - The corresponding altitude of the object measured in metres above sea level

    `worldRotationEUN` - The rotation of the object relative to East-Up-North axes

#### TangentialToWorld<a href="#TangentialToWorld" class="hash-link" aria-label="Direct link to TangentialToWorld" title="Direct link to TangentialToWorld">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void TangentialToWorld(
     Transform tangentialPose,
       out double latitudeDegrees,
     out double longitudeDegrees,
        out double altitudeMetres,
      out Quaternion worldRotationEUN
 )
```

</div>

</div>

Converts a position in the tangential Euclidean coordinate system to a position in world geographic coordinates

    **Parameters**:

    `tangentialPose` - The pose of the object in the local tangential Euclidean coordinate system

    `latitudeDegrees` - The corresponding latitude of the object measured in degrees

    `longitudeDegrees` - The corresponding longitude of the object measured in degrees

    `altitudeMetres` - The corresponding altitude of the object measured in metres above sea level

    `worldRotationEUN` - The rotation of the object relative to East-Up-North axes

</div>

</div>
