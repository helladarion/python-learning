from classes.person import Person

dark_magic = [{"name": "Fire", "cost": 10, "damage": 100},
              {"name": "Thunder", "cost": 10, "damage": 100},
              {"name": "Blizzard", "cost": 10, "damage": 100}]

player = Person(420, 65, 50, 35, dark_magic)
enemy = Person(250, 110, 65, 40, [])

#hero.show_options()

running = True

print("Um inimigo se aproximaaaaa")
while running:
    player.show_options()
    choice = input("choose your action: ")
    index = int(choice)
    print("You choose {}".format(index))
    if index == 1:
        print("You attack the enemy ")
        atk_dmg = player.generate_damage()
        enemy.take_damage(atk_dmg)
        print("You attacked for {} of damage".format(atk_dmg))
        print("Enemy HP is {}/{}".format(enemy.get_hp(),enemy.get_max_hp()))
        
        
