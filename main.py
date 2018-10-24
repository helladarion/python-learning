import random
import sys
import os
from time import sleep
from classes.person import Person
from classes.game import bcolor


magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 10, "dmg": 100},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]
player = Person("Jack", 460, 65, 60, 34, magic)
enemy = Person("Magus", 1100, 125, 45, 25, magic)

running = True

print(bcolor.FAIL + bcolor.BOLD + "AN ENEMY ATTACKS!" + bcolor.ENDC)

while running:
    os.system('clear')
    player_status, enemy_status = player.show_status(25), enemy.show_status(40)
    while True:
        try:
            next(player_status)
            print(' ', end='')
            next(enemy_status)
            print()
        except StopIteration:
            break
    print("============================")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) -1
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked {} for {} points of damage.".format(enemy.name, dmg))
        sleep(0.5)

    print("{c.FAIL}{c.BOLD}ENEMY PHASE:{c.ENDC}".format(c=bcolor))
    dmg = enemy.generate_damage()
    player.take_damage(dmg)
    print("{} attacked you for {} points of damage.".format(enemy.name, dmg))
    sleep(1.5)
    """ for i in range(21):
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
        sys.stdout.flush()
        sleep(0.25)"""
