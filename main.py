from classes.person import Person

dark_magic = [{"name": "Fire", "cost": 10, "damage": 100},
              {"name": "Thunder", "cost": 10, "damage": 100},
              {"name": "Blizzard", "cost": 10, "damage": 100}]

hero = Person(420, 65, dark_magic)

hero.show_options()

