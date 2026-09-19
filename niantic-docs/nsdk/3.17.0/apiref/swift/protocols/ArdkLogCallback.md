---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/protocols/ArdkLogCallback/
title: ArdkLogCallback
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**PROTOCOL**

<div>

# `ArdkLogCallback`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
public protocol ArdkLogCallback: AnyObject
```

</div>

</div>

Protocol for receiving log messages from ARDK.

Implement this protocol to receive ARDK log messages in your application. The callback will be invoked on background threads, so ensure your implementation is thread-safe.

## Example Usage<a href="#example-usage" class="hash-link" aria-label="Direct link to Example Usage" title="Direct link to Example Usage">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
class MyLogCallback: ArdkLogCallback {
    func onLog(level: ArdkLogLevel, message: String, fileName: String?, fileLine: Int, funcName: String?) {
        let levelStr = level.description
        let location = fileName.map { "\($0):\(fileLine)" } ?? ""
        let funcInfo = funcName.map { " \($0)" } ?? ""
        print("[ARDK-\(levelStr)] \(location)\(funcInfo): \(message)")
    }
}

let callback = MyLogCallback()
let session = ArdkSession(apiKey: "your-key", logCallback: callback)
```

</div>

</div>

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

### `onLog(level:message:fileName:fileLine:funcName:)`<a href="#onloglevelmessagefilenamefilelinefuncname" class="hash-link" aria-label="Direct link to onloglevelmessagefilenamefilelinefuncname" title="Direct link to onloglevelmessagefilenamefilelinefuncname">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
func onLog(level: ArdkLogLevel, message: String, fileName: String?, fileLine: Int, funcName: String?)
```

</div>

</div>

Called when ARDK generates a log message.

- Parameters:
  - level: The severity level of the log message
  - message: The log message content
  - fileName: Optional source file name where the log was generated
  - fileLine: Line number in the source file
  - funcName: Optional function name where the log was generated

#### Parameters<a href="#parameters" class="hash-link" aria-label="Direct link to Parameters" title="Direct link to Parameters">​</a>

| Name     | Description                                           |
|----------|-------------------------------------------------------|
| level    | The severity level of the log message                 |
| message  | The log message content                               |
| fileName | Optional source file name where the log was generated |
| fileLine | Line number in the source file                        |
| funcName | Optional function name where the log was generated    |

</div>

</div>
