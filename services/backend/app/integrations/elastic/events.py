import asyncio
import json
import logging
from datetime import datetime, timezone, timedelta
from uuid import uuid4

logger = logging.getLogger(__name__)


def parse_rows(response):
    names = [column['name'] for column in response['columns']]
    return [dict(zip(names, row)) for row in response['values']]


class EventService:
    def __init__(self, elastic):
        self.elastic = elastic
        self.pending = set()
        self.failed_writes = 0

    def record(self, session, event_type, data):
        # Historical indexing must never block immediate obstacle/navigation delivery.
        if len(self.pending) >= 256:
            self.failed_writes += 1
            logger.warning('Event queue full; historical event dropped')
            return
        event = {'id': str(uuid4()), 'session_id': session.session_id, 'site_id': session.site_id,
                 'event_type': event_type, 'timestamp': datetime.now(timezone.utc).isoformat(),
                 'summary': json.dumps(data, ensure_ascii=False), 'data': data}
        task = asyncio.create_task(self._write(event))
        self.pending.add(task)
        task.add_done_callback(self.pending.discard)

    async def _write(self, event):
        try:
            await self.elastic.require().index(index='live_events', id=event['id'], document=event)
        except Exception as error:
            self.failed_writes += 1
            logger.warning('Event indexing unavailable (%s)', type(error).__name__)

    async def recent(self, site_id, session_id, event_type=None, minutes=5):
        cutoff = (datetime.now(timezone.utc) - timedelta(minutes=minutes)).isoformat()
        query = ('FROM live_events | WHERE site_id == ?site AND session_id == ?session '
                 'AND timestamp >= TO_DATETIME(?cutoff)')
        params = [{'site': site_id}, {'session': session_id}, {'cutoff': cutoff}]
        if event_type:
            query += ' AND event_type == ?kind'
            params.append({'kind': event_type})
        query += ' | KEEP id, event_type, timestamp, summary | SORT timestamp DESC | LIMIT 50'
        result = await self.elastic.require().esql.query(query=query, params=params)
        return parse_rows(result)

    async def close(self):
        if self.pending:
            await asyncio.gather(*tuple(self.pending))
