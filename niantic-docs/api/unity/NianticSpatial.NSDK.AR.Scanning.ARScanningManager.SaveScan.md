---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager.SaveScan/
title: SaveScan
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Scanning](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning/ "NianticSpatial.NSDK.AR.Scanning") <span class="api-breadcrumbs-nav">←</span>[ARScanningManager](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ARScanningManager/ "NianticSpatial.NSDK.AR.Scanning.ARScanningManager") 

</div>

<div class="api-title">

#  SaveScan

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">async</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Task</a></span><span class="ctoken plain"> </span><span class="ctoken class-name">SaveScan</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Save the current scan. This stops any further recording immediately, and the coroutine finishes when\
the saving is fully complete.

\

\
Please call GetFrameCount() to guarantee the scan has frames, as if it doesnt have any, the save will fail

\

\
Do not disable the component or exit the app when this is in progress. The scan will not be saved correctly\
if this process is interrupted.

</div>

------------------------------------------------------------------------

</div>

</div>
