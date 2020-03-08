from common.serialization import Serializer
from api.model import Note


class NoteSerializer(Serializer):
    fields = ('id', 'author', 'note')
    model = Note
