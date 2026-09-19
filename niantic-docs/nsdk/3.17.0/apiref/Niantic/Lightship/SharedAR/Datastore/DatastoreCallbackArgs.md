---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Datastore/DatastoreCallbackArgs/
title: struct DatastoreCallbackArgs
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# struct DatastoreCallbackArgs

</div>

(Niantic.Lightship.SharedAR.Datastore.DatastoreCallbackArgs)

Data passed in the [Datastore](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Datastore/) callback

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
struct DatastoreCallbackArgs {
        // properties
    
     DatastoreOperationType OperationType;
       Result Result;
      UInt32 RequestId;
       string Key;
       byte[] Value;
     UInt32 Version;

     // methods
   
     DatastoreCallbackArgs(
           DatastoreOperationType operationType,
           Result result,
          UInt32 requestId,
           string key,
           byte[] value,
            UInt32 version
        );
    };
```

</div>

</div>

</div>

</div>
