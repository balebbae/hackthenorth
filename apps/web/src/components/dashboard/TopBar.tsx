import { Icon } from "@/components/Icon";
import { Logo } from "@/components/Logo";
import { UploadSplatButton } from "@/components/worlds/UploadSplatButton";
import { Avatar } from "./Avatar";
import { CURRENT_USER } from "@/lib/worlds";

type Props = { title: string; crumbs?: string[] };

/** Dashboard header: breadcrumb left, the single primary action right. */
export function TopBar({ title, crumbs = [] }: Props) {
  return (
    <header className="sticky top-0 z-30 flex h-[var(--nav-height)] items-center gap-3 border-b border-hairline bg-stellar-white px-4 md:px-8">
      <Logo className="lg:hidden" size={24} />
      <nav aria-label="Breadcrumb" className="hidden min-w-0 items-center gap-1.5 text-body-sm lg:flex">
        {crumbs.map((c) => (
          <span key={c} className="flex items-center gap-1.5 text-void-black/50">
            <span>{c}</span>
            <Icon name="chevronRight" size={14} />
          </span>
        ))}
        <h1 className="truncate font-semibold text-void-black">{title}</h1>
      </nav>

      <div className="flex-1" />

      <UploadSplatButton className="btn-ghost hidden sm:inline-flex">
        <Icon name="upload" size={15} />
        Import splat
      </UploadSplatButton>
      <UploadSplatButton className="btn-primary">
        <Icon name="plus" size={15} />
        New world
      </UploadSplatButton>
      <button type="button" className="btn-icon" aria-label="Notifications">
        <Icon name="bell" size={17} />
      </button>
      <Avatar person={CURRENT_USER} size={30} />
    </header>
  );
}
