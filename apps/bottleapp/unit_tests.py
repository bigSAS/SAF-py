import pytest
from json import loads
from pony.orm import db_session, select
from api.model import Note
from common.serialization import Serializer, SerializerError


def test_db_insert(db):
    with db_session:
        Note(author='jimmy', note='...')
        new_notes = select(n for n in Note)[:]
        assert len(new_notes) == 1


# @Serializer tests
class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
jimmy = Person('Jimmy', 69)


class PersonSerializer(Serializer):
    fields = ('name', 'age')
    model = Person


def test_serializer__json_should_return_valid_json_when_single_obj_instance():
    loaded = loads(PersonSerializer(jimmy).json)


def test_serializer__json_should_return_valid_json_when_list_of_obj_instance():
    loaded = loads(PersonSerializer([jimmy, jimmy]).json)


def test_serializer__serialized_should_return_dict_when_single_obj_instance():
    assert isinstance(PersonSerializer(jimmy).serialized, dict)


def test_serializer__when_instatiated_with_obj_list_should_return_list():
    assert isinstance(PersonSerializer([jimmy, jimmy]).serialized, list)


def test_serializer__serialized_should_have_correct_keys():
    # todo: rozbic na dwa testy, jeden na dlugosc drugi na klucze
    person_serializer = PersonSerializer(jimmy)
    assert len(person_serializer.fields) == len(person_serializer.serialized.keys())
    for field in person_serializer.fields:
        assert field in person_serializer.serialized.keys()


def test_serializer__model_attr_cannot_be_empty():
    class EmptyModelAttrSerializer(Serializer):
        fields = ('name',)
        model = None
    
    with pytest.raises(SerializerError) as se:
        EmptyModelAttrSerializer(jimmy)
    assert 'model attr missing' in str(se)


def test_serializer__can_construct_only_from_model_obj_instance():
    class Foo: pass
    with pytest.raises(SerializerError) as se:
        PersonSerializer(Foo())
    assert f'invalid obj passed in constructor' in str(se)


def test_serializer__can_construct_only_from_list_of_model_objs_instances():
    class Foo: pass
    with pytest.raises(SerializerError) as se:
        PersonSerializer([Foo(), Foo()])
    assert f'invalid obj passed in constructor' in str(se)


def test_serializer__should_return_list_od_model_obj_when_constructed_with_list_of_obj():
    assert isinstance(PersonSerializer([jimmy, jimmy]).serialized, list)


def test_serializer__serializer_fields_cannot_be_empty():
    class EmptyFieldsSerializer(Serializer):
        fields = tuple()
        model = Person

    with pytest.raises(SerializerError) as se:
        EmptyFieldsSerializer(jimmy).serialized
    assert 'fields not specified' in str(se)


def test_serializer__serializer_fields_must_have_correct_attr_names():
    incorrect_field = 'foo'
    
    class BrokenPersonSerializer(Serializer):
        fields = (incorrect_field, 'name')
        model = Person

    with pytest.raises(SerializerError) as se:
        BrokenPersonSerializer(jimmy).serialized
    assert f'incorrect field name: {incorrect_field}' in str(se)


def test_serializer__fields_must_be_a_tuple_or_list_of_strings():
    class BrokenFieldsSerializer(Serializer):
        fields = (1, 2)
        model = Person

    with pytest.raises(SerializerError) as se:
        BrokenFieldsSerializer(jimmy).serialized
    assert 'fields must be a tuple or list of strings' in str(se)


class Weapon:
        def __init__(self, name):
            self.name = name
    
class WeaponSerializer(Serializer):
    fields = ('name',)
    model = Weapon


def test_serializer_custom_field_serializer_is_binded():
    class ArmedPerson(Person):
        def __init__(self, name, age, weapon):
            super().__init__(name, age)
            self.weapon = weapon

    class ArmedPersonSerializer(Serializer):
        fields = ('weapon', )
        model = ArmedPerson

        @staticmethod
        def serialized_weapon(weapon):
            return WeaponSerializer(weapon).serialized
    
    serialized = ArmedPersonSerializer(ArmedPerson('sas', 34, Weapon('AK47'))).serialized
    assert serialized.get('weapon', {'name': 'foo'}).get('name') == 'AK47'


def test_serializer_custom_list_field_serializer_is_binded():
    class MultiArmedPerson(Person):
        def __init__(self, name, age, weapons):
            super().__init__(name, age)
            self.weapons = weapons
    
    class MultiArmedPersonSerializer(Serializer):
        fields = ('weapons', )
        model = MultiArmedPerson

        @staticmethod
        def serialized_weapons(weapons):
            return WeaponSerializer(weapons).serialized
    
    serialized = MultiArmedPersonSerializer(MultiArmedPerson('sas', 34, [Weapon('AK47'), Weapon('glok')])).serialized
    assert serialized.get('weapons', {'name': 'foo'})[1].get('name') == 'glok'


def test_serializer__nested_deeper_custom_type_binding_correct():
    class WeaponStack:
        def __init__(self, name, weapons):
            self.name = name
            self.weapons = weapons

    class WeaponStackSerializer(Serializer):
        model = WeaponStack
        fields = ('weapons',)

    @staticmethod
    def serialized_weapons(weapons):
        return WeaponSerializer(weapons).serialized

    class Rambo(Person):
        def __init__(self):
            super().__init__('rambo', 99)
            self.weapon_stack = WeaponStack('warstack', [Weapon('bazooka'), Weapon('knife')])
   
    class RamboSerializer(Serializer):
        model = Rambo
        fields = ('name', 'weapon_stack')
        
        @staticmethod
        def serialized_weapon_stack(weapon_stack):
            return WeaponStackSerializer(weapon_stack).serialized
    
    serialized = RamboSerializer(Rambo()).serialized
    assert serialized.get('weapon_stack').get('weapons')[1].get('name') == 'knife'


def test_serializer__nested_deeper_list_custom_type_binding_correct():
    assert False, "todo"


def test_serializer__custom_type_should_have_serialized_method():
    # hint: when type is not in default types and no method raise
    class MissingSerializerMethodArmedPersonSerializer(Serializer):
        fields = ('weapon', )
        model = ArmedPerson

    with pytest.raises(SerializerError) as se:
        MissingSerializerMethodArmedPersonSerializer(
            ArmedPerson('sas', 34, Weapon('AK47'))
        ).serialized
    assert f'serializer_method not found for field: weapon' in str(se)


def test_serializer__deserializing_json_should_return_model_object_instance():
    json = '{"name": "jimmy", "age": 21}'
    person = PersonSerializer.deserialize_json(json)
    assert isinstance(person, PersonSerializer.model)


def test_serializer__deserializing_json_with_list_should_return_model_obj_instance_list():
    json = '[{"name": "jimmy", "age": 21}, {"name": "jimmyh", "age": 23}]'
    persons = PersonSerializer.deserialize_json(json)
    assert isinstance(persons, list)
    for person in persons:
        assert isinstance(person, PersonSerializer.model)


def test_serializer__when_deserialize_json_must_be_valid_json_string():
    invalid_json = json = '{name: "jimmy", "age": 21}'
    with pytest.raises(SerializerError) as se:
        PersonSerializer.deserialize_json(invalid_json)
    assert 'invalid json' in str(se)


def test_serializer__deserializing_json_must_contain_correct_fields():
    json = '{"name": "jimmy"}'
    with pytest.raises(SerializerError) as se:
        PersonSerializer.deserialize_json(json)
    assert 'field missing' in str(se)


# todo: custom fields
def test_serializer__custom_field_when_defined_should_be_added_to_serialized_obj():
    assert False, "todo"

def test_serializer__custom_field_when_defined_should_be_added_to_serialized_obj_list():
    assert False, "todo"

def test_serializer__when_custom_field_then_method_for_it_should_be_defined():
    assert False, "todo"
# todo: feature -> xml ???

