from pony.orm import Database, Required, db_session
from common.serialization import Serializer


INIT_DB = False
db = Database()


class Note(db.Entity):
    author = Required(str)
    note = Required(str)

class NoteSerializer(Serializer):
    fields = ('author', 'note')
    model = Note


def init_db(db_name='db.sqlite'):
    db.bind(provider='sqlite', filename=db_name, create_db=db_name != ':memory:')
    db.generate_mapping(create_tables=True)
    if INIT_DB:
        init_data()


@db_session
def init_data():
    Note(author='sas', note='lorem')
    Note(author='ben', note='ipsum')
