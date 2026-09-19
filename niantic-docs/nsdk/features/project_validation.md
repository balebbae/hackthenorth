---
source: https://www.nianticspatial.com/docs/nsdk/features/project_validation/
title: Project Validation
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Project Validation

</div>

Niantic Spatial SDK enables the Unity Project Validation system to identify issues with NSDK, including configuration problems in Projects and Scenes. These checks complement ARKit/ARCore validations by making sure you have also met the NSDK requirements. We recommend using Project Validation to detect common issues before building your application.

## Using Project Validation<a href="#using-project-validation" class="hash-link" aria-label="Direct link to Using Project Validation" title="Direct link to Using Project Validation">​</a>

To open the **Project Validation** menu, open the **NSDK** top menu in Unity, then select **Project Validation**.

<img src="https://www.nianticspatial.com/docs/assets/images/project_validation_example-e0385e4ec66fc0dbadbec1b23d93208c.png" width="800" alt="A list of project validation options and buttons to automatically fix them." />

As in this example, Project Validation includes triggers from multiple sources, such as NSDK, Unity, ARKit, and ARCore. Some issues offer a **Fix** button for automatic adjustments, while others provide an **Edit** button that directs you to a window for manual corrections.

## Common Project Validation Issues<a href="#common-project-validation-issues" class="hash-link" aria-label="Direct link to Common Project Validation Issues" title="Direct link to Common Project Validation Issues">​</a>

### Is NSDK activated?<a href="#is-nsdk-activated" class="hash-link" aria-label="Direct link to Is NSDK activated?" title="Direct link to Is NSDK activated?">​</a>

If the NSDK plugin is not activated for the selected platform, a warning will appear:

<img src="https://www.nianticspatial.com/docs/assets/images/project_validation_activate-3e4fdaff1eda11998bbf27d76c6de29f.png" width="800" alt="Warning that NSDK is not activated." />

Pressing the **Edit** button next to it opens the page where you can tick the checkbox to activate NSDK for that platform.

### Is Authentication set up?<a href="#is-authentication-set-up" class="hash-link" aria-label="Direct link to Is Authentication set up?" title="Direct link to Is Authentication set up?">​</a>

For more information, see the [Auth guide](https://www.nianticspatial.com/docs/nsdk/auth_getting_started/).

### Are the platform settings valid?<a href="#are-the-platform-settings-valid" class="hash-link" aria-label="Direct link to Are the platform settings valid?" title="Direct link to Are the platform settings valid?">​</a>

The system will check if all the settings required for this platform are valid and will present **Fix** buttons for things that can be fixed automatically by the system. Pressing the **Fix All** button in the top-right corner will fix all invalid settings that can be fixed automatically:

<img src="https://www.nianticspatial.com/docs/assets/images/project_validation_fix_all-e540114de5923f199b441c32e7254f17.png" width="800" alt="Error that NSDK has enabled features that require authentication." />

<div class="theme-admonition theme-admonition-caution admonition_xJq3 alert alert--warning">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)</span>Attention!

</div>

<div class="admonitionContent_BuS1">

XR Plug-in Management Project Validation for Android displays two errors and two **Fix** buttons for setting the Graphics API to **OpenGLES3**, one from Google ARCore and one from NSDK. If this happens, click the NSDK **Fix** button to fix both issues.

</div>

</div>

</div>

</div>
