import importlib
from pathlib import Path

import falcon

from regex._base import _BaseAPI

_CURRENT_DIR = Path(__file__).parent


def add_apis(app: falcon.API) -> None:
    for file in _CURRENT_DIR.glob('*.py'):
        if file.name.startswith('_'):
            continue

        importlib.import_module(f'.{file.stem}', 'regex')

    for klass in _BaseAPI.__subclasses__():
        uri_template = klass.__name__.lower().rstrip('api')
        app.add_route(f'/{uri_template}', klass())
