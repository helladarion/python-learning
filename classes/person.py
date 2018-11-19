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
    
    def get_max_mp(self):
      	return self.maxmp

    def show_options(self):
        i = 1
        print("What do you want to do?")
        for act in self.actions:
            #print(str(i) + ". " + act)
            print("{}. {}".format(i, act))
            i += 1
    
    def show_magic(self):
        i = 1
        print("What magic you want to use?")
        for magic in self.magic:
            #print(str(i) + ". " + magic["name"])
            print("{}. {} - cost {}".format(i, magic["name"], magic["cost"]))
            i += 1
            
    def generate_magic_effect(self, magic_id):
        print("You choose the magic {} this is a magic type {} and with the effect {}".format(self.magic[magic_id]["name"],self.magic[magic_id]["type"],self.magic[magic_id]["effect"]))
        self.mp -= self.magic[magic_id]["cost"] 
        if self.magic[magic_id]["type"] == "dark":
          return self.magic[magic_id]["effect"]
        else:
          self.hp += self.magic[magic_id]["effect"]
          if self.hp > self.maxhp:
            self.hp = self.maxhp
          return 0 
        
        
    def generate_damage(self):
        atk_high = self.atk + 10
        atk_low = self.atk - 10
        return random.randrange(atk_low, atk_high)

    def take_damage(self, dmg):
        if self.df > dmg:
        	dmg_taken = 0
        else:
        	dmg_taken = dmg - self.df
          
        self.hp -= dmg_taken

        if self.hp < 0:
        	self.hp = 0

