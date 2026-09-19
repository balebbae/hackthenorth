"use client";

import { useEffect, useRef, useState } from "react";
import { parseQueries, sortQueries, type LocalizationQuery } from "@/lib/localization";

export type FeedState = {
  queries: LocalizationQuery[];
  /** True while the browser tab is visible and polling. */
  live: boolean;
  error: string | null;
  /** Wall-clock ms of the last successful poll. */
  fetchedAt: number | null;
};

const POLL_MS = 1000;
const ERROR_BACKOFF_MS = 4000;
const LIMIT = 30;

/**
 * Polls `/api/worlds/:id/localizations` about once a second while the tab is
 * visible, merging new VPS image queries into a newest-first list. Records are
 * immutable once stored, so merging is by id and nothing ever re-renders the
 * same query twice.
 */
export function useLocalizationFeed(worldId: string, initial: LocalizationQuery[], enabled: boolean): FeedState {
  const [queries, setQueries] = useState(() => sortQueries(initial));
  const [error, setError] = useState<string | null>(null);
  const [fetchedAt, setFetchedAt] = useState<number | null>(null);
  const [polling, setLive] = useState(false);
  const known = useRef(new Set(initial.map((q) => q.id)));

  useEffect(() => {
    if (!enabled) return;
    let cancelled = false;
    let timer: ReturnType<typeof setTimeout> | undefined;
    const controller = new AbortController();

    const schedule = (ms: number) => {
      if (cancelled) return;
      clearTimeout(timer);
      timer = setTimeout(tick, ms);
    };

    const tick = async () => {
      if (cancelled) return;
      if (document.visibilityState === "hidden") {
        setLive(false);
        return; // resumed by the visibilitychange listener
      }
      setLive(true);
      try {
        const res = await fetch(`/api/worlds/${encodeURIComponent(worldId)}/localizations?limit=${LIMIT}`, {
          cache: "no-store",
          signal: controller.signal,
        });
        if (!res.ok) throw new Error((await res.json().catch(() => null))?.error ?? `Feed failed (${res.status})`);
        const fresh = parseQueries(await res.json());
        if (cancelled) return;
        const added = fresh.filter((q) => !known.current.has(q.id));
        if (added.length) {
          for (const q of added) known.current.add(q.id);
          setQueries((list) => sortQueries([...added, ...list]).slice(0, LIMIT * 2));
        }
        setError(null);
        setFetchedAt(Date.now());
        schedule(POLL_MS);
      } catch (err) {
        if (cancelled || (err instanceof DOMException && err.name === "AbortError")) return;
        setError(err instanceof Error ? err.message : "Feed failed");
        schedule(ERROR_BACKOFF_MS);
      }
    };

    const onVisible = () => {
      if (document.visibilityState === "visible") schedule(0);
    };
    document.addEventListener("visibilitychange", onVisible);
    schedule(0);

    return () => {
      cancelled = true;
      clearTimeout(timer);
      controller.abort();
      document.removeEventListener("visibilitychange", onVisible);
    };
  }, [worldId, enabled]);

  return { queries, live: enabled && polling, error, fetchedAt };
}

/** Re-renders on an interval so "3 s ago" labels stay honest without calling `Date.now()` in render. */
export function useNow(intervalMs = 1000): number {
  const [now, setNow] = useState(() => Date.now());
  useEffect(() => {
    const t = setInterval(() => setNow(Date.now()), intervalMs);
    return () => clearInterval(t);
  }, [intervalMs]);
  return now;
}

/** A phone is "online" when its newest query is this recent. */
export const PHONE_ONLINE_MS = 15_000;
