# Medieval - Text adventure Game 
# Programmers - Rafael de Paiva and Rafael e Paula
import random

# Hero Class, which is going to setup a new hero
class Hero():
    def __init__(self, name = "none", hp = 100, ap = 20):
        self.name = name
        self.hp = hp
        self.ap = ap
        
    def take_dmg(self, dmg):
        self.hp = self.hp - dmg
        
    def is_dead(self):
        if self.hp < 1:
            return True
        else:
            return False
    
    def get_atk(self):
        atk = random.randint(0, self.ap)
        return atk
        
pc = Character()

print(pc.get_atk())