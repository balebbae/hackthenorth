import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ..models import Query

router = APIRouter()


@router.websocket('/ws/sessions/{session_id}/assistant')
async def assistant_socket(socket: WebSocket, session_id: str):
    await socket.accept()
    try:
        socket.app.state.store.get(session_id)
    except KeyError:
        await socket.send_json({'type': 'error', 'message': 'Session not found'})
        await socket.close(code=1008)
        return
    try:
        while True:
            try:
                raw = await socket.receive_text()
                if len(raw) > 16384:
                    raise ValueError('Message exceeds 16 KiB')
                message = json.loads(raw)
                if not isinstance(message, dict) or set(message) != {'type', 'text'} or message['type'] != 'assistant_message':
                    raise ValueError('Expected assistant_message with text')
                query = Query(session_id=session_id, text=message['text'])
                response = await socket.app.state.agent.query(query.session_id, query.text)
                await socket.send_json({'type': 'assistant_response', **response})
            except ValueError as error:
                await socket.send_json({'type': 'error', 'message': str(error)})
    except WebSocketDisconnect:
        pass
