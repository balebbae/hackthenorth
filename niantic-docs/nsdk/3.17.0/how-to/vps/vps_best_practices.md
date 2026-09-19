---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/how-to/vps/vps_best_practices/
title: VPS Best Practices
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# VPS Best Practices

</div>

## The Localization User Experience<a href="#the-localization-user-experience" class="hash-link" aria-label="Direct link to The Localization User Experience" title="Direct link to The Localization User Experience">​</a>

Localization is a powerful tool that allows AR to sync up with the real world in real time and create truly magical experiences. Unfortunately, it is also a fussy process that requires precision to properly perform, something that the average player will not have much patience for. How do we reconcile this when designing an AR game? The answer is in the first-time user experience and how you explain the process of localization!

- Keep It Simple
  - Above all, remember to keep it simple. Players may have intuition for other game mechanics, but localization is a new task that they will probably fail at a few times before succeeding. If your first-time localization UX is unclear, they will quickly lose interest and stop playing.
  - Use plain language as much as possible. Keep each instruction small so that players can stay on task and not get lost.
  - Guide the player exactly to where they need to stand and the direction they need to face. Leaving room for interpretation only serves to complicate the process.
- Provide Hints
  - When creating a hint image, instead of telling the player where to stand, give them an image that exactly matches what they should see on their screen. This encourages them to point their phone in the right direction rather than directing them to a spot and then asking them to look around afterwards.
  - Make sure your hint images are human-readable and draw the eye in the same way a photograph might. A well-composed hint image creates a distinct view that your players can try to replicate when localizing.
- Use Your Scans
  - Using scans to build your points of interest means that localization is all but guaranteed if the player stands in the same spot the scan was taken from. Pulling hint images directly from the scans can be a great way to make them.
  - The most well-known image of your chosen location may not actually serve as a good localization image. Choosing a famous photo might seem like a time-saving measure, but the scans are the only images that are already guaranteed to work!
- Go Slowly
  - Hurrying while localizing results in partial localizations and poor performance. For best results, tell your players to slow down and sweep their phone slowly over the are they are trying to localize to.
- Prototype and Test
  - Make sure you hand your localization UX to people who have never worked on it or used AR localization! If they can't figure it out without your help, you may need to reconsider your first-time experience.

## Choosing Locations<a href="#choosing-locations" class="hash-link" aria-label="Direct link to Choosing Locations" title="Direct link to Choosing Locations">​</a>

When choosing a location for your AR experience, there are many different issues to consider. Before you start writing your game at all, ask yourself: is this location good for AR play? Will players be safe here if they are focused on their phones? Are players being sent to unpleasant or unsafe places? To answer these questions and many others, consider the following:

- What makes a good location to play in?
  - Safety: players should not be in danger while playing.
    - Safety means different things to different locations and cultures. For example, in London, players reported feeling unsafe walking around with their phones out because it made it easier for thieves to steal them!
    - Choose locations that are in well-traveled and well-lit public spaces.
  - Accessibility: players should be able to reach the game space, regardless of their ability.
  - Size: players need enough room to play the game without disrupting foot traffic around them.
  - Interesting features: the space should be fun and interesting to inhabit. Distinct features also help with localization issues!
  - Flavor: choosing a space that matches your game's premise can make a huge difference. For example, a game themed around Water-type Pokemon will make more sense to players if they play it near a body of water!
- Space requirements to play
  - How much space does each player need to play? Do they need to walk around an area? Do they need to swing their limbs around while playing?
  - How many players do you expect in a single session?
  - How much space does your AR experience need in order to make sense? For example, a Pokemon battle needs space for both trainers to stand and both Pokemon to animate, while a stationary puzzle doesn't move at all.
- VPS concerns during gameplay
  - Increasing the playable area of your game increases the complexity of its mesh as well. The more objects that can be in your game environment, the more meshing issues you will have.
  - VPS requires aligning the physical space to the boundaries of the mesh, so increasing that complexity creates more opportunities for a desync.
  - All of that said, the minimum space requirement for a VPS experience is **25 square meters**. This is not that much room, so you will probably need to increase it!
- Culture and safety concerns
  - Don't encourage players to enter spaces where they might be disruptive. Schools, places of worship, and similar locations should be off-limits.
  - Keep your points of interest away from unsafe or unpleasant areas, such as roads, parking lots, and urban infrastructure.
  - Players will need to take photos to localize to your game. Avoid asking them to take pictures of strangers by creating localization images from features that don't normally have people hanging out on them, such as park benches.
  - Crowdsourced location information can be wrong. Double-check any information that comes from your players before allowing a location based on it.

## Use cases to consider before using VPS<a href="#use-cases-to-consider-before-using-vps" class="hash-link" aria-label="Direct link to Use cases to consider before using VPS" title="Direct link to Use cases to consider before using VPS">​</a>

- Is my use case one where I want to choose from a set of premapped sites or one where I want to activate sites myself?
  - Are the premades good enough, or do you need control over the input data and POI quality?
- How much does it matter to you that things are persistent? What about socially interactive?
  - Better VPS/localization comes at a cost of persistence and social interactivity
  - If you want persistence, that defines what localization methods you might use

## Barriers to Localization<a href="#barriers-to-localization" class="hash-link" aria-label="Direct link to Barriers to Localization" title="Direct link to Barriers to Localization">​</a>

Like anything else, places change over time. A space that was great for localization three years ago may have changed, losing the features that made it so clearly recognizable. VPS experiences are strongly impacted by this kind of stale data, making it difficult to keep an experience running if a place changes too frequently. To mitigate these issues, consider the following:

- Fighting POI degradation
  - Over time, points of interest change, potentially losing the features originally used to localize to them. If your AR experience uses public locations, consider POIs with distinctive and permanent fixtures, like water features or statues.
- Urban spaces
  - Urban spaces are the most subject to frequent change. They will require more upkeep with regular scans to stay current.
  - Avoid localizing based on city features that might change based on factors outside your control, such as shops, signs, or tree placement.
- Self-healing systems
  - By incentivizing players to re-scan places and re-localize to them, your system can be self-healing and combat point-of-interest degradation without direct maintenance. Places that are popular for your game will see the most re-scanning, so you may still need to maintain any locations that are farther out.

## Help! My Players Can't Localize\!<a href="#help-my-players-cant-localize" class="hash-link" aria-label="Direct link to Help! My Players Can&#39;t Localize!" title="Direct link to Help! My Players Can&#39;t Localize!">​</a>

When localization fails, the reason is usually the combination of poor location choice and lack of localization technique. Following this guide helps with the former, but if your players are still having trouble localizing in your carefully-considered VPS location, these pointers may help them succeed:

- Partial localizations are a good sign! If a player is seeing a partial localization, it means they are almost there and should only need to retry once or twice to complete it.
- Tell your players to look through their phones at the real world! Localization is much harder when looking back and forth between your phone and the real world instead of simply lining it up using the phone's camera.
  - The Limited Localization Guidance system surfaces a small amount of spatial guidance by creating AR elements that point out important localization features through the phone camera. This is a good way to nudge players towards looking at the world through their device!
- Tell your players to slow down when localizing! One common mistake players make is moving their phone too quickly or jerkily while trying to localize, causing a partial when their phone only catches part of the image.
- Remind players to raise their eyes and look around! Players often point their phones at the ground when trying to localize because they want to find the "right place to stand", but the ground usually has no distinctive features and is terrible for localizing.
  - Choosing locations where the distinctive features are not on the ground can also reduce this issue.

## Miscellaneous Localization Tips<a href="#miscellaneous-localization-tips" class="hash-link" aria-label="Direct link to Miscellaneous Localization Tips" title="Direct link to Miscellaneous Localization Tips">​</a>

- Weather and season matter a lot when choosing a location! A space might be great for localization in the spring and summer but suffer greatly in the autumn and winter due to changes in local plants, snowfall, and so on.
- Avoid asking players to localize at night. Not only does nighttime come with lighting conditions that make localization more likely to fail, playing AR games at night is unsafe and carries risks.
- When creating scans for a location, take them in a variety of settings, such as at different times of day or in different weather conditions. This will increase the chance of your localization images matching those your players take when trying to play the game.
- Avoid choosing locations with lots of foot traffic for your AR experience. Humans do not stay still long enough to make good localization hint images, nor do they tend to enjoy being photographed by strangers.
- When testing your locations out, ask your players how they felt while trying to localize in that area. If they felt awkward or like they were intruding while trying to play your game, consider moving it to another location.
- Because distinct features are required for strong localization, avoid choosing areas with repeated structures, such as sets of identical park benches or statues.

</div>

</div>
