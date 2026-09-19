---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/tooling/activate_existing_location/
title: How to Activate an Existing VPS Location
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# How to Activate an Existing VPS Location

</div>

Using the Geospatial Browser, you can view and interact with locations on the Niantic Map and activate existing locations in your area. If you want to activate a new location, instead see [How to Create a Public Location](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/tooling/create_vps_activated_location/).

## Prerequisites<a href="#prerequisites" class="hash-link" aria-label="Direct link to Prerequisites" title="Direct link to Prerequisites">​</a>

1.  You must have an account set up on the <a href="https://lightship.dev" target="_blank" rel="noopener noreferrer">Niantic Spatial Platform website</a>.

## Activating an Existing Location<a href="#activating-an-existing-location" class="hash-link" aria-label="Direct link to Activating an Existing Location" title="Direct link to Activating an Existing Location">​</a>

To activate an existing VPS Location:

1.  Sign in to the <a href="https://lightship.dev" target="_blank" rel="noopener noreferrer">Niantic Spatial Platform website</a>, then click **Geospatial Browser** in the left-hand menu.

2.  Using the map or the search bar, find the location you want to activate.

3.  Select your location, then click **View Details** in its information box.

    <img src="https://www.nianticspatial.com/docs/assets/images/gsb_view_details-878b2a3f91e0acf36e07bd0d00d48599.png" style="width:70.0%" alt="Viewing location details in the Geospatial Browser" />

4.  For locations that have never been activated, verify that the location has ten scans with a five-hour difference between them and that the **Activation Status** meter says **Ready to Activate**, then click **Activate**.

    <img src="https://www.nianticspatial.com/docs/assets/images/gsb_ready_to_activate-e4731d61d4ae2a39da86952b58e5f32e.png" style="width:70.0%" alt="A ready-to-activate location in the Geospatial Browser" />

    <div class="theme-admonition theme-admonition-info admonition_xJq3 alert alert--info">

    <div class="admonitionHeading_Gvgb">

    <span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)</span>info

    </div>

    <div class="admonitionContent_BuS1">

    If the location needs more scans to be ready for activation, see [Browsing The Geospatial Browser Map In Scaniverse](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/tooling/lightship_scaniverse/#browsing-the-gsb-map-in-scaniverse) for instructions on how to add scans. The location must have **two sets of five scans** with a **minimum of five hours** between when they were taken. For example, if the first five scans were taken at 8am, the other five scans must be taken later than 3pm.

    </div>

    </div>

5.  For locations that need reactivation, you will need to refresh them by submitting five new scans. Follow the instructions on [Browsing The Geospatial Browser Map In Scaniverse](https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/tooling/lightship_scaniverse/#browsing-the-gsb-map-in-scaniverse) to create and submit the scans, then return to this page and click **Reactivate Location**.

    <img src="https://www.nianticspatial.com/docs/assets/images/gsb_reactivate-6791761ee2c280dc09780fbd8718f2f3.png" style="width:70.0%" alt="A location ready for reactivation in the Geospatial Browser" />

6.  Once you have submitted your request, the activation status should change to **Processing**. This process usually takes around five hours. Once the location is activated, you will be able to see its mesh and localize against it.

If you have issues with the activation process, [contact us](https://www.nianticspatial.com/docs/nsdk/3.17.0/contact_us/).

</div>

</div>
