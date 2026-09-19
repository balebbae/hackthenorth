---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/enums/WpsError/
title: WpsError
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**ENUM**

<div>

# `WpsError`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public enum WpsError: Error
```

</div>

</div>

Represents the current error status of the WPS (World Positioning System) feature.

## Cases<a href="#cases" class="hash-link" aria-label="Direct link to Cases" title="Direct link to Cases">​</a>

### `noGnss`<a href="#nognss" class="hash-link" aria-label="Direct link to nognss" title="Direct link to nognss">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case noGnss
```

</div>

</div>

No GPS data has been provided to the system.

### `trackingFailed`<a href="#trackingfailed" class="hash-link" aria-label="Direct link to trackingfailed" title="Direct link to trackingfailed">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case trackingFailed
```

</div>

</div>

WPS tracking has failed.

### `noHeading`<a href="#noheading" class="hash-link" aria-label="Direct link to noheading" title="Direct link to noheading">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case noHeading
```

</div>

</div>

No compass data has been provided to the system.

### `notInitialized`<a href="#notinitialized" class="hash-link" aria-label="Direct link to notinitialized" title="Direct link to notinitialized">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case notInitialized
```

</div>

</div>

WPS has not yet finished initializing.

</div>

</div>
