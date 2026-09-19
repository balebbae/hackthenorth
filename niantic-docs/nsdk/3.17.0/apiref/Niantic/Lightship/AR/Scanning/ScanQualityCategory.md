---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Scanning/ScanQualityCategory/
title: enum ScanQualityCategory
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# enum ScanQualityCategory

</div>

(Niantic.Lightship.AR.Scanning.ScanQualityCategory)

Scan quality categories. Note, if changing this category, it needs to change the relevant native enum.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs

enum ScanQualityCategory: UInt32 {
     Overall              = 0,
       Blurry               = 1,
       Dark                 = 2,
       BadQuality           = 3,
       GroundOrFeet         = 4,
       ScanIndoor           = 5,
       ScanFromCar          = 6,
       Obstruction          = 7,
       ScanTargetNotVisible = 8,
};
```

</div>

</div>

</div>

</div>
