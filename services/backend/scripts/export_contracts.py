"""Regenerate shared JSON schemas from backend validation models."""
import json
from ..app.config import ROOT
from ..app.models import Pose, Localization, Destination, DestinationRequest, Obstacle, Query, Document
from ..app.routing.graph import Graph


def main():
    schemas = {model.__name__: model.model_json_schema(ref_template='#/$defs/{model}')
               for model in (Pose, Localization, Destination, DestinationRequest, Obstacle, Query, Document, Graph)}
    definitions = {}
    for schema in schemas.values():
        definitions.update(schema.pop('$defs', {}))
    definitions.update(schemas)
    output = {'$schema': 'https://json-schema.org/draft/2020-12/schema',
              'title': 'Backend contract component schemas v0.1', '$defs': definitions}
    path = ROOT / 'shared/contracts/backend.schema.json'
    path.write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
    print(path)


if __name__ == '__main__':
    main()
