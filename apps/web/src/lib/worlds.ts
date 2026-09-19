import type { ImageId } from "./images";
import { assetUrl, formatSplatCount, type WorldManifest } from "./world-manifest";

export type WorldStatus = "aligned" | "processing" | "draft" | "review";

export type Owner = { name: string; initials: string; color: string };

export type World = {
  id: string;
  name: string;
  /** Project / space the world belongs to (Figma "project" equivalent). */
  space: string;
  status: WorldStatus;
  splats: string;
  waypoints: number;
  routes: number;
  editedAt: string;
  owner: Owner;
  collaborators: Owner[];
  /** Registered illustration used as the thumbnail (sample worlds). */
  image?: ImageId;
  /** Thumbnail served from the worlds API (real worlds with `assets.thumbnail`). */
  thumbnailUrl?: string;
  starred?: boolean;
  /** True when the world comes from the volume rather than the sample list. */
  live?: boolean;
};

export function worldHref(id: string): string {
  return `/worlds/${encodeURIComponent(id)}`;
}

/** Shape a manifest from the volume into the dashboard's `World` row. */
export function worldFromManifest(m: WorldManifest, owner: Owner): World {
  const graph = m.navigationGraph;
  return {
    id: m.id,
    name: m.name,
    space: m.space ?? "Modal volume",
    status: m.status ?? (m.alignment ? "aligned" : "processing"),
    splats: formatSplatCount(m.stats?.splatCount),
    waypoints: graph?.nodes.length ?? 0,
    routes: graph?.edges.length ? 1 : 0,
    editedAt: m.updatedAt ? relativeTime(m.updatedAt) : "—",
    owner,
    collaborators: [],
    thumbnailUrl: m.assets.thumbnail ? assetUrl(m.assets.thumbnail) : undefined,
    live: true,
  };
}

function relativeTime(iso: string): string {
  const then = Date.parse(iso);
  if (Number.isNaN(then)) return "—";
  const mins = Math.max(0, Math.round((Date.now() - then) / 60_000));
  if (mins < 1) return "Just now";
  if (mins < 60) return `${mins} min ago`;
  const hours = Math.round(mins / 60);
  if (hours < 24) return `${hours} hour${hours === 1 ? "" : "s"} ago`;
  const days = Math.round(hours / 24);
  if (days === 1) return "Yesterday";
  if (days < 14) return `${days} days ago`;
  const weeks = Math.round(days / 7);
  return `${weeks} week${weeks === 1 ? "" : "s"} ago`;
}

export const STATUS_META: Record<
  WorldStatus,
  { label: string; className: string }
> = {
  aligned: { label: "Aligned", className: "bg-sky-tint text-wander-blue" },
  processing: { label: "Processing", className: "bg-pink-tint text-wander-pink" },
  draft: { label: "Draft", className: "bg-stellar-white text-void-black/70" },
  review: { label: "Needs review", className: "bg-wander-pink text-pure-white" },
};

const PEOPLE = {
  ada: { name: "Ada Chen", initials: "AC", color: "#2e4885" },
  mo: { name: "Mo Farah", initials: "MF", color: "#d85598" },
  priya: { name: "Priya Nair", initials: "PN", color: "#3a8fd0" },
  leo: { name: "Leo Marsh", initials: "LM", color: "#1e293b" },
  sam: { name: "Sam Okafor", initials: "SO", color: "#64748b" },
} satisfies Record<string, Owner>;

export const CURRENT_USER: Owner = PEOPLE.ada;

export const SPACES = [
  { id: "e7", name: "Engineering 7", worlds: 3, color: "#2e4885" },
  { id: "mc", name: "MC Building", worlds: 2, color: "#d85598" },
  { id: "field", name: "Field tests", worlds: 4, color: "#1e293b" },
  { id: "home", name: "Home loop", worlds: 1, color: "#60baf4" },
];

export const WORLDS: World[] = [
  {
    id: "w-e7-atrium",
    name: "E7 Atrium — ground floor",
    space: "Engineering 7",
    status: "aligned",
    splats: "1.2M",
    waypoints: 14,
    routes: 3,
    editedAt: "2 hours ago",
    owner: PEOPLE.ada,
    collaborators: [PEOPLE.mo, PEOPLE.priya],
    image: "worldE7Atrium",
    starred: true,
  },
  {
    id: "w-mc-tunnels",
    name: "MC tunnels to DC",
    space: "MC Building",
    status: "processing",
    splats: "3.4M",
    waypoints: 22,
    routes: 1,
    editedAt: "Yesterday",
    owner: PEOPLE.mo,
    collaborators: [PEOPLE.ada],
    image: "worldMcTunnels",
  },
  {
    id: "w-kitchen",
    name: "Kitchen loop (demo)",
    space: "Home loop",
    status: "aligned",
    splats: "480K",
    waypoints: 6,
    routes: 2,
    editedAt: "3 days ago",
    owner: PEOPLE.priya,
    collaborators: [],
    image: "worldKitchenLoop",
    starred: true,
  },
  {
    id: "w-transit",
    name: "ION platform — Uptown",
    space: "Field tests",
    status: "review",
    splats: "2.1M",
    waypoints: 9,
    routes: 1,
    editedAt: "Last week",
    owner: PEOPLE.leo,
    collaborators: [PEOPLE.sam, PEOPLE.ada, PEOPLE.mo],
    image: "worldTransitPlatform",
  },
  {
    id: "w-library",
    name: "Dana Porter stacks, L4",
    space: "Field tests",
    status: "draft",
    splats: "—",
    waypoints: 0,
    routes: 0,
    editedAt: "Last week",
    owner: PEOPLE.sam,
    collaborators: [],
    image: "worldLibraryStacks",
  },
  {
    id: "w-courtyard",
    name: "E7 courtyard path",
    space: "Engineering 7",
    status: "aligned",
    splats: "900K",
    waypoints: 11,
    routes: 2,
    editedAt: "2 weeks ago",
    owner: PEOPLE.ada,
    collaborators: [PEOPLE.leo],
    image: "worldCourtyardPath",
  },
];

export const DEVICES = [
  { name: "Chest · iPhone 15", battery: 82, online: true },
  { name: "Left · iPhone 13", battery: 41, online: true },
  { name: "Back · iPhone 12", battery: 0, online: false },
];
