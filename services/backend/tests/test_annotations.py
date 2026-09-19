import hashlib
from types import SimpleNamespace
from unittest.mock import AsyncMock
import pytest
from ..app.services.annotations import (AnnotationBatch, Candidate, Finding, Findings,
    Review, ReviewFile, annotate, batch_digest, publish)


def sample(graph):
    candidate = Candidate(id='annotation-example', frame='frame.jpg', frame_sha256='abc',
        category='restroom', name='Women restroom', description='Door with sign',
        sign_text='Women', designation='women', uncertainty='')
    batch = AnnotationBatch(site_id=graph.site_id, map_revision='v1', floor=1,
                            model='fake', candidates=[candidate])
    review = ReviewFile(site_id=graph.site_id, map_revision='v1', batch_sha256=batch_digest(batch),
        graph_sha256=hashlib.sha256(graph.model_dump_json().encode()).hexdigest(),
        reviews=[Review(candidate_id=candidate.id, decision='approve', waypoint_id=graph.waypoints[0].id,
                        verified_by='Surveyor', verified_at='2026-09-19T12:00:00Z')])
    return batch, review


def test_publish_requires_review_and_preserves_provenance(graph):
    batch, review = sample(graph)
    result, notes = publish(batch, review, graph, 'v1')
    assert notes == []
    assert len(result.destinations) == len(graph.destinations) + 1
    destination = result.destination('annotation-example')
    assert destination.annotation.frame == 'frame.jpg'
    assert destination.waypoint_id == graph.waypoints[0].id
    assert 'women' in destination.tags
    assert destination.annotation.category == 'restroom'
    assert destination.annotation.navigation_role == 'landmark'


@pytest.mark.parametrize('role,permanence', [('potential_hazard', 'movable'), ('context', 'fixed')])
def test_note_decision_captures_evidence_without_a_destination(graph, role, permanence):
    batch, review = sample(graph)
    batch.candidates[0].navigation_role = role
    batch.candidates[0].permanence = permanence
    batch.candidates[0].visual_location = 'left foreground'
    batch.candidates[0].uncertainty = 'Partially occluded'
    review.batch_sha256 = batch_digest(batch)
    review.reviews[0].decision = 'note'
    result, notes = publish(batch, review, graph, 'v1')
    assert result.destinations == graph.destinations
    assert len(notes) == 1
    note = notes[0]
    assert note['id'] == 'annotation-example'
    assert note['navigation_role'] == role
    assert note['permanence'] == permanence
    assert note['visual_location'] == 'left foreground'
    assert note['uncertainty'] == 'Partially occluded'
    assert note['waypoint_id'] == graph.waypoints[0].id


def test_note_decision_still_requires_a_verified_waypoint(graph):
    batch, review = sample(graph)
    review.reviews[0].decision = 'note'
    review.reviews[0].waypoint_id = 'missing'
    with pytest.raises(ValueError, match='verified approach waypoint'):
        publish(batch, review, graph, 'v1')


@pytest.mark.parametrize('mutation', ['batch', 'graph', 'revision', 'waypoint', 'missing', 'duplicate'])
def test_rejects_invalid_publication(graph, mutation):
    batch, review = sample(graph)
    if mutation == 'batch':
        batch.candidates[0].name = 'Changed'
    elif mutation == 'graph':
        graph.waypoints[0].x += 2
    elif mutation == 'revision':
        review.map_revision = 'v2'
    elif mutation == 'waypoint':
        review.reviews[0].waypoint_id = 'missing'
    elif mutation == 'missing':
        review.reviews = []
    else:
        review.reviews.append(review.reviews[0])
    with pytest.raises(ValueError):
        publish(batch, review, graph, 'v1')


def test_rejected_candidate_never_becomes_destination(graph):
    batch, review = sample(graph)
    review.reviews[0].decision = 'reject'
    result, notes = publish(batch, review, graph, 'v1')
    assert result.destinations == graph.destinations
    assert notes == []


@pytest.mark.parametrize('role,permanence', [('potential_hazard', 'movable'), ('context', 'fixed'), ('landmark', 'temporary')])
def test_observations_do_not_become_route_targets(graph, role, permanence):
    batch, review = sample(graph)
    batch.candidates[0].navigation_role = role
    batch.candidates[0].permanence = permanence
    review.batch_sha256 = batch_digest(batch)
    with pytest.raises(ValueError, match='routing destinations'):
        publish(batch, review, graph, 'v1')


def test_landmark_preserves_uncertainty_and_image_frame(graph):
    batch, review = sample(graph)
    candidate = batch.candidates[0]
    candidate.category = 'seating'
    candidate.permanence = 'movable'
    candidate.visual_location = 'left foreground'
    candidate.uncertainty = 'May have moved since capture'
    review.batch_sha256 = batch_digest(batch)
    result = publish(batch, review, graph, 'v1')[0].destination(candidate.id)
    assert 'not user-relative' in result.description
    assert candidate.uncertainty in result.description
    assert 'not live state' in result.description


def test_duplicate_review_preserves_only_corrected_object(graph):
    batch, review = sample(graph)
    batch.candidates.append(batch.candidates[0].model_copy(update={'id': 'duplicate'}))
    review.batch_sha256 = batch_digest(batch)
    review.reviews.append(Review(candidate_id='duplicate', decision='duplicate',
        duplicate_of='annotation-example', verified_by='Surveyor', verified_at='2026-09-19'))
    review.reviews[0].corrected = Finding(category='restroom', name='All-gender restroom',
        description='Corrected from visible sign', sign_text='All gender',
        designation='all_gender', uncertainty='')
    result, notes = publish(batch, review, graph, 'v1')
    assert result.destination('annotation-example').name == 'All-gender restroom'
    assert all(d.id != 'duplicate' for d in result.destinations)
    assert notes == []


def test_failed_extraction_does_not_leave_partial_frames(tmp_path, monkeypatch):
    import subprocess
    from ..app.services.annotations import extract_frames
    def fail(*args, **kwargs):
        raise subprocess.CalledProcessError(1, 'ffmpeg')
    monkeypatch.setattr(subprocess, 'run', fail)
    with pytest.raises(ValueError, match='Frame extraction failed'):
        extract_frames(tmp_path / 'video.mp4', tmp_path / 'frames')
    assert not (tmp_path / 'frames').exists()


@pytest.mark.asyncio
async def test_annotation_cache_avoids_duplicate_api_calls(tmp_path, settings):
    frames = tmp_path / 'frames'
    frames.mkdir()
    (frames / 'one.jpg').write_bytes(b'fake image for fake provider')
    result = Findings(findings=[Finding(category='bottle_filler', name='Bottle filler',
        description='Fixture', sign_text='', designation='unknown', uncertainty='Check position')])
    client = SimpleNamespace(responses=SimpleNamespace(parse=AsyncMock(
        return_value=SimpleNamespace(output_parsed=result))))
    first = await annotate(frames, tmp_path / 'batch.json', 'site', 'v1', 0, settings, client=client)
    second = await annotate(frames, tmp_path / 'batch.json', 'site', 'v1', 0, settings, client=client)
    assert first == second
    assert client.responses.parse.await_count == 1
    assert first.candidates[0].timestamp_seconds is None
    assert not hasattr(first.candidates[0], 'waypoint_id')


@pytest.mark.asyncio
async def test_annotation_limit_prevents_unbounded_spend(tmp_path, settings):
    (tmp_path / 'a.jpg').write_bytes(b'a')
    (tmp_path / 'b.jpg').write_bytes(b'b')
    with pytest.raises(ValueError):
        await annotate(tmp_path, tmp_path / 'batch.json', 'site', 'v1', 0, settings, limit=1)
