"""Explicit paid smoke test. Importing this module never calls an external service."""
import asyncio
import json
from ..app.config import Settings
from ..app.main import create_app


async def main():
    settings = Settings()
    if not settings.openai_api_key or not settings.openai_model:
        raise SystemExit('Set OPENAI_API_KEY and OPENAI_MODEL in services/backend/.env first.')
    app = create_app(settings)
    async with app.router.lifespan_context(app):
        session = app.state.navigation.create('demo_building')
        result = await app.state.agent.query(session.session_id, 'Where am I? Use the current location tool.')
        print('Answer:', result['text'])
        print('Tool calls:', json.dumps(result['tool_calls'], indent=2))
        print('Source IDs:', json.dumps(result['sources']))
        if not any(call['name'] == 'get_current_location' for call in result['tool_calls']):
            raise SystemExit('FAILED: no location tool call; verify API key/model access and provider logs.')
        print('PASS: real Responses tool loop; unknown localization is expected.')


if __name__ == '__main__':
    asyncio.run(main())
