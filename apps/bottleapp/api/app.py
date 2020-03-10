"""
API - demo api - notes app
"""
from json import dumps
from bottle import Bottle, request, HTTPResponse
from pony.orm import select, db_session, commit
from pony.orm.core import ObjectNotFound

from enum import Enum
from typing import List
from api.model import init_db, Note
from api.validators import NoteValidator
from api.serializers import NoteSerializer


API_ROOT = '/api'


class Route(Enum):
    NOTES = '/notes'
    NOTE = '/notes/<note_id:int>'

    @staticmethod
    def list() -> List[str]:
        return [
            {
                "route": "notes",
                "path": route(Route.NOTES),
                "method": "GET",
                "description": "list notes",
                "body": None
            },
            {
                "route": "notes",
                "path": route(Route.NOTES),
                "method": "POST",
                "description": "add note",
                "body": {
                    "author": "str(R)",
                    "note": "str(R)"
                }
            },
            {
                "route": "note",
                "path": route(Route.NOTE) + '{note_id}',
                "method": "GET",
                "description": "get note",
                "body": None
            }
        ]


def route(route: Route) -> str:
    return API_ROOT + route.value


api = Bottle()
init_db()


@api.route(API_ROOT)
def api_root():
    return dumps(Route.list(), indent=2, sort_keys=True)


def not_found():
    return HTTPResponse(body=None, status=404)


def bad_request(errors):
    return HTTPResponse(body=dumps(errors), status=400)


from api.modules.notes import list_notes, add_note, get_note

