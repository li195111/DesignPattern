from __future__ import annotations

from models import SkillType, Skill, Hero

class Collide(Skill):
    def __init__(self, skill_type: SkillType=SkillType.Physic) -> None:
        super().__init__(skill_type)
    
    def attack(self, attacker: Hero, target: Hero):
        damage = attacker.Strength - target.Defense
        target.HP -= damage
        return damage
        
class WaterBall(Skill):
    def __init__(self, skill_type: SkillType=SkillType.Magic) -> None:
        super().__init__(skill_type)
        
    def attack(self, attacker: Hero, target: Hero):
        attacker.MP -= 5
        damage = attacker.Wisdom * 2
        target.HP -= damage
        return damage

class 天外飛仙(Skill):
    def __init__(self, skill_type: SkillType = SkillType.Magic) -> None:
        super().__init__(skill_type)
        
    def attack(self, attacker: Hero, target: Hero):
        attacker.MP -= 100
        damage = 10000
        target.HP -= damage
        return damage