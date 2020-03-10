class ValidationError(Exception):
    def __init__(self, error_msg, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_msg = error_msg


class ValidationResult:
    """
    Validation result returned by Validator.validate method.
    """
    def __init__(self, result):
        self.__result = result

    @property
    def is_valid(self):
        """ check if validation was successfull """
        return len(self.errors) == 0

    @property
    def data(self):
        """ validated data (dict) """
        return self.__result.get('data', None)

    @property
    def object(self):
        """ model instance when validation is successfull """
        if not self.is_valid: raise ValidationError('Validation failed, cannot obtain object')
        return self.__result.get('object', None)

    @property
    def errors(self):
        """ errors dict wher validation is unsuccessfull """
        return self.__result.get('errors', [])


class MissingValidationMethod(Exception): pass


class ValidatorError(Exception): pass


class Validator:
    """
    Base class for validators.
    Example child implementation:
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
        
        class PersonValidator(Validator):
            model = Person
            fields = ('name', 'age')
            
            @staticmethod
            def validate_name(name):
                if len(name) < 3: raise ValidationError('name must be at least 3 chars long')
            
            @staticmethod
            def validate_age(age):
                if age > 99: raise ValidationError('to old')
    
    Example usage - failed validation:
        person_data = {
            'name': 'Jo',
            'age': 100
        }
        validator = PersonValidator(person_data)
        validation_result = validator.validate()
        validation_result.is_valid
        > False
        validation_result.data
        > {'name': 'Jo', 'age': 100}
        validation_result.errors
        > {'name': ['name must be at least 3 chars long'], 'age': ['to old']}
        validation_result.object
        > ValidationError => Validation failed, cannot obtain object
    Example usage - successfull validation:
        person_data = {
            'name': 'Joe',
            'age': 77
        }
        validator = PersonValidator(person_data)
        validation_result = validator.validate()
        validation_result.is_valid
        > True
        validation_result.data
        > {'name': 'Joe', 'age': 77}
        validation_result.errors
        > {}
        validation_result.object
        > <Person object>
    
    ! important !
    Each field should have its own validation staticmethod in convention:
        @staticmethod
        def validate_<field>(field_value):
            raise ValidationError('incorrect value')
    When validation fails method must raise ValidationError('<error_message>')
    
    ! important !
    create_obj() default behavior is to unpack data as kwargs and pass it do model class constructor.
    Override create_obj() when nessesary :)
    
    Nested example: => common__validation_test.py -> nested in test func
    """
    model = None
    fields = tuple()

    def __init__(self, data):
        self.__validate_model_attr()
        self.__data = data
        self.__errors = {}
        
    @property
    def data(self):
        return self.__data

    def validate(self, fields=None):
        validate_fields = fields if fields else self.fields
        result = {}
        result["data"] = self.__data
        self.__errors = {}
        for field in validate_fields:
            validator_func = getattr(self, f'validate_{field}', None)
            if callable(validator_func):
                try:
                    validator_func(self.__data.get(field, None))
                except ValidationError as ve:
                    if isinstance(ve.error_msg, dict):
                        self.__errors[field] = ve.error_msg
                    else:
                        try:
                            self.__errors[field].append(ve.error_msg)
                        except:
                            self.__errors[field] = []
                            self.__errors[field].append(ve.error_msg)
                except Exception as e:
                    try:
                        self.__errors['non_field_errors'].append(str(e))
                    except:
                        self.__errors['non_field_errors'] = []
                        self.__errors['non_field_errors'].append(str(e))
            else: raise MissingValidationMethod(f'validate_{field} staticmethod missing')
        if len(self.__errors.keys()) == 0:
            result["object"] = self.create_obj()
        else:
            result["errors"] = self.__errors
        return ValidationResult(result)

    def create_obj(self):
        return self.model(**self.__data)
    
    
    def __validate_model_attr(self):
        if not self.model:
            raise ValidatorError('model attr not set')

