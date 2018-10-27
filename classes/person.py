import random

class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.hp = hp
        self.mp = mp
        self.maxhp = hp
        self.maxmp = mp
        self.atk = atk
        self.df = df
        self.magic = magic
        self.actions = ["Attack","Magic"]

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def show_options(self):
        i = 1
        print("What do you want to do?")
        for act in self.actions:
            print(str(i) + ". " + act)
            i += 1

    def generate_damage(self):
        atk_high = self.atk + 10
        atk_low = self.atk - 10
        return random.randrange(atk_low, atk_high)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

