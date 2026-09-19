"use client";

import { useState } from "react";
import { Icon, type IconName } from "@/components/Icon";
import { UploadSplatDialog } from "@/components/worlds/UploadSplatDialog";

const TEMPLATES: {
  icon: IconName;
  title: string;
  sub: string;
  tone: string;
  /** Opens the upload dialog; the others are placeholders for later capture flows. */
  action?: "upload";
}[] = [
  {
    icon: "plus",
    title: "Blank world",
    sub: "Create now, add the splat later",
    tone: "bg-sky-tint text-wander-blue",
    action: "upload",
  },
  {
    icon: "upload",
    title: "Import .spz / .ply",
    sub: "Bring a Scaniverse export",
    tone: "bg-pink-tint text-wander-pink",
    action: "upload",
  },
  {
    icon: "phone",
    title: "Capture with iPhone",
    sub: "Scan a space with the app",
    tone: "bg-wander-pink text-pure-white",
  },
  {
    icon: "layers",
    title: "From Niantic scan",
    sub: "Pull a VPS-aligned location",
    tone: "bg-wander-navy text-pure-white",
  },
];

/** Figma-style "start a new file" template row. */
export function QuickStart() {
  const [open, setOpen] = useState(false);
  return (
    <section aria-labelledby="quickstart-heading">
      <h2
        id="quickstart-heading"
        className="text-caption font-semibold tracking-[0.01em] text-void-black/50 uppercase"
      >
        Start a new world
      </h2>
      <ul className="mt-3 grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
        {TEMPLATES.map((t) => (
          <li key={t.title}>
            <button
              type="button"
              disabled={!t.action}
              title={t.action ? undefined : "Coming with the iOS app"}
              onClick={() => t.action && setOpen(true)}
              className="card flex w-full items-center gap-3 p-3 text-left transition-colors duration-200 hover:border-void-black/20 hover:bg-void-black/[0.02] disabled:cursor-not-allowed disabled:opacity-60 disabled:hover:border-hairline disabled:hover:bg-pure-white"
            >
              <span
                className={`inline-flex size-10 shrink-0 items-center justify-center rounded-lg ${t.tone}`}
              >
                <Icon name={t.icon} size={18} />
              </span>
              <span className="min-w-0">
                <span className="block truncate text-body-sm font-medium text-void-black">
                  {t.title}
                </span>
                <span className="block truncate text-caption text-void-black/50">
                  {t.sub}
                </span>
              </span>
            </button>
          </li>
        ))}
      </ul>
      <UploadSplatDialog open={open} mode={{ kind: "new" }} onClose={() => setOpen(false)} />
    </section>
  );
}
