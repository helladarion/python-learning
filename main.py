import random
from classes.person import Person
from classes.game import bcolor

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 10, "dmg": 100},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]
player = Person(460, 65, 60, 34, magic)
enemy = Person(1200,65, 45, 25, magic)

running = True

print(bcolor.FAIL + bcolor.BOLD + "AN ENEMY ATTACKS!" + bcolor.ENDC)

while running:
    print("============================")
    player.choose_action()
    choice = input("Chose action:")
    index = int(choice) -1
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for {} points of damage. Enemy HP: {}".format(dmg, enemy.get_hp()))
