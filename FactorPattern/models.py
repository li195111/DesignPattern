from __future__ import annotations

import abc
from enum import Enum


class GraphType(Enum):
    Circle=0
    Rectangle=1
    Triangle=2

class Graphic:
    def __init__(self, width:int=0, height:int=0, radius:int=0) -> None:
        self._width = width
        self._height = height
        self._radius = radius
        
    def __str__(self) -> str:
        return f"{self.__class__.__name__} Width: {self.width} Height: {self.height} Radius: {self.radius}"

    @property
    def width(self):
        return self._width
        
    @width.setter
    def width(self, value):
        self._width = max(value,0)
        
    @property
    def height(self):
        return self._height
        
    @height.setter
    def height(self, value):
        self._height = max(value,0)
        
    @property
    def radius(self):
        return self._radius
        
    @radius.setter
    def radius(self, value):
        self._radius = max(value,0)
        
    def dimension(self):
        return {'width':self.width, 'height':self.height, 'radius':self.radius}

class Factory:
    def __init__(self, graph_type:GraphType) -> None:
        self._graph_type = graph_type
        
    def __str__(self) -> str:
        return f"{self.__class__.__name__}"

    @property
    def graph_type(self):
        return self._graph_type
    
    @graph_type.setter
    def graph_type(self, value):
        self._graph_type = value
        
    @abc.abstractmethod
    def create(self, dimensions:dict):
        """Implement Factory Create Method"""

class Circle(Graphic):
    def __init__(self, width: int = 0, height: int = 0, radius: int = 0) -> None:
        super().__init__(width, height, radius)
    
class Rectangle(Graphic):
    def __init__(self, width: int = 0, height: int = 0, radius: int = 0) -> None:
        super().__init__(width, height, radius)

class Triangle(Graphic):
    def __init__(self, width: int = 0, height: int = 0, radius: int = 0) -> None:
        super().__init__(width, height, radius)

class CircleFactory(Factory):
    def __init__(self, graph_type: GraphType=GraphType.Circle) -> None:
        super().__init__(graph_type)
        
    def create(self, dimensions:dict)->Graphic:
        return Circle(**dimensions)

class RectangleFactory(Factory):
    def __init__(self, graph_type: GraphType=GraphType.Rectangle) -> None:
        super().__init__(graph_type)
        
    def create(self, dimensions:dict)->Graphic:
        return Rectangle(**dimensions)

class TriangleFactory(Factory):
    def __init__(self, graph_type: GraphType=GraphType.Triangle) -> None:
        super().__init__(graph_type)
        
    def create(self, dimensions:dict)->Graphic:
        return Triangle(**dimensions)
        
class GraphicFactory(Factory):
    def __init__(self, graph_type: GraphType) -> None:
        super().__init__(graph_type)
        self.graph_map = {GraphType.Circle:CircleFactory, 
                          GraphType.Rectangle:RectangleFactory, 
                          GraphType.Triangle:TriangleFactory}
    def create(self)->Factory:
        return self.graph_map[self.graph_type](self.graph_type)
    