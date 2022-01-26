import abc

class IPerson(abc.ABC):
    def __init__(self, name, age) -> None:
        super().__init__()
        self.__name = name
        self.__age = age
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = max(value,0)
        
    @abc.abstractmethod
    def interview(self):
        """ Implement Methods """
        
class Person(IPerson):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        
    def interview(self):
        print (f"Hi my name is {self.name}, I'm {self.age} years old.")
        
class ProxyPerson(IPerson):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        self.person:Person = Person(name, age)
        
    def interview(self):
        print (f"Hi I'm {self.person.name}'s proxy.")
        self.person.interview()
        
if __name__ == "__main__":
    person = Person("Peter", 18)
    person.interview()
    proxy = ProxyPerson("Peter", 18)
    proxy.interview()