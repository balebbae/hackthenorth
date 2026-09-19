import json
import logging
from .agent_context import AgentContextBuilder

logger = logging.getLogger(__name__)


class BuildingAgentService:
    def __init__(self, store, model, tools, context=None):
        self.store, self.model, self.tools = store, model, tools
        self.context = context or AgentContextBuilder(store)

    async def query(self, session_id: str, text: str):
        session = self.store.get(session_id)
        async with session.agent_lock:
            self.tools.events.record(session, 'assistant_query', {'text': text})
            turn = [{'role': 'user', 'content': text}]
            sources, actions, trace = {}, [], []
            # Preserve provenance of evidence still available in compact conversation history.
            for entry in session.history:
                if entry.get('role') == 'developer' and entry.get('content', '').startswith('Historical tool evidence (not current state): '):
                    for prior_call in json.loads(entry['content'].split(': ', 1)[1]):
                        for source in prior_call['result'].get('sources', []):
                            sources[(source['type'], source['id'])] = source
            answer = 'I do not have enough information to answer right now.'
            for _ in range(8):
                context = await self.context.build(session_id)
                dynamic = {'role': 'developer', 'content': '<application_context>\n' +
                           context.model_dump_json() + '\n</application_context>'}
                try:
                    response = await self.model.respond([*session.history, dynamic, *turn])
                except Exception as error:
                    logger.warning('Agent provider unavailable (%s)', type(error).__name__)
                    answer = 'The assistant service is unavailable. Please check its configuration or try again.'
                    if actions:
                        answer += ' The destination was already set; navigation remains active.'
                    break
                turn.extend(item.model_dump(exclude_none=True) for item in response.output)
                calls = [item for item in response.output if item.type == 'function_call']
                if not calls:
                    answer = response.output_text or answer
                    break
                for call in calls:
                    try:
                        if call.name == 'set_destination' and actions:
                            raise ValueError('A destination was already set this turn')
                        result = await self.tools.execute(session, call.name, call.arguments)
                        for source in result['sources']:
                            sources[(source['type'], source['id'])] = source
                        actions.extend(result['actions'])
                    except ValueError as error:
                        result = {'error': str(error)}
                    except Exception as error:
                        logger.warning('Tool unavailable (%s)', type(error).__name__)
                        result = {'error': 'Tool unavailable; do not invent a result.'}
                    trace.append({'name': call.name, 'arguments': call.arguments, 'result': result})
                    turn.append({'type': 'function_call_output', 'call_id': call.call_id, 'output': json.dumps(result)})
            else:
                answer = 'I could not complete that request within the tool limit.'
                if actions:
                    answer += ' The destination was set; navigation remains active.'
            # Complete turns only; never truncate a function call away from its output.
            session.history.extend([{'role': 'user', 'content': text},
                {'role': 'assistant', 'content': answer},
                {'role': 'developer', 'content': 'Historical tool evidence (not current state): ' + json.dumps(trace)}])
            session.history = session.history[-18:]
            return {'text': answer, 'sources': list(sources.values()), 'actions': actions, 'tool_calls': trace}
