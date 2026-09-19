---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/enums/MeshDownloaderResults.Error/
title: MeshDownloaderResults.Error
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**ENUM**

<div>

# `MeshDownloaderResults.Error`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
enum Error: Swift.Error
```

</div>

</div>

Possible errors from Mesh Downloader network operations.

## Cases<a href="#cases" class="hash-link" aria-label="Direct link to Cases" title="Direct link to Cases">​</a>

### `sizeExceedsLimit`<a href="#sizeexceedslimit" class="hash-link" aria-label="Direct link to sizeexceedslimit" title="Direct link to sizeexceedslimit">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case sizeExceedsLimit
```

</div>

</div>

The total download size exceeds the limit specified in the request.

### `curlClientError`<a href="#curlclienterror" class="hash-link" aria-label="Direct link to curlclienterror" title="Direct link to curlclienterror">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case curlClientError
```

</div>

</div>

There was a network error on the device.

### `httpResponseError`<a href="#httpresponseerror" class="hash-link" aria-label="Direct link to httpresponseerror" title="Direct link to httpresponseerror">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case httpResponseError
```

</div>

</div>

There was an error in the HTTP response.

- Note: See logs for the specific HTTP response code.

### `unexpectedResponse`<a href="#unexpectedresponse" class="hash-link" aria-label="Direct link to unexpectedresponse" title="Direct link to unexpectedresponse">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case unexpectedResponse
```

</div>

</div>

Downloaded data could not be decompressed or parsed.

### `internalError`<a href="#internalerror" class="hash-link" aria-label="Direct link to internalerror" title="Direct link to internalerror">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case internalError
```

</div>

</div>

An unexpected error occurred.

### `invalidPayload`<a href="#invalidpayload" class="hash-link" aria-label="Direct link to invalidpayload" title="Direct link to invalidpayload">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case invalidPayload
```

</div>

</div>

The payload used to request the mesh download was invalid

</div>

</div>
