---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/ARDK/AR/Scanning/ScanStore/SavedScan/
title: class SavedScan
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class SavedScan

</div>

(Niantic.ARDK.AR.Scanning.ScanStore.SavedScan)

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class SavedScan {
 public:
       // fields
    
      string ScanPath;
      string ScanId;

       // methods
   
     SavedScan(string scanPath);
       ScanMetadataProto GetScanMetadata();
        void SetScanMetadata(ScanMetadataProto proto);
     FramesProto GetScanFrames();
    };
```

</div>

</div>

</div>

</div>
