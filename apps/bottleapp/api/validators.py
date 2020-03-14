from common.validation import Validator, ValidationError
from api.model import Note


class NoteValidator(Validator):
    # todo: legitimize validator -> this one is for tests
    validate_fields = ('author', 'note')

    def __init__(self, data):
        super().__init__(data, Note)

    @staticmethod
    def validate_author(author):
        if author != 'sas': raise ValidationError('author must be sas')

    @staticmethod
    def validate_note(note):
        if len(note) > 5: raise ValidationError('note must be max 5 chars long')
