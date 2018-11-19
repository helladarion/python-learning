import random
import sys
import os
from time import sleep
from classes.person import Person
from classes.game import bcolor
from classes.game import Persistence
from classes.game import ascii_text
from classes.game import Enemy

# Loading assets
def load_assets():
    magic = Persistence.load("magic.json")
    weapons = Persistence.load("weapons.json")
    items = Persistence.load("items.json")
    armors = Persistence.load("armors.json")
    return magic, weapons, items, armors

player = Person("Patric", 4, 6, 5)

POINTS = 15

magic, weapons, items, armors = load_assets()

def gen_enemy(points, luck, difficult):
    ascii_text.indent_ascii_text(ascii_text.center_text(),ascii_text.AN_ENEMY_ATTACKS, "RED")
    sleep(0.5)
    enemy = Person.generate_random_person(Enemy.generate_random_name(), points)
    get_random_gear(enemy,difficult)
    enemy.luck = luck
    return enemy

def get_random_gear(entity, difficult):
    weapon_id = random.randint(0,difficult)
    armor_id = random.randint(0,difficult)
    item_id = random.randint(0,difficult)
    entity.weapon = weapons[weapon_id]
    entity.armor = armors[armor_id]
    entity.items.append(items[item_id])



player.weapon = weapons[0]
player.armor = armors[0]

# Generating the first Enemy
enemy = gen_enemy(POINTS, random.randint(0,3), Enemy.DIFFICULT)

running = True

sleep(2)

def show_header_status():
    # Getting width of the tty screen
    rows, cols = os.popen('stty size', 'r').read().split()
    os.system('clear')
    player_status, enemy_status = player.show_status(25), enemy.show_status(30)
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
            if choice == 98:
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
    # Check if victorious
    if enemy.check_defeat():
        player.add_kill()
        if player.statistics["streaks"] % 5 == 0:
            Enemy.DIFFICULT += 1
            Enemy.LUCK += 3
        ###############
        # Drop chance #
        ###############
        if random.randint(0,100) < player.luck:
            print("{c.BOLD}{c.PURPLE}The Enemy Dropped something{c.ENDC}".format(c=bcolor))
            sleep(2)
            equip = random.randint(1,3)
            if equip == 1:
                player.items.append(enemy.weapon)
            elif equip == 2:
                player.items.append(enemy.armor)
            else:
                player.items.extend(enemy.items)

        del enemy
        enemy = gen_enemy(POINTS, random.randint(0,Enemy.LUCK), Enemy.DIFFICULT)
        continue
    # Enemy Phase
    show_header_status()
    ascii_text.indent_ascii_text(ascii_text.center_text(),ascii_text.ENEMY_PHASE, "RED")
    #print("{c.RED}{c.BOLD}{}{c.ENDC}".format(ascii_text.ENEMY_PHASE,c=bcolor))
    dmg = enemy.generate_damage()
    player.take_damage(dmg)
    print("{} attacked you for {c.BOLD}{}{c.ENDC} points of damage.".format(enemy.name, dmg, c=bcolor))
    sleep(2)
    if player.check_defeat():
        ascii_text.indent_ascii_text(ascii_text.center_text(),ascii_text.DEFEATED, "RED")
        sleep(1)
        player.revive()
        player.hp = player.max_hp
    if player.max_hp < 4:
        print("Game Over")
        break


