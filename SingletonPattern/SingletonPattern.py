from __future__ import annotations

import abc

class IEarth(abc.ABC):
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
        
    @abc.abstractstaticmethod
    def print():
        """ Implement method """
        
class Earth(IEarth):
    
    __instance:Earth = None
    
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        if not Earth.__instance is None:
            raise ValueError(f"{self.__class__.__name__} already instantiated, Signleton can't instance more than one.")
        Earth.__instance = self
           
    @staticmethod
    def get_instance():
        if Earth.__instance is None:
            Earth("Earth", 4300)
        return Earth.__instance
    
    @staticmethod
    def print():
        print (f"{Earth.__instance.__class__.__name__} {Earth.__instance.name} {Earth.__instance.age}")
        
if __name__ == "__main__":
    e1 = Earth("Earth1",4300)
    e1.print()
    print (e1)
    e2 = Earth.get_instance()
    e2.print()
    print (e2)
    e3 = Earth("Earth3",3000)
    e3.print()
    print (e3)
    