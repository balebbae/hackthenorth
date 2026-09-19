import Link from "next/link";
import { ImageSlot } from "@/components/ImageSlot";
import { Icon } from "@/components/Icon";
import { IMAGES } from "@/lib/images";
import { BRAND } from "@/lib/brand";
import { HeroMarkRow, Sparkle, Squiggle } from "./Marks";

export function Hero() {
  return (
    <section className="section relative overflow-hidden pt-16 md:pt-24">
      <div className="container-page flex flex-col items-center text-center">
        <HeroMarkRow />

        <div className="relative mt-8 max-w-4xl">
          <Sparkle
            color="#d85598"
            size={22}
            className="absolute -top-4 -left-6 hidden md:block"
          />
          <Squiggle
            color="#60baf4"
            className="absolute -right-10 bottom-2 hidden lg:block"
          />
          <h1 className="text-[40px] leading-[1.1] font-medium tracking-[-1.2px] text-void-black sm:text-display-sm md:text-display">
            Navigation
            <br />
            you can{" "}
            <span className="highlight-pill bg-pink-tint align-baseline">hear</span>
            .
          </h1>
        </div>

        <p className="editorial mt-6 max-w-2xl text-balance">
          {BRAND.name} turns real places into walkable 3D maps, then guides you
          through them with a chest-worn phone, live obstacle cues, and a calm
          voice in your ear.
        </p>

        <div className="mt-8 flex flex-wrap items-center justify-center gap-3">
          <Link href="/login" className="btn-primary btn-lg">
            Get started
            <Icon name="arrowRight" size={16} />
          </Link>
          <Link href="#how-it-works" className="btn-ghost btn-lg">
            See how it works
          </Link>
        </div>

        <p className="mt-4 text-caption text-void-black/40">
          Free for teams building accessible routes · No card required
        </p>

        <div className="mt-14 w-full max-w-6xl md:mt-20">
          <ImageSlot
            asset={IMAGES.heroProduct}
            priority
            sizes="(min-width: 1280px) 1152px, 100vw"
            className="rounded-xl border border-hairline bg-pure-white shadow-[var(--shadow-mockup)]"
          />
        </div>
      </div>
    </section>
  );
}
