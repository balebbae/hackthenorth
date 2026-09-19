---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.NSDKResult/
title: NSDKResult
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk/ "com.nianticspatial.nsdk") 

</div>

<div class="api-title">

#  NSDKResult 

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line api-obsolete"><span class="ctoken keyword">sealed</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">NSDKResult</span><span class="ctoken punctuation">\<</span><span class="ctoken class-name keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name">TData</span><span class="ctoken punctuation">,</span><span class="ctoken plain"> </span><span class="ctoken class-name keyword">out</span><span class="ctoken plain"> </span><span class="ctoken class-name">TError</span><span class="ctoken plain"> </span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[ErrorCodeProvider](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ErrorCodeProvider/ "Browse to ErrorCodeProvider")</span><span class="ctoken punctuation">\></span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

ResultDeprecated wrapper for NSDK operations that can succeed or fail. NSDKResult is a Kotlin sealed class designed to provide a type-safe abstraction over the return values of low-level C APIs. Instead of directly handling raw integer status codes from the C layer, Kotlin callers receive structured results as either Success or Error.

## Samples<a href="#samples" class="hash-link" aria-label="Direct link to Samples" title="Direct link to Samples">​</a>

<div class="language-kotlin codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` kotlin
val result = NSDK.getVpsDevicePoseAsGeolocation(handle, pose)
when (result) {
    is NSDKResult.Success -> {
        val location = result.value
    }
    is NSDKResult.Error -> {
        println("Failed to track anchor: $result.code")
    }
}
```

</div>

</div>

------------------------------------------------------------------------

</div>

</div>
