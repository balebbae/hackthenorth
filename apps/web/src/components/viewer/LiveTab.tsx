"use client";

import Image from "next/image";
import type { ReactNode } from "react";
import { Icon } from "@/components/Icon";
import {
  formatAge,
  humanError,
  queryImageUrl,
  queryOutcome,
  querySucceeded,
  type LocalizationQuery,
} from "@/lib/localization";
import { ConnectPhoneQR, type ConnectPhoneInfo } from "@/components/worlds/ConnectPhoneQR";
import { formatMetres } from "./SplatViewerEngine";
import { PHONE_ONLINE_MS, useNow, type FeedState } from "./useLocalizationFeed";

export type LiveTabProps = {
  feed: FeedState;
  /** The query drawn on the splat; null when there is nothing yet. */
  selected: LocalizationQuery | null;
  /** True while the newest query is auto-selected as it arrives. */
  pinnedToLatest: boolean;
  onSelectQuery: (id: string | null) => void;
  followPhone: boolean;
  onFollowPhone: (on: boolean) => void;
  onFocusPhone: () => void;
  onViewFromPhone: () => void;
  hasSplat: boolean;
  /** QR hand-off for this world; null when the world has no manifest yet. */
  connectInfo: ConnectPhoneInfo | null;
  onConnectPhone: () => void;
};

/** Status vocabulary from FRONTEND_STYLE: sky tint = good, pink tint = degraded, pink fill = needs attention. */
const TONE_PILL = {
  ok: "bg-sky-tint text-wander-blue",
  warn: "bg-pink-tint text-wander-pink",
  bad: "bg-wander-pink text-pure-white",
} as const;

const TONE_DOT = {
  ok: "bg-wander-blue",
  warn: "bg-wander-pink/60",
  bad: "bg-wander-pink",
} as const;

/** Right-hand panel tab: the phone's latest VPS image query and where it landed on the splat. */
export function LiveTab(p: LiveTabProps) {
  const now = useNow(1000);
  const { queries, live, error, fetchedAt } = p.feed;
  const latest = queries[0] ?? null;
  const freshMs = latest ? now - Date.parse(latest.capturedAt) : Infinity;
  const phoneOnline = freshMs < PHONE_ONLINE_MS;

  if (!latest) {
    return (
      <div className="p-4">
        <div className="flex items-center gap-2">
          <LiveDot live={live} online={false} />
          <p className="text-body-sm font-medium text-void-black">{live ? "Waiting for the phone" : "Feed paused"}</p>
        </div>
        {p.connectInfo ? (
          <>
            <p className="mt-3 text-body-sm text-void-black/60">
              Scan this on the front phone (Settings › <strong>Scan world QR</strong>, or the iOS Camera). It picks up
              the world, its Niantic site and the backend; every frame the SDK sends to VPS then shows up here within a
              second, drawn on the splat where it was localized.
            </p>
            <div className="mt-4">
              <ConnectPhoneQR info={p.connectInfo} size={200} compact />
            </div>
            <p className="mt-3 text-caption text-void-black/50">
              Still needed on the phone itself: the Niantic developer token and the backend API key (LocalConfig.plist or
              Settings), and <em>Upload query images</em> switched on.
            </p>
          </>
        ) : (
          <p className="mt-3 text-body-sm text-void-black/60">
            Add a world.json (upload a splat) before a phone can localize into this world.
          </p>
        )}
        {error && <FeedError error={error} />}
      </div>
    );
  }

  const q = p.selected ?? latest;
  const outcome = queryOutcome(q);
  const imageUrl = queryImageUrl(q);
  const pose = q.result.pose;
  const aspect = q.image.width && q.image.height ? `${q.image.width} / ${q.image.height}` : "3 / 4";

  return (
    <div>
      {/* Status header */}
      <div className="flex items-center justify-between gap-2 border-b border-hairline px-4 py-3">
        <div className="flex min-w-0 items-center gap-2">
          <LiveDot live={live} online={phoneOnline} />
          <span className={`pill-sm ${TONE_PILL[outcome.tone]}`}>{outcome.label}</span>
        </div>
        <span className="shrink-0 text-caption text-void-black/50" title={new Date(q.capturedAt).toLocaleString()}>
          {formatAge(q.capturedAt, now)}
        </span>
      </div>

      {/* The query image */}
      <div className="p-3">
        <figure className="overflow-hidden rounded-xl border border-hairline bg-wander-navy">
          <div className="relative w-full" style={{ aspectRatio: aspect }}>
            {imageUrl ? (
              <Image
                key={q.id}
                src={imageUrl}
                alt={`Camera frame the phone sent to VPS at ${new Date(q.capturedAt).toLocaleTimeString()}`}
                fill
                sizes="340px"
                unoptimized
                className="object-contain"
              />
            ) : (
              <div className="absolute inset-0 flex items-center justify-center text-caption text-pure-white/60">
                No image stored
              </div>
            )}
            {!p.pinnedToLatest && (
              <button
                type="button"
                onClick={() => p.onSelectQuery(null)}
                className="absolute top-2 left-2 rounded-lg bg-pure-white/95 px-2 py-1 text-caption font-medium text-wander-blue transition-colors duration-200 hover:bg-pure-white"
              >
                ← Back to latest
              </button>
            )}
            <span className="absolute right-2 bottom-2 rounded-lg bg-pure-white/90 px-2 py-0.5 font-mono text-[11px] text-void-black/70">
              {q.image.width}×{q.image.height}
              {q.request.latencyMs !== undefined && ` · ${q.request.latencyMs} ms`}
            </span>
          </div>
          <figcaption className="flex items-center justify-between gap-2 px-3 py-2 text-caption text-pure-white/80">
            <span className="truncate">What the phone saw</span>
            <span className="shrink-0 font-mono">{q.request.identifier.slice(0, 8)}</span>
          </figcaption>
        </figure>

        {/* Camera actions */}
        <div className="mt-3 grid grid-cols-2 gap-2">
          <button type="button" className="btn-ghost" disabled={!pose || !p.hasSplat} onClick={p.onFocusPhone}>
            <Icon name="frame" size={15} />
            Fly to phone
          </button>
          <button type="button" className="btn-text border border-hairline" disabled={!pose || !p.hasSplat} onClick={p.onViewFromPhone}>
            <Icon name="eye" size={15} />
            View from phone
          </button>
        </div>
        <label className="mt-2 flex cursor-pointer items-center justify-between gap-2 rounded-lg px-2 py-1.5 text-body-sm text-void-black/80 hover:bg-void-black/5">
          <span className="flex items-center gap-2">
            <Icon name="phone" size={15} />
            Follow the phone as it moves
          </span>
          <input
            type="checkbox"
            className="size-4 accent-wander-blue"
            checked={p.followPhone}
            onChange={(e) => p.onFollowPhone(e.target.checked)}
          />
        </label>
      </div>

      {/* Details */}
      <dl className="grid grid-cols-[auto_1fr] gap-x-4 gap-y-1.5 border-t border-hairline p-4 text-body-sm">
        <Row label="VPS request">
          <span className="capitalize">{q.request.status.replace(/([A-Z])/g, " $1").toLowerCase()}</span>
          {q.request.error && q.request.error !== "none" && (
            <span className="text-void-black/60"> · {humanError(q.request.error)}</span>
          )}
        </Row>
        <Row label="Tracking">
          <span className="capitalize">{q.result.trackingState}</span>
          {q.result.anchorState && <span className="text-void-black/60"> · anchor {q.result.anchorState}</span>}
        </Row>
        {q.result.confidence !== undefined && (
          <Row label="Confidence">
            <ConfidenceBar value={q.result.confidence} />
          </Row>
        )}
        <Row label="Position">
          {pose ? (
            <span className="font-mono text-[12px]" title="Camera position in the world frame (metres)">
              {pose.position.map((v) => v.toFixed(2)).join(", ")}
            </span>
          ) : (
            <span className="text-void-black/40">Unknown — not localized</span>
          )}
        </Row>
        {q.nearestNode && (
          <Row label="Nearest stop">
            {q.nearestNode.name ?? q.nearestNode.id}
            {q.nearestNode.distanceMetres !== undefined && (
              <span className="text-void-black/60"> · {formatMetres(q.nearestNode.distanceMetres)}</span>
            )}
            {q.offGraphMetres !== undefined && q.offGraphMetres > 0.5 && (
              <span className="text-wander-pink"> · {formatMetres(q.offGraphMetres)} off path</span>
            )}
          </Row>
        )}
        {q.image.fovDeg && (
          <Row label="Field of view">
            {Math.round(q.image.fovDeg.horizontal)}° × {Math.round(q.image.fovDeg.vertical)}°
            {q.image.orientation && <span className="text-void-black/60"> · {q.image.orientation}</span>}
          </Row>
        )}
        <Row label="Captured">{new Date(q.capturedAt).toLocaleTimeString()}</Row>
        <Row label="Device">
          <span className="font-mono text-[12px]">{q.deviceId.slice(0, 8)}</span>
          {q.role && <span className="text-void-black/60"> · {q.role}</span>}
          {q.request.frameMatch && q.request.frameMatch !== "exact" && (
            <span className="text-void-black/40"> · frame {q.request.frameMatch}</span>
          )}
        </Row>
      </dl>

      {/* Recent queries */}
      <div className="border-t border-hairline p-4">
        <div className="flex items-center justify-between">
          <h3 className="text-caption font-semibold tracking-[0.01em] text-void-black/50 uppercase">Recent queries</h3>
          <span className="text-caption text-void-black/40">
            {queries.filter(querySucceeded).length}/{queries.length} localized
          </span>
        </div>
        <ol className="mt-2 flex gap-1.5 overflow-x-auto pb-1" aria-label="Recent image queries">
          {queries.slice(0, 16).map((item) => {
            const isSel = item.id === q.id;
            const tone = queryOutcome(item).tone;
            const url = queryImageUrl(item);
            return (
              <li key={item.id} className="shrink-0">
                <button
                  type="button"
                  onClick={() => p.onSelectQuery(item.id === latest.id ? null : item.id)}
                  aria-pressed={isSel}
                  title={`${queryOutcome(item).label} · ${formatAge(item.capturedAt, now)}`}
                  className={`relative block h-16 w-12 overflow-hidden rounded-lg border bg-wander-navy transition-colors duration-200 ${
                    isSel ? "border-wander-blue ring-2 ring-wander-blue/30" : "border-hairline hover:border-void-black/20"
                  }`}
                >
                  {url && (
                    <Image src={url} alt="" fill sizes="48px" unoptimized className={`object-cover ${tone === "ok" ? "" : "opacity-60"}`} />
                  )}
                  <span aria-hidden="true" className={`absolute top-1 right-1 size-2 rounded-full ring-1 ring-pure-white ${TONE_DOT[tone]}`} />
                </button>
              </li>
            );
          })}
        </ol>
        <p className="mt-2 text-caption text-void-black/40">
          {live ? `Polling every second${fetchedAt ? ` · updated ${formatAge(new Date(fetchedAt).toISOString(), now)}` : ""}` : "Paused while this tab is hidden"}
        </p>
        {error && <FeedError error={error} />}
        {p.connectInfo && (
          <button type="button" className="btn-text mt-2 w-full" onClick={p.onConnectPhone}>
            <Icon name="phone" size={15} />
            Connect another phone (QR)
          </button>
        )}
      </div>
    </div>
  );
}

/* ---------------------------------------------------------------- pieces */

function LiveDot({ live, online }: { live: boolean; online: boolean }) {
  const label = !live ? "Feed paused" : online ? "Phone online" : "Phone quiet";
  return (
    <span className="relative inline-flex size-2.5 shrink-0" title={label} aria-label={label} role="img">
      {live && online && (
        <span className="absolute inline-flex size-full rounded-full bg-wander-blue opacity-60 motion-safe:animate-ping" />
      )}
      <span className={`relative inline-flex size-2.5 rounded-full ${!live ? "bg-void-black/20" : online ? "bg-wander-blue" : "bg-void-black/40"}`} />
    </span>
  );
}

function ConfidenceBar({ value }: { value: number }) {
  const pct = Math.round(Math.max(0, Math.min(1, value)) * 100);
  return (
    <span className="flex items-center gap-2">
      <span className="h-1.5 w-24 overflow-hidden rounded-full bg-void-black/10" role="meter" aria-valuenow={pct} aria-valuemin={0} aria-valuemax={100}>
        <span className="block h-full rounded-full bg-wander-blue" style={{ width: `${pct}%` }} />
      </span>
      <span className="tabular-nums">{pct}%</span>
    </span>
  );
}

function FeedError({ error }: { error: string }) {
  return (
    <p className="mt-3 rounded-lg bg-pink-tint px-2.5 py-1.5 text-caption text-wander-pink" role="alert">
      {error} — retrying
    </p>
  );
}

function Row({ label, children }: { label: string; children: ReactNode }) {
  return (
    <>
      <dt className="text-void-black/50">{label}</dt>
      <dd className="min-w-0 text-void-black">{children}</dd>
    </>
  );
}
