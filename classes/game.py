import random


class bcolor:
  ROXO       = '\033[95m'
  BLUE       = '\033[94m'
  GREEN      = '\033[92m'
  YELLOW     = '\033[93m'
  RED        = '\033[91m'
  ENDC       = '\033[0m'
  BOLD       = '\033[1m'
  UNDERLINE  = '\033[4m'

class utils:
  def diceRoller(dsize):
    roll_result = random.randint(1,dsize)
    return roll_result
  
  def chanceCalculator(real_chance):
    chance = utils.diceRoller(100)
    if chance <= real_chance:
      #print('Lucky day! You got {} chance'.format(chance))
      return True
    else:
      #print('Not today! You got {} chance'.format(chance))
      return False
      

