---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/ARDK/AR/Scanning/ScanStore/
title: class ScanStore
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class ScanStore

</div>

(Niantic.ARDK.AR.Scanning.ScanStore)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class ScanStore {
 public:
   
     class SavedScan;

       // properties
    
     string ScanBasePath;

      // methods
   
     ScanStore(string basePath);
       void DeleteScan(SavedScan scan);
       Task DeleteScanAsync(SavedScan scan);
        List<SavedScan> GetSavedScans();
    };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### ScanStore<a href="#ScanStore" class="hash-link" aria-label="Direct link to ScanStore" title="Direct link to ScanStore">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
ScanStore(string basePath)
```

</div>

</div>

Create a [ScanStore](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/ARDK/AR/Scanning/ScanStore/) given the base path for all your scans. The path should match the ScanBasePath of XRScanningConfiguration.

    **Parameters**:

    `basePath` -

#### DeleteScan<a href="#DeleteScan" class="hash-link" aria-label="Direct link to DeleteScan" title="Direct link to DeleteScan">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
void DeleteScan(SavedScan scan)
```

</div>

</div>

Delete the given saved scan from disk. This must not be a scan that is currently in progress. Deleting a scan in progress is undefined behavior. The scan is invalid after deletion.

    **Parameters**:

    `scan` - The scan to delete.

#### DeleteScanAsync<a href="#DeleteScanAsync" class="hash-link" aria-label="Direct link to DeleteScanAsync" title="Direct link to DeleteScanAsync">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
Task DeleteScanAsync(SavedScan scan)
```

</div>

</div>

Delete the scan in an async way..     **See also**:     [DeleteScan](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/ARDK/AR/Scanning/ScanStore/#DeleteScan)

    **Parameters**:

    `scan` -

    **Returns:**

    

#### GetSavedScans<a href="#GetSavedScans" class="hash-link" aria-label="Direct link to GetSavedScans" title="Direct link to GetSavedScans">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
List<SavedScan> GetSavedScans()
```

</div>

</div>

Return the list of scans currently saved. This will include the current active scan if called with a scan in-progress.

    **Returns:**

    A List of scans that are currently on-disk

</div>

</div>
