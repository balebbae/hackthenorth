import type { Metadata } from "next";
import { TopBar } from "@/components/dashboard/TopBar";
import { QuickStart } from "@/components/dashboard/QuickStart";
import { WorldsBrowser, type WorldView } from "@/components/dashboard/WorldsBrowser";
import { IMAGES } from "@/lib/images";
import { hasImage } from "@/lib/images.server";
import { CURRENT_USER, WORLDS, worldFromManifest } from "@/lib/worlds";
import { listWorlds } from "@/lib/worlds-api.server";

export const metadata: Metadata = { title: "Dashboard" };

/** Worlds on the volume change without a rebuild, so render per request. */
export const dynamic = "force-dynamic";

export default async function DashboardPage() {
  const live = await listWorlds().catch((err: unknown) => {
    console.error("[dashboard] worlds backend unavailable:", err);
    return [];
  });
  const liveIds = new Set(live.map((m) => m.id));

  const worlds: WorldView[] = [
    ...live.map((m) => ({ ...worldFromManifest(m, CURRENT_USER), imageReady: false })),
    ...WORLDS.filter((w) => !liveIds.has(w.id)).map((w) => ({
      ...w,
      imageReady: w.image ? hasImage(IMAGES[w.image]) : false,
    })),
  ];

  return (
    <>
      <TopBar title="Recents" crumbs={["HTN 2026"]} />
      <main className="flex-1 px-4 py-6 md:px-8 md:py-8">
        <QuickStart />
        <WorldsBrowser worlds={worlds} />
      </main>
    </>
  );
}
