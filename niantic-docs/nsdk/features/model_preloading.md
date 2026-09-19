---
source: https://www.nianticspatial.com/docs/nsdk/features/model_preloading/
title: Preloading the Model File
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Neural Network Model Preloading

</div>

NSDK's awareness features rely on neural network models to know how to draw each pixel in an AR environment. Because these models are not included with NSDK, the SDK must download them the first time an awareness feature starts, resulting in long load times that can negatively impact the user experience. To prevent this download delay, NSDK provides the Model Preloading feature, allowing applications to download the model beforehand and reduce startup latency when using awareness features. (There will still be some latency because of the time that model initialization takes, just not as much as downloading the full model.)

Applications can either register an existing local model file or request that NSDK download one.

## Known Limitations<a href="#known-limitations" class="hash-link" aria-label="Direct link to Known Limitations" title="Direct link to Known Limitations">​</a>

- Model decryption still occurs when the feature starts, so some latency is still expected when starting awareness features.
- NSDK resets to the default model file definitions at startup, and custom local model file registrations from previous sessions are not retained. To use a local model file downloaded by the application, the application must register the file(s) with `RegisterModel` at the start of each AR session.

## More Information<a href="#more-information" class="hash-link" aria-label="Direct link to More Information" title="Direct link to More Information">​</a>

See [How to Use Neural Network Model Preloading](https://www.nianticspatial.com/docs/nsdk/how-to/ar/use_model_preloading/) for details on using this feature in your NSDK project.

</div>

</div>
