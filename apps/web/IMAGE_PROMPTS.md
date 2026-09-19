# Wander — image assets and generation prompts

Every image placeholder in the web app maps to one entry below. This file is generated from
`src/lib/images.ts` (the source of truth) by `npm run image-prompts` — edit prompts there, then regenerate.

The logo is **not** a placeholder: the gradient orb already ships at `public/brand/wander-mark.png` and needs no prompt.

## How to use

1. Copy the **Prompt** for an asset into ChatGPT (or any image model).
2. Ask for the listed aspect ratio; export as PNG (WebP/JPG also work if you update the `src` in `images.ts`).
3. Save the file to `apps/web/public` at the exact **File** path.
4. Reload — `<ImageSlot>` detects the file and swaps the placeholder for the real image. No code change needed.

Tips for iterating with the model:

- Every prompt already embeds the palette below. If a result drifts warm (yellows, oranges, corals), reply
  "Use only these colors: #f8fafc, #ffffff, #0f172a, #2e4885, #d85598, #60baf4, #1e293b."
- If it adds gradients, shadows, or stray text, reply "Flat fills only, no gradients, no drop shadows, no text
  other than the labels described." The only gradient in the brand is the logo orb, and it never appears inside
  these images.
- Feature-panel images (2–4) sit on solid pink / sky / navy panels, so their backgrounds should be that exact
  color edge to edge. The login image (6) sits on the brand gradient, so it should be white-backed.

## Palette reference

| Name | Hex | Use in imagery |
|---|---|---|
| Stellar White | `#f8fafc` | page canvas behind mockups |
| Pure White | `#ffffff` | cards, device frames, chips |
| Void Black | `#0f172a` | text and line-art strokes on light surfaces |
| Wander Blue | `#2e4885` | route lines, primary UI, dotted paths |
| Wander Pink | `#d85598` | destination pins, urgent labels, one feature-panel background |
| Wander Sky | `#60baf4` | light accent, one feature-panel background |
| Wander Navy | `#1e293b` | dark feature-panel background, outlines on light art |
| Sky Tint | `#e9f4fe` | status pills, ghost buttons in mockups |
| Pink Tint | `#fbe4f0` | soft highlight pills in mockups |

## Checklist

| # | File (under `apps/web/public`) | Size | Ratio | Page |
|---|---|---|---|---|
| 1 | `/images/landing/hero-product.png` | 1600×1000 | 8:5 | Landing |
| 2 | `/images/landing/feature-voice.png` | 1200×900 | 4:3 | Landing |
| 3 | `/images/landing/feature-vision.png` | 1200×900 | 4:3 | Landing |
| 4 | `/images/landing/feature-splat.png` | 1200×900 | 4:3 | Landing |
| 5 | `/images/landing/viewer-card.png` | 1600×720 | 20:9 | Landing |
| 6 | `/images/login/side-panel.png` | 1000×1200 | 5:6 | Login |
| 7 | `/images/worlds/e7-atrium.png` | 800×500 | 8:5 | Dashboard |
| 8 | `/images/worlds/mc-tunnels.png` | 800×500 | 8:5 | Dashboard |
| 9 | `/images/worlds/kitchen-loop.png` | 800×500 | 8:5 | Dashboard |
| 10 | `/images/worlds/transit-platform.png` | 800×500 | 8:5 | Dashboard |
| 11 | `/images/worlds/library-stacks.png` | 800×500 | 8:5 | Dashboard |
| 12 | `/images/worlds/courtyard-path.png` | 800×500 | 8:5 | Dashboard |

## Landing page (`/`)

### 1. `/images/landing/hero-product.png`

- **Size:** 1600×1000 (8:5)
- **Where:** Hero product mockup beneath the headline (white card with drop shadow).
- **Alt text:** Wander web app showing a Gaussian splat map with a planned route beside an iPhone running the companion app

**Prompt**

```text
Create a wide 16:10 product mockup for a navigation-assistant web app called "Wander". Flat, illustration-first style in the spirit of Notion's marketing site: no gradients on content, no photorealism, no 3D renders, no drop shadows on content. Cool off-white canvas #f8fafc ("Stellar White"), pure white surfaces with 1px hairline borders and 12px rounded corners, near-black slate text #0f172a ("Void Black") with alpha for hierarchy. Accent colors only as sparse punctuation, from the Wander palette: deep blue #2e4885, pink #d85598, sky blue #60baf4, navy #1e293b. Clean geometric sans-serif labels. Generous whitespace. Crisp edges suitable for a website hero. Composition: a large browser window on the left (about 70% of the width) showing a 3D map editor. Inside the editor is a university engineering building atrium with a glass staircase and railings, rendered as a Gaussian splat. The 3D scene is rendered as a Gaussian splat: a soft, slightly painterly point-splat texture where surfaces are made of thousands of tiny overlapping elliptical blobs, sharp near the camera and dissolving into sparse floating specks at the edges. Overlaid on the scene: a crisp flat UI route line in deep blue #2e4885 with small circular numbered waypoint markers and one pink #d85598 destination pin. The editor has a slim white left sidebar listing "Worlds", "Routes", "Devices" and a right panel titled "Live session" with a small route summary ("14 waypoints · 220 m · 4 min"), a battery pill, and a pale sky-blue #e9f4fe "Localized" status pill with deep blue #2e4885 text. On the right of the browser window, partially overlapping it, a flat illustration of an iPhone showing the companion app: a very large text cue "Left in 3 m", a simple horizontal audio waveform, and a bottom row with "Repeat" and "Pause" buttons. Both devices sit on the cool off-white canvas. No people, no logos, no watermark text.
```

### 2. `/images/landing/feature-voice.png`

- **Size:** 1200×900 (4:3)
- **Where:** Inside the pink accent panel of the "Hear the path, not the noise." feature block.
- **Alt text:** iPhone screen showing a large voice cue and a waveform, next to a chest-worn phone mount illustration

**Prompt**

```text
Create a 4:3 flat illustration for a feature block titled "Hear the path, not the noise". Flat, illustration-first style in the spirit of Notion's marketing site: no gradients on content, no photorealism, no 3D renders, no drop shadows on content. Cool off-white canvas #f8fafc ("Stellar White"), pure white surfaces with 1px hairline borders and 12px rounded corners, near-black slate text #0f172a ("Void Black") with alpha for hierarchy. Accent colors only as sparse punctuation, from the Wander palette: deep blue #2e4885, pink #d85598, sky blue #60baf4, navy #1e293b. Clean geometric sans-serif labels. Generous whitespace. Crisp edges suitable for a website hero. The background is solid pink #d85598 edge to edge. In the center, a white iPhone-shaped card with 12px rounded corners shows a minimal screen: very large near-black #0f172a text "Left in 3 m", a thin flat audio waveform below it in deep blue #2e4885, and a small pill reading "Obstacle ahead · low" in navy #1e293b with white text. To the left, a simple line-art figure of a person seen from the front wearing a small phone in a chest harness, drawn with a 2px white stroke and no fill. Add two or three small hand-drawn white sparkle marks and one squiggle as decorative punctuation. No gradients, no shadows, no extra text.
```

### 3. `/images/landing/feature-vision.png`

- **Size:** 1200×900 (4:3)
- **Where:** Inside the sky-blue accent panel of the "See what your phone sees." feature block.
- **Alt text:** Camera view from chest height with flat outlines highlighting a doorway, a bench, and a person ahead

**Prompt**

```text
Create a 4:3 flat illustration for a feature block titled "See what your phone sees". Flat, illustration-first style in the spirit of Notion's marketing site: no gradients on content, no photorealism, no 3D renders, no drop shadows on content. Cool off-white canvas #f8fafc ("Stellar White"), pure white surfaces with 1px hairline borders and 12px rounded corners, near-black slate text #0f172a ("Void Black") with alpha for hierarchy. Accent colors only as sparse punctuation, from the Wander palette: deep blue #2e4885, pink #d85598, sky blue #60baf4, navy #1e293b. Clean geometric sans-serif labels. Generous whitespace. Crisp edges suitable for a website hero. Background is solid sky blue #60baf4 edge to edge. Centered, a white card with 12px rounded corners frames a first-person view down a bright hallway drawn in a simplified flat vector style (floor, walls, a glass door at the end, a bench on the right, a person walking ahead on the left). Over the scene are crisp flat detection outlines: a pink #d85598 rounded rectangle around the bench labeled "bench · 1.8 m", a navy #1e293b outline around the person labeled "person · 4 m", and a deep blue #2e4885 dotted path line on the floor curving around the bench. A small white pill in the corner reads "Chest cam · 30 fps". No photorealism, no gradients, no shadows, no other text.
```

### 4. `/images/landing/feature-splat.png`

- **Size:** 1200×900 (4:3)
- **Where:** Inside the navy panel of the "Maps you can walk through." feature block.
- **Alt text:** Gaussian splat rendering of a building interior on a dark navy background with a route and waypoints

**Prompt**

```text
Create a 4:3 image for a dark feature block titled "Maps you can walk through". Background is solid navy #1e293b edge to edge with no gradient. Floating in the center is a slightly tilted 3D reconstruction of a two-storey campus building interior (atrium, stairs, corridors) with the roof removed so you can see inside like a dollhouse. The 3D scene is rendered as a Gaussian splat: a soft, slightly painterly point-splat texture where surfaces are made of thousands of tiny overlapping elliptical blobs, sharp near the camera and dissolving into sparse floating specks at the edges. Overlaid on the scene: a crisp flat UI route line in deep blue #2e4885 with small circular numbered waypoint markers and one pink #d85598 destination pin. The splat blobs are lit softly in cool sky-blue #60baf4 tones so the model glows a little against the navy. Around the model, a few flat white UI chips: "Aligned to Niantic VPS", "1.2M splats", "14 waypoints". Two small hand-drawn white sparkle marks near the corners. Flat vector UI, no photorealism, no lens effects, no extra text.
```

### 5. `/images/landing/viewer-card.png`

- **Size:** 1600×720 (20:9)
- **Where:** Right side of the full-width "Splat viewer" card in the toolkit grid.
- **Alt text:** The Wander splat viewer with a route editor, waypoint list, and a mini-map

**Prompt**

```text
Create a very wide 20:9 product UI mockup of a web-based "splat viewer" for editing indoor navigation routes. Flat, illustration-first style in the spirit of Notion's marketing site: no gradients on content, no photorealism, no 3D renders, no drop shadows on content. Cool off-white canvas #f8fafc ("Stellar White"), pure white surfaces with 1px hairline borders and 12px rounded corners, near-black slate text #0f172a ("Void Black") with alpha for hierarchy. Accent colors only as sparse punctuation, from the Wander palette: deep blue #2e4885, pink #d85598, sky blue #60baf4, navy #1e293b. Clean geometric sans-serif labels. Generous whitespace. Crisp edges suitable for a website hero. Layout: a white browser window with a thin top toolbar (tool icons for select, add waypoint, measure, align) and a title "Engineering 7 — Atrium". The main canvas shows a Gaussian splat of a building atrium from a slightly elevated angle. The 3D scene is rendered as a Gaussian splat: a soft, slightly painterly point-splat texture where surfaces are made of thousands of tiny overlapping elliptical blobs, sharp near the camera and dissolving into sparse floating specks at the edges. Overlaid on the scene: a crisp flat UI route line in deep blue #2e4885 with small circular numbered waypoint markers and one pink #d85598 destination pin. On the right, a white panel lists numbered waypoints ("1 Entrance", "2 Elevator bank", "3 Ramp", "4 Room 7302") each with a small colored dot. Bottom-left, a small flat mini-map with a deep blue route. Cool off-white page behind the window. No people, no logos, no watermark, no extra text beyond the labels described.
```


## Login page (`/login`)

### 6. `/images/login/side-panel.png`

- **Size:** 1000×1200 (5:6)
- **Where:** White card on the brand-gradient side panel to the right of the login form (desktop only).
- **Alt text:** Illustration of a person walking a dotted route between waypoint pins with a chest-worn phone

**Prompt**

```text
Create a tall 5:6 flat illustration for the side panel of a login page. Flat, illustration-first style in the spirit of Notion's marketing site: no gradients on content, no photorealism, no 3D renders, no drop shadows on content. Cool off-white canvas #f8fafc ("Stellar White"), pure white surfaces with 1px hairline borders and 12px rounded corners, near-black slate text #0f172a ("Void Black") with alpha for hierarchy. Accent colors only as sparse punctuation, from the Wander palette: deep blue #2e4885, pink #d85598, sky blue #60baf4, navy #1e293b. Clean geometric sans-serif labels. Generous whitespace. Crisp edges suitable for a website hero. Background is solid pure white #ffffff edge to edge (the image will sit on a navy-to-pink-to-sky brand gradient card, so keep the artwork itself flat and white-backed). A simplified line-art person (2px navy #1e293b stroke, no fill) walks left to right wearing a small phone in a chest harness, with a white cane optional. In front of them, a dotted deep blue #2e4885 path curves across the canvas connecting three small white circular waypoint markers with 2px colored borders (deep blue, pink #d85598, sky #60baf4). At the end of the path, a pink pin outlined in navy. Scatter three or four hand-drawn navy decorative marks: a sparkle, a squiggle, a small arrow. Lots of empty white space. No gradients, no shadows, no text.
```


## Dashboard world thumbnails (`/dashboard`)

### 7. `/images/worlds/e7-atrium.png`

- **Size:** 800×500 (8:5)
- **Where:** Thumbnail for "E7 Atrium — ground floor".
- **Alt text:** Gaussian splat thumbnail of a university engineering building atrium

**Prompt**

```text
Create a 16:10 thumbnail image of a 3D scan of a modern university engineering building atrium: a wide open hall with a glass-railed staircase, tall windows, and a polished concrete floor, seen from a slightly elevated camera. The 3D scene is rendered as a Gaussian splat: a soft, slightly painterly point-splat texture where surfaces are made of thousands of tiny overlapping elliptical blobs, sharp near the camera and dissolving into sparse floating specks at the edges. Overlaid on the scene: a crisp flat UI route line in deep blue #2e4885 with small circular numbered waypoint markers and one pink #d85598 destination pin. Neutral daylight colors, warm off-white and gray tones. No people, no text, no UI chrome other than the route overlay.
```

### 8. `/images/worlds/mc-tunnels.png`

- **Size:** 800×500 (8:5)
- **Where:** Thumbnail for "MC tunnels to DC".
- **Alt text:** Gaussian splat thumbnail of an underground campus tunnel corridor

**Prompt**

```text
Create a 16:10 thumbnail image of a 3D scan of an underground campus pedestrian tunnel: a long concrete corridor with exposed pipes along the ceiling, fluorescent light strips, and a few wall-mounted direction signs with blank faces. The 3D scene is rendered as a Gaussian splat: a soft, slightly painterly point-splat texture where surfaces are made of thousands of tiny overlapping elliptical blobs, sharp near the camera and dissolving into sparse floating specks at the edges. Overlaid on the scene: a crisp flat UI route line in deep blue #2e4885 with small circular numbered waypoint markers and one pink #d85598 destination pin. Muted beige and gray palette. No people, no readable text.
```

### 9. `/images/worlds/kitchen-loop.png`

- **Size:** 800×500 (8:5)
- **Where:** Thumbnail for "Kitchen loop (demo)".
- **Alt text:** Gaussian splat thumbnail of an apartment kitchen and living room

**Prompt**

```text
Create a 16:10 thumbnail image of a 3D scan of a small apartment kitchen opening into a living room: a counter with stools, a sofa, a rug, and a window with soft daylight. The 3D scene is rendered as a Gaussian splat: a soft, slightly painterly point-splat texture where surfaces are made of thousands of tiny overlapping elliptical blobs, sharp near the camera and dissolving into sparse floating specks at the edges. Overlaid on the scene: a crisp flat UI route line in deep blue #2e4885 with small circular numbered waypoint markers and one pink #d85598 destination pin. Warm domestic palette with light wood and off-white walls. No people, no text.
```

### 10. `/images/worlds/transit-platform.png`

- **Size:** 800×500 (8:5)
- **Where:** Thumbnail for "ION platform — Uptown".
- **Alt text:** Gaussian splat thumbnail of a light rail station platform

**Prompt**

```text
Create a 16:10 thumbnail image of a 3D scan of an outdoor light-rail station platform: a covered platform with benches, a ticket machine, tactile paving along the platform edge, and rails leading away. The 3D scene is rendered as a Gaussian splat: a soft, slightly painterly point-splat texture where surfaces are made of thousands of tiny overlapping elliptical blobs, sharp near the camera and dissolving into sparse floating specks at the edges. Overlaid on the scene: a crisp flat UI route line in deep blue #2e4885 with small circular numbered waypoint markers and one pink #d85598 destination pin. Overcast daylight, gray and blue-gray palette with one pink accent on the destination pin. No people, no readable text.
```

### 11. `/images/worlds/library-stacks.png`

- **Size:** 800×500 (8:5)
- **Where:** Thumbnail for "Dana Porter stacks, L4".
- **Alt text:** Gaussian splat thumbnail of library aisles with tall shelves

**Prompt**

```text
Create a 16:10 thumbnail image of a 3D scan of a library floor: long parallel aisles of tall bookshelves, a reading table at the end, and carpet with a subtle pattern. The 3D scene is rendered as a Gaussian splat: a soft, slightly painterly point-splat texture where surfaces are made of thousands of tiny overlapping elliptical blobs, sharp near the camera and dissolving into sparse floating specks at the edges. Overlaid on the scene: a crisp flat UI route line in deep blue #2e4885 with small circular numbered waypoint markers and one pink #d85598 destination pin. Warm wood and cream palette. No people, no readable spines or text.
```

### 12. `/images/worlds/courtyard-path.png`

- **Size:** 800×500 (8:5)
- **Where:** Thumbnail for "E7 courtyard path".
- **Alt text:** Gaussian splat thumbnail of an outdoor courtyard with benches and trees

**Prompt**

```text
Create a 16:10 thumbnail image of a 3D scan of a campus courtyard: a paved path between lawns, two benches, three young trees, and a low brick wall, seen from a slightly elevated angle. The 3D scene is rendered as a Gaussian splat: a soft, slightly painterly point-splat texture where surfaces are made of thousands of tiny overlapping elliptical blobs, sharp near the camera and dissolving into sparse floating specks at the edges. Overlaid on the scene: a crisp flat UI route line in deep blue #2e4885 with small circular numbered waypoint markers and one pink #d85598 destination pin. Fresh green and warm brick palette under soft daylight. No people, no text.
```
