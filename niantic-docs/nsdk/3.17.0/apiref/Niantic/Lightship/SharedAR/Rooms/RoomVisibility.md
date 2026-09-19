---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/SharedAR/Rooms/RoomVisibility/
title: enum RoomVisibility
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# enum RoomVisibility

</div>

(Niantic.Lightship.SharedAR.Rooms.RoomVisibility)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

Visibility of the room. Public means accessible from any users using same application (API key). When the room is private, passcode is required to access.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs

enum RoomVisibility: byte {
     Unknown = 0,
        Public,
        Private,
};
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

Visibility of the room. Public means accessible from any users using same application (API key). When the room is private, passcode is required to access.

### Enum Values<a href="#enum-values" class="hash-link" aria-label="Direct link to Enum Values" title="Direct link to Enum Values">​</a>

**Public** - Publicly visible and can be found through the ExperienceService.

**Private** - Private room that can only be joined through RoomId.

</div>

</div>
