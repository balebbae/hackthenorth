---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Rooms/RoomManagementServiceStatus/
title: enum RoomManagementServiceStatus
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# enum RoomManagementServiceStatus

</div>

(Niantic.Lightship.SharedAR.Rooms.RoomManagementServiceStatus)

Status of Room Management Service requests. Values corresponds to HTTP response codes.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs

enum RoomManagementServiceStatus: Int32 {
      Ok              = 200,
      BadRequest      = 400,
      Unauthorized    = 401,
      NotFound        = 404,
      AsyncApiFailure = 460,
};
```

</div>

</div>

</div>

</div>
