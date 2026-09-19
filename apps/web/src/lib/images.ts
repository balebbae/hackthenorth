/**
 * Image asset registry.
 *
 * Every placeholder in the UI points at one of these entries. Generate the
 * image with the `prompt` below, save it to `public/<src>` at roughly the
 * listed size, and the placeholder is replaced automatically on next render.
 */
export type ImageAsset = {
  id: string;
  /** Path under /public, also the URL. */
  src: string;
  alt: string;
  width: number;
  height: number;
  /** Prompt to paste into ChatGPT (or any image model) to produce this asset. */
  prompt: string;
};

const STYLE_BASE =
  "Flat, illustration-first style in the spirit of Notion's marketing site: no gradients on content, no photorealism, no 3D renders, no drop shadows on content. Cool off-white canvas #f8fafc (\"Stellar White\"), pure white surfaces with 1px hairline borders and 12px rounded corners, near-black slate text #0f172a (\"Void Black\") with alpha for hierarchy. Accent colors only as sparse punctuation, from the Wander palette: deep blue #2e4885, pink #d85598, sky blue #60baf4, navy #1e293b. Clean geometric sans-serif labels. Generous whitespace. Crisp edges suitable for a website hero.";

const SPLAT_LOOK =
  "The 3D scene is rendered as a Gaussian splat: a soft, slightly painterly point-splat texture where surfaces are made of thousands of tiny overlapping elliptical blobs, sharp near the camera and dissolving into sparse floating specks at the edges. Overlaid on the scene: a crisp flat UI route line in deep blue #2e4885 with small circular numbered waypoint markers and one pink #d85598 destination pin.";

export const IMAGES = {
  heroProduct: {
    id: "heroProduct",
    src: "/images/landing/hero-product.png",
    alt: "Wander web app showing a Gaussian splat map with a planned route beside an iPhone running the companion app",
    width: 1600,
    height: 1000,
    prompt: `Create a wide 16:10 product mockup for a navigation-assistant web app called "Wander". ${STYLE_BASE} Composition: a large browser window on the left (about 70% of the width) showing a 3D map editor. Inside the editor is a university engineering building atrium with a glass staircase and railings, rendered as a Gaussian splat. ${SPLAT_LOOK} The editor has a slim white left sidebar listing "Worlds", "Routes", "Devices" and a right panel titled "Live session" with a small route summary ("14 waypoints · 220 m · 4 min"), a battery pill, and a pale sky-blue #e9f4fe "Localized" status pill with deep blue #2e4885 text. On the right of the browser window, partially overlapping it, a flat illustration of an iPhone showing the companion app: a very large text cue "Left in 3 m", a simple horizontal audio waveform, and a bottom row with "Repeat" and "Pause" buttons. Both devices sit on the cool off-white canvas. No people, no logos, no watermark text.`,
  },
  featureVoice: {
    id: "featureVoice",
    src: "/images/landing/feature-voice.png",
    alt: "iPhone screen showing a large voice cue and a waveform, next to a chest-worn phone mount illustration",
    width: 1200,
    height: 900,
    prompt: `Create a 4:3 flat illustration for a feature block titled "Hear the path, not the noise". ${STYLE_BASE} The background is solid pink #d85598 edge to edge. In the center, a white iPhone-shaped card with 12px rounded corners shows a minimal screen: very large near-black #0f172a text "Left in 3 m", a thin flat audio waveform below it in deep blue #2e4885, and a small pill reading "Obstacle ahead · low" in navy #1e293b with white text. To the left, a simple line-art figure of a person seen from the front wearing a small phone in a chest harness, drawn with a 2px white stroke and no fill. Add two or three small hand-drawn white sparkle marks and one squiggle as decorative punctuation. No gradients, no shadows, no extra text.`,
  },
  featureVision: {
    id: "featureVision",
    src: "/images/landing/feature-vision.png",
    alt: "Camera view from chest height with flat outlines highlighting a doorway, a bench, and a person ahead",
    width: 1200,
    height: 900,
    prompt: `Create a 4:3 flat illustration for a feature block titled "See what your phone sees". ${STYLE_BASE} Background is solid sky blue #60baf4 edge to edge. Centered, a white card with 12px rounded corners frames a first-person view down a bright hallway drawn in a simplified flat vector style (floor, walls, a glass door at the end, a bench on the right, a person walking ahead on the left). Over the scene are crisp flat detection outlines: a pink #d85598 rounded rectangle around the bench labeled "bench · 1.8 m", a navy #1e293b outline around the person labeled "person · 4 m", and a deep blue #2e4885 dotted path line on the floor curving around the bench. A small white pill in the corner reads "Chest cam · 30 fps". No photorealism, no gradients, no shadows, no other text.`,
  },
  featureSplat: {
    id: "featureSplat",
    src: "/images/landing/feature-splat.png",
    alt: "Gaussian splat rendering of a building interior on a dark navy background with a route and waypoints",
    width: 1200,
    height: 900,
    prompt: `Create a 4:3 image for a dark feature block titled "Maps you can walk through". Background is solid navy #1e293b edge to edge with no gradient. Floating in the center is a slightly tilted 3D reconstruction of a two-storey campus building interior (atrium, stairs, corridors) with the roof removed so you can see inside like a dollhouse. ${SPLAT_LOOK} The splat blobs are lit softly in cool sky-blue #60baf4 tones so the model glows a little against the navy. Around the model, a few flat white UI chips: "Aligned to Niantic VPS", "1.2M splats", "14 waypoints". Two small hand-drawn white sparkle marks near the corners. Flat vector UI, no photorealism, no lens effects, no extra text.`,
  },
  viewerCard: {
    id: "viewerCard",
    src: "/images/landing/viewer-card.png",
    alt: "The Wander splat viewer with a route editor, waypoint list, and a mini-map",
    width: 1600,
    height: 720,
    prompt: `Create a very wide 20:9 product UI mockup of a web-based "splat viewer" for editing indoor navigation routes. ${STYLE_BASE} Layout: a white browser window with a thin top toolbar (tool icons for select, add waypoint, measure, align) and a title "Engineering 7 — Atrium". The main canvas shows a Gaussian splat of a building atrium from a slightly elevated angle. ${SPLAT_LOOK} On the right, a white panel lists numbered waypoints ("1 Entrance", "2 Elevator bank", "3 Ramp", "4 Room 7302") each with a small colored dot. Bottom-left, a small flat mini-map with a deep blue route. Cool off-white page behind the window. No people, no logos, no watermark, no extra text beyond the labels described.`,
  },
  loginSide: {
    id: "loginSide",
    src: "/images/login/side-panel.png",
    alt: "Illustration of a person walking a dotted route between waypoint pins with a chest-worn phone",
    width: 1000,
    height: 1200,
    prompt: `Create a tall 5:6 flat illustration for the side panel of a login page. ${STYLE_BASE} Background is solid pure white #ffffff edge to edge (the image will sit on a navy-to-pink-to-sky brand gradient card, so keep the artwork itself flat and white-backed). A simplified line-art person (2px navy #1e293b stroke, no fill) walks left to right wearing a small phone in a chest harness, with a white cane optional. In front of them, a dotted deep blue #2e4885 path curves across the canvas connecting three small white circular waypoint markers with 2px colored borders (deep blue, pink #d85598, sky #60baf4). At the end of the path, a pink pin outlined in navy. Scatter three or four hand-drawn navy decorative marks: a sparkle, a squiggle, a small arrow. Lots of empty white space. No gradients, no shadows, no text.`,
  },
  worldE7Atrium: {
    id: "worldE7Atrium",
    src: "/images/worlds/e7-atrium.png",
    alt: "Gaussian splat thumbnail of a university engineering building atrium",
    width: 800,
    height: 500,
    prompt: `Create a 16:10 thumbnail image of a 3D scan of a modern university engineering building atrium: a wide open hall with a glass-railed staircase, tall windows, and a polished concrete floor, seen from a slightly elevated camera. ${SPLAT_LOOK} Neutral daylight colors, warm off-white and gray tones. No people, no text, no UI chrome other than the route overlay.`,
  },
  worldMcTunnels: {
    id: "worldMcTunnels",
    src: "/images/worlds/mc-tunnels.png",
    alt: "Gaussian splat thumbnail of an underground campus tunnel corridor",
    width: 800,
    height: 500,
    prompt: `Create a 16:10 thumbnail image of a 3D scan of an underground campus pedestrian tunnel: a long concrete corridor with exposed pipes along the ceiling, fluorescent light strips, and a few wall-mounted direction signs with blank faces. ${SPLAT_LOOK} Muted beige and gray palette. No people, no readable text.`,
  },
  worldKitchenLoop: {
    id: "worldKitchenLoop",
    src: "/images/worlds/kitchen-loop.png",
    alt: "Gaussian splat thumbnail of an apartment kitchen and living room",
    width: 800,
    height: 500,
    prompt: `Create a 16:10 thumbnail image of a 3D scan of a small apartment kitchen opening into a living room: a counter with stools, a sofa, a rug, and a window with soft daylight. ${SPLAT_LOOK} Warm domestic palette with light wood and off-white walls. No people, no text.`,
  },
  worldTransitPlatform: {
    id: "worldTransitPlatform",
    src: "/images/worlds/transit-platform.png",
    alt: "Gaussian splat thumbnail of a light rail station platform",
    width: 800,
    height: 500,
    prompt: `Create a 16:10 thumbnail image of a 3D scan of an outdoor light-rail station platform: a covered platform with benches, a ticket machine, tactile paving along the platform edge, and rails leading away. ${SPLAT_LOOK} Overcast daylight, gray and blue-gray palette with one pink accent on the destination pin. No people, no readable text.`,
  },
  worldLibraryStacks: {
    id: "worldLibraryStacks",
    src: "/images/worlds/library-stacks.png",
    alt: "Gaussian splat thumbnail of library aisles with tall shelves",
    width: 800,
    height: 500,
    prompt: `Create a 16:10 thumbnail image of a 3D scan of a library floor: long parallel aisles of tall bookshelves, a reading table at the end, and carpet with a subtle pattern. ${SPLAT_LOOK} Warm wood and cream palette. No people, no readable spines or text.`,
  },
  worldCourtyardPath: {
    id: "worldCourtyardPath",
    src: "/images/worlds/courtyard-path.png",
    alt: "Gaussian splat thumbnail of an outdoor courtyard with benches and trees",
    width: 800,
    height: 500,
    prompt: `Create a 16:10 thumbnail image of a 3D scan of a campus courtyard: a paved path between lawns, two benches, three young trees, and a low brick wall, seen from a slightly elevated angle. ${SPLAT_LOOK} Fresh green and warm brick palette under soft daylight. No people, no text.`,
  },
} as const satisfies Record<string, ImageAsset>;

export type ImageId = keyof typeof IMAGES;
