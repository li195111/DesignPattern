import abc

class IDog(abc.ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abc.abstractmethod
    def bark(self):
        """Implement Method"""

class Dog(IDog):
    def __init__(self) -> None:
        super().__init__()
    
    def bark(self):
        return f"Woof Woof"
        
class ICat(abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        
    @abc.abstractmethod
    def meow(self):
        """Implement Method"""

class Cat(ICat):
    def __init__(self) -> None:
        super().__init__()
        
    def meow(self):
        return f"Meow Meow"
        
class CatAdapter(IDog):
    def __init__(self, cat:Cat) -> None:
        super().__init__()
        self.cat = cat
        
    def bark(self):
        return self.cat.meow()

if __name__ == "__main__":
    cat = Cat()
    dog = Dog()
    
    print (cat, cat.meow())
    print (dog, dog.bark())
    
    cat_dog = CatAdapter(cat)
    print (cat_dog, cat_dog.bark())
    pass