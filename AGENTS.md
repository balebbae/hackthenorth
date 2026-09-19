# Repository instructions

These instructions apply to the entire repository, including every application and nested directory.

## Frontend design — required

- Before creating or changing a frontend design, read [FRONTEND_STYLE.md](FRONTEND_STYLE.md) in full. It is the shared design reference for all agents working on this project.
- Follow its colors, typography, spacing, surfaces, component treatments, and motion rules for new screens and changes to existing UI. Use its shared tokens rather than introducing unrelated colors or styles. In the Next.js app, express the design through Tailwind CSS and shared CSS variables.
- Use the documented font substitutes when the original fonts are unavailable: Inter for NotionInter and Source Serif Pro for Lyon Text.
- If an example conflicts with the reference's token tables or component definitions, follow the tables and definitions. In particular, standard buttons use an 8px radius, cards use 12px, and pills use 9999px.
- Treat Notion-specific copy, screenshots, and marketing layouts as examples. Adapt the style to this navigation application; required functional content such as the Gaussian splat viewer and camera imagery remains part of the product.
- Keep controls accessible, with readable contrast, visible keyboard focus, and reduced-motion support while applying the style.
- Explicit user requests for a design override take precedence. Otherwise, use this reference consistently across frontend work.

Follow any additional framework instructions in the application directory alongside these design rules.
