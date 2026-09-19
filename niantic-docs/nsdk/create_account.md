---
source: https://www.nianticspatial.com/docs/nsdk/create_account/
title: Account
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div class="theme-admonition theme-admonition-info admonition_xJq3 alert alert--info">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)</span><a href="https://lightship.dev/signin" target="_blank" rel="noopener noreferrer">Lightship.dev</a> has been decommissioned.

</div>

<div class="admonitionContent_BuS1">

If you previously used Lightship.dev, log in to <a href="https://scaniverse.nianticspatial.com" target="_blank" rel="noopener noreferrer">scaniverse.nianticspatial.com</a>, and select **Migrate a Lightship account** to create a new account and access your projects. For more information, see the [Migration guide](https://www.nianticspatial.com/docs/nsdk/migration_guide/).

</div>

</div>

<div>

# Overview

</div>

To use Niantic's SDK (NSDK), you must have a <a href="https://www.nianticspatial.com/faq/scaniverse" target="_blank" rel="noopener noreferrer">Scaniverse</a> account. Each account belongs to an **Organization**, which manages projects, collaborators, and shared resources.

Scaniverse is designed for production workflows, shared ownership, and scalable deployment. Scaniverse enables cloud processing for large-scale reconstruction, VPS map generation, and lets you merge scans from multiple team members into a single site output for use with the NSDK.

The Scaniverse app includes a **New** experience designed for NSDK workflows and cloud processing. To use it, existing users must [create a new Scaniverse account](#create-a-scaniverse-account); you can use the same email address. The **Classic** experience remains available for single scans and local processing.

## Scaniverse use cases<a href="#scaniverse-use-cases" class="hash-link" aria-label="Direct link to Scaniverse use cases" title="Direct link to Scaniverse use cases">​</a>

The **New** Scaniverse experience lets you:

- Scan large or production-scale environments.
- Create and manage VPS-enabled locations.
- Collaborate with a team.
- Manage shared projects across an organization.
- Build client-facing or commercial applications.

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

Before you begin, ensure that you have the following:

- An **iPhone 13 or newer**. iPhone Pro models with LiDAR produce higher-quality results. Android support is coming soon.
- Physical access to the location you want to scan.
- A **New** <a href="https://scaniverse.nianticspatial.com/signin" target="_blank" rel="noopener noreferrer">Scaniverse account</a>. If you don't have an account, follow the steps in [Create a Scaniverse account](#create-a-scaniverse-account).

### Plans and pricing<a href="#plans-and-pricing" class="hash-link" aria-label="Direct link to Plans and pricing" title="Direct link to Plans and pricing">​</a>

Scaniverse offers subscription plans with different levels of usage capacity. Higher tiers provide increased processing credits, storage, collaboration capabilities, and additional features for production workflows.

Pricing scales with usage, allowing individuals to experiment with smaller projects while giving teams and organizations the resources needed to manage larger environments and deployments.

For current plan options and limits, see <a href="https://www.nianticspatial.com/pricing?preview=true" target="_blank" rel="noopener noreferrer">Plans and Pricing</a>.

## Install the Scaniverse app<a href="#install-the-scaniverse-app" class="hash-link" aria-label="Direct link to Install the Scaniverse app" title="Direct link to Install the Scaniverse app">​</a>

Download the latest version of <a href="https://apps.apple.com/us/app/scaniverse-3d-scanner/id1541433223" target="_blank" rel="noopener noreferrer">Scaniverse</a> from the Apple App Store.

Existing Scaniverse users can update to **version 5.2 or later**, then switch to the **New** experience as follows:

1.  Open the Scaniverse app.
2.  Tap **LIBRARY** at the bottom of your screen.
3.  Tap the **Settings** wheel at the top of the screen.
4.  Tap **Discover the New Scaniverse**.
5.  Tap **Continue**.
6.  Log in using the email address associated with Scaniverse or authenticate with Google.

## Create a Scaniverse account<a href="#create-a-scaniverse-account" class="hash-link" aria-label="Direct link to Create a Scaniverse account" title="Direct link to Create a Scaniverse account">​</a>

You can create a Scaniverse account by [signing yourself up](#sign-yourself-up) or by [accepting an invitation](#accept-an-invitation) into an existing Organization in Scaniverse.

### Sign yourself up<a href="#sign-yourself-up" class="hash-link" aria-label="Direct link to Sign yourself up" title="Direct link to Sign yourself up">​</a>

You can sign yourself up on the [Scaniverse app](#install-the-scaniverse-app) or in <a href="https://scaniverse.nianticspatial.com/signin" target="_blank" rel="noopener noreferrer">Scaniverse Web</a>.

1.  Open the Scaniverse app or navigate to <a href="https://scaniverse.nianticspatial.com/signin" target="_blank" rel="noopener noreferrer">Scaniverse Web</a>.
2.  Select the **New** experience. You can't use the Scaniverse NSDK with the **Classic** experience.
3.  Select **Continue**.
4.  Tap **Sign up** at the bottom of the screen.
5.  Choose a sign-up method:
    - **Sign up with Email** to associate your email with your Niantic login.
    - **Sign up with Google** to authenticate with your Google account.
6.  Select the verification link sent to your email to activate your account. If you don't receive an email, check your spam or junk folder.
7.  Enter an Organization name.
8.  Select **Allow Once** or **Allow While Using App** to grant Scaniverse permission to use your location.

### Accept an invitation<a href="#accept-an-invitation" class="hash-link" aria-label="Direct link to Accept an invitation" title="Direct link to Accept an invitation">​</a>

You can also create an account by accepting an invitation from someone inside an existing Organization.

1.  Ask someone inside an existing Organization to complete the steps to [add others](#add-others-to-your-organization).
2.  Select the **Accept Invitation** link sent to your email to activate your account. If you don't receive an email, check your spam or junk folder. A web browser opens to prompt you to join Scaniverse.
3.  Enter your first and last name to **Join your team on Scaniverse**.
4.  Choose a sign-up method:
    - **Sign up with email** to associate your email with your Niantic login.
    - **Sign up with Google** to authenticate with your Google account.

Contact <a href="https://www.nianticspatial.com/capture/contact-sales?preview=true" target="_blank" rel="noopener noreferrer">Niantic's Sales team</a> if you have questions or need additional capacity for production deployments.

## Check usage quotas<a href="#check-usage-quotas" class="hash-link" aria-label="Direct link to Check usage quotas" title="Direct link to Check usage quotas">​</a>

Quotas apply per Organization. For current limits, see <a href="https://www.nianticspatial.com/pricing" target="_blank" rel="noopener noreferrer">Plans and Pricing</a>.

You can check your usage against your plan in the Scaniverse Dashboard as follows:

1.  Log in to <a href="https://scaniverse.nianticspatial.com" target="_blank" rel="noopener noreferrer">Scaniverse Web</a>.
2.  Select **Dashboard** from the left navigation bar.

If you exhaust your monthly credits, you can purchase Top Ups rather than waiting for your credits to refresh. To purchase, select **Add credits** from the Dashboard. For higher ongoing capacity, select **Contact sales** to reach out to <a href="https://www.nianticspatial.com/capture/contact-sales" target="_blank" rel="noopener noreferrer">Niantic's Sales team</a> or see <a href="https://www.nianticspatial.com/pricing" target="_blank" rel="noopener noreferrer">Plans and Pricing</a> to upgrade your plan.

## Add others to your Organization<a href="#add-others-to-your-organization" class="hash-link" aria-label="Direct link to Add others to your Organization" title="Direct link to Add others to your Organization">​</a>

You can invite someone by email to join your Organization. They do not have to have an existing Niantic account.

1.  Log in to the <a href="https://scaniverse.nianticspatial.com" target="_blank" rel="noopener noreferrer">Scaniverse Web</a>.
2.  Select your profile at the bottom of the left navigation bar.
3.  Select **Account settings**.
4.  Select the name of the Organization that you want to add a person to.
5.  Select **Send invite**.
6.  Enter their email address. You can also select **Add another** to invite more people.
7.  Select **Send invite**.
8.  Ask the person to check their email for your invitation. The link in the email expires 7 days after you invite them.

</div>

</div>
