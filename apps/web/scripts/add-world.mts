/**
 * Registers a local splat export as a world the viewer can open.
 *
 *   npm run world:add -- <id> <path/to/scene.spz> [--name "Display name"] [--version v1]
 *                        [--site <nianticSiteId>] [--space "Field tests"]
 *
 * Copies the file to maps/assets/worlds/<id>/<version>/scene.<ext> and writes
 * (or updates) worlds/<id>/world.json, keeping any navigationGraph / alignment
 * already present. The resulting folder mirrors the Modal Volume layout, so it
 * can be uploaded as-is:  modal volume put <volume> maps/assets/worlds/<id> worlds/<id>
 */
import { copyFileSync, existsSync, mkdirSync, readFileSync, statSync, writeFileSync } from "node:fs";
import { basename, extname, join, resolve } from "node:path";
import { parseArgs } from "node:util";
import { validateManifest, volumePath, WORLD_SCHEMA, type WorldManifest } from "../src/lib/world-manifest.ts";

const { values, positionals } = parseArgs({
  allowPositionals: true,
  options: {
    name: { type: "string" },
    version: { type: "string", default: "v1" },
    site: { type: "string" },
    space: { type: "string" },
    "assets-dir": { type: "string" },
  },
});

const [id, source] = positionals;
if (!id || !source) {
  console.error('Usage: npm run world:add -- <id> <path/to/scene.spz> [--name "Name"] [--version v1] [--site <id>] [--space "Space"]');
  process.exit(1);
}
if (!existsSync(source) || !statSync(source).isFile()) {
  console.error(`No such file: ${source}`);
  process.exit(1);
}

const SPLAT_EXT = new Set([".spz", ".ply", ".splat", ".ksplat", ".sog"]);
const ext = extname(source).toLowerCase();
if (!SPLAT_EXT.has(ext)) {
  console.error(`Unsupported splat format "${ext}". Expected one of ${[...SPLAT_EXT].join(", ")}.`);
  process.exit(1);
}

const assetsDir = resolve(
  values["assets-dir"] ?? process.env.WANDER_ASSETS_DIR ?? join(import.meta.dirname, "../../../maps/assets"),
);
const worldDir = join(assetsDir, "worlds", id);
const versionDir = join(worldDir, values.version!);
const manifestPath = join(worldDir, "world.json");
const fileName = `scene${ext}`;

mkdirSync(versionDir, { recursive: true });
copyFileSync(source, join(versionDir, fileName));

const existing: Partial<WorldManifest> = existsSync(manifestPath)
  ? JSON.parse(readFileSync(manifestPath, "utf8"))
  : {};

const manifest: WorldManifest = {
  schema: WORLD_SCHEMA,
  id,
  name: values.name ?? existing.name ?? titleCase(id),
  space: values.space ?? existing.space,
  description: existing.description,
  nianticSiteId: values.site ?? existing.nianticSiteId ?? null,
  version: values.version!,
  assets: { ...existing.assets, splat: volumePath(id, values.version!, fileName) },
  navigationGraph: existing.navigationGraph,
  alignment: existing.alignment ?? { frame: "splat", position: [0, 0, 0], rotation: [0, 0, 0, 1], scale: 1 },
  stats: { ...existing.stats, captureApp: existing.stats?.captureApp ?? "Scaniverse" },
  status: existing.status ?? (values.site ? "aligned" : "processing"),
  updatedAt: new Date().toISOString(),
};
// Drop undefined optionals so the JSON stays tidy.
const clean = JSON.parse(JSON.stringify(manifest));

const problems = validateManifest(clean);
if (problems.length) {
  console.error(`Refusing to write an invalid manifest:\n - ${problems.join("\n - ")}`);
  process.exit(1);
}
writeFileSync(manifestPath, `${JSON.stringify(clean, null, 2)}\n`);

const size = statSync(join(versionDir, fileName)).size;
console.log(`✓ ${basename(source)} → ${join(versionDir, fileName)} (${(size / 1_048_576).toFixed(1)} MB)`);
console.log(`✓ ${manifestPath}`);
console.log(`\nOpen http://localhost:3000/dashboard/worlds/${id}`);
console.log(`Upload:  modal volume put <volume-name> ${join(assetsDir, "worlds", id)} worlds/${id}`);

function titleCase(slug: string): string {
  return slug.replace(/[-_]+/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
}
