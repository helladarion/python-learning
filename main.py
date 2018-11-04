import random
from classes.game import utils
from classes.game import bcolor
from classes.person import Person

'''
diceRoller(8)  
diceRoller(6)
diceRoller(12)
diceRoller(20)
'''
# Each initial player have 10 points to use

player = Person('Josemar', 6, 3, 1)
print(player.name)
print("{} appears with {} attack power and he has {} hp, and OMG {} MP".format(player.name, player.atk, player.max_hp, player.max_mp))

enemy = Person('Sauron', 10, 8, 5)
print(enemy.name)
print("{} appears with {} attack power and he has {} hp, and OMG {} MP".format(enemy.name, enemy.atk, enemy.max_hp, enemy.max_mp))




Spell = {
  "cost": 10,
  "dmg": 100,
  "effect": 20
}
print(Spell["effect"])

Magic = [{
  "name": "Fireball",
  "type": "dark",
  "cost": 10,
  "dmg": 100,
  "effect": 20
},{
  "name": "Blizzard",
  "type": "dark",
  "cost": 12,
  "dmg": 130,
  "effect": 30
},{
  'name': 'Hurricane',
  'type': 'dark',
  'cost': 10,
  'dmg': 90,
  'effect': 12
}
]

utils.diceRoller(56)

def listMagic():
  for trick in Magic:
    print("{} costs: {}".format(trick['name'], trick['cost']))

print("{}Rafa{} testing".format(bcolor.ROXO, bcolor.ENDC))  
#print(Magic[1]["dmg"])
spell = 0
print("You attacked the enemy using {} dealing {} damage, and with {} chance to apply extra effect".format( Magic[spell]["name"], Magic[spell]["dmg"], Magic[spell]["effect"]) )


utils.chanceCalculator(Spell["effect"])
listMagic()