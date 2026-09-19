import { Icon, type IconName } from "@/components/Icon";

const STEPS: {
  n: string;
  title: string;
  body: string;
  icon: IconName;
  ring: string;
}[] = [
  {
    n: "01",
    title: "Capture a space",
    body: "Walk the building once with an iPhone. We turn the scan into a Gaussian splat and align it to Niantic's visual positioning system.",
    icon: "camera",
    ring: "#2e4885",
  },
  {
    n: "02",
    title: "Annotate the route",
    body: "Drop waypoints, name destinations, and write the cue for each turn in the web dashboard. Preview exactly what a walker will hear.",
    icon: "route",
    ring: "#d85598",
  },
  {
    n: "03",
    title: "Walk with guidance",
    body: "Clip the phone to a chest mount. It localizes, watches for obstacles, and speaks calm turn-by-turn directions the whole way.",
    icon: "mic",
    ring: "#60baf4",
  },
];

export function HowItWorks() {
  return (
    <section id="how-it-works" className="section scroll-mt-16">
      <div className="container-page">
        <div className="mx-auto max-w-2xl text-center">
          <h2 className="text-[32px] leading-[1.15] font-medium tracking-[-0.9px] text-balance text-void-black md:text-heading-lg md:leading-[1.1] md:tracking-[-1.7px]">
            Three steps from scan to first walk.
          </h2>
          <p className="editorial mt-4 text-balance">
            No beacons to install, no floor plans to redraw. If you can walk
            it, you can map it.
          </p>
        </div>

        <ol className="mt-12 grid gap-4 md:grid-cols-3">
          {STEPS.map((s) => (
            <li key={s.n} className="card flex flex-col">
              <div className="flex items-center justify-between">
                <span
                  aria-hidden="true"
                  className="inline-flex size-11 items-center justify-center rounded-full bg-pure-white text-void-black"
                  style={{ border: `2px solid ${s.ring}` }}
                >
                  <Icon name={s.icon} size={18} />
                </span>
                <span className="text-caption font-semibold tracking-[0.01em] text-void-black/40">
                  STEP {s.n}
                </span>
              </div>
              <h3 className="mt-6 text-heading-sm font-bold text-void-black">
                {s.title}
              </h3>
              <p className="mt-2 text-body text-graphite">{s.body}</p>
            </li>
          ))}
        </ol>
      </div>
    </section>
  );
}
