---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/Settings/PrivacyData/
title: class PrivacyData
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# class PrivacyData

</div>

(Niantic.Lightship.AR.Settings.PrivacyData)

## Overview<a href="#overview" class="hash-link" aria-label="Direct link to Overview" title="Direct link to Overview">​</a>

This class contains all the data required for data management requests.

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
class PrivacyData {
   public:
       // properties
    
     string ClientId;
      string UserId;

        // methods
   
     static void SetUserId(string userId);
      static void ClearUserId();
  };
```

</div>

</div>

## Detailed Documentation<a href="#detailed-documentation" class="hash-link" aria-label="Direct link to Detailed Documentation" title="Direct link to Detailed Documentation">​</a>

This class contains all the data required for data management requests.

### Properties<a href="#properties" class="hash-link" aria-label="Direct link to Properties" title="Direct link to Properties">​</a>

#### ClientId<a href="#ClientId" class="hash-link" aria-label="Direct link to ClientId" title="Direct link to ClientId">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
string ClientId
```

</div>

</div>

This is the device Id used to identify any device. In case there is no userId, the clientId can be provided for your GDPR data requests. If you are a Lightship developer, clientId is Unity's SystemInfo.deviceUniqueIdentifier.

For your game users, it is a random Guid. In case of no userId, you have to record it. It changes if the ios/android app is uninstalled and reinstalled. It remains the same over app upgrades

#### UserId<a href="#UserId" class="hash-link" aria-label="Direct link to UserId" title="Direct link to UserId">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
string UserId
```

</div>

</div>

This is the user Id that identifies each individual end user so that their data can be identified.

### Methods<a href="#methods" class="hash-link" aria-label="Direct link to Methods" title="Direct link to Methods">​</a>

#### SetUserId<a href="#SetUserId" class="hash-link" aria-label="Direct link to SetUserId" title="Direct link to SetUserId">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static void SetUserId(string userId)
```

</div>

</div>

Sets the userId of the user when the user logs in.

    **Parameters**:

    `userId` - the userId of the user

#### ClearUserId<a href="#ClearUserId" class="hash-link" aria-label="Direct link to ClearUserId" title="Direct link to ClearUserId">​</a>

<div class="language-cs codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa">

<div class="codeBlockContent_QJqH">

``` cs
static void ClearUserId()
```

</div>

</div>

Clears the userId when the user logs out so that we can dissociate the data from that user.

</div>

</div>
