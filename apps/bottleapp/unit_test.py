from pony.orm import db_session, select
from api.model import Note


def test_db_insert(db):
    with db_session:
        Note(author='jimmy', note='...')
        new_notes = select(n for n in Note)[:]
        assert len(new_notes) == 1
