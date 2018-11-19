import os
from classes.game import bcolor
from time import sleep
from classes.person import Person

"""
TODO
1. Subtract the df from attack - DONE
2. Include magic on enemy
3. Add items
4. Add weapons
5. Colour - DONE
6. Better status display - DONE
7. Add armor
8. Energy bar


""" 

dark_magic = [{"name": "Fire", "cost": 12, "effect": 120, "type": "dark"},
              {"name": "Thunder", "cost": 10, "effect": 100, "type": "dark"},
              {"name": "Blizzard", "cost": 15, "effect": 150, "type": "dark"}]

white_magic = [{"name": "Healing", "cost": 5, "effect": 20, "type": "white"},
               {"name": "Super Heal", "cost": 10, "effect": 50, "type": "white"}]

player_magic = [ dark_magic[0], dark_magic[2], white_magic[1] ]

player = Person(420, 65, 50, 35, player_magic)
enemy = Person(250, 110, 65, 35, [])

#hero.show_options()
def show_battle_status():
  os.system("clear")
  #print("{c.GREEN}{ca}{c.ENDC}".format(c=bcolor, ca = bcolor.ASCII_CODE * 20))
  print("Your HP is {c.GREEN}{c.BOLD}{}/{}{c.ENDC} |{c.GREEN}{ca}{c.ENDC}| MP {c.BLUE}{c.BOLD}{}/{}{c.ENDC} |{c.BLUE}{ca}{c.ENDC}|".format(player.get_hp(), player.get_max_hp(), player.get_mp(), player.get_max_mp(), c=bcolor, ca = bcolor.ASCII_CODE * 20))
  #print("Your MP is {c.BLUE}{c.BOLD}{}/{}{c.ENDC}", player.get_mp(), player.get_max_mp(), c=bcolor))
  print("Enemy HP is {c.GREEN}{c.BOLD}{}/{}{c.ENDC}".format(enemy.get_hp(),enemy.get_max_hp(), c = bcolor))
  player.show_options()
  
  
running = True

print("{c.UNDERLINE}{c.YELLOW}Um inimigo se aproximaaaaa{c.ENDC}".format(c=bcolor))
sleep(2)
while running:
    show_battle_status()
    choice = input("choose your action: ")
    index = int(choice)
    #print("You choose {}".format(index))
    if index == 1:
        print("You attack the enemy ")
        atk_dmg = player.generate_damage()
        enemy.take_damage(atk_dmg)
        if enemy.df > atk_dmg:
          total_dmg = 0
        else:
          total_dmg = atk_dmg - enemy.df  
        print("You attacked for {c.YELLOW}{c.BOLD}{}{c.ENDC} of damage, the enemy defence reduced you damage to {c.YELLOW}{c.BOLD}{}{c.ENDC}".format(atk_dmg, total_dmg, c = bcolor))
        sleep(2)
    elif index == 2:
        player.show_magic()
        choice_spell = input("Choose your spell")
        spell = int(choice_spell) - 1
        spell_effect = player.generate_magic_effect(spell)
        if spell_effect > 0:
            enemy.take_damage(spell_effect)
            print("You attacked using {} for {} of damage".format(player.magic[spell]["name"], player.magic[spell]["effect"]))
            sleep(2)
    # Enemy Turn
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    if player.df > enemy_dmg:
      enemy_total_dmg = 0
    else:
      enemy_total_dmg = enemy_dmg - player.df
    print("The enemy attacked you for {c.PURPLE}{c.BOLD}{}{c.ENDC} of damage, you managed to defend yourself and took {c.PURPLE}{c.BOLD}{}{c.ENDC} of damage".format(enemy_dmg, enemy_total_dmg, c = bcolor))
    sleep(5)