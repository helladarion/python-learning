class Person:
    def __init__(self, hp, mp, magic):
        self.hp = hp
        self.mp = mp
        self.maxhp = hp
        self.maxmp = mp
        self.magic = magic
        self.actions = ["Attack","Magic"]

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def show_options(self):
        i = 1
        print("What do you want to do?")
        for act in self.actions:
            print(str(i) + ". " + act)
            i += 1
