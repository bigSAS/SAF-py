from pony.orm import Database, Required, db_session


INIT_DB = False
db = Database()


class User(db.Entity):
    """ User entity """
    email = Required(str, unique=True)
    password = Required(str)
    username = Optional(str)
    info = Optional(str)
    is_superuser = Required(bool)
    
    def __str__(self):
        return f'{self.email} [su: {self.is_superuser}]'


class Note(db.Entity):
    author = Required(str)
    note = Required(str)


def init_db(db_name='db.sqlite'):
    db.bind(provider='sqlite', filename=db_name, create_db=db_name != ':memory:')
    db.generate_mapping(create_tables=True)
    if INIT_DB:
        init_data()


@db_session
def init_data():
    Note(author='sas', note='lorem')
    Note(author='ben', note='ipsum')
