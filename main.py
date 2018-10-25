import random
import sys
import os
from time import sleep
from classes.person import Person
from classes.game import bcolor
from classes.game import Save

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 10, "dmg": 100},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]
player = Person("Patric", 560, 65, 60, 34, magic)
enemy = Person("Magus", 1100, 125, 45, 25, magic)

running = True

print(bcolor.FAIL + bcolor.BOLD + "AN ENEMY ATTACKS!" + bcolor.ENDC)

while running:
    # Getting width of the tty screen
    rows, cols = os.popen('stty size', 'r').read().split()
    os.system('clear')
    player_status, enemy_status = player.show_status(25), enemy.show_status(40)
    cols_left = int(cols) - (25 + 40 + 9 ) - 80
    space_between_status = " " * cols_left

    while True:
        try:
            next(player_status)
            print(space_between_status, end='')
            next(enemy_status)
            print()
        except StopIteration:
            break
    print("============================ rows " + rows + " Cols: " + cols + " Cols Left: " + str(cols_left))
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked {} for {} points of damage.".format(enemy.name, dmg))
        sleep(0.5)
    elif index == 1:
        player.choose_magic()
        choice = input("Choose Spell:")
        spell_index = int(choice) - 1
        magic_damage = player.generate_magic_damage(spell_index)
        enemy.take_damage(magic_damage)
        print("You attacked {} with {} for {} points of damage.".format(enemy.name, player.magic[spell_index]["name"], magic_damage))
        sleep(1.0)

    print("{c.FAIL}{c.BOLD}ENEMY PHASE:{c.ENDC}".format(c=bcolor))
    dmg = enemy.generate_damage()
    player.take_damage(dmg)
    print("{} attacked you for {} points of damage.".format(enemy.name, dmg))
    sleep(1.5)
    Save.savedata(player.name, player.get_hp())




    print("Saving the hp from player")
    """ for i in range(21):
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
        sys.stdout.flush()
        sleep(0.25)"""
