---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession.configure/
title: configure
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.scanning](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning/ "com.nianticspatial.nsdk.scanning") <span class="api-breadcrumbs-nav">←</span>[ScanningSession](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.scanning.ScanningSession/ "com.nianticspatial.nsdk.scanning.ScanningSession") 

</div>

<div class="api-title">

#  configure

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">configure</span><span class="ctoken punctuation">(</span><span class="ctoken plain">config</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name">[ScannerConfig](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.ScannerConfig/ "Configuration parameters for scanning functionality....")</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Configure the session with the specified settings.

\

\> Note: It is only valid to call this when the session is stopped.\
\> Note: Configuration is asynchronous and can fail later, even if this call\
does not throw an error. Use `getFeatureStatus()` to check there are no issues.

</div>

#### See also<a href="#see-also" class="hash-link" aria-label="Direct link to See also" title="Direct link to See also">​</a>

- ScannerConfig

------------------------------------------------------------------------

</div>

</div>
