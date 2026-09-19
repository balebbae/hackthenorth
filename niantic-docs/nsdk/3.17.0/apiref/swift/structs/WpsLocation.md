---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/WpsLocation/
title: WpsLocation
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `WpsLocation`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct WpsLocation: CustomStringConvertible
```

</div>

</div>

Contains world positioning data from the WPS (World Positioning System).

`WpsLocation` provides global positioning information that combines GPS/GNSS data with visual positioning for enhanced accuracy and reliability.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

WPS location data includes:

- Reference GPS coordinates (latitude, longitude, altitude)
- Transformation matrix for coordinate conversions
- Status information about positioning quality

## Example Usage<a href="#example-usage" class="hash-link" aria-label="Direct link to Example Usage" title="Direct link to Example Usage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
let (status, location) = wpsSession.latestLocation()
if status.isOk() {
    print("GPS Coordinates: \(location.referenceLatitudeDegrees), \(location.referenceLongitudeDegrees)")
    print("Altitude: \(location.referenceAltitudeMetres) meters")
    print("Status: \(location.status)")
    
    // Use the transformation matrix for coordinate conversions
    let worldPosition = location.trackingToRelativeEdn
    placeARContent(at: worldPosition)
}
```

</div>

</div>

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `referenceLatitudeDegrees`<a href="#referencelatitudedegrees" class="hash-link" aria-label="Direct link to referencelatitudedegrees" title="Direct link to referencelatitudedegrees">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let referenceLatitudeDegrees: Double
```

</div>

</div>

Reference latitude in degrees (WGS84 coordinate system).

This represents the GPS latitude of the reference point used for WPS positioning calculations.

### `referenceLongitudeDegrees`<a href="#referencelongitudedegrees" class="hash-link" aria-label="Direct link to referencelongitudedegrees" title="Direct link to referencelongitudedegrees">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let referenceLongitudeDegrees: Double
```

</div>

</div>

Reference longitude in degrees (WGS84 coordinate system).

This represents the GPS longitude of the reference point used for WPS positioning calculations.

### `referenceAltitudeMetres`<a href="#referencealtitudemetres" class="hash-link" aria-label="Direct link to referencealtitudemetres" title="Direct link to referencealtitudemetres">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let referenceAltitudeMetres: Double
```

</div>

</div>

Reference altitude in meters above sea level.

This represents the GPS altitude of the reference point used for WPS positioning calculations.

### `trackingToRelativeEdn`<a href="#trackingtorelativeedn" class="hash-link" aria-label="Direct link to trackingtorelativeedn" title="Direct link to trackingtorelativeedn">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public let trackingToRelativeEdn: simd_float4x4
```

</div>

</div>

Transformation matrix from tracking to relative coordinate system.

This 4x4 transformation matrix converts between the tracking coordinate system and the relative coordinate system used for AR content placement.

### `description`<a href="#description" class="hash-link" aria-label="Direct link to description" title="Direct link to description">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var description: String
```

</div>

</div>

</div>

</div>
