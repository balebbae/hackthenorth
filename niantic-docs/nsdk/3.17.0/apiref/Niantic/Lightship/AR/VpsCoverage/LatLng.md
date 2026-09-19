---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/LatLng/
title: struct LatLng
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct LatLng

</div>

(Niantic.Lightship.AR.VpsCoverage.LatLng)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

The [LatLng](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/LatLng/) struct represents a Latitude and Longitude pair and provides functionality for comparing [LatLng](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/LatLng/) instances with each other.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
   struct LatLng: IEquatable< LatLng > {
     // fields
    
      double Latitude => lat_degrees;
         double Longitude => lng_degrees;

       // methods
   
     LatLng(double latitude, double longtitude);
        LatLng(LocationInfo locationInfo);
      bool Equals(LatLng other);
     override int GetHashCode();
     override string ToString();
     override bool Equals(object obj);
      double Distance(LatLng other);
     LatLng Add(double bearing, double distance);
        LatLng ToRadian();
      LatLng ToDegrees();
     static double Distance(LatLng l1, LatLng l2);
       static double Bearing(LatLng l1, LatLng l2);
        static bool operator == (LatLng l1, LatLng l2);
     static bool operator != (LatLng l1, LatLng l2);
 };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

The [LatLng](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/LatLng/) struct represents a Latitude and Longitude pair and provides functionality for comparing [LatLng](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/VpsCoverage/LatLng/) instances with each other.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### Distance<a href="#Distance" class="hash-link" aria-label="Direct link to Distance" title="Direct link to Distance">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
double Distance(LatLng other)
```

</div>

</div>

Calculates "as-the-crow-flies" distance between points using the Haversine formula.

    **Returns:**

    Distance between points in meters.

#### Add<a href="#Add" class="hash-link" aria-label="Direct link to Add" title="Direct link to Add">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
LatLng Add(double bearing, double distance)
```

</div>

</div>

    **Parameters**:

    `bearing` - Bearing in degrees, clockwise from north

    `distance` - Distance travelled in meters

#### Distance<a href="#Distance" class="hash-link" aria-label="Direct link to Distance" title="Direct link to Distance">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static double Distance(LatLng l1, LatLng l2)
```

</div>

</div>

Calculates "as-the-crow-flies" distance between points using the Haversine formula.

    **Returns:**

    Distance between points in meters.

#### Bearing<a href="#Bearing" class="hash-link" aria-label="Direct link to Bearing" title="Direct link to Bearing">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static double Bearing(LatLng l1, LatLng l2)
```

</div>

</div>

Calculates the initial bearing (sometimes referred to as forward azimuth) which if followed in a straight line along a great-circle arc will take you from the l1 to l2 points.

    **Returns:**

    Initial bearing in degrees

</div>

</div>
