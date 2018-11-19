import random
from classes.game import bcolor
from classes.game import ascii_text

class Person:
    ##############
    # Contructor #
    ##############
    def __init__(self, name, strength, constitution, skill):
       self.name = name
       hp = strength * constitution
       mp = skill * constitution
       atk = strength * skill
       df = constitution
       self.max_hp = hp
       self.hp = hp
       self.max_mp = mp
       self.mp = mp
       self.atk = atk
       self.df = df
       self.magic = []
       self.actions = ["Attack", "Inventory"]
       self.items = []
       self.armor = None
       self.weapon = None
       self.luck = 10
       self.statistics = {"kills": 0,"streaks": 0}

    def generate_random_person(name, points):
        # Attributes
        strength = random.randint(1,points - 2)
        constitution = random.randint(1,(points - strength) - 1)
        skill = points - (strength + constitution)
        print("Str: {}, Con: {}, Skill: {}".format(strength, constitution, skill))
        return Person(name, strength, constitution, skill)

    ####################
    # Combat functions #
    ####################

    def generate_damage(self):
        return random.randrange(self.get_attack() -10, self.get_attack() +10)

    def generate_magic_damage(self,index):
        return random.randrange(self.magic[index]["dmg"] -5, self.magic[index]["dmg"] +5 )

    def take_damage(self, dmg):
        if self.df > dmg:
            dmg_taken = 0
        else:
            dmg_taken = dmg - self.get_defence()
        self.hp -= dmg_taken
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def reduce_mp(self, cost):
        self.mp -= cost

    def check_defeat(self):
        if self.hp <= 0:
            self.statistics["streaks"] = 0
            return True
        else:
            return False

    def add_kill(self):
        self.statistics["kills"] += 1
        self.statistics["streaks"] += 1
        self.luck += 5
        if self.luck > 100:
            self.luck = 100

    def revive(self):
        self.max_hp = round(self.max_hp * 0.8)
        self.luck -= 6
        if self.luck < 0:
            self.luck = 0

    #################
    # Gets and Sets #
    #################

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.max_mp

    def get_spell_name(self, index):
        return self.magic[index]["name"]

    def get_spell_cost(self, index):
        return self.magic[index]["cost"]

    def get_defence(self):
        if random.randint(1,100) < self.luck:
            defence_value = self.df + self.armor["effect"] + self.armor["bonus"]
        else:
            defence_value = self.df + self.armor["effect"]
        return defence_value

    def get_attack(self):
        if random.randint(1,100) < self.luck:
            attack_value = self.atk + self.weapon["effect"] + self.weapon["bonus"]
        else:
            attack_value = self.atk + self.weapon["effect"]
        return attack_value

    #############
    # Inventory #
    #############

    def show_inventory(self):
        i = 1
        ascii_text.indent_ascii_text(ascii_text.center_text(),ascii_text.INVENTORY, "BLUE")
        #print("{}{}{}".format(bcolor.YELLOW, ascii_text.INVENTORY, bcolor.ENDC))
        if not self.items:
            print("You have no items")
            return False
        else:
            for item in self.items:
                print("{}{}: {} amount: {}".format((ascii_text.center_text() - 6)  * " ", i, item["name"], item["amount"]))
                #print("    {}. {} - ({})".format(i,item["name"], item["type"]))
                i += 1
            #print("    99. Exit")
            print("{}{}: {}".format((ascii_text.center_text() - 6)  * " ", "99", "Exit"))
            return True

    def use_item(self,item_id):
        if self.items[item_id]["type"] in ["armor", "weapon"]:
            print("You equiped {} {}".format(self.items[item_id]["name"],self.items[item_id]["type"]))
            if self.items[item_id]["type"] == "armor":
                self.armor = self.items[item_id]
                self.items.pop(item_id)
            else:
                self.weapon = self.items[item_id]
                self.items.pop(item_id)
        elif self.items[item_id]["type"] == "magic":
            print("You open the old scroll and learn the {} spell".format(self.items[item_id]["name"]))
            self.magic.append(self.items[item_id])
            self.items.pop(item_id)
        else:
            if self.items[item_id]["use"] == "cure":
                if self.items[item_id]["name"] == "Ultra Potion":
                    print("You use {} and it increases your Maximum HP in {}".format(self.items[item_id]["name"],self.items[item_id]["effect"]))
                    self.max_hp += self.items[item_id]["effect"]
                    self.hp = self.max_hp
                else:
                    print("You use {} and heals for {}".format(self.items[item_id]["name"],self.items[item_id]["effect"]))
                    self.hp += self.items[item_id]["effect"]
                if self.hp > self.max_hp:
                    self.hp = self.max_hp
                self.items[item_id]["amount"] -= 1
                if self.items[item_id]["amount"] <= 0:
                    self.items.pop(item_id)
            else:
                print("You use {} in the enemy dealing {} damage".format(self.items[item_id]["name"],self.items[item_id]["effect"]))
                #TODO include damage to the enemy
                self.items[item_id]["amount"] -= 1
                if self.items[item_id]["amount"] <= 0:
                    self.items.pop(item_id)

    ###############
    # Action Menu #
    ###############

    def choose_action(self):
        i = 1
        ascii_text.indent_ascii_text(ascii_text.center_text(),ascii_text.ACTION, "YELLOW")
        for act in self.actions:
            if act == "Inventory":
                num_items = len(self.items)
                print("{}{}: {} {}".format((ascii_text.center_text() - 6)  * " ",i, act, num_items))
            else:
                print("{}{}: {}".format((ascii_text.center_text() - 6)  * " ",i, act))
            i += 1

    ##############
    # Magic Menu #
    ##############

    def choose_magic(self):
        i = 1
        ascii_text.indent_ascii_text(ascii_text.center_text(),ascii_text.MAGIC, "PURPLE")
        #print("{}{}{}".format(bcolor.YELLOW, ascii_text.MAGIC, bcolor.ENDC))
        for spell in self.magic:
            print("{}{}: {} cost: {}".format((ascii_text.center_text() - 6)  * " ", i, spell["name"], spell["cost"]))
            #print(str(i) + ":", spell["name"], "(cost:", str(spell["cost"]) +")")
            i += 1
    ###############
    # Status Menu #
    ###############

    def show_status(self, bar_size):
        name_spaces = " " * (bar_size + 16)
        # hp bar configuration
        hp_bar_total = bar_size
        hp_bar_left = round(self.hp / self.max_hp * hp_bar_total)
        hp_bar_spaces = " " * (hp_bar_total - hp_bar_left)
        hp_bar = "█" *  round(self.hp / self.max_hp * hp_bar_total)
        hp_top = " " * (hp_bar_total + 9)
        hp_current = hp_bar + hp_bar_spaces
        hp_value_offset = len(str(self.get_maxhp()))
        hp_title_spaces = " " * ((len(str(self.get_maxhp()).zfill(hp_value_offset))*2)+7)

        # mp bar configuration
        mp_bar_total = 20
        mp_bar_left = round(self.mp / self.max_mp * mp_bar_total)
        mp_bar_spaces = " " * (mp_bar_total - mp_bar_left)
        mp_bar = "█" *  round(self.mp / self.max_mp * mp_bar_total)
        mp_top = " " * (mp_bar_total - 4)
        mp_current = mp_bar + mp_bar_spaces

        print("{}'s k: {} KS: {} Lk: {}{} ".format(self.name, self.statistics["kills"], self.statistics["streaks"], self.luck, name_spaces), end='')
        yield
        print("weapon: {c.BOLD}{}{c.ENDC} dmg: {}{}     ".format(self.weapon["name"], self.weapon["effect"], name_spaces, c=bcolor), end='')
        yield
        print("armor: {c.BOLD}{}{c.ENDC} def: {}{}     ".format(self.armor["name"], self.armor["effect"], name_spaces, c=bcolor), end='')
        yield
        print("{}{c.BOLD}HP{}MP{}{c.ENDC}   ".format(hp_title_spaces, hp_top, mp_top, c=bcolor), end='')
        yield
        print("{c.BOLD}{:04}/{:04}{c.ENDC} |{c.GREEN}{}{c.ENDC}| {c.BOLD}{:03}/{:03}{c.ENDC} |{c.BLUE}{}{c.ENDC}|".format(self.get_hp(), self.get_maxhp(), hp_current, self.get_mp(), self.get_maxmp(), mp_current, c=bcolor), end='')
        yield

