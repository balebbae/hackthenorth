---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/ErrorCode/
title: enum ErrorCode
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# enum ErrorCode

</div>

(Niantic.Lightship.AR.XRSubsystems.ErrorCode)

Reports the error code of a localization network request, if any

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs

enum ErrorCode: uint {
      Unknown               = 0,
      None,
      BadNetworkConnection,
      BadApiKey,
     PermissionDenied,
      RequestsLimitExceeded,
     InternalServer,
        InternalClient,
};
```

</div>

</div>

</div>

</div>
