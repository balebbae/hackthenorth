---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/enums/CoverageArea.Localizability/
title: CoverageArea.Localizability
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**ENUM**

<div>

# `CoverageArea.Localizability`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
enum Localizability
```

</div>

</div>

Indicates the quality and reliability of VPS localization in a coverage area.

`Localizability` provides information about the expected quality and reliability of VPS localization within a specific coverage area, helping applications make informed decisions about VPS usage.

Different coverage areas may have varying levels of localization quality based on factors such as mapping completeness, feature density, and environmental conditions. This enum helps applications understand what to expect from VPS localization in different areas.

## Cases<a href="#cases" class="hash-link" aria-label="Direct link to Cases" title="Direct link to Cases">​</a>

### `unset`<a href="#unset" class="hash-link" aria-label="Direct link to unset" title="Direct link to unset">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case unset
```

</div>

</div>

Localizability quality is not specified.

The coverage area does not specify localization quality information. Applications should use default behavior or request additional information.

### `experimental`<a href="#experimental" class="hash-link" aria-label="Direct link to experimental" title="Direct link to experimental">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case experimental
```

</div>

</div>

Experimental localization quality.

The coverage area provides experimental VPS localization that may be less reliable or accurate than production-quality localization. Use with caution and implement appropriate fallback mechanisms.

### `production`<a href="#production" class="hash-link" aria-label="Direct link to production" title="Direct link to production">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case production
```

</div>

</div>

Production-quality localization.

The coverage area provides high-quality, reliable VPS localization suitable for production applications. This represents the best available localization quality.

</div>

</div>
