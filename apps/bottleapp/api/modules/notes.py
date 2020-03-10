from pony.orm import db_session, select
from pony.orm.core import ObjectNotFound

from api.app import api, API_ROOT, Route, route, not_found
from api.model import Note
from api.serializers import NoteSerializer
from api.validators import NoteValidator


@api.route(route(Route.NOTES), method=['GET'])
def list_notes():
    with db_session:
        notes = list(select(n for n in Note)[:])
        return NoteSerializer(notes).json


@api.route(route(Route.NOTES), method=['POST'])
def add_note():
    with db_session:
        result = NoteValidator(request.json).validate()
        if result.is_valid:
            new_note = result.object
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

#todo: update, delete note

