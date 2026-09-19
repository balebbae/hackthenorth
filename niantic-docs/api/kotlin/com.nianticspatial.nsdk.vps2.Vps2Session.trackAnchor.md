---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session.trackAnchor/
title: trackAnchor
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.vps2](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2/ "com.nianticspatial.nsdk.vps2") <span class="api-breadcrumbs-nav">←</span>[Vps2Session](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.vps2.Vps2Session/ "com.nianticspatial.nsdk.vps2.Vps2Session") 

</div>

<div class="api-title">

#  trackAnchor

<div class="api-package">

Start tracking an anchor specified by a base64 payload.

</div>

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">fun</span><span class="ctoken plain"> </span><span class="ctoken class-name">trackAnchor</span><span class="ctoken punctuation">(</span><span class="ctoken plain">payload</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string" target="_blank" rel="noopener noreferrer" title="Opens an external reference">String</a></span><span class="ctoken punctuation">)</span><span class="ctoken punctuation">:</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array" target="_blank" rel="noopener noreferrer" title="Opens an external reference">UUID</a></span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Start tracking an anchor specified by a base64 payload.

</div>

#### Returns<a href="#returns" class="hash-link" aria-label="Direct link to Returns" title="Direct link to Returns">​</a>

<div class="ctoken comment">

The anchor's unique id — an NSDK `UUID` (`typealias UUID = ByteArray`, a 32-byte ASCII uppercase-hex id, not `java.util.UUID`). Use `anchorIdToString` for a printable string.

</div>

#### Throws<a href="#throws" class="hash-link" aria-label="Direct link to Throws" title="Direct link to Throws">​</a>

- `NsdkInvalidArgumentStatusException` — if the payload is invalid. Check NSDK's C logs for more information.

------------------------------------------------------------------------

</div>

</div>
