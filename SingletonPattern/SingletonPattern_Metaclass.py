from __future__ import annotations

import abc
from typing import Any

# Create Singleton Abstract Metaclass
class Singleton(abc.ABCMeta):
    __instance = None
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if Singleton.__instance is None:
            Singleton.__instance = super().__call__(*args, **kwds)
        # Always return the object was already instancetied.
        return Singleton.__instance

class IEarth(abc.ABC, metaclass=Singleton):
    def __init__(self, name, age) -> None:
        super().__init__()
        self._name = name
        self._age = age
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        self._age = max(value,0)

class Earth(IEarth):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
                
if __name__ == "__main__":
    e1 = Earth("Earth1",4300)
    print (e1)
    e3 = Earth("Earth3",3000)
    print (e3)
    