---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/ArdkFrameData.GpsData/
title: ArdkFrameData.GpsData
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `ArdkFrameData.GpsData`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct GpsData: Equatable
```

</div>

</div>

GPS location data for geographic positioning.

This structure contains location information from the device's GPS system, providing geographic coordinates and accuracy estimates for location-based AR features and location positioning.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `timestampMs`<a href="#timestampms" class="hash-link" aria-label="Direct link to timestampms" title="Direct link to timestampms">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var timestampMs: UInt64
```

</div>

</div>

Timestamp when the GPS reading was captured (in milliseconds).

### `latitude`<a href="#latitude" class="hash-link" aria-label="Direct link to latitude" title="Direct link to latitude">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var latitude: Double
```

</div>

</div>

Latitude coordinate in decimal degrees.

Positive values represent locations north of the equator, negative values represent locations south of the equator.

### `longitude`<a href="#longitude" class="hash-link" aria-label="Direct link to longitude" title="Direct link to longitude">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var longitude: Double
```

</div>

</div>

Longitude coordinate in decimal degrees.

Positive values represent locations east of the Prime Meridian, negative values represent locations west of the Prime Meridian.

### `altitude`<a href="#altitude" class="hash-link" aria-label="Direct link to altitude" title="Direct link to altitude">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var altitude: Double
```

</div>

</div>

Altitude above sea level in meters.

This value may be negative for locations below sea level. Accuracy depends on GPS signal quality and atmospheric conditions.

### `verticalAccuracy`<a href="#verticalaccuracy" class="hash-link" aria-label="Direct link to verticalaccuracy" title="Direct link to verticalaccuracy">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var verticalAccuracy: Float
```

</div>

</div>

Vertical accuracy of the altitude measurement in meters.

Lower values indicate more accurate altitude readings. GPS altitude is typically less accurate than horizontal position.

### `horizontalAccuracy`<a href="#horizontalaccuracy" class="hash-link" aria-label="Direct link to horizontalaccuracy" title="Direct link to horizontalaccuracy">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var horizontalAccuracy: Float
```

</div>

</div>

Horizontal accuracy of the position measurement in meters.

Lower values indicate more accurate position readings. Values under 5 meters are considered good accuracy for most AR applications.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(timestampMs:latitude:longitude:altitude:verticalAccuracy:horizontalAccuracy:)`<a href="#inittimestampmslatitudelongitudealtitudeverticalaccuracyhorizontalaccuracy" class="hash-link" aria-label="Direct link to inittimestampmslatitudelongitudealtitudeverticalaccuracyhorizontalaccuracy" title="Direct link to inittimestampmslatitudelongitudealtitudeverticalaccuracyhorizontalaccuracy">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(timestampMs: UInt64,
            latitude: Double,
            longitude: Double,
            altitude: Double,
            verticalAccuracy: Float,
            horizontalAccuracy: Float)
```

</div>

</div>

Creates GPS data with the specified location parameters.

- Parameters:
  - timestampMs: Timestamp of the GPS reading in milliseconds
  - latitude: Latitude in decimal degrees
  - longitude: Longitude in decimal degrees
  - altitude: Altitude above sea level in meters
  - verticalAccuracy: Vertical accuracy in meters
  - horizontalAccuracy: Horizontal accuracy in meters

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name               | Description                                  |
|--------------------|----------------------------------------------|
| timestampMs        | Timestamp of the GPS reading in milliseconds |
| latitude           | Latitude in decimal degrees                  |
| longitude          | Longitude in decimal degrees                 |
| altitude           | Altitude above sea level in meters           |
| verticalAccuracy   | Vertical accuracy in meters                  |
| horizontalAccuracy | Horizontal accuracy in meters                |

</div>

</div>
