class Chair:
    def __init__(self, width, height, depth) -> None:
        self._width = width
        self._height = height
        self._depth = depth
        
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
    def depth(self):
        return self._depth
        
    @depth.setter
    def depth(self, value):
        self._depth = max(value,0)
        
    def dimension(self):
        return {'width':self.width, 'height':self.height, 'depth':self.depth}

class SmallChair(Chair):
    def __init__(self, width=10, height=10, depth=10) -> None:
        super().__init__(width, height, depth)

class MiddleChair(Chair):
    def __init__(self, width=20, height=20, depth=20) -> None:
        super().__init__(width, height, depth)

class LargeChair(Chair):
    def __init__(self, width=30, height=30, depth=30) -> None:
        super().__init__(width, height, depth)
        
class ChairFactor:
    def __init__(self) -> None:
        self.chair_map = {'s':SmallChair, 'm':MiddleChair, 'l':LargeChair}
    
    def create(self, chair_type:str)->Chair:
        return self.chair_map[chair_type]()
    
if __name__ == "__main__":
    
    factor = ChairFactor()
    
    print (factor.create('s').dimension())
    print (factor.create('m').dimension())
    print (factor.create('l').dimension())