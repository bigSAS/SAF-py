import pytest
from common.validation import Validator, ValidationError


class Owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Pet:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner


class OwnerValidator(Validator):
    model = Owner
    fields = ('name', 'age')
    
    @staticmethod
    def validate_name(name):
        if name != 'sas': raise ValidationError('must be sas')
    
    @staticmethod
    def validate_age(age):
        if age != 34: raise ValidationError('must be 34')


class PetValidator(Validator):
    model = Pet
    fields = ('name', 'owner')
    
    @staticmethod
    def validate_name(name):
        if name != 'fjus': raise ValidationError('must be fjus')
    
    @staticmethod
    def validate_owner(owner):
        print(owner)
        result = OwnerValidator(owner).validate()
        print(result.errors)
        if not result.is_valid:
            raise ValidationError(result.errors)
    
    def create_obj(self):
        return Pet(
            name=self.data['name'],
            owner=Owner(**self.data['owner'])
        )


def test_validator__example_flat_happy():
    loaded_owner = {
        'name': 'sas',
        'age': 34
    }
    v = OwnerValidator(loaded_owner)
    result = v.validate()
    assert result.is_valid
    assert isinstance(result.object, Owner)


def test_validator__example_nested_happy():
    loaded_pet = {
        'name': 'fjus',
        'owner': {
            'name': 'sas',
            'age': 34
        }
    }
    
    v = PetValidator(loaded_pet)
    result = v.validate()
    assert result.is_valid
    assert isinstance(result.object, Pet)
    assert isinstance(result.object.owner, Owner)


def test_validator__example_flat_not_happy():
    bad_owner = {
        'name': 'sos',
        'age': 33
    }

    result = OwnerValidator(bad_owner).validate()
    assert not result.is_valid
    with pytest.raises(ValidationError) as ve:
        result.object
    assert 'Validation failed, cannot obtain object' in ve.value.error_msg
    assert 'must be sas' in result.errors['name']
    assert 'must be 34' in result.errors['age']


def test_validator__example_nested_not_happy():
    bad_pet = {
        'name': 'fjas',
        'owner': {
            'name': 'sos',
            'age': 33
        }
    }
    
    result = PetValidator(bad_pet).validate()
    assert not result.is_valid
    with pytest.raises(ValidationError) as ve:
        result.object
    assert 'Validation failed, cannot obtain object' in ve.value.error_msg
    assert 'must be fjus' in result.errors['name']
    assert 'must be sas' in result.errors['owner']['name']
