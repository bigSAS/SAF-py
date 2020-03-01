from enum import Enum
from typing import NamedTuple, Tuple


class Using(Enum):
    ID = 'id'
    NAME = 'name'
    XPATH = 'xpath'


class Selector(NamedTuple):
    using: Using
    value: str
    
    @property
    def selector_tuple(self) -> Tuple[str, str]:
        return (self.using.value, self.value)
