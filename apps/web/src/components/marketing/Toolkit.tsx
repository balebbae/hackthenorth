import Link from "next/link";
import { ImageSlot } from "@/components/ImageSlot";
import { Icon } from "@/components/Icon";
import { IMAGES } from "@/lib/images";

const WAYPOINTS = [
  { n: 1, name: "Main entrance", tag: "Start", tagClass: "bg-sky-tint text-wander-blue" },
  { n: 2, name: "Elevator bank", tag: "Audio cue", tagClass: "bg-pink-tint text-wander-pink" },
  { n: 3, name: "Ramp to atrium", tag: "Obstacle-prone", tagClass: "bg-wander-pink text-pure-white" },
  { n: 4, name: "Room 7302", tag: "Destination", tagClass: "bg-wander-navy text-pure-white" },
];

const TELEMETRY = [
  { label: "Localization", value: "Locked · 0.3 m", tone: "bg-sky-tint text-wander-blue" },
  { label: "Chest device", value: "iPhone 15 · 82%", tone: "bg-stellar-white text-void-black/90" },
  { label: "Next cue", value: "Left in 3 m", tone: "bg-pink-tint text-wander-pink" },
  { label: "Obstacle", value: "Bench · 1.8 m", tone: "bg-wander-pink text-pure-white" },
];

/** 2×2 grid: a full-width top card and two half-width cards beneath it. */
export function Toolkit() {
  return (
    <section id="maps" className="section scroll-mt-16">
      <div className="container-page">
        <div className="max-w-2xl">
          <h2 className="text-[32px] leading-[1.15] font-medium tracking-[-0.9px] text-void-black md:text-heading-lg md:leading-[1.1] md:tracking-[-1.7px]">
            Everything the team needs to ship a route.
          </h2>
          <p className="editorial mt-4">
            One workspace for the people who scan, the people who annotate, and
            the people who walk.
          </p>
        </div>

        <div className="mt-10 grid gap-4 md:grid-cols-2">
          {/* Full-width card */}
          <article className="card md:col-span-2 md:p-8">
            <div className="grid gap-8 lg:grid-cols-[1fr_1.6fr] lg:items-center">
              <div>
                <span className="pill bg-sky-tint text-wander-blue">
                  Splat viewer
                </span>
                <h3 className="mt-4 text-heading-sm font-bold text-void-black">
                  Edit routes inside the scan itself.
                </h3>
                <p className="mt-3 text-body text-graphite">
                  Drop waypoints onto the Gaussian splat, measure distances,
                  and preview the exact voice cues a walker will hear at each
                  turn. Aligned to Niantic VPS so the map matches the world.
                </p>
                <Link
                  href="/dashboard"
                  className="btn-outline mt-6 inline-flex"
                >
                  Open the dashboard
                  <Icon name="arrowRight" size={14} />
                </Link>
              </div>
              <ImageSlot
                asset={IMAGES.viewerCard}
                sizes="(min-width: 1024px) 60vw, 100vw"
                className="rounded-lg border border-hairline"
              />
            </div>
          </article>

          {/* Waypoints */}
          <article className="card">
            <span className="pill bg-pink-tint text-wander-pink">Waypoints</span>
            <h3 className="mt-4 text-heading-sm font-bold text-void-black">
              Destinations people actually ask for.
            </h3>
            <p className="mt-3 text-body text-graphite">
              Name rooms, exits, and landmarks. Each waypoint carries its own
              cue, so &ldquo;take the ramp, not the stairs&rdquo; is baked into
              the map.
            </p>
            <ul className="mt-6 space-y-2">
              {WAYPOINTS.map((w) => (
                <li
                  key={w.n}
                  className="flex items-center justify-between gap-3 rounded-lg border border-hairline bg-pure-white px-3 py-2"
                >
                  <span className="flex items-center gap-3">
                    <span className="inline-flex size-6 items-center justify-center rounded-full bg-stellar-white text-caption font-semibold text-void-black/90">
                      {w.n}
                    </span>
                    <span className="text-body-sm font-medium text-void-black">
                      {w.name}
                    </span>
                  </span>
                  <span className={`pill-sm ${w.tagClass}`}>{w.tag}</span>
                </li>
              ))}
            </ul>
          </article>

          {/* Telemetry */}
          <article className="card">
            <span className="pill bg-wander-pink text-pure-white">Live session</span>
            <h3 className="mt-4 text-heading-sm font-bold text-void-black">
              Watch a walk as it happens.
            </h3>
            <p className="mt-3 text-body text-graphite">
              Position confidence, battery, the next cue, and any obstacle the
              chest camera has flagged, streamed to the dashboard over a
              single WebSocket.
            </p>
            <dl className="mt-6 grid gap-2 sm:grid-cols-2">
              {TELEMETRY.map((t) => (
                <div
                  key={t.label}
                  className="rounded-lg border border-hairline bg-pure-white px-3 py-2"
                >
                  <dt className="text-caption text-void-black/60">{t.label}</dt>
                  <dd className="mt-1">
                    <span className={`pill-sm ${t.tone}`}>{t.value}</span>
                  </dd>
                </div>
              ))}
            </dl>
          </article>
        </div>
      </div>
    </section>
  );
}
