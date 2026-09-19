import type { Owner } from "@/lib/worlds";

type Props = { person: Owner; size?: number; className?: string };

/** Initials avatar in a solid accent circle; white text for contrast. */
export function Avatar({ person, size = 28, className = "" }: Props) {
  return (
    <span
      title={person.name}
      className={`inline-flex shrink-0 items-center justify-center rounded-full font-semibold text-pure-white ring-2 ring-pure-white ${className}`}
      style={{
        width: size,
        height: size,
        background: person.color,
        fontSize: Math.max(10, Math.round(size * 0.38)),
      }}
    >
      {person.initials}
    </span>
  );
}

export function AvatarStack({ people, max = 3 }: { people: Owner[]; max?: number }) {
  const shown = people.slice(0, max);
  const extra = people.length - shown.length;
  return (
    <span className="flex items-center -space-x-1.5">
      {shown.map((p) => (
        <Avatar key={p.name} person={p} size={24} />
      ))}
      {extra > 0 && (
        <span className="inline-flex size-6 items-center justify-center rounded-full bg-stellar-white text-caption font-medium text-void-black/60 ring-2 ring-pure-white">
          +{extra}
        </span>
      )}
    </span>
  );
}
