from json import dumps
from bottle import Bottle
from enum import Enum
from typing import List

API_ROOT = '/api'


class Route(Enum):
    NOTES = '/notes'
    
    @staticmethod
    def list() -> List[str]:
        return [
            {
                "route": "notes",
                "path": route(Route.NOTES),
                "description": "notes list"
            }
        ]


def route(route: Route) -> str:
    return API_ROOT + route.value


api = Bottle()


@api.route(API_ROOT)
def api_root():
    return dumps(Route.list())


@api.route(route(Route.NOTES))
def notes():
    return dumps(['foo', 'bar'])
