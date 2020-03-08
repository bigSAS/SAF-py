"""
API - demo api - notes app
"""
from json import dumps
from bottle import Bottle, request, HTTPResponse
from pony.orm import select, db_session, commit

from enum import Enum
from typing import List
from api.model import init_db, Note, NoteSerializer
from common.validation import Validator, ValidationResult, ValidationError


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


@api.route(route(Route.NOTES), method=['GET'])
def list_notes():
    with db_session:
        notes = list(select(n for n in Note)[:])
        return NoteSerializer(notes).json


class NoteValidator(Validator):
    validate_fields = ('author', 'note')

    def __init__(self, data):
        super().__init__(data, Note)

    @staticmethod
    def validate_author(author):
        if author != 'sas': raise ValidationError('author must be sas')

    @staticmethod
    def validate_note(note):
        if len(note) > 5: raise ValidationError('note must be max 5 chars long')


@api.route(route(Route.NOTES), method=['POST'])
def add_note():
    with db_session:
        result: ValidationResult = NoteValidator(request.json).validate()
        if result.is_valid:
            new_note: Note = result.object
            commit()
            return NoteSerializer(new_note).json
        else:
            return HTTPResponse(body=dumps(result.errors), status=400)
