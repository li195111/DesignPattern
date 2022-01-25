'''
建造者模式
    假設建造 (設計) 一棟房子
    需要知道:
        牆壁材質
        建造類型
        房間的數量
        客廳的數量
        廁所數量
        產出結果
'''

from __future__ import annotations

import abc
from enum import Enum
        
class BuildType(Enum):
    typeA = 0
    typeB = 1
    typeC = 2
    
class Material(Enum):
    Mud = 0
    Wood = 1
    Rock = 2
    Cement = 3
        
class IHouseBuilder(abc.ABC):
    def __init__(self) -> None:
        pass
        
    @abc.abstractstaticmethod
    def set_wall_material(self):
        """Implement Method"""
    
    @abc.abstractstaticmethod
    def set_build_type(self):
        """Implement Method"""
    
    @abc.abstractstaticmethod
    def set_room_number(self):
        """Implement Method"""
    
    @abc.abstractstaticmethod
    def set_living_room_number(self):
        """Implement Method"""
    
    @abc.abstractstaticmethod
    def set_bath_room_number(self):
        """Implement Method"""

class HouseBuilder(IHouseBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.house = House()
    
    def set_wall_material(self, material:Material):
        self.house.wall_material = material
        return self
    
    def set_build_type(self, build_type:BuildType):
        self.house.build_type = build_type
        return self
    
    def set_room_number(self, value):
        self.house.room_number = value
        return self
    
    def set_living_room_number(self, value):
        self.house.living_room_number = value
        return self
    
    def set_bath_room_number(self, value):
        self.house.bath_room_number = value
        return self
    
    def get_result(self):
        return self.house
        
class House:
    def __init__(self, wall_material:Material=Material.Mud, build_type:BuildType=BuildType.typeA, room_number:int=0, living_room_number:int=0, bath_room_number:int=0) -> None:
        self._wall_material = wall_material
        self._build_type = build_type
        self._room_number = room_number
        self._living_room_number = living_room_number
        self._bath_room_number = bath_room_number
        
    def __str__(self) -> str:
        return f"用 {self.wall_material.name} 的 {self.build_type.name} 型建築 有 {self.room_number} 房 {self.living_room_number} 廳 {self.bath_room_number} 衛浴"
    
    @property
    def wall_material(self):
        return self._wall_material
    
    @wall_material.setter
    def wall_material(self, value):
        self._wall_material = value
        
    @property
    def build_type(self):
        return self._build_type
    
    @build_type.setter
    def build_type(self, value):
        self._build_type = value
        
    @property
    def room_number(self):
        return self._room_number
    
    @room_number.setter
    def room_number(self, value):
        self._room_number = max(value,0)
        
    @property
    def living_room_number(self):
        return self._living_room_number
    
    @living_room_number.setter
    def living_room_number(self, value):
        self._living_room_number = max(value,0)
        
    @property
    def bath_room_number(self):
        return self._bath_room_number
    
    @bath_room_number.setter
    def bath_room_number(self, value):
        self._bath_room_number = max(value,0)
        
class CementDirector:
    
    @staticmethod
    def construct():
        return HouseBuilder()\
            .set_wall_material(Material.Cement)\
                .set_build_type(BuildType.typeA)\
                    .set_room_number(3)\
                        .set_living_room_number(2)\
                            .set_bath_room_number(1)\
                                .get_result()
                            
class MudDirector:
    @staticmethod
    def construct():
        return HouseBuilder()\
            .set_wall_material(Material.Mud)\
                .set_build_type(BuildType.typeB)\
                    .set_room_number(1)\
                        .set_living_room_number(0)\
                            .set_bath_room_number(0)\
                                .get_result()

class WoodDirector:
    @staticmethod
    def construct():
        return HouseBuilder()\
            .set_wall_material(Material.Wood)\
                .set_build_type(BuildType.typeC)\
                    .set_room_number(2)\
                        .set_living_room_number(1)\
                            .set_bath_room_number(1)\
                                .get_result()
                            
if __name__ == "__main__":
    cement_house = CementDirector.construct()
    mud_house = MudDirector.construct()
    wood_house = WoodDirector.construct()
    print (cement_house)
    print (mud_house)
    print (wood_house)
    pass