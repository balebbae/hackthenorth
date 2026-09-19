---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/classes/ArdkVpsCoverageSession/
title: ArdkVpsCoverageSession
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**CLASS**

<div>

# `ArdkVpsCoverageSession`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public final class ArdkVpsCoverageSession: ArdkSession.IDisposable
```

</div>

</div>

A session object for querying Visual Positioning System (VPS) coverage data related resources.

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `requestCoverageAreas(locationLatLng:searchRadius:timeout:pollingInterval:)`<a href="#requestcoverageareaslocationlatlngsearchradiustimeoutpollinginterval" class="hash-link" aria-label="Direct link to requestcoverageareaslocationlatlngsearchradiustimeoutpollinginterval" title="Direct link to requestcoverageareaslocationlatlngsearchradiustimeoutpollinginterval">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func requestCoverageAreas(
    locationLatLng latLng: LatLng,
    searchRadius radius: Int,
    timeout: TimeInterval = 60.0,
    pollingInterval: TimeInterval = 0.5
) async throws -> CoverageAreaResult
```

</div>

</div>

Requests VPS coverage areas within a specified radius around the given location.

Initiates a network request and suspends until the result is available, the operation fails, or the timeout is reached.

- Parameters:
  - locationLatLng: The center coordinates of the search area.
  - searchRadius: The radius in meters around the center to search for coverage areas.
  - timeout: Maximum time to wait for completion. Default is 60 seconds.
  - pollingInterval: Interval between completion checks. Default is 0.5 seconds.
- Returns: A `CoverageAreaResult` containing coverage area information.
- Throws:
  - `CancellationError` if the Task running this function was cancelled.
  - `TimeoutError` if the function timed out before it could complete execution.
  - `VpsCoverageResult.Error` if there was an error specific to the VPS Coverage query.

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| locationLatLng | The center coordinates of the search area. |
| searchRadius | The radius in meters around the center to search for coverage areas. |
| timeout | Maximum time to wait for completion. Default is 60 seconds. |
| pollingInterval | Interval between completion checks. Default is 0.5 seconds. |

### `requestLocalizationTargets(identifiers:timeout:pollingInterval:)`<a href="#requestlocalizationtargetsidentifierstimeoutpollinginterval" class="hash-link" aria-label="Direct link to requestlocalizationtargetsidentifierstimeoutpollinginterval" title="Direct link to requestlocalizationtargetsidentifierstimeoutpollinginterval">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func requestLocalizationTargets(
    identifiers targetIdentifiers: [String],
    timeout: TimeInterval = 60.0,
    pollingInterval: TimeInterval = 0.5
) async throws -> LocalizationTargetResult
```

</div>

</div>

Requests detailed information about specific localization targets.

Starts a network request for the given target identifiers and suspends until the request completes successfully, fails, or times out.

- Parameters:
  - targetIdentifiers: A list of localization target identifiers to query.
  - timeout: Maximum time to wait for completion. Default is 60 seconds.
  - pollingInterval: Interval between completion checks. Default is 0.5 seconds.
- Returns: A `LocalizationTargetResult` containing target details.
- Throws:
  - `CancellationError` if the Task running this function was cancelled.
  - `TimeoutError` if the function timed out before it could complete execution.
  - `VpsCoverageResult.Error` if there was an error specific to the VPS Coverage query.

#### Parameters<a href="#parameters-1" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| targetIdentifiers | A list of localization target identifiers to query. |
| timeout | Maximum time to wait for completion. Default is 60 seconds. |
| pollingInterval | Interval between completion checks. Default is 0.5 seconds. |

### `requestAreaTargets(locationLatLng:searchRadius:timeout:pollingInterval:)`<a href="#requestareatargetslocationlatlngsearchradiustimeoutpollinginterval" class="hash-link" aria-label="Direct link to requestareatargetslocationlatlngsearchradiustimeoutpollinginterval" title="Direct link to requestareatargetslocationlatlngsearchradiustimeoutpollinginterval">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func requestAreaTargets(
    locationLatLng latLng: LatLng,
    searchRadius radius: Int,
    timeout: TimeInterval = 60.0,
    pollingInterval: TimeInterval = 0.5
) async throws -> AreaTargetResult
```

</div>

</div>

Requests all available area targets within a specified radius.

Starts a network request to fetch nearby area targets and suspends until the operation completes, fails, or times out.

- Parameters:
  - locationLatLng: The center coordinates of the search area.
  - searchRadius: The radius in meters to search for area targets.
  - timeout: Maximum duration to wait for a result. Default is 60 seconds.
  - pollingInterval: Interval between progress checks. Default is 0.5 seconds.
- Returns: An `AreaTargetResult` containing area target data.
- Throws:
  - `CancellationError` if the Task running this function was cancelled.
  - `TimeoutError` if the function timed out before it could complete execution.
  - `VpsCoverageResult.Error` if there was an error specific to the VPS Coverage query.

#### Parameters<a href="#parameters-2" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| locationLatLng | The center coordinates of the search area. |
| searchRadius | The radius in meters to search for area targets. |
| timeout | Maximum duration to wait for a result. Default is 60 seconds. |
| pollingInterval | Interval between progress checks. Default is 0.5 seconds. |

### `requestHintImage(url:timeout:pollingInterval:)`<a href="#requesthintimageurltimeoutpollinginterval" class="hash-link" aria-label="Direct link to requesthintimageurltimeoutpollinginterval" title="Direct link to requesthintimageurltimeoutpollinginterval">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public func requestHintImage(
    url: String,
    timeout: TimeInterval = 60.0,
    pollingInterval: TimeInterval = 0.5
) async throws -> HintImageResult
```

</div>

</div>

Downloads the hint image associated with a localization target.

Starts a network request for the specified hint image URL and suspends until the operation completes, fails, or times out.

- Parameters:
  - url: The remote URL of the hint image to download.
  - timeout: Maximum duration to wait for completion. Default is 60 seconds.
  - pollingInterval: Interval between progress checks. Default is 0.5 seconds.
- Returns: A `HintImageResult` containing the downloaded image data.
- Throws:
  - `CancellationError` if the Task running this function was cancelled.
  - `TimeoutError` if the function timed out before it could complete execution.
  - `VpsCoverageResult.Error` if there was an error specific to the VPS Coverage query.

#### Parameters<a href="#parameters-3" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name | Description |
|----|----|
| url | The remote URL of the hint image to download. |
| timeout | Maximum duration to wait for completion. Default is 60 seconds. |
| pollingInterval | Interval between progress checks. Default is 0.5 seconds. |

</div>

</div>
