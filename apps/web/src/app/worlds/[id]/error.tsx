"use client";

import Link from "next/link";
import { Icon } from "@/components/Icon";

/** Shown when the worlds backend can't be reached while opening a world. */
export default function WorldError({ reset }: { reset: () => void }) {
  return (
    <main className="flex flex-1 items-center justify-center p-6">
      <div className="card w-full max-w-sm text-center">
        <span className="mx-auto inline-flex size-11 items-center justify-center rounded-full border-2 border-wander-pink bg-pure-white text-wander-pink">
          <Icon name="x" size={18} />
        </span>
        <p className="mt-4 text-body font-medium text-void-black">Worlds backend unavailable</p>
        <p className="mt-1 text-body-sm text-graphite">
          The FastAPI service that fronts the Modal Volume didn&apos;t answer or rejected the key. Check{" "}
          <code>WANDER_API_URL</code> and <code>WANDER_API_KEY</code>, or unset the URL to read from{" "}
          <code>maps/assets</code>.
        </p>
        <div className="mt-4 flex justify-center gap-2">
          <button type="button" className="btn-ghost" onClick={reset}>
            <Icon name="refresh" size={15} />
            Try again
          </button>
          <Link href="/dashboard" className="btn-text">
            Back to worlds
          </Link>
        </div>
      </div>
    </main>
  );
}
