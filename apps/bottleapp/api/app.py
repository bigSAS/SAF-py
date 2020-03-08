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
from common.validation import ValidationResult


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
                "description": "notes list"
            }
        ]


def route(route: Route) -> str:
    return API_ROOT + route.value


api = Bottle()
init_db()


def not_found():
    return HTTPResponse(body=None, status=404)


def bad_request(errors):
    return HTTPResponse(body=dumps(errors), status=400)


@api.route(API_ROOT)
def api_root():
    return dumps(Route.list())


@api.route(route(Route.NOTES), method=['GET'])
def list_notes():
    with db_session:
        notes = list(select(n for n in Note)[:])
        return NoteSerializer(notes).json


@api.route(route(Route.NOTES), method=['POST'])
def add_note():
    with db_session:
        result: ValidationResult = NoteValidator(request.json).validate()
        if result.is_valid:
            new_note: Note = result.object
            commit()
            return NoteSerializer(new_note).json
        else:
            return bad_request(result.errors)


@api.route(route(Route.NOTE), method=['GET'])
def get_note(note_id):
    with db_session:
        try:
            note = Note[note_id]
            return NoteSerializer(note).json
        except ObjectNotFound:
            return not_found()
