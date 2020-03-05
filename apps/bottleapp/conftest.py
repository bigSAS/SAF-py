import pytest
from pony.orm import Database, Required, set_sql_debug, commit, select, db_session
from api.model import init_db, Note

@pytest.fixture(scope='session')
def db():
    init_db(':memory:')

@db_session
@pytest.fixture(scope='session')
def notes(db):
    init_data()
    notes = select(n for n in Note)[:]
    return notes


@db_session
def init_data():
    Note(author='sas', note='lorem')
    Note(author='ben', note='ipsum')
