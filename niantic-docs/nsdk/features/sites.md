---
source: https://www.nianticspatial.com/docs/nsdk/features/sites/
title: Sites
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Niantic Spatial Sites

</div>

## What is Sites?<a href="#what-is-sites" class="hash-link" aria-label="Direct link to What is Sites?" title="Direct link to What is Sites?">​</a>

The Sites feature provides access to organized entity data in the Niantic Spatial platform, enabling your application to discover and navigate the relationships between a user, organization, site, and spatial data asset. This feature allows you to query what spatial content is available to users and how it's structured within your organization.

## What can Sites be used for?<a href="#what-can-sites-be-used-for" class="hash-link" aria-label="Direct link to What can Sites be used for?" title="Direct link to What can Sites be used for?">​</a>

Sites is essential for applications that need to discover available spatial content, navigate hierarchy structures, access spatial data metadata, and build location-aware experiences that adapt based on the site and its associated assets.

Here is an example where we use the Sites API to display entity metadata that a test user has access to on the Niantic Spatial platform.

<img src="https://www.nianticspatial.com/docs/assets/images/sites_visualization-20b6569c0fc533a863be0492405a2639.gif" width="400" alt="Sites API visualization showing organization information and loading sites" />

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

All data returned by the Sites API is scoped to the authenticated user. Users can only access organizations, sites, and assets that they have permission to view based on their authentication credentials.

</div>

</div>

## How is Sites data organized?<a href="#how-is-sites-data-organized" class="hash-link" aria-label="Direct link to How is Sites data organized?" title="Direct link to How is Sites data organized?">​</a>

The Sites feature organizes spatial data in a hierarchical structure:

**User** → **Organization** → **Site** → **Asset**

A **User** represents an authenticated individual who has access to the Niantic Spatial platform. Each user belongs to one or more organizations and can query information about themselves, including their associated organizations, sites, and assets.

An **Organization** is a top-level container that groups related sites and assets together. Organizations typically represent companies, teams, or projects that manage multiple spatial locations. Users can belong to multiple organizations, and each organization can contain multiple sites.

A **Site** represents a specific physical location or area where spatial data has been collected or is being managed. Sites belong to an organization and can contain multiple assets. A site may have geographic coordinates and can represent anything from a building to an outdoor area to a specific region of interest.

An **Asset** is a spatial data resource associated with a site. Assets can include various types of spatial content such as meshes, Gaussian splats, VPS anchors, or other processed spatial data. Each asset belongs to a specific site and represents the actual spatial content that applications can use for AR experiences.

The hierarchy flows downward: Users access Organizations, Organizations contain Sites, and Sites contain Assets. This structure allows you to:

- Discover what spatial content is available to a user
- Navigate from high-level organizational context down to specific spatial assets
- Understand the relationships and permissions that govern access to spatial data
- Build location-aware applications that adapt based on the site and its available assets

## Next Steps<a href="#next-steps" class="hash-link" aria-label="Direct link to Next Steps" title="Direct link to Next Steps">​</a>

- Get started with [Getting Started with Sites](https://www.nianticspatial.com/docs/nsdk/how-to/sites/getting_started/)

</div>

</div>
