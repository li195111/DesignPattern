from __future__ import annotations

from enum import Enum

class SkillType(Enum):
    Physic = 0
    Magic = 1
        
class Skill:
    def __init__(self, skill_type:SkillType=None) -> None:
        self._skill_type = skill_type
    
    @property
    def skill_type(self):
        return self._skill_type
    
    @skill_type.setter
    def skill_type(self, value):
        self._skill_type = value
        
    def attack(self, attacker:Hero, target:Hero):
        return NotImplementedError
    

class Attribute:
    def __init__(self, HP:int, MP:int, Strength:int, Wisdom:int, Defense:int) -> None:
        self._HP = HP
        self._MP = MP
        self._Strength = Strength
        self._Wisdom = Wisdom
        self._Defense = Defense
        
    @property
    def HP(self):
        return self._HP
    
    @HP.setter
    def HP(self, value):
        self._HP = max(value,0)
    
    @property
    def MP(self):
        return self._MP
    
    @MP.setter
    def MP(self, value):
        self._MP = max(value,0)

    @property
    def Strength(self):
        return self._Strength
    
    @Strength.setter
    def Strength(self, value):
        self._Strength = max(value,0)

    @property
    def Wisdom(self):
        return self._Wisdom
    
    @Wisdom.setter
    def Wisdom(self, value):
        self._Wisdom = max(value,0)

    @property
    def Defense(self):
        return self._Defense
    
    @Defense.setter
    def Defense(self, value):
        self._Defense = max(value,0)

class Hero(Attribute):
    def __init__(self, 
                 HP: int, MP: int, Strength: int, Wisdom: int, Defense: int,
                 name:str, skill:Skill) -> None:
        super().__init__(HP, MP, Strength, Wisdom, Defense)
        self._name = name
        self._skill = skill
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
                
    @property
    def skill(self):
        return self._skill
    
    @skill.setter
    def skill(self, value):
        self._skill = value
        
    def attack(self, target:Hero):
        damage = self.skill.attack(self,target)
        print (f"{self.name} 使出了 {self.skill.__class__.__name__} 攻擊 {target.name} 傷害值 {damage}")
        print (f"{target.name} HP 剩餘 {target.HP}")
        return target.HP <= 0
    