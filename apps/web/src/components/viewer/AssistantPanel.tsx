"use client";

import { useEffect, useRef, useState } from "react";
import { Icon } from "@/components/Icon";

type ChatMessage = { role: "user" | "assistant"; text: string };

type Props = { worldId: string };

const DEVICE_ID_KEY = "wander-device-id";

function deviceId(): string {
  let id = localStorage.getItem(DEVICE_ID_KEY);
  if (!id) {
    id = crypto.randomUUID();
    localStorage.setItem(DEVICE_ID_KEY, id);
  }
  return id;
}

// Minimal Web Speech API surface — not part of the standard TS DOM lib, and
// only Chrome/Edge/Safari ship it (as the vendor-prefixed webkit* global).
type SpeechRecognitionResultLike = { transcript: string };
type SpeechRecognitionEventLike = { results: ArrayLike<ArrayLike<SpeechRecognitionResultLike>> };
type SpeechRecognitionLike = {
  continuous: boolean;
  interimResults: boolean;
  lang: string;
  start: () => void;
  stop: () => void;
  onresult: ((e: SpeechRecognitionEventLike) => void) | null;
  onerror: (() => void) | null;
  onend: (() => void) | null;
};

function getSpeechRecognition(): (new () => SpeechRecognitionLike) | null {
  const w = window as unknown as {
    SpeechRecognition?: new () => SpeechRecognitionLike;
    webkitSpeechRecognition?: new () => SpeechRecognitionLike;
  };
  return w.SpeechRecognition ?? w.webkitSpeechRecognition ?? null;
}

/** Inspector tab: type or speak a question, get an answer from the building assistant
 * (POST /api/assistant/sessions, /api/assistant/query -> the FastAPI backend on Modal). */
export function AssistantPanel({ worldId }: Props) {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [sending, setSending] = useState(false);
  const [listening, setListening] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const sessionRef = useRef<string | null>(null);
  const listRef = useRef<HTMLDivElement>(null);
  const recognitionRef = useRef<SpeechRecognitionLike | null>(null);

  useEffect(() => {
    sessionRef.current = sessionStorage.getItem(`wander-assistant-session-${worldId}`);
    return () => recognitionRef.current?.stop();
  }, [worldId]);

  useEffect(() => {
    listRef.current?.scrollTo({ top: listRef.current.scrollHeight, behavior: "smooth" });
  }, [messages, sending]);

  async function ensureSession(): Promise<string> {
    if (sessionRef.current) return sessionRef.current;
    const res = await fetch("/api/assistant/sessions", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ worldId, deviceId: deviceId() }),
    });
    const body = (await res.json()) as { sessionId?: string; error?: string };
    if (!res.ok || !body.sessionId) throw new Error(body.error ?? "Could not start a session");
    sessionRef.current = body.sessionId;
    sessionStorage.setItem(`wander-assistant-session-${worldId}`, body.sessionId);
    return body.sessionId;
  }

  async function send(text: string) {
    const trimmed = text.trim();
    if (!trimmed || sending) return;
    setInput("");
    setError(null);
    setMessages((m) => [...m, { role: "user", text: trimmed }]);
    setSending(true);
    try {
      const sessionId = await ensureSession();
      const res = await fetch("/api/assistant/query", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ sessionId, text: trimmed }),
      });
      const body = (await res.json()) as { text?: string; error?: string };
      if (!res.ok) throw new Error(body.error ?? "The assistant did not respond");
      setMessages((m) => [...m, { role: "assistant", text: body.text ?? "" }]);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong");
    } finally {
      setSending(false);
    }
  }

  function toggleMic() {
    if (listening) {
      recognitionRef.current?.stop();
      setListening(false);
      return;
    }
    const Recognition = getSpeechRecognition();
    if (!Recognition) {
      setError("Voice input isn't supported in this browser — try typing instead.");
      return;
    }
    const recognition = new Recognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = "en-US";
    recognition.onresult = (e) => {
      const last = e.results[e.results.length - 1];
      const transcript = last?.[0]?.transcript;
      if (transcript) void send(transcript);
    };
    recognition.onerror = () => setListening(false);
    recognition.onend = () => setListening(false);
    recognitionRef.current = recognition;
    recognition.start();
    setListening(true);
  }

  return (
    <div className="flex h-full flex-col">
      <div ref={listRef} className="flex-1 space-y-2 overflow-y-auto p-4">
        {messages.length === 0 && (
          <p className="text-body-sm text-void-black/60">
            Ask about this building — “Where’s the nearest restroom?”, “What obstacles were reported recently?”
          </p>
        )}
        {messages.map((m, i) => (
          <div key={i} className={`flex ${m.role === "user" ? "justify-end" : "justify-start"}`}>
            <div
              className={`max-w-[85%] rounded-xl px-3 py-2 text-body-sm whitespace-pre-wrap ${
                m.role === "user"
                  ? "bg-wander-blue text-pure-white"
                  : "border border-hairline bg-pure-white text-void-black"
              }`}
            >
              {m.text}
            </div>
          </div>
        ))}
        {sending && (
          <div className="flex justify-start">
            <div className="rounded-xl border border-hairline bg-pure-white px-3 py-2 text-body-sm text-void-black/60">
              Thinking…
            </div>
          </div>
        )}
        {error && <p className="text-body-sm text-wander-pink">{error}</p>}
      </div>
      <form
        className="flex items-end gap-2 border-t border-hairline p-3"
        onSubmit={(e) => {
          e.preventDefault();
          void send(input);
        }}
      >
        <textarea
          className="input min-h-9 flex-1 resize-none"
          rows={1}
          placeholder="Type a question…"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              e.preventDefault();
              void send(input);
            }
          }}
        />
        <button
          type="button"
          aria-label={listening ? "Stop listening" : "Ask by speaking"}
          aria-pressed={listening}
          onClick={toggleMic}
          className={`btn-icon ${listening ? "bg-pink-tint text-wander-pink" : ""}`}
        >
          <Icon name="mic" />
        </button>
        <button type="submit" className="btn-primary" disabled={sending || !input.trim()} aria-label="Send">
          <Icon name="arrowRight" />
        </button>
      </form>
    </div>
  );
}
