import abc
import copy

class IPerson(abc.ABC):
    def __init__(self, name, age) -> None:
        super().__init__()
        self.__name = name
        self.__age = age
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value:str):
        self.__name = value
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value:int):
        self.__age = max(value,0)
    
    @abc.abstractmethod
    def copy(self):
        """Implement method"""
        
class Person(IPerson):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
    
    def copy(self):
        return copy.deepcopy(self)

if __name__ == "__main__":
    
    A = Person("Gary", 18)
    print (A, A.name, A.age)
    B = A
    B.name = "Billy"
    print (A, A.name, A.age)
    print (B, B.name, B.age)

    B = A.copy()
    A.name = "Gary"
    print (A, A.name, A.age)
    print (B, B.name, B.age)
    print (A is B)