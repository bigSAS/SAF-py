from json import dumps, loads
from collections.abc import Iterable


class SerializerError(Exception): pass


class Serializer:
    """
    # todo: docs
    # todo: feature - xml ?
    """
    fields = tuple()
    model = None

    def __init__(self, obj):
        self.__class__.__validate_model_attr()
        self.__validate_fields_attr()
        self.__validate_obj_instance(obj)
        self.obj = obj
    
    @property
    def serialized(self):
        def dictify(instance):
            basic_types = [str, int, bool, None]
            try:
                result = {}
                for field in self.fields:
                    attr_val = getattr(instance, field)
                    if type(attr_val) in basic_types:
                        result[field] = getattr(instance, field)
                    else:
                        getter = getattr(self, f'serialized_{field}', None)
                        if callable(getter):
                            result[field] = getter(getattr(instance, field))
                        else:
                            raise SerializerError(f'serializer_method not found for field: {field}')
                return result
            except Exception as e:
                raise SerializerError(f'serialization failed:\n{e}')

        if isinstance(self.obj, Iterable):
            return [dictify(ins) for ins in self.obj]                            
        else:
            return dictify(self.obj)

    @property
    def json(self) -> str:
        return dumps(self.serialized)
        
    @classmethod
    def deserialize_json(cls, json):
        loaded = cls.__load_json(json)
        if isinstance(loaded, list):
            return [cls.__create_model_obj(obj) for obj in loaded]
        return cls.__create_model_obj(loaded)
    
    @classmethod
    def __create_model_obj(cls, data):
        for field in cls.fields:
            if field not in data.keys():
                raise SerializerError(f'field missing: {field}')
        return cls.model(**data)
    
    @staticmethod
    def __load_json(json):
        try:
            return loads(json)
        except:
            raise SerializerError('invalid json')

    @classmethod
    def __validate_model_attr(cls):
        if not cls.model:
            raise SerializerError('model attr missing')

    def __validate_fields_attr(self):
        if len(self.fields) == 0:
            raise SerializerError('fields not specified')
        msg = 'fields must be a tuple or list of strings'
        if (
            not isinstance(self.fields, list)
            and not isinstance(self.fields, tuple)
        ): raise SerializerError(msg)
        for field in self.fields:
            if not isinstance(field, str):
                raise SerializerError(msg)

    def __validate_obj_instance(self, obj):
        if isinstance(obj, list):
            for ins in obj:
                self.__validate_obj_instance(ins)
        else:
            if not isinstance(obj, self.model):
                raise SerializerError(
                    'invalid obj passed in constructor must be of:\n'
                    f'{self.model}.\nInstead got: {obj.__class__.__name__}'
                )
            self.__validate_field_names(obj)

    def __validate_field_names(self, obj):
        for field in self.fields:
            if not hasattr(obj, field):
                raise SerializerError(f'incorrect field name: {field}')
