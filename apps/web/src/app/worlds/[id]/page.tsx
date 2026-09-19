import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { cache } from "react";
import { WorldViewer } from "@/components/viewer/WorldViewer";
import { assetUrl } from "@/lib/world-manifest";
import { WORLDS, type WorldStatus } from "@/lib/worlds";
import { getMeasurements, getWorld, worldsSource } from "@/lib/worlds-api.server";

/** Always read the volume at request time — new exports and saved stops must show up without a rebuild. */
export const dynamic = "force-dynamic";

/** A world is viewable when it has a manifest on the volume; sample worlds still get a page. */
const resolveWorld = cache(async (id: string) => {
  const manifest = await getWorld(id);
  const sample = WORLDS.find((w) => w.id === id);
  if (!manifest && !sample) return null;
  const status: WorldStatus =
    manifest?.status ?? sample?.status ?? (manifest?.alignment ? "aligned" : "processing");
  return { manifest, name: manifest?.name ?? sample?.name ?? id, status };
});

export async function generateMetadata({ params }: PageProps<"/worlds/[id]">): Promise<Metadata> {
  const { id } = await params;
  const world = await resolveWorld(id);
  return { title: world?.name ?? "World" };
}

/** Full-viewport splat editor. Lives outside the dashboard shell so the scene is the whole page. */
export default async function WorldPage({ params }: PageProps<"/worlds/[id]">) {
  const { id } = await params;
  const world = await resolveWorld(id);
  if (!world) notFound();
  const measurements = world.manifest ? await getMeasurements(id).catch(() => []) : [];

  return (
    <main className="flex flex-1 flex-col">
      <WorldViewer
        worldId={id}
        name={world.name}
        status={world.status}
        manifest={world.manifest}
        splatUrl={world.manifest ? assetUrl(world.manifest.assets.splat) : null}
        initialMeasurements={measurements}
        source={worldsSource}
      />
    </main>
  );
}
