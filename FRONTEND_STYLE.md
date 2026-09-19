# Wander — Style Reference
> a clean slate notebook under cool morning light

**Theme:** light
**Lineage:** Notion-derived layout, type, and surface rules; Wander brand palette and mark.

Wander reads like a crisp, cool-toned notebook: a stellar-white canvas (#f8fafc) that feels calm rather than clinical, generous sans typography that gives editorial weight to product copy, and color used as sparse punctuation — a pale pink pill highlights a verb, a single deep blue anchors the primary action, and a small cast of accent hues (deep blue, pink, sky, navy) paints feature-card backgrounds like sticky notes. Cards sit on the canvas with 1px hairline borders and 12px corners — no shadows, no chrome. The brand mark is a gradient orb (navy → pink → deep blue → sky); that gradient is the one place the system breaks its flat-fill rule, and it is reserved for the logo and a few designated brand surfaces. Motion is playful and springy, with 200ms ease transitions and bouncy character-mark animations that make the interface feel alive without ever being decorative.

## Tokens — Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Wander Blue | `#2e4885` | `--color-wander-blue` | Primary CTA fill, active nav accent, filled action buttons, focus rings, route lines — the single chromatic commitment in a near-monochrome system |
| Stellar White | `#f8fafc` | `--color-stellar-white` | Page canvas, hero background, section backgrounds, dashboard content area — cool off-white gives the system its calm feel |
| Pure White | `#ffffff` | `--color-pure-white` | Card surfaces, elevated panels, sidebar, logo-wall background, contrast text on dark and brand surfaces |
| Void Black | `#0f172a` | `--color-void-black` | Primary text, nav links, headings — deployed at varying alpha (100%, 95%, 90%, 60%, 40%, 20%) to build hierarchy without adding new colors |
| Charcoal | `#1e293b` | `--color-charcoal` | Dark text variant for UI moments where Void Black would feel too heavy; identical to Wander Navy |
| Stone | `#64748b` | `--color-stone` | Secondary nav text, muted helper text, deactivated button labels |
| Graphite | `#475569` | `--color-graphite` | Body text with a cool cast — the slate gray that harmonizes with the canvas; also the editorial serif color |
| Slate | `#5b6b85` | `--color-slate` | Card body text, secondary content within cards — between Stone and Graphite |
| Sky Tint | `#e9f4fe` | `--color-sky-tint` | Ghost CTA background, active sidebar item, "Aligned" status pill, tinted hover states |
| Pink Tint | `#fbe4f0` | `--color-pink-tint` | Hero highlight pill, eyebrow pills, "Processing" status pill — the soft form of the pink accent |
| Wander Pink | `#d85598` | `--color-wander-pink` | Signature accent: feature-card backgrounds, urgent status pills ("Needs review"), starred state, decorative marks |
| Wander Sky | `#60baf4` | `--color-wander-sky` | Lightest accent — feature-card backgrounds, airy washes, character-mark rings |
| Wander Navy | `#1e293b` | `--color-wander-navy` | Dark card surface, "Destination" pills, dark feature blocks — the system's 'dark mode island' |
| Hairline | `rgba(15, 23, 42, 0.08)` | `--color-hairline` | The only border color: card edges, dividers, sidebar rail, table rows |
| Brand Gradient | `linear-gradient(45deg, #60baf4 0%, #2e4885 38%, #d85598 66%, #1e293b 100%)` | `--background-image-wander` (`bg-wander`) | Logo orb and designated brand surfaces only (CTA band, login side panel). Never on content cards, buttons, or text. |

### Accent cast

Rotate through **Wander Blue → Wander Pink → Wander Navy → Wander Sky** for character-mark rings, space/project dots, avatar fills, and feature-panel backgrounds. Text on Wander Blue, Pink, and Navy is Pure White; text on Sky and the tints is Void Black or Wander Blue.

## Tokens — Typography

### NotionInter — Primary sans-serif — geometric humanist with slight quirks, deployed at 400 for body, 500 for nav/UI, 600-700 for display headings. The type-scale uses aggressive negative letter-spacing at large sizes (-4.6px at 96px, -2px at 72px) that tightens the headline to feel confident and compact rather than airy. · `--font-notioninter`
- **Substitute:** Inter (loaded via `next/font/google`, exposed as `--font-inter` → `font-sans`)
- **Weights:** 400, 500, 600, 700
- **Sizes:** 12px, 14px, 16px, 20px, 22px, 24px, 40px, 42px, 48px, 54px, 72px, 96px
- **Line height:** 0.83, 1.00, 1.04, 1.14, 1.21, 1.27, 1.33, 1.40, 1.43, 1.50
- **Letter spacing:** -0.048em at 96px, -0.036em at 42px, -0.035em at 54px, -0.028em at 72px, -0.011em at 22px, +0.01em at 12px, normal at body sizes
- **OpenType features:** `"lnum", "locl" 0`
- **Role:** Primary sans-serif — geometric humanist with slight quirks, deployed at 400 for body, 500 for nav/UI, 600-700 for display headings. The wordmark "Wander" is set in this face at 600.

### Lyon Text — Editorial serif reserved for specific body-text moments and section intros — used sparingly to give voice a literary weight, like a pull-quote in a magazine layout. Functions as a system accent, not a parallel hierarchy. · `--font-lyon-text`
- **Substitute:** Source Serif 4 (Google Fonts' current name for Source Serif Pro; exposed as `--font-source-serif` → `font-serif`)
- **Weights:** 400
- **Sizes:** 18px, 32px
- **Line height:** 1.25, 1.56
- **Color:** Graphite `#475569` on light surfaces; Pure White at 90% on brand/dark surfaces
- **Role:** Editorial serif reserved for hero subheads, section intros, and pull-quotes. Never for UI labels or navigation.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 12px | 1.33 | 0.12px | `--text-caption` |
| body-sm | 14px | 1.43 | — | `--text-body-sm` |
| body | 16px | 1.5 | — | `--text-body` |
| editorial | 18px | 1.56 | — | `--text-editorial` |
| subheading | 20px | 1 | — | `--text-subheading` |
| heading-sm | 22px | 1.27 | -0.242px | `--text-heading-sm` |
| heading | 40px | 1.5 | — | `--text-heading` |
| heading-lg | 48px | 1.5 | — | `--text-heading-lg` |
| display-sm | 54px | 1.04 | -1.89px | `--text-display-sm` |
| display | 72px | 1.21 | -2.016px | `--text-display` |
| display-lg | 96px | 1.04 | -4.608px | `--text-display-lg` |

## Tokens — Spacing & Shapes

**Base unit:** 4px

**Density:** comfortable

### Spacing Scale

| Name | Value | Token |
|------|-------|-------|
| 4 | 4px | `--spacing-4` |
| 8 | 8px | `--spacing-8` |
| 12 | 12px | `--spacing-12` |
| 16 | 16px | `--spacing-16` |
| 20 | 20px | `--spacing-20` |
| 24 | 24px | `--spacing-24` |
| 28 | 28px | `--spacing-28` |
| 32 | 32px | `--spacing-32` |
| 36 | 36px | `--spacing-36` |
| 64 | 64px | `--spacing-64` |
| 80 | 80px | `--spacing-80` |

### Border Radius

| Element | Value |
|---------|-------|
| cards | 12px |
| pills | 9999px |
| small | 4px |
| buttons | 8px |

### Layout

- **Page max-width:** 1440px
- **Section gap:** 80px
- **Card padding:** 24px
- **Element gap:** 8px
- **Nav height:** 64px
- **Dashboard sidebar:** 260px, Pure White, hairline right border

## Components

### Logo
**Role:** Brand identification in the nav, login header, dashboard workspace switcher, and footer

The mark is the Wander gradient orb, shipped as a PNG at `/brand/wander-mark.png` (also used as the app icon). Render it at 24–28px beside the wordmark "Wander" in Inter 600, 16px, letter-spacing -0.01em, Void Black. On navy or brand-gradient surfaces the wordmark switches to Pure White; the orb is unchanged. Never recolor, outline, or flatten the orb, and never place it on a busy image.

### Primary CTA Button
**Role:** Filled blue action button for the main conversion goal

Background #2e4885, text #ffffff at 14px NotionInter weight 500, border-radius 8px, padding 6px 15px. Hover #273f76, active #213666. The only chromatic filled button in a view — every other action defers to ghost or text styles.

### Inverted CTA Button
**Role:** Primary action when it sits on a brand-gradient or navy surface

Background #ffffff, text #2e4885, same geometry as the Primary CTA. Hover Sky Tint. Only used where a Wander Blue fill would lose contrast against the gradient; never on the light canvas.

### Ghost CTA Button
**Role:** Secondary action with a subtle blue tint

Background #e9f4fe (sky tint), text #2e4885 at 14px weight 500, border-radius 8px, padding 6px 15px. Pairs beside the primary CTA as the lower-commitment alternative.

### Ghost Text Button
**Role:** Minimal action button with no fill or border

Background transparent, text #0f172a at 95% alpha, border-radius 8px, padding 6px 15px. Hover adds a 5% Void Black wash. The default for tertiary actions in the hero and feature cards.

### Outlined Text Button
**Role:** Bordered button with no fill for mid-priority actions

Background transparent, text #0f172a at 90% alpha, 1px border at same color, border-radius 4px, padding 5px 10px. Used for compact inline actions like view-all links.

### Muted Nav Link
**Role:** Low-emphasis navigation item

Background transparent, text #0f172a at 54% alpha, border-radius 8px, padding 12px 16px. The default nav-item state — text darkens to full alpha on hover, never gets an underline.

### Pill Tag
**Role:** Category label or status indicator

Colored fill, border-radius 9999px, padding 4px 12px (2px 8px for the small variant), 12px weight 500. Status vocabulary: Aligned = Sky Tint bg / Wander Blue text; Processing = Pink Tint bg / Wander Pink text; Needs review = Wander Pink bg / white text; Draft = Stellar White bg / Void Black 70%; Destination = Wander Navy bg / white text.

### White Feature Card
**Role:** Standard content card on the canvas

Background #ffffff, border-radius 12px, padding 24px, 1px solid border at rgba(15,23,42,0.08), no shadow. The default card — sits on the stellar-white canvas like a sticky note. Hover may darken the border to Void Black 20%.

### Accent Feature Card
**Role:** Full-bleed colored card for feature blocks

Background one of the accent hues (#d85598, #60baf4, #1e293b, #e9f4fe, #fbe4f0), border-radius 12px, padding 24px, no border. Functions as a colored panel that paints the canvas — text inside uses #0f172a or #ffffff depending on contrast.

### Dark Feature Card
**Role:** Inverted card for dark-on-light contrast moments

Background #1e293b (Wander Navy), text #ffffff, border-radius 12px, padding 24px. Used sparingly as a 'dark mode island' on the light page — not as a full dark theme.

### Brand Gradient Surface
**Role:** Hero-level brand moment — CTA band, login side panel

Background `--background-image-wander` (45°: Sky → Wander Blue → Wander Pink → Navy, matching the logo orb), border-radius 12px, padding 24px+, text #ffffff (body at 80%). Buttons on it use the Inverted CTA plus a white text button; decorative marks are white. At most one per page, never behind body copy, never on content cards.

### Hero Highlight Pill
**Role:** Colored pill placed behind a verb in hero copy

Background Pink Tint #fbe4f0, text #0f172a, border-radius 9999px, padding 8px 24px. The signature typographic device — wraps a single word in a sentence to draw the eye and give it weight.

### Avatar Character Mark
**Role:** Decorative illustrated character in a circle

40–48px circle with 2px colored border rotating through the accent cast (Wander Blue, Wander Pink, Wander Navy, Wander Sky), flat glyph inside, white background. On brand-gradient surfaces the ring is white. Used in hero arrangements and scattered as decorative marks with squiggle/sparkle companions.

### Initials Avatar
**Role:** People in the dashboard

24–30px circle, solid fill from the accent cast (plus Stone for the fifth person), white initials at ~38% of the diameter, 2px white ring when stacked.

### Kanban Task Card
**Role:** Product UI task item in embedded product mockups

Background #ffffff, border-radius 8px, padding 8px 12px, 1px border at rgba(15,23,42,0.08), small status pill. Replicates the real product aesthetic inside marketing screenshots and dashboard mini-UIs.

### Section Header
**Role:** Large heading that opens a new content section

NotionInter weight 500-700, 48-54px, line-height 1.04-1.5, letter-spacing -1.89 to -2.016px. Color #0f172a. Followed by an optional Source Serif subhead at 18px for editorial voice.

### Logo Wall Item
**Role:** Greyscale partner/client logo

SVG logo or wordmark at native proportions, color desaturated to Void Black at 60% alpha, no individual borders or backgrounds. Centered grid layout with generous spacing — logos are treated as typography, not imagery.

### Dashboard Sidebar
**Role:** Figma-style left rail for the worlds browser

260px, Pure White, hairline right border, sticky full-height. Workspace switcher (orb + name + chevrons) → search input with ⌘K hint → primary nav (active item: Sky Tint bg, Wander Blue text) → "Spaces" list with accent-cast dots → "Devices" with online dots (Wander Blue = online) → account block pinned to the bottom.

## Do's and Don'ts

### Do
- Use #f8fafc as the page canvas and #ffffff for card surfaces — never invert this hierarchy by putting a tinted card on a white page
- Reserve #2e4885 for the single primary action per screen; all secondary actions should use ghost (#e9f4fe bg) or text styles
- Apply negative letter-spacing to all display sizes: -4.6px at 96px, -2px at 72px, -1.9px at 54px — body text stays at normal tracking
- Use 1px solid borders at rgba(15,23,42,0.08) instead of shadows to separate cards from the canvas
- Use 12px border-radius for cards and 8px for buttons; reserve 9999px for pills and hero highlight pills only
- Paint feature-block backgrounds with the accent cast (#d85598, #60baf4, #1e293b, and the two tints) rather than adding borders or shadows to create visual variety
- Use the brand gradient exactly where the brand should be felt: the logo orb, the CTA band, the login side panel
- Keep motion at 200ms with ease timing for hovers and transitions; reserve spring/bounce animations for character marks and hero elements
- Provide visible `:focus-visible` rings in Wander Blue and honor `prefers-reduced-motion`

### Don't
- Do not use pure #ffffff as the page background — the cool #f8fafc canvas is the system's signature
- Do not add shadows to content cards — the system uses hairline borders only; shadows appear only on product UI mockups and the nav bar
- Do not use multiple chromatic filled buttons in the same view — #2e4885 is the only filled button (white-inverted on brand surfaces); color variety belongs in card backgrounds
- Do not use pure #000000 — text is Void Black #0f172a, with hierarchy built through alpha (100%, 95%, 60%, 40%)
- Do not reintroduce warm accents (yellows, oranges, corals) — the cast is blue, pink, sky, navy
- Do not use the serif for UI labels or navigation — it is reserved for editorial body copy moments at 18px
- Do not apply border-radius larger than 12px to rectangular content — pills (9999px) and cards (12px) are the two shapes
- Do not use gradients on content, buttons, text, or backgrounds behind body copy — the brand gradient is the only gradient, and only on the logo and designated brand surfaces
- Do not recolor, outline, or flatten the logo orb

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Page Canvas | `#f8fafc` | Cool off-white base for the entire page and the dashboard content area |
| 1 | Card Surface | `#ffffff` | White cards, sidebar, and panels on the canvas — pure white is reserved for surfaces that need to read as 'on top of the page' |
| 2 | Accent Card Surface | `#d85598` / `#60baf4` / tints | Colored card backgrounds — feature blocks paint the canvas with single-hue fills |
| 3 | Dark Card Surface | `#1e293b` | Navy panels for dark-mode-style feature blocks — inverting the surface stack with white text |
| 4 | Brand Surface | `--background-image-wander` | The gradient orb's colors as a surface; CTA band and login panel only |

## Elevation

- **Nav (sticky):** `0px 0.7px 1.462px 0px rgb(15 23 42 / 0.02), 0px 3px 9px 0px rgb(15 23 42 / 0.04)`
- **Product UI Mockup:** `0px 4px 12px rgba(15, 23, 42, 0.1)`

## Imagery

Illustration-first, photography-free. The visual language is built from flat character marks (glyphs in 2px colored circles), abstract decorative elements (hand-drawn squiggles, sparkles, arrows), product UI mockups, and Gaussian-splat renders of real spaces. Character marks appear in the hero as a horizontal row of 7 and scatter across the page as playful punctuation. Product screenshots and splat renders are the only 'real' visuals; the hero mockup is large, centered, and casts a single drop-shadow to separate it from the canvas. The logo orb is the only gradient image. There are no lifestyle photos, no stock imagery, no abstract 3D renders. Every image asset is registered in `apps/web/src/lib/images.ts` with a generation prompt that repeats this palette; see `apps/web/IMAGE_PROMPTS.md`.

## Layout

Centered, max-width contained at ~1440px. The hero is a centered stack: character-mark row → large two-line headline with an embedded pink-tint pill → serif subhead → two-button CTA row → large product UI mockup. Below the hero, sections alternate between white-card grids and full-bleed colored accent panels. The logo wall is a centered single-row grid of greyscale wordmarks. Feature blocks use a 2-column layout (text left, colored panel right) that alternates left-right between sections. The toolkit section uses a 2×2 card grid where the top card is full-width and the bottom row splits into two equal columns. The CTA band is the page's single brand-gradient surface. Section gaps are generous (~80px). Navigation is a fixed top bar at 64px height with centered nav items and right-aligned action buttons. The dashboard is a two-column app shell: 260px white sidebar plus a canvas-colored content area with a sticky 64px top bar.

## Agent Prompt Guide

## Quick Color Reference
- text: #0f172a (build hierarchy through alpha: 100% / 95% / 60% / 40%)
- background: #f8fafc (stellar white canvas)
- card surface: #ffffff
- border: rgba(15, 23, 42, 0.08)
- primary action: #2e4885 (filled action; white-inverted on brand surfaces)
- ghost / active tint: #e9f4fe
- highlight tint: #fbe4f0
- accent cast: #2e4885, #d85598, #60baf4, #1e293b (rotate through these for rings, dots, and card backgrounds)
- brand gradient: 45°, #60baf4 → #2e4885 → #d85598 → #1e293b (logo, CTA band, login panel only)

## Example Component Prompts

1. **Hero headline with highlight pill**: Render a centered hero on #f8fafc. Headline: 'Navigation you can hear.' at 72px Inter weight 500, #0f172a, line-height 1.21, letter-spacing -2.016px. Wrap the word 'hear' in a pill: background #fbe4f0, text #0f172a, border-radius 9999px, padding 8px 24px, inline within the sentence. Subhead below at 18px Source Serif 4 weight 400, #475569, line-height 1.56.

2. **White feature card**: Create a card on the canvas. Background #ffffff, border-radius 12px, padding 24px, 1px solid border rgba(15,23,42,0.08). No shadow. Title at 22px Inter weight 700, #0f172a, letter-spacing -0.242px. Body at 16px weight 400, #475569, line-height 1.5.

3. **Accent feature block**: Create a full-bleed colored panel. Background #d85598, border-radius 12px, padding 24px. A product UI screenshot sits inside with a drop-shadow at 0px 4px 12px rgba(15,23,42,0.1) to create depth against the colored background. Alternate panels use #60baf4 and #1e293b.

4. **Primary action button**: #2e4885 background, #ffffff text at 14px weight 500, 8px radius, padding 6px 15px. Use this filled treatment for the single main CTA on the view.

5. **Brand CTA band**: Create a 12px-radius panel filled with the brand gradient (45°, #60baf4 → #2e4885 → #d85598 → #1e293b). Headline at 40px Inter weight 500 in #ffffff, body at 16px #ffffff 80%. Buttons: a white-filled button with #2e4885 text, and a white text button. Decorative white sparkle in a corner.

6. **Kanban task card (product mockup)**: Create a task card inside a product screenshot. Background #ffffff, border-radius 8px, padding 8px 12px, 1px solid border rgba(15,23,42,0.08). Task text at 14px Inter weight 500, #0f172a. Status pill: e.g. background #fbe4f0 with #d85598 text, border-radius 9999px, padding 2px 8px, font 12px.

## Decorative Marks System

Character marks (glyphs in 2px colored circles) and abstract decorative elements (squiggles, sparkles, arrows) are deployed as visual punctuation, not as illustrations with content. They cluster around hero copy, scatter near feature cards, and animate on scroll. Colors for the circle borders rotate through the accent cast: #2e4885 (blue), #d85598 (pink), #1e293b (navy), #60baf4 (sky); on brand-gradient surfaces rings and marks are white. The marks are 40-48px circles with flat glyphs inside, always on white fills. They never carry information or link to content — they exist purely to make the interface feel alive and handcrafted.

## Similar Brands

- **Linear** — Same monochrome-light approach with a single accent color, hairline-border cards, generous display typography with negative tracking, and zero shadows on content surfaces
- **Notion** — The layout, type scale, and surface rules this reference is derived from; Wander swaps the warm paper palette for a cool slate one
- **Figma** — Same playful character marks as decorative punctuation, rotating accent hues for section variety, and the file-browser dashboard pattern
- **Stripe** — Same editorial use of serif+sans pairing and a single restrained gradient as a brand signature

## Quick Start

### CSS Custom Properties

```css
:root {
  /* Colors */
  --color-wander-blue: #2e4885;
  --color-wander-pink: #d85598;
  --color-wander-sky: #60baf4;
  --color-wander-navy: #1e293b;
  --color-stellar-white: #f8fafc;
  --color-pure-white: #ffffff;
  --color-void-black: #0f172a;
  --color-charcoal: #1e293b;
  --color-stone: #64748b;
  --color-graphite: #475569;
  --color-slate: #5b6b85;
  --color-sky-tint: #e9f4fe;
  --color-pink-tint: #fbe4f0;
  --color-hairline: rgba(15, 23, 42, 0.08);
  --background-image-wander: linear-gradient(45deg, #60baf4 0%, #2e4885 38%, #d85598 66%, #1e293b 100%);

  /* Typography — Font Families */
  --font-notioninter: 'Inter', ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-lyon-text: 'Source Serif 4', ui-serif, Georgia, "Times New Roman", serif;

  /* Typography — Scale */
  --text-caption: 12px;
  --leading-caption: 1.33;
  --tracking-caption: 0.12px;
  --text-body-sm: 14px;
  --leading-body-sm: 1.43;
  --text-body: 16px;
  --leading-body: 1.5;
  --text-editorial: 18px;
  --leading-editorial: 1.56;
  --text-subheading: 20px;
  --leading-subheading: 1;
  --text-heading-sm: 22px;
  --leading-heading-sm: 1.27;
  --tracking-heading-sm: -0.242px;
  --text-heading: 40px;
  --leading-heading: 1.5;
  --text-heading-lg: 48px;
  --leading-heading-lg: 1.5;
  --text-display-sm: 54px;
  --leading-display-sm: 1.04;
  --tracking-display-sm: -1.89px;
  --text-display: 72px;
  --leading-display: 1.21;
  --tracking-display: -2.016px;
  --text-display-lg: 96px;
  --leading-display-lg: 1.04;
  --tracking-display-lg: -4.608px;

  /* Typography — Weights */
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  /* Spacing */
  --spacing-unit: 4px;
  --spacing-4: 4px;
  --spacing-8: 8px;
  --spacing-12: 12px;
  --spacing-16: 16px;
  --spacing-20: 20px;
  --spacing-24: 24px;
  --spacing-28: 28px;
  --spacing-32: 32px;
  --spacing-36: 36px;
  --spacing-64: 64px;
  --spacing-80: 80px;

  /* Layout */
  --page-max-width: 1440px;
  --section-gap: 80px;
  --card-padding: 24px;
  --element-gap: 8px;
  --nav-height: 64px;

  /* Border Radius */
  --radius-md: 4px;
  --radius-lg: 8px;
  --radius-xl: 12px;
  --radius-full: 9999px;

  /* Named Radii */
  --radius-cards: 12px;
  --radius-pills: 9999px;
  --radius-small: 4px;
  --radius-buttons: 8px;

  /* Surfaces */
  --surface-page-canvas: #f8fafc;
  --surface-card-surface: #ffffff;
  --surface-accent-card-surface: #d85598;
  --surface-dark-card-surface: #1e293b;
  --surface-brand: var(--background-image-wander);

  /* Elevation */
  --shadow-nav: 0px 0.7px 1.462px 0px rgb(15 23 42 / 0.02), 0px 3px 9px 0px rgb(15 23 42 / 0.04);
  --shadow-mockup: 0px 4px 12px rgba(15, 23, 42, 0.1);
}
```

### Tailwind v4

The live implementation is `apps/web/src/app/globals.css`. Shared component classes (`btn-primary`, `btn-ghost`, `btn-inverted`, `btn-text`, `btn-outline`, `card`, `card-accent`, `card-dark`, `card-brand`, `pill`, `pill-sm`, `highlight-pill`, `input`, `label`, `nav-link`, `section`, `container-page`, `editorial`) are defined there as `@utility` blocks.

```css
@theme {
  /* Colors */
  --color-wander-blue: #2e4885;
  --color-wander-pink: #d85598;
  --color-wander-sky: #60baf4;
  --color-wander-navy: #1e293b;
  --color-stellar-white: #f8fafc;
  --color-pure-white: #ffffff;
  --color-void-black: #0f172a;
  --color-charcoal: #1e293b;
  --color-stone: #64748b;
  --color-graphite: #475569;
  --color-slate: #5b6b85;
  --color-sky-tint: #e9f4fe;
  --color-pink-tint: #fbe4f0;
  --color-hairline: rgba(15, 23, 42, 0.08);

  /* Brand gradient → `bg-wander` */
  --background-image-wander: linear-gradient(45deg, #60baf4 0%, #2e4885 38%, #d85598 66%, #1e293b 100%);

  /* Typography */
  --font-sans: var(--font-inter), ui-sans-serif, system-ui, sans-serif;
  --font-serif: var(--font-source-serif), ui-serif, Georgia, serif;

  /* Typography — Scale (each size carries its own line-height / letter-spacing) */
  --text-caption: 12px;
  --text-caption--line-height: 1.33;
  --text-caption--letter-spacing: 0.12px;
  --text-body-sm: 14px;
  --text-body-sm--line-height: 1.43;
  --text-body: 16px;
  --text-body--line-height: 1.5;
  --text-editorial: 18px;
  --text-editorial--line-height: 1.56;
  --text-subheading: 20px;
  --text-subheading--line-height: 1;
  --text-heading-sm: 22px;
  --text-heading-sm--line-height: 1.27;
  --text-heading-sm--letter-spacing: -0.242px;
  --text-heading: 40px;
  --text-heading--line-height: 1.5;
  --text-heading-lg: 48px;
  --text-heading-lg--line-height: 1.5;
  --text-display-sm: 54px;
  --text-display-sm--line-height: 1.04;
  --text-display-sm--letter-spacing: -1.89px;
  --text-display: 72px;
  --text-display--line-height: 1.21;
  --text-display--letter-spacing: -2.016px;
  --text-display-lg: 96px;
  --text-display-lg--line-height: 1.04;
  --text-display-lg--letter-spacing: -4.608px;

  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 4px;
  --radius-lg: 8px;
  --radius-xl: 12px;
  --radius-full: 9999px;

  /* Elevation */
  --shadow-nav: 0px 0.7px 1.462px 0px rgb(15 23 42 / 0.02), 0px 3px 9px 0px rgb(15 23 42 / 0.04);
  --shadow-mockup: 0px 4px 12px rgba(15, 23, 42, 0.1);
}
```
