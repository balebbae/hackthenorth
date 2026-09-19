---
source: https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Input/
title: Input
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

UnitySwiftKotlin

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="api-breadcrumbs">

<span class="api-breadcrumbs-nav">←</span>[API Reference](https://www.nianticspatial.com/docs/api/unity/ "Return to API Reference index") <span class="api-breadcrumbs-nav">←</span>[NianticSpatial.NSDK.AR](https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR/ "NianticSpatial.NSDK.AR") 

</div>

<div class="api-title">

#  Input

</div>

------------------------------------------------------------------------

## Declaration<a href="#declaration" class="hash-link" aria-label="Direct link to Declaration" title="Direct link to Declaration">​</a>

<span class="ctoken-line"><span class="ctoken keyword">public</span><span class="ctoken plain"> </span><span class="ctoken keyword">class</span><span class="ctoken plain"> </span><span class="ctoken class-name">Input</span></span>

## Summary<a href="#summary" class="hash-link" aria-label="Direct link to Summary" title="Direct link to Summary">​</a>

For the most part, a straight pass-through wrapper of the UnityEngine.Input class. However, if AR is running using Playback, then Input.location and Input.compass will return Playback-compatible objects that return values from recorded datasets.

------------------------------------------------------------------------

## Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

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
<td><span id="property-acceleration"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">acceleration</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector3</a></span></span></td>
<td><div class="ctoken comment">
Last measured linear acceleration of a device in three-dimensional space. (Read Only)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-accelerationeventcount"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">accelerationEventCount</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
Number of acceleration measurements which occurred during last frame.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-accelerationevents"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">accelerationEvents</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AccelerationEvent.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">AccelerationEvent</a></span><span class="ctoken punctuation">[</span><span class="ctoken punctuation">]</span></span></td>
<td><div class="ctoken comment">
Returns list of acceleration measurements which occurred during the last frame. (Read Only) (Allocates temporary variables).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-anykey"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">anyKey</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Is any key or mouse button currently held down? (Read Only)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-anykeydown"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">anyKeyDown</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Returns true the first frame the user hits any key or mouse button. (Read Only)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-backbuttonleavesapp"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">backButtonLeavesApp</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Should Back button quit the application?<br />
Only usable on Android, Windows Phone or Windows Tablets.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-compass"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">compass</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Compass/" title="Interface into compass functionality.">Compass</a></span></span></td>
<td><div class="ctoken comment">
Property for accessing compass (handheld devices only). (Read Only)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-compensatesensors"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">compensateSensors</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
This property controls if input sensors should be compensated for screen orientation.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-compositioncursorpos"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">compositionCursorPos</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector2</a></span></span></td>
<td><div class="ctoken comment">
The current text input position used by IMEs to open windows.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-compositionstring"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">compositionString</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
The current IME composition string being typed by the user.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-deviceorientation"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">deviceOrientation</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceOrientation.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">DeviceOrientation</a></span></span></td>
<td><div class="ctoken comment">
Device physical orientation as reported by OS. (Read Only)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-gyro"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">gyro</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gyroscope.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Gyroscope</a></span></span></td>
<td><div class="ctoken comment">
Returns default gyroscope.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-imecompositionmode"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">imeCompositionMode</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMECompositionMode.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">IMECompositionMode</a></span></span></td>
<td><div class="ctoken comment">
Controls enabling and disabling of IME input composition.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-imeisselected"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">imeIsSelected</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Does the user have an IME keyboard input source selected?
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-inputstring"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">inputString</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span></span></td>
<td><div class="ctoken comment">
Returns the keyboard input entered this frame. (Read Only)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-location"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">location</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.LocationService/" title="Interface into location service functionality.">LocationService</a></span></span></td>
<td><div class="ctoken comment">
Property for accessing device location (handheld devices only). (Read Only)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-mouseposition"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">mousePosition</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector3</a></span></span></td>
<td><div class="ctoken comment">
The current mouse position in pixel coordinates. (Read Only).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-mousepresent"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">mousePresent</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Indicates if a mouse device is detected.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-mousescrolldelta"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">mouseScrollDelta</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Vector2</a></span></span></td>
<td><div class="ctoken comment">
The current mouse scroll delta. (Read Only)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-multitouchenabled"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">multiTouchEnabled</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Property indicating whether the system handles multiple touches.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-simulatemousewithtouches"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name">simulateMouseWithTouches</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Enables/Disables mouse simulation with touches. By default this option is enabled.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-stylustouchsupported"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">stylusTouchSupported</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Returns true when Stylus Touch is supported by a device or platform.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-touchcount"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">touchCount</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">int</span></span></td>
<td><div class="ctoken comment">
Number of touches. Guaranteed not to change throughout the frame. (Read Only)
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-touches"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">touches</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Touch</a></span><span class="ctoken punctuation">[</span><span class="ctoken punctuation">]</span></span></td>
<td><div class="ctoken comment">
Returns list of objects representing status of all touches during last frame. (Read Only) (Allocates temporary variables).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-touchpressuresupported"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">touchPressureSupported</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Bool value which let's users check if touch pressure is supported.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="property-touchsupported"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken keyword">readonly</span><span class="ctoken plain"> </span><span class="ctoken class-name">touchSupported</span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Returns whether the device on which application is currently running supports touch input.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

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
<td><span id="method-getaccelerationevent"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Input.GetAccelerationEvent/" title="Returns specific acceleration measurement which occurred during last frame. (Does not allocate temporary variables).">GetAccelerationEvent</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AccelerationEvent.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">AccelerationEvent</a></span></span></td>
<td><div class="ctoken comment">
Returns specific acceleration measurement which occurred during last frame. (Does not allocate temporary variables).
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getaxis"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Input.GetAxis/" title="Returns the value of the virtual axis identified by axisName.">GetAxis</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
Returns the value of the virtual axis identified by axisName.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getaxisraw"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Input.GetAxisRaw/" title="Returns the value of the virtual axis identified by axisName with no smoothing filtering applied.">GetAxisRaw</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">float</span></span></td>
<td><div class="ctoken comment">
Returns the value of the virtual axis identified by axisName with no smoothing filtering applied.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getbutton"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Input.GetButton/" title="Returns true while the virtual button identified by buttonName is held down.">GetButton</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Returns true while the virtual button identified by buttonName is held down.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getbuttondown"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Input.GetButtonDown/" title="Returns true during the frame the user pressed down the virtual button identified by buttonName.">GetButtonDown</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Returns true during the frame the user pressed down the virtual button identified by buttonName.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getbuttonup"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Input.GetButtonUp/" title="Returns true the first frame the user releases the virtual button identified by buttonName.">GetButtonUp</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Returns true the first frame the user releases the virtual button identified by buttonName.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getjoysticknames"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Input.GetJoystickNames/" title="Retrieves a list of input device names corresponding to the index of an Axis configured within Input Manager.">GetJoystickNames</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">string</span><span class="ctoken punctuation">[</span><span class="ctoken punctuation">]</span></span></td>
<td><div class="ctoken comment">
Retrieves a list of input device names corresponding to the index of an Axis configured within Input Manager.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getkey"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Input.GetKey/" title="Returns true while the user holds down the key identified by the key KeyCode enum parameter.">GetKey</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Returns true while the user holds down the key identified by the key KeyCode enum parameter.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getkeydown"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Input.GetKeyDown/" title="Returns true during the frame the user starts pressing down the key identified by the key KeyCode enum parameter.">GetKeyDown</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Returns true during the frame the user starts pressing down the key identified by the key KeyCode enum parameter.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getkeyup"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Input.GetKeyUp/" title="Returns true during the frame the user releases the key identified by the key KeyCode enum parameter.">GetKeyUp</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Returns true during the frame the user releases the key identified by the key KeyCode enum parameter.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getmousebutton"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Input.GetMouseButton/" title="Returns whether the given mouse button is held down.">GetMouseButton</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Returns whether the given mouse button is held down.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getmousebuttondown"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Input.GetMouseButtonDown/" title="Returns true during the frame the user pressed the given mouse button.">GetMouseButtonDown</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Returns true during the frame the user pressed the given mouse button.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-getmousebuttonup"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Input.GetMouseButtonUp/" title="Returns true during the frame the user releases the given mouse button.">GetMouseButtonUp</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">bool</span></span></td>
<td><div class="ctoken comment">
Returns true during the frame the user releases the given mouse button.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-gettouch"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Input.GetTouch/" title="Call Input.GetTouch to obtain a Touch struct.">GetTouch</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name"><a href="https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html" target="_blank" rel="noopener noreferrer" title="Opens an external reference">Touch</a></span></span></td>
<td><div class="ctoken comment">
Call Input.GetTouch to obtain a Touch struct.
</div></td>
</tr>
<tr class="api-table-row">
<td><span id="method-resetinputaxes"></span><span class="ctoken-line"><span class="ctoken keyword">static</span><span class="ctoken plain"> </span><span class="ctoken class-name"><a href="https://www.nianticspatial.com/docs/api/unity/NianticSpatial.NSDK.AR.Input.ResetInputAxes/" title="Resets all input. After ResetInputAxes all axes return to 0 and all buttons return to 0 for one frame.">ResetInputAxes</a></span></span></td>
<td><span class="ctoken-line"><span class="ctoken class-name keyword">void</span></span></td>
<td><div class="ctoken comment">
Resets all input. After ResetInputAxes all axes return to 0 and all buttons return to 0 for one frame.
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

</div>

</div>
