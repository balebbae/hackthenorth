---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanArchiveBuilder.CreateTaskToGetNextChunk/
title: CreateTaskToGetNextChunk
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR.Scanning](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning/ "NianticSpatial.NSDK.AR.Scanning") <span class="api-breadcrumbs-nav">←</span>[ScanArchiveBuilder](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Scanning.ScanArchiveBuilder/ "NianticSpatial.NSDK.AR.Scanning.ScanArchiveBuilder") 

</div>

<div class="api-title">

#  CreateTaskToGetNextChunk

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<div class="api-constructor">

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1?view=net-9.0" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Task</a></span><span class="ctoken punctuation">\<</span><span class="ctoken class-name keyword">string</span><span class="ctoken punctuation">\></span><span class="ctoken plain"> </span><span class="ctoken class-name">CreateTaskToGetNextChunk</span><span class="ctoken punctuation">(</span><span class="ctoken punctuation">)</span></span>

</div>

#### Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

<div class="ctoken comment">

Creates a task for packing the next chunk. Must only be called if HasMoreChunks is true, and\
no other task is currently running.

\

\
The task is not started automatically. The caller of this method should start the task. The\
task does not block.

</div>

------------------------------------------------------------------------

</div>

</div>
