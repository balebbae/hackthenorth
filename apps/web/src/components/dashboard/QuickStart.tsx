import { Icon, type IconName } from "@/components/Icon";

const TEMPLATES: {
  icon: IconName;
  title: string;
  sub: string;
  tone: string;
}[] = [
  {
    icon: "plus",
    title: "Blank world",
    sub: "Start from an empty scene",
    tone: "bg-sky-tint text-wander-blue",
  },
  {
    icon: "upload",
    title: "Import .ply / .splat",
    sub: "Bring an existing scan",
    tone: "bg-pink-tint text-wander-pink",
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
              className="card flex w-full items-center gap-3 p-3 text-left transition-colors duration-200 hover:border-void-black/20 hover:bg-void-black/[0.02]"
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
    </section>
  );
}
