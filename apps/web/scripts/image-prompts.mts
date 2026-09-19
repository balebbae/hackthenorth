/**
 * Generates IMAGE_PROMPTS.md from the image registry.
 * Run with: npm run image-prompts
 */
import { writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { IMAGES } from "../src/lib/images.ts";

type Id = keyof typeof IMAGES;

const SECTIONS: { title: string; short: string; ids: Id[] }[] = [
  {
    title: "Landing page (`/`)",
    short: "Landing",
    ids: ["heroProduct", "featureVoice", "featureVision", "featureSplat", "viewerCard"],
  },
  { title: "Login page (`/login`)", short: "Login", ids: ["loginSide"] },
  {
    title: "Dashboard world thumbnails (`/dashboard`)",
    short: "Dashboard",
    ids: [
      "worldE7Atrium",
      "worldMcTunnels",
      "worldKitchenLoop",
      "worldTransitPlatform",
      "worldLibraryStacks",
      "worldCourtyardPath",
    ],
  },
];

const WHERE: Record<Id, string> = {
  heroProduct: "Hero product mockup beneath the headline (white card with drop shadow).",
  featureVoice: 'Inside the pink accent panel of the "Hear the path, not the noise." feature block.',
  featureVision: 'Inside the sky-blue accent panel of the "See what your phone sees." feature block.',
  featureSplat: 'Inside the navy panel of the "Maps you can walk through." feature block.',
  viewerCard: 'Right side of the full-width "Splat viewer" card in the toolkit grid.',
  loginSide: "White card on the brand-gradient side panel to the right of the login form (desktop only).",
  worldE7Atrium: 'Thumbnail for "E7 Atrium — ground floor".',
  worldMcTunnels: 'Thumbnail for "MC tunnels to DC".',
  worldKitchenLoop: 'Thumbnail for "Kitchen loop (demo)".',
  worldTransitPlatform: 'Thumbnail for "ION platform — Uptown".',
  worldLibraryStacks: 'Thumbnail for "Dana Porter stacks, L4".',
  worldCourtyardPath: 'Thumbnail for "E7 courtyard path".',
};

const PALETTE: [string, string, string][] = [
  ["Stellar White", "#f8fafc", "page canvas behind mockups"],
  ["Pure White", "#ffffff", "cards, device frames, chips"],
  ["Void Black", "#0f172a", "text and line-art strokes on light surfaces"],
  ["Wander Blue", "#2e4885", "route lines, primary UI, dotted paths"],
  ["Wander Pink", "#d85598", "destination pins, urgent labels, one feature-panel background"],
  ["Wander Sky", "#60baf4", "light accent, one feature-panel background"],
  ["Wander Navy", "#1e293b", "dark feature-panel background, outlines on light art"],
  ["Sky Tint", "#e9f4fe", "status pills, ghost buttons in mockups"],
  ["Pink Tint", "#fbe4f0", "soft highlight pills in mockups"],
];

function ratio(w: number, h: number) {
  const gcd = (a: number, b: number): number => (b ? gcd(b, a % b) : a);
  const d = gcd(w, h);
  return `${w / d}:${h / d}`;
}

const rows: string[] = [];
const details: string[] = [];
let n = 0;

for (const section of SECTIONS) {
  details.push(`\n## ${section.title}\n`);
  for (const id of section.ids) {
    const a = IMAGES[id];
    n++;
    rows.push(`| ${n} | \`${a.src}\` | ${a.width}×${a.height} | ${ratio(a.width, a.height)} | ${section.short} |`);
    details.push(
      [
        `### ${n}. \`${a.src}\``,
        "",
        `- **Size:** ${a.width}×${a.height} (${ratio(a.width, a.height)})`,
        `- **Where:** ${WHERE[id]}`,
        `- **Alt text:** ${a.alt}`,
        "",
        "**Prompt**",
        "",
        "```text",
        a.prompt,
        "```",
        "",
      ].join("\n"),
    );
  }
}

const out = `# Wander — image assets and generation prompts

Every image placeholder in the web app maps to one entry below. This file is generated from
\`src/lib/images.ts\` (the source of truth) by \`npm run image-prompts\` — edit prompts there, then regenerate.

The logo is **not** a placeholder: the gradient orb already ships at \`public/brand/wander-mark.png\` and needs no prompt.

## How to use

1. Copy the **Prompt** for an asset into ChatGPT (or any image model).
2. Ask for the listed aspect ratio; export as PNG (WebP/JPG also work if you update the \`src\` in \`images.ts\`).
3. Save the file to \`apps/web/public\` at the exact **File** path.
4. Reload — \`<ImageSlot>\` detects the file and swaps the placeholder for the real image. No code change needed.

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
${PALETTE.map(([name, hex, use]) => `| ${name} | \`${hex}\` | ${use} |`).join("\n")}

## Checklist

| # | File (under \`apps/web/public\`) | Size | Ratio | Page |
|---|---|---|---|---|
${rows.join("\n")}
${details.join("\n")}`;

const target = resolve(import.meta.dirname, "../IMAGE_PROMPTS.md");
writeFileSync(target, out);
console.log(`Wrote ${n} assets to ${target}`);
