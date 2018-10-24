import random
from classes.game import bcolor

class Person:
    def __init__(self, name, hp, mp, atk, df, magic):
       self.name = name
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
        print("{}ACTIONS{}".format(bcolor.WARNING, bcolor.ENDC))
        for item in self.actions:
            print("    {}: {}".format(str(i), item))
            i += 1

    def choose_magic(self):
        i = 1
        print("MAGIC")
        for spell in self.magic:
            print(str(i) + ":", spell["name"], "(cost:", str(spell["cost"]) +")")
            i += 1

    def show_status(self, bar_size):
        name_spaces = " " * (bar_size + 29)
        # hp bar configuration
        hp_bar_total = bar_size
        hp_bar_left = round(self.hp / self.max_hp * hp_bar_total)
        hp_bar_spaces = " " * (hp_bar_total - hp_bar_left)
        hp_bar = "█" *  round(self.hp / self.max_hp * hp_bar_total)
        hp_top = " " * (hp_bar_total + 9)
        hp_current = hp_bar + hp_bar_spaces
        hp_value_offset = len(str(self.get_maxhp()))
        hp_title_spaces = " " * ((len(str(self.get_maxhp()).zfill(hp_value_offset))*2)+5)

        # mp bar configuration
        mp_bar_total = 20
        mp_bar_left = round(self.mp / self.max_mp * mp_bar_total)
        mp_bar_spaces = " " * (mp_bar_total - mp_bar_left)
        mp_bar = "█" *  round(self.mp / self.max_mp * mp_bar_total)
        mp_top = " " * (mp_bar_total - 4)
        mp_current = mp_bar + mp_bar_spaces

        print("{}'s status:{}".format(self.name, name_spaces), end='')
        yield
        print("{}{c.BOLD}HP{}MP{}{c.ENDC} ".format(hp_title_spaces, hp_top, mp_top, c=bcolor), end='')
        yield
        print("{c.BOLD}{:04}/{:04}{c.ENDC} |{c.OKGREEN}{}{c.ENDC}| {c.BOLD}{:03}/{:03}{c.ENDC} |{c.OKBLUE}{}{c.ENDC}|".format(self.get_hp(), self.get_maxhp(), hp_current, self.get_mp(), self.get_maxmp(), mp_current, c=bcolor), end='')
        yield

