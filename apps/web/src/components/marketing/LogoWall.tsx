/** Partner/tech logos treated as typography: greyscale, no borders, generous spacing. */
const LOGOS = [
  "Niantic",
  "ARKit",
  "OpenAI",
  "Modal",
  "FastAPI",
  "Next.js",
];

export function LogoWall() {
  return (
    <section aria-label="Built with" className="border-y border-hairline bg-pure-white">
      <div className="container-page py-10">
        <p className="text-center text-caption font-medium tracking-[0.01em] text-void-black/40 uppercase">
          Built on tools teams already trust
        </p>
        <ul className="mt-6 flex flex-wrap items-center justify-center gap-x-12 gap-y-4 md:gap-x-16">
          {LOGOS.map((name) => (
            <li
              key={name}
              className="text-heading-sm font-semibold tracking-[-0.02em] text-void-black/60"
            >
              {name}
            </li>
          ))}
        </ul>
      </div>
    </section>
  );
}
