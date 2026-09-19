---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/enums/ArdkLogLevel/
title: ArdkLogLevel
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**ENUM**

<div>

# `ArdkLogLevel`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public enum ArdkLogLevel
```

</div>

</div>

Defines the available logging levels for ARDK.

`ArdkLogLevel` controls the verbosity of logging output from the ARDK system. Logging can be configured separately for stdout, files, and callback functions.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Log levels follow a hierarchical structure where higher levels include all messages from lower levels. For example, setting the level to `.warn` will include warning, error, and fatal messages, but exclude debug and info messages.

## Cases<a href="#cases" class="hash-link" aria-label="Direct link to Cases" title="Direct link to Cases">​</a>

### `all`<a href="#all" class="hash-link" aria-label="Direct link to all" title="Direct link to all">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case all
```

</div>

</div>

Logs all messages regardless of level.

This is the most verbose logging level and should only be used for debugging.

### `debug`<a href="#debug" class="hash-link" aria-label="Direct link to debug" title="Direct link to debug">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case debug
```

</div>

</div>

Logs debug messages and all higher priority messages.

Debug messages provide detailed information useful for development and troubleshooting.

### `info`<a href="#info" class="hash-link" aria-label="Direct link to info" title="Direct link to info">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case info
```

</div>

</div>

Logs informational messages and all higher priority messages.

Info messages provide general information about system operation and state changes.

### `warn`<a href="#warn" class="hash-link" aria-label="Direct link to warn" title="Direct link to warn">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case warn
```

</div>

</div>

Logs warning messages and all higher priority messages.

Warning messages indicate potential issues that don't prevent operation but may affect performance or reliability.

### `error`<a href="#error" class="hash-link" aria-label="Direct link to error" title="Direct link to error">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case error
```

</div>

</div>

Logs error messages and fatal messages.

Error messages indicate problems that prevent normal operation or may cause unexpected behavior.

### `off`<a href="#off" class="hash-link" aria-label="Direct link to off" title="Direct link to off">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case off
```

</div>

</div>

Disables all logging output.

This level completely suppresses all log messages for maximum performance.

</div>

</div>
