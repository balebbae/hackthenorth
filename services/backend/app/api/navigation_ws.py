import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pydantic import ValidationError
from ..models import Pose, Obstacle, DestinationRequest
from ..services.sessions import broadcast

router = APIRouter()


@router.websocket('/ws/legacy/sessions/{session_id}')
async def navigation_socket(socket: WebSocket, session_id: str):
    state = socket.app.state
    await socket.accept()
    try:
        session = state.store.get(session_id)
    except KeyError:
        await socket.send_json({'type': 'error', 'message': 'Session not found'})
        await socket.close(code=1008)
        return
    session.sockets.add(socket)
    try:
        await socket.send_json({'type': 'session_state', **session.snapshot()})
        while True:
            try:
                raw = await socket.receive_text()
                if len(raw) > 65536:
                    raise ValueError('Message exceeds 64 KiB')
                message = json.loads(raw)
                if not isinstance(message, dict):
                    raise ValueError('Message must be an object')
                kind = message.pop('type', None)
                if kind == 'hello':
                    if message:
                        raise ValueError('hello takes no fields')
                    await socket.send_json({'type': 'session_state', **session.snapshot()})
                elif kind == 'pose_update':
                    if set(message) != {'pose'}:
                        raise ValueError('pose_update requires only pose')
                    pose = Pose.model_validate(message['pose'])
                    was_localized = session.snapshot()['localization']['localized']
                    previous_instruction = session.instruction
                    state.navigation.update_pose(session, pose)
                    await broadcast(session, {'type': 'pose_update', 'pose': pose.model_dump()})
                    await broadcast(session, {'type': 'navigation_instruction', **session.snapshot()['navigation']})
                    if pose.localized != was_localized:
                        state.events.record(session, 'localization_acquired' if pose.localized else 'localization_lost', {})
                    if session.instruction == 'arrived' and previous_instruction != 'arrived':
                        state.events.record(session, 'arrived', {'destination_id': session.destination_id})
                elif kind == 'set_destination':
                    body = DestinationRequest.model_validate(message)
                    result = state.navigation.set_destination(session, body.destination_id, body.accessible_only)
                    await broadcast(session, {'type': 'route_update', **result})
                    await broadcast(session, {'type': 'navigation_instruction', **result})
                    state.events.record(session, 'destination_set', body.model_dump())
                    state.events.record(session, 'route_generated', result)
                    if result['instruction'] == 'arrived':
                        state.events.record(session, 'arrived', {'destination_id': body.destination_id})
                elif kind == 'obstacle':
                    body = Obstacle.model_validate(message)
                    state.navigation.obstacle(session, body)
                    await broadcast(session, {'type': 'obstacle', **body.model_dump()})
                    location = None
                    if session.snapshot()['localization']['localized']:
                        location = {'nearest_waypoint_id': state.navigation.graph.nearest(session.pose).id}
                    state.events.record(session, 'obstacle', body.model_dump(), location=location)
                else:
                    raise ValueError('Unknown message type')
            except (ValueError, ValidationError) as error:
                await socket.send_json({'type': 'error', 'message': str(error)})
    except WebSocketDisconnect:
        pass
    finally:
        session.sockets.discard(socket)
