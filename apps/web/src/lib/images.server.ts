import "server-only";
import { existsSync } from "node:fs";
import { join } from "node:path";
import type { ImageAsset } from "./images";

/** True when the generated asset has been dropped into /public at `asset.src`. */
export function hasImage(asset: ImageAsset): boolean {
  return existsSync(join(process.cwd(), "public", asset.src));
}
