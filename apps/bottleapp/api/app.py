"""
API - demo api - notes app
"""
from json import dumps
from bottle import Bottle
from pony.orm import select, db_session

from enum import Enum
from typing import List
from api.model import init_db, Note, NoteSerializer



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
init_db()

@api.route(API_ROOT)
def api_root():
    return dumps(Route.list())


@db_session
@api.route(route(Route.NOTES))
def notes():
    notes = select(n for n in Note)[:]
    return dumps([NoteSerializer(note).serialize() for note in notes])
