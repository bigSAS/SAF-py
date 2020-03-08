class ValidationError(Exception):
    def __init__(self, error_msg, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_msg = error_msg


class ValidationResult:
    def __init__(self, result):
        self.__result = result

    @property
    def is_valid(self):
        return len(self.errors) == 0

    @property
    def data(self):
        return self.__result.get('data', None)

    @property
    def object(self):
        if not self.is_valid: raise ValidationError('Validation failed')
        return self.__result.get('object', None)

    @property
    def errors(self):
        return self.__result.get('errors', [])


class MissingValidationMethod(Exception): pass


class Validator:
    validate_fields = tuple()

    def __init__(self, data, model_class):
        self.__data = data
        self.__model_class = model_class
        self.__errors = []

    def validate(self, fields=None):
        validate_fields = fields if fields else self.validate_fields
        result = {}
        result["data"] = self.__data
        self.__errors = []
        for field in validate_fields:
            validator_func = getattr(self, f'validate_{field}', None)
            if callable(validator_func):
                try:
                    validator_func(self.__data.get(field, None))
                except ValidationError as ve:
                    self.__errors.append({
                        field: ve.error_msg
                    })
                except Exception as e:
                    self.__errors.append({
                        field: str(e)
                    })
            else: raise MissingValidationMethod(f'validate_{field} staticmethod missing')
        if len(self.__errors) == 0:
            result["object"] = self.create_obj()
        else:
            result["errors"] = self.__errors
        return ValidationResult(result)

    def create_obj(self):
        return self.__model_class(**self.__data)
