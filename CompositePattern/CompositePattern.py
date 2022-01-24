from __future__ import annotations
from typing import List

class Product:
    def __init__(self, price=0) -> None:
        self._orignal_price = price
        
    @property
    def price(self):
        return self._orignal_price
    
    @price.setter
    def price(self, value):
        self._orignal_price = max(value,0)
        
class CompositeProduct(Product):
    def __init__(self, price=0) -> None:
        super().__init__(price)
        self._additional_price = 0
        self.child_products:List[CompositeProduct] = []
        
    def add(self, product:CompositeProduct):
        self.child_products.append(product)
        
    @property
    def price(self):
        self._additional_price = sum([p.price for p in self.child_products])
        return self._orignal_price + self._additional_price
    
class ProductA(CompositeProduct):
    def __init__(self, price=0) -> None:
        super().__init__(price)
        
class ProductB(Product):
    def __init__(self, price=0) -> None:
        super().__init__(price)
        
class ProductC(Product):
    def __init__(self, price=0) -> None:
        super().__init__(price)
        
class Box(CompositeProduct):
    def __init__(self, price=0) -> None:
        super().__init__(price)
        
if __name__ == "__main__":
    box = Box()
    a = ProductA(100)
    b = ProductB(25)
    c = ProductC(50)
    box.add(a)
    box.add(b)
    box.add(c)
    print (f"Box 1 Price {box.price}")

    c2 = ProductC(50)
    a.add(c2)
    print (f"A Price {a.price}")
    print (f"Box 1 Price {box.price}")
    
    box2 = Box()
    a.add(ProductB(25))
    box2.add(a)
    box2.add(box)
    print (f"Box 2 Price {box2.price}")
    print (f"A Price {a.price}")
    print (f"Box 1 Price {box.price}")