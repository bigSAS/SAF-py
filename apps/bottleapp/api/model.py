from pony.orm import Database, Required, set_sql_debug, commit, select, db_session

INIT_DB = False
db = Database()


class Note(db.Entity):
    author = Required(str)
    note = Required(str)
    
class SerializerError(Exception): pass

class Serializer:
    fields = tuple()
    def __init__(self, obj):
        self.obj = obj

    def serialize(self):
        try:
            result = {}
            for field in self.fields:
                result[field] = getattr(self.obj, field)
            return result
        except Exception as e:
            #todo: specialize error handling
            raise SerializerError('serialization failed')
        

class NoteSerializer(Serializer):
    fields = ('author', 'note')
    

def init_db():
    db.bind(provider='sqlite', filename='db.sqlite', create_db=True)
    db.generate_mapping(create_tables=True)
    if INIT_DB:
        init_data()


@db_session
def init_data():
    Note(author='sas', note='lorem')
    Note(author='ben', note='ipsum')
