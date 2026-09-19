# Main world integration

The canonical world schema and API from main take precedence. The CLI now accepts
world.json for --graph, binding reviews to the full manifest hash and active asset
version. PUT /worlds/{id}/annotations publishes reviewed nodes and stores evidence
in a separate annotations.json; POST /worlds/{id}/index refreshes Elastic. Both
require X-API-Key. See services/backend/WORLDS_MIGRATION.md. Legacy Graph JSON
export/restart instructions below apply only to /legacy navigation.

---

# Semantic annotation handoff (implemented MVP)

The pipeline is an offline operator CLI, not an HTTP upload endpoint. No SAM,
automatic 3D projection, segmentation training, or automatic route generation is
implemented. The scan viewer/client can build a review UI around these contracts.

## Input from capture / Niantic team

- Original JPEG/PNG images or FFmpeg-decodable perspective walkthrough video.
- Site ID, floor number, immutable scan/map revision identifier.
- Existing navigation graph in the same metric coordinate frame as localization.
- A reviewed approach waypoint for every published feature. The position of a
  sign is not necessarily the position of its door or the walkable approach.
- Preserve source media. The PLY can be used for review; it is not sent to OpenAI.
- 360 videos must first be converted into perspective images externally. This
  version does not unwarp panoramas or process raw INSV containers.
- For future automatic placement: synchronized per-frame camera-to-map poses,
  intrinsics/projection convention, registered depth or usable mesh, metric
  scale, and the transform into the navigation coordinate frame.

## Artifacts

`AnnotationBatch` and `ReviewFile` schemas are in backend.schema.json. Each batch
contains candidate IDs, descriptions, visible sign text, uncertainty, image
filenames and SHA256 hashes. Sample timestamps are approximate, not pose timestamps.
Empty findings are valid. Candidates have no usable navigation position.

An operator prepares a review file and explicitly decides approve/reject/duplicate
for every candidate. Fill verified_by and verified_at (ISO 8601 recommended),
assign an existing waypoint_id for approvals, optionally supply a complete
corrected Finding, and record notes. Duplicate decisions reference an approved
candidate in the same batch. The review binds the exact batch and graph hashes.
These are operator assertions, not cryptographic identity verification.

Publication validates the review and exports a new Graph. Approved records become
destinations with `annotation` evidence metadata. Rejected/duplicate candidates
are excluded. Neither model uncertainty nor designation implies accessibility.
Routes continue to use the manually surveyed edge accessibility flags.

Index the exported graph and restart the backend with GRAPH_PATH set to it.
Publication does not hot-reload an active session. Old Elastic records may remain
but search_places intersects retrieval with the active graph, so removed IDs
cannot become destinations. Deploy and index the same graph before a demo; stale
index hits may otherwise reduce recall. Preserve batch/review files for auditing.

## Review client requirements

Display candidate evidence images with names/sign text and uncertainty. Allow
corrections, duplicate merging, rejection and waypoint selection. Never approve
by default. Validate floor/door association and reachable side of walls. Do not
expose OpenAI keys. This backend change does not implement the review frontend.
# Expanded visual annotations

Findings now cover doors, corridors/junctions, ramps/escalators, signs/directories,
floor indicators, tactile paving, handrails/buttons, emergency equipment, furniture,
windows/pillars/artwork, services, waste/storage/charging, visible obstacles, surface
changes and scene context, in addition to the original destination categories.
Each finding includes permanence (fixed/movable/temporary/unknown), navigation_role
(destination/landmark/context/potential_hazard), visual_location (image-relative,
never user-relative), navigation_relevance and uncertainty. Defaults allow older
candidate files to load; existing reviews must be regenerated if their digest changes.
These are recorded observations, not live obstacle detections or accessibility proof.
Context, potential_hazard and temporary findings remain review evidence; publishing
them as routing destinations is rejected. Permanent/movable landmarks still require
reviewed approach waypoints. Context-only retrieval is not yet implemented.
Use scan_pipeline --reannotate to preserve prior output and rerun with the expanded
prompt. This invokes paid annotation again; cached pipeline output is otherwise reused.
