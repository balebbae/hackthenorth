---
source: https://www.nianticspatial.com/docs/nsdk/migration_guide/
title: Migration guide
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Migration guide

</div>

Upgrade from legacy Lightship.dev and ARDK SDK to Scaniverse and NSDK 4.0. Developers must migrate Lightship.dev content to Scaniverse. Developers maintaining apps must also upgrade to NSDK 4.0.

Developers managing both VPS content and applications must complete **both** Lightship.dev and SDK migration. Developers who only manage Lightship.dev content without managing applications only need to migrate to Scaniverse. Before upgrading, create a backup or branch of your project.

There are two steps in the migration process: **Lightship.dev migration** and (optional) **SDK migration**.

1.  [Lightship.dev migration](#migrate-lightshipdev) – Move Lightship content, including workspaces, private and public POIs, scans, and API keys, into Scaniverse. Applies to **all developers managing Scaniverse content**. Complete self-serve migration before February 27, 2027. After that date, contact support to migrate content.

2.  [SDK migration](#migrate-sdk) – Upgrade applications from ARDK 3.x/Lightship SDK to NSDK 4.0. Update namespaces, class names, and authentication to use Enterprise Authentication. Applies only to **developers maintaining applications**. NSDK 3.17 will receive critical bug and security fixes only through February 2027. Projects using legacy Wayspots that are not fully scanned must upgrade to maintain full functionality. Completed projects continue working but can upgrade to access the latest features and performance improvements.

Migrate to NSDK 4.0 and Scaniverse to ensure all your assets and applications remain fully functional and up to date. Completing migration allows you to:

- Use new Scaniverse capabilities: Access VPS 2.0, updated APIs, and improved scanning workflows.
- Transition seamlessly: Continue using existing workspaces, sites, scans, and API keys in Scaniverse without disruption.
- Keep applications up to date: Ensure ongoing compatibility with new projects and upcoming NSDK features.

| Area | Motivation | Timeline / Notes |
|----|----|----|
| NSDK | NSDK 4.0 improves VPS performance, adds new features, and removes deprecated APIs such as SharedAR. NSDK 3.17 receives only critical bug fixes and security updates through February 2027. | Projects actively in development should migrate promptly. SharedAR is no longer functional as of May 1, 2026. Completed projects continue functioning. |
| Scaniverse | Lightship.dev and the Geospatial Browser are deprecated. Migration preserves your content and assets including sites, scans, VPS maps, and API keys, though public POIs are converted to private sites. | Self-serve migration started Feb 20, 2026. Lightship.dev decommissioned on Feb 20, 2027. After then, contact support to migrate content. |

## Migrate Lightship.dev<a href="#migrate-lightshipdev" class="hash-link" aria-label="Direct link to Migrate Lightship.dev" title="Direct link to Migrate Lightship.dev">​</a>

Use the <a href="https://scaniverse.nianticspatial.com/" target="_blank" rel="noopener noreferrer">Scaniverse Web</a> and the <a href="https://apps.apple.com/us/app/scaniverse-3d-scanner/id1541433223" target="_blank" rel="noopener noreferrer">Scaniverse app</a> to manage and access all migrated Lightship content:

- The Scaniverse Web handles organizations, sites, VPS maps, and API keys.
- The Scaniverse app captures scans, uploads them to the cloud, and generates assets for testing localization.

Migrate Lightship content to Scaniverse to preserve existing assets and continue using them in VPS experiences without interruption. No re-scanning or app rebuild is required to maintain current behavior. Migration moves workspaces, projects, sites (formerly POIs), scans, VPS maps, and API keys into the new Scaniverse platform as follows:

**What Scaniverse replaces:**

| Legacy Lightship | Scaniverse Replacement |
|----|----|
| Workspace | Becomes an Organization. |
| Private POI | Becomes a Private Site. |
| Public POI | Migrates to a Private Site. Access to public POIs is no longer available. Contributed scans remain accessible. |
| Project | Converts to a Service Account. |
| Scans | Remain as Scans. |
| API Key | Remain valid for existing apps. |

### How to migrate to Scaniverse<a href="#how-to-migrate-to-scaniverse" class="hash-link" aria-label="Direct link to How to migrate to Scaniverse" title="Direct link to How to migrate to Scaniverse">​</a>

You must migrate to Scaniverse on your desktop.

1.  Navigate to the <a href="https://scaniverse.nianticspatial.com/" target="_blank" rel="noopener noreferrer">Scaniverse Web</a>.
2.  Select **Migrate a Lightship account** under the login screen.
3.  Enter the email address associated with Niantic Spatial. Existing personal Scaniverse accounts cannot be merged with migrated business accounts. If needed, log out and sign in with the account associated with your Lightship content.
4.  Select **Continue**.
5.  Check your inbox for an email from Niantic Spatial. If you don't see it, check your spam or trash folders.
6.  Select the **Create Scaniverse Login** button in the Niantic Spatial email.
7.  Create a new password for your Scaniverse account.
8.  Select **Continue**.

### Key dates<a href="#key-dates" class="hash-link" aria-label="Direct link to Key dates" title="Direct link to Key dates">​</a>

The following dates highlight critical milestones for migration and SDK updates. Adhering to these dates ensures continued access to Scaniverse content, uninterrupted app functionality, and access to the latest NSDK features:

| Date | Action / Guidance |
|----|----|
| February 20, 2026 | Self-serve migration to Scaniverse opened. Developers can start moving Lightship content. |
| May 1, 2026 | Shared AR is no longer functional in NSDK 3.17. Upgrade active projects to NSDK 4.0 to maintain VPS functionality. |
| After February 20, 2027 | Lightship.dev and Geospatial Browser decommissioned. Self-serve migration is no longer available. Contact support for migration. |
| For all new projects | Use NSDK 4.0 to access VPS 2.0 and updated APIs. |

For migration issues, contact <a href="mailto:support@nianticspatial.com" target="_blank" rel="noopener noreferrer">support@nianticspatial.com</a> and include your Lightship email.

## Migrate SDK<a href="#migrate-sdk" class="hash-link" aria-label="Direct link to Migrate SDK" title="Direct link to Migrate SDK">​</a>

Upgrading from ARDK 3.x/Lightship SDK to NSDK 4.0 ensures your applications remain compatible with the latest APIs, VPS workflows, and NSDK features. The migration involves updating project packages, code references, authentication, and VPS sessions in the following steps:

1.  [Install NSDK 4.0](#install-nsdk-40) – Replace ARDK/Lightship packages with NSDK 4.0 UPMs.
2.  [Update namespaces and API references](#update-namespaces-and-api-references) – Replace legacy namespaces, class names, and properties/methods with NSDK equivalents.
3.  [Update project files](#update-project-files) – Rename settings files and update version control in Git.
4.  [Update authentication](#update-authentication) – Switch from API key to Enterprise Authentication.
5.  [Remove unsupported features](#remove-unsupported-features) - Remove features that are no longer supported in NSDK 4.0.
6.  [Upgrade VPS to VPS2](#upgrade-from-vps-to-vps2) – Replace VPS/WPS sessions with VPS2 sessions, migrate anchors, and update AR↔geoposition conversions.

### Install NSDK 4.0<a href="#install-nsdk-40" class="hash-link" aria-label="Direct link to Install NSDK 4.0" title="Direct link to Install NSDK 4.0">​</a>

Install NSDK 4.0 by replacing existing Lightship/ARDK packages with the new NSDK 4.0 as follows:

Remove all ARDK/Lightship packages before installing NSDK 4.0.

1.  Download [NSDK 4.0 UPMs](https://www.nianticspatial.com/docs/nsdk/downloads/).
2.  In Unity, Remove the existing Lightship UPMs from Package Manager.
3.  Add NSDK 4.0 UPMs using the package manager.
    - Note: Unity may re-open the project, and prompt for Safe Mode due to compilation failures. Click ignore and open the project anyway.
4.  You may see many compilation errors in the console. Use the following steps to update your project and resolve them.

### Update namespaces and API references<a href="#update-namespaces-and-api-references" class="hash-link" aria-label="Direct link to Update namespaces and API references" title="Direct link to Update namespaces and API references">​</a>

**Update namespaces as follows:**

1.  Open your code editor.
2.  Use your code editor's bulk replace operation with case-sensitive matching enabled.
3.  Replace `using Niantic.Lightship.AR.` with `using NianticSpatial.NSDK.AR.`
    - If you have custom namespaces that use `Niantic.Lightship.AR.*`, either exclude them from the replacement or rename them. Leaving them unchanged may cause compile errors if they reference NSDK APIs.
4.  Replace `using Niantic.ARDK.AR.` with `using NianticSpatial.NSDK.AR.`
5.  Replace any other instances of `Niantic.Lightship.AR` or `Niantic.ARDK.AR` namespaces with `NianticSpatial.NSDK.AR`.

**Update class names as follows:**

All class names beginning with `Lightship` have been renamed to use the `Nsdk` prefix. Use your code editor's bulk replace operation to update the following class names:

- `LightshipSettingsHelper` → `NsdkSettingsHelper`
- `LightshipOcclusionExtension` → `NsdkOcclusionExtension`
- `LightshipMeshingExtension` → `NsdkMeshingExtension`
- `LightshipSettings` → `NsdkSettings`

### Update property and method names<a href="#update-property-and-method-names" class="hash-link" aria-label="Direct link to Update property and method names" title="Direct link to Update property and method names">​</a>

All Properties and methods containing `Lightship` now use the `Nsdk` prefix to distinguish NSDK 4.0 from legacy Lightship APIs. Search your project for properties and methods containing Lightship and rename them to use the Nsdk prefix to align with NSDK 4.0 APIs.

### Update project files<a href="#update-project-files" class="hash-link" aria-label="Direct link to Update project files" title="Direct link to Update project files">​</a>

The main settings file name changed from `Lightship Settings` to `NSDK Settings`. Add `NSDK Settings.asset` to your project and version control. Remove `Lightship Settings.asset` from the project and version control.

### Update authentication<a href="#update-authentication" class="hash-link" aria-label="Direct link to Update authentication" title="Direct link to Update authentication">​</a>

NSDK 4.0 no longer supports API key-based authentication. Configure Enterprise Authentication instead. To remove the API key from the project:

1.  Open Unity's Player Settings.
2.  Set `NIANTICSPATIAL_NSDK_APIKEY_ENABLED` in the script define symbols. This will reveal the API key in NSDK Settings.
3.  Go to NSDK Settings, and remove the API key.
4.  Return to player settings and remove `NIANTICSPATIAL_NSDK_APIKEY_ENABLED` to re-enable Enterprise Authentication.
5.  Configure Enterprise Authentication as described in [Access](https://www.nianticspatial.com/docs/nsdk/auth_getting_started/).

### Remove unsupported features<a href="#remove-unsupported-features" class="hash-link" aria-label="Direct link to Remove unsupported features" title="Direct link to Remove unsupported features">​</a>

NSDK 4.0 removes the following features. Update your project to:

1.  Remove all `SharedAR` usage.
2.  Replace or delete all APIs and properties previously marked as `Obsolete`.

Search your project for these references and refactor or remove the affected code before building with NSDK 4.0.

### Upgrade from VPS to VPS2<a href="#upgrade-from-vps-to-vps2" class="hash-link" aria-label="Direct link to Upgrade from VPS to VPS2" title="Direct link to Upgrade from VPS to VPS2">​</a>

While VPS is still available in NSDK 4.0, upgrading to VPS2 provides better localization accuracy, improved performance, and full support for NSDK 4.0 features. [VPS2](https://www.nianticspatial.com/docs/nsdk/features/vps2/) ensures your projects stay compatible with new APIs, scanning workflows, and future updates.

To upgrade, developers must replace legacy VPS and WPS sessions with `VPS2Session` in NSDK 4.0. VPS2 unifies VPS and WPS functionality under a single session type and provides global geoposition, map-relative localization, and anchor persistence with built-in geolocation. Anchors deliver geographic coordinates directly via updates, and independent APIs remain available for device geolocation and arbitrary coordinate conversion. For detailed instructions, examples, and full guidance on migrating anchors, session code, and geolocation conversion, see the [VPS2 migration guide](https://www.nianticspatial.com/docs/nsdk/features/vps2_migration/).

</div>

</div>
