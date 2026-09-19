# Main world integration

Create a canonical session with {worldId, deviceId}, use the returned sessionId,
and send X-API-Key on the voice WebSocket upgrade in addition to the first-message
voice token. Niantic poses now go to POST /sessions/{id}/pose; the dashboard WS is
read-only. World sessions persist. Production ownership and voice interruption
limitations below still apply. See services/backend/WORLDS_MIGRATION.md.

---

# Live voice handoff (experimental backend implementation)

Endpoint: `/ws/sessions/{session_id}/voice`. Create the existing navigation session
first and continue supplying Niantic pose updates on the existing navigation WS.

The existing `/assistant` WS remains text-only. The new bridge uses OpenAI Live
`gpt-live-1` for audio and client-owned delegation to the current Responses agent.
Set OPENAI_MODEL=gpt-6-astra to use Astra for those delegated requests; the Live
model is configured independently. Astra is not the audio transport model.

Enable VOICE_ENABLED=true and configure VOICE_ACCESS_TOKEN plus OPENAI_API_KEY.
This is a shared demo token, not per-user production authorization. Do not ship
it embedded in a public app; production needs authenticated session ownership.
The remaining backend routes still use the existing unauthenticated demo model.

## Client protocol

1. Open WS and within 10 seconds send `{"type":"auth","token":"demo-access-token"}`.
2. Wait for `voice_ready` (pcm16le, rate 24000, channels 1).
3. Send `{"type":"audio","audio":"<base64 raw PCM>"}` in roughly 100 ms chunks.
   Use little-endian signed 16-bit mono, 24 kHz. No WAV header. Maximum encoded
   chunk is 64 KiB. Only auth, audio and close messages are accepted.
4. Play returned `{"type":"audio","audio":"..."}` chunks in order at 24 kHz.
5. Transcript events contain speaker=user/assistant and delta text; fragments are
   not complete turns. assistant_response includes backend text/sources/actions.
6. `{"type":"close"}` ends the call. Calls are capped at 15 minutes. Errors are
   sanitized. Reconnect explicitly after failure; never replay action requests.

Native/web owners must implement microphone capture, resampling, echo cancellation,
audio playback and a visible AI-generated voice disclosure. No microphone UI is
added by this backend implementation. Use HTTPS/WSS for remote connections.

## Delegation and limitations

The backend collects input transcript fragments and, on session.delegation.created,
submits available fragments ending at/before that event's offset to the existing
agent. Duplicate delegation IDs are ignored. Missing transcript causes a repeat
request, not guessed work. A bounded worker processes delegations serially while
audio continues. Current pose/routes are injected by the existing agent context.

Live has no transcript-done event or task text in delegation.created. Timeline
ordering and incomplete/late transcripts must be checked with real recordings.
This bridge has mocked protocol tests, not a verified production audio session.
Commentary is speakable context, not a guarantee of exact wording or playback.

The bridge does not yet implement interruption-aware cancellation, automatic
obstacle announcements, or clearing queued client audio on barge-in. Navigation
and obstacle events still arrive on the navigation WS and must take priority in
the client's audio UX. Do not use this experimental voice path as the immediate
hazard-alert channel. A disconnected/cancelled model turn may already have set a
destination; consult navigation state after reconnecting.

Protocol reference: https://developers.openai.com/api/reference/resources/live/primary-websocket
