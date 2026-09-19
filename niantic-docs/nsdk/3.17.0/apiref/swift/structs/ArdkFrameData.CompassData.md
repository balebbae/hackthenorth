---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/ArdkFrameData.CompassData/
title: ArdkFrameData.CompassData
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `ArdkFrameData.CompassData`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public struct CompassData: Equatable
```

</div>

</div>

Compass and magnetometer data for heading information.

This structure contains orientation data from the device's compass, providing heading information that can be used for location-based AR experiences and waypoint navigation.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `timestampMs`<a href="#timestampms" class="hash-link" aria-label="Direct link to timestampms" title="Direct link to timestampms">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var timestampMs: UInt64
```

</div>

</div>

Timestamp when the compass reading was captured (in milliseconds).

### `headingAccuracy`<a href="#headingaccuracy" class="hash-link" aria-label="Direct link to headingaccuracy" title="Direct link to headingaccuracy">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var headingAccuracy: Float
```

</div>

</div>

Accuracy of the heading measurement (in degrees).

Lower values indicate more accurate readings. Values above 15-20 degrees may indicate poor compass calibration or magnetic interference.

### `trueHeading`<a href="#trueheading" class="hash-link" aria-label="Direct link to trueheading" title="Direct link to trueheading">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var trueHeading: Float
```

</div>

</div>

True heading relative to geographic north (in degrees).

This value is corrected for magnetic declination and represents the actual direction relative to true north (0-360 degrees).

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(timestampMs:headingAccuracy:trueHeading:)`<a href="#inittimestampmsheadingaccuracytrueheading" class="hash-link" aria-label="Direct link to inittimestampmsheadingaccuracytrueheading" title="Direct link to inittimestampmsheadingaccuracytrueheading">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(timestampMs: UInt64,
            headingAccuracy: Float,
            trueHeading: Float)
```

</div>

</div>

Creates compass data with the specified parameters.

- Parameters:
  - timestampMs: Timestamp of the compass reading in milliseconds
  - headingAccuracy: Accuracy of the heading measurement in degrees
  - trueHeading: True heading relative to geographic north in degrees

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name            | Description                                          |
|-----------------|------------------------------------------------------|
| timestampMs     | Timestamp of the compass reading in milliseconds     |
| headingAccuracy | Accuracy of the heading measurement in degrees       |
| trueHeading     | True heading relative to geographic north in degrees |

</div>

</div>
