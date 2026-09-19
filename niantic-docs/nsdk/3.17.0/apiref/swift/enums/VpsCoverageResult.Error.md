---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/swift/enums/VpsCoverageResult.Error/
title: VpsCoverageResult.Error
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

**ENUM**

<div>

# `VpsCoverageResult.Error`

</div>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
enum Error: Swift.Error
```

</div>

</div>

Network request errors that can occur during VPS coverage operations.

`VpsCoverageNetworkRequestError` provides detailed error information for network-related issues when querying VPS coverage data from the server.

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

These errors help diagnose network connectivity issues, server problems, and request validation failures when accessing VPS coverage services.

## Cases<a href="#cases" class="hash-link" aria-label="Direct link to Cases" title="Direct link to Cases">​</a>

### `curlClientError`<a href="#curlclienterror" class="hash-link" aria-label="Direct link to curlclienterror" title="Direct link to curlclienterror">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case curlClientError
```

</div>

</div>

Client-side network error (e.g., connection failure, timeout).

This indicates a problem with the network connection or client-side networking stack, such as DNS resolution failure or connection timeout.

### `httpForbidden`<a href="#httpforbidden" class="hash-link" aria-label="Direct link to httpforbidden" title="Direct link to httpforbidden">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case httpForbidden
```

</div>

</div>

HTTP 403 Forbidden - access denied.

The API key lacks permission to access the requested resource or the request is not authorized.

### `httpNotFound`<a href="#httpnotfound" class="hash-link" aria-label="Direct link to httpnotfound" title="Direct link to httpnotfound">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case httpNotFound
```

</div>

</div>

HTTP 404 Not Found - requested resource not found.

The requested VPS coverage data or area does not exist.

### `httpTooManyRequests`<a href="#httptoomanyrequests" class="hash-link" aria-label="Direct link to httptoomanyrequests" title="Direct link to httptoomanyrequests">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case httpTooManyRequests
```

</div>

</div>

HTTP 429 Too Many Requests - rate limit exceeded.

The request rate has exceeded the allowed limits. Implement exponential backoff and retry later.

### `invalidRequest`<a href="#invalidrequest" class="hash-link" aria-label="Direct link to invalidrequest" title="Direct link to invalidrequest">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case invalidRequest
```

</div>

</div>

Invalid request format or parameters.

The request was rejected due to invalid format or parameters before reaching the server.

### `tooManyEntitiesRequested`<a href="#toomanyentitiesrequested" class="hash-link" aria-label="Direct link to toomanyentitiesrequested" title="Direct link to toomanyentitiesrequested">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case tooManyEntitiesRequested
```

</div>

</div>

Too many entities requested in a single query.

The request attempted to query more entities than allowed in a single operation.

### `internalServerError`<a href="#internalservererror" class="hash-link" aria-label="Direct link to internalservererror" title="Direct link to internalservererror">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case internalServerError
```

</div>

</div>

HTTP 500 Internal Server Error - server-side error.

An unexpected error occurred on the server side. This is typically a temporary issue.

### `unexpectedResponse`<a href="#unexpectedresponse" class="hash-link" aria-label="Direct link to unexpectedresponse" title="Direct link to unexpectedresponse">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case unexpectedResponse
```

</div>

</div>

Unexpected or unrecognized response from server.

The server returned a response that could not be processed or was in an unexpected format.

### `internalError`<a href="#internalerror" class="hash-link" aria-label="Direct link to internalerror" title="Direct link to internalerror">​</a>

<div class="language-swift codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` swift
case internalError
```

</div>

</div>

An unexpected error occurred.

</div>

</div>
