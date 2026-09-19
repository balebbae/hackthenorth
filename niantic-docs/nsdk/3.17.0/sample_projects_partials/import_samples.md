---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/sample_projects_partials/import_samples/
title: import_samples
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# import_samples

</div>

The samples are available on our github <a href="https://github.com/niantic-lightship/ardk-samples" target="_blank" rel="noopener noreferrer">https://github.com/niantic-lightship/ardk-samples</a>

How to clone/download the samples:

<div>

<div class="collapsibleContent_i85q">

`git clone https://github.com/niantic-lightship/ardk-samples.git`

or

Download the repo from <a href="https://github.com/niantic-lightship/ardk-samples" target="_blank" rel="noopener noreferrer">https://github.com/niantic-lightship/ardk-samples</a> using the **code/download** button on **github**.

</div>

</div>

Open the samples project in Unity by pressing **Add** in **Unity Hub** and browsing to the project.

You will also need to [add an API key](https://www.nianticspatial.com/docs/nsdk/3.17.0/setup/#adding-your-api-key-to-your-unity-project) to have all samples work correctly.

### Running the Samples in Unity 2022

By default, our sample projects run on Unity **6000.0.58f2**, but you can downgrade them to version **2022.3.62f2** if you would prefer to use Unity 2022.

To downgrade the samples to Unity 2022:

1.  In **Unity Hub**, under **Installs**, install **2022.3.62f2** if you do not have it already.
2.  Under **Projects**, find the ARDK sample project. Click on the **Editor Version** and change it to **2022.3.62f2**. Then click the **Open with 2022.3.62f2** button.
3.  When the **Change Editor version?** dialog comes up, click **Change Version**.
4.  When the **Opening Project in Non-Matching Editor Installation** dialog comes up, click **Continue**.
5.  Disable the custom base Gradle template:
    1.  In the Unity top menu, click **Edit**, then **Project Settings**.
    2.  In the left-hand **Project Settings** menu, select **Player**, then click the Android tab.
    3.  Scroll down to **Publishing Settings**, then un-check the box labeled **Custom Base Gradle Template**.
6.  In the **Window** top menu, open the **Package Manager**. Select **Visual Scripting** from the package list, then, if you are using version 1.9.0 or earlier, click the **Update** button.
7.  If there are any errors, the **Enter Safe Mode?** dialog will pop up. Click **Enter Safe Mode** to fix the errors.

</div>

</div>
