from json import dumps


class SerializerError(Exception): pass


class Serializer:
    fields = tuple()
    model = None

    def __init__(self, obj):
        self.__validate_model_attr()
        self.__validate_fields_attr()
        self.__validate_obj_instance(obj)
        self.obj = obj
    
    @property
    def serialized(self):
        def dictify(instance):
            try:
                result = {}
                for field in self.fields:
                    result[field] = getattr(instance, field)
                return result
            except Exception as e:
                # todo: specialize error handling
                raise SerializerError('serialization failed')

        if isinstance(self.obj, list):
            return [dictify(ins) for ins in self.obj]                            
        else:
            return dictify(self.obj)

    @property
    def json(self) -> str:
        return dumps(self.serialized)
    
    def __validate_model_attr(self):
        if not self.model:
            raise SerializerError('model attr missing')

    def __validate_fields_attr(self):
        if len(self.fields) == 0:
            raise SerializerError('fields not specified')

    def __validate_obj_instance(self, obj):
        if isinstance(obj, list):
            for ins in obj:
                self.__validate_obj_instance(ins)
        else:
            if not isinstance(obj, self.model):
                raise SerializerError(f'invalid obj passed in constructor must be of: {self.model}')
