import Link from "next/link";
import { Icon } from "@/components/Icon";
import { CharacterMark, Sparkle } from "./Marks";

export function CtaBand() {
  return (
    <section className="section">
      <div className="container-page">
        <div className="card-brand relative overflow-hidden p-8 md:p-14">
          <Sparkle
            color="#ffffff"
            size={26}
            className="absolute top-6 right-8 hidden md:block"
          />
          <div className="grid items-center gap-8 md:grid-cols-[1.4fr_1fr]">
            <div>
              <h2 className="text-[32px] leading-[1.15] font-medium tracking-[-0.9px] text-pure-white md:text-heading md:leading-[1.2] md:tracking-[-1.2px]">
                Ready to map your first space?
              </h2>
              <p className="mt-3 max-w-lg text-body text-pure-white/80">
                Sign in, create a world, and have a walkable route ready before
                the coffee cools.
              </p>
              <div className="mt-6 flex flex-wrap gap-3">
                <Link href="/login" className="btn-inverted btn-lg">
                  Get started
                  <Icon name="arrowRight" size={16} />
                </Link>
                <Link
                  href="/dashboard"
                  className="btn btn-lg text-pure-white hover:bg-pure-white/10 active:bg-pure-white/15"
                >
                  Preview the dashboard
                </Link>
              </div>
            </div>
            <div className="flex items-center justify-center gap-3 md:justify-end">
              <CharacterMark icon="pin" color="#d85598" ring="#ffffff" size={48} />
              <CharacterMark icon="route" color="#2e4885" ring="#ffffff" size={48} />
              <CharacterMark icon="mic" color="#1e293b" ring="#ffffff" size={48} />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
