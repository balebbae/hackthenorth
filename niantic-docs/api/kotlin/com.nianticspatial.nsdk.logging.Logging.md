---
source: https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.logging.Logging/
title: Logging
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/kotlin/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[com.nianticspatial.nsdk.logging](https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.logging/ "com.nianticspatial.nsdk.logging") 

</div>

<div class="api-title">

#  Logging

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">Logging</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

Logging utility class for configuring ARDK log levels. This class provides methods to set the log level for different log outputs:

- stdout: Logs written to standard output
- file: Logs written to log files
- callback: Logs sent to registered callback handlers

------------------------------------------------------------------------

## Functions<a href="#functions" class="hash-link" aria-label="Direct link to Functions" title="Direct link to Functions">​</a>

<table class="api-table">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr class="api-table-row">
<td><span id="function-setcallbackloglevel"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.logging.Logging.setCallbackLogLevel/" title="Sets the log level for callback logs....">setCallbackLogLevel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Sets the log level for callback logs.<br />
This function filters out logs of less severity than the specified level<br />
for the callback logger.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-setfileloglevel"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.logging.Logging.setFileLogLevel/" title="Sets the log level for file logs....">setFileLogLevel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Sets the log level for file logs.<br />
This function filters out logs of less severity than the specified level<br />
for the file logger.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-setstdoutloglevel"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.logging.Logging.setStdoutLogLevel/" title="Sets the log level for stdout logs....">setStdoutLogLevel</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Sets the log level for stdout logs.<br />
This function filters out logs of less severity than the specified level<br />
for the stdout logger.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="function-setthrottleenabled"></span><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/kotlin/com.nianticspatial.nsdk.logging.Logging.setThrottleEnabled/" title="Enables or disables log throttling globally....">setThrottleEnabled</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken keyword">void</span></span></td>
<td><div class="ctoken comment">
Enables or disables log throttling globally.<br />
When disabled, all throttled log callsites log unconditionally regardless of their<br />
configured interval. Useful for debugging noisy per-frame logs. Throttling is enabled<br />
by default.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
