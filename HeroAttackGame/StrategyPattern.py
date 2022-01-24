from models import Hero
from skills import Collide, WaterBall, 天外飛仙

class Battle:
    def __init__(self, hero1:Hero, hero2:Hero) -> None:
        self.hero1 = hero1
        self.hero2 = hero2
        
    def attack(self, hero1:Hero, hero2:Hero):
        hero1.attack(hero2)
        return not (hero1.HP > 0 and hero2.HP > 0)
    
    def start(self):
        gg = False
        while not gg:
            gg = self.attack(self.hero1,self.hero2)
            if gg: break
            gg = self.attack(self.hero2,self.hero1)
            
        print (f"{self.hero1.name if self.hero1.HP <= 0 else self.hero2.name} 已陣亡")
        print (f"勝利者為 {self.hero1.name if self.hero1.HP > 0 else self.hero2.name}")
        
if __name__ == "__main__":
    hero1 = Hero(name="小王",
                 HP=500,
                 MP=500,
                 Strength=150,
                 Wisdom=80,
                 Defense=50,
                 skill=Collide())
    hero2 = Hero(name="小明",
                 HP=500,
                 MP=500,
                 Strength=150,
                 Wisdom=80,
                 Defense=50,
                 skill=WaterBall())
    
    battle = Battle(hero1, hero2)
    battle.start()