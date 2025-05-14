from dataclasses import dataclass
from utils import Base, Error, UndefinedError 


@dataclass(init=True, repr=False)
class A(Base):
    _a: str | int = "Result True"

    @property
    def a(self):
        return self._a
 
    @a.setter
    def a(self, value):
        if value == "one":
            raise Error()
        self._a = value
    
    def func(self, value: int | float = None):
        if not value and isinstance(self._a, (int, float)):
            return self._a * 3 * 5
        elif isinstance(value, (int, float)) :
            return value * value * 3
        else:
            raise AttributeError()