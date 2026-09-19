---
source: https://www.nianticspatial.com/docs/scaniverse/troubleshoot/
title: Troubleshooting Scaniverse Scans
---

<div class="mobile-docs-controls">

<div class="mobile-docs-controls__main">

</div>

</div>

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="theme-admonition theme-admonition-info admonition_xJq3 alert alert--info">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)</span><a href="https://lightship.dev/signin" target="_blank" rel="noopener noreferrer">Lightship.dev</a> has been decommissioned.

</div>

<div class="admonitionContent_BuS1">

If you previously used Lightship.dev, log in to <a href="https://scaniverse.nianticspatial.com" target="_blank" rel="noopener noreferrer">scaniverse.nianticspatial.com</a>, and select **Migrate a Lightship account** to create a new account and access your projects. For more information, see the [Migration guide](https://www.nianticspatial.com/docs/scaniverse/migration_guide/).

</div>

</div>

<div>

# Troubleshoot

</div>

## Common issues and how to avoid them<a href="#common-issues-and-how-to-avoid-them" class="hash-link" aria-label="Direct link to Common issues and how to avoid them" title="Direct link to Common issues and how to avoid them">​</a>

Even with careful inspection and targeted scans, common issues can occur. Use the following guidance to identify and prevent these problems.

### Patchy results<a href="#patchy-results" class="hash-link" aria-label="Direct link to Patchy results" title="Direct link to Patchy results">​</a>

A sparse mesh usually indicates insufficient overlap or limited perspective change. You can:

- Move side-to-side and vary height while scanning.
- Capture multiple viewpoints to ensure sufficient detail.

### Poor localization<a href="#poor-localization" class="hash-link" aria-label="Direct link to Poor localization" title="Direct link to Poor localization">​</a>

Localization can fail if scans begin in areas with few distinct features. You can:

- Start scans from previously captured views with strong geometry.
- Include visually distinct surfaces in your scan path.

### Disconnected rooms<a href="#disconnected-rooms" class="hash-link" aria-label="Direct link to Disconnected rooms" title="Direct link to Disconnected rooms">​</a>

Rooms may fail to align if doorways or hallways lack overlap. You can:

- Move slowly through transitions between spaces.
- Keep shared features visible between connected spaces.

### Large outdoor drift<a href="#large-outdoor-drift" class="hash-link" aria-label="Direct link to Large outdoor drift" title="Direct link to Large outdoor drift">​</a>

Drift occurs when scans gradually shift from their true position, often in open areas with few landmarks. You can:

- Include stable reference points such as trees, benches, or building edges.
- Perform multiple passes through the area to strengthen alignment.

### Missing ceilings or floors<a href="#missing-ceilings-or-floors" class="hash-link" aria-label="Direct link to Missing ceilings or floors" title="Direct link to Missing ceilings or floors">​</a>

Vertical surfaces are often under-captured. You can:

- Perform upward and downward passes during overview scans.
- Ensure both ceilings and floors are captured in each room.

### Over-scanning<a href="#over-scanning" class="hash-link" aria-label="Direct link to Over-scanning" title="Direct link to Over-scanning">​</a>

Long scans without adding a new perspective do not improve quality. You can:

- Prioritize coverage and viewpoint diversity over scan duration.
- Add short, targeted scans instead of repeating long passes.

------------------------------------------------------------------------

## Final tips for reliable, reusable scans<a href="#final-tips-for-reliable-reusable-scans" class="hash-link" aria-label="Direct link to Final tips for reliable, reusable scans" title="Direct link to Final tips for reliable, reusable scans">​</a>

The following best practices help ensure your scans are complete, accurate, and reusable.

- Move deliberately and maintain steady motion throughout each scan.
- Focus on what the camera sees rather than what you know is present.
- Maintain overlap within each scan and between adjacent scans.
- Favor stable, static features over dynamic or moving elements.
- Plan scans according to intended user behavior and expected paths.
- When in doubt, add a short, targeted scan instead of repeating a full session.
- After completing new scans, inspect meshes and splats to verify coverage and alignment.

By combining careful review, incremental scanning, and these best practices, you can create reliable, reusable Sites with accurate localization.

</div>

</div>
