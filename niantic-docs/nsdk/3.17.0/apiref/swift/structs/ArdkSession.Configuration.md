---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/structs/ArdkSession.Configuration/
title: ArdkSession.Configuration
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**STRUCT**

<div>

# `ArdkSession.Configuration`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
struct Configuration
```

</div>

</div>

Configuration settings for initializing an ARDK session.

This struct encapsulates various configuration options including device info, cloud environment settings, user credentials, and logging preferences.

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

### `forceDisableCTrace`<a href="#forcedisablectrace" class="hash-link" aria-label="Direct link to forcedisablectrace" title="Direct link to forcedisablectrace">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var forceDisableCTrace: Bool
```

</div>

</div>

### `deviceInfo`<a href="#deviceinfo" class="hash-link" aria-label="Direct link to deviceinfo" title="Direct link to deviceinfo">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var deviceInfo: DeviceInfo
```

</div>

</div>

### `envConfig`<a href="#envconfig" class="hash-link" aria-label="Direct link to envconfig" title="Direct link to envconfig">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var envConfig: CloudEnvConfig
```

</div>

</div>

### `userConfig`<a href="#userconfig" class="hash-link" aria-label="Direct link to userconfig" title="Direct link to userconfig">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var userConfig: UserConfig
```

</div>

</div>

### `useLidar`<a href="#uselidar" class="hash-link" aria-label="Direct link to uselidar" title="Direct link to uselidar">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var useLidar: Bool
```

</div>

</div>

### `logCallback`<a href="#logcallback" class="hash-link" aria-label="Direct link to logcallback" title="Direct link to logcallback">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public var logCallback: ArdkLogCallback?
```

</div>

</div>

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `init(forceDisableCTrace:deviceInfo:envConfig:userConfig:useLidar:logCallback:)`<a href="#initforcedisablectracedeviceinfoenvconfiguserconfiguselidarlogcallback" class="hash-link" aria-label="Direct link to initforcedisablectracedeviceinfoenvconfiguserconfiguselidarlogcallback" title="Direct link to initforcedisablectracedeviceinfoenvconfiguserconfiguselidarlogcallback">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public init(
    forceDisableCTrace: Bool = false,
    deviceInfo: DeviceInfo = DeviceInfo(),
    envConfig: CloudEnvConfig = CloudEnvConfig(),
    userConfig: UserConfig = UserConfig(),
    useLidar: Bool = false,
    logCallback: ArdkLogCallback? = nil
)
```

</div>

</div>

</div>

</div>
