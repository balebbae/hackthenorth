import type { Metadata } from "next";
import Link from "next/link";
import { Logo } from "@/components/Logo";
import { Icon } from "@/components/Icon";
import { ImageSlot } from "@/components/ImageSlot";
import { LoginForm } from "@/components/auth/LoginForm";
import { CharacterMark, Sparkle, Squiggle } from "@/components/marketing/Marks";
import { IMAGES } from "@/lib/images";

export const metadata: Metadata = { title: "Log in" };

export default function LoginPage() {
  return (
    <main className="flex flex-1 flex-col">
      <header className="container-page flex h-[var(--nav-height)] items-center justify-between">
        <Logo />
        <Link href="/" className="btn-text">
          <Icon name="arrowRight" size={14} className="rotate-180" />
          Back to site
        </Link>
      </header>

      <div className="container-page grid flex-1 items-center gap-10 pb-16 lg:grid-cols-[1fr_1fr] lg:gap-16">
        {/* Form column */}
        <section className="flex justify-center lg:justify-end">
          <div className="card w-full max-w-md p-8 md:p-10">
            <LoginForm />
          </div>
        </section>

        {/* Accent panel — hidden on small screens */}
        <aside className="hidden lg:block">
          <div className="card-brand relative p-8">
            <Sparkle
              color="#ffffff"
              size={22}
              className="absolute top-5 right-6"
            />
            <Squiggle color="#ffffff" className="absolute top-7 left-8" />
            <div className="mx-auto max-w-sm">
              <ImageSlot
                asset={IMAGES.loginSide}
                sizes="(min-width: 1024px) 28rem, 0px"
                className="rounded-lg shadow-[var(--shadow-mockup)]"
              />
            </div>
            <div className="mt-8 flex items-start gap-4">
              <div className="flex -space-x-2">
                <CharacterMark icon="pin" color="#d85598" ring="#ffffff" size={40} />
                <CharacterMark icon="route" color="#2e4885" ring="#ffffff" size={40} />
                <CharacterMark icon="mic" color="#1e293b" ring="#ffffff" size={40} />
              </div>
              <p className="font-serif text-editorial text-pure-white/90">
                &ldquo;The map is the interface. Everything else is just a
                calmer way to read it.&rdquo;
              </p>
            </div>
          </div>
        </aside>
      </div>
    </main>
  );
}
