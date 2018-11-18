import random
import sys
import os
from time import sleep
from classes.person import Person
from classes.game import bcolor
from classes.game import Persistence
from classes.game import ascii_text

# Loading assets
magic = Persistence.load("magic.json")
weapons = Persistence.load("weapons.json")
items = Persistence.load("items.json")
armors = Persistence.load("armors.json")

player = Person("Patric", 4, 2, 4)
enemy = Person("Magus", 9, 12, 6)

enemy.weapon = weapons[1]
enemy.armor = armors[1]

player.weapon = weapons[0]
player.armor = armors[0]
player.items.append(weapons[3])

running = True

ascii_text.indent_ascii_text(ascii_text.center_text(),ascii_text.AN_ENEMY_ATTACKS, "RED")
sleep(2)

def show_header_status():
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
    print("=" * int(cols))

while running:
    show_header_status()
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked {} for {c.BOLD}{}{c.ENDC} points of damage.".format(enemy.name, dmg, c=bcolor))
        sleep(0.5)
    elif index == 1:
        show_header_status()
        if player.show_inventory():
            choice = int(input("Choose item: ")) - 1
            if choice == 99:
                continue
            else:
                player.use_item(choice)
                continue

        else:
            sleep(0.5)
            continue
    elif index == 2:
        show_header_status()
        if "Magic" in player.actions:
            player.choose_magic()
            choice = input("Choose Spell: ")
            spell_index = int(choice) - 1
            magic_damage = player.generate_magic_damage(spell_index)
            player.reduce_mp(player.magic[spell_index]["cost"])
            enemy.take_damage(magic_damage)
            print("You attacked {} with {} for {c.BOLD}{}{c.ENDC} points of damage.".format(enemy.name, player.magic[spell_index]["name"], magic_damage, c=bcolor))
            sleep(1.0)
        else:
            print("Option not available")
            sleep(0.5)
    # Enemy Phase
    show_header_status()
    ascii_text.indent_ascii_text(ascii_text.center_text(),ascii_text.ENEMY_PHASE, "RED")
    #print("{c.RED}{c.BOLD}{}{c.ENDC}".format(ascii_text.ENEMY_PHASE,c=bcolor))
    dmg = enemy.generate_damage()
    player.take_damage(dmg)
    print("{} attacked you for {c.BOLD}{}{c.ENDC} points of damage.".format(enemy.name, dmg, c=bcolor))
    sleep(2)

    #Persistence.savedata("magic.json", magic)




    print("Saving the hp from player")
    """ for i in range(21):
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
        sys.stdout.flush()
        sleep(0.25)"""

