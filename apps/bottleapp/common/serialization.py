from json import dumps
from dicttoxml import dicttoxml
from collections.abc import Iterable


class SerializerError(Exception): pass


class Serializer:
    """
    Object serializer. Serialize any object instance into JSON / XML
    Usage example:

    class Person:
        first_name = 'jimmy'
        last_name = 'whick'
        age = 99

    class PersonSerializer(Serializer):
        model = Person
        fields = ('first_name', 'last_name', 'age')

    serializer = PersonSerializer(Person())
    serialized: dict = serializer.serialized
    json: str = serializer.json
    xml: str = serializer.xml

    List of objects can be passed in constructor, example:
    serializer = PersonSerializer([Person(), Person()])

    ! important !
    If field is a type other than str, int, bool, None then serializer must have static method in convention:
    @staticmethod
    def serialized_<field>(obj)
    method must return json serializable object
    Example:
    class PersonSerializer(Serializer):
        model = Person
        fields = ('first_name', 'last_name', 'age')
        custom_fields = ('full_name',)

        @staticmethod
        def get_full_name(person):
            return f'{person.first_name} {person.last_name}'

    ! important !
    U can define custom fields in custom_fields attr, then serializer must have static method in convention:
    def serialized_<custom_field>(obj)
    Method must return serializable object, esiaset way is to add serializer for custom field type
    Example:

    class Pet:
        name = 'fefe'
        species = 'dog'

    class PetSerializer(Serializer):
        model = Pet
        fields = ('name', 'species')

    class PetPerson:
        pet = Pet()
        name = 'sas'

    class PetPersonSerializer(Serializer):
        model = PetPerson
        fields = ('pet', 'name')

        @staticmethod
        def serialized_pet(pet_obj):
            return PetSerializer(pet_obj).serialized


    U can instantiate model instance from json string.
    ! important ! model class must provide valid __init__ for unpacking loaded dict
    Example:
    class Pet:
        def __init__(self, name, species):
            self.name = name
            self.species = species

    class PetSerializer(Serializer):
        model = Pet
        fields = ('name', 'species')

    json = '{"name": "fjus", "species": "dog"}'
    fjus: Pet = PetSerializer.model_instance_from(json)
    """
    model = None
    validator_class = None
    fields = tuple()
    custom_fields = tuple()

    def __init__(self, obj):
        self.__class__.__validate_model_attr()
        self.__validate_fields_attr()
        self.__validate_obj_instance(obj)
        self.obj = obj

    @property
    def serialized(self):

        def dictify(instance):
            basic_types = [str, int, bool, float]
            result = {}
            for field in self.fields:
                attr_val = getattr(instance, field, None)
                if attr_val is None:
                    result[field] = None
                elif type(attr_val) in basic_types:
                    result[field] = attr_val
                else:
                    getter = getattr(self, f'serialized_{field}', None)
                    if callable(getter):
                        result[field] = getter(attr_val)
                    else:
                        raise SerializerError(f'serializer_method not found for field: {field}')
            for custom_field in self.custom_fields:
                getter = getattr(self, f'get_{custom_field}', None)
                if callable(getter):
                    result[custom_field] = getter(instance)
                else:
                    raise SerializerError(f'get_{custom_field} not defined')
            return result

        if isinstance(self.obj, Iterable):
            return [dictify(ins) for ins in self.obj]
        else:
            return dictify(self.obj)

    @property
    def json(self) -> str:
        return dumps(self.serialized)

    @property
    def xml(self) -> str:
        if isinstance(self.obj, Iterable):
            return dicttoxml(
                self.serialized,
                attr_type=False,
                custom_root=f'{self.model.__name__}s',
                item_func=lambda x: self.model.__name__
            )
        return dicttoxml(self.serialized, attr_type=False, custom_root=self.model.__name__)

    # @classmethod
    # def load_json(cls, json):
    #     return cls.__load_json(json)

    # @classmethod
    # def model_instance_from(cls, json):
    #     loaded = cls.__load_json(json)
    #     if isinstance(loaded, list):
    #         return [cls.__create_model_obj(obj) for obj in loaded]
    #     return cls.__create_model_obj(loaded)

    # @classmethod
    # def __create_model_obj(cls, data):
    #     # todo: wrap result into own class, adapt tests
    #     for field in cls.fields:
    #         if field not in data.keys():
    #             raise SerializerError(f'field missing: {field}')
    #     result = {
    #         "object": None,
    #         "errors": []
    #     }
    #     if cls.validator_class:
    #         validator = cls.validator_class(data)
    #         validator.validate(cls.fields)
    #         if validator.data_is_valid:
    #             result["object"] = cls.model(**data)
    #         else:
    #             result["errors"] = validator.errors
    #     else:
    #         result["object"] = cls.model(**data)
    #     return result

    # @staticmethod
    # def __load_json(json):
    #     try:
    #         return loads(json)
    #     except:
    #         raise SerializerError('invalid json')

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
