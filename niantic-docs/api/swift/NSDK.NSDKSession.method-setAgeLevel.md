---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKSession.method-setAgeLevel/
title: setAgeLevel
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") <span class="api-breadcrumbs-nav">←</span>[NSDKSession](https://www.nianticspatial.com/docs/api/swift/NSDK.class-NSDKSession/ "NSDKSession") 

</div>

<div class="api-title">

#  setAgeLevel

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">func</span><span class="ctoken plain"> </span><span class="ctoken class-name">setAgeLevel</span><span class="ctoken plain">(</span><span class="ctoken plain">\_</span><span class="ctoken plain"> </span><span class="ctoken plain">ageLevel</span><span class="ctoken plain">: </span><span class="ctoken class-name">[AgeLevel](https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AgeLevel/ "Codes describing the age level of the user....")</span><span class="ctoken plain">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Sets the age level for the NSDK session.\
This method sets the age classification for the user

</div>

#### Example<a href="#example" class="hash-link" aria-label="Direct link to Example" title="Direct link to Example">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
session.setAgeLevel(.adult)
```

</div>

</div>

### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

<table class="api-table">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr class="api-table-row">
<td><span id="external parameter-agelevel"></span><span class="ctoken-line"><span class="ctoken class-name">ageLevel</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.enum-AgeLevel/" title="Codes describing the age level of the user....">AgeLevel</a></span></span></td>
<td><div class="ctoken comment">
The age level to set (unknown, minor, teen, or adult)
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
