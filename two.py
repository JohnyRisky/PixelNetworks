from dataclasses import dataclass
from one import Base
import re

@dataclass(init=True, repr=False)
class B(Base):
    _a: str = "Result False"
    
    @property
    def a(self):
        return self._a
 
    @a.setter
    def a(self, value):
        self._a = value

    def func(self, string, pattern: str = r"^\s*(123-ab(?:c|ce|cef)-ABC)\s*$"):
        # pattern = r"^\s*(123-ab(?:c|ce|cef)-ABC)\s*$"
        return re.match(pattern=pattern, string=string)
