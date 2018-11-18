from classes.person import Person

"""
TODO
1. Subtract the df from attack
2. Include magic on enemy
3. Add items
4. Add weapons
5. Colour
6. Better status display

""" 

dark_magic = [{"name": "Fire", "cost": 12, "effect": 120, "type": "dark"},
              {"name": "Thunder", "cost": 10, "effect": 100, "type": "dark"},
              {"name": "Blizzard", "cost": 15, "effect": 150, "type": "dark"}]

white_magic = [{"name": "Healing", "cost": 5, "effect": 20, "type": "white"},
               {"name": "Super Heal", "cost": 10, "effect": 50, "type": "white"}]

player_magic = [ dark_magic[0], dark_magic[2], white_magic[1] ]

player = Person(420, 65, 50, 35, player_magic)
enemy = Person(250, 110, 65, 40, [])

#hero.show_options()

running = True

print("Um inimigo se aproximaaaaa")
while running:
    print("Your HP is {}/{} and your MP is {}/{}".format(player.get_hp(), player.get_max_hp(), player.get_mp(), player.get_max_mp()))
    print("Enemy HP is {}/{}".format(enemy.get_hp(),enemy.get_max_hp()))
    player.show_options()
    choice = input("choose your action: ")
    index = int(choice)
    #print("You choose {}".format(index))
    if index == 1:
        print("You attack the enemy ")
        atk_dmg = player.generate_damage()
        enemy.take_damage(atk_dmg)
        print("You attacked for {} of damage".format(atk_dmg))
    elif index == 2:
        player.show_magic()
        choice_spell = input("Choose your spell")
        spell = int(choice_spell) - 1
        spell_effect = player.generate_magic_effect(spell)
        if spell_effect > 0:
            enemy.take_damage(spell_effect)
            print("You attacked using {} for {} of damage".format(player.magic[spell]["name"], player.magic[spell]["effect"]))
    # Enemy Turn
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("The enemy attacked you and you took {} of damage".format(enemy_dmg))
        