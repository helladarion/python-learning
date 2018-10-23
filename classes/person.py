import random

class Person:
    def __init__(self, hp, mp, atk, df, magic):
       self.max_hp = hp
       self.hp = hp
       self.max_mp = mp
       self.mp = mp
       self.atk = atk
       self.df = df
       self.magic = magic
       self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atk -10, self.atk +10)

    def generate_magic_damage(self,index):
        return random.randrange(self.magic[index]["dmg"] -5, self.magic[index]["dmg"] +5 )

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, index):
        return self.magic[index]["name"]

    def get_spell_cost(self, index):
        return self.magic[index]["cost"]

    def choose_action(self):
        i = 1
        print("ACTIONS")
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("MAGIC")
        for spell in self.magic:
            print(str(i) + ":", spell["name"], "(cost:", str(spell["cost"]) +")")
            i += 1

    def show_status(self):
        print(" HP                       MP                    ")
        print(" ______________________   ______________________")
        print("|████████████          | |████████████          |") 

