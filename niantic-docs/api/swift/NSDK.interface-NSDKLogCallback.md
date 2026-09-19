---
source: https://www.nianticspatial.com/docs/api/swift/NSDK.interface-NSDKLogCallback/
title: NSDKLogCallback
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/swift/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NSDK](https://www.nianticspatial.com/docs/api/swift/NSDK/ "NSDK") 

</div>

<div class="api-title">

#  NSDKLogCallback

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">protocol</span><span class="ctoken plain"> </span><span class="ctoken class-name">NSDKLogCallback</span><span class="ctoken plain"> : AnyObject</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Protocol for receiving log messages from NSDK. Implement this protocol to receive NSDK log messages in your application. The callback will be invoked on background threads, so ensure your implementation is thread-safe.

## Example Usage<a href="#example-usage" class="hash-link" aria-label="Direct link to Example Usage" title="Direct link to Example Usage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
class MyLogCallback: NSDKLogCallback {
    func onLog(level: NSDKLogLevel, message: String, fileName: String?, fileLine: Int, funcName: String?) {
        let levelStr = level.description
        let location = fileName.map { "\($0):\(fileLine)" } ?? ""
        let funcInfo = funcName.map { " \($0)" } ?? ""
        print("[NSDK-\(levelStr)] \(location)\(funcInfo): \(message)")
    }
}
let callback = MyLogCallback()
let session = NSDKSession(apiKey: "your-key", logCallback: callback)
```

</div>

</div>

------------------------------------------------------------------------

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

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
<td><span id="method-onlog"></span><span class="ctoken-line"><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/swift/NSDK.NSDKLogCallback.method-onLog/" title="Called when NSDK generates a log message.">onLog</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Called when NSDK generates a log message.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
