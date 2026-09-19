---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/LocalizationStatus/
title: enum LocalizationStatus
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# enum LocalizationStatus

</div>

(Niantic.Lightship.AR.XRSubsystems.LocalizationStatus)

Reports the status of a localization request (may contain multiple client -\> server requests) A limited localization means that localization returned a value, but there is not enough confidence to provide a meaningful pose.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs

enum LocalizationStatus: byte {
     Unknown = 0,
        Failure,
       Limited,
       Success,
};
```

</div>

</div>

</div>

</div>
