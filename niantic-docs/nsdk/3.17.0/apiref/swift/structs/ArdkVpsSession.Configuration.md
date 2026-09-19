---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/ArdkVpsSession.Configuration/
title: ArdkVpsSession.Configuration
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `ArdkVpsSession.Configuration`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
struct Configuration
```

</div>

</div>

Configuration structure for the VPS session.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `continuousLocalizationEnabled`<a href="#continuouslocalizationenabled" class="hash-link" aria-label="Direct link to continuouslocalizationenabled" title="Direct link to continuouslocalizationenabled">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var continuousLocalizationEnabled: Bool
```

</div>

</div>

Whether to enable continuous localization.

This will continuously send localization requests to the VPS server even after the first successful localization response has been received. These results will help refine the position of the anchor over time. This will also help mitigate AR tracking drift.

- Attention: This will increase the bandwidth used by the VPS feature.
- Attention: This will also cause anchored objects to move in the scene as their positions are refined.
- Attention: This is disabled in the default configuration.

See `cloudLocalizerContinuousRequestsPerSecond` to define the frequency of the requests.

### `temporalFusionEnabled`<a href="#temporalfusionenabled" class="hash-link" aria-label="Direct link to temporalfusionenabled" title="Direct link to temporalfusionenabled">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var temporalFusionEnabled: Bool
```

</div>

</div>

Whether to enable temporal fusion.

This will combine the results of successive localizations over time to provide a more stable result. This will help mitigate AR tracking drift. This requires that continuous localization is enabled.

Enabling temporal fusion will generate more stable results, but it will also take longer to resolve tracking drift compared to only taking the latest localization result.

- Attention: This is disabled in the default configuration.

### `interpolationEnabled`<a href="#interpolationenabled" class="hash-link" aria-label="Direct link to interpolationenabled" title="Direct link to interpolationenabled">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var interpolationEnabled: Bool
```

</div>

</div>

Whether to enable interpolation.

This will interpolate the position of the anchor over time to provide a smoother result. Anchor updates will be surfaced as sequential smooth updates rather than a single update at the latest localization result.

- Attention: This is disabled in the default configuration.

### `cloudLocalizerInitialRequestsPerSecond`<a href="#cloudlocalizerinitialrequestspersecond" class="hash-link" aria-label="Direct link to cloudlocalizerinitialrequestspersecond" title="Direct link to cloudlocalizerinitialrequestspersecond">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var cloudLocalizerInitialRequestsPerSecond: Float
```

</div>

</div>

Defines the number of localization requests per second which are sent to the VPS server prior to the first successful localization.

This is 1.0f in the default configuration.

### `cloudLocalizerContinuousRequestsPerSecond`<a href="#cloudlocalizercontinuousrequestspersecond" class="hash-link" aria-label="Direct link to cloudlocalizercontinuousrequestspersecond" title="Direct link to cloudlocalizercontinuousrequestspersecond">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var cloudLocalizerContinuousRequestsPerSecond: Float
```

</div>

</div>

Defines the number of localization requests per second which are sent to the VPS server after the first successful localization. This is only used if continuous localization is enabled.

This is 0.2f in the default configuration (one request every 5 seconds).

### `cloudTemporalFusionWindowSize`<a href="#cloudtemporalfusionwindowsize" class="hash-link" aria-label="Direct link to cloudtemporalfusionwindowsize" title="Direct link to cloudtemporalfusionwindowsize">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var cloudTemporalFusionWindowSize: UInt32
```

</div>

</div>

Defines the number of entries that are considered for temporal fusion in cloud localization.

This config option is currently disabled

### `jpegCompressionQuality`<a href="#jpegcompressionquality" class="hash-link" aria-label="Direct link to jpegcompressionquality" title="Direct link to jpegcompressionquality">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var jpegCompressionQuality: UInt32
```

</div>

</div>

Defines the quality of the JPEG compression used for the camera image sent to the VPS server as part of a localization request. Lower values will result in lower bandwidth usage.

We have benchmarked that 50-90 quality for jpeg compression does not significantly impact the accuracy of the localization results.

This is 70 in the default configuration.

### `gpsCorrectionForContinuousLocalization`<a href="#gpscorrectionforcontinuouslocalization" class="hash-link" aria-label="Direct link to gpscorrectionforcontinuouslocalization" title="Direct link to gpscorrectionforcontinuouslocalization">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var gpsCorrectionForContinuousLocalization: Bool
```

</div>

</div>

Whether to enable GPS correction for continuous localization.

This will download additional GPS graph data from the VPS server to help correct the GPS location of the device. This is useful for refining device GPS location after localization.

### `deviceMapLocalizationEnabled`<a href="#devicemaplocalizationenabled" class="hash-link" aria-label="Direct link to devicemaplocalizationenabled" title="Direct link to devicemaplocalizationenabled">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var deviceMapLocalizationEnabled: Bool
```

</div>

</div>

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(continuousLocalizationEnabled:temporalFusionEnabled:interpolationEnabled:cloudLocalizerInitialRequestsPerSecond:cloudLocalizerContinuousRequestsPerSecond:cloudTemporalFusionWindowSize:jpegCompressionQuality:gpsCorrectionForContinuousLocalization:deviceMapLocalizationEnabled:)`<a href="#initcontinuouslocalizationenabledtemporalfusionenabledinterpolationenabledcloudlocalizerinitialrequestspersecondcloudlocalizercontinuousrequestspersecondcloudtemporalfusionwindowsizejpegcompressionqualitygpscorrectionforcontinuouslocalizationdevicemaplocalizationenabled" class="hash-link" aria-label="Direct link to initcontinuouslocalizationenabledtemporalfusionenabledinterpolationenabledcloudlocalizerinitialrequestspersecondcloudlocalizercontinuousrequestspersecondcloudtemporalfusionwindowsizejpegcompressionqualitygpscorrectionforcontinuouslocalizationdevicemaplocalizationenabled" title="Direct link to initcontinuouslocalizationenabledtemporalfusionenabledinterpolationenabledcloudlocalizerinitialrequestspersecondcloudlocalizercontinuousrequestspersecondcloudtemporalfusionwindowsizejpegcompressionqualitygpscorrectionforcontinuouslocalizationdevicemaplocalizationenabled">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(continuousLocalizationEnabled: Bool = false,
            temporalFusionEnabled: Bool = false,
            interpolationEnabled: Bool = false,
            cloudLocalizerInitialRequestsPerSecond: Float = 0,
            cloudLocalizerContinuousRequestsPerSecond: Float = 0,
            cloudTemporalFusionWindowSize: UInt32 = 0,
            jpegCompressionQuality: UInt32 = 0,
            gpsCorrectionForContinuousLocalization: Bool = true,
            deviceMapLocalizationEnabled: Bool = false)
```

</div>

</div>

</div>

</div>
